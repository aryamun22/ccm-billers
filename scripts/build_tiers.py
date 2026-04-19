#!/usr/bin/env python3
"""Rescan CMS Provider-and-Service for ALL clinicians billing sleep CPTs (not just
those self-registered as 'Sleep Medicine'), so academic Pulmonology/Neurology sleep
physicians at MGH/Brigham/BIDMC/Tufts/BU actually surface.

Then tier:
  Tier 1  — Northeast (MA/NH/VT/ME/RI/CT/NY/NJ/PA) + Boston-area academic ZIPs, top by charges
  Tier 2  — National top 50 by Medicare $ (sleep + pulm + neuro on sleep CPTs)
  Tier 3  — Everyone else

Join with AASM directory by ZIP, and emit:
  web/tiers.json            — for the website
  web/outreach_tier1.csv    — Google-Sheet-ready
  web/outreach_tier2.csv
  web/outreach_tracker.csv  — full tracker with status columns for the 30-day sprint
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

SRC = Path.home() / "Data" / "MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv"
WEB = Path.home() / "Repos" / "ccm-billers" / "web"

# Sleep CPT / HCPCS universe — billing behavior is the signal, not the specialty label
SLEEP_CODES = {
    "95810": "PSG",
    "95811": "PSG",
    "95806": "HSAT",
    "95782": "PSG",
    "95783": "PSG",
    "G0399": "HSAT",
    "99490": "CCM",
    "99439": "CCM",
    "99491": "CCM",
    "99487": "CCM",
    "99489": "CCM",
    "99437": "CCM",
    "99453": "RPM",
    "99454": "RPM",
    "99457": "RPM",
    "99458": "RPM",
}

# Specialties that actually do sleep medicine, named as CMS types them
ALLOWED_SPECS = {
    "Sleep Medicine",
    "Pulmonary Disease",
    "Neurology",
    "Internal Medicine",
    "Family Practice",
    "Otolaryngology",
    "Nurse Practitioner",
    "Physician Assistant",
    "Psychiatry",
    "Pediatrics",
}

NE_STATES = {"MA","NH","VT","ME","RI","CT","NY","NJ","PA"}

# Boston academic ZIPs — MGH, Brigham, BIDMC, Tufts, BU, Boston Children's, BMC, Mt Auburn, Lahey, Cambridge Health
BOSTON_ACADEMIC_ZIPS = {
    "02114",  # MGH main
    "02115",  # Longwood — Brigham, BIDMC, Boston Children's
    "02215",  # BIDMC / BU Medical
    "02118",  # Boston Medical Center
    "02111",  # Tufts Medical Center
    "02139",  # Cambridge (CHA)
    "02138",  # Cambridge
    "02140",  # Mt Auburn / North Cambridge
    "02141",  # East Cambridge
    "02142",  # Kendall
    "02143",  # Somerville
    "02144",  # Somerville
    "02145",  # Somerville
    "02446",  # Brookline
    "02445",  # Brookline
    "02138",  # Cambridge
    "01805",  # Lahey Burlington
    "01803",  # Lahey Burlington
    "02135",  # Brighton / St Elizabeth's
    "02215",  # BU
}


def main():
    by_npi = defaultdict(lambda: {
        "npi": "", "name": "", "org": "", "specialty": "",
        "city": "", "state": "", "zip": "",
        "services": 0, "benes": 0, "total_payment": 0.0,  # SLEEP-CPT dollars only
        "cats": {"PSG": 0, "HSAT": 0, "CCM": 0, "RPM": 0},
        "cats_pay": {"PSG": 0.0, "HSAT": 0.0, "CCM": 0.0, "RPM": 0.0},
    })

    scanned = kept = 0
    with SRC.open(newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            scanned += 1
            if scanned % 2_000_000 == 0:
                print(f"  scanned {scanned:,}, kept NPIs {len(by_npi):,}", file=sys.stderr)
            code = (row.get("HCPCS_Cd") or "").strip()
            if code not in SLEEP_CODES:
                continue
            spec = (row.get("Rndrng_Prvdr_Type") or "").strip()
            if spec not in ALLOWED_SPECS:
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
            rec["specialty"] = spec
            rec["city"] = (row.get("Rndrng_Prvdr_City") or "").strip()
            rec["state"] = (row.get("Rndrng_Prvdr_State_Abrvtn") or "").strip()
            rec["zip"] = (row.get("Rndrng_Prvdr_Zip5") or "").strip()
            rec["services"] += int(svc)
            rec["benes"] = max(rec["benes"], benes)
            cat = SLEEP_CODES[code]
            rec["cats"][cat] += int(svc)
            rec["cats_pay"][cat] += total_pay
            # Only PSG + HSAT count toward the ranking dollars — CCM/RPM are upsell, not anchor volume
            if cat in ("PSG", "HSAT"):
                rec["total_payment"] += total_pay

    # GATE: an NPI only qualifies as a sleep practice if it billed ≥1 actual sleep CPT
    # (PSG or HSAT). CCM and RPM codes are generic and would otherwise pull in Brooklyn
    # chronic-care billing mills that have nothing to do with sleep medicine.
    before = len(by_npi)
    providers = [p for p in by_npi.values() if (p["cats"]["PSG"] + p["cats"]["HSAT"]) > 0]
    for p in providers:
        p["total_payment"] = round(p["total_payment"], 2)
    providers.sort(key=lambda p: p["total_payment"], reverse=True)
    print(f"scanned {scanned:,}, kept {kept:,} rows; {before:,} NPIs touched any sleep code, "
          f"{len(providers):,} billed ≥1 PSG/HSAT (sleep-gated)", file=sys.stderr)

    # ZIP-level practice aggregation
    prac = defaultdict(lambda: {
        "city": "", "state": "", "zip": "",
        "npis": 0, "services": 0, "benes": 0, "total_payment": 0.0,
        "specialties": defaultdict(int),
        "cats": {"PSG": 0, "HSAT": 0, "CCM": 0, "RPM": 0},
        "names": [],
        "top_npis": [],  # for tracker rows
    })
    for p in providers:
        key = f"{p['state']}|{p['zip']}"
        g = prac[key]
        g["city"] = p["city"]
        g["state"] = p["state"]
        g["zip"] = p["zip"]
        g["npis"] += 1
        g["services"] += p["services"]
        g["benes"] += p["benes"]
        g["total_payment"] += p["total_payment"]
        g["specialties"][p["specialty"]] += 1
        for k, v in p["cats"].items():
            g["cats"][k] += v
        name = p["name"] or p["org"]
        if name and len(g["names"]) < 10:
            g["names"].append(name)
        g["top_npis"].append(p)
    practices = list(prac.values())
    for g in practices:
        g["total_payment"] = round(g["total_payment"], 2)
        g["specialties"] = dict(g["specialties"])
        g["top_npis"].sort(key=lambda x: -x["total_payment"])
        g["top_npis"] = g["top_npis"][:5]
    practices.sort(key=lambda g: g["total_payment"], reverse=True)

    # Attach AASM
    aasm = json.loads((WEB / "aasm.json").read_text())
    aasm_by_zip = defaultdict(list)
    for c in aasm["centers"]:
        if c["zip"]:
            aasm_by_zip[(c["state"], c["zip"])].append(c)
    for g in practices:
        g["aasm_centers"] = aasm_by_zip.get((g["state"], g["zip"]), [])

    # Tiering
    top50 = set(id(g) for g in practices[:50])
    for rank, g in enumerate(practices, 1):
        ne = g["state"] in NE_STATES
        boston_academic = g["state"] == "MA" and g["zip"] in BOSTON_ACADEMIC_ZIPS
        if ne or boston_academic:
            g["tier"] = 1
        elif id(g) in top50:
            g["tier"] = 2
        else:
            g["tier"] = 3
        g["rank"] = rank

    tier1 = [g for g in practices if g["tier"] == 1]
    tier2 = [g for g in practices if g["tier"] == 2]
    tier3 = [g for g in practices if g["tier"] == 3]

    # Rank tier 1 by charges; cap at top 25 to match the 10-15 quota with headroom
    tier1.sort(key=lambda g: -g["total_payment"])
    tier1_top = tier1[:25]

    # Emit JSON for the website
    payload = {
        "source": "CMS Provider+Service 2023 × AASM directory — tiered for 30-day outreach sprint",
        "counts": {
            "total_npis": len(providers),
            "total_practices": len(practices),
            "tier1": len(tier1),
            "tier2": len(tier2),
            "tier3": len(tier3),
        },
        "tier1": tier1_top,
        "tier2": tier2,
        "tier3_preview": tier3[:100],
    }
    (WEB / "tiers.json").write_text(json.dumps(payload))
    print(f"\nwrote web/tiers.json ({(WEB/'tiers.json').stat().st_size/1e6:.1f} MB)")
    print(f"  tier1: {len(tier1)} practices ({len(tier1_top)} in top slice)")
    print(f"  tier2: {len(tier2)}")
    print(f"  tier3: {len(tier3)}")

    # CSV writers
    def write_tier_csv(path, rows, label):
        with path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["tier","rank","city","state","zip","medicare_$","npis","services","benes",
                        "psg","hsat","ccm","rpm","top_clinicians","top_specialty",
                        "aasm_center","aasm_street","aasm_phone","aasm_website","aasm_member",
                        "linkedin_search","google_search","gsheet_status","assigned_date","contacted","response","zoom_booked"])
            for r in rows:
                center = r["aasm_centers"][0] if r["aasm_centers"] else {}
                top_spec = max(r["specialties"].items(), key=lambda kv: kv[1])[0] if r["specialties"] else ""
                top_clin = "; ".join(r["names"][:5])
                li_q = "+".join((r["names"][0] or "").split() + [r["city"], "sleep"])
                g_q = "+".join(((center.get("name") or r["names"][0] or "sleep center") + " " + r["city"] + " " + r["state"]).split())
                w.writerow([
                    label, r["rank"], r["city"], r["state"], r["zip"], f'{r["total_payment"]:.0f}',
                    r["npis"], r["services"], r["benes"],
                    r["cats"]["PSG"], r["cats"]["HSAT"], r["cats"]["CCM"], r["cats"]["RPM"],
                    top_clin, top_spec,
                    center.get("name", ""), center.get("street", ""), center.get("phone", ""),
                    center.get("website", ""), "yes" if center.get("is_member") else "no",
                    f"https://www.linkedin.com/search/results/people/?keywords={li_q}",
                    f"https://www.google.com/search?q={g_q}",
                    "NEW", "", "", "", "",
                ])
        print(f"  wrote {path.name}: {len(rows)} rows")

    write_tier_csv(WEB / "outreach_tier1.csv", tier1_top, "T1")
    write_tier_csv(WEB / "outreach_tier2.csv", tier2, "T2")

    # Unified tracker: T1 (top 25) + T2 (top 50), deduped
    seen = set()
    combined = []
    for r in tier1_top + tier2:
        key = (r["state"], r["zip"])
        if key in seen:
            continue
        seen.add(key)
        combined.append(r)
    write_tier_csv(WEB / "outreach_tracker.csv", combined, "")

    print(f"\nDONE. Open web/outreach_tracker.csv in Google Sheets to start the 30-day machine.")


if __name__ == "__main__":
    main()
