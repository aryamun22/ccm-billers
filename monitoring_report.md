# CMS Data Monitoring Report

**Run date/time:** 2026-10-07 10:02 UTC

---

## Task 1: CMS Medicare Physician & Other Practitioners — by Provider and Service

**STATUS: NEW DATA AVAILABLE ⚠️**

2024 service year data has been released on CMS data portal.

- **Dataset page:** https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service
- **Created:** May 11, 2026 | **Last updated:** May 21, 2026
- **Rows:** 1,296,739 | **Columns:** 81
- Prior latest in repo: 2023

**ACTION REQUIRED:** Download the 2024 Public Use File (CSV) from the dataset page and run `filter_ccm.py` to update the project data.

> Note: Direct CSV download URL not captured (egress proxy blocked data.cms.gov). Retrieve from the dataset page above.

---

## Task 2: AASM Scoring Manual / Practice Guidelines

**STATUS: No confirmed 2026 updates**

- Current scoring manual is **Version 3** — no new version release found for 2025–2026.
- Search did not surface any new practice parameters or guideline documents published in 2026.
- Recommend manually checking https://aasm.org/clinical-resources/practice-standards/ if network access is restored.

---

## Task 3: CMS Federal Register — Sleep Apnea Proposed/Final Rules (2026+)

**STATUS: TWO RELEVANT RULES FOUND ⚠️**

### CY 2026 MPFS Final Rule
- **Published:** November 5, 2025 | Doc: 2025-19787
- **URL:** https://www.federalregister.gov/documents/2025/11/05/2025-19787/medicare-and-medicaid-programs-cy-2026-payment-policies-under-the-physician-fee-schedule-and-other
- Effective January 1, 2026.

### CY 2027 MPFS Proposed Rule
- **Published:** July 16, 2026 | Doc: 2026-14327
- **URL:** https://www.federalregister.gov/documents/2026/07/16/2026-14327/medicare-and-medicaid-programs-cy-2027-payment-policies-under-the-physician-fee-schedule-and-other
- **Comment period closed:** September 14, 2026.
- **Key sleep apnea provisions:** New unattended sleep study CPT codes proposed (95X18, 95X19, 95X20) to replace existing codes 95800/95801, with RUC-recommended direct PE inputs. CMS not proposing refinement of these RUC recommendations.

---

## Task 4: MPFS Updates Affecting Sleep / CCM Codes

**STATUS: SIGNIFICANT CHANGES IN CY 2027 PROPOSED RULE ⚠️**

Source: CY 2027 MPFS Proposed Rule (doc 2026-14327, https://public-inspection.federalregister.gov/2026-14327.pdf)

### Sleep CPT Codes
- CPT **95800 / 95801** (unattended sleep study) are being **replaced** with new codes:
  - **95X18** — Unattended sleep study, low complexity (3–4 channels, ≥3–5 parameter categories)
  - **95X19** — Unattended sleep study, moderate complexity (5–10 channels)
  - **95X20** — (additional related code)
- CMS proposing RUC-recommended PE inputs without refinement.
- No changes to **95810 / 95811** (polysomnography) referenced in this rule.

### CCM Codes
- **99490 / 99439** referenced as crosswalk targets for new visit-based codes:
  - **0591T / 0592T** crosswalked to **99490 / 99439** respectively (under general supervision)
  - New HCPCS **GACP1**: work RVU = 1.00 (crosswalk to 99490)
  - New HCPCS **GACP2**: work RVU = 0.70 (crosswalk to 99439)
- Codes **99487, 99491, 99453, 99454, 99457, G0399** — no specific changes found in this pass.

---

## Summary of Action Items

| Priority | Action |
|----------|--------|
| **HIGH** | Download 2024 Provider & Service data from CMS portal and run `filter_ccm.py` |
| **HIGH** | Review CY 2027 MPFS proposed rule for new sleep codes 95X18/19/20 replacing 95800/95801 — update code mapping in project |
| **MEDIUM** | Review CCM code RVU changes (GACP1/GACP2, 0591T/0592T crosswalks) for billing impact |
| **LOW** | Verify AASM guidelines directly at aasm.org when egress access is available |

---

*Note: data.cms.gov, aasm.org, and federalregister.gov were blocked by egress proxy (403). Data collected via web search index. Download URLs may need to be retrieved manually.*
