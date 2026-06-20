---
id: paper:Girgis2025
type: paper
title: 'Aberrant T-cell phenotypes in a cohort of patients with post-treatment Lyme
  disease'
status: active
ontology_terms:
- post-treatment Lyme disease syndrome
- T-cell phenotypes
- T-cell exhaustion / activation
- Borrelia burgdorferi
- immune dysregulation
source_refs:
- cite:Girgis2025
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- topic:post-infectious-dysautonomia-and-autoimmunity
created: '2026-06-20'
updated: '2026-06-20'
---
# Aberrant T-cell phenotypes in a cohort of patients with post-treatment Lyme disease

- **Authors:** Alexander A. Girgis, Raffaello Cimbro, Ting Yang, Alison W. Rebman, Thelio Sewell, Daniela Villegas de Flores, Aarti Vadalia, William H. Robinson, Andrea L. Cox, Erika Darrah, Mark J. Soloski, John Aucott
- **Year:** 2025
- **Journal:** Frontiers in Immunology
- **DOI:** 10.3389/fimmu.2025.1607619
- **PMID:** 40703523
- **PMCID:** PMC12283721
- **BibTeX key:** Girgis2025
- **Tier:** Core now
- **Source:** Europe PMC XML (full text; no PDF available via paper-fetch)

## Key Contribution

This paper provides systematic immunophenotyping of a well-characterised cohort of 285 post-treatment Lyme disease (PTLD) patients from the Johns Hopkins Lyme Disease Research Center, comparing them to 28 healthy controls. It demonstrates that PTLD is associated with specific T-cell perturbations detectable in peripheral blood — notably a depletion of CXCR5+ naïve CD4 T cells and an expansion of Th1-like (CXCR3+ CCR4- CCR6-) CD8 T cells — and builds an elastic net classifier (AUC 0.83) on these flow cytometry features that discriminates PTLD from healthy controls. Critically, no serum cytokine/chemokine differences were detected, suggesting that the immune signature in established (retrospective, median ~635 days post-infection) PTLD is primarily cellular rather than soluble.

This study fills the PTLD cell of the cross-pathogen T-cell immune-dysregulation axis: it demonstrates that Borrelia burgdorferi infection, a bacterium rather than a virus, can produce a post-infectious state with an inflammatory/exhausted-T-cell phenotypic fingerprint parallel to those documented in long COVID and ME/CFS. The evidence is assembled (single-trigger, not head-to-head), but the parallel is explicit in the Discussion.

## Methods

**Cohort:** 285 PTLD patients enrolled through a referral-based clinic at Johns Hopkins. Case definition (Aucott/Rebman criteria): documented prior Lyme disease diagnosis per CDC criteria, functionally impairing symptoms (fatigue, musculoskeletal pain, cognitive dysfunction) persisting after appropriate antibiotic treatment, minimum symptom duration not specified by the case definition but cohort enrolled median 635 days post-infection (IQR 222–1484 days). Exclusions: depression, cancer, HIV, autoimmune disorders. 28 healthy controls (negative two-tier serology for Borrelia; no prior Lyme diagnosis). Demographics: median age 48, 56.5% male, 91.2% white non-Hispanic. Blood drawn 2014–2018.

**Symptom profiling:** 272 PTLD participants completed the 36-item Post-Lyme Questionnaire of Symptoms (PLQS). Factor analysis reduced 30 items to six latent factors (Fatigue/Cognitive, Ocular Disequilibrium, Infection-Type, Mood-Related, Musculoskeletal Pain, Neurologic). PCA + k-means clustering (k=6) generated six patient symptom subgroups with distinct profiles.

**Flow cytometry:** 144 PTLD participants and 20 healthy controls; whole blood; 19-parameter panel measuring T cells (CD4, CD8, naïve/memory subsets via CCR7/CD45RA), B cells, NK cells, and monocytes; markers included CXCR5, CD57, HLA-DR, CXCR3, CCR4, CCR6. Analysis yielded 119 manually derived gates. Data acquired on a five-laser FACS Aria II. Freshly drawn blood analysed same day.

**Cytokine/chemokine profiling:** 258 PTLD and 28 controls; Bio-Plex Luminex multiplex for 34 analytes (including CCL19, IL-23, IFNα, IFNγ, TNFα, IL-17).

**Statistics:** Shapiro-Wilk normality; Wilcoxon/Kruskal-Wallis or t-test/ANOVA; Benjamini-Hochberg FDR correction (alpha = 0.05 for each data modality). Confounder adjustment via GLM (age, sex, race, income, year of collection). Symptom-immune associations via Spearman correlation + GLM verification. Elastic net classifier (cv.glmnet, 3-fold CV, 100 iterations; 70/30 train-test split stratified by sex and PTLD status).

## Key Findings

**T-cell alterations distinguishing PTLD from healthy controls (flow cytometry, Table 2):**

| Population | % HC | % PTLD | Padj |
|---|---|---|---|
| CXCR5+ CD4 Naive | 8.84 | 5.17 | 0.001 |
| CD8 Th1 (CXCR3+ CCR4- CCR6-) | 25.68 | 43.15 | 0.003 |
| CD8 Th1/17 (CXCR3- CCR4+ CCR6+) | 13.43 | 3.88 | 0.003 |
| CD57+ HLA-DR+ CD4 EMRA | 1.58 | 5.12 | 0.024 |

- CXCR5+ naïve CD4 T cells are reduced: these cells may be precursors to follicular-helper T cells (TFH) or related to T-B cooperation; the authors link their depletion to impaired T-cell–dependent B-cell function, consistent with prior mouse-model evidence for dysregulated humoral immunity after Borrelia infection.
- The CD8 Th1-like expansion (CXCR3+ CCR4- CCR6-) corresponds to a putative Tc1 cytotoxic-T-cell phenotype with inflammatory IFNγ/TNFα potential, consistent with chronic inflammation or autoimmune-adjacent processes. Authors are cautious — functional cytokine secretion was not measured.
- Increased CD57+ HLA-DR+ CD4 EMRA cells support an inflammatory milieu; CD57+/KLRG1 expression has been associated with cytotoxic function in prior literature.
- Multivariate dimensional reduction (UMAP + k-means) did not generate clusters that separated PTLD from controls or matched symptom subgroups — the effect is visible only in univariate testing.

**Cytokines/chemokines:** No significant differences between PTLD and healthy controls in any of the 34 analytes (including CCL19, IL-23, IFNα). No cytokine correlated with symptom factor scores. The authors note this contrasts with longitudinal cohorts analysed closer to acute infection, and attribute the discrepancy to late enrolment (median >1.7 years post-infection).

**Elastic net classifier:** Flow cytometry features alone drove classification performance (AUC 0.83, misclassification error 0.26). Cytokine features added no predictive power. In the representative model, CXCR5+ naive CD4 T cells explained ~32% of variance, CD8 Th1 ~25%, CD8 Th1/17 ~25%.

**Symptom associations (Table 3, Spearman within PTLD):**
- CXCR5+ naive CD4 T cells positively correlated with Musculoskeletal Pain (rho=0.21, Padj=0.041) — and notably showed the opposite direction in healthy controls (rho=−0.56, Padj=0.017).
- NK cells (CD8+ and CD8-) negatively correlated with Ocular Disequilibrium and Musculoskeletal Pain scores.
- CD4 T cell frequency positively correlated with Neurological factor score.

**Sex-specific findings:** The cohort is 56.5% male, unusual for PAIS. "Mild symptom" cluster 6 was significantly more male (71% male vs. 35% in high-severity cluster 5). Female PTLD participants in "Fatigue/Cognitive" cluster 3 showed elevated central memory (CM) CD8 T cells relative to other subgroups (21.2% vs. 12.2%, Padj=0.04), not observed in males or the combined cohort.

**Symptom subgroup immune associations:** No flow cytometry or cytokine features significantly distinguished any of the six PTLD symptom subgroups from each other.

## Relevance to Project

This paper is a core PTLDS data point for the cross-pathogen immune-dysregulation track (t001) and directly grounds two project-level entities:

- **hypothesis:0001-shared-dysregulated-attractor** — The paper provides positive PTLD evidence for the "exhausted/activated T-cell" arm of the shared dysregulated immune attractor. Specifically: depletion of CXCR5+ naive CD4 T cells (impaired TFH precursor pool / humoral regulation), expansion of CD8 Th1-like cytotoxic cells (inflammatory effector expansion), and elevation of CD57+ HLA-DR+ CD4 EMRA cells (cytotoxic/senescent effector pool). These phenotypic signatures are the Borrelia-triggered counterpart to the CD8 exhaustion and activation profiles described in ME/CFS (Iu2024) and long COVID. Evidence is assembled — this paper does not compare to other PAIS cohorts — so the cross-trigger parallel is inferential.
- **question:0001-shared-molecular-signature-across-triggers** — The PTLDS T-cell immunophenotype described here is a candidate column for the cross-pathogen signature matrix. The elastic net classifier features (CXCR5+ naive CD4, CD8 Th1, CD8 Th1/17) are interpretable enough to test whether analogous gates are altered in long COVID or ME/CFS immunophenotyping datasets.

The paper explicitly situates PTLD within the PAIS frame: the authors write that the T-cell findings "are consistent with literature supporting dysregulated humoral responses following borrelial infection, and an inflammatory/exhausted T cell profile similar to those observed in other chronic or post-acute infection syndromes."

The **topic:post-infectious-dysautonomia-and-autoimmunity** link is indirect: the discussion invokes autoimmune-adjacent mechanisms (persistent antigen or infection-induced autoimmunity) as the plausible drivers of the CD8 Th1/EMRA expansion, and prior literature on Lyme arthritis (Lochhead et al. 2021) frames the broader autoimmunity connection.

## Project Framework Mapping

| Framework element | Mapping |
|---|---|
| PAIS trigger | Borrelia burgdorferi (bacterium; tick-borne) |
| Case definition | Aucott/Rebman PTLD criteria (CDC-confirmed Lyme + symptoms >6 months post-treatment) |
| Immune domain | T-cell activation/exhaustion axis; humoral dysregulation (TFH precursor depletion) |
| Evidence class | Cross-sectional observational; controlled (healthy controls); not longitudinal |
| Covariates controlled | Age, sex, race, income, year of sample collection (GLM) |
| Cross-pathogen assembly role | PTLDS column in signature matrix for hypothesis:0001 / question:0001 |

## Limitations

1. **Cross-sectional retrospective design**: No pre-illness or return-to-health comparison arm. Cannot distinguish chronic PTLD-specific changes from post-Borrelia changes present even in recovered individuals.
2. **Late enrolment**: Median ~635 days post-infection (IQR 222–1484). Cytokine signals (CCL19, IL-23, IFNα) previously reported in longitudinal early-PTLD cohorts were absent here; the immune landscape at >1 year may differ substantially from the acute-to-post-acute transition.
3. **Small healthy control group**: n=20 for flow cytometry; reduces power for sex-stratified comparisons and may inflate false-negative rates.
4. **Cohort skew**: 91.2% white non-Hispanic; predominantly high-income; referral-based clinic population — limits generalisability. Cohort is also majority male (56.5%), atypical for PAIS and potentially confounding sex-specific conclusions.
5. **Incomplete sex/gender data**: Self-reported gender used as proxy for biological sex; sex assigned at birth was collected only partially.
6. **No functional validation**: The CD8 Th1-like phenotype is defined by surface markers (CXCR3+ CCR4- CCR6-) only; cytokine secretion (IFNγ, TNFα) not directly measured. Authors appropriately flag this.
7. **Limited B-cell, innate, and monocyte panels**: T-cell phenotypes were most exhaustively explored; other lineages may carry additional signal.
8. **Day-to-day assay variation**: Flow cytometry on fresh whole blood over a multi-year period (2014–2018) introduces technical noise despite year-of-collection covariate adjustment.
9. **Heterogeneous case definition elements**: Not all patients required an EM rash; prior Lyme disease confirmed by CDC criteria (symptoms + serology) introduces some diagnostic ambiguity.

## Model / Tool Availability

None. Code and raw data will be made available by the authors on request (stated in Data Availability Statement); no repository link provided in the published paper.

## Follow-up

- Compare CXCR5+ naive CD4 depletion and CD8 Th1 expansion quantitatively against analogous flow cytometry gates in published long COVID (e.g., Peluso2024, Ryan2022) and ME/CFS (Iu2024) cohorts to populate the cross-pathogen signature matrix for question:0001.
- A "return to health after Lyme treatment" comparison arm is explicitly called out as missing; future cohort studies should include this.
- Investigate whether CXCR5+ naive CD4 T cell frequencies also show inverted symptom-correlation directionality (opposite sign in patients vs. controls) in long COVID datasets — this would be a strong cross-trigger convergence signal.
- The sex distribution (majority male) is unusual for PAIS; explore whether this reflects referral bias or genuine sex-specific penetrance of PTLD vs. other PAIS.
