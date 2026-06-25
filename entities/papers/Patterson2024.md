---
id: paper:Patterson2024
type: paper
title: 'Long COVID diagnostic with differentiation from chronic Lyme disease using
  machine learning and cytokine hubs'
status: active
updated: '2026-06-25'
ontology_terms:
- long COVID
- chronic Lyme disease
- cytokine hubs
- machine learning classifier
- immune signature
- differential diagnosis
source_refs:
- cite:Patterson2024
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- discussion:0002-cross-pathogen-pais-signature-convergence
created: '2026-06-20'
---
# Long COVID diagnostic with differentiation from chronic Lyme disease using machine learning and cytokine hubs

- **Authors:** Bruce K. Patterson, Jose Guevara-Coto, Javier Mora, Edgar B. Francisco, Ram Yogendra, Rodrigo A. Mora-Rodriguez, Christopher Beaty, Gwyneth Lemaster, Gary Kaplan, Amiram Katz, Joseph A. Bellanti
- **Year:** 2024
- **Journal:** Scientific Reports
- **DOI:** 10.1038/s41598-024-70929-y
- **PMID:** 39187577
- **PMC:** PMC11347643
- **BibTeX key:** Patterson2024
- **Tier:** Core now
- **Source:** Europe PMC full-text XML (OA)

## Key Contribution

This paper presents a head-to-head comparison of long COVID/PASC and chronic Lyme disease (CLD) using a 14-analyte plasma cytokine panel plus two composite cytokine-hub scores, fed into tree-based machine learning classifiers (decision tree, random forest, gradient boosting machine). The central claim is that long COVID and CLD, while sharing a broad symptom repertoire (fatigue, brain fog, post-exertional malaise), are immunologically distinguishable by distinct cytokine "hubs." The GBM classifier achieves ~89% weighted accuracy (sensitivity 89%, specificity 96%) on a held-out 20% partition, and a separately reported validation set of 124 patients (106 LC, 18 CLD) yields a weighted sensitivity of 97.6% and specificity of 90.4%. The authors further introduce a two-feature "CLD Index" (ratios of TNF-alpha/IL-4 over IFN-gamma/IL-2 combinations) that they report achieves 100% sensitivity and specificity on both the held-out split and a separate 25-CLD dataset.

**Project significance:** This is the only paper in the current PAIS corpus to directly run a within-study head-to-head cytokine comparison between long COVID and a distinct non-COVID PAIS trigger (Borrelia). Its finding of immunological *separation* is the strongest accessible disputing datapoint against the molecule-level shared-signature prediction of `hypothesis:0001`. However, this finding must be held at exactly the evidence level the methods warrant — see Limitations below.

## Methods

**Cohorts and sample sizes (full dataset):**

| Class | N (full) | N (train, 80%) | N (eval, 20%) |
|---|---|---|---|
| Not Perturbed (HC + mild-moderate COVID-19) | 67 | 54 | 13 |
| LC/PASC | 103 | 82 | 21 |
| CLD | 53 | 42 | 11 |

Validation set (independent, randomly selected, blinded): 124 patients (106 LC/PASC, 18 CLD).

**Case definitions:**
- LC/PASC: confirmed/probable SARS-CoV-2 infection (WHO guidelines), age ≥18, persistent symptoms >12 weeks post-infection. Symptom scoring per Thaweethai et al. 2023 (JAMA RECOVER definition).
- CLD: pre-2020 onset (predates SARS-CoV-2 pandemic), duration >6 months (ILADS Working Group), confirmed Borrelia burgdorferi seropositivity by two-tier immunologic testing including immunoblot. Co-infections noted but not required.
- Not Perturbed (NP): healthy controls + mild-to-moderate acute COVID-19 combined. Combination justified by a Mann-Whitney U-test showing no significant difference in any of the 14 cytokines or composite scores between healthy controls and mild-moderate acute COVID (all p > 0.05; VEGF showed a trend at p = 0.09). Severe acute COVID was excluded.

**Cytokine panel:** 14-plex bead-based flow cytometric assay (IncellKINE, IncellDx, Inc.) on a Beckman Coulter CytoFlex LX. Analytes: TNF-alpha, IL-4, IL-13, IL-2, GM-CSF, sCD40L, CCL5 (RANTES), CCL3 (MIP-1alpha), IL-6, IL-10, IFN-gamma, VEGF, IL-8, CCL4 (MIP-1beta). 25 µL plasma per well (plasma preparation tubes, BD Biosciences).

**Pre-existing composite scores used as additional features:**
- Lymphocyte/Helper Index (LHI) = (IL-2 + IFN-gamma) / CCL4 — characterizes LC/PASC (elevated IL-2 and IFN-gamma, supports lymphopenia/virus persistence hypothesis)
- Severity Index (SI) = (IL-6 + sCD40L/1000 + VEGF/10 + 10*IL-10) / (IL-2 + IL-8) — previously reported for LC severity stratification

**Outlier removal:** Isolation forest (contamination parameter not reported in XML).

**Data split:** Stratified 80/20 train/hold-out. Reported as a single partition (no k-fold cross-validation described).

**ML models:** Decision Tree (scikit-learn), Random Forest (scikit-learn), Gradient Boosting Machine (LightGBM). Hyperparameter optimization performed for each (parameters tuned not fully enumerated in the XML text).

**Model selection:** GBM selected based on best weighted performance on hold-out and shortest training time. Decision paths interpreted via a surrogate single-tree visualization.

**CLD Index (post-hoc heuristic):** Two engineered ratio features:
- Feature 1 = (TNF-alpha + IL-4) / (IFN-gamma + IL-2)
- Feature 2 = (TNF-alpha × IL-4) / (IFN-gamma + IL-2 + CCL3)

These were constructed by programmatic search over cytokine combinations guided by domain expertise (ratios, powers, multiplication, sums), then validated with a separate decision tree on the 25-CLD dataset (CLD-only, no LC or NP comparators in that test). The paper states the features were developed to improve classification of misclassified instances from the GBM.

**Blinded validation:** 125 patients enrolled (1 removed for missing clinical data), leaving 124. GBM applied to blinded cytokine profiles; disease state confirmed by clinical assessment post-prediction.

**Statistical tests:** Mann-Whitney U-test for group comparisons; no multiple testing correction reported. No confidence intervals on performance metrics.

## Key Findings

**Cytokine signatures distinguishing LC/PASC from CLD:**

- LC/PASC is characterized by elevated **IL-2 and IFN-gamma** (captured in LHI numerator) and elevated IL-6/VEGF/IL-10/sCD40L (SI numerator). Authors interpret the IFN-gamma + IL-2 elevation as consistent with lymphopenia and persistent viral antigen driving T-cell activation.
- CLD is characterized by elevated **TNF-alpha and IL-4** in the numerator of the Lyme Index. Authors interpret TNF-alpha as driving central sensitization syndrome and neuroinflammation; IL-4 elevation is interpreted as either a Th2 compensatory response to TNF-alpha-mediated damage or as TNF-alpha-induced GATA-3/Th2 polarization.

**GBM classifier performance (hold-out 20%):**
- Sensitivity: 89%, Specificity: 96%, F1: 0.89, Accuracy: 89%
- Training metrics were 100% for both GBM and RF, and 97%/99% for DT (train), revealing a large train-to-test performance gap.

**GBM validation on 124-patient independent set:**
- LC/PASC: sensitivity 99.1%, specificity 88.9%, PPV 98.1%, NPV 94.1%, F1 0.986
- CLD: sensitivity 88.9%, specificity 99.1%, PPV 94.1%, NPV 98.1%, F1 0.914
- Weighted: sensitivity 97.6%, specificity 90.4%, PPV 97.6%, NPV 94.7%, F1 0.950, accuracy 94%

**CLD Index (decision-tree on two engineered features):**
- Hold-out split: 100% sensitivity, 100% specificity
- 25-CLD dataset (CLD-only): 100% sensitivity, accuracy, PPV, F1

**No AUC (AUROC) is reported anywhere in the paper.**

**GBM surrogate-tree interpretation:** High IL-2 levels lead to LC/PASC classification; lower IL-2 levels lead toward CLD or NP; VEGF is a secondary discriminating node.

## Relevance

### Cross-pathogen shared-signature verdict

This paper constitutes the single clearest within-study **disputing** datapoint against the molecular-level claim in `hypothesis:0001`. If the classifier genuinely captures distinct biology, then long COVID and chronic Lyme disease are not instances of the same molecular attractor state — they differ in cytokine hub structure in a way detectable from a 14-analyte plasma panel. This is the most tractable head-to-head cytokine comparison in the corpus.

**However, "separation by classifier" is weaker evidence than it appears for biology** (see Limitations). A classifier can separate groups by features that reflect recruitment-site, timing, or cohort confounds rather than fundamental mechanisms. The finding of distinction is therefore **necessary but not sufficient** to conclude distinct biology; it rules out identity of cytokine profiles but does not rule out shared upstream mechanisms expressed differently downstream.

### Specific cytokine hubs

The paper identifies concrete, interpretable candidate hubs:
- **Long COVID hub:** IFN-gamma + IL-2 (Th1/cytotoxic activation, lymphopenic/virus-persistent phenotype)
- **CLD hub:** TNF-alpha + IL-4 (Th1 neuroinflammation + Th2 compensation or CNS sensitization)

These are mechanistically plausible if taken individually; the IL-2/IFN-gamma finding is consistent with prior long-COVID immune profiling. The TNF-alpha/IL-4 finding in CLD is consistent with neuroborreliosis CSF literature cited. But in this study they are derived from the same data used to build the classifier, so the hub structure is not independently validated — only the classifier output is (partially) validated.

### Connections to t001 cross-pathogen track

This paper addresses `question:0001-shared-molecular-signature-across-triggers` directly. It is cited in `discussion:0002` as the primary head-to-head *disputer* of convergence. The result from this paper should be read as "distinguishable cytokine profiles between LC and CLD at the time of cross-sectional plasma sampling in a single clinical center" — not as "distinct mechanisms all the way to pathogenesis."

## Project Framework Mapping

- **hypothesis:0001-shared-dysregulated-attractor** — Patterson2024 is the main in-corpus challenge to the molecule-level shared-signature prediction. Weight it at: "cytokine profiles distinguish these two syndromes in a single-center clinical-population classifier study." That is a meaningful empirical constraint, but it does not adjudicate whether the *pathogenic* mechanisms upstream are the same or different.
- **question:0001-shared-molecular-signature-across-triggers** — Directly informative. Current evidence entry: Patterson2024 finds distinguishable cytokine patterns (disputes shared molecule-level signature at the plasma cytokine level); head-to-head design; limited by COI, single center, no harmonization with other trigger comparators.
- **discussion:0002** — Already noted as the strongest disputer in the signature matrix; this note provides the detail needed to interpret the cell entry "distinguishable vs LC (Patterson2024 h2h)."

## Limitations

### ML overfitting and generalization — primary critical concern

1. **Near-perfect training scores, systematic train/test gap.** The RF and GBM models score 100% on training data; both drop to 89% on the hold-out 20% split. DT trains at 97%/99%, drops to 84% on test. A 11-percentage-point drop from train to test in a 45-sample test set (21 LC + 11 CLD + 13 NP) is a strong overfitting signal. The authors assert that "similarity of metrics between training and hold-out set indicates no overfitting" — this interpretation is questionable given the absolute gap and the small hold-out N.
2. **Very small hold-out evaluation set.** The 20% hold-out contains 45 total individuals (11 CLD observations). Performance metrics from 11 CLD test cases have wide confidence intervals; the paper does not report CIs or bootstrap estimates.
3. **No k-fold cross-validation.** A single 80/20 split is highly dependent on which 20% was selected; without k-fold or leave-one-out the variance in performance estimates is unknown.
4. **Hyperparameter optimization on the same dataset partition.** If hyperparameters were tuned on the training set and evaluated on the same hold-out, there is no fully held-out test set.
5. **"Independent" validation set shares the same clinical site and cytokine platform.** The blinded validation set (n=124) was drawn from the same IncellDx / Chronic COVID Treatment Center clinical population where the training data were collected. This is not independent in the sense of different institution, geography, patient demographic, or assay batch.
6. **No external validation, no multi-site replication.** The classifier has not been evaluated in any external cohort.
7. **CLD Index "100% sensitivity/specificity" result is unreliable.** The 25-CLD dataset used to validate the CLD Index contains only one class (CLD). Without a mixed-class test set (LC/PASC + NP individuals included), specificity cannot be computed — the paper's "100% specificity" on the 25-CLD set does not test whether LC/PASC cases are falsely labeled as CLD. The hold-out split test (100% on both) has only 11 CLD + 34 non-CLD samples in the test partition, making those metrics very noisy.

### Class imbalance
- The training set has LC (82) >> NP (54) >> CLD (42). Class imbalance can bias classifiers toward over-recognizing the majority class. The paper reports "class weight" as a hyperparameter that was adjusted for the decision tree; it is not clear whether class weighting or oversampling was applied to GBM.

### Cohort and case-definition concerns
1. **CLD definition is contested.** "Chronic Lyme disease" is not an IDSA-recognized diagnosis; the ILADS Working Group definition used here is broader than post-treatment Lyme disease syndrome (PTLDS). The cohort may include individuals with other diagnoses. The paper does not report alternative diagnoses excluded, nor negative tick-borne organism workup prevalence.
2. **Single-site clinical population (IncellDx / CCTC).** Individuals were recruited through a specialized clinic focused on long COVID and Lyme. Selection bias toward patients with overlapping symptoms seeking differential diagnosis is likely. This limits generalizability to broader population-based PAIS cohorts.
3. **No pre-infection baselines, no time-matched healthy controls.** The "Not Perturbed" class merges healthy controls with mild-moderate acute COVID (combined post-hoc because no statistically significant differences found). Pre-infection cytokine data are absent; trajectory information is not available.
4. **Sex, age, and severity covariates.** The validation-set demographics (45% male/55% female in LC; 32%/68% in CLD; median age 45 vs 41) show modest covariate differences between groups that were not adjusted for in the classifier.
5. **Duration since illness onset not reported.** Cytokine profiles in both LC and CLD may vary substantially with time since onset; whether samples were matched on this is not stated.

### Conflict of interest
The lead author (Patterson) and several co-authors (Beaty, Guevara-Coto, Francisco) are employees of IncellDx, Inc., the company that developed the IncellKINE assay platform used in this study and that has a commercial interest in plasma cytokine testing for long COVID diagnostics. This does not invalidate the findings but is a relevant consideration for interpreting the strength of the claims and the absence of external replication.

### Methodological reporting gaps
- No AUROC/AUC reported (only accuracy, sensitivity, specificity, PPV, NPV, F1).
- No confidence intervals on any performance metric.
- Number of features selected for final model not stated (all 16 features used, or a subset?).
- Contamination parameter for isolation-forest outlier removal not stated.
- Hyperparameter grid/search method not fully described.
- No SHAP or feature importance analysis reported (only surrogate tree approximation).

## Model / Tool Availability

The GBM classifier and CLD Index are described but **not released as a public tool or code repository** in this publication. Raw data available on request from the corresponding author (brucep@incelldx.com). The IncellKINE assay is a proprietary commercial product of IncellDx, Inc.

## Follow-up

1. **Cross-validate against an independent multi-site LC vs PTLDS cohort** — ideally one using a standardized cytokine panel and a confirmed PTLDS definition (post-treatment, seropositive, IDSA criteria), to determine whether the IL-2/IFN-gamma vs TNF-alpha/IL-4 hub separation holds outside IncellDx.
2. **Interrogate the LHI/SI hub structures in ME/CFS cohorts** — the LHI (IL-2 + IFN-gamma / CCL4) is claimed to be characteristic of LC; whether this also marks ME/CFS or is LC-specific would directly test whether molecular convergence between long COVID and ME/CFS extends to this same axis.
3. **Compare with Galbraith2011** — the Dubbo cohort found *partial* shared transcripts across EBV, Ross River virus, and Q-fever post-infective fatigue. Patterson2024 finds LC–CLD separation on a different modality (plasma cytokines); assessing whether the Galbraith shared transcripts include IFN-gamma or IL-2 pathway genes would triangulate whether convergence exists at gene-expression level while divergence exists at plasma cytokine level.
4. **Resolve the CLD definition issue** — repeat the analysis restricting CLD to IDSA-compliant PTLDS (documented acute Lyme, treated, persistent symptoms); current "CLD" may be heterogeneous.
5. **SHAP or permutation-importance analysis** — determine which of the 14 analytes are load-bearing for the GBM; the surrogate-tree approximation is coarse and may misrepresent the GBM's actual feature usage.
