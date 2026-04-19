#!/usr/bin/env python3
"""Join AASM sleep center directory with Medicare sleep-medicine billing data.

Inputs (already produced by filter_sleep.py and fetch_aasm.py):
  ~/Repos/ccm-billers/web/sleep.json
  ~/Repos/ccm-billers/web/aasm.json

Output:
  ~/Repos/ccm-billers/web/outreach.json  — unified practice-level outreach list
"""
import json
from collections import defaultdict
from pathlib import Path

WEB = Path.home() / "Repos" / "ccm-billers" / "web"

sleep = json.loads((WEB / "sleep.json").read_text())
aasm = json.loads((WEB / "aasm.json").read_text())

# Group AASM centers by (state, zip) so we can join on Medicare ZIP buckets
aasm_by_zip = defaultdict(list)
for c in aasm["centers"]:
    if c["zip"]:
        aasm_by_zip[(c["state"], c["zip"])].append(c)

# Build unified records. Anchor on the ZIP-level Medicare practice, attach matched AASM facilities.
unified = []
matched_zips = set()
for p in sleep["practices"]:
    key = (p["state"], p["zip"])
    aasm_matches = aasm_by_zip.get(key, [])
    if aasm_matches:
        matched_zips.add(key)
    unified.append({
        "city": p["city"],
        "state": p["state"],
        "zip": p["zip"],
        "medicare_providers": p["providers"],
        "medicare_services": p["services"],
        "medicare_benes": p["benes"],
        "medicare_payment": p["total_payment"],
        "mix": p["cats"],
        "clinicians": p["names"],
        "aasm_centers": [
            {
                "name": c["name"],
                "street": c["street"],
                "phone": c["phone"],
                "website": c["website"],
                "email": c["email"],
                "is_member": c["is_member"],
            }
            for c in aasm_matches
        ],
        "aasm_matched": len(aasm_matches) > 0,
    })

# AASM centers with NO Medicare sleep-specialty match (different ZIP) — append as secondary targets
# (they exist but didn't bill enough sleep CPTs under Sleep Medicine specialty in 2023)
unified.sort(key=lambda r: r["medicare_payment"], reverse=True)

# Coverage stats
total_practices = len(sleep["practices"])
matched = sum(1 for p in unified if p["aasm_matched"])

payload = {
    "source": "Join of CMS Medicare Provider+Service (2023, Sleep Medicine) × AASM Accredited Facility Directory",
    "unified": unified,
    "stats": {
        "medicare_zip_practices": total_practices,
        "aasm_centers_total": aasm["count"],
        "matched_zips": matched,
        "match_rate": round(100 * matched / max(1, total_practices), 1),
    },
}
(WEB / "outreach.json").write_text(json.dumps(payload))
print(f"wrote web/outreach.json — {total_practices} Medicare ZIPs, {matched} matched to ≥1 AASM center ({payload['stats']['match_rate']}%)")

# Preview top 25
print("\nTOP 25 UNIFIED OUTREACH TARGETS (by Medicare $):")
for i, r in enumerate(unified[:25], 1):
    tag = f"[{len(r['aasm_centers'])} AASM]" if r["aasm_centers"] else "[no AASM match]"
    name = r["aasm_centers"][0]["name"] if r["aasm_centers"] else "(no AASM center)"
    phone = r["aasm_centers"][0]["phone"] if r["aasm_centers"] else ""
    print(f" {i:>2}. {r['city']},{r['state']} {r['zip']:<6} ${r['medicare_payment']:>9,.0f}  {tag}  {name}  {phone}")
