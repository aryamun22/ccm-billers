# CMS Data Monitor Report

**Run date/time:** 2026-09-09 (automated scheduled run)  
**Status:** BLOCKED — network egress policy prevents external HTTP access (recurring issue since 2026-09-08)

---

## Task 1: CMS Medicare Physician & Other Practitioners — by Provider and Service
- **Result:** BLOCKED  
- `data.cms.gov` is blocked by the environment's network egress proxy  
- Cannot determine whether a 2024 distribution is available  
- **Last known state (2026-09-06):** CY2024 (RY26) D24_Prov_Svc dataset was confirmed released  
- **Action:** Run `filter_ccm.py` from a machine with unrestricted outbound access to pull the 2024 data

## Task 2: AASM Practice Standards / Scoring Manual Updates
- **Result:** BLOCKED  
- `aasm.org` is blocked by the environment's network egress proxy  
- **Action:** Check manually at https://aasm.org/clinical-resources/practice-standards/ for any 2026 updates

## Task 3: Federal Register — CMS Sleep Apnea Rules (2026+)
- **Result:** BLOCKED  
- `www.federalregister.gov` is blocked by the environment's network egress proxy  
- **Action:** Query manually: https://www.federalregister.gov/documents/search?conditions[agencies][]=centers-for-medicare-medicaid-services&conditions[term]=sleep+apnea&conditions[publication_date][gte]=2026-01-01

## Task 4: MPFS Updates (CPT: 95810, 95811, 95806, G0399, 99490, 99439, 99487, 99491, 99453, 99454, 99457)
- **Result:** BLOCKED  
- `www.federalregister.gov` is blocked (same proxy restriction as Task 3)  
- **Last known state (2026-09-05):** CY2027 MPFS proposed rule included RPM/RTM overhaul  
- **Action:** Check for any corrections or final rules at https://www.federalregister.gov/documents/search?conditions[agencies][]=centers-for-medicare-medicaid-services&conditions[term]=physician+fee+schedule&conditions[publication_date][gte]=2026-01-01

---

## Summary
All monitoring checks have been blocked by network egress restrictions for 2 consecutive days (2026-09-08 and 2026-09-09). The last successful run with new findings was 2026-09-06 (CY2024 dataset) and 2026-09-05 (MPFS rule).

**Fix required:** Update the Claude Code remote environment to allow egress to:
- `data.cms.gov`
- `www.federalregister.gov`
- `aasm.org`

See environment network policy docs: https://code.claude.com/docs/en/claude-code-on-the-web
