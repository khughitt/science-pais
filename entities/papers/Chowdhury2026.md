---
id: "paper:Chowdhury2026"
kind: "paper"
title: "Distinct plasma proteome signature at 3 months post-COVID-19 infection irrespective of post-COVID condition"
status: active
ontology_terms:
  - plasma proteomics
  - DIA mass spectrometry
  - post-COVID condition
  - oxidative stress
  - complement activation
  - coagulation cascade
  - antioxidant response
  - biomarker discovery
  - SARS-CoV-2 convalescence
dataset_usage: []
datasets: []
source_refs:
  - cite:Chowdhury2026
related:
  - topic:long-covid-immune-dysregulation
  - topic:biomarkers-and-objective-endpoints
  - topic:shared-failure-mode-across-pais
  - question:0001-shared-molecular-signature-across-triggers
  - hypothesis:0001-shared-dysregulated-attractor
  - paper:Talla2023
  - paper:Klein2023
created: "2026-06-20"
updated: "2026-06-20"
---

# Distinct plasma proteome signature at 3 months post-COVID-19 infection irrespective of post-COVID condition

- **Authors:** Mohammad Mobarak H. Chowdhury, Akouavi Julite Irmine Quenum, Christine Rioux-Perreault, Jean-François Lucier, Subburaj Ilangumaran, Alain Piché, Hugues Allard-Chamard, Sheela Ramanathan
- **Year:** 2026
- **Journal:** Scientific Reports, 16:18201
- **DOI/URL:** https://doi.org/10.1038/s41598-026-46180-y
- **BibTeX key:** Chowdhury2026
- **Source:** Full-text PDF (papers/pdfs/2026_Chowdhury_plasma-proteome-3month-postcovid.pdf), read 2026-06-20.

## Key Contribution

DIA-MS plasma proteomics at 3 months post-infection reveals a robust, persistent proteome signature distinguishing SARS-CoV-2-experienced individuals (both convalescent and PCC) from never-infected controls, but that signature does **not** discriminate individuals with post-COVID condition (PCC) from those who fully recovered (convalescent). The study therefore constitutes a partly-negative result for the hypothesis that PCC carries a proteome-level signature large enough to separate it from uncomplicated recovery at this time point; only 2 proteins differ between PCC and convalescent groups while 49–53 differ between either infected group and uninfected controls. A subsidiary finding is that both infected groups show elevated oxidative stress markers relative to uninfected controls, with PCC exhibiting the strongest oxidative stress signal.

## Methods

**Design:** Cross-sectional plasma proteomics of three groups sampled at 3 months post-PCR-confirmed mild (non-hospitalised) SARS-CoV-2 infection, recruited from the Biobanque Québécoise de la COVID-19 (BQC19) at the Université de Sherbrooke Hospital Research Center, March 2020 – October 2021.

**Cohort (n = 150 unique samples after exclusions):**
- Uninfected controls (Un-inf): n = 35 (SARS-CoV-2 PCR-negative; 60% female; ages 18–73)
- Convalescent (Conv): n = 62 (PCR-confirmed prior infection; symptom-free at 3 months; 41.9% female; ages 18–81)
- Post-COVID Condition (PCC): n = 53 (PCR-confirmed prior infection; persistent symptoms meeting WHO criteria at 3 months; 64.1% female; ages 18–88; mean 2.9 ± 2.8 symptoms)

All infections were mild (WHO severity classification: asymptomatic, mild, or moderate); no hospitalised individuals were included. Case definition of PCC follows the WHO October 2021 criteria.

**Proteomics:** Data-independent acquisition mass spectrometry (DIA-MS) on a TimsTOF Pro (Bruker Daltonics, diaPASEF mode). Sample preparation: 75 µg plasma protein per sample, Lowry assay, reduction (DTT), alkylation (ClAA), Pierce MS-grade trypsin digestion, C18 solid-phase extraction. Analysis by HPLC-nanoElute with a 2-h ACN gradient. Raw data processed with DIA-NN v1.8.1 using the human proteome (UniProt UP000005640, 96,418 entries) at 1% global FDR. Output: 235 unique proteins quantified across groups (n = 150 unique samples; 20 repeated samples used for validation only and excluded from final analysis).

**Validation:** ELISA for six selected proteins — GAPDH, PCSK9, DPP4, CPB2, C1QA, CST3 — in a subset (40 PCC, 20 Conv, 20 Un-inf).

**Oxidative stress assays:** Plasma GSH and GSSG by colorimetric assay (Glutathione Colorimetric Detection Kit, Invitrogen); 8-hydroxy-2'-deoxyguanosine (8-OHdG) by competitive ELISA (Stressmarq Biosciences); Cu/Zn SOD by ELISA (Invitrogen).

**Pathway / network analysis:** GO enrichment and gene set enrichment via SRplot; protein–protein interaction (PPI) networks with STRING v12.2 visualised in Cytoscape 3.10.2; hub proteins ranked by CytoHubba degree centrality.

**Statistics:** One-way ANOVA with Tukey's post-hoc test; significance threshold p ≤ 0.05; GraphPad Prism v10.0.3.

## Key Findings

**PCA and overall structure:**
- PCA (PC1 12.7%, PC2 9.8%) clearly separates uninfected controls from both Conv and PCC groups.
- Conv and PCC groups cluster together and show minimal mutual separation, indicating near-identical global proteomic profiles at 3 months post-infection.

**Differentially expressed proteins (DEPs) — headline counts:**
- Conv vs Un-inf: 49 DEPs (26 up, 23 down relative to uninfected)
- PCC vs Un-inf: 53 DEPs (21 up, 32 down relative to uninfected)
- PCC vs Conv: **only 2 DEPs** (VNN1 up, CST3 up in PCC relative to Conv)
- 224 proteins are shared across all three groups; only 8 proteins exclusive to the Conv+PCC intersection vs uninfected

**The PCC-vs-Conv null:** The Venn diagram of significant DEPs shows almost complete overlap between the two infected groups' signatures. There is broad sharing of DEP identities when each infected group is compared to uninfected controls, confirming that proteomic changes from mild COVID-19 persist for at least 3 months but do not differentiate PCC from uncomplicated recovery at the whole-proteome level.

**Prominent proteins in the post-infection signature (shared Conv and PCC vs Un-inf):**
- Downregulated: PRDX6 (peroxiredoxin 6; antioxidant enzyme) — significantly down in both infected groups vs uninfected (p < 0.0001)
- Upregulated: PON3 (paraoxonase-3; oxidative stress response) — significantly elevated in both infected groups (p < 0.0001); PON3 PCC ≈ Conv (p = 0.97)
- VNN1 (vanin-1; oxidative stress sensor) — upregulated in PCC vs uninfected (p = 0.039); the sole robust directional difference between PCC and Conv (p = 0.63 Conv vs Un-inf)
- PCSK9, CST3, C1QA, CPB2, KNG1, GAPDH — differentially expressed in both infected groups

**Key proteins validated by ELISA:**
- GAPDH: peptide intensity elevated in PCC > Conv > Un-inf by DIA-MS; ELISA detected GAPDH in infected but not uninfected individuals, with differences between PCC and Conv groups (DIA-MS trend reproduced)
- CPB2 (carboxypeptidase B2, coagulation/fibrinolysis): significantly elevated in PCC vs Un-inf by both DIA-MS and ELISA; both infected groups elevated vs uninfected by ELISA
- C1QA: significantly elevated in PCC and Conv vs Un-inf by DIA-MS; ELISA showed comparable elevations in both infected groups
- CST3 (cystatin C): upregulated by DIA-MS in both groups; ELISA showed discordant (reduced) levels — likely reflecting post-translational or epitope-accessibility differences
- PCSK9: elevated by DIA-MS in both infected groups; ELISA did not confirm significance — possible assay mismatch
- DPP4: not detected in uninfected by DIA-MS but detected in all groups by ELISA

**Pathway enrichment (GO Biological Process):**
- Both infected groups: enrichment for humoral immune response, complement activation (classical pathway), immunoglobulin-mediated immune response, B cell–mediated immunity, phagocytosis, regulation of complement activation
- PCC hub proteins (CytoHubba): GSN, TGFBI, CST3, PCSK9, LYZ, PF4, ITIH4, HSPG2, C1QA, KNG1 (top 10 by degree)
- Conv hub proteins: similar set including GAPDH, PCSK9, TGFBI, GSN, CST3, LYZ, HSPG2, PPBP, PF4, KNG1

**Oxidative stress (biochemical assays):**
- Plasma GSH: no PCC vs Conv difference (p = 0.90); both PCC and Conv significantly lower than Un-inf (p = 0.021 and p = 0.035, respectively) — sex-stratified: significant only in males
- GSSG: lower in PCC than Conv (p = 0.024), suggesting divergent glutathione redox trajectories post-infection
- 8-OHdG (DNA oxidative damage): PCC significantly higher than Conv (p = 0.0095); no significant Conv vs Un-inf difference — sex-stratified: driven by males
- Cu/Zn SOD: comparable across all three groups

**PCA of combined DIA-MS + ELISA data (Fig. 4):** Integrating the six validated proteins by PCA (PC1 38.9%, PC2 12.7%) produces partial separation of PCC from both Conv and Un-inf, with GAPDH, PCSK9, CST3, CBP2, and C1QA driving the separation — but with substantial group overlap, confirming limited discriminatory power of individual biomarkers.

## Relevance

**For question:0001 (shared molecular signature across triggers):** This paper provides a direct cautionary data point. At 3 months, the plasma proteome robustly distinguishes the post-infection state from never-infected controls (Conv vs Un-inf: 49 DEPs; PCC vs Un-inf: 53 DEPs), but fails to resolve PCC from uncomplicated recovery (only 2 DEPs: VNN1, CST3). This suggests that at least some of the "post-infection signature" is a general scar of SARS-CoV-2 exposure rather than a PCC-specific driver — an important caution for interpreting biomarker studies that lack a convalescent (recovered) control arm.

**For hypothesis:0001 (shared dysregulated attractor):** The near-identical Conv and PCC proteomic profiles raise the question of whether PCC represents a quantitative shift along the same post-infection recovery trajectory or a qualitatively distinct attractor state. The oxidative stress data offer a partial answer: at the biochemical level, 8-OHdG is higher in PCC than Conv (p = 0.0095), suggesting that even if the proteome converges, downstream oxidative damage continues to diverge. This pattern is consistent with a graded attractor where PCC occupies a more severely perturbed region.

**For topic:long-covid-immune-dysregulation:** Complement pathway activation (C1QA, humoral immune response GO terms) persists in both infected groups at 3 months, consistent with prolonged immune perturbation but not uniquely tied to symptom burden. The 2-DEP PCC-vs-Conv difference (VNN1, CST3) is too small to anchor a mechanistic model of PCC-specific immune dysregulation at this time point.

**For topic:biomarkers-and-objective-endpoints:** GAPDH and CPB2 showed the best DIA-MS / ELISA concordance and are highlighted by the authors as candidate monitoring biomarkers for PCC progression or therapeutic response. However, neither discriminates PCC from Conv in the DIA-MS alone; their utility would be for tracking infection-related burden vs uninfected baseline rather than for PCC case identification. PCSK9 and CST3 showed poor assay-to-assay concordance, underscoring the importance of multi-platform validation before clinical translation.

**Comparison with paper:Talla2023 and paper:Klein2023:** Both those studies reported longitudinal immune/proteomic signatures distinguishing long COVID from recovered controls. The present study's failure to find robust PCC-vs-Conv separation may reflect cohort differences (mild vs mixed severity, earlier pandemic variant era, Canadian vs US populations) or time-point differences. The partial convergence in hub proteins (complement, coagulation, immunoglobulin-related) across studies supports a common post-infection biology even where PCC discrimination fails.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post-COVID Condition (PCC), WHO Oct 2021 definition | Long COVID / PAIS | WHO criteria; symptoms ≥ 2 months post-infection, not explained otherwise |
| Convalescent (Conv) | Recovered post-acute state | PCR-confirmed prior infection, symptom-free at 3 months — important negative control absent from many studies |
| DIA-MS plasma proteome | Plasma proteomics | Untargeted, 235 proteins quantified |
| PRDX6 downregulation | Antioxidant depletion | Shared with Conv; not PCC-specific |
| PON3, VNN1 upregulation | Oxidative stress response activation | PON3 shared; VNN1 more specific to PCC vs Un-inf |
| C1QA, CPB2, KNG1 elevation | Complement and coagulation dysregulation | Shared Conv+PCC signature; consistent with thromboinflammation frame |
| GAPDH upregulation | Metabolic/glycolytic reprogramming | Elevated in PCC by DIA-MS and ELISA; associated with mitochondrial dysfunction and SARS-CoV-2 spike interaction |
| 8-OHdG elevation | Oxidative DNA damage | Significantly higher PCC vs Conv in males; suggests ongoing oxidative injury in PCC |
| BQC19 biobank | External cohort (Canadian) | Sherbrooke subset; mild infections only; 2020–2021 |

## Limitations

- **Small sample size:** n = 35 / 62 / 53 per group; underpowered for detecting modest PCC-specific effects or performing robust sex-stratified analyses.
- **Cross-sectional design:** Single 3-month time point; cannot assess trajectory or distinguish persistent vs newly emerged signals. Longitudinal follow-up is needed to determine predictive value.
- **Early pandemic cohort (2020–2021):** Collected before Omicron and before widespread vaccination. PCC prevalence, variant biology, and immunological context differ substantially from subsequent waves; generalisability to current PCC is uncertain.
- **Mild infections only:** Non-hospitalised individuals recruited during strict public health measures limiting community recruitment. Excludes the range of acute severity that strongly predicts PCC risk.
- **WHO 2020-era PCC case definition:** The authors note that PCC incidence and symptom profiles vary by variant; the 2021 WHO criteria may misclassify some cases relative to current definitions.
- **ELISA discordance for CST3 and PCSK9:** DIA-MS showed upregulation of both in infected groups, but ELISA showed reduced or non-significant CST3 and non-significant PCSK9. Post-translational modification, proteolytic processing, or epitope masking may explain discordance; underscores that peptide-level MS and intact-protein antibody assays are not interchangeable.
- **No pre-infection baseline:** Cross-sectional design cannot confirm that uninfected controls are truly comparable at baseline to the infected groups.
- **Sex imbalance across groups:** PCC group 64% female vs Conv 42% female; sex-stratified analyses are exploratory given small subgroup sizes.
- **No symptom subtype resolution within PCC:** PCC is treated as a single heterogeneous group; subtype-specific proteomic profiles (e.g., dysautonomia vs fatigue vs cognitive subtype) are not examined.
- **Plasma proteome coverage:** 235 proteins quantified — standard for DIA-MS plasma proteomics, but the lower-abundance tissue-leaked proteins most relevant to specific organ pathology are likely below detection limits.
- **Limited pathway resolution for PCC-specific biology:** With only 2 DEPs between PCC and Conv, pathway enrichment analyses within the PCC-specific contrast are underpowered; the study cannot rule out PCC-specific effects in low-abundance proteins, intracellular compartments, or post-translational states invisible to untargeted plasma proteomics.

## Model / Tool Availability

Proteomics data deposited in ProteomeXchange Consortium via PRIDE partner repository, dataset identifier **PXD066724** (https://www.ebi.ac.uk/pride/archive?keyword=pxd066724).

DIA-NN v1.8.1 source code available at https://github.com/vdemichev/DiaNN (Docker image: https://hub.docker.com/layers/vdemichev/diann/v1.8.1_cv1/images).

No standalone model or tool is released with this paper beyond the deposited raw/processed MS data.

## Follow-up

- **Longitudinal proteomic studies of PCC vs Conv** are needed to determine if the proteomic convergence at 3 months is a snapshot of eventual convergence or a pre-divergence phase; papers with 6-month and 12-month time points (e.g., Gu et al. EBioMedicine 2024, cited as refs 45–46) are a natural follow-on read.
- **PCC subtype-stratified proteomics** — the heterogeneity within PCC likely masks subgroup-specific signals; studies applying clustering (e.g., Wang et al. Cell Rep Med 2023, ref 48) warrant direct comparison.
- **Orthogonal platforms:** The DIA-MS / ELISA discordances for CST3 and PCSK9 highlight the need for SomaScan or Olink proximity extension assay comparisons, which avoid trypsin-digestion artefacts and cover more proteins at lower abundance.
- **Oxidative stress as a PCC-stratifying biomarker:** 8-OHdG (higher in PCC vs Conv in males) and GSSG (lower in PCC vs Conv) warrant replication in larger, sex-balanced cohorts; connect to paper:Appelman2024 mitochondrial oxygen consumption work and the oxidative stress mechanism thread in this project.
- **Complement and coagulation persistence:** C1QA, CPB2, KNG1 elevated at 3 months in both groups — complement dysregulation paper (paper:CerviaHasler2024) is directly relevant; assess whether the Sherbrooke cohort converges on the complement-thromboinflammation signature.
- **Project question:0001:** This paper should be entered as a key evidence item for the "cautionary/negative" arm — a post-infection signature exists but does not resolve PCC from Conv at 3 months; discuss alongside papers that do find PCC-specific signatures at earlier or later time points.
