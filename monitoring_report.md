# CMS Data Monitor Report

**Run date/time:** 2026-09-29 10:00:00 UTC  
**Status:** ERROR — Network egress blocked (recurring)

---

## Task 1: CMS Provider-and-Service Data (2024 Release Check)
- **Source:** https://data.cms.gov/data.json
- **Result:** BLOCKED — Network egress proxy blocked access to `data.cms.gov`
- **Action:** Cannot check for 2024 Medicare Physician & Other Practitioners data. Run manually or whitelist domain.

---

## Task 2: AASM Scoring Manual / Guideline Updates
- **Source:** https://aasm.org/clinical-resources/practice-standards/
- **Result:** BLOCKED — Network egress proxy blocked access to `aasm.org`
- **Action:** Check manually at https://aasm.org/clinical-resources/practice-standards/ for 2026 publications.

---

## Task 3: CMS Federal Register — Sleep Apnea Rules (2026)
- **Source:** https://www.federalregister.gov/api/v1/documents (CMS, sleep apnea, ≥2026-01-01)
- **Result:** BLOCKED — Network egress proxy blocked access to `www.federalregister.gov`
- **Action:** Check manually at https://www.federalregister.gov for CMS sleep apnea proposed/final rules.

---

## Task 4: MPFS Updates — Sleep/CCM CPT Codes
- **Source:** https://www.federalregister.gov/api/v1/documents (CMS, physician fee schedule, ≥2026-01-01)
- **CPT codes monitored:** 95810, 95811, 95806, G0399, 99490, 99439, 99487, 99491, 99453, 99454, 99457
- **Result:** BLOCKED — Network egress proxy blocked access to `www.federalregister.gov`
- **Action:** Check manually for 2027 MPFS proposed rule or 2026 MPFS corrections.

---

## Summary

| Task | Status |
|------|--------|
| CMS 2024 data release | BLOCKED |
| AASM guideline updates | BLOCKED |
| Federal Register — sleep apnea rules | BLOCKED |
| MPFS CPT code updates | BLOCKED |

**Root cause:** The remote execution environment's network egress proxy is blocking all four required external domains (`data.cms.gov`, `aasm.org`, `www.federalregister.gov`). This has persisted since at least 2026-09-28.

**Recommended action:** Whitelist these domains in the environment's network policy, or run this monitor from an environment with unrestricted HTTPS egress. See https://code.claude.com/docs/en/claude-code-on-the-web for environment configuration.
