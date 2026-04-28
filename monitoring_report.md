# CMS Data Monitor Report

**Last successful run:** 2026-04-20  
**Latest run:** 2026-04-28 — **ALL FETCHES BLOCKED** (403 `Host not in allowlist` on all four sources)  
**Checked by:** CMS Data Monitor (automated)  
**Baseline:** Provider-and-Service data newest distribution = 2023-12-31

> **Network note:** data.cms.gov, aasm.org, federalregister.gov, and cms.gov all returned 403 (`Host not in allowlist`). No new data could be retrieved. Findings from 2026-04-20 remain the last known state. Action items from that run are still open.

---

## Task 1 — CMS Provider-and-Service 2024 Data Release

**Status: FETCH BLOCKED — prior finding unverified**

- Attempted: `https://data.cms.gov/data.json` → 403
- Attempted: `https://data.cms.gov/provider-summary-by-type-of-service/...` → 403

As of 2026-04-20: a `last_modified` date of **2025-10-28** on the catalog entry suggested a post-2023 release. Could not confirm or deny a CY2024 distribution today.

> **Action item (open):** Manually visit the dataset page and check for a distribution newer than 2023-12-31. If found, download and run `filter_ccm.py`.  
> Dataset page: https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service

---

## Task 2 — AASM Scoring Manual / Guideline Updates

**Status: FETCH BLOCKED — prior finding unverified**

- Attempted: `https://aasm.org/clinical-resources/practice-standards/` → 403
- Attempted: `https://aasm.org/clinical-resources/` → 403

As of 2026-04-20: two new guidelines were identified (Central Sleep Apnea and Inpatient OSA, published Feb 2026). No update to Scoring Manual v3 was detected.

> **Action item (open):** Review the Feb 2026 AASM guidelines for coding/documentation impact on 95810, 95811, 95806, G0399.

---

## Task 3 — Federal Register: Sleep Apnea Rules (CMS, 2026)

**Status: FETCH BLOCKED — no new rules confirmed or denied**

- Attempted: Federal Register API + web search → 403 on all variants

As of 2026-04-20: no dedicated sleep apnea CMS rules published in 2026 were found.

> No action item. Monitor for changes.

---

## Task 4 — MPFS Updates: Sleep & CCM Codes

**Status: FETCH BLOCKED — prior finding unverified**

- Attempted: `https://www.federalregister.gov/...physician+fee+schedule...` → 403
- Attempted: `https://www.cms.gov/medicare/physician-fee-schedule/search` → 403

As of 2026-04-20: CY2026 MPFS Final Rule (CMS-1832-F) changes:
- **95800** — PE inputs revised for disposable HSAT devices
- **99457** — time threshold reduced (may increase qualifying RPM encounters)
- CY2027 MPFS proposed rule: not yet released (expected ~July 2026)

> **Action items (open):**
> 1. Audit 99457 RPM claims against lowered time threshold.
> 2. Confirm 95800 PE input change impact on reimbursement.
> 3. Watch for CY2027 MPFS proposed rule (~July 2026).

---

## Run History

| Date | Result |
|---|---|
| 2026-04-28 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-26 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-24 | All fetches blocked (403 `Host not in allowlist`) — no new findings |
| 2026-04-22 | All fetches blocked (403 / ECONNREFUSED) — no new findings |
| 2026-04-21 | All fetches blocked (403) — findings carried from 2026-04-20 |
| 2026-04-20 | Partial success — findings above |

---

## Summary

| Task | Last Known Finding | Fetch Today | Action Required |
|---|---|---|---|
| CMS 2024 Provider-Service data | Likely released Oct 2025 | BLOCKED | Yes — verify manually |
| AASM guidelines | 2 new guidelines (Feb 2026) | BLOCKED | Yes — review for coding impact |
| Federal Register sleep rules 2026 | None found | BLOCKED | No |
| MPFS sleep/CCM codes | 95800 PE + 99457 time threshold changed | BLOCKED | Yes — audit RPM claims |
