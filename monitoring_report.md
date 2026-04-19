# CMS Data Monitor Report

**Date/Time:** 2026-04-19 (automated daily check)
**Status:** FETCH ERRORS — outbound network access blocked (HTTP 403 on all sources)

---

## Task 1: CMS Medicare Physician & Other Practitioners — by Provider and Service

- **Source:** https://data.cms.gov/data.json
- **Result:** FETCH ERROR (HTTP 403)
- **Current baseline:** 2023 data (released 2023-12-31)
- **Action:** Manual check required — visit https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service to verify if 2024 data has been released.

---

## Task 2: AASM Scoring Manual / Practice Parameter Updates (2026)

- **Source:** https://aasm.org/clinical-resources/practice-standards/
- **Result:** FETCH ERROR (HTTP 403)
- **Action:** Manual check required — visit AASM clinical resources page to review for new scoring manual versions or practice parameter updates published in 2026.

---

## Task 3: CMS Federal Register — Sleep Apnea Rules (2026-01-01 onward)

- **Source:** https://www.federalregister.gov (CMS agency, term: "sleep apnea", date ≥ 2026-01-01)
- **Result:** FETCH ERROR (HTTP 403)
- **Action:** Manual check required — search Federal Register at https://www.federalregister.gov/documents/search for CMS documents mentioning "sleep apnea" published in 2026.

---

## Task 4: MPFS Updates — Sleep & CCM CPT Codes

- **CPT codes monitored:** 95810, 95811, 95806, G0399, 99490, 99439, 99487, 99491, 99453, 99454, 99457
- **Source:** Federal Register (CMS, "physician fee schedule", date ≥ 2026-01-01)
- **Result:** FETCH ERROR (HTTP 403)
- **Action:** Manual check required — search for 2027 MPFS proposed rule or 2026 MPFS corrections at https://www.federalregister.gov.

---

## Summary

| Task | Status |
|------|--------|
| CMS Provider/Service 2024 data | ERROR — fetch blocked |
| AASM guideline updates (2026) | ERROR — fetch blocked |
| Federal Register sleep apnea rules | ERROR — fetch blocked |
| MPFS sleep/CCM code updates | ERROR — fetch blocked |

**No changes detected** (checks could not complete due to network restrictions).

**Recommended fix:** Run this monitor from an environment with outbound HTTPS access, or configure network egress rules to allow requests to `data.cms.gov`, `aasm.org`, and `federalregister.gov`.
