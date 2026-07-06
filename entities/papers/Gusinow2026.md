---
id: paper:Gusinow2026
kind: paper
title: Latent transition analysis for longitudinal studies of post-acute infection
  syndromes
status: active
ontology_terms:
- latent transition analysis
- hidden Markov model
- post-COVID condition
- longitudinal cohort study
- disease phenotyping
- health-related quality of life
- symptom trajectory
- post-acute infection syndrome
dataset_usage: []
source_refs:
- cite:Gusinow2026
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Latent transition analysis for longitudinal studies of post-acute infection syndromes

- **Authors:** Roy Gusinow, Anna Gorska, Lorenzo Maria Canziani, Iris Lopes-Rafegas, Carolina Alvarez Garavito, Adriana Tami, Elisa Gentilotti, Elisa Sicuri, Cedric Laou??nan, Jade Ghosn, Aline-Marie Florence, Nadhem Lahfej, Fulvia Mazzaferri, Lidia Del Piccolo, Maddalena Giannella, Alice Toschi, Michela Di Chiara, Maria Giulia Caponcello, Zaira R. Palacios-Baena, Karin I. Wold, Elisa Rossi, Evelina Tacconelli, Jan Hasenauer (on behalf of the ORCHESTRA study group)
- **Year:** 2026
- **Journal:** Nature Communications, vol. 17, art. 2557
- **DOI:** 10.1038/s41467-026-68650-7
- **BibTeX key:** Gusinow2026
- **Source:** PDF

## Key Contribution

This paper introduces a generalisable Latent Transition Analysis (LTA) framework for the data-driven identification of disease phenotypes and patient-level trajectory modelling in longitudinal Post-Acute Infection Syndrome (PAIS) studies, without relying on predefined clinical categorisations. Applied to the ORCHESTRA Long-Term Sequelae Cohort (5,094 SARS-CoV-2 patients, 6-24 month follow-up across five European countries), the framework identifies seven distinct Post-COVID Condition (PCC) phenotypic states and shows that age, sex, infection wave, and comorbidities differentially shape both initial state membership and state-transition probabilities — producing quantified individual-level recovery trajectories and recovery time predictions. A key methodological advance is a parsimonious projection of patient covariates onto a low-dimensional scalar that modulates the full transition probability matrix, enabling large-covariate-set inference without combinatorial parameter explosion.

## Methods

- **Framework:** Latent Transition Analysis (LTA) built on Hidden Markov Models (HMMs) using a discrete-time, discrete-state formulation. Observations at each timepoint are modelled as emissions from latent health states, with covariate-dependent state transition probabilities inferred via maximum likelihood.
- **Observation types:** Joint modelling of binary symptom indicators (9 PCC-related symptoms: ageusia, anosmia, arthralgia, cough, dyspnoea, fatigue, headache, memory loss, myalgia) and continuous HRQoL scores (SF-36 physical and mental component scores, SF-36 scored using US 1998 norms, suboptimal threshold = 50).
- **Covariate incorporation:** Patient characteristics (age, sex, infection wave, comorbidities, treatment history, hospitalisation) are projected onto two low-dimensional scalar intermediary variables — one for initial state probabilities (p_initial) and one for transition probabilities (p_trans) — which then modulate the latent state distribution. This reduces the parameter space from >1,000 to a manageable number while preserving covariate interpretability.
- **Individual-level prediction:** A recursive Bayesian filtering step updates latent state probabilities at each timepoint using sequentially accumulated symptom and HRQoL observations, enabling patient-specific forecasts without full model re-estimation.
- **Model selection:** BIC-based selection over 4-8 state models; 7-state model selected as optimal. Fully connected HMM — no a priori constraints on transition structure.
- **Validation:** Comprehensive simulation-based validation study for parameter recovery, predictive performance, and covariate interpretability under controlled scenarios (varying data sparsity, symptom noise, covariate effects). Overfitting assessed via 5-fold cross-validation.
- **Cohort — ORCHESTRA Long-Term Sequelae Cohort:**
  - 5 prospective subcohorts from 56 centres across 4 countries (France, Italy, Netherlands, Spain)
  - 5,094 individuals with laboratory-confirmed SARS-CoV-2 infection, aged >14 years
  - Timepoints: acute infection (baseline), 6, 12, 18, and 24 months
  - 75.4% of participants hospitalised (general or ICU) at the acute stage — **not** representative of the general SARS-CoV-2-infected population
  - Complete 5-timepoint data: 419 patients; 12-month follow-up: 1,796 patients; 18-month: 2,120 patients; 24-month: 628 patients
  - Demographics: ~2,939 male, ~2,155 female (from age pyramid); median age roughly 50s
  - CT registration: NCT05097677
- **Software:** Open-source Julia implementation; available at https://doi.org/10.5281/zenodo.17787061

## Key Findings

### Seven Latent PCC States

The 7-state LTA model identifies two acute-phase-exclusive states and five persistent states:

| State | Label | Key emission features | HRQoL (Physical / Mental) |
|---|---|---|---|
| 1 | Acute Respiratory | Cough 74%, Dyspnoea 57%, Fatigue 54%, Headache 16% | Highly uncertain (no HRQoL at acute phase) |
| 2 | Acute Moderate | Cough 77%, Dyspnoea 60%, Fatigue 81%, Arthralgia 49%, Myalgia 91%, Headache 48% | Highly uncertain |
| 3 | Healthy | Fatigue <15%, all symptoms <10% | Physical ~57, Mental ~58 (above norm) |
| 4 | Sensorial PCC | Anosmia 81%, Ageusia 89% | Reduced physical, preserved mental HRQoL |
| 5 | Respiratory PCC | Fatigue 85%, Dyspnoea 43% (elevated vs healthy) | Physical 46.86, Mental 47.72 |
| 6 | Fatigue PCC | Fatigue 59%, broad intermediate symptom probabilities (30-60%) | Markedly reduced physical and mental HRQoL |
| 7 | Severe Symptoms | Nearly all symptoms >70%, Ageusia 95%, Anosmia 98% | SF-36 significantly compromised |

### Cohort-Level Trajectory Dynamics

- At 6 months, 32.6% of patients are in the Healthy state, rising to 39.2% at 24 months.
- The Respiratory PCC state declines from 41.5% at 6 months to 35.5% at 24 months, driving most of the recovery signal.
- Sensorial PCC (6.0%), Fatigue PCC (17.0%), and Severe Symptom (2.3%) states remain present at 24 months.
- Patients who enter Healthy, Respiratory PCC, Sensorial PCC, or Fatigue PCC states show high self-persistence over follow-up periods, with rare subsequent state transitions.

### Covariate Effects on Trajectories

Risk factors confirmed by LTA (all Wald-test significant, p < 0.05 two-sided, no multiple comparisons adjustment):
- **Female sex:** Increases probability of Respiratory PCC and Fatigue PCC states; worsening trajectory.
- **Age 41-60:** OR ~0.40 ± 0.36; age > 60: OR ~0.50 ± 0.45 — increased PCC risk.
- **Chronic respiratory disease:** OR ~0.33 ± 0.29 — increased PCC risk.
- **Third and fourth infection waves:** Significantly better recovery vs. first wave (effect estimates -0.35 ± 0.32 and -0.35 ± 0.33, respectively), consistent with variant attenuation and pre-existing immunity.
- **Corticosteroid use at acute infection:** OR 0.25 ± 0.23 — indicates worsening; in context, corticosteroids were given to patients with respiratory failure, so interpretability is limited (indication bias).

### Differential Recovery Time Predictions

Forward simulation on 1,000 model runs:
- Young men (ages 15-30, fourth wave): 72.2% probability of being in the Healthy state at 24 months.
- Women aged >60: 26.6% probability of being in the Healthy state at 24 months.
- Predicted median time-to-recovery from PCC states to Healthy:
  - Fourth-wave males: 20.81 months
  - Males aged >60: 54.76 months
  - Females aged >60: **89.46 months** (>7 years extrapolated)

### Predictive Performance

- Overall AUROC of 0.69 on the full ORCHESTRA dataset; 5-fold cross-validation mean AUROC = 0.65.
- Prediction accuracy improves monotonically as more longitudinal observations are incorporated (filtering update step), approaching ~80-90% of maximum achievable AUROC for most symptoms at 18-month update.

### Model Validation

- 1,000 model simulations reproduce observed symptom prevalence trajectories within 2x standard error for nearly all symptoms and timepoints.
- Physical (51-56%) and mental (60-65%) SF-36 component distributions reproduced accurately.
- PCA structure of observed vs. simulated data closely match, confirming latent mechanisms are captured.

## Relevance

This paper directly addresses the project research question (`research-question:post-acute-infection-syndromes`) at a methodological and empirical level, providing the most rigorous quantitative picture yet of within-patient PAIS trajectory dynamics.

**Alignment with the PAIS failed-homeostatic-recovery frame:**

1. **Quantifying the failure-to-recover population:** The LTA directly maps the project's core construct — "failed homeostatic recovery after acute infection" — onto a probabilistic latent state space. The Healthy state represents successful recovery; Fatigue PCC, Sensorial PCC, Respiratory PCC, and Severe Symptom states represent graded degrees of persistent homeostatic failure. At 24 months, ~60.8% of a hospitalised-enriched SARS-CoV-2 cohort remain in non-Healthy states, providing a quantitative estimate of the recovery failure burden.

2. **State persistence as a key failure-mode characteristic:** The high self-persistence probabilities for all PCC states — particularly Fatigue PCC and Sensorial PCC — directly reflect the project's framing of PAIS as a failure to exit the post-infectious dysregulated state, not merely a delayed but inevitable recovery. This supports the "attractor state" conceptualisation of PAIS pathophysiology.

3. **Sex and age as homeostatic-resilience modulators:** The dramatically differential recovery trajectories (females aged >60 requiring an extrapolated 89.46 months vs. 20.81 months for young fourth-wave males) quantify the biological vulnerability gradient predicted by the PAIS framework. Female sex, which dominates the PAIS literature across pathogens (long COVID, ME/CFS, post-dengue), here receives a trajectory-level mechanistic framing: not merely higher PAIS prevalence but fundamentally slower homeostatic restoration.

4. **Infection wave as a proxy for pathogen-host adaptation:** Later-wave infections show significantly better recovery rates, consistent with a model in which initial pathogen characteristics (viral tropism, replication kinetics, immune evasion profile) set the degree of acute homeostatic disruption that determines subsequent PAIS probability — aligning with the project's "acute insult severity as PAIS determinant" hypothesis.

5. **Phenotypic heterogeneity within shared failure:** The identification of four distinct persistent PCC states (Sensorial, Respiratory, Fatigue, Severe) from the same infected cohort demonstrates that PAIS is not a single failure mode but a family of failure modes, each with distinct symptom and HRQoL profiles. This is critical for the project's cross-PAIS comparative framework, because the same biological underpinnings could produce phenotypically distinct outcomes depending on which organ systems bear the brunt of homeostatic failure.

6. **Methodological contribution enabling PAIS research:** The LTA framework itself is a direct contribution to the project's research infrastructure. Its data-driven state inference without predefined case definitions circumvents the WHO PCC definition's imprecision while preserving temporal dynamics — a methodological advance for future computational analyses in this project.

7. **HRQoL as a continuous homeostasis metric:** The joint modelling of binary symptoms and continuous SF-36 scores operationalises health-related quality of life as a quantitative proxy for functional homeostasis — aligning with the project's interest in multi-modal outcome integration.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Healthy latent state (State 3) | Successful homeostatic recovery after SARS-CoV-2 | Characterised by <15% fatigue, <10% all other symptoms, SF-36 ≈ 57-58 |
| Fatigue PCC (State 6) | PAIS — chronic fatigue/energy deficit phenotype | Broadest symptom involvement; greatest HRQoL impairment; mirrors ME/CFS-like failure |
| Sensorial PCC (State 4) | PAIS — neurological/sensory phenotype | Anosmia/ageusia dominant; preserved mental HRQoL; may reflect distinct nerve-target recovery failure |
| Respiratory PCC (State 5) | PAIS — cardiorespiratory phenotype | Fatigue + dyspnoea; mildly impaired HRQoL; most prevalent persistent state |
| Severe Symptoms (State 7) | PAIS — severe/multi-system failure mode | Low prevalence (2.3% at 24 months); analogue to severe ME/CFS or multi-system inflammatory failure |
| State self-persistence probabilities | Attractor-state failure mode | High persistence = difficulty escaping pathological equilibrium = homeostatic failure |
| Transition probability modulation by covariates | Risk/resilience modifier of homeostatic trajectory | Quantified at individual level via scalar projection |
| p_trans scalar (covariate projection) | Homeostatic resilience index (computational analogue) | Low p_trans = tendency toward PCC/worsening states; high = toward Healthy |
| Infection wave effect (3rd/4th vs. 1st wave better recovery) | Acute-insult severity as PAIS probability determinant | Later waves (Omicron era) = lower intrinsic pathogenicity → lower homeostatic disruption |
| Female sex worsening trajectory | Sex-differentiated immune/homeostatic regulation | Consistent with cross-PAIS female predominance literature |
| Age >60 worsening trajectory | Age-related homeostatic capacity decline | Mirrors immune senescence / inflammaging PAIS vulnerability |
| SF-36 PCS and MCS continuous outcomes | Physical and mental homeostatic function metrics | Joint modelling enables multi-domain homeostatic profiling |
| Filtering-based individual prediction | Personalised homeostatic trajectory forecast | Real-time updating as new data arrive; clinically actionable |

## Limitations

- **Hospitalised-enriched cohort (75.4% hospitalised):** Results are not directly generalisable to the broader SARS-CoV-2-infected population, particularly mild/asymptomatic infections. The model likely overestimates PCC burden and underestimates Healthy-state recovery rates in the general population.
- **Patient attrition:** From 5,094 at baseline to 628 at 24 months; only 419 with complete 5-timepoint data. The authors assume Missing Completely At Random (MCAR), but if healthier patients are disproportionately lost to follow-up, the trajectory estimates are biased toward apparent non-recovery. The 18- to 24-month window is particularly uncertain.
- **No HRQoL data at acute timepoint:** SF-36 scores are unavailable at the acute infection phase; the Acute Respiratory and Acute Moderate state HRQoL distributions have high uncertainty (wide CIs).
- **Label switching ambiguity in HMMs:** The non-identifiability issue of HMMs (label switching) can overinflate uncertainty in covariate estimates despite careful initialisation and multiple warm restarts.
- **Corticosteroid effect non-interpretable:** Corticosteroids were administered to the most severely ill patients, so the worsening association reflects indication bias and cannot be causally interpreted.
- **No pre-infection HRQoL baseline:** Pre-infection SF-36 data are not available. Initial health state and subsequent trajectory may both be endogenous to pre-infection HRQoL, introducing unmeasured confounding.
- **Symptoms are self-reported binary indicators:** Dichotomised symptom reporting (present/absent) collapses symptom severity gradations. More granular symptom scales or objective biomarkers are absent from the model.
- **No biomarker or mechanistic variables:** The model is entirely symptom- and HRQoL-based. Immune, virological, or metabolic variables are not incorporated, limiting mechanistic inference.
- **Limited geographic/variant diversity:** Cohorts from France, Italy, Netherlands, Spain; early variants (first wave through Omicron era), but limited representation of non-European populations or post-Omicron infection trajectories.
- **HRQoL recovery plateau at 24 months:** The model extrapolates recovery times beyond 24 months (e.g., 89.46 months for females >60) based on steady-state assumptions; extrapolations beyond observed follow-up window carry large uncertainty.

## Model / Tool Availability

- **Framework:** Open-source Julia implementation of the full LTA framework for PAIS longitudinal studies.
- **Repository/DOI:** https://doi.org/10.5281/zenodo.17787061
- **Includes:** Model fitting, prediction (filtering-based), simulation, visualisation routines, and interactive trajectory exploration tools.
- **License:** Not specified in paper text; check Zenodo repository.
- **Input requirements:** Longitudinal mixed-type data (binary symptom indicators + continuous HRQoL scores); missingness tolerated via HMM marginalisation.
- **ORCHESTRA data availability:** Dataset used in analysis available as Supplementary Data 1-3; full cohort data via ORCHESTRA project (EU-funded, NCT05097677).

## Follow-up

- **Methodological extension opportunities:** The LTA framework as described is symptom-only; incorporating immune biomarkers (cytokines, autoantibodies, viral load kinetics) into the emission model would enable mechanistic state characterisation. Future work explicitly mentioned in the discussion.
- **Cross-PAIS applicability:** The authors explicitly note the framework is applicable to any PAIS study with longitudinal binary/continuous multimodal data — direct invitation to apply to ME/CFS, post-Lyme, post-dengue, or post-Q-fever datasets in this project.
- **Causal inference extension:** The paper notes future work may incorporate time-varying covariates and explicit modelling of interventions (e.g., post-infection vaccination or rehabilitation), enabling causal inference on recovery-modifying treatments — directly relevant to the project's intervention question.
- **Individual prediction clinical utility:** The filtering-based prediction approach, if validated prospectively, could support personalised clinical monitoring — a key translational goal of this project.
- **Related papers in ORCHESTRA group:** Tacconelli et al. (project PI) and the 12-month ORCHESTRA results paper (1,796 patients) published previously — cited as reference 21 in the paper. The 18- and 24-month data are new in this study.
- **Comparison with cross-sectional clustering literature:** PCC phenotypes identified by LTA (Sensorial, Respiratory, Fatigue) largely replicate symptom-based clusters from prior PCA/k-means work (Chronic Fatigue, Respiratory, Pain, Neurosensorial, Gastro-intestinal), providing convergent validity — but LTA adds longitudinal dynamics that cross-sectional approaches cannot.
- **Recovery time predictions as clinical benchmarks:** The model-derived recovery time distributions (20.81 months for low-risk profiles; 89.46 months for high-risk females >60) could serve as reference benchmarks for trial design (expected natural history) and for evaluating whether interventions meaningfully alter trajectory.
