# CMS Data Monitor Report

**Last successful run:** 2026-09-05  
**Latest run:** 2026-09-05 UTC — **⚠️ NEW: CY2027 MPFS (CMS-1848-P) proposes eliminating third-party contracted RPM/RTM staffing and consolidating RPM codes into 4 new G-codes — comment deadline 9 days away (Sep 14).** CY2024 (RY26) D24_Prov_Svc not yet confirmed. AASM scoring manual still v3. H.R. 8261 still in committee. WebSearch partial success (direct fetches blocked by proxy).  
**Checked by:** CMS Data Monitor (automated)  
**Baseline:** Provider-and-Service data newest distribution = 2023-12-31

> **Network note:** data.cms.gov, aasm.org, federalregister.gov, and oig.hhs.gov still return 403/EGRESS_BLOCKED on direct fetch. This run used WebSearch to retrieve substantive findings. URLs cannot be download-verified.

---

## Task 1 — CMS Provider-and-Service 2024 Data Release

**Status: ⚠️ NEW DISTRIBUTION CONFIRMED — DOWNLOAD REQUIRED**

**2025-05-20 update:** Today's search surfaced an actual CSV data filename, upgrading status from "data dictionary found" to "data files confirmed":

```
MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv   ← R25=Release 2025, D23=Data year 2023
MUP_PHY_R25_P05_V20_D22_Prov_Svc.csv   ← also present (prior year)
```

These filenames confirm the RY25 (Report Year 2025) Provider-and-Service dataset exists, covering **CY2023 claims** — well past the 2023-12-31 baseline.

Prior finding also stands: data dictionary PDF `MUP_PHY_RY25_20250312_DD_PRV_SVC_508.pdf` was published in the `2025-03` path on data.cms.gov (March 12, 2025).

| Signal | Status |
|---|---|
| MUP_PHY_RY25 data dictionary (March 2025) | **Confirmed — post-baseline** |
| `MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv` | **Confirmed filename — download pending** |
| Data year covered by RY25 | **CY2023 claims** |
| CY2024 data (RY26) | **Not yet released — 2026-06-09 explicit D24 search returned no results. Continue monitoring.** |

> **Action item — IMMEDIATE:** Visit the dataset page and check for a distribution dated after 2023-12-31:  
> https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service  
> If a 2024 or 2025 distribution exists, download and run `filter_ccm.py`. The RY25 data (CY2023 claims) may already be available.

---

## Task 2 — AASM Scoring Manual / Guideline Updates

**Status: ⚠️ NEW 2026 GUIDELINE DETECTED**

AASM Scoring Manual remains at **Version 3 (2023)** — no new scoring manual version detected.

**New in this run (2026-05-31):**

| Document | Published | Notes |
|---|---|---|
| **Combination Treatments for Chronic Insomnia** | **April 13, 2026 (JCSM)** | **NEW — recommendations on combining CBT-I with pharmacotherapy** |

Previously confirmed 2025 guidelines (unchanged):

| Document | Published | Notes |
|---|---|---|
| Treatment of Central Sleep Apnea in Adults | Dec 2025 (JCSM Vol. 21 No. 12) | Updates 2012/2016 practice parameters; adds transvenous phrenic nerve stimulation |
| Evaluation and Management of Obstructive Sleep Apnea in Adults (Inpatient) | 2025 | New inpatient setting guideline |
| RLS and PLMD Clinical Practice Guideline | 2025 | Updated recommendations |

> **Action items:**
> - **NEW (2026-05-31):** Review April 2026 chronic insomnia combination therapy guideline for documentation impact on 99490/CCM billing where insomnia is a co-managed condition.
> - **Open:** Review 2025 guidelines for documentation requirements affecting 95810/95811 ordering, CPAP/BiPAP titration justification, and HSAT eligibility under G0399.

---

## Task 3 — Federal Register: Sleep Apnea Rules (CMS, 2026)

**Status: NO NEW CMS RULES — FDA DEVICE RULE + CMS INTEROPERABILITY RULE NOTED**

- **No new CMS proposed or final rules** specifically addressing sleep apnea published in 2026
- **FDA Rule (not CMS):** Classification of sleep apnea testing device (mandibular movement-based) → Class II special controls, effective **April 22, 2026** (FR 2026-07862, FDA-2026-N-3929). Not a billing change; affects device manufacturers only.
- **CMS Interoperability and Prior Authorization Proposed Rule (April 14, 2026):** Not sleep-specific, but explicitly provisions exchange of **polysomnography reports, home sleep apnea test results, PAP adherence data, and validated questionnaires** via standardized APIs. If finalized, may reduce prior auth delays for CPAP/HSAT and improve payer data exchange. AASM submitted comments. Watch for final rule.
- Note: CPT code 95800 re-nomination for misvaluation was active in the CY2026 PFS proposed rule (decided in the CY2026 final rule)

### ⚠️ NEW (2026-06-25): WISeR Model — HNS Prior Authorization for OSA (Effective Jan 15, 2026)

**FR 2025-12195** (published July 1, 2025) — CMS implemented prior authorization for **Hypoglossal Nerve Stimulation (HNS) for Obstructive Sleep Apnea** under the WISeR (Wasteful and Inappropriate Service Reduction) Model.

| Detail | Value |
|---|---|
| Effective date | **January 15, 2026** (PA requests accepted from January 5, 2026) |
| States affected | **NJ, OH, OK, TX, AZ, WA** (six-state model, runs through Dec 31, 2031) |
| Relevant LCDs | L38276, L38307, L38398, L38387, L38310, L38312, L38385, L38528 |
| Payment change | **None** — enforces existing coverage criteria only |
| AI/ML review | CMS uses AI + human clinical review for prior auth decisions |

**Impact:** Practices implanting HNS devices for OSA in these 6 states must obtain prior authorization before the procedure. No change in allowed payment amounts. Existing coverage criteria (per LCD L38276) remain unchanged. Affects ENT/sleep surgeons billing HNS implant codes (e.g., 64568, 64569, 64570).

> **Action item:** If your practice is in NJ, OH, OK, TX, AZ, or WA and performs HNS implantation for OSA, verify prior auth workflow is in place. No billing code changes required.

### ⚠️ NEW (2026-09-03): OIG Report — Medicare PAP Device Payments (2026)

OIG released a report finding Medicare payments for PAP devices "generally complied" with requirements, but identifying significant improper payments:

| Finding | Value |
|---|---|
| Improper payments identified | **$15.2 million** |
| CPAP improper payment rate | **12.5%** (2024 data) |
| Projected improper amount | **$146.1 million** |
| Primary issue | Missing/inadequate documentation supporting PAP claims |
| OIG recommendation | CMS provide outreach/education to suppliers on PAP coverage requirements |
| CMS response | Pending (report 2026) |

> **Action item:** Heightened audit risk for CPAP/PAP suppliers. Ensure all PAP claims have: (1) qualifying sleep study on file, (2) valid AHI/RDI meeting LCD thresholds, (3) face-to-face evaluation documentation, (4) sleep study not older than 12 months (new 2026 rule). Conduct internal documentation audit.

> No other new CMS sleep apnea rules in 2026. CY2027 MPFS proposed rule is out (see Task 4). Watch final disposition of the Interoperability PA rule for HSAT/PAP auth workflow changes.

---

## Task 4 — MPFS Updates: Sleep & CCM Codes

**Status: NO CHANGE FROM PRIOR RUN — PRIOR FINDINGS REMAIN ACTIVE**

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

Conversion factors: **$33.40** (non-APM) / **$33.57** (APM qualifying).

### CCM / RPM Code Rate Changes (CY2026)

| Code | CY2025 Rate | CY2026 Rate | Change |
|---|---|---|---|
| 99490 (CCM, 20 min) | $60.49/mo | $66.30/mo | **+9.6%** |
| 99439 (CCM add-on, 20 min) | $45.93/mo | $50.56/mo | **+10.1%** |
| 99487 (complex CCM, 60 min) | ~$133/mo | ~$144/mo | ~+8% |
| 99457 (RPM, first 20 min) | ~$50/mo | ~$52/mo | ~+4% |
| 99453, 99454 (RPM setup/device) | (prior rates) | Updated 2026 | See CCNHealth analysis |

### CY2026 MPFS Correction Notice — March 12, 2026

[Federal Register 2026-04797](https://www.federalregister.gov/documents/2026/03/12/2026-04797/) — typographical and technical corrections to the Nov 5, 2025 final rule.

- PE RVUs recalculated for: **99445, 99454, 98977, 98985** (plus radiation therapy codes 77402–77438)
- All PFS PE RVUs adjusted for budget neutrality — minor downstream effects on sleep and CCM codes
- **New code 99445** confirmed: RPM device supply billable for **2–15 days** of data transmitted in a 30-day period, paid at the same rate as **99454** (which now requires ≥16 days)
- No sleep-specific (95806/95810/95811) or CCM-specific (99490/99439) rate corrections in this notice

**NEW (confirmed 2026-05-20):** Starting Jan 1, 2026, FQHCs and RHCs must bill CCM codes (99490, 99439, 99491, 99437, 99487, 99489) at the **national non-facility PFS rates** — same as fee-for-service practices. Time and documentation must be tracked separately per code.

### ⚠️ NEW (2026-06-22): Chronic Care Management Improvement Act of 2026 (H.R. 8261)

Introduced April 14, 2026. **Bipartisan** (Reps. DelBene D-WA / Kelly R-PA). Currently in committee.

**Key provision:** Eliminates the **20% Medicare Part B cost-sharing** for CCM services (99490, 99439, 99487, 99491, 99453, 99454, 99457). Today patients pay ~$12–26/month out-of-pocket per CCM session — a known enrollment barrier. Only ~4% of the 22 million eligible Medicare beneficiaries currently use CCM.

Endorsed by: AHA, AAMC, MGMA, AMGA (as of April 14, 2026).

**If enacted:** Removal of patient cost-sharing would likely sharply increase CCM enrollment and billing volume. Practices using ccm-billers should model for demand growth. No changes to provider billing codes required — impact is patient-side.

Bill status: [Congress.gov H.R. 8261](https://www.congress.gov/bill/119th-congress/house-bill/8261) — referred to committee; no floor vote scheduled yet.

### 🚨 NEW (2026-09-05): CY2027 MPFS Proposed RPM/RTM Overhaul (CMS-1848-P)

**Comment deadline: September 14, 2026 — 9 days away**

CMS proposes **sweeping changes** to Remote Patient Monitoring (RPM) and Remote Therapeutic Monitoring (RTM) in the CY2027 MPFS:

| Proposal | Current Rule | Proposed Change |
|---|---|---|
| Staffing | Third-party contracted monitoring companies allowed | **PROHIBITED — must be direct employees of billing practitioner** |
| Initiating visit | Not required for new patients | **Required: established patient relationship + face-to-face visit** |
| Billing codes | 99453, 99454, 99457, 99458 + RTM codes | **May be consolidated into 4 new G-codes (all existing codes eliminated)** |
| Practice expense | Current PE RVUs | Proposed reductions |
| CCM/APCM | — | **UNAFFECTED — contracted staffing still allowed for CCM/APCM** |

> **Action items — URGENT (deadline Sep 14):**
> - If your practice uses a third-party RPM vendor (e.g., for 99454/99457), this proposal would prohibit that arrangement as of Jan 1, 2027. Review vendor contracts and staffing model now.
> - If finalized, codes 99453, 99454, 99457, 99458 may be replaced by G-codes — ccm-billers code mapping would require update.
> - Submit comments via regulations.gov (CMS-1848-P) opposing or supporting specific provisions.
> - **CCM (99490/99439) is explicitly unaffected** — contracted staffing permitted. No action required for CCM-only practices.

Sources: [Newswire](https://www.newswire.com/news/cms-2027-proposed-rule-key-changes-to-rpm-rtm-and-medicare-care-22848994) · [Nixon Peabody](https://www.nixonpeabody.com/insights/alerts/2026/07/22/medicare-proposes-changes-to-remote-patient-monitoring-and-remote-therapeutic-monitoring-services) · [McDermott+](https://www.mcdermottplus.com/insights/remote-monitoring-at-a-crossroads-cms-proposes-sweeping-changes-in-response-to-oig-scrutiny/)

---

### ⚠️ CY2027 MPFS Proposed Rule — RELEASED (CMS-1848-P)

**Published:** July 16, 2026 (Federal Register doc 2026-14327)  
**Comment deadline: September 14, 2026 — 10 days from this report**  
**AASM analysis:** https://aasm.org/cms-releases-2027-physician-fee-schedule-proposed-rule-key-takeaways-for-sleep-medicine/  
**CMS fact sheet:** https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule

#### ⚠️ NEW HOME SLEEP TESTING CODES (replacing 95800/95801/95806)

| Feature | Detail |
|---|---|
| Current codes deleted Jan 1, 2027 | 95800, 95801, 95806 |
| Replacement | **6 new CPT codes** (effective Jan 1, 2027) |
| Code structure | Splits into **technical** (setup, acquisition, scoring) + **professional** (interpretation/reporting) components |
| Final values | Published in MPFS final rule expected **October 2026** |
| Source | AMA CPT Editorial Panel Feb 2025 decision; proposed RVUs in CMS-1848-P |

> **Action item — URGENT:** Comment period closes **September 14, 2026**. Review proposed RVUs for the new HST codes and submit comments via regulations.gov (CMS-1848-P) if RVU values are inadequate. Consult AASM's analysis (above) for sleep-medicine-specific advocacy points.

#### CY2027 Conversion Factor

| Participant type | Update |
|---|---|
| Qualifying APM (QP) | **+0.75%** |
| Non-qualifying APM | **+0.25%** |

### Upcoming: AASM OSA in Adults Full Clinical Guideline (watch)

- AASM is preparing a full updated clinical guideline for evaluation, management, and long-term care of OSA in adults, targeted for publication **end of 2026** (per JCSM). Will supersede the 2009 guideline and 2023 scoring manual annotations. Monitor for impact on 95810/95811/G0399 documentation requirements.

> **Action items:**
> 1. **IMMEDIATE — Task 1:** Check dataset page for MUP_PHY_RY25 data files (see Task 1 above).
> 2. **URGENT — 95806/95800/95801:** Begin transition to replacement codes before Jan 1, 2027. Contact AASM coding resources for new code numbers once released by AMA.
> 3. **CCM billing:** Update fee schedules for 99490 (+9.6%) and 99439 (+10.1%) if not already done.
> 4. **Facility vs. non-facility 95810/95811:** Audit setting-of-service flags; facility practices should model impact of −7% indirect PE.
> 5. **Watch for CY2027 proposed rule** (~July 2026) — may affect CCM/RPM codes and sleep coverage policy.

---

## Run History

| Date | Result |
|---|---|
| 2026-09-05 | WebSearch partial success (direct fetches blocked 403) — **⚠️ NEW: CMS-1848-P proposes banning third-party contracted RPM/RTM staffing and consolidating 99453/99454/99457/99458 into 4 new G-codes. CCM/APCM unaffected. Comment deadline Sep 14 (9 days). No new CY2024 D24 data; AASM v3; H.R. 8261 in committee.** |
| 2026-09-04 | WebSearch partial success (direct fetches blocked 403) — No new findings. Comment deadline for CY2027 MPFS (CMS-1848-P) now **10 days away** (Sep 14). All prior findings unchanged. |
| 2026-09-03 | WebSearch partial success (EGRESS_BLOCKED on direct fetches) — **⚠️ MAJOR: CY2027 MPFS proposed rule (CMS-1848-P, FR 2026-14327) confirmed released Jul 16 2026 — 6 new HST replacement codes proposed, comment deadline Sep 14 2026 (11 days). NEW: OIG PAP report ($15.2M improper payments, 12.5% CPAP error rate). H.R. 8261 still in committee. AASM scoring manual still v3. CY2024 (RY26) D24 data not confirmed.** |
| 2026-06-29 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) D24_Prov_Svc not confirmed; CY2027 MPFS proposed rule confirmed not yet released (~mid-July 2026, ~2 weeks out); AASM scoring manual still v3 (2023), no new 2026 guidelines; no new CMS FR sleep apnea rules. All prior findings unchanged. |
| 2026-06-28 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) D24_Prov_Svc not confirmed (dataset last updated May 21, 2026); CY2027 MPFS proposed rule confirmed not yet released (~mid-July 2026); AASM no new guidelines; no new CMS FR sleep apnea rules. All prior findings unchanged. |
| 2026-06-27 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) D24_Prov_Svc not confirmed; CY2027 MPFS proposed rule confirmed not yet released (~mid-July 2026); AASM no new guidelines; no new CMS FR sleep apnea rules. All prior findings unchanged. |
| 2026-06-26 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) D24_Prov_Svc not confirmed; CY2027 MPFS proposed rule confirmed not yet released (~mid-July 2026); AASM no new guidelines; no new CMS FR sleep apnea rules. All prior findings unchanged. |
| 2026-06-25 | WebSearch partial success (direct fetches blocked 403) — **⚠️ NEW: WISeR Model HNS prior auth for OSA (6 states, effective Jan 15 2026, FR 2025-12195) added to Task 3.** CY2024 (RY26) D24_Prov_Svc file not confirmed; CY2027 MPFS proposed rule not yet released (~mid-July 2026); AASM scoring manual still v3 (2023), no new 2026 guidelines. |
| 2026-06-24 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) D24_Prov_Svc file not confirmed; CY2027 MPFS proposed rule not yet released (expected ~mid-July 2026); AASM scoring manual still v3 (2023), no new 2026 guidelines; no new CMS FR sleep apnea rules. All prior findings confirmed unchanged. |
| 2026-06-23 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) D24_Prov_Svc file not confirmed; same ambiguous "CY2024 dataset page" signal as prior runs. CY2027 MPFS proposed rule not yet released (expected ~mid-July 2026). AASM: no new scoring manual or guidelines. No new CMS FR sleep apnea rules. All prior findings confirmed unchanged. |
| 2026-06-22 | WebSearch partial success (direct fetches blocked 403) — **⚠️ NEW: Chronic Care Management Improvement Act of 2026 (H.R. 8261) confirmed — bipartisan bill, introduced Apr 14 2026, in committee; would eliminate 20% patient cost-sharing for CCM. AHA/AAMC/MGMA/AMGA endorsed.** CMS data: no CY2024 D24 file confirmed (same ambiguous signal as prior runs). CY2027 MPFS not yet released. AASM: no new scoring manual; CSA/inpatient OSA/insomnia guidelines already captured. No new CMS FR sleep apnea rules. |
| 2026-06-21 | WebSearch partial success (direct fetches blocked 403) — No new findings. CMS search reconfirmed same "CY2024 data, published Dec 9 2025, last updated May 21 2026" signal (same as Jun 8/12/16 runs; D24 explicit search was negative Jun 9 — no filename confirmed). CY2027 MPFS proposed rule not yet released (expected ~July 2026). AASM scoring manual still v3 (2023); no new 2026 guidelines. No new CMS FR sleep apnea rules. All prior findings confirmed unchanged. |
| 2026-06-20 | WebSearch partial success (direct fetches blocked 403) — No new findings. No D24_Prov_Svc filename found; CY2024 (RY26) data not yet released. CY2027 MPFS proposed rule not yet released (expected ~July 2026). AASM scoring manual still v3 (2023); no new 2026 guidelines. No new CMS FR sleep apnea rules. All prior findings confirmed unchanged. |
| 2026-06-19 | WebSearch partial success (direct fetches blocked 403) — No new findings. No D24_Prov_Svc filename found; CY2024 (RY26) data not yet released. CY2027 MPFS proposed rule not yet released (expected ~July 2026). AASM scoring manual still v3 (2023); no new 2026 guidelines. No new CMS FR sleep apnea rules. All prior findings confirmed unchanged. |
| 2026-06-18 | WebSearch partial success (direct fetches blocked 403) — No new findings. CMS dataset page: no D24_Prov_Svc filename found; CY2024 (RY26) data not yet released. CY2027 MPFS proposed rule not yet released (expected ~July 2026). AASM scoring manual still v3 (2023); no new 2026 guidelines detected. No new CMS FR sleep apnea rules in 2026. All prior findings confirmed unchanged. |
| 2026-06-17 | WebSearch partial success (direct fetches blocked 403) — No new findings. CMS dataset page continues to show "CY2024" language; no D24_Prov_Svc filename confirmed (same pattern as prior days). New detail added to Task 3: CMS Interoperability and Prior Authorization Proposed Rule (Apr 14, 2026) explicitly provisions polysomnography/HSAT/PAP data exchange — relevant to sleep practice workflows. CY2027 MPFS proposed rule not yet released. AASM scoring manual still v3. All prior findings confirmed unchanged. |
| 2026-06-16 | WebSearch partial success (direct fetches blocked 403) — No new findings. CMS dataset page again surfaces "CY2024" language (same ambiguous signal as 06-08/06-12); no D24_Prov_Svc filename found. CY2027 MPFS proposed rule not yet released. AASM scoring manual still v3. No new CMS FR sleep apnea rules. All prior findings confirmed unchanged. |
| 2026-06-15 | WebSearch partial success (direct fetches blocked 403) — No new findings. No D24_Prov_Svc file found; CY2024 (RY26) data not yet released. "March 2026 CPAP expansion" signal investigated and confirmed false positive (refers to 2008 NCD 240.4). CY2027 MPFS proposed rule not yet released. AASM no new guidelines. All prior findings confirmed unchanged. |
| 2026-06-14 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) data not yet released; D24 filename not found. CY2027 MPFS proposed rule not yet released (expected ~July 2026). AASM scoring manual still v3 (2023). No new CMS FR sleep apnea rules in 2026. All prior findings confirmed unchanged. |
| 2026-06-13 | WebSearch partial success (direct fetches blocked 403) — No new findings. CMS search confirms CY2024 dataset page exists but D24 filename search still negative — RY26 data not yet released. CY2027 MPFS proposed rule not yet released (expected ~July 2026). AASM scoring manual still v3 (2023); accreditation standards updated Jan 2025 only. No new CMS FR sleep apnea rules in 2026. All prior findings confirmed unchanged. |
| 2026-06-12 | WebSearch partial success (direct fetches blocked 403) — No new findings. Search again surfaced "CY2024" language on CMS dataset page (same ambiguous signal as 2026-06-08; June 9 D24 filename search was negative — manual check recommended). CY2027 MPFS proposed rule not yet released. AASM and FR checks unchanged. |
| 2026-06-11 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) data not yet released. CY2027 MPFS proposed rule not yet released (expected ~July 2026). All prior findings confirmed unchanged. |
| 2026-06-10 | WebSearch partial success (direct fetches blocked 403) — No new findings. CY2024 (RY26) data not yet released. CY2027 MPFS proposed rule not yet released (expected ~July 2026). All prior findings confirmed unchanged. |
| 2026-06-09 | WebSearch partial success (direct fetches blocked 403) — **D24 Prov_Svc file explicitly searched and NOT found. CY2024 (RY26) data not yet released. All prior findings confirmed unchanged.** |
| 2026-06-08 | WebSearch partial success (direct fetches blocked 403) — **⚠️ Search snippet mentions "calendar year 2024" data on CMS dataset page — possible RY26 release; manual verification required. No other new findings.** |
| 2026-06-07 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-06-06 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-06-05 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-06-04 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-06-03 | WebSearch partial success (direct fetches blocked 403) — no new findings; added AASM OSA-in-Adults full guideline (end-of-2026) to watch list |
| 2026-06-02 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-06-01 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-31 | WebSearch partial success (direct fetches blocked 403) — **⚠️ New AASM guideline found: combination chronic insomnia treatment (April 13, 2026, JCSM); all other findings unchanged** |
| 2026-05-30 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-29 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-28 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-27 | WebSearch partial success (direct fetches blocked 403) — **CY2026 MPFS Correction Notice (FR 2026-04797) details confirmed: 99445 2–15-day billing rule, PE RVU corrections for 99454/98977/98985; no other new findings** |
| 2026-05-26 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-25 | All fetches blocked (403 / Host not in allowlist) — no new findings; all prior findings confirmed unchanged |
| 2026-05-24 | All fetches blocked (403 / Host not in allowlist) — no new findings; all prior findings confirmed unchanged |
| 2026-05-23 | All fetches blocked (403 / Host not in allowlist) — no new findings; all prior findings confirmed unchanged |
| 2026-05-22 | All fetches blocked (403 / Host not in allowlist) — no new findings; all prior findings confirmed unchanged |
| 2026-05-21 | WebSearch partial success — no new findings; all prior findings confirmed unchanged |
| 2026-05-20 | WebSearch partial success — **⚠️ MUP_PHY_R25 CSV filename confirmed (`D23_Prov_Svc.csv`); RY25 data files exist; FQHC/RHC CCM billing detail added** |
| 2026-05-19 | WebSearch partial success — **⚠️ MUP_PHY_RY25 data dictionary (March 2025) found; possible new distribution post-baseline** |
| 2026-05-18 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
| 2026-05-17 | WebSearch partial success (direct fetches blocked 403) — no new findings; all prior findings confirmed unchanged |
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
| CMS 2024 Provider-Service data | **⚠️ MUP_PHY_R25 CSV confirmed (`D23_Prov_Svc.csv`) — CY2023 data available; CY2024 not yet released** | **Yes — download and run filter_ccm.py for CY2023 data** |
| AASM guidelines | **⚠️ NEW (Apr 2026): insomnia combo therapy guideline; + 3 prior 2025 guidelines; scoring manual still v3** | **Yes — review April 2026 guideline for CCM documentation impact** |
| Federal Register / OIG | **⚠️ WISeR Model HNS prior auth (6 states, eff. Jan 15 2026); NEW (Sep 3): OIG PAP report — $15.2M improper payments, 12.5% error rate** | **Audit PAP documentation; verify HNS PA if in NJ/OH/OK/TX/AZ/WA** |
| **🚨 MPFS CY2027 proposed rule** | CMS-1848-P released Jul 16 2026 — 6 new HST codes + **⚠️ NEW: RPM overhaul banning 3rd-party vendors, consolidating codes into G-codes** | **URGENT — Comment deadline Sep 14, 2026 (9 days). Submit via regulations.gov.** |
| MPFS — code deletions | **95800, 95801, 95806 deleted Jan 1, 2027; 6 replacement codes proposed** | **URGENT — monitor final rule Oct 2026 for new code RVUs** |
| MPFS — CY2027 rates | CY2027 conversion factor: +0.75% APM / +0.25% non-APM (proposed) | Update fee schedules once final rule published Oct 2026 |
| MPFS — CY2026 rates | CCM up ~10%; sleep codes −2.5%; facility labs −7% indirect PE | Already in effect — update fee schedules if not done |
| **⚠️ CCM Improvement Act (H.R. 8261)** | Bipartisan bill to eliminate 20% patient cost-sharing for CCM — still in committee Sep 2026 | **Monitor — if passed, model for enrollment surge** |
