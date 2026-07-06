---
id: paper:Zhang2022
kind: paper
title: Data-driven identification of post-acute SARS-CoV-2 infection subphenotypes
status: active
ontology_terms:
- post-acute sequelae of SARS-CoV-2 infection
- long COVID subphenotypes
- electronic health records
- probabilistic topic modeling
- machine learning clustering
- ICD-10 diagnosis codes
- clinical research network
- PAIS heterogeneity
dataset_usage: []
source_refs:
- cite:Zhang2022
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Data-driven identification of post-acute SARS-CoV-2 infection subphenotypes

- **Authors:** Hao Zhang, Chengxi Zang, Zhenxing Xu, Yongkang Zhang, Jie Xu, Jiang Bian, Dmitry Morozyuk, Dhruv Khullar, Yiye Zhang, Anna S. Nordvig, Edward J. Schenck, Elizabeth A. Shenkman, Russell L. Rothman, Jason P. Block, Kristin Lyman, Mark G. Weiner, Thomas W. Carton, Fei Wang, Rainu Kaushal
- **Year:** 2022 (published online 1 December 2022; print January 2023)
- **Journal:** Nature Medicine, vol. 29, no. 1, pp. 226–235
- **DOI:** 10.1038/s41591-022-02116-3
- **BibTeX key:** Zhang2022
- **Source:** PDF

## Key Contribution

This paper develops a data-driven machine-learning framework to decompose the heterogeneous clinical presentation of post-acute sequelae of SARS-CoV-2 infection (PASC) into four reproducible, biologically coherent subphenotypes using EHR data from 20,881 (development) and 13,724 (validation) patients across two large US clinical research networks. By applying probabilistic topic modeling (Poisson factor analysis) to 137 ICD-10-coded PASC-related diagnosis categories observed 30–180 days post-infection, then clustering patients in the resulting low-dimensional topic space, the study identifies four distinct multi-organ PASC subphenotypes — cardiac/renal, respiratory/sleep/anxiety, musculoskeletal/nervous, and digestive/respiratory — each with distinct patient demographics, acute illness severity, and medication prescription profiles. The four subphenotypes were validated on an independent geographically distinct cohort with >90% patient stability under bootstrap resampling (ARI 0.902, NMI 0.937), establishing that the heterogeneity of PASC is structured and reproducible at clinical scale.

## Methods

**Data sources and cohorts:**
- INSIGHT Clinical Research Network (CRN): ~12 million patients in the New York City area; development cohort of 20,881 SARS-CoV-2-positive adults (age ≥20).
- OneFlorida+ CRN: ~19 million patients mainly from Florida, Georgia, and Alabama; validation cohort of 13,724 SARS-CoV-2-positive adults.
- Both cohorts drawn from the PCORnet National Patient-Centered Clinical Research Network; both are part of the NIH RECOVER initiative.
- Eligibility: lab-confirmed SARS-CoV-2 (PCR or antigen) between 1 March 2020 and 30 November 2021; age ≥20; at least one baseline diagnosis in 3 years to 1 week pre-index; at least one new PASC diagnosis in the 30–180 day post-infection window.

**PASC condition set:** 137 diagnosis categories derived from ICD-10 codes mapped to Clinical Classification Software Refined (CCSR) categories, compiled via literature review and clinician input; further refined using a high-dimensional propensity-score adjustment pipeline to the 44 conditions with statistically significant excess risk in SARS-CoV-2-positive vs. matched SARS-CoV-2-negative patients (used for sensitivity analysis).

**Analytic pipeline (4 steps):**
1. Binary vector encoding: each of the N patients represented as a 137-dimensional binary vector (1 if a PASC condition newly appeared in the post-acute window, 0 otherwise).
2. Topic modeling (TM): Poisson Factor Analysis (PFA; implemented in Python package Pydpm v3.0.1, trained via Gibbs sampling with 500 burn-in steps, Q=500 collected samples) learned K=10 PASC topics — each a probability distribution over the 137 conditions representing a co-occurrence pattern. K was selected by maximizing validation data log-likelihood and topic coherence across K=2–20, with topic coherence measured using normalized pointwise mutual information (NPMI) via the GENSIM library.
3. Patient representation: each patient mapped to a K=10 dimensional continuous topic-loading vector θ_n (the degree to which each topic characterizes their post-acute record).
4. Subphenotype clustering: hierarchical agglomerative clustering (Euclidean distance, Ward linkage) applied to topic-loading vectors; optimal cluster count determined by NbClust R package (21 cluster quality indices; majority vote selected K=4 for both cohorts).

**Validation and robustness:**
- Bootstrap stability: 1,000 bootstraps with 80% random subsamples; ARI 0.902 (95% CI 0.863–0.927) and NMI 0.937 (95% CI 0.908–0.952) on INSIGHT; ARI 0.914, NMI 0.950 on OneFlorida+.
- Cross-cohort topic consistency: cosine similarity matrix between INSIGHT and OneFlorida+ topics showed one-to-one correspondence (diagonal cosine similarities: T1=0.94, T2=0.86, T3=0.96, T4=0.74, T5=0.95, T6=0.90, T7=0.74, T8=0.69, T9=0.71, T10=0.87).
- Comparison with SARS-CoV-2-negative matched controls: propensity-score-matched controls for demographics, ADI, index date, medical utilization, and baseline comorbidities confirmed PASC subphenotype conditions had higher co-incidence rates in positive vs. negative patients, with denser network hubs in positive subphenotypes.
- Sensitivity analysis: subphenotyping repeated on the restricted 44-condition set; >90% patient overlap with 137-condition subphenotypes.

**Comparators:** SARS-CoV-2-negative patients who visited hospitals between March 2020 and November 2021 but tested negative, matched 1:1 per subphenotype using propensity scoring plus robust PS pipeline.

**Statistical analysis:** All analyses in Python 3.7; scikit-learn-0.23.2, numpy-1.16.5, umap-learn-0.5.1, Pydpm-3.0; scipy-1.7.3.

## Key Findings

**Four reproducible PASC subphenotypes (INSIGHT / OneFlorida+ N, %)**

**Subphenotype 1 — Cardiac and Renal (7,047 / 3,492; 33.75% / 25.43%)**
- Dominated by topics including cardiac arrhythmias, heart failure, circulatory conditions, renal failure, anemia, and fluid/electrolyte disorders.
- Oldest patients: median age 65.0 years (IQR 52.0–75.0) on INSIGHT; 62.0 years on OneFlorida+.
- Highest proportion of males: 48.53% on INSIGHT; 46.93% on OneFlorida+ (vs. 38.29% overall).
- Highest acute illness severity: hospitalization 61.15%, mechanical ventilation 4.81%, critical care 9.95% on INSIGHT.
- Most prevalent in March–June 2020 (first COVID-19 wave, NYC epicenter): 37.38% of this subphenotype infected in that wave.
- Highest burden of pre-existing cardiovascular, blood, and endocrine comorbidities. Highest incident prescription rates for circulatory, blood, and endocrine medications in the post-acute period.

**Subphenotype 2 — Respiratory, Sleep and Anxiety (6,838 / 5,281; 32.75% / 38.48%)**
- Largest subphenotype on OneFlorida+; dominated by upper/lower respiratory conditions, sleep-wake disorders, anxiety/fear-related disorders, headache, chest pain.
- Youngest of the two large subphenotypes: median age 51.0 years (IQR 35.0–64.0) on INSIGHT; 47.0 years on OneFlorida+.
- Highest female representation: 62.80% female on INSIGHT.
- Most patients infected during November 2020–February 2021 (44.11% on INSIGHT): this wave followed the early pandemic and represented different variant/treatment landscape.
- Higher pre-existing burden of COPD, pneumonia, and upper respiratory tract conditions. Higher post-acute prescriptions for respiratory medications (anti-asthma, anti-allergy, anti-inflammatory, inhaled steroids, levalbuterol, montelukast).

**Subphenotype 3 — Musculoskeletal and Nervous (4,879 / 3,205; 23.37% / 23.35%)**
- Dominated by musculoskeletal pain, headache, sleep-wake disorders, spondylopathies, connective tissue disease, other nervous system conditions, and dermatological conditions.
- Median age 57.0 years (IQR 42.0–69.0); 60.71% female on INSIGHT.
- Highest proportion with >5 pre-COVID outpatient visits (78.4%): the most healthcare-engaged group at baseline.
- Highest baseline autoimmune burden: rheumatoid arthritis, asthma, and other musculoskeletal/connective tissue/nervous system conditions. Also highest baseline prevalence of skin and subcutaneous conditions.
- Hospitalization 38.02%, mechanical ventilation 1.11%, critical care 3.57% on INSIGHT — moderate acute severity.
- Highest post-acute prescriptions for pain medications (ibuprofen, ketorolac); higher prescriptions for skin-related medications.

**Subphenotype 4 — Digestive and Respiratory (2,117 / 1,748; 10.14% / 12.74%)**
- Smallest subphenotype; dominated by digestive system conditions (gastrointestinal disorders, gastritis/duodenitis, esophageal disorders, abdominal and pelvic pain, nausea/vomiting), combined with some respiratory conditions.
- Youngest patients: median age 54.0 years (IQR 39.0–67.0) on INSIGHT; 46.0 years on OneFlorida+.
- Highest female proportion: 61.64% female on INSIGHT; 67.11% on OneFlorida+ (highest across all subphenotypes).
- Mildest acute severity: lowest hospitalization rate 33.3% on INSIGHT; mechanical ventilation 0.8%, critical care 2.79%. Lowest rates of mechanical ventilation (0.97%) and critical care admission (2.8%) on OneFlorida+.
- Highest rate of zero-baseline emergency visits (57.06%): least medically complex baseline.
- Higher pre-existing prevalence of digestive system conditions (hematemesis, stomach and duodenum disorders, digestive system neoplasm). More incident prescriptions for digestive medications in the post-acute period.
- Many conditions in this subphenotype (abdominal pain, nausea, esophageal disorders) are relatively subjective diagnoses, which the authors note likely encompass functional disorders rather than clear disease etiologies.

**Cross-subphenotype comparisons:**
- Subphenotype 1 patients had the highest overall PASC burden and were most likely to represent complications of severe acute COVID-19.
- Subphenotypes 2, 3, and 4 represent milder PASC that is less explained by alternative disease etiologies and more aligned with patient-reported symptoms.
- Sex was a significant stratifying variable across all subphenotypes (p=4.91×10⁻⁴⁶): Subphenotype 1 skewed male, Subphenotypes 3 and 4 skewed female.
- Age was a significant stratifying variable (p=0): Subphenotype 1 oldest, Subphenotype 4 youngest.
- All four subphenotypes covered the major PASC conditions confirmed in independent studies (cardiovascular, respiratory, neurological, gastrointestinal).

## Relevance

This paper directly addresses the project research question (research-question:post-acute-infection-syndromes) and the PAIS frame of failed homeostatic recovery by providing large-scale empirical evidence that PASC is not a single undifferentiated syndrome but a structured set of at least four distinct multi-organ failure modes. This structured heterogeneity is critical to the PAIS frame:

**1. PAIS as structured, not random, heterogeneity.** The finding that four coherent subphenotypes emerge from unsupervised analysis of 34,605 patients' post-acute diagnoses — and replicate across two geographically distinct cohorts — demonstrates that the clinical manifestations of failed homeostatic recovery after SARS-CoV-2 infection are not arbitrary. Each subphenotype likely reflects a distinct pathophysiological mechanism or pre-existing vulnerability that biases the recovery failure mode. This is foundational for any mechanistic or computational investigation of PAIS.

**2. Pre-existing biology shapes PAIS failure mode.** The strong association between subphenotype membership and pre-infection comorbidities (cardiovascular for Subphenotype 1; respiratory for Subphenotype 2; autoimmune/musculoskeletal for Subphenotype 3; digestive for Subphenotype 4) demonstrates that PAIS is not purely a consequence of viral damage but is shaped by host vulnerability — consistent with the immune homeostasis frame from the peer project (health-immunity). Patients who could not maintain homeostasis in a given organ system before infection were more likely to fail to recover it afterward.

**3. Acute severity is not the primary determinant of most PAIS.** Subphenotypes 2, 3, and 4 together comprise ~66% of patients and show moderate-to-mild acute severity. The large Subphenotype 2 (respiratory/anxiety/sleep) with low mechanical ventilation rates (1.24%) but dominant symptom burden represents a clinically significant PASC population whose conditions are not reducible to severe acute illness complications. This challenges a naive "PASC = severe COVID sequela" framing.

**4. Demographic patterning (sex, age) as a biological clue.** The strong sex divergence — male-skewed Subphenotype 1 (cardiac/renal) vs. female-skewed Subphenotypes 3 and 4 (musculoskeletal/nervous and digestive) — mirrors known sex differences in autoimmune disease prevalence. The project notes (AGENTS.md) that immune phenotypes are highly sensitive to sex; these subphenotypes provide a large-scale clinical correlate for stratified mechanistic investigation.

**5. EHR-based clinical subphenotyping as a scalable PAIS characterization approach.** The PFA + clustering pipeline can, in principle, be applied to any PAIS dataset with sufficient ICD-10-coded longitudinal records. This positions the method as a computational scaffold for future cross-PAIS comparative studies (e.g., post-Q-fever, post-Lyme, post-EBV) if large EHR datasets exist — directly relevant to the project's computational analysis goal.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post-acute sequelae of SARS-CoV-2 infection (PASC) | post-acute infection syndrome (PAIS) — COVID-19 variant | Case definition: newly incident ICD-10 diagnoses 30–180 days post positive SARS-CoV-2 test; not self-reported symptom criteria |
| Four PASC subphenotypes (cardiac/renal, respiratory/sleep/anxiety, musculoskeletal/nervous, digestive/respiratory) | PAIS failure modes stratified by predominant organ system | Each subphenotype = a distinct pattern of homeostatic non-recovery after acute infection |
| Pre-existing comorbidity burden predicts subphenotype membership | host vulnerability as a determinant of PAIS failure mode | Consistent with homeostasis-threshold framing: organ systems already near failure threshold are most likely to fail to recover |
| Acute infection severity (hospitalization, ventilation, ICU) predicts Subphenotype 1 but not 2–4 | decoupling of PAIS from acute severity for most patients | Critical finding for the PAIS shared-failure-mode hypothesis: most PAIS is not just severe acute illness persistence |
| Topic modeling of ICD-10 co-occurrence patterns | unsupervised discovery of PAIS phenotypic structure | Poisson Factor Analysis extracts latent co-incidence structure from high-dimensional binary clinical data |
| PASC topics (10 topics, K=10) | latent disease axes driving PAIS presentation | Topics are interpretable: cardiac/circulatory, digestive, musculoskeletal, nervous, respiratory, electrolyte/endocrine clusters |
| Sex as a subphenotype stratifier (male-skewed Subphenotype 1, female-skewed Subphenotypes 3–4) | sex as a biological covariate in PAIS | Mirrors autoimmune sex bias; consistent with AGENTS.md guidance on sex as a key covariate |
| Comparison with SARS-CoV-2-negative matched controls | establishing PASC excess incidence above background | Rigorous comparison shows PASC conditions are not random post-illness diagnoses but excess relative to matched population |
| Validated across INSIGHT (NYC) and OneFlorida+ (FL/GA/AL) | PAIS subphenotype generalizability | Replication across different geography, demographics, and COVID wave timing strengthens clinical claim |
| CCSR diagnosis categories (ICD-10 mapped) | clinical phenotype taxonomy for PAIS | CCSR provides a publicly available, standardized clinical terminology useful for cross-dataset comparison |

## Limitations

- **EHR-based diagnosis codes, not patient-reported symptoms:** The study relies entirely on ICD-10 codes entered by clinicians. Conditions with subjective or inconsistent diagnostic criteria (e.g., abdominal pain, nausea, esophageal disorders in Subphenotype 4) may be systematically under- or over-coded. Patients with symptoms that do not generate healthcare encounters are invisible.
- **No biological mechanism validation:** The subphenotypes are clinically defined by co-occurring diagnoses. Whether each subphenotype corresponds to a distinct pathophysiological mechanism (e.g., immune dysregulation vs. direct organ injury vs. autonomic dysfunction) is not assessed; the paper explicitly states biological mechanism inference is a limitation.
- **Does not capture pre-existing condition persistence vs. new incidence precisely:** Although the authors required newly incident conditions (excluding any condition present in the baseline period), the distinction between a pre-existing condition worsening vs. a truly new post-COVID diagnosis may be imperfect in ICD-10 coding practice, particularly for chronic conditions.
- **Study period does not include Omicron:** Data span March 2020 to November 2021. Whether the four subphenotypes, their proportions, and demographic correlates generalize to the Omicron-dominated era (and post-vaccination PASC) is untested.
- **Geographic and demographic heterogeneity not fully controlled:** INSIGHT is NYC-centric; OneFlorida+ covers a different demographic mix (more White patients, lower ADI median, more patients infected during later waves). The cross-cohort robustness is demonstrated, but state-level healthcare-seeking behavior differences are not fully adjustable.
- **No predictive modeling performed:** The goal was subphenotype identification, not prediction. Whether subphenotype membership at 30 days can be predicted from acute phase features — enabling prospective triage — was explicitly left as future work.
- **30-day post-infection window excludes very early PASC symptoms:** The analysis begins at 30 days post-index date. Conditions presenting in the first 30 days post-acute phase are excluded, potentially missing early-onset PASC manifestations.
- **Propensity score matching for negative controls may not balance all confounders:** The PS pipeline adjusts for listed confounders (demographics, ADI, medical utilization, baseline comorbidities, index date window), but unmeasured confounders (e.g., socioeconomic factors beyond ADI, access to specialist care) could bias the excess incidence estimates.
- **No longitudinal trajectory data:** The study captures the 30–180 day window as a single observation period; it cannot distinguish patients who had symptoms for 30 days from those who had them for all 180 days, or whether conditions resolved vs. persisted beyond 180 days.

## Model / Tool Availability

- **Code:** Available at https://github.com/haozhangWCM/Subphenotyping-for-PASC (GitHub repository).
- **Software dependencies:** Python 3.7; scikit-learn 0.23.2, numpy 1.16.5, umap-learn 0.5.1, Pydpm 3.0 (for PFA topic modeling; https://pypi.org/project/pydpm/), scipy 1.7.3, GENSIM (for NPMI topic coherence).
- **Data:** INSIGHT data requires an approved study protocol (contact insightcrn@med.cornell.edu or https://nyc-cdrn.atlassian.net/servicedesk/customer/portal/2/group/6/create/16). OneFlorida+ data available with approved protocol (https://onefloridaconsortium.org/front-door/prep-to-research-data-query/). Source data provided with the paper at the DOI link.
- **No pre-trained models or pre-computed topic matrices** are deposited as standalone artifacts; the code must be retrained on approved EHR data.

## Follow-up

- **Mechanism behind each subphenotype:** What immunological, autonomic, or metabolic mechanisms underlie each of the four subphenotypes? Subphenotype 1 (cardiac/renal) likely reflects CRS/hyperinflammation + direct organ injury; Subphenotype 3 (musculoskeletal/nervous) may reflect autoimmune/neuroinflammatory mechanisms; Subphenotype 4 (digestive) may involve gut dysbiosis or gut-brain axis dysregulation. Mechanistic work (e.g., Ryan2022, Peluso2024) should be cross-referenced against these clinical clusters.
- **Cross-PAIS subphenotyping:** Would a similar PFA+clustering approach applied to post-Q-fever, post-Lyme, or post-dengue EHR data produce the same four subphenotypes? Convergence would strongly support the hypothesis that PAIS subphenotypes reflect conserved post-infectious pathophysiology rather than SARS-CoV-2-specific mechanisms.
- **Longitudinal subphenotype stability:** Do patients remain in the same subphenotype beyond 180 days, or do they transition between subphenotypes? A longitudinal extension would clarify whether the four clusters represent static states or dynamic recovery trajectories.
- **Sex-stratified mechanisms:** The strong female predominance of Subphenotypes 3 and 4 warrants mechanistic investigation into whether these reflect sex differences in autoimmunity susceptibility (HLA, hormonal regulation of immune response) or sex differences in healthcare-seeking behavior biasing ICD-10 coding.
- **Prediction of subphenotype from acute phase:** Can clinical features measurable at the time of acute COVID-19 infection (severity scores, inflammatory biomarkers, initial diagnoses) predict which subphenotype a patient will develop? This has direct clinical utility for early stratified intervention.
- **Validation with symptom-based criteria:** The EHR-based subphenotypes should be compared with symptom-cluster studies (e.g., Kenny et al. 2022, which identified distinct long COVID clinical phenotypes from self-reported symptoms in 233 patients) to assess concordance between diagnosis code-based and patient-reported subphenotyping approaches.
