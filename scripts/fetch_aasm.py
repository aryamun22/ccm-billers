#!/usr/bin/env python3
"""Pull AASM sleep center directory for all 50 states via the real API.

Endpoint reverse-engineered from sleepeducation.org/wp-content/js/FindASleepCenterV2.js:
  https://api.aasm.org/v1/FindASleepCenter/FindAHealthcareCenter?SearchQuery=State|<StateName>
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

STATES = [
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
    "Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa",
    "Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan",
    "Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire",
    "New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
    "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
    "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia",
    "Wisconsin","Wyoming","District of Columbia",
]

OUT = Path.home() / "Repos" / "ccm-billers" / "web" / "aasm.json"


def fetch(state):
    url = "https://api.aasm.org/v1/FindASleepCenter/FindAHealthcareCenter?SearchQuery=" + \
          urllib.parse.quote(f"State|{state}", safe="|")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def clean(c):
    # strip embedded jsCode / HTML garbage from every string field
    out = {}
    for k, v in c.items():
        if k == "jsCode":
            continue
        if isinstance(v, str):
            v = re.sub(r"\s+", " ", v).strip()
        out[k] = v
    return out


def main():
    all_centers = []
    seen = set()
    for st in STATES:
        try:
            data = fetch(st)
        except Exception as e:
            print(f"  {st}: ERROR {e}", file=sys.stderr)
            continue
        rows = data.get("myHealthcareAddressResults", []) or []
        kept = 0
        for c in rows:
            c = clean(c)
            key = (c.get("SleepProgramName", ""), c.get("Street1", ""), c.get("Zip", ""))
            if key in seen:
                continue
            seen.add(key)
            all_centers.append({
                "name": c.get("SleepProgramName", ""),
                "street": " ".join(x for x in [c.get("Street1",""), c.get("Street2","")] if x),
                "city": c.get("City", ""),
                "state": c.get("State", ""),
                "zip": (c.get("Zip", "") or "")[:5],
                "phone": c.get("Phone", ""),
                "fax": c.get("Fax", ""),
                "email": c.get("EmailAddress", ""),
                "website": c.get("Website", ""),
                "is_member": c.get("OrganizationType") == "1" or c.get("isMemberCenter") == "1",
                "lat": c.get("Lat", ""),
                "lng": c.get("Long", ""),
            })
            kept += 1
        print(f"  {st}: {kept} centers", file=sys.stderr)
        time.sleep(0.2)  # be polite
    payload = {
        "source": "AASM Accredited Facility Directory (sleepeducation.org)",
        "fetched": time.strftime("%Y-%m-%d"),
        "centers": all_centers,
        "count": len(all_centers),
    }
    OUT.write_text(json.dumps(payload))
    print(f"wrote {OUT} ({OUT.stat().st_size/1e6:.1f} MB, {len(all_centers)} centers)", file=sys.stderr)


if __name__ == "__main__":
    main()
