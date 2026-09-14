# CMS Data Monitor Report

**Run date/time:** 2026-09-14 10:04:58 UTC

---

## Task 1: CMS Provider-and-Service Data (Medicare Physician & Other Practitioners)

**Status: BLOCKED — network egress proxy denied access to `data.cms.gov`**

- Current latest in repo: 2023-12-31
- Could not check for 2024 release
- **Action item:** Run manually: `curl "https://data.cms.gov/data.json" | python3 -c "import json,sys; [print(json.dumps(ds,indent=2)) for ds in json.load(sys.stdin).get('dataset',[]) if 'by Provider and Service' in ds.get('title','')]"` — if a 2024 distribution exists, run `filter_ccm.py` to update.

---

## Task 2: AASM Scoring Manual / Practice Parameters

**Status: BLOCKED — network egress proxy denied access to `aasm.org`**

- Could not check for 2026 updates
- **Action item:** Visit https://aasm.org/clinical-resources/practice-standards/ manually and check for 2026-dated documents.

---

## Task 3: CMS Federal Register — Sleep Apnea Rules (2026)

**Status: BLOCKED — network egress proxy denied access to `www.federalregister.gov`**

- Could not query for CMS sleep apnea proposed/final rules published ≥ 2026-01-01
- **Action item:** Check manually: https://www.federalregister.gov/agencies/centers-for-medicare-medicaid-services (filter by date and keyword "sleep apnea")

---

## Task 4: MPFS Updates — Sleep/CCM CPT Codes

**Status: BLOCKED — network egress proxy denied access to `www.federalregister.gov`**

- CPT codes of interest: 95810, 95811, 95806, G0399 (sleep studies); 99490, 99439, 99487, 99491 (CCM); 99453, 99454, 99457 (RPM)
- CY 2027 MPFS Proposed Rule is typically published in July — check for it at https://www.federalregister.gov/agencies/centers-for-medicare-medicaid-services
- **Action item:** Search Federal Register manually for "physician fee schedule 2027" to confirm if the proposed rule is out.

---

## Summary

| Task | Result |
|------|--------|
| CMS Provider-and-Service 2024 data | ❌ Egress blocked |
| AASM guideline updates 2026 | ❌ Egress blocked |
| Federal Register sleep apnea rules 2026 | ❌ Egress blocked |
| MPFS CPT code updates | ❌ Egress blocked |

**Root cause:** The scheduled monitoring environment's network egress proxy blocks all four target domains (`data.cms.gov`, `aasm.org`, `www.federalregister.gov`). No data comparisons were possible.

**Recommended fix:** Either (a) configure the proxy allowlist to permit these domains, or (b) run the monitoring script locally where internet access is unrestricted. See `/root/.ccr/README.md` for proxy configuration.
