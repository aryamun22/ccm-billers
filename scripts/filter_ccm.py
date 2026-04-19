#!/usr/bin/env python3
"""Filter the CMS Provider-and-Service CSV to CCM HCPCS codes and emit JSON for the web UI.

Input:  ~/Data/MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv  (~2 GB, 2023 data)
Output: ~/Repos/ccm-billers/web/data.json
"""
import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

CCM_CODES = {
    "99490": "CCM 20 min/month (non-complex, staff time)",
    "99439": "CCM each additional 20 min (add-on to 99490)",
    "99487": "Complex CCM first 60 min",
    "99489": "Complex CCM each additional 30 min",
    "99491": "CCM 30 min/month (physician/QHP personally)",
    "99437": "CCM each additional 30 min (add-on to 99491)",
    "G0506": "Comprehensive assessment for CCM",
}

TARGET_SPECIALTIES = {
    "Sleep Medicine",
    "Otolaryngology",
    "Oral Surgery",
    "Endocrinology",
    "Internal Medicine",
    "Family Practice",
    "Geriatric Medicine",
    "Nurse Practitioner",
    "Physician Assistant",
    "Cardiology",
    "Nephrology",
    "Pulmonary Disease",
    "Neurology",
    "Rheumatology",
}

SRC = Path.home() / "Data" / "MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv"
OUT = Path.home() / "Repos" / "ccm-billers" / "web" / "data.json"


def main():
    if not SRC.exists():
        sys.exit(f"Missing input: {SRC}")

    rows = []
    specialty_totals = defaultdict(lambda: {"services": 0, "payment": 0.0, "providers": set()})
    code_totals = defaultdict(lambda: {"services": 0, "payment": 0.0, "providers": set()})

    with SRC.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        # Column names vary slightly by year — pick by prefix
        def col(prefix):
            for c in fields:
                if c.lower().startswith(prefix.lower()):
                    return c
            return None

        c_code = col("HCPCS_Cd") or col("HCPCS Cd") or col("HCPCS_CD")
        c_npi = col("Rndrng_NPI") or col("NPI")
        c_last = col("Rndrng_Prvdr_Last")  # Rndrng_Prvdr_Last_Org_Name — doubles as org when Ent_Cd=O
        c_first = col("Rndrng_Prvdr_First")
        c_ent = col("Rndrng_Prvdr_Ent_Cd")
        c_org = c_last  # same field; disambiguated below by Ent_Cd
        c_city = col("Rndrng_Prvdr_City")
        c_state = col("Rndrng_Prvdr_State_Abrvtn") or col("Rndrng_Prvdr_State")
        c_spec = col("Rndrng_Prvdr_Type")
        c_svc_cnt = col("Tot_Srvcs")
        c_benes = col("Tot_Benes")
        c_pay = col("Avg_Mdcr_Pymt_Amt")
        c_submitted = col("Avg_Sbmtd_Chrg")

        if not c_code:
            sys.exit(f"Could not find HCPCS code column. Fields: {fields[:10]}")

        scanned = 0
        for row in reader:
            scanned += 1
            if scanned % 1_000_000 == 0:
                print(f"  scanned {scanned:,} rows, kept {len(rows):,}", file=sys.stderr)
            code = (row.get(c_code) or "").strip()
            if code not in CCM_CODES:
                continue
            try:
                svc = float(row.get(c_svc_cnt) or 0)
                avg_pay = float(row.get(c_pay) or 0)
            except ValueError:
                continue
            total_pay = svc * avg_pay
            specialty = (row.get(c_spec) or "").strip() if c_spec else ""
            npi = (row.get(c_npi) or "").strip() if c_npi else ""

            ent = (row.get(c_ent) or "").strip() if c_ent else ""
            last_or_org = (row.get(c_last) or "").strip() if c_last else ""
            is_org = ent == "O"
            rec = {
                "npi": npi,
                "last": "" if is_org else last_or_org,
                "first": "" if is_org else ((row.get(c_first) or "").strip() if c_first else ""),
                "org": last_or_org if is_org else "",
                "city": (row.get(c_city) or "").strip() if c_city else "",
                "state": (row.get(c_state) or "").strip() if c_state else "",
                "specialty": specialty,
                "code": code,
                "services": int(svc),
                "benes": int(float(row.get(c_benes) or 0)) if c_benes else 0,
                "avg_payment": round(avg_pay, 2),
                "total_payment": round(total_pay, 2),
            }
            rows.append(rec)

            st = specialty_totals[specialty]
            st["services"] += rec["services"]
            st["payment"] += total_pay
            st["providers"].add(npi)

            ct = code_totals[code]
            ct["services"] += rec["services"]
            ct["payment"] += total_pay
            ct["providers"].add(npi)

    print(f"scanned {scanned:,} total rows, kept {len(rows):,} CCM rows", file=sys.stderr)

    # Aggregate per NPI across all CCM codes for the ranked table
    by_npi = defaultdict(lambda: {
        "npi": "", "name": "", "org": "", "city": "", "state": "", "specialty": "",
        "services": 0, "benes": 0, "total_payment": 0.0, "codes": {},
    })
    for r in rows:
        key = r["npi"]
        agg = by_npi[key]
        agg["npi"] = r["npi"]
        agg["name"] = f"{r['first']} {r['last']}".strip()
        agg["org"] = r["org"]
        agg["city"] = r["city"]
        agg["state"] = r["state"]
        agg["specialty"] = r["specialty"]
        agg["services"] += r["services"]
        agg["benes"] = max(agg["benes"], r["benes"])
        agg["total_payment"] += r["total_payment"]
        agg["codes"][r["code"]] = agg["codes"].get(r["code"], 0) + r["services"]

    providers = list(by_npi.values())
    for p in providers:
        p["total_payment"] = round(p["total_payment"], 2)
    providers.sort(key=lambda p: p["total_payment"], reverse=True)

    def finalize_totals(d):
        out = []
        for k, v in d.items():
            out.append({
                "name": k or "(Unknown)",
                "services": v["services"],
                "payment": round(v["payment"], 2),
                "providers": len(v["providers"]),
            })
        out.sort(key=lambda x: x["payment"], reverse=True)
        return out

    payload = {
        "source": "CMS Medicare Physician & Other Practitioners — by Provider and Service (2023)",
        "ccm_codes": CCM_CODES,
        "target_specialties": sorted(TARGET_SPECIALTIES),
        "providers": providers,
        "by_specialty": finalize_totals(specialty_totals),
        "by_code": finalize_totals(code_totals),
        "totals": {
            "rows_scanned": scanned,
            "ccm_rows": len(rows),
            "providers": len(providers),
            "total_payment": round(sum(p["total_payment"] for p in providers), 2),
            "total_services": sum(p["services"] for p in providers),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as f:
        json.dump(payload, f)
    print(f"wrote {OUT} ({OUT.stat().st_size/1e6:.1f} MB)", file=sys.stderr)
    print(f"  providers: {len(providers):,}  total Medicare payment: ${payload['totals']['total_payment']:,.0f}", file=sys.stderr)


if __name__ == "__main__":
    main()
