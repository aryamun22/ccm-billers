# CMS Data Monitoring Report

**Generated:** 2026-09-30  
**Monitoring interval:** Daily

---

## Task 1: CMS Medicare Physician & Other Practitioners — by Provider and Service

**Status: NEW DATA AVAILABLE**

A 2024 dataset (labeled `2024-12-01`) is now published and was last updated **May 21, 2026**. This is newer than the current dataset we have (2023-12-31).

- **CMS Data Portal:** https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service  
- **Data.gov Catalog:** https://catalog.data.gov/dataset/medicare-physician-other-practitioners-by-provider-and-service-2024-12-01  
- **Contact:** ipag_data_products@cms.hhs.gov  

> **ACTION ITEM:** New 2024 data is available. Run `filter_ccm.py` to download and process the updated dataset.

Note: Direct file size could not be retrieved (data.cms.gov domain blocked by egress proxy in this environment). Download manually or via VPN to confirm size before processing.

---

## Task 2: AASM Scoring Manual / Practice Standards Updates

**Status: NO NEW RELEASE FOUND**

AASM Scoring Manual **Version 3 (2023)** remains the current major version. No new 2025 or 2026 version of the scoring manual was announced. The manual is updated annually online; no new practice parameter documents published in 2026 were identified in this check.

- Scoring manual page: https://aasm.org/clinical-resources/scoring-manual/

> **No action required.** Re-check periodically; direct access to aasm.org is blocked in this environment so full page scraping was not possible.

---

## Task 3: CMS Federal Register — Sleep Apnea Rules (2026)

**Status: ONE NEW DEVICE CLASSIFICATION RULE**

One relevant 2026 Federal Register document found:

| Date | Type | Title | FR Doc |
|------|------|-------|--------|
| 2026-04-22 | Final Rule | Medical Devices; Anesthesiology Devices; Classification of the Device for Sleep Apnea Testing Based on Mandibular Movement | 2026-07862 |

- URL: https://www.federalregister.gov/documents/2026/04/22/2026-07862/medical-devices-anesthesiology-devices-classification-of-the-device-for-sleep-apnea-testing-based-on

This is an FDA device classification rule (mandibular movement-based sleep apnea testing device), **not** a CMS payment rule. No CMS-specific proposed or final rules on sleep apnea payment/coverage were found for 2026.

> **No billing action required** from this rule.

---

## Task 4: MPFS Updates — Sleep & CCM Codes

**Status: CRITICAL CHANGE IN 2027 MPFS PROPOSED RULE**

CMS released the **CY 2027 Medicare Physician Fee Schedule Proposed Rule** on **July 14, 2026**.

### Sleep Testing Codes — Breaking Change (Effective Jan 1, 2027 if finalized)

| Action | Codes |
|--------|-------|
| **DELETED** | 95800, 95801, **95806** |
| **NEW (replacement)** | 95X18, 95X19, 95X20, 95X21, 95X22, 95X23 (6 new codes) |

**CPT 95806** (one of our monitored codes) is proposed for deletion. The 6 new codes (95X18–95X23) replace the entire unattended HSAT family and are designed to capture different complexity levels and broader sleep disorder types.

- AASM analysis: https://aasm.org/cms-releases-2027-physician-fee-schedule-proposed-rule-key-takeaways-for-sleep-medicine/
- CMS fact sheet: https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule
- AASM submitted formal comments (September 2026): https://aasm.org/wp-content/uploads/2026/09/AASM-PFS-Proposed-Rule-Comments-Final.pdf

### CCM Codes (99490, 99439, 99487, 99491, 99453, 99454, 99457)

No specific changes to CCM or RPM codes were identified in this check. The conversion factor is proposed to decrease from $33.5675 → $33.1693 (APM) and $33.4009 → $32.8409 (non-APM), which will reduce reimbursement modestly across all codes.

> **ACTION ITEM:** Review the 2027 MPFS proposed rule impact on 95806. If finalized, `filter_ccm.py` and any downstream billing logic referencing 95806 will need to be updated to map to the new 95X18–95X23 codes effective Jan 1, 2027. Comment period closed September 14, 2026; final rule expected November 2026.

---

## Summary of Action Items

| Priority | Item |
|----------|------|
| **HIGH** | Download and process 2024 CMS Provider & Service data — run `filter_ccm.py` |
| **HIGH** | Review 2027 MPFS impact on CPT 95806 deletion; plan code mapping to 95X18–95X23 |
| Low | Monitor AASM site for any 2026 scoring manual updates (direct access blocked) |
