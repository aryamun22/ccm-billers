# CMS Data Monitoring Report

**Run date/time:** 2026-10-10 (automated daily run)

**Status: NO NEW CHANGES DETECTED — NETWORK ACCESS BLOCKED (4th consecutive day)**

---

## Network Access

All external domains blocked by egress policy (proxy returns 403 on CONNECT tunnel):
- data.cms.gov
- aasm.org
- www.federalregister.gov

No new data could be fetched. Findings below carry forward from the 2026-10-07 run (first successful fetch).

---

## Outstanding Action Items (from 2026-10-07)

| Priority | Action | Status |
|----------|--------|--------|
| **HIGH** | Download 2024 Provider & Service data from CMS portal and run `filter_ccm.py` | ⏳ Pending |
| **HIGH** | Review CY 2027 MPFS proposed rule for new sleep codes 95X18/19/20 replacing 95800/95801 — update code mapping | ⏳ Pending |
| **MEDIUM** | Review CCM code RVU changes (GACP1/GACP2, 0591T/0592T crosswalks) for billing impact | ⏳ Pending |
| **LOW** | Verify AASM guidelines directly at aasm.org when egress access is available | ⏳ Pending |

---

## Task Results

### Task 1: CMS Medicare Provider & Service Data
No new fetch possible. Last known state (2026-10-07): **2024 data released** on CMS portal.
- Dataset: https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service

### Task 2: AASM Scoring Manual / Practice Guidelines
No new fetch possible. Last known state: No confirmed 2026 updates; Version 3 remains current.

### Task 3: Federal Register — Sleep Apnea Rules (2026+)
No new fetch possible. Last known state: CY 2027 MPFS Proposed Rule (doc 2026-14327, published 2026-07-16) contains new unattended sleep study codes (95X18/19/20).

### Task 4: MPFS Updates — Sleep / CCM Codes
No new fetch possible. Last known state: CY 2027 proposed rule has CPT replacements for 95800/95801 and CCM crosswalk codes (GACP1/GACP2).

---

*Network has been blocked for 4 consecutive days (2026-10-07 through 2026-10-10). Action items from 2026-10-07 remain unaddressed. To restore monitoring, unblock egress to data.cms.gov, aasm.org, and www.federalregister.gov, or run checks locally. See commit `721ecaa` for full 2026-10-07 findings.*
