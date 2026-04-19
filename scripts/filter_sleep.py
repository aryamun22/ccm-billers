#!/usr/bin/env python3
"""Filter Medicare Provider-and-Service to Sleep Medicine specialty on target CPTs,
aggregate per NPI, and emit ranked practice list for outreach.

Target CPTs:
  95810  - Polysomnography (PSG), age 6+, 4+ parameters, attended
  95811  - PSG with CPAP/BiPAP titration
  95806  - Sleep study, unattended (respiratory analysis)
  G0399  - Home sleep test (HSAT) with Type III portable monitor
  95782  - PSG under 6 years old
  95783  - PSG under 6 with titration
  99490  - CCM 20 min non-complex
  99439  - CCM add-on
  99491  - CCM 30 min by physician/QHP
  99437  - CCM add-on to 99491
  99487  - Complex CCM 60 min
  99489  - Complex CCM add-on
  99453  - RPM device setup/education
  99454  - RPM device supply, each 30 days
  99457  - RPM treatment mgmt 20 min
  99458  - RPM treatment mgmt add-on 20 min
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

CODES = {
    "95810": {"cat": "PSG",  "label": "PSG attended (age 6+)"},
    "95811": {"cat": "PSG",  "label": "PSG with CPAP/BiPAP titration"},
    "95806": {"cat": "HSAT", "label": "Unattended sleep study (respiratory)"},
    "G0399": {"cat": "HSAT", "label": "Home sleep test (Type III)"},
    "95782": {"cat": "PSG",  "label": "PSG pediatric <6"},
    "95783": {"cat": "PSG",  "label": "PSG pediatric <6 with titration"},
    "99490": {"cat": "CCM",  "label": "CCM 20 min (staff time)"},
    "99439": {"cat": "CCM",  "label": "CCM add-on"},
    "99491": {"cat": "CCM",  "label": "CCM 30 min (physician)"},
    "99437": {"cat": "CCM",  "label": "CCM add-on (99491)"},
    "99487": {"cat": "CCM",  "label": "Complex CCM 60 min"},
    "99489": {"cat": "CCM",  "label": "Complex CCM add-on"},
    "99453": {"cat": "RPM",  "label": "RPM setup/education"},
    "99454": {"cat": "RPM",  "label": "RPM device supply (30d)"},
    "99457": {"cat": "RPM",  "label": "RPM mgmt 20 min"},
    "99458": {"cat": "RPM",  "label": "RPM mgmt add-on 20 min"},
}

SRC = Path.home() / "Data" / "MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv"
OUT = Path.home() / "Repos" / "ccm-billers" / "web" / "sleep.json"


def main():
    by_npi = defaultdict(lambda: {
        "npi": "", "name": "", "org": "", "city": "", "state": "", "zip": "",
        "rural": "", "services": 0, "benes": 0, "total_payment": 0.0,
        "codes": {}, "cats": {"PSG": 0, "HSAT": 0, "CCM": 0, "RPM": 0},
        "cats_pay": {"PSG": 0.0, "HSAT": 0.0, "CCM": 0.0, "RPM": 0.0},
    })

    scanned = kept = 0
    with SRC.open(newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            scanned += 1
            if scanned % 2_000_000 == 0:
                print(f"  scanned {scanned:,}, kept {kept:,}", file=sys.stderr)
            if (row.get("Rndrng_Prvdr_Type") or "") != "Sleep Medicine":
                continue
            code = (row.get("HCPCS_Cd") or "").strip()
            if code not in CODES:
                continue
            try:
                svc = float(row.get("Tot_Srvcs") or 0)
                avg_pay = float(row.get("Avg_Mdcr_Pymt_Amt") or 0)
                benes = int(float(row.get("Tot_Benes") or 0))
            except ValueError:
                continue
            total_pay = svc * avg_pay
            kept += 1
            npi = (row.get("Rndrng_NPI") or "").strip()
            ent = (row.get("Rndrng_Prvdr_Ent_Cd") or "").strip()
            last_or_org = (row.get("Rndrng_Prvdr_Last_Org_Name") or "").strip()
            first = (row.get("Rndrng_Prvdr_First_Name") or "").strip()
            is_org = ent == "O"

            rec = by_npi[npi]
            rec["npi"] = npi
            rec["name"] = "" if is_org else f"{first} {last_or_org}".strip()
            rec["org"] = last_or_org if is_org else ""
            rec["city"] = (row.get("Rndrng_Prvdr_City") or "").strip()
            rec["state"] = (row.get("Rndrng_Prvdr_State_Abrvtn") or "").strip()
            rec["zip"] = (row.get("Rndrng_Prvdr_Zip5") or "").strip()
            rec["rural"] = (row.get("Rndrng_Prvdr_RUCA_Desc") or "").strip()
            rec["services"] += int(svc)
            rec["benes"] = max(rec["benes"], benes)
            rec["total_payment"] += total_pay
            rec["codes"][code] = rec["codes"].get(code, 0) + int(svc)
            cat = CODES[code]["cat"]
            rec["cats"][cat] += int(svc)
            rec["cats_pay"][cat] += total_pay

    providers = list(by_npi.values())
    for p in providers:
        p["total_payment"] = round(p["total_payment"], 2)
        for k in p["cats_pay"]:
            p["cats_pay"][k] = round(p["cats_pay"][k], 2)
    providers.sort(key=lambda p: p["total_payment"], reverse=True)

    # Practice proxy: aggregate by (state, zip) since individual file lacks org name
    practice = defaultdict(lambda: {
        "zip": "", "state": "", "city": "",
        "providers": 0, "services": 0, "benes": 0, "total_payment": 0.0,
        "cats": {"PSG": 0, "HSAT": 0, "CCM": 0, "RPM": 0},
        "names": [],
    })
    for p in providers:
        key = f"{p['state']}|{p['zip']}"
        g = practice[key]
        g["zip"] = p["zip"]
        g["state"] = p["state"]
        g["city"] = p["city"]
        g["providers"] += 1
        g["services"] += p["services"]
        g["benes"] += p["benes"]
        g["total_payment"] += p["total_payment"]
        for k, v in p["cats"].items():
            g["cats"][k] += v
        if len(g["names"]) < 8:
            g["names"].append(p["name"] or p["org"])
    practices = list(practice.values())
    for g in practices:
        g["total_payment"] = round(g["total_payment"], 2)
    practices.sort(key=lambda g: g["total_payment"], reverse=True)

    # Totals
    state_tot = defaultdict(lambda: {"payment": 0.0, "services": 0, "providers": 0})
    code_tot = defaultdict(lambda: {"services": 0, "payment": 0.0})
    cat_tot = {"PSG": 0.0, "HSAT": 0.0, "CCM": 0.0, "RPM": 0.0}
    for p in providers:
        state_tot[p["state"]]["payment"] += p["total_payment"]
        state_tot[p["state"]]["services"] += p["services"]
        state_tot[p["state"]]["providers"] += 1
        for c, n in p["codes"].items():
            code_tot[c]["services"] += n
        for k, v in p["cats_pay"].items():
            cat_tot[k] += v

    by_state = [{"state": k, **v, "payment": round(v["payment"], 2)} for k, v in state_tot.items()]
    by_state.sort(key=lambda x: x["payment"], reverse=True)

    by_code = [{"code": c, "label": CODES[c]["label"], "cat": CODES[c]["cat"], **v}
               for c, v in code_tot.items()]
    by_code.sort(key=lambda x: x["services"], reverse=True)

    payload = {
        "source": "CMS Medicare Physician & Other Practitioners — by Provider and Service (2023), Sleep Medicine specialty",
        "codes": CODES,
        "providers": providers,
        "practices": practices,
        "by_state": by_state,
        "by_code": by_code,
        "by_category": {k: round(v, 2) for k, v in cat_tot.items()},
        "totals": {
            "rows_scanned": scanned,
            "kept_rows": kept,
            "providers": len(providers),
            "practices": len(practices),
            "total_payment": round(sum(p["total_payment"] for p in providers), 2),
            "total_services": sum(p["services"] for p in providers),
        },
    }

    with OUT.open("w") as f:
        json.dump(payload, f)
    print(f"wrote {OUT} ({OUT.stat().st_size/1e6:.1f} MB)", file=sys.stderr)
    t = payload["totals"]
    print(f"  {t['providers']:,} NPIs, {t['practices']:,} ZIP-level practices, ${t['total_payment']:,.0f} Medicare", file=sys.stderr)


if __name__ == "__main__":
    main()
