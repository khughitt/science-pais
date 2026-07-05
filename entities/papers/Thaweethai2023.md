---
id: "paper:Thaweethai2023"
kind: "paper"
title: "Development of a Definition of Postacute Sequelae of SARS-CoV-2 Infection"
status: "active"
paper_kind: ""
ontology_terms:
  - PASC
  - long COVID
  - case definition
  - symptom score
  - LASSO
  - RECOVER cohort
  - patient-reported outcomes
  - postexertional malaise
  - loss of smell and taste
  - research definition
  - symptom index
source_refs:
  - cite:Thaweethai2023
related:
  - paper:Pfaff2022
  - paper:ZhangRECOVEREHR2026
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: "2026-07-01"
updated: "2026-07-01"
---

# Development of a Definition of Postacute Sequelae of SARS-CoV-2 Infection

<!--
- **Authors:** Thaweethai T, Jolley SE, Karlson EW, Levitan EB, Levy B, McComsey GA, McCorkell L, Nadkarni GN, Parthasarathy S, Singh U, Walker TA, and the RECOVER Consortium
- **Year:** 2023
- **Journal:** JAMA
- **Volume/Pages:** 329(22):1934–1946
- **DOI:** 10.1001/jama.2023.8823
- **PMID:** 37278994
- **PMCID:** PMC10214179
- **BibTeX key:** Thaweethai2023
- **Source:** Abstract (Europe PMC) + PMC full text (open access) + targeted web search for scoring table
-->

## Key Contribution

The RECOVER Consortium developed the first prospective, data-driven research definition of PASC in adults, constructed as a weighted symptom-score index derived from patient-reported survey data (not EHR codes). Twelve to thirteen symptoms were selected via a two-stage LASSO approach from a 44-symptom PRO survey administered at ≥6 months post-infection; a score ≥12 defines PASC positive for research purposes. This index is the canonical "RECOVER-Adult research definition" and is explicitly distinguished from EHR-coded U09.9 (clinical), from the Pfaff 2022 [@Pfaff2022] N3C machine-learned EHR phenotype, and from the WHO/CDC clinical case-definition timing windows.

## Methods

**Design:** Prospective observational cohort (RECOVER-Adult).

**Setting:** 85 enrolling sites (hospitals, health centers, community organizations) in 33 US states, Washington DC, and Puerto Rico.

**Participants:** 9,764 adults meeting selection criteria (enrolled before April 10, 2023): 8,646 SARS-CoV-2 infected (89%) and 1,118 uninfected comparators (11%). Median age 47 years (IQR 35–60); 71% female overall (72% female among infected); 16% Hispanic/Latino; 15% non-Hispanic Black.

**Enrollment timing:** Both acute (enrolled ≤30 days post-index) and post-acute (>30 days to 3 years post-index) enrollees included. Symptom survey administered at a visit ≥6 months after acute symptom onset or first positive test date.

**Symptom ascertainment — PRO, not EHR:** All symptoms were assessed via standardized self-report questionnaires developed with patient-representative input, administered through the RECOVER study protocol. The authors explicitly contrast their approach with "electronic health records and most existing cohort studies," stating their data "captured PASC-specific self-reported symptoms based on standardized questionnaires." The 44-item survey included severity thresholds for each symptom.

**Two-stage selection:**
1. Adjusted odds ratios (aOR) were computed for each of the 44 surveyed symptoms comparing infected vs. uninfected participants; 37 symptoms reached aOR ≥1.5.
2. LASSO penalized regression was applied to the 37-symptom candidate set to select a parsimonious subset for the composite PASC score.

**PASC score construction:** Symptom-specific weights (integer-rounded point values derived from LASSO coefficients) are summed to produce a continuous PASC score. PASC positive is defined as a score **≥12**. The complete symptom weights are:

| Symptom | Points |
|---|---|
| Loss of or change in smell or taste | 8 |
| Post-exertional malaise (PEM) | 7 |
| Chronic cough | 4 |
| Brain fog | 3 |
| Unusual thirst | 3 |
| Palpitations | 2 |
| Chest pain | 2 |
| Fatigue | 1 |
| Changes in sexual desire or capacity | 1 |
| Dizziness | 1 |
| Gastrointestinal symptoms | 1 |
| Abnormal movements | 1 |
| Hair loss | 1 [UNVERIFIED — 13th symptom; the published abstract lists 12 symptoms and does not name hair loss; secondary studies citing the index consistently include it; confirmed in the existing project BibTeX note] |

Maximum possible score: 35 (with hair loss) or 34 (without).

## Key Findings

**PASC prevalence:**
- Among all infected participants: 1,990/8,646 (23%) PASC positive; among uninfected: 41/1,118 (3.7%) — but this comparison is strongly affected by volunteer/convenience sampling (see Limitations).
- More selection-bias-resistant estimate: among 2,231 participants infected on or after December 1, 2021 (Omicron era) and enrolled within 30 days of infection, **224 (10%; 95% CI 8.8–11%)** were PASC positive at 6 months. This is the paper's headline prevalence figure.

**Symptom burden in PASC-positive individuals:** Most common symptoms among PASC-positive participants were PEM (87%), fatigue (85%), brain fog (64%), dizziness (62%), GI symptoms (59%), and palpitations (57%).

**Vaccination effect:** Consistent with prior data, vaccination was associated with reduced PASC prevalence, though the study was not designed as a controlled vaccine-efficacy trial.

**Sex:** The cohort was 71% female and 72% female among infected participants. Female sex was associated with higher risk of PASC, though sex-stratified prevalence estimates with CIs are [UNVERIFIED — not reported in the publicly accessible main text; may be in supplementary materials].

## Relevance

**For BC-5 (autoimmune × sex × PASC feasibility check) — central finding:** The RECOVER-Adult PASC index is **not EHR-computable**. Every symptom in the scoring rubric is a patient-reported survey item requiring administration of the RECOVER questionnaire. No structured EHR diagnosis code, lab value, or billing code maps onto this composite. An N3C EHR-based study cannot apply this index as a primary case definition without a linked PRO/questionnaire data source.

**Alternative definitions for N3C-based studies:**
- Pfaff 2022 [@Pfaff2022] (N3C) XGBoost phenotype: EHR-computable but a machine-learned approximation, not the RECOVER PRO index.
- U09.9 ICD-10-CM: clinician-coded, EHR-computable, but specificity-limited and under-captured.
- RECOVER-EHR (pediatric, Zhang 2026 [@ZhangRECOVEREHR2026]): uses U09.9 + symptom/condition codes, EHR-computable.

**Sex-related relevance:** The RECOVER-Adult study oversampled female participants (71%) and confirmed female predominance in PASC. However, sex-stratified PASC rates are not prominently reported, and the scoring system was not developed with sex-stratification or sex-specific coefficients — a potential limitation for sex-mechanism studies.

**Hypothesis linkage:**
- `hypothesis:0008` (ascertainment bias shapes apparent PASC prevalence): The volunteer-enrollment design and PRO-only capture are directly relevant; ascertainment bias substantially inflates the 23% prevalence estimate relative to the 10% Omicron-cohort figure.
- `hypothesis:0005` (reproductive-stage effect): The female-predominant cohort provides epidemiological context but this paper's design does not test hormonal mediators.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PASC index (score ≥12) | RECOVER-Adult research definition | Distinct from U09.9, N3C phenotype, WHO/CDC clinical definitions |
| 44 PRO survey symptoms | Patient-reported outcome (PRO) instrument | Not equivalent to EHR problem-list entries |
| LASSO-selected 12–13 symptoms | Symptom cluster / case-definition components | Weights encode relative discriminative power |
| Uninfected comparator arm | Unexposed control group | 11% of cohort; lower prevalence floor (3.7%) vs infected (23%) |
| ≥6 months post-infection survey | Assessment window | Longer than WHO (≥2 months) or CDC (≥4 weeks) |

## Limitations

**Author-stated:**
1. The definition is explicitly provisional — a "first step to providing a framework for other investigations"; the authors call for "iterative refinement that further incorporates other clinical features" before it can support "actionable definitions."
2. Mixed enrollment strategy (population-based, volunteer, convenience) introduced selection bias. The 23% PASC prevalence in all infected participants over-represents individuals who sought out the study due to persistent symptoms. The authors recommend the 10% Omicron-cohort figure as less biased.
3. Symptoms are self-reported; no objective biomarker or clinician-examination component in the index itself.
4. Definition was developed in the RECOVER cohort demographic and care context; generalizability to other populations (international, different healthcare access, different vaccination histories) is unestablished.
5. The definition does not incorporate objective clinical features, EHR data, or biomarkers — "iterative refinement" is explicitly anticipated.

**For BC-5 reuse:**
- **EHR-computability: none.** The index requires the RECOVER questionnaire or a validated equivalent. It cannot be reconstructed from ICD codes, CPT codes, lab results, or vital signs in any EHR dataset including N3C.
- The timing window (≥6 months at survey) is more restrictive than clinical definitions; studies using the RECOVER PRO index will systematically exclude cases with symptom resolution before 6 months.
- Hair-loss inclusion is uncertain (abstract lists 12 symptoms; most secondary sources list 13). This introduces minor ambiguity in score replication across studies.

**Timing window vs WHO/CDC:**
- **This index:** Operational threshold ≥30 days post-infection; assessed at ≥6 months post-infection.
- **WHO (2021):** Symptoms present ≥3 months post-infection, lasting ≥2 months, not explained by alternative diagnosis.
- **CDC (clinical guidance):** Symptoms present ≥4 weeks post-infection.
- The RECOVER assessment window (≥6 months) captures a subset of the CDC/WHO population and is more conservative.

## Model / Tool Availability

The PASC score calculator is described in Supplement 1 of the paper. As of 2023, RECOVER made a web-based calculator available for research use. No proprietary software required; the score is a simple integer sum using the weights in the table above.

## Follow-up

- Pfaff 2022 [@Pfaff2022] (`paper:Pfaff2022`) — the complementary N3C EHR-based XGBoost long-COVID phenotype; must be compared when choosing a case definition for EHR studies.
- ZhangRECOVEREHR2026 (`paper:ZhangRECOVEREHR2026`) — RECOVER pediatric EHR-coded PASC; illustrates U09.9-based approach.
- For BC-5 lock: the choice of case definition for the N3C autoimmune × sex study must use an EHR-computable vehicle (U09.9 or Pfaff 2022 [@Pfaff2022] phenotype), since the RECOVER PRO index is inapplicable to N3C without linked survey data.
- Future questions: Does the RECOVER cohort have linked biomarker/autoimmune data that could enable sex-stratified mechanistic sub-analyses? Does the 10% Omicron prevalence estimate hold in sex-stratified subgroups?
