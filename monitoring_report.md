# CMS Data Monitor Report

**Generated:** 2026-04-20  
**Checked by:** CMS Data Monitor (automated)  
**Baseline:** Provider-and-Service data newest distribution = 2023-12-31

---

## Task 1 — CMS Provider-and-Service 2024 Data Release

**Status: POSSIBLE NEW DATA — Needs manual confirmation**

The `catalog.data.gov` entry for *Medicare Physician & Other Practitioners - by Provider and Service* shows a `last_modified` date of **2025-10-28**, suggesting a release after our 2023-12-31 baseline.

- Dataset page: https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service
- Data.gov catalog: https://catalog.data.gov/dataset/medicare-physician-other-practitioners-by-provider-and-service-b156e

**Direct download URL and file size could not be confirmed via automated fetch** (data.cms.gov returns 403 to automated requests). The CY2024 service-year file (covering 2024 claims) would follow the RY26 naming convention.

> **Action item:** Manually visit the dataset page above or run `python filter_ccm.py --check-latest` to confirm whether a distribution newer than 2023-12-31 exists. If yes, download and run `filter_ccm.py` to update local data.

---

## Task 2 — AASM Scoring Manual / Guideline Updates

**Status: NEW GUIDELINES FOUND (2025, published Feb 2026)**

The AASM Scoring Manual remains at **Version 3** (no new version of the scoring manual itself).

Two new **clinical practice guidelines** were posted to aasm.org in **February 2026**:

| Document | Published | URL |
|---|---|---|
| Treatment of Central Sleep Apnea in Adults (2025 guideline) | Feb 2026 | https://aasm.org/wp-content/uploads/2026/02/central-sleep-apnea-guideline-AASM-2025.pdf |
| Evaluation & Management of Obstructive Sleep Apnea in Adults — Inpatient (2025 guideline) | Feb 2026 | https://aasm.org/wp-content/uploads/2026/02/inpatient-sleep-apnea-guideline-AASM-2025.pdf |

> **Action item:** Review both guidelines for any diagnostic criteria or coding implications affecting billed services (95810, 95811, 95806, G0399). Update clinical documentation templates if criteria have changed.

---

## Task 3 — Federal Register: Sleep Apnea Rules (CMS, 2026)

**Status: NO NEW DEDICATED SLEEP APNEA RULES IN 2026**

No CMS proposed or final rules specifically targeting sleep apnea were published in the Federal Register on or after 2026-01-01.

Sleep apnea coding (CPT **95800** — unattended home sleep test) was addressed in the **CY 2026 MPFS Final Rule** (published Nov 2025, effective Jan 1 2026) and a subsequent correction notice — see Task 4 below.

---

## Task 4 — MPFS Updates: Sleep & CCM Codes

**Status: ACTIONABLE CHANGES EFFECTIVE 2026-01-01**

### CY 2026 MPFS Final Rule (CMS-1832-F)
- **Federal Register:** https://www.federalregister.gov/documents/2025/11/05/2025-19787/medicare-and-medicaid-programs-cy-2026-payment-policies-under-the-physician-fee-schedule-and-other
- **CMS Fact Sheet:** https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-medicare-physician-fee-schedule-final-rule-cms-1832-f

#### Sleep codes
| Code | Change |
|---|---|
| **95800** | PE inputs revised: reusable device equipment codes removed; new supply code added for **WatchPAT ONE disposable** device. Direct PE costs updated accordingly. |

#### RPM / CCM codes
| Code | Change |
|---|---|
| **99457 / 99458** | Time threshold for initial RPM month lowered from **20 minutes** to **11–20 minutes**. This may increase qualifying encounters. |
| CCM (99490, 99439, 99487, 99491) | No direct payment changes noted; however, new **Advanced Primary Care Management (APCM)** add-on G-codes were finalized for behavioral health integration — review whether your CCM workflow interacts with APCM billing. |
| **99453 / 99454** (RPM setup/device supply) | No specific changes found in search results; verify against full rule text. |

### CY 2026 MPFS Correction
- **Federal Register:** https://www.federalregister.gov/documents/2025/08/14/2025-15492/medicare-and-medicaid-programs-cy-2026-payment-policies-under-the-physician-fee-schedule-and-other
- Corrects typographical/technical errors from the July 2025 proposed rule; includes CPT 95800 WatchPAT ONE nominator language.

### CY 2027 MPFS Proposed Rule
- **Not yet released.** Expected ~July 2026 per CMS annual schedule. No CY 2027 proposed rule documents found as of this report date.

> **Action items:**
> 1. Confirm 95800 PE input change does not affect billing or reimbursement amounts for your facility's HSAT workflow.
> 2. Review 99457 time threshold change — encounters previously just under 20 min may now qualify; audit recent RPM claims.
> 3. Monitor federalregister.gov in July 2026 for CY 2027 MPFS proposed rule.

---

## Summary

| Task | Finding | Action Required |
|---|---|---|
| CMS 2024 Provider-Service data | Likely released Oct 2025 — confirm manually | Yes — verify & run filter_ccm.py |
| AASM guidelines | 2 new guidelines (CSA + inpatient OSA, Feb 2026) | Yes — review for coding/documentation impact |
| Federal Register sleep rules 2026 | None found | No |
| MPFS sleep/CCM codes | 95800 PE inputs changed; 99457 time threshold lowered | Yes — audit 99457 claims; confirm 95800 impact |
