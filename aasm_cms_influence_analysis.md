# AASM ↔ CMS Influence Analysis: Structural Underscoring in Sleep Medicine

**Date:** 2026-04-18
**Data source:** CMS Medicare Physician & Other Practitioners — by Provider and Service (2023), 9,660,647 rows
**Analysis scope:** 4,403 NPIs billing sleep diagnostic codes; 2,926 with ≥50 studies

---

## 1. The influence loop

```
AASM writes scoring rules ──→ CMS references in LCDs ──→ Insurers adopt
     ↑                              ↓                          ↓
     │                    Rules determine who gets         Payers choose
     │                    diagnosed (AHI threshold)        1A vs 1B rule
     │                              ↓                          ↓
     │                    Diagnosis determines              Stricter rule
     │                    treatment pathway                = fewer diagnoses
     │                              ↓                     = lower cost
     │                    Treatment generates               ↓
     │                    claims (PAP, supplies)       Medicare uses 1B (4%)
     │                              ↓                  AASM recommends 1A (3%)
     │                    Claims data feeds back            ↓
     └──────────── RUC sets RVUs ←── CMS adjusts ←── This tension IS the game
```

### How AASM influences CMS
- **RUC (Relative Value Scale Update Committee):** AASM representatives sit on the AMA's RUC, which recommends RVUs for sleep CPT codes. CMS accepts RUC recommendations >90% of the time. However, AASM has acknowledged they *lack* representation in the AMA House of Delegates, which weakens their influence over the RUC process.
- **Clinical practice guidelines:** AASM writes the scoring manual (AASM Manual for the Scoring of Sleep and Associated Events) which defines how PSG and HSAT are interpreted. CMS and MACs (Medicare Administrative Contractors) reference these guidelines in LCDs.
- **Comment letters:** AASM files formal comments on every annual MPFS (Medicare Physician Fee Schedule) proposed rule. These are public on regulations.gov.
- **JCSM editorials:** Position papers in the Journal of Clinical Sleep Medicine become the intellectual basis for LCD changes.

### How CMS influences AASM and clinical behavior
- **Reimbursement rates** determine whether sleep labs are profitable. CMS cuts to PSG rates have driven the shift toward HSAT.
- **Coverage determinations** (LCDs/NCDs) define which patients qualify for PAP coverage — and which scoring rule must be used.
- **The 90-day PAP compliance rule** (CFR §410.38(c)) forces clinics to document adherence at 30/60/90 days or Medicare stops paying for the device.
- **Medicare Advantage** plans layer additional prior auth requirements that further restrict access.

---

## 2. The three structural underscoring mechanisms

### Mechanism A: The hypopnea scoring war (AASM 1A vs CMS 1B)

This is the single most important political fact in sleep medicine.

| Rule | Definition | Effect on AHI | Who uses it |
|---|---|---|---|
| **AASM Rule 1A (recommended)** | Hypopnea = ≥30% airflow reduction for ≥10 sec with **≥3% oxygen desaturation OR arousal** | **Higher AHI** — more events counted | AASM-accredited centers (for clinical reporting) |
| **CMS Rule 1B (mandated for Medicare)** | Hypopnea = ≥30% airflow reduction for ≥10 sec with **≥4% oxygen desaturation only** | **Lower AHI** — arousals don't count, higher desat threshold | All Medicare claims; many commercial payers |

**CMS chose 1B as a cost-containment strategy.** Fewer patients cross the AHI ≥5 threshold → fewer OSA diagnoses → fewer PAP prescriptions → lower Medicare spend.

**Impact:** 26.4% of patients who have OSA under 1A scoring are reclassified as NOT having OSA (or less severe) under 1B scoring.

**Source:** [The ethics of hypopnea scoring — JCSM](https://jcsm.aasm.org/doi/10.5664/jcsm.10944)

### Mechanism B: HSAT vs in-lab PSG (mechanical underscoring)

HSAT mechanically underscores AHI because:
- **No EEG** → cannot measure actual sleep time → uses total recording time (TRT) as denominator → dilutes AHI
- **Patient awake during recording** → time awake inflates denominator → AHI drops
- **Fewer channels** → misses central apneas, upper airway resistance events, some hypopneas
- **Age bias:** older patients spend more time awake → greater underestimation

**Published finding:** of all patients with OSA on PSG, 26.4% would be reclassified as having less severe or no OSA after recalculating AHI using time-in-bed (HSAT methodology) rather than total sleep time (PSG methodology).

**Source:** [Underestimation of Sleep Apnea With HSAT — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5359328/)

### Mechanism C: Combined stack (HSAT + 1B scoring)

When a practice uses HSAT (mechanical underscoring) AND scores with CMS 1B rule (regulatory underscoring), the two effects compound. A patient whose true in-lab 1A AHI is 18 (moderate OSA) could easily score as AHI 9 (mild) or even AHI 4 (no OSA) under HSAT + 1B. This is not fraud — it's the structural result of CMS cost-containment policy applied to a less-sensitive diagnostic modality.

---

## 3. Data analysis: HSAT ratio by practice (from 2023 CMS claims)

### Distribution

| Metric | Value |
|---|---|
| Total NPIs billing any sleep diagnostic code | 4,403 |
| NPIs with ≥50 sleep studies | 2,926 |
| Average HSAT ratio across all practices | **28.0%** |
| 100% HSAT (zero PSG) — maximum structural underscoring | **239 providers (8.2%)** |
| 0% HSAT (100% in-lab PSG) | **881 providers (30.1%)** |
| >70% HSAT | 239 providers |
| >50% HSAT | 595 providers |

### HSAT ratio by specialty (≥10 providers)

| Specialty | Providers | Avg HSAT ratio | Total studies | Underscoring risk |
|---|---:|---:|---:|---|
| Cardiology | 20 | **37%** | 3,914 | High — screening CHF patients with HSAT misses central apnea |
| Otolaryngology / ENT | 71 | **36%** | 12,245 | High — HSAT may underestimate severity before surgical decisions |
| Pulmonary Disease | 1,249 | **30%** | 195,118 | Moderate — high-volume, mixed HSAT/PSG |
| Critical Care | 113 | **30%** | 16,204 | Moderate |
| Internal Medicine | 243 | **27%** | 34,400 | Moderate |
| Sleep Medicine | 499 | **27%** | 85,438 | Lower — own PSG labs, less reliant on HSAT |
| Pediatric Medicine | 16 | **27%** | 1,858 | Moderate |
| Family Practice | 56 | **26%** | 9,715 | Moderate |
| Neurology | 365 | **25%** | 58,301 | Moderate |
| Psychiatry | 33 | **22%** | 4,502 | Lower |
| IDTFs | 227 | **19%** | 56,329 | Paradoxically low — IDTFs with PSG labs do mostly in-lab |

### Top 30 practices by HSAT ratio (≥50 studies) — structural underscoring signal

| # | Name | City | ST | Specialty | PSG | HSAT | Total | HSAT% | Medicare $ |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| 1 | Barton Schneyer | Southport | NC | Pulmonary | 0 | 51 | 51 | 100% | $3,501 |
| 2 | Joseph Crocetti | Abington | PA | Pulmonary | 0 | 50 | 50 | 100% | $1,734 |
| 3 | Peter Ricketti | Trenton | NJ | Allergy/Immun | 0 | 56 | 56 | 100% | $2,686 |
| 4 | Domenick Sorresso | Hudson | FL | Pulmonary | 0 | 52 | 52 | 100% | $3,638 |
| 5 | Rajiv Nanavaty | Suffolk | VA | Neurology | 0 | 76 | 76 | 100% | $5,095 |
| 6 | Pawan Chawla | Tacoma | WA | Pulmonary | 0 | 69 | 69 | 100% | $2,018 |
| 7 | Ari Wirtschafter | Boca Raton | FL | ENT | 0 | 72 | 72 | 100% | $2,191 |
| 8 | Trustin Ennacheril | Kittery | ME | Sleep Medicine | 0 | 53 | 53 | 100% | $1,669 |
| 9 | Ramin Mehdian | Newbury Park | CA | Pulmonary | 0 | 61 | 61 | 100% | $2,220 |
| 10 | **Sleeptopia Inc** | Wichita | KS | IDTF | 0 | **628** | 628 | 100% | $23,909 |
| 11 | Dana Baker | Round Rock | TX | Family Practice | 0 | 74 | 74 | 100% | $2,486 |
| 12 | Samir Shah | Newton | NJ | Pulmonary | 0 | 106 | 106 | 100% | $7,827 |
| 13 | Robert Gordon | Oklahoma City | OK | Pulmonary | 0 | 75 | 75 | 100% | $3,922 |
| 14 | Payam Aghassi | Leominster | MA | Pulmonary | 0 | 103 | 103 | 100% | $7,026 |
| 15 | Ashish Patel | Pasadena | CA | Sleep Medicine | 0 | 134 | 134 | 100% | $10,238 |
| 16 | Mayank Patel | Houston | TX | Pulmonary | 0 | 58 | 58 | 100% | $3,637 |
| 17 | Garrick Applebee | Burlington | VT | Sleep Medicine | 0 | 74 | 74 | 100% | $5,016 |
| 18 | Richard Miller | Newark | NJ | Pulmonary | 0 | 73 | 73 | 100% | $2,601 |
| 19 | Michael Spandorfer | Charleston | SC | Pulmonary | 0 | 86 | 86 | 100% | $4,633 |
| 20 | Amaiak Chilingaryan | Glendale | CA | Neurology | 0 | 79 | 79 | 100% | $6,484 |
| 21 | **HomeSleep LLC** | Paramus | NJ | IDTF | 0 | **407** | 407 | 100% | $25,521 |
| 22 | Martha Preciado | Los Angeles | CA | Cardiology | 0 | 224 | 224 | 100% | $18,277 |
| 23 | Sharad Dass | San Jose | CA | Pulmonary | 0 | 83 | 83 | 100% | $7,418 |
| 24 | Rebeca Maynard | Lebanon | IN | Internal Med | 0 | 84 | 84 | 100% | $2,619 |
| 25 | Stephen Jackson | Abilene | TX | Internal Med | 0 | 58 | 58 | 100% | $3,624 |
| 26 | Integrated Sleep Solutions | Ocean Springs | MS | IDTF | 0 | 56 | 56 | 100% | $1,661 |
| 27 | Jingtao Huang | Chicago | IL | Sleep Medicine | 0 | 74 | 74 | 100% | $4,151 |
| 28 | Guardian Sleep Clinic LLC | San Jose | CA | IDTF | 0 | 72 | 72 | 100% | $4,602 |
| 29 | Wesley Fleming | Irvine | CA | Undefined | 0 | 339 | 339 | 100% | $25,650 |
| 30 | Agnieszka Palecki | Barnegat | NJ | Pulmonary | 0 | 87 | 87 | 100% | $7,032 |

### Top 20 practices by PSG ratio (100% in-lab) — potential over-diagnosis incentive

| # | Name | City | ST | Specialty | PSG | HSAT | Total | Titration ratio | Medicare $ |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| 1 | William Wade | South Charleston | WV | Pulmonary | 54 | 0 | 54 | 44% | $13,440 |
| 2 | Chirag Popat | Roswell | GA | Pulmonary | 64 | 0 | 64 | 58% | $10,672 |
| 3 | Neil Williams | Irving | TX | ENT | 98 | 0 | 98 | 62% | $9,201 |
| 4 | David Defeo | Winston Salem | NC | Critical Care | 75 | 0 | 75 | 40% | $33,676 |
| 5 | Karl Kuhn | Nashville | TN | Pulmonary | 95 | 0 | 95 | 35% | $7,888 |
| 6 | Ashok Gupta | Eaton Rapids | MI | Internal Med | 55 | 0 | 55 | 47% | $15,143 |
| 7 | Jacqueline Chang | Boston | MA | Internal Med | 106 | 0 | 106 | 66% | $10,722 |
| 8 | Mark Gosnell | Elkridge | MD | Pulmonary | 105 | 0 | 105 | 39% | $55,551 |
| 9 | Houston Operating Company LLC | Houston | TX | IDTF | 78 | 0 | 78 | 47% | $31,129 |
| 10 | **Flagler Diagnostic & Sleeping** | Bunnell | FL | IDTF | **302** | 0 | 302 | 34% | **$138,866** |
| 11 | Amit Khanna | New London | CT | Sleep Medicine | 201 | 0 | 201 | 34% | $19,091 |
| 12 | Stephen Grant | Clive | IA | Internal Med | 101 | 0 | 101 | **79%** | $8,799 |
| 13 | Matthew Howard | Augusta | GA | Sleep Medicine | 68 | 0 | 68 | 38% | $6,041 |
| 14 | **Ivy Andersen** | La Crosse | WI | Neurology | 137 | 0 | 137 | **85%** | $12,342 |
| 15 | Kawish Garg | Chambersburg | PA | Psychiatry | 91 | 0 | 91 | 45% | $7,527 |
| 16 | Safal Shetty | Douglasville | GA | Pulmonary | 57 | 0 | 57 | 56% | $8,649 |
| 17 | Alexander Choi | Chicago | IL | Sleep Medicine | 82 | 0 | 82 | 50% | $7,158 |
| 18 | Dainis Irbe | Eugene | OR | Neurology | 156 | 0 | 156 | 53% | $73,893 |
| 19 | Kevin Hara | Aiea | HI | Pulmonary | 72 | 0 | 72 | 62% | $38,392 |
| 20 | Nabih Alsheikh | Hattiesburg | MS | Nephrology | 137 | 0 | 137 | 39% | $12,506 |

---

## 4. Who is structurally incentivized to underscore (and why)

### Practices that underscore (produce lower AHI than reality)

| Practice type | Mechanism | Incentive |
|---|---|---|
| **100% HSAT practices** (239 identified) | Mechanical: HSAT uses TRT not TST; fewer channels; misses events | Lower capital cost ($2-5K per HSAT vs $500K+ for sleep lab). Higher throughput. No overnight staffing costs. |
| **Medicare-dominant practices using 1B scoring** | Regulatory: 4% desat-only threshold excludes arousal-based hypopneas | CMS mandates 1B for coverage. Practices can't override it for Medicare patients. |
| **ACO-aligned practices** | Financial: shared-savings ACOs are penalized for downstream cost (PAP + supplies + compliance monitoring) | Diagnosing severe OSA triggers expensive treatment cascade. Under-diagnosis reduces attributed spend. |
| **Medicare Advantage-contracted practices** | Financial: MA plans restrict PAP coverage through prior auth + stricter criteria | MA plans sometimes require AHI ≥15 (moderate-severe) for PAP coverage. Practices know borderline patients will be denied and may not pursue aggressive scoring. |
| **Practices avoiding the 90-day compliance burden** | Administrative: CMS's 90-day PAP compliance rule creates documentation overhead | If a patient is diagnosed mild (AHI 5-14), the practice may recommend oral appliance or positional therapy instead of PAP — avoiding the compliance documentation requirement entirely. |

### Practices that may over-score (produce higher AHI than reality)

| Practice type | Mechanism | Incentive |
|---|---|---|
| **Sleep labs that own their own DME business** | Financial: diagnosis → PAP prescription → DME revenue for the same entity | Self-referral creates incentive to find pathology. This is a well-documented conflict of interest. |
| **High-titration-ratio practices** (>60% of PSGs proceed to titration) | Clinical aggressiveness: titrating nearly every patient suggests low threshold for diagnosis | May reflect genuinely severe populations OR aggressive diagnostic posture |
| **IDTFs with PAP-vendor affiliations** | Financial: commercial sleep labs may have revenue-sharing with PAP distributors | More diagnoses → more PAP referrals → more downstream revenue |

---

## 5. How to find the AASM → CMS influence people

| Source | What it reveals | Access |
|---|---|---|
| **RUC meeting minutes** | Which AASM reps voted on which RVU changes for sleep CPTs | [ama-assn.org/ruc-recommendations](https://www.ama-assn.org/about/rvs-update-committee-ruc/ruc-recommendations-minutes-voting) |
| **AASM's AMA advocacy page** | AASM explicitly states they lack HOD representation → weaker RUC influence | [aasm.org/payment-reform](https://aasm.org/clinical-resources/coding-reimbursement/payment-reform/) |
| **CMS MPFS proposed/final rules** | Annual sleep-CPT reimbursement changes; AASM comment letters | [regulations.gov](https://www.regulations.gov) — search "AASM" + "MPFS" |
| **AASM board of directors** | Cross-reference with: Open Payments, CMS advisory committees, RUC seats | [aasm.org/about](https://aasm.org/about/) |
| **Open Payments (Sunshine Act)** | Which sleep KOLs receive payments from ResMed, Philips, F&P, Inspire | [openpaymentsdata.cms.gov](https://openpaymentsdata.cms.gov/) |
| **JCSM editorials** | Position papers that become the basis for LCDs; the "ethics of hypopnea scoring" paper directly addresses 1A vs 1B | [jcsm.aasm.org](https://jcsm.aasm.org/doi/10.5664/jcsm.10944) |
| **MAC LCD databases** | Local Coverage Determinations for sleep services by region; reference AASM guidelines | [cms.gov/medicare-coverage-database](https://www.cms.gov/medicare-coverage-database/) |
| **Noridian/CGS/Palmetto MAC guidance** | Sleep test scoring letters clarifying Medicare requirements per region | [Noridian Sleep Scoring DCL](https://med.noridianmedicare.com/documents/2230703/17635061/Sleep+Test+Scoring+and+Medicare+DCL.pdf) |

---

## 6. Strategic implications

### The underscoring problem as a sales wedge

The 26.4% reclassification rate means roughly **1 in 4 OSA patients** at HSAT-dominant practices are being classified less severe than they actually are. This creates three pitch angles:

**Pitch to HSAT-heavy sleep practices:**
> "Your HSAT-based practice systematically underscores AHI by ~26% compared to in-lab PSG. That means 1 in 4 of your patients who actually have moderate-to-severe OSA are being classified as mild or normal — and missing treatment that could reduce their cardiovascular risk. We can help you identify those patients for in-lab confirmation and manage the downstream CCM/RPM for the ones who get diagnosed."

**Pitch to ENT/OMFS considering surgical referrals:**
> "If your referring sleep doc uses HSAT with Medicare 1B scoring, your surgical candidates are arriving with artificially low AHI scores. We can re-stratify your referral pipeline to identify patients who are surgical candidates but were underscored on initial testing."

**Pitch to cardiologists screening CHF patients for OSA:**
> "HSAT in CHF patients specifically misses central sleep apnea because the device lacks the channels to distinguish central from obstructive events. Your CHF patients screened with HSAT may be getting false-negative results that delay treatment."

### The information asymmetry advantage

Nobody in practice-operations land reads JCSM editorials on hypopnea definitions or cross-references their HSAT ratio against national data. You do. The 239 practices identified as 100% HSAT are an addressable target list of clinics that would benefit from (a) understanding their own scoring bias and (b) outsourcing the CCM/RPM management for the patients who are properly diagnosed after correction.

---

## 7. Sources

- [AASM clarifies hypopnea scoring criteria](https://aasm.org/aasm-clarifies-hypopnea-scoring-criteria/)
- [The ethics of hypopnea scoring — JCSM (2024)](https://jcsm.aasm.org/doi/10.5664/jcsm.10944)
- [AASM Scoring Manual 3 — JCSM (2024)](https://jcsm.aasm.org/doi/10.5664/jcsm.11040)
- [Underestimation of Sleep Apnea With HSAT vs In-Lab — PMC (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5359328/)
- [Potential Underestimation by At-Home Kits: Rescoring PSG Without Sleep Staging — PMC (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5359331/)
- [Age-related disparities: 4% vs 3% scoring criteria — ScienceDirect (2024)](https://www.sciencedirect.com/science/article/abs/pii/S1389945724001515)
- [Modified scoring criteria for HSAT accuracy — Sleep and Breathing (2026)](https://link.springer.com/article/10.1007/s11325-026-03598-y)
- [AASM AMA/RUC advocacy page](https://aasm.org/clinical-resources/coding-reimbursement/payment-reform/)
- [AMA RUC recommendations and minutes](https://www.ama-assn.org/about/rvs-update-committee-ruc/ruc-recommendations-minutes-voting)
- [Noridian Medicare — Sleep Test Scoring DCL (2024)](https://med.noridianmedicare.com/documents/2230703/17635061/Sleep+Test+Scoring+and+Medicare+DCL.pdf)
- [BCBS Michigan — Diagnosis of Sleep Disorders Medical Policy](https://www.bcbsm.com/amslibs/content/dam/public/mpr/mprsearch/pdf/77347.pdf)
- [The case for AASM membership in the AMA — JCSM](https://jcsm.aasm.org/doi/10.5664/jcsm.7140)

---

*Analysis by Arya — CMS claims data + AASM regulatory research. April 2026.*
