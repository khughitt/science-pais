---
id: paper:Talla2023
kind: paper
title: Persistent serum protein signatures define an inflammatory subcategory of long
  COVID
status: active
ontology_terms:
- post-acute sequelae of SARS-CoV-2 (PASC)
- serum proteomics
- type II interferon signaling
- NF-kB canonical pathway
- neutrophil activation / NETosis
- persistent inflammation
- cytokine / chemokine dysregulation
- diagnostic biomarker panel
dataset_usage: []
datasets: []
source_refs:
- cite:Talla2023
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Persistent serum protein signatures define an inflammatory subcategory of long COVID

<!--
- **Authors:** Talla, Aarthi et al. (Allen Institute for Immunology; Fred Hutch Cancer Center)
- **Year:** 2023
- **Journal:** Nature Communications, 14:3417
- **DOI/URL:** https://doi.org/10.1038/s41467-023-38682-4
- **BibTeX key:** Talla2023
- **Source:** PDF
-->

## Key Contribution

Using the Olink Explore 1536 serum proteomics platform applied to a longitudinal cohort of 55 PASC individuals with symptoms >=60 days post-symptom onset (PSO), 24 recovered COVID-19 individuals, and 22 uninfected controls, this study demonstrates that PASC is biologically heterogeneous: approximately 65% of PASC participants cluster into two distinct inflammatory subgroups (clusters 4 and 5) defined by persistent elevation of type II IFN (IFN-gamma), NF-kB, TNF signaling, and — especially in cluster 5 — a neutrophil activation / NETosis signature with type I IFN involvement. The remaining ~35% of PASC participants show no distinguishable inflammatory protein signature relative to recovered or uninfected individuals. The inflammatory serum protein signature persists longitudinally (assessed up to 275 days PSO) and is replicated in an independent INCOV cohort (Su et al. 2022, n = 204 COVID-19 participants, 289 healthy controls), where the equivalent inflammatory cluster was enriched for more-severe acute disease (WHO ordinal scale >=3). A three-protein diagnostic panel (CCL7, CD40LG, S100A12) achieves AUROC 0.865 (95% CI 0.765-0.966) in training and 0.788 (95% CI 0.590-0.985) in the independent test cohort for distinguishing inflammatory from non-inflammatory PASC.

## Methods

**Cohort:** Seattle COVID-19 Cohort (Allen Institute / Fred Hutch IRB IR10440). 55 unvaccinated adults with PASC (21 M, 34 F; age 22-82 years; symptoms >=60 days after PCR-confirmed ancestral-strain SARS-CoV-2 infection); 24 PCR-confirmed COVID-19 recovered individuals (9 M, 15 F); 22 PCR-negative uninfected controls (12 M, 10 F). Predominantly mild acute disease (WHO ordinal scale 2-3); only 3 participants hospitalized. Longitudinal serum draws from as early as acute infection through 379 days PSO.

**Proteomics:** Olink Explore 1536 platform (proximity extension assay with next-generation sequencing readout), measuring 1,472 serum proteins across inflammation, oncology, cardiometabolic, and neurology panels. Normalized Protein Expression (NPX) values reported as log2 normalized relative quantities. Two batches bridged with 42 cohort samples run in both.

**Bioinformatics pipeline:**
1. Used curated canonical MolSigDB (MSigDB) pathways with pAUC rule-in statistical approach (90-100% specificity window, 99% CI two-sided) to identify 85 pathways that distinguish PASC from recovered and uninfected. After Jaccard-based enrichment map merging (threshold 25%), 54 pathway modules were produced.
2. Unsupervised k-means clustering (k=5, ssGSEA scores per module) on the full cohort (PASC + recovered + uninfected) using the first >=60-day sample per PASC participant and last >=60-day sample per recovered participant.
3. Differentially expressed proteins (DEPs) per cluster identified by Wilcoxon test with Benjamini-Hochberg multiple testing correction (adjusted p <0.05).
4. Longitudinal ssGSEA module scores assessed on all available samples per participant (beginning from early acute infection through 275 days PSO).

**Validation cohort:** INCOV (Su et al. 2022) — 204 SARS-CoV-2-infected participants, 289 healthy controls; 75 met >=60-day PASC criteria with Olink proteomic data (plasma, qPCR-quantified). 163 proteins overlapped with the inflammatory DEPs from clusters 4 & 5; k-means clustering with k=5 on those 163 proteins.

**Diagnostic panel:** Candidate proteins (n=35) identified in both cohorts with adjusted p<0.008; subset (n=15) with literature support as COVID-19/PASC biomarkers. Logistic regression (LogReg) with 10-fold cross-validation and stepwise elimination; training n=36 inflammatory + 19 non-inflammatory PASC; test n=34 inflammatory + 9 non-inflammatory INCOV PASC.

**Additional assays:** SARS-CoV-2 RBD-specific IgG ELISA (serum ~day 60 PSO); SARS-CoV-2-specific CD4+/CD8+ T-cell intracellular cytokine staining (ICS) by flow cytometry (MIMOSA analysis). Clinical activity score for acute COVID based on ADL impact.

## Key Findings

**Heterogeneity of PASC by serum proteome:**
- k-means clustering (k=5) on 54 pathway modules identified 5 clusters across the full cohort. Clusters 4 and 5 were enriched for PASC participants (91% and 80% respectively), accounting for ~65% of PASC participants. Clusters 1-3 were dominated by uninfected and recovered individuals (with 35% of PASC).
- The inflammatory serum signatures within clusters 4 and 5 were stable over the longitudinal study period; most individuals remained in the same cluster.

**Cluster 4 — IFN-gamma-dominated inflammatory PASC:**
- Most significantly enriched modules: Type II interferon (IFN-gamma) signaling (M32), IL-27 pathway (M30), TID pathway (M33), cytokine pathway (M31), allograft rejection (M37), ILC family (M29), regulation of IFN-gamma signaling (M34). NF-kB canonical (M15) and TNF (M11) also enriched.
- Top differentially expressed proteins include: IFNG (IFN-gamma, most highly expressed and most differentially expressed single protein in cluster 4), IL12B, IL27, CXCL9, CXCL10, CXCL11, IL-6, CCL7 (MCP-3), TNF, multiple TNF receptor superfamily members (TNFRSF1A/1B, TNFRSF4/8/10A/10B/11A/13B), IL32, IL18BP, CCL20.
- IFN-gamma and IFN-gamma-driven chemokines (CXCL9, CXCL10, CXCL11, IL27, IL12 p40) were consistently elevated longitudinally in inflammatory PASC vs. non-inflammatory PASC and recovered individuals over the entire observation period (up to 275 days PSO).
- CD74, CD5, TIM-3 (HAVCR2), PDCD1, CD83 (checkpoint molecules and activation markers) elevated in cluster 4, suggesting ongoing adaptive immune activation.
- Participants in cluster 4 were significantly older (Wilcoxon, p-values shown in Fig. 1G/I) and age-associated inflammatory proteins (CXCL9, CXCL10, IL18BP) were positively correlated with age.

**Cluster 5 — Neutrophil activation / NETosis + type I IFN inflammatory PASC:**
- Dominant modules: NF-kB canonical (M15), TNF signaling (M11), IL18 pathway (M03), TID pathway (M33), IL1 signaling/TLR cascade (M4), anthrax pathway (M5). Type I IFN signature (regulation of IFNA signaling, M12) also enriched.
- Top differentially expressed proteins beyond cytokines/chemokines: ANXA3 (annexin-3), ANXA11 (annexin-11) — both involved in neutrophil granule calcium-dependent degranulation; MMP8 (neutrophil collagenase), MPO, SERPINB1 (neutrophil serine protease inhibitor), SNAP23, STX8, SNAP29 (membrane/vesicle trafficking). This composite signature is consistent with persistent neutrophil activation, degranulation, and possible NETosis.
- Type I IFN-associated proteins (SAMD9L, DDX58, MNDA, LAMP3) elevated at the earliest sampling timepoints and remained elevated for approximately 180 days post-infection.
- IL-6, TNF, CCL7 also elevated in cluster 5 (TNF and IL-6 less prominent than cluster 4 in cross-sectional view but persistently elevated longitudinally).

**Shared inflammatory features across clusters 4 and 5:**
- IL-12/IFN-gamma axis highly active in both; combined with NF-kB-driven cytokine expression (IL-18, TNF, IL-1), possibly TNF-driven NF-kB activation leading to excess IL-6.
- IFN-gamma and TNF-driven cytokines elevated persistently vs. non-inflammatory PASC and recovered; differences grew more distinct with longer follow-up.

**Clinical and demographic correlates of inflammatory PASC:**
- Inflammatory PASC participants (clusters 4+5) had significantly higher pre-PASC clinical activity score (ADL impact) than non-inflammatory (Wilcoxon p=0.002), indicating more symptomatic acute COVID-19.
- BMI significantly higher in inflammatory clusters (p=0.008, Fig. 1D); leptin and FABP4 elevated; Leptin signaling module (M6) significantly correlated with BMI (Spearman rho=0.5, p<0.0001, Fig. 1F). BMI does not fully account for the full inflammatory signature.
- No significant difference in RBD-specific IgG, CD4+ or CD8+ T-cell frequencies between inflammatory and non-inflammatory PASC or recovered individuals, suggesting humoral/cellular adaptive responses against spike do not distinguish the inflammatory subset.

**Independent cohort validation (INCOV):**
- k-means clustering of 163 overlapping proteins (INCOV n=75 PASC-qualifying) identified 5 clusters; INCOV cluster E was made up of 64.2% PASC participants and 35.85% INCOV recovered, equivalent to inflammatory clusters 4+5.
- INCOV cluster E significantly enriched for acute WHO ordinal scale >=3 (more severe acute disease vs. mild clusters B, C, D; Fig. 5D).
- Key proteins TNF, IL12B, CCL7, CXCL11, CXCL10, IFNG, and DDX58, LAMP3, etc. significantly elevated in cluster E vs. other INCOV clusters (Wilcoxon p<0.05).

**3-protein diagnostic panel (CCL7, CD40LG, S100A12):**
- All three proteins persistently elevated in inflammatory PASC clusters at >=60 days PSO and remained elevated through 250+ days (Fig. 6B).
- LogReg model AUROC: training 0.865 (95% CI 0.765-0.966); test (INCOV) 0.788 (95% CI 0.590-0.985).
- LogReg probability scores significantly higher in inflammatory vs. non-inflammatory PASC (training p<0.0001; test p=0.007).

## Relevance

This paper directly addresses the PAIS frame of **failed homeostatic recovery after acute infection** in several ways:

1. **Homeostatic failure sub-typing:** The central finding — that ~65% of PASC individuals display persistent, molecularly-defined inflammatory protein signatures 60-275+ days post-infection — provides a direct molecular readout of failed post-infection immune homeostasis. The signatures are not acute-phase responses but persistent states, distinguishing true "failure to recover" from delayed recovery.

2. **Mechanism specificity:** The two inflammatory sub-clusters map to distinct failure modes within the shared PAIS frame: cluster 4 represents a failure to resolve adaptive/IFN-gamma-driven inflammation (possibly antigen-driven T-cell effector persistence), while cluster 5 represents failure to resolve innate inflammatory programs (neutrophil hyperactivation, NETosis, type I IFN persistence — possibly related to viral antigen or RNA persistence).

3. **Antigen persistence hypothesis:** The persistence of type I IFN-associated proteins (SAMD9L, DDX58, MNDA) in cluster 5 participants from the earliest sampling through ~180 days PSO parallels reports of SARS-CoV-2 RNA and spike protein persistence in tissues up to 1 year post-infection. This connects directly to the antigen/pathogen persistence mechanism in the PAIS framework.

4. **Stratification for trials:** The 3-protein diagnostic panel (CCL7, CD40LG, S100A12) directly enables patient stratification for immunomodulatory interventions, a key goal of research-question:post-acute-infection-syndromes. JAK inhibitors or targeted cytokine blockade (anti-TNF, anti-IL-6, anti-IFN-gamma) are highlighted as potential therapeutic candidates for the inflammatory subtype.

5. **Cross-syndrome relevance:** The persistent IFN-gamma/NF-kB/TNF inflammatory signatures overlap with immune dysregulation described in ME/CFS and other PAIS, supporting the shared-failure-mode framing of the project. The non-inflammatory PASC subgroup (~35%) may instead reflect tissue damage, dysautonomia, or other mechanisms studied elsewhere in the project.

6. **Biomarker utility:** This is the first study to demonstrate that a small (3-protein) serum panel can prospectively stratify PASC participants into biologically meaningful subgroups with AUROC ~0.79-0.87, validated in an independent cohort — enabling mechanistic substratification in future PAIS studies.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PASC (post-acute sequelae of SARS-CoV-2) | Post-acute infection syndrome (PAIS) | PASC is the COVID-19 instance of PAIS |
| Inflammatory PASC (clusters 4 & 5, ~65%) | Failed homeostatic recovery — immune axis | Persistent molecular inflammation defines the failure mode |
| Non-inflammatory PASC (clusters 2 & 3, ~35%) | Failed homeostatic recovery — non-immune axis | Tissue damage, dysautonomia, or other mechanisms |
| Type II IFN (IFN-gamma) signaling module (M32) | Persistent adaptive immune activation | Driven by antigen-presenting cells + CD4/CD8 effectors |
| NF-kB canonical pathway (M15) + TNF signaling (M11) | Chronic innate/inflammatory pathway activation | Convergence point for multiple upstream danger signals |
| Neutrophil activation signature (ANXA3, MMP8, MPO, SERPINB1) | Innate immune dysregulation / NETosis | Cluster 5 hallmark; potential connection to coagulopathy |
| Type I IFN-associated proteins (SAMD9L, DDX58) | Antigen/pathogen persistence signal | Type I IFNs induced by viral RNA/proteins; early and persistent |
| 3-protein panel (CCL7, CD40LG, S100A12) | Inflammatory PAIS biomarkers | Practical stratification tool for clinical trials |
| Clinical activity score (ADL impact) | Acute disease severity covariate | Higher score in inflammatory PASC confirms severity-inflammation link |
| BMI as risk factor for inflammatory PASC | Host metabolic state covariate | Confounds but does not explain full inflammatory signature |
| INCOV cohort replication | External validation | More severe acute illness (WHO >=3) enriched in inflammatory cluster |

## Limitations

1. **Small cohort, predominantly mild disease:** 55 PASC participants, mostly WHO ordinal scale 2-3. The INCOV validation covers a wider severity range, but both datasets are modest in size for sub-clustering. The 3-protein panel requires validation in larger, more diverse cohorts before clinical deployment.
2. **Ancestral-strain only:** All participants were infected with the ancestral SARS-CoV-2 strain. Inflammatory subtypes and protein signatures may differ for Delta, Omicron, or subsequent variants.
3. **All unvaccinated:** Cohort was enrolled before vaccines were available. Whether vaccination modifies the inflammatory PASC subtype distribution is unknown.
4. **Cross-assay comparison for INCOV validation:** Main cohort used serum + NGS readout; INCOV used plasma + qPCR readout. Olink advises against direct cross-cohort NPX comparison; authors addressed this by performing independent within-cohort clustering.
5. **Symptom clustering does not drive biological clustering:** Symptom categories alone (respiratory, cardiovascular, neurological, etc.) did not distinguish the inflammatory from non-inflammatory PASC groups (Supplemental Figs. S2B-D), indicating that clinical phenotyping alone is insufficient and that molecular biomarkers are required.
6. **Missing mechanistic driver experiment:** The study is observational/correlational. Whether persistent viral antigen, autoantibodies, reactivated herpesviruses, or another trigger maintains the inflammatory state is not directly tested.
7. **No T-cell or B-cell resolution of mechanism:** SARS-CoV-2-specific CD4+/CD8+ T cell frequencies did not differ between inflammatory and non-inflammatory PASC (Supplemental Fig. S3C-D), suggesting bulk T-cell quantities are not the discriminator — but T-cell functional state, exhaustion, or specificity were not fully resolved.
8. **Batch design bias:** Two-batch design introduced group bias by disease status (p<0.05); batch correction via 42 bridging samples was applied but residual batch effects cannot be fully excluded.
9. **Generalizability:** All participants were adults in the greater Seattle area, limiting demographic generalizability.

## Model / Tool Availability

- **Processed Olink data and source data:** Deposited in Zenodo (https://doi.org/10.5281/zenodo.7872791).
- **R code for analysis and figure generation:** Available at Zenodo (same DOI) and GitHub: https://github.com/aifimmunology/PASC-proteomics-talla-vasaikar-et-al
- **Input canonical pathways genesets database:** c2.cp.v7.2.symbols from MSigDB (v7.2), publicly available.
- **INCOV (Su et al. 2022) Olink data:** Used with permission; publicly available through original publication.
- No trained machine learning models are deposited as standalone artifacts; R code for the logistic regression is available in the GitHub repository.

## Follow-up

- Peluso et al. 2024 (cite:Peluso2024) on plasma antigen persistence in PASC — directly tests whether viral antigen persistence drives inflammatory signatures like those in cluster 5.
- Peppercorn et al. 2023 (cite:Peppercorn2023) on PBMC proteome in long COVID with ME/CFS comparison — complementary intracellular proteomics.
- Ryan et al. 2022 (cite:Ryan2022) on long-term peripheral immune perturbation — longitudinal immune cell phenotyping that complements this serum proteomics study.
- Su et al. 2022 (INCOV cohort, not separately summarized) — the validation dataset used here; would benefit from a dedicated summary.
- Whether the 3-protein panel (CCL7, CD40LG, S100A12) performs in variant-era PASC cohorts or in other PAIS (ME/CFS, post-Lyme) is an open question relevant to the shared-failure-mode hypothesis.
- The neutrophil/NETosis cluster 5 signature (MMP8, MPO, SERPINB1, ANXA3, ANXA11) connects to thromboinflammation literature (Nicolai 2023, cite:Nicolai2023) — worth cross-referencing.
