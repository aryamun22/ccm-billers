# CMS Data Monitor Report

**Last successful run:** 2026-05-16  
**Latest run:** 2026-05-16T00:00:00Z — **NO NEW FINDINGS** (WebSearch partial success; findings confirmed unchanged from 2026-05-06)  
**Checked by:** CMS Data Monitor (automated)  
**Baseline:** Provider-and-Service data newest distribution = 2023-12-31

> **Network note:** data.cms.gov, aasm.org, and federalregister.gov still return 403 on direct fetch. This run used WebSearch to retrieve substantive findings. URLs cannot be download-verified.

---

## Task 1 — CMS Provider-and-Service 2024 Data Release

**Status: NO NEW DISTRIBUTION CONFIRMED**

- catalog.data.gov shows latest resource still dated **2023-12-31** (same as baseline)
- A CY2024 distribution (covering claims year 2024, release year 2026) would be expected May–June 2026 — **not yet detected**
- A methodology document dated May 30, 2024 (`MUP_PHY_RY24`) exists; that covers CY2022 data, not 2024

> **Action item (open):** CY2024 data release likely imminent — **we are now in the expected May–June 2026 release window.** Manually check the dataset page weekly:  
> https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service  
> When a 2024-12-31 distribution appears, download and run `filter_ccm.py`.

---

## Task 2 — AASM Scoring Manual / Guideline Updates

**Status: NEW GUIDELINES CONFIRMED (2025–2026)**

AASM Scoring Manual remains at **Version 3 (2023)** — no new version released.

Two new clinical practice guidelines confirmed published in 2025, hosted on aasm.org as of Feb 2026:

| Document | Published | Notes |
|---|---|---|
| Treatment of Central Sleep Apnea in Adults | Dec 2025 (JCSM Vol. 21 No. 12) | Updates 2012/2016 practice parameters; adds transvenous phrenic nerve stimulation |
| Evaluation and Management of Obstructive Sleep Apnea in Adults (Inpatient) | 2025 | New inpatient setting guideline |

> **Action item:** Review both guidelines for documentation requirements that may affect 95810/95811 ordering, CPAP/BiPAP titration justification, and HSAT eligibility criteria under G0399.

---

## Task 3 — Federal Register: Sleep Apnea Rules (CMS, 2026)

**Status: NO NEW CMS SLEEP APNEA RULES — FDA DEVICE RULE NOTED**

- **No new CMS proposed or final rules** specifically addressing sleep apnea published in 2026
- **FDA Rule (not CMS):** Classification of sleep apnea testing device (mandibular movement-based) → Class II special controls, effective **April 22, 2026** (FR 2026-07862). Not a billing change; affects device manufacturers.
- VA proposed sleep apnea rating changes are a separate, non-CMS rulemaking

> No billing action required. Monitor for 2027 MPFS proposed rule (~July 2026) which may include sleep apnea coverage changes.

---

## Task 4 — MPFS Updates: Sleep & CCM Codes

**Status: CRITICAL FINDING — CODE DELETIONS AND RATE CHANGES CONFIRMED**

**CY2026 MPFS Final Rule (CMS-1832-F), effective Jan 1, 2026:**

### ⚠️ CRITICAL: Home Sleep Test Code Deletions (Jan 1, 2027)

| Code | Description | Status |
|---|---|---|
| **95800** | Unattended sleep study, min 4 channels | **DELETED 1/1/2027** |
| **95801** | Unattended sleep study, min 4 channels, oximetry | **DELETED 1/1/2027** |
| **95806** | Home sleep test (HST), 4+ parameters | **DELETED 1/1/2027** |

Replacement codes are under development by the AMA CPT Editorial Panel. New codes take effect Jan 1, 2027. **Transition planning must begin now.**

### Sleep Testing Rate Changes (CY2026)

| Code | Change | Notes |
|---|---|---|
| 95810 (in-facility) | ~−7% indirect PE | Hospital-owned labs see reduction |
| 95810 (non-facility) | ~+4% indirect PE | Independent sleep centers benefit |
| 95811 (in-facility) | ~−7% indirect PE | Same as 95810 |
| 95811 (non-facility) | ~+4% indirect PE | |
| All sleep/PAP codes | −2.5% overall | CY2026 conversion factor reduction |
| Telehealth / virtual supervision | ✓ Permanent | Benefits HSAT oversight via APPs |

Conversion factors: **$33.40** (non-APM) / **$33.57** (APM qualifying) — ~3–4% increase from CY2025.

### CCM / RPM Code Rate Changes (CY2026)

| Code | CY2025 Rate | CY2026 Rate | Change |
|---|---|---|---|
| 99490 (CCM, 20 min) | $60.49/mo | $66.30/mo | **+9.6%** |
| 99439 (CCM add-on, 20 min) | $45.93/mo | $50.56/mo | **+10.1%** |
| 99457 (RPM, first 20 min) | ~$50/mo | ~$52/mo | ~+4% |
| 99453, 99454 (RPM setup/device) | (prior rates) | Updated 2026 | See CCNHealth analysis |

### 2027 MPFS Proposed Rule

- **Not yet released.** Expected ~July 2026. Monitor cms.gov for CMS-1833-P.

> **Action items:**
> 1. **URGENT — 95806/95800/95801:** Begin transition to replacement codes before Jan 1, 2027. Contact AASM coding resources for new code numbers once released by AMA.
> 2. **CCM billing:** Update fee schedules for 99490 (+9.6%) and 99439 (+10.1%) if not already done.
> 3. **Facility vs. non-facility 95810/95811:** Audit setting-of-service flags; facility practices should model impact of −7% indirect PE.
> 4. **Watch for CY2027 proposed rule** (July 2026) — may affect CCM/RPM codes and sleep coverage policy.

---

## Run History

| Date | Result |
|---|---|
| 2026-05-16 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-15 | All fetches blocked (403 / Host not in allowlist) — no new findings; prior findings carried forward |
| 2026-05-09 | All fetches blocked (403 / Host not in allowlist) — no new findings; prior findings carried forward |
| 2026-05-07 | All fetches blocked (403 / Host not in allowlist) — no new findings; prior findings carried forward |
| 2026-05-06 | WebSearch partial success — new findings: AASM guidelines confirmed, 95800/95806/95801 deletion 1/1/2027 confirmed, CCM rate increases confirmed |
| 2026-05-04 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-28 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-26 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-24 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-22 | All fetches blocked (403 / ECONNREFUSED) — no new findings |
| 2026-04-21 | All fetches blocked (403) — findings carried from 2026-04-20 |
| 2026-04-20 | Partial success — baseline findings |

---

## Summary

| Task | Finding | Action Required |
|---|---|---|
| CMS 2024 Provider-Service data | No new distribution confirmed; CY2024 expected May–June 2026 | Yes — check weekly |
| AASM guidelines | 2 new 2025 guidelines (CSA treatment + inpatient OSA) | Yes — review for documentation impact |
| Federal Register sleep rules | No new CMS rules; FDA device classification (non-billing) | No |
| MPFS — code deletions | **95800, 95801, 95806 deleted Jan 1, 2027** | **URGENT — begin transition** |
| MPFS — rate changes | CCM up ~10%; sleep codes −2.5%; facility labs −7% indirect PE | Yes — update fee schedules |
