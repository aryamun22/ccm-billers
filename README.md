# CCM Medicare Billers

Visualization of Medicare Part B providers billing Chronic Care Management (CCM) HCPCS codes, sourced from the CMS **Medicare Physician & Other Practitioners — by Provider and Service** public use file.

## CCM codes tracked
- 99490 — CCM 20 min/month (non-complex, staff time)
- 99439 — CCM each additional 20 min (add-on to 99490)
- 99487 — Complex CCM first 60 min
- 99489 — Complex CCM each additional 30 min
- 99491 — CCM 30 min/month (physician/QHP personally)
- 99437 — CCM each additional 30 min (add-on to 99491)
- G0506 — Comprehensive assessment for CCM

## Setup

```bash
# 1. Raw file lives at ~/Data/MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv (~2 GB)
# 2. Filter to CCM codes + aggregate
python3 scripts/filter_ccm.py

# 3. Serve the web UI
cd web && python3 -m http.server 8000
# open http://localhost:8000
```

The Python script writes `web/data.json` with:
- Per-provider aggregates (NPI, name, org, specialty, city/state, services, beneficiaries, Medicare $)
- Top specialties and code mix for the charts
- Totals for the KPI tiles

## Data source
CMS Provider Data Catalog — dataset `92396110-2aed-4d63-a6a2-5d6207d46a29`
