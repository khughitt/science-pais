---
id: paper:Klein2023
kind: paper
title: Distinguishing features of long COVID identified through immune profiling
status: active
ontology_terms:
- long COVID
- immune profiling
- post-acute sequelae of SARS-CoV-2
- Epstein-Barr virus reactivation
- cortisol dysregulation
- non-conventional monocytes
- machine learning biomarker discovery
- T cell exhaustion
dataset_usage: []
source_refs:
- cite:Klein2023
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Distinguishing features of long COVID identified through immune profiling

- **Authors:** Jon Klein, Jamie Wood, Jillian R. Jaycox, Rahul M. Dhodapkar, Peiwen Lu, Jeff R. Gehlhausen, Alexandra Tabachnikova, et al. (Akiko Iwasaki, David Putrino, Aaron M. Ring, David van Dijk — corresponding authors)
- **Year:** 2023
- **Journal:** Nature, vol. 623, pp. 139–148
- **DOI:** 10.1038/s41586-023-06651-y
- **BibTeX key:** Klein2023
- **Source:** PDF

## Key Contribution

This cross-sectional immune-profiling study of 275 individuals (MY-LC cohort, Mount Sinai–Yale) identifies a multi-domain biological signature distinguishing long COVID (LC) from demographically matched controls more than a year after acute infection. Using multidimensional flow cytometry, plasma proteomics, SARS-CoV-2 antibody profiling, exoproteome autoantibody screening, and viral serology — integrated by unbiased machine learning — the study demonstrates that LC is associated with distinct myeloid and lymphocyte perturbations, exaggerated SARS-CoV-2 humoral responses, reactivation of latent herpesviruses (especially EBV), and markedly reduced systemic cortisol. An integrated LASSO classifier achieves AUC 0.94 (95% CI 0.84–1.00) for LC versus control discrimination, with cortisol as the single strongest predictor (AUC 0.96 alone), providing the first validated multi-omic biomarker panel for LC.

## Methods

**Design:** Cross-sectional, observational. The Mount Sinai–Yale Long COVID (MY-LC) study enrolled 185 participants at one site (Mount Sinai Hospital) and 90 at a second (Yale New Haven Hospital); a separate external validation cohort (EXT-LC, n = 53) was also analyzed.

**Five study groups (final n = 268 after exclusions):**
1. Healthcare workers infected with SARS-CoV-2 before vaccination (HCW; n = 37)
2. Healthy uninfected controls (HC; n = 40)
3. Previously infected, vaccinated controls without persistent symptoms (convalescent controls, CC; n = 39)
4. Individuals with long COVID persistent symptoms after acute infection (LC; n = 99)
5. External long COVID cohort (EXT-LC; n = 53)

LC and CC participants had primarily mild (non-hospitalized) acute COVID-19; samples collected on average >1 year after acute infection. Two LC participants excluded for pharmacological immunosuppression; 2 HC for pregnancy/misclassification; 3 CC for pregnancy, monogenic disorder, and misclassification.

**Assays:**
- Flow cytometry: comprehensive PBMC immunophenotyping (T cell subsets, B cell subsets, myeloid populations)
- Plasma proteomics: soluble immune mediators and hormones (multiplex)
- SARS-CoV-2 antibody profiling: ELISA (anti-S, anti-S1, anti-RBD, anti-N); peptide immunome-wide association study (PIWAS) for spike linear epitope mapping
- Exoproteome autoantibody profiling: rapid extracellular antigen profiling (REAP) against >6,000 secreted and extracellular human proteins in 98 LC + 38 control participants
- Viral serology: serum epitope repertoire analysis (SERA) against 225 viral surface proteins spanning 38 conformational epitopes; ELISA for herpesvirus antigens
- LC propensity score (LCPS): parsimonious logistic regression model (AUC 0.95, bootstrap 95% CI 0.91–0.98) for case classification
- Machine learning: k-nearest neighbour (k-NN; AUC 0.94), PCA, and final LASSO regression model on matched subset (n = 40 HC, 39 CC, 79 LC selected by Gale–Shapley procedure)
- Symptom clustering: agglomerative hierarchical clustering of 30 self-reported binary symptoms → 3 LC clusters

**Key statistical approaches:** Kruskal–Wallis with Benjamini–Hochberg FDR correction; linear models (incorporating age, sex, LC status, BMI, vaccination status, days from acute disease, cohort); PERMANOVA; Spearman correlation; Fisher's exact tests; k-NN; LASSO.

## Key Findings

**Cohort characteristics:**
- LC group mean age 46 years vs. CC 38 years (Kruskal–Wallis P = 0.0040); no significant sex difference
- 87% of LC had mild (non-hospitalized) acute COVID-19; 13% hospitalized
- Most LC infections occurred during epidemiological weeks 7–17 of 2020 (WA-1 strain)
- Top self-reported symptoms: fatigue (87%), brain fog (78%), memory difficulty (62%), confusion (55%); POTS prevalent in 38%

**Circulating immune cell populations:**
- Non-conventional monocytes (CD14^low CD16^high) significantly elevated in LC vs. CC (linear model: P significant after adjusting for age, sex, LC status, BMI)
- MHC class II (HLA-DR) expression significantly elevated in LC monocytes
- Conventional type 1 dendritic cells (cDC1) significantly lower in LC
- B lymphocyte activated subsets (CD86^high HLA-DR^high) significantly higher: 17% (LC) vs. 11% (CC) vs. 12% (HC)
- Double-negative B cells (IgD^− CD27^− CD24^− CD38^−; DN2) significantly increased in LC (absolute count)
- CD4^+ central memory T cells (CD45RA^− CD127^+ CCR7^+) significantly lower in LC: 27% vs. 33% (CC) vs. 32% (HC)
- Absolute exhausted CD4^+ T cells significantly elevated in LC
- CD4^+ T cells from LC produced significantly higher intracellular IL-2 (17%), IL-4 (11%), and IL-6 (1.2%) vs. CC upon PMA/ionomycin stimulation; IL-4/IL-6 double-positive CD4^+ T cells elevated (0.3% LC vs. 0.2% CC and HC)

**SARS-CoV-2 antibody responses:**
- Anti-S1 IgG and total anti-S IgG significantly higher in vaccinated LC vs. CC (Kruskal–Wallis P < 0.0001)
- Anti-RBD IgG elevated in LC but not significantly vs. CC
- Anti-N IgG significantly higher in unvaccinated LC vs. pre-pandemic controls (P = 0.0004)
- PIWAS spike epitope mapping: LC enriched for KFLPFQQ (P = 0.023), RDPQTLE (P = 0.00058), LDK[WY]F (P = 0.0034), and DISGI (P = 0.0086) motifs — mapping to surface-exposed regions near S1/S2 cleavage site and furin cleavage site (residues 556–572 and 625–638/680–690), consistent with persistent viral antigens
- Linear models confirm LC status is a significant positive predictor of anti-spike humoral response after accounting for demographics and vaccination

**Cortisol and soluble immune mediators:**
- Cortisol significantly lower in LC vs. HC and CC (Kruskal–Wallis P < 0.0001); significant after controlling for age, sex, BMI, sample-collection time, and cohort
- Cortisol alone achieves AUC 0.96 (95% CI 0.93–0.99) for LC prediction
- ACTH levels did not differ significantly across groups (MY-LC cohort only), suggesting possible blunting of hypothalamic-pituitary-adrenal axis regulation
- Additional significant differences: complement C4b elevated (P < 0.0001), CCL19 elevated (P = 0.00058), galectin-1 elevated (P = 0.0015), CCL20 elevated (P = 0.0032), CCL4 elevated (P = 0.0092), APRIL elevated (P = 0.013), LH elevated (P = 0.022), IL-5 marginally elevated (P = 0.024) in LC

**Autoantibodies against exoproteome:**
- Total number of autoantibody reactivities per participant did not differ significantly between LC and controls (Kruskal–Wallis P = 0.99)
- No individual autoantibody reactivity was significantly more frequent in LC vs. controls (Fisher's exact)
- GPCR autoantibodies also did not differ between LC and controls

**Herpesvirus antibody responses:**
- REAP scores for EBV antigens significantly elevated in LC: EBV minor viral capsid antigen gp23 (P = 4.62 × 10^−3), EBV fusion-receptor component gp42 (P = 3.2 × 10^−2), and VZV glycoprotein E (P = 1.51 × 10^−2)
- SERA z-scores for EBV gp42 PVXF[ND]K motif significantly elevated in LC (P = 0.031, P = 0.0072 for individual comparisons)
- Anti-EBV IgM not elevated and no evidence of EBV viraemia (SERA measurement) → pattern consistent with recent latent EBV reactivation rather than acute infection
- EBV p23 REAP score correlated with terminally differentiated effector memory T cells (T_EMRA; CD4^+ subset; R = 0.26, P = 0.018)
- EBV gp42 PVXF[ND]K z-score correlated with IL-4/IL-6 double-positive CD4^+ T cells (R = 0.26, P = 0.013) — correlation not seen in controls
- HSV-1 lower REAP reactivity in LC explained by lower HSV-1 seroprevalence in LC group

**Machine learning classification:**
- k-NN classifier on matched cohort: AUC 0.94 (95% CI 0.84–1.00)
- PCA: flow cytometry (pseudo-R^2 = 59%) and plasma proteomics/hormones (pseudo-R^2 = 74%) most informative data segments
- LASSO model pseudo-R^2 = 82%; final parsimonious model identified features: cortisol (down in LC), cDC1 (down), CD8^+ T cells (down), PD-1^+ CD4^+ T_CM cells (down), galectin-1 (up), APRIL (up), CCL23 (up), CD4^+ T cells (up), EBV gp42 PVXF[ND]K (up), EBV p23 (up)
- Classification accuracies agreed between immunological data models and patient-reported outcome models (Cohen's kappa = 0.52; 95% CI 0.33–0.72)
- External validation (EXT-LC) confirmed cortisol decreases but galectin-1 and EBV gp42 were MY-LC-specific, possibly reflecting clinical phenotype differences between cohorts

## Relevance

This paper is directly central to the project research question (research-question:post-acute-infection-syndromes): "Why do some people fail to recover after acute infection, and what shared mechanisms drive post-acute infection syndromes?"

**Connection to the PAIS frame of failed homeostatic recovery:**

1. **Persistent immune activation as a failure-to-resolve signal.** Elevated non-conventional monocytes, activated B cell subsets, and double-negative B cells more than one year post-infection are canonical markers of chronic immune activation — the system has not returned to its pre-infection set point. Reduced cDC1 and central memory CD4^+ T cells may reflect ongoing consumptive immune demand.

2. **HPA axis dysregulation as a systemic homeostatic failure.** The robust cortisol deficit (AUC 0.96 for LC vs. non-LC) with non-compensatory ACTH suggests that the hypothalamic-pituitary-adrenal axis — a key mediator of both immune regulation and stress recovery — is persistently blunted. This is a direct biological correlate of failed neuroendocrine homeostasis following acute infection.

3. **Antigen/pathogen persistence hypothesis.** Exaggerated anti-spike humoral responses (anti-S1, anti-S, PIWAS enrichment near furin cleavage site) >1 year post-infection are consistent with ongoing antigen stimulation from tissue-resident viral reservoirs — one of the four canonical PAIS mechanisms proposed by Choutka et al. (cite:Choutka2022).

4. **Latent herpesvirus reactivation hypothesis.** Elevated EBV lytic antigen reactivity without acute EBV infection markers is the most direct empirical support yet in a controlled LC cohort for EBV reactivation as a contributing mechanism — specifically the third PAIS hypothesis (latent virus reactivation). The correlation with IL-4/IL-6-skewed T helper activity suggests EBV reactivation may sustain or amplify a Th2-skewed, non-resolving inflammatory state.

5. **Biomarker gap / translational opportunity.** The multi-omic ML panel (cortisol + galectin-1 + EBV antibodies + circulating immune cell subsets) provides concrete candidate biomarkers for the diagnostic gap the project aims to address. Cortisol is particularly valuable: a simple, clinically accessible measure with near-perfect individual-level discriminative performance.

6. **Shared-failure-mode vs. pathogen-specific frame.** The findings parallel immune perturbations described in ME/CFS and other PAISs (e.g., non-conventional monocyte elevation, T_EMRA expansion, HPA axis blunting), supporting the project's working hypothesis that long COVID is one instantiation of a shared post-infectious dysregulated attractor.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Long COVID (LC) as PAIS | post-acute infection syndrome | Direct instance; MY-LC study provides quantitative immune signature |
| Persistent immune activation (elevated non-conventional monocytes, activated B cells, exhausted CD4^+ T cells) | failed immune resolution / chronic immune activation | Primary cellular signature of failed homeostatic recovery |
| Reduced cortisol with non-compensatory ACTH | HPA axis dysregulation / neuroendocrine homeostatic failure | Strongest single biomarker; suggests systemic regulatory failure beyond immune compartment |
| Exaggerated anti-spike antibodies / PIWAS enrichment near furin cleavage site | antigen/pathogen persistence | Supports persistence hypothesis; surface-exposed epitopes → possible tissue-reservoir antigen |
| EBV lytic antigen reactivation without acute infection markers | latent herpesvirus reactivation | Second strongest mechanistic signal; consistent with Choutka2022 mechanism 3 |
| IL-4/IL-6 double-positive CD4^+ T cells correlated with EBV gp42 | Th2-skewed / non-resolving inflammatory state | Possible EBV-driven immune polarization sustaining PAIS |
| Reduced cDC1 | impaired antigen presentation / innate immune failure | May contribute to viral antigen clearance failure |
| Integrated LASSO biomarker model (AUC 0.94) | diagnostic gap / biomarker panel | Provides framework for future objective LC/PAIS diagnosis |
| LC propensity score (LCPS; AUC 0.95) | quantitative PAIS severity metric | Enables dimensional rather than categorical analysis |
| Symptom clusters (LC-C1, LC-C2, LC-C3) | PAIS subtype heterogeneity | Three clusters with differing LCPS distributions; subtype-specific mechanisms need further study |
| Cortisol deficit (AUC 0.96) | neuroendocrine dysregulation biomarker | Clinically accessible; aligns with hypocortisolism reported in ME/CFS and post-SARS |
| Absence of individual autoantibody enrichment | autoimmunity hypothesis not supported by this assay | REAP screens secreted/extracellular proteins; intracellular targets not assessed |

## Limitations

- **Convenience sampling and cross-sectional design.** Participants were recruited through long-COVID clinics and advocacy groups; CC and LC recruitment strategies differed, introducing potential selection bias. No longitudinal tracking of individual immune trajectories; cannot determine whether observed immune perturbations preceded or resulted from persistent symptoms.
- **Modest sample sizes for ML.** The matched subset used for the LASSO model comprised 40 HC, 39 CC, and 79 LC — substantially fewer independent observations than typical machine learning training sets (several thousands). Generalizability and robustness may be limited.
- **Peripheral blood only.** Flow cytometry and proteomics assess circulating immune cells; LC commonly presents with organ-specific dysfunction (pulmonary, neurological, gastrointestinal) where tissue-resident immune perturbations would not be captured. Cerebrospinal fluid from LC participants showed elevated TIGIT^+ CD8^+ T cells (cited from another study), reinforcing this gap.
- **Exoproteome autoantibody screen limited to secreted/extracellular proteins.** Whether autoantibodies targeting intracellular antigens, nuclear proteins, or non-exoproteome membrane receptors contribute to LC pathogenesis was not assessed. GPCR autoantibodies (implicated in other studies) were not significantly elevated here, but only a subset of GPCR epitopes was probed.
- **ACTH measurements only in MY-LC cohort, not EXT-LC.** ACTH has a very short plasma half-life, limiting the reliability of these measurements. The suggestion of blunted HPA axis feedback is therefore preliminary and requires dedicated studies with dynamic HPA testing.
- **EBV reactivation inference is indirect.** Higher EBV lytic antigen reactivity was observed in seropositive participants without EBV viraemia or elevated IgM; the authors interpret this as latent reactivation but cannot exclude local/salivary EBV shedding or differential baseline seroprevalence contributing to the signal.
- **External validation (EXT-LC) partial.** Cortisol decrease replicated, but galectin-1 and EBV gp42 signals were cohort-specific, likely reflecting clinical phenotype differences. The biomarker panel requires validation in larger, independent, multi-site cohorts.
- **Acute COVID-19 severity confounding.** Although 87% of LC cases had mild initial illness, the study did not exclude potential residual confounding from heterogeneous severity within the mild range or differences in infecting variant.
- **Case definition.** Long COVID defined by self-reported persistent symptoms + clinical evaluation; no single standardized diagnostic criterion (e.g., WHO definition) was applied uniformly, consistent with field-wide challenges but limiting cross-study comparability.

## Model / Tool Availability

- Data and code availability: Source data, extended data figures, and supplementary materials are available at https://doi.org/10.1038/s41586-023-06651-y (open access).
- The PIWAS (peptide immunome-wide association study) methodology and SERA (serum epitope repertoire analysis) platform are third-party tools described in the Methods; SERA is a commercially available platform (SerImmune).
- REAP (rapid extracellular antigen profiling) was developed by the Ring lab (Yale); the assay covers >6,000 extracellular/secreted human proteins using a yeast display library.
- No pre-trained ML model or standalone software tool is released for clinical use; the LASSO model parameters are described in Extended Data Table 7.

## Follow-up

- **Longitudinal design needed:** A prospective cohort tracking immune parameters from acute infection through recovery (or non-recovery) would enable causal inference about whether the immune perturbations observed here precede or follow symptom persistence — the key question for mechanistic understanding and intervention timing.
- **HPA axis deep phenotyping:** Dynamic HPA testing (e.g., low-dose ACTH stimulation, CRH challenge, 24-hour urine cortisol) in an LC cohort would validate the cortisol deficit and determine whether it reflects primary adrenal insufficiency, central blunting, or altered cortisol-binding protein levels (as seen in post-SARS, per Leow et al. 2005).
- **Tissue-level studies:** Pairing peripheral immune profiling with tissue biopsies (gut, lung, lymph node) would address the antigen-persistence question directly — whether PIWAS-enriched spike epitopes correspond to tissue-resident antigen depots.
- **EBV mechanistic dissection:** Determine whether EBV reactivation drives IL-4/IL-6-skewed T helper polarization or is merely a bystander of an already dysregulated immune environment; experiments using EBV-specific T cell depletion / antiviral intervention in LC models could distinguish these.
- **Cross-PAIS comparison:** Apply the MY-LC biomarker panel (cortisol, galectin-1, non-conventional monocytes, cDC1, EBV antibodies) to ME/CFS, post-Q-fever, and post-treatment Lyme cohorts to test whether the "shared PAIS attractor" hypothesis holds at the immunological level.
- **Related papers:** Peluso et al. 2024 (cite:Peluso2024; viral persistence / tissue reservoir SARS-CoV-2); Choutka et al. 2022 (cite:Choutka2022; PAIS mechanistic framework); Komaroff & Lipkin 2023 (ME/CFS and long COVID overlap); Su et al. 2022 (multi-omics of mild/moderate COVID-19 recovery).
