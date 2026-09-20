# CMS Data Monitor Report

**Run date/time:** 2026-09-20 (automated daily run)
**Consecutive days network blocked: 13** (since 2026-09-08)

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

- Could not check for 2027 MPFS proposed rule or 2026 MPFS corrections
- Codes of interest: 95810, 95811, 95806, G0399, 99490, 99439, 99487, 99491, 99453, 99454, 99457
- **Action item:** Check https://www.federalregister.gov manually for the 2027 MPFS Proposed Rule (typically released July–August each year)

---

## Summary

All four tasks blocked for **13 consecutive days** by the session's network egress policy.

| Blocked Host | Task |
|---|---|
| data.cms.gov | CMS 2024 provider/service data |
| aasm.org | AASM scoring manual updates |
| www.federalregister.gov | Sleep apnea rules + MPFS updates |

**This monitoring schedule requires outbound access to government and medical association sites.** To resolve:
1. Reconfigure the Claude Code on the web environment to allow `data.cms.gov`, `www.federalregister.gov`, and `aasm.org` in the egress policy.
2. Or run the checks locally where those sites are accessible.

The 2024 CMS dataset found on 2026-09-07 still needs to be downloaded and processed — this is the highest-priority pending action.
