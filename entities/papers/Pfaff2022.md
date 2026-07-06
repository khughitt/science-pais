---
id: paper:Pfaff2022
kind: paper
title: 'Identifying who has long COVID in the USA: a machine learning approach using
  N3C data'
status: active
ontology_terms:
- long COVID
- post-acute sequelae of SARS-CoV-2
- computable phenotype
- machine learning
- XGBoost
- N3C
- RECOVER
- electronic health records
- OMOP
- healthcare utilization
- ascertainment bias
dataset_usage: []
source_refs:
- cite:Pfaff2022
related:
- paper:Hill2022
- paper:Brannock2023
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
created: '2026-07-01'
updated: '2026-07-01'
---

# Identifying who has long COVID in the USA: a machine learning approach using N3C data

- **Authors:** Emily R Pfaff, Andrew T Girvin, Tellen D Bennett, Abhishek Bhatia, Ian M Brooks,
  Rachel R Deer, Jonathan P Dekermanjian, Sarah Elizabeth Jolley, Michael G Kahn, Kristin Kostka,
  Julie A McMurry, Richard Moffitt, Anita Walden, Christopher G Chute, Melissa A Haendel,
  and The N3C Consortium
- **Year:** 2022
- **Journal:** The Lancet Digital Health
- **Volume/Issue/Pages:** 4(7):e532-e541
- **DOI:** 10.1016/S2589-7500(22)00048-6
- **PMID:** 35589549
- **PMC:** PMC9110014
- **BibTeX key:** Pfaff2022
- **Source:** Europe PMC full text (XML)

## Key Contribution

Pfaff2022 introduced the primary machine-learned PASC computable phenotype for the N3C/RECOVER
infrastructure: three XGBoost models trained on long-COVID specialty-clinic attendance as a silver
standard, producing a continuous probability score over structured EHR data inside the N3C Data
Enclave. This established the "potential long COVID" flag used in many downstream N3C studies
(including Brannock2023) and remains the canonical N3C ML phenotype. Its central methodological
bet is that clinic attendance is a tractable proxy for long COVID in the absence of a consensus
clinical definition, and that the learned model can then be applied to patients who lack clinic
access.

## Narrow Extraction: BC-5 Feasibility Focus

### 1. Exact Phenotype Definition

**Algorithm:** XGBoost (Python `xgboost` package), hyperparameters tuned with `GridSearchCV`
(scikit-learn), 10-fold cross-validation repeated five times, optimising AUROC.

**Three models** trained separately:
- All-patients model
- Hospitalised patients model
- Non-hospitalised patients model

**Training label (silver standard):** Patients who attended a long COVID specialty clinic at least
once, curated from three N3C sites (n=597 patients meeting base population criteria). Called "long
COVID clinic patients" — explicitly not a true gold standard.

**Base population entry criteria:** Non-deceased adults (≥18 years) with either (a) ICD-10-CM
U07.1 (COVID-19 diagnosis code) from an inpatient or emergency visit, or (b) a positive SARS-CoV-2
PCR or antigen test, AND ≥90 days elapsed since COVID-19 index date (earliest positive indicator).
Full base population: n=1,793,604. Training/testing subset (3-site only): n=97,995.

**Output:** A continuous **probability score** (0 to 1), not a binary flag. The threshold is
adjustable per use-case.

**Recommended threshold:** 0.45, chosen to slightly favour recall over precision.

**Features:** 924 features total, drawn from:
- Healthcare visit rates (outpatient, inpatient) — continuous
- Age — continuous
- Diagnoses newly occurring or occurring at higher frequency in post-COVID window — binary
- Medications newly prescribed post-COVID — binary
- Categorical variables one-hot encoded

A 45-day buffer before and after the COVID-19 index date is excluded to separate acute illness from
pre/post windows; post-COVID data are only counted up to 365 days post-index.

### 2. Performance

**Internal validation (3-site test set, class-balanced sampling):**

| Model | AUROC | Precision (threshold 0.45) | Recall (threshold 0.45) |
|---|---|---|---|
| All patients | 0.92 | 0.85 | 0.86 |
| Hospitalised | 0.90 | not reported | not reported |
| Non-hospitalised | 0.85 | not reported | not reported |

**External validation (independent 4th site, n=32,411; 125 long COVID clinic patients; NO
class-balancing applied):**

| Model | AUROC |
|---|---|
| All patients | 0.82 |
| Hospitalised | 0.79 |
| Non-hospitalised | 0.78 |

The AUROC drop from internal (0.92) to external (0.82) for the all-patients model indicates
meaningful site-to-site variability. Sensitivity and specificity at the 0.45 threshold for the
external validation site are not reported separately in the main text.

The silver standard against which all performance is measured is **long-COVID clinic attendance**,
not U09.9 and not a patient-reported survey instrument. PPV/NPV values in a real-world
(class-imbalanced) setting are not directly provided.

### 3. EHR-Computability

**Fully computable from OMOP structured EHR data inside the N3C Data Enclave.** No survey, no
patient-reported outcomes, no clinical notes, no lab values (labs were evaluated but excluded as
too sparse, especially for non-hospitalised patients).

Required OMOP tables / feature classes:
- `condition_occurrence` — ICD-10-CM diagnosis codes (for COVID-19 entry criterion U07.1 and
  post-COVID condition features)
- `measurement` / `observation` — positive SARS-CoV-2 test (PCR or antigen; entry criterion)
- `visit_occurrence` — visit rates (outpatient, inpatient, emergency), used as continuous features;
  also the source of COVID-19 index date when U07.1 from inpatient/ED
- `drug_exposure` — newly prescribed medications (post-COVID window, no prior-period record)
- `person` — age (continuous), demographics (examined but race/sex NOT included as model features)

Code and model artifacts published to GitHub (`NCTraCSIDSci/n3c-longcovid`).

### 4. Coding-Drift / Ascertainment Profile

**U09.9 independence:** The model does NOT use U09.9 (post-COVID condition) as a feature or
outcome. U09.9 was not yet in widespread use when this study was conducted (published May 2022;
U09.9 activated October 2021). The training label is long-COVID clinic attendance, not any billing
code. This is a key architectural difference from the Hill2022 phenotype (which used U09.9 OR
clinic visit).

**Healthcare-utilisation confounding (critical bias concern):** Outpatient visit rate is the
**single most important Shapley-ranked feature** in all three models. The paper explicitly
acknowledges this dual interpretation: patients who remain unwell visit providers more often, but
the model cannot distinguish health-seeking behaviour from disease severity. Because the training
label is itself clinic attendance — a utilization-dependent event — the phenotype structurally
favours high utilisers. This is a known, acknowledged limitation.

**Long-COVID clinic access as ascertainment filter:** The silver standard selects patients who (a)
had COVID-19, (b) remained unwell, AND (c) accessed a specialty long-COVID clinic. Patients with
equivalent symptom burden but no clinic access are structurally absent from positive labels. The
authors explicitly name this as a motivation for the ML approach — the model is meant to recover
those patients — but the training signal is still clinic-derived.

**Site-specific clinic speciality bias:** Two of the three long-COVID clinic sites that contributed
training labels are pulmonary departments. This propagates a systematic respiratory feature bias
(dyspnoea, cough, albuterol, inhaled steroids) into Shapley-ranked top features. Authors
acknowledge this explicitly.

**Temporal / calendar-time considerations:**
- 6 N3C sites removed before analysis due to randomly shifted service dates.
- Base population requires positive COVID-19 indicator (U07.1 or positive test) — excludes patients
  who had COVID-19 early pandemic when testing was unavailable.
- No explicit analysis of model drift by calendar quarter or variant era.
- U09.9 was not available at time of study; models cannot be compared against coded diagnosis in
  the same dataset.

**Healthcare access inequity:** Authors name uninsured patients, patients at small community
practices, and those with limited ability to pay as systematically underrepresented in N3C data
and in the positive-label clinic population.

**Race/ethnicity:** Race was NOT included as a feature; the training cohort was not judged
adequately representative on race. Authors flag this as a known gap for future model versions.

### 5. Sex Handling

**Sex deliberately excluded as a model feature.** Race/ethnicity was also excluded. Stated reason:
the three-site long-COVID clinic sample (n=597) was "not appropriately representative" for
demographic features. No sex-specific AUROC, sensitivity, or specificity values are reported.

**Sex distribution in training data:**
- Non-hospitalised long COVID clinic patients: 75.1% female vs 59.8% female among non-clinic
  non-hospitalised patients — marked female overrepresentation in the positive non-hospitalised
  label.
- Hospitalised long COVID clinic patients: 55.4% female vs 55.7% female among non-clinic
  hospitalised — similar proportions.

The female overrepresentation in the non-hospitalised silver-standard group means that model
features implicitly encode some sex signal (conditions and utilisation patterns more common among
women who attend long-COVID clinics), even though sex itself is excluded. Sex-stratified
performance evaluation was not conducted and is an unresolved gap.

### 6. Relationship to U09.9 and RECOVER Survey-Based PASC Index

**vs U09.9:** The Pfaff2022 phenotype is architecturally independent of U09.9. It predates
widespread U09.9 coding, uses clinic attendance as label, and explicitly aims to identify patients
who "might not have access to a long COVID clinic" — the opposite of U09.9's role as a
clinician-coded diagnosis. In Hill2022 (the other N3C N3C paper in this project), U09.9 and clinic
visits are combined as a broader outcome; Pfaff2022's outcome is narrower (clinic only) but its
inference target is broader (any COVID patient with matching EHR fingerprint).

**vs RECOVER survey-based PASC index (Thaweethai2023):** The Thaweethai2023 PASC index was
published in 2023, after this paper. Pfaff2022 does not reference it. The two instruments differ
fundamentally: Thaweethai2023 derives a symptom-based score from patient-reported survey data in
a prospective cohort; Pfaff2022 derives a probability score from structured EHR data in a
retrospective observational cohort. They are complementary and non-interchangeable: the Pfaff
phenotype is EHR-computable at scale; the RECOVER survey index captures symptoms not coded in EHR.

**Within the N3C/RECOVER context:** Pfaff2022's all-patients model was applied to 846,981 patients
meeting base criteria (at least one post-COVID healthcare visit with ≥1 diagnosis or medication) to
generate a nationwide "potential long COVID" flag. This flag is the primary ML-based outcome
definition used in downstream N3C studies, including Brannock2023.

## Methods

- **Design:** Retrospective observational ML model development, N3C Data Enclave (OMOP harmonised
  EHR, 65 US sites, >8 million patients).
- **Training data:** 97,995 patients from 3 N3C sites with long-COVID clinic lists; sub-split into
  hospitalised (n=19,368) and non-hospitalised (n=78,627); further filtered to those with ≥1
  post-COVID visit and ≥1 diagnosis or medication (n=15,621 hospitalised, n=58,351 not).
- **Positive labels:** 597 patients who attended a long COVID specialty clinic ≥1 visit.
- **Temporal windows:** Pre-COVID (before 45-day buffer), post-COVID (after 45-day buffer, up to
  365 days post-index); data at/after first clinic visit excluded for positive-label patients to
  avoid label leakage.
- **Model:** XGBoost with GridSearchCV hyperparameter tuning, 10-fold CV × 5 repeats, AUROC
  optimisation; 924 features (one-hot + continuous).
- **Feature importance:** Shapley values (SHAP); reviewed by clinical experts.
- **Validation:** 4th-site holdout (n=32,411; 125 long COVID clinic patients).
- **Application:** All-patients model applied to n=846,981 (full N3C base population with ≥1
  post-COVID visit and ≥1 diagnosis or medication) to generate nationwide potential long COVID
  probability scores.

## Key Findings

- All three XGBoost models achieve high internal AUROC (0.85–0.92); external validation AUROCs
  are lower (0.78–0.82), indicating real site-to-site variability.
- Threshold 0.45 yields precision=0.85, recall=0.86 for the all-patients model (class-balanced
  test set); true PPV in unbalanced clinical populations is expected to be substantially lower.
- **Top Shapley-ranked features (all-patients model):** outpatient visit rate, patient age,
  dyspnoea, COVID-19 vaccination after acute disease (protective, decreases probability), dyssomnia,
  chest pain, malaise.
- Post-COVID vaccination is among the most important features across all models and decreases the
  predicted probability of long COVID — consistent with Brannock2023's vaccination-protective
  finding.
- Healthcare utilisation rate (outpatient visits) dominates feature importance; the model
  structurally captures who keeps seeking care, not independently of that signal.
- Race/ethnicity and sex were deliberately excluded as features; lab values excluded as too sparse.

## Relevance

This paper provides the primary **machine-learned computable phenotype** for N3C-based PASC
studies. For the BC-5 autoimmune × sex × PASC feasibility check, the key implications are:

1. **Outcome definition option:** The Pfaff2022 probability score (thresholded at 0.45) is one of
   the two main PASC outcome definitions available in N3C, alongside the Hill2022 coded definition
   (U09.9 or clinic visit). They are not interchangeable — Pfaff2022's positive labels require
   EHR-visible post-COVID healthcare activity; Hill2022's include any U09.9 code.

2. **Utilisation confounding (critical for sex analysis):** Because outpatient utilisation rate is
   the #1 feature, a sex × PASC association using this phenotype will partially reflect sex
   differences in healthcare-seeking behaviour, not purely in PASC biology. Women's higher baseline
   primary-care utilisation could artificially inflate their predicted probability relative to men
   with equivalent symptom burden.

3. **Ascertainment by sex:** The non-hospitalised positive-label pool is 75% female. Model features
   are calibrated on a female-predominant "long COVID" fingerprint for the non-hospitalised stratum.
   Sex-stratified performance was not evaluated. This is a bias concern for any sex-comparative
   downstream analysis.

4. **No U09.9 dependency:** A key advantage for studies beginning before widespread U09.9 adoption
   or spanning the pre/post U09.9 era — the Pfaff phenotype is calendar-time stable in that
   dimension, though it may still drift as site-level coding and care-seeking patterns change.

Links to `hypothesis:0008` (ascertainment bias shapes apparent PAIS group differences): the
utilisation-driven feature structure of this phenotype is a concrete instantiation of h0008's
measurement-channel concern.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Long COVID clinic attendance (silver standard) | PASC case definition | Utilization-dependent; not interchangeable with U09.9 or survey PASC |
| XGBoost predicted probability | PASC outcome variable | Continuous score; binary at threshold 0.45 |
| Outpatient visit rate (top feature) | Healthcare utilisation as ascertainment proxy | Core h0008 concern |
| Race/sex excluded as features | Demographic fairness gap | Sex-stratified performance unknown |
| 4th-site external validation AUROC drop | Site-to-site generalisability | 0.92 → 0.82 for all-patients |
| "Potential long COVID" label | N3C ML phenotype | Applied to 846,981 patients nationwide |

## Limitations

- **Silver standard, not gold:** Training label is long-COVID clinic attendance — a
  utilization-dependent, specialty-access-dependent proxy. Patients with equivalent disease but no
  clinic access are absent from positive labels.
- **Utilisation circularity:** Outpatient visit rate is the top feature AND the training label
  (clinic attendance) is itself a utilisation event. The phenotype cannot fully decouple symptom
  burden from care-seeking behaviour.
- **Pulmonary site bias:** Two of three training sites are pulmonary clinics, inflating importance
  of respiratory features. Underrepresents non-respiratory PASC phenotypes (autonomic, cognitive,
  fatigue-dominant).
- **Sex not a feature; no sex-stratified performance:** Female overrepresentation in the
  non-hospitalised positive labels is not corrected for. Unknown whether model sensitivity/
  specificity differs by sex.
- **Race/ethnicity excluded:** Model not evaluated for differential performance by race.
- **No lab or NLP features:** Misses biomarker and symptom-note signals available in EHR.
- **Calendar time / variant era:** No analysis of model drift by time period. Pre-test era
  patients excluded. U09.9 was not available at time of study.
- **External validation AUROC drop:** 10-point AUROC decline on 4th-site holdout suggests
  site-specific overfitting to the three training sites.
- **PPV in real populations:** At 0.45 threshold, the paper reports precision in class-balanced
  test sets. True PPV in unbalanced populations (where PASC is a minority) will be substantially
  lower; the paper explicitly acknowledges "non-trivial false positives."
- **No comparison to U09.9 or survey PASC index:** The paper was written before Thaweethai2023;
  no concordance analysis between phenotype channels exists in this paper.

## Model / Tool Availability

- **GitHub:** `https://github.com/NCTraCSIDSci/n3c-longcovid` — code and future model iterations
- **Data environment:** N3C Data Enclave (NCATS); requires institutional IRB-approved protocol
  and data use request; DACO-gated access
- **Reproducibility:** All analysis code available within the N3C Enclave to credentialed users
- **License:** Not specified in main text [UNVERIFIED from supplementary]

## Follow-up

- Compare Pfaff2022 ML phenotype with Hill2022 U09.9-or-clinic definition on the same N3C cohort
  to estimate concordance, discordance, and who is captured by each but not the other.
- Evaluate sex-stratified AUROC for the Pfaff2022 model on held-out N3C data — critical gap for
  the BC-5 autoimmune × sex × PASC analysis.
- Check whether post-2022 N3C studies (e.g. using RECOVER data) have retrained or updated this
  model with U09.9 labels or survey-derived labels as a ground truth.
- Consult GitHub repository for later model versions incorporating non-hospitalised subtype
  refinements or updated training labels.
- See Brannock2023 for a downstream use of both phenotype channels (coded diagnosis cohort and
  this ML phenotype cohort) in the same vaccination study.
