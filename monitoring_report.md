# CMS Data Monitor Report

**Run date/time:** 2026-09-15 10:03:27 UTC
**Consecutive days network blocked: 8** (since 2026-09-08)

---

## Task 1: CMS Provider-and-Service Data (Medicare Physician & Other Practitioners)

**Status: BLOCKED — network egress proxy denied access to `data.cms.gov`**

- Current latest in repo: 2023-12-31
- ⚠️ NOTE: The 2026-09-07 run confirmed CY2024 (RY26) D24_Prov_Svc dataset was released — however the download has not been run since the network went down.
- Could not re-verify or retrieve that release
- **Action item:** Run `filter_ccm.py` against the 2024 dataset — download URL was confirmed on 2026-09-07. Check that commit for the URL.

---

## Task 2: AASM Scoring Manual / Practice Parameters

**Status: BLOCKED — network egress proxy denied access to `aasm.org`**

- Could not check for 2026 updates
- **Action item:** Visit https://aasm.org/clinical-resources/practice-standards/ manually and check for 2026-dated documents.

---

## Task 3: CMS Federal Register — Sleep Apnea Rules (2026)

**Status: BLOCKED — network egress proxy denied access to `www.federalregister.gov`**

- Could not query for CMS sleep apnea proposed/final rules published ≥ 2026-01-01
- **Action item:** Check manually: https://www.federalregister.gov/agencies/centers-for-medicare-medicaid-services (filter by date and keyword "sleep apnea")

---

## Task 4: MPFS Updates — Sleep/CCM CPT Codes

**Status: BLOCKED — network egress proxy denied access to `www.federalregister.gov`**

- CPT codes of interest: 95810, 95811, 95806, G0399 (sleep studies); 99490, 99439, 99487, 99491 (CCM); 99453, 99454, 99457 (RPM)
- ⚠️ NOTE: The 2026-09-05 run found the CY2027 MPFS proposed rule includes an RPM/RTM overhaul — this has not been re-verified since the network went down.
- **Action item:** Search Federal Register manually for "physician fee schedule 2027" to confirm current status of the proposed rule and any CPT code changes.

---

## Summary

| Task | Result |
|------|--------|
| CMS Provider-and-Service 2024 data | ❌ Egress blocked (day 8) |
| AASM guideline updates 2026 | ❌ Egress blocked (day 8) |
| Federal Register sleep apnea rules 2026 | ❌ Egress blocked (day 8) |
| MPFS CPT code updates | ❌ Egress blocked (day 8) |

**Root cause:** The scheduled monitoring environment's network egress proxy (`selective: false`) blocks all four target domains (`data.cms.gov`, `aasm.org`, `www.federalregister.gov`). This has persisted for 8 consecutive days.

**Recommended fix:** In the Claude Code web session configuration, enable outbound access to these domains:
- `data.cms.gov`
- `www.federalregister.gov`
- `aasm.org`

See the [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment network policy configuration. Until then, all four monitoring tasks must be run manually.

**Pending actions from last successful runs:**
1. (from 2026-09-07) CY2024 D24_Prov_Svc dataset confirmed released — run `filter_ccm.py` to ingest
2. (from 2026-09-05) CY2027 MPFS proposed rule includes RPM/RTM overhaul — review CPT impact on 99453/99454/99457
