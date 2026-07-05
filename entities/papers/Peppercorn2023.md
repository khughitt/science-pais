---
id: paper:Peppercorn2023
kind: paper
title: A pilot study on the immune cell proteome of long COVID patients shows changes
  to physiological pathways similar to those in myalgic encephalomyelitis/chronic
  fatigue syndrome
status: active
ontology_terms:
  - long COVID
  - myalgic encephalomyelitis/chronic fatigue syndrome
  - peripheral blood mononuclear cells
  - quantitative proteomics
  - immune dysregulation
  - mitochondrial dysfunction
  - post-viral fatigue syndrome
  - SWATH mass spectrometry
dataset_usage: []
datasets: []
source_refs:
- cite:Peppercorn2023
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# A pilot study on the immune cell proteome of long COVID patients shows changes to physiological pathways similar to those in myalgic encephalomyelitis/chronic fatigue syndrome

- **Authors:** Katie Peppercorn, Christina D. Edgar, Torsten Kleffmann, Warren P. Tate
- **Year:** 2023
- **Journal:** Scientific Reports, vol. 13, article 22068
- **DOI:** 10.1038/s41598-023-49402-9
- **PMC:** PMC10716514
- **BibTeX key:** Peppercorn2023
- **Source:** PDF

## Key Contribution

This pilot study from the University of Otago (New Zealand) used quantitative SWATH mass spectrometry proteomics on peripheral blood mononuclear cells (PBMCs) from 6 long COVID (LC) patients (~1 year post SARS-CoV-2) and 5 healthy controls to identify 162 differentially regulated proteins out of 3,131 detected. The core finding is that the PBMC proteome of LC patients shows extensive overlap with a previously published ME/CFS PBMC proteome dataset analysed by the same laboratory using identical methods, particularly in immune-system and mitochondrial function pathways — providing molecular-level evidence that LC and ME/CFS share a common immune-cell pathophysiology. This is notable because the two cohorts had starkly different illness durations (LC: 1 year; ME/CFS: 16 years on average), suggesting the shared proteomic signature is not simply a byproduct of chronicity.

## Methods

**Study design:** Pilot case-control study; 6 LC patients (5F/1M, median age 39, illness duration ~1 year, initial trigger SARS-CoV-2, first wave NZ March/April 2020) versus 5 age/sex-matched healthy controls (4F/1M, median age 40). All LC patients had classical ME/CFS-like fatigue symptoms meeting the WHO clinical case definition criteria for post-COVID-19. Comparison cohort: 9 ME/CFS patients (5F/4M, median age 49, illness duration 16 years) and 9 matched controls, pre-pandemic NZ cohort, previously published (Sweetman et al., cited as the prior ME/CFS proteomics dataset).

**Sample preparation:** 20 mL blood collected into K2 EDTA tubes; PBMCs isolated by Ficoll-Paque Plus density gradient centrifugation; cells lysed using S-Trap-mini kit (ProtiFi) with three vortex/sonication cycles; proteins digested with trypsin; cysteines alkylated with TCEP/IAM.

**Proteomics:** Pooled DDA mass spectrometry (5600 Triple TOF + nanoLC) generated a spectral library of 3,566 protein groups (FDR ≤ 0.01, q ≤ 0.01); DIA SWATH-MS with 11,127 individual peptides then quantified each patient sample in 4 technical replicates. Statistical criteria: ≥1.5-fold change (log2FC ≥ 0.58 or ≤ −0.58) and p ≤ 0.05 (−log10(p) ≥ 1.3) by two-tailed Student's t-test; no FDR correction applied to LC data (n=6 per group, limited power).

**Network / pathway analysis:** STRING v12 functional association network; Markov Cluster Algorithm (MCL, inflation 1.5) for module detection; Gene Ontology and Reactome/KEGG pathway enrichment. Mitochondrial annotation via Human MitoCarta 3.0 database. ME/CFS dataset re-analysed with same STRING/MCL parameters at same fold-change threshold for direct comparison.

## Key Findings

**Differential expression overview**
- 3,131 proteins quantified in the spectral library; 162 differentially regulated (79 down-regulated, 83 up-regulated) in LC vs. healthy controls.
- PCA on all quantified proteins cleanly separated all 6 LC patients from all 5 controls in principal component 3 (6.8% of variance), confirming a robust whole-proteome difference.

**Pathway enrichment (LC)**
STRING enrichment of the 162 proteins returned highly significant pathway clusters:
- Reactome "Immune System" (HSA-168256): 37/162 proteins, strength 0.36, FDR 4.50×10⁻⁴
- Reactome "Innate Immune System" (HSA-168249): 27 proteins, strength 0.50, FDR 6.81×10⁻⁵
- Reactome "Cytokine Signaling in Immune system" (HSA-1280215): 19 proteins, strength 0.51, FDR 1.60×10⁻³
- Reactome "SARS-CoV Infections" (HSA-9679506): 17 proteins, strength 0.70, FDR 6.37×10⁻⁵
- KEGG "Natural killer cell mediated cytotoxicity" (hsa04650): 8 proteins, strength 0.91, FDR 1.70×10⁻³
- KEGG "Epstein-Barr virus infection" (hsa05169): 9 proteins, strength 0.92, FDR 3.50×10⁻³

**MCL module structure (LC)**
Three main protein clusters among the 162 differentially regulated proteins:
1. Immune system / cytokine signaling / NK cell cytotoxicity / EBV infection — major immune cluster including CD4, BCL2, SYK, HLA-DRB1, TLR2, LCK, NMP1, NRAS, PLCG2, PSMB9
2. Gene expression / RNA splicing / spliceosome — includes SNRPD1, HNRNPM, GFM1
3. Gene expression / RNA polymerase II transcription — includes POLR2H, H2AZ1, NPM1

**Mitochondrial proteins (LC)**
21 of the 162 differentially regulated proteins mapped to mitochondria (MitoCarta 3.0); 16 were up-regulated. Binomial test: probability of finding ≥16 up-regulated mitochondrial proteins from a pool of 83 up-regulated proteins = 0.018 (significant enrichment). Pathway enrichment of the 83 up-regulated proteins showed mitochondrial enrichment (GO "Cellular Compartment", adjusted p = 0.023). Key mitochondrial proteins: SFXN1 (FC 1.70, sideroflexin-1, serine/vitamin B6 metabolism), PDPR (FC 2.85, pyruvate dehydrogenase phosphatase, pyruvate metabolism), DLAT (FC 1.64, dihydrolipoyllysine acetyltransferase, pyruvate complex), PRDX2 (FC 1.70, peroxiredoxin-2, ROS/GSH metabolism), SARS2/IARS2/GFM1 (mitochondrial tRNA synthetases and translation factor), BCL2 (FC 2.20, apoptosis), FIS1 (FC 1.54, mitochondrial fission).

**HLA proteins**
Multiple HLA proteins differentially regulated: HLA-B down-regulated ~1.7-fold in both LC and ME/CFS (suggesting reduced antigen presentation to T cells and reduced NK inhibitory signaling); HLA-DRB1 (Class II, antigen presenting) down-regulated in both; HLA-E up-regulated ~1.7-fold in LC but down-regulated ~1.6-fold in ME/CFS (discordant — HLA-E overexpression impairs NK cytotoxicity via CD94 recognition).

**Comparison with ME/CFS**
- 2,032 proteins quantified in both LC and ME/CFS datasets; 346 differentially regulated in ME/CFS vs. 162 in LC.
- Of the common 2,032 proteins: 47/83 LC up-regulated proteins overlapped with ME/CFS dataset; 56/79 LC down-regulated proteins overlapped; 9 proteins up-regulated in both, 6 proteins down-regulated in both.
- Shared proteins (same direction in both): PRDX2 (up), C16orf54 (up, energy homeostasis transmembrane protein), PSMB9 (up, proteasome subunit β9 — linked to autoinflammation and COVID-19 increased expression), FIS1 (up, mitochondrial fission), TMA7 (up), RPL28 (up, 60S ribosomal protein), ARHGDIB (up), NPM1 (up, nucleophosmin).
- Discordant: S100A4 (Ca²⁺-binding, up ~fourfold in LC, down 1.5-fold in ME/CFS); GMFG/GMFB (glia maturation factors, discordant — GMFB up in LC but down in ME/CFS; GMFG up in ME/CFS but down in LC).
- 22 of 34 LC-enriched Reactome categories were also enriched in ME/CFS; 5 of 38 LC-enriched KEGG pathways also enriched in ME/CFS.
- ME/CFS MCL clusters: immune system / antigen presentation / cytokine signaling (63 proteins), immune system process / platelet activation (20 proteins), translation / RNA/protein metabolism / stress response (119 proteins), mitochondria / oxidative phosphorylation (13 proteins), vesicle-mediated transport (12 proteins).

## Relevance

This paper directly supports the project research question (research-question:post-acute-infection-syndromes) in multiple ways:

1. **Molecular evidence for shared post-infectious failure mode:** By using the identical proteomics platform and statistical thresholds on LC and ME/CFS cohorts from the same lab, this study provides the most methodologically controlled direct comparison yet of PBMC proteomes in two PAIS conditions. The shared immune and mitochondrial pathway dysregulation supports the PAIS frame that LC and ME/CFS represent convergent failures of the same homeostatic systems rather than distinct disease entities.

2. **Persistence of molecular signature at 1 year:** The fact that LC patients still show clear PCA separation from controls at ~1 year post-infection — with 162 differentially regulated proteins primarily in immune and mitochondrial pathways — is direct evidence that immune and metabolic homeostasis has not been restored. This is the PAIS "failed recovery" signature at the protein level.

3. **Mitochondrial dysfunction as shared effector:** The significant enrichment of up-regulated mitochondrial proteins in LC (particularly pyruvate dehydrogenase complex, mitochondrial tRNA synthetases, ROS-management enzymes like PRDX2) mirrors prior ME/CFS findings. Both conditions show altered mitochondrial dynamics (FIS1 up), ROS stress (PRDX2 up), and impaired pyruvate/oxidative metabolism — consistent with the hypothesis that PAIS involves a sustained shift toward a low-efficiency metabolic state as part of failed homeostatic recovery.

4. **Immune dysregulation as the dominant molecular signal:** 37 of the 162 differentially regulated proteins map to the Reactome "Immune System" pathway (FDR 4.5×10⁻⁴); specifically, NK cell cytotoxicity, cytokine signaling, and antigen presentation are all disrupted. The down-regulation of HLA-B (reduced antigen presentation / reduced NK inhibitory signal) and changes in CD cluster proteins (CD4, CD5, CD84, CD300LF) suggest ongoing remodeling of adaptive and innate immune tone — an immune system that has not returned to its pre-infection state.

5. **SARS-CoV-2 persistence signature:** 17 proteins enriched in the Reactome "SARS-CoV Infections" category (FDR 6.37×10⁻⁵) remain dysregulated one year post-infection. This is consistent with the hypothesis that persistent viral antigen (or ongoing innate immune memory) drives sustained PBMC proteome remodeling.

6. **Cross-PAIS inference:** The partial but significant overlap between LC and ME/CFS proteomes (including shared up-regulation of PSMB9, PRDX2, FIS1) provides molecular grounding for the project's cross-PAIS hypothesis that therapeutic and mechanistic insights from ME/CFS research are directly applicable to LC — and vice versa.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PCA separation of LC from HC at 1 year | failed homeostatic recovery | Quantitative demonstration that PBMC proteome has not normalized |
| 37 immune-system differentially regulated proteins | persistent immune activation | Reactome "Immune System" FDR 4.5×10⁻⁴; immune dysregulation is the dominant signal |
| 21 mitochondrial proteins dysregulated (16 up) | metabolic/mitochondrial dysfunction | Significant enrichment (p=0.018 binomial); pyruvate, ROS, fission, translation all affected |
| PRDX2 up in both LC and ME/CFS | shared oxidative stress signature | Antioxidant enzyme responding to increased ROS in PBMC compartment |
| HLA-B down in both LC and ME/CFS | antigen presentation failure | Reduced MHC-I surface expression may impair viral clearance and NK regulation |
| HLA-E up in LC vs. down in ME/CFS | discordant NK regulation | HLA-E overexpression impairs NK lysis; discordance may reflect illness stage (1 yr vs. 16 yr) |
| NK cell cytotoxicity pathway enriched | innate immune dysfunction | KEGG hsa04650, FDR 1.70×10⁻³; impaired cytotoxic surveillance |
| SARS-CoV-2 infections Reactome cluster | antigen/pathogen persistence | 17 proteins still dysregulated 1 year post-infection; compatible with viral reservoir |
| EBV infection KEGG pathway enriched | latent-virus reactivation | Overlap with EBV pathways connects to known ME/CFS herpesvirus reactivation literature |
| Spliceosome / RNA pol II transcription clusters | gene expression dysregulation | Secondary consequence of chronic immune activation or direct viral interference |
| LC vs. ME/CFS proteome comparison | cross-PAIS shared failure mode | Same methods, partial overlap in direction-concordant proteins; shared pathways despite different illness duration |
| PSMB9 up in both conditions | immune activation / autoinflammation | Proteasome subunit linked to autoinflammation; elevated in COVID-19 |
| FIS1 up in both conditions | mitochondrial dynamics | Mitochondrial fission protein; increased fragmentation under stress |
| Cohort duration difference (1 yr LC vs. 16 yr ME/CFS) | PAIS illness trajectory | Despite duration difference, similar molecular signature — suggests early establishment of stable dysregulated state |

## Limitations

- **Very small cohort:** n=6 LC patients and n=5 controls; n=9 ME/CFS and n=9 controls. Underpowered for FDR adjustment — the authors acknowledge that Benjamin-Hochberg correction yielded only 9 significant differences, and explicitly frame this as a discovery study. Many findings require replication.
- **No FDR correction applied to primary LC analysis:** The stated rationale (false negatives worse than false positives for discovery) is reasonable, but inflates the risk of spurious findings; enrichment results should be interpreted cautiously.
- **Cross-cohort comparison is indirect:** The LC and ME/CFS cohorts were not collected simultaneously and have substantially different disease duration (1 vs. 16 years), sex ratios (5F:1M LC vs. 5F:4M ME/CFS), and age (median 39 vs. 49). The authors note no PCA separation by sex or age in their ME/CFS cohort, but confounding cannot be excluded.
- **PBMC compartment only:** Whole-blood PBMCs reflect lymphocyte/monocyte biology but miss tissue-resident immune cells, endothelial cells, neurons, and other cells likely involved in PAIS pathophysiology.
- **Single time-point:** Cross-sectional design cannot distinguish whether observed changes are causally upstream or downstream of symptoms, or whether they are recovering or worsening relative to acute disease.
- **LC patients selected for ME/CFS-like phenotype:** Recruitment via ME/CFS support networks and based on classical ME/CFS-like symptoms means the cohort is not representative of the full LC spectrum — generalizability to LC patients without fatigue-dominant phenotype is limited.
- **p-value threshold without correction:** At p ≤ 0.05 across 3,131 proteins, ~156 false positives are expected by chance alone; the actual detected set of 162 differentially regulated proteins is only marginally larger.

## Model / Tool Availability

- **Proteomics data:** Deposited to ProteomeXchange Consortium via PRIDE repository; dataset identifier **PXD045508**.
- No software model or computational tool released; standard bioinformatics tools (STRING v12, SWATH 2.0/PeakView 2.2/MarkerView 1.2) used.

## Follow-up

- **Replicate in larger cohort:** The primary need is validation of the 162 differentially regulated proteins in a larger, more heterogeneous LC cohort with proper FDR control.
- **Longitudinal design:** Serial PBMC proteomics at 3, 6, 12, 24 months post-infection to track which protein clusters resolve (immune activation?) vs. persist (mitochondrial?), mapping the trajectory of homeostatic recovery failure.
- **Cross-PAIS proteomics:** Compare with PBMC proteomes from post-treatment Lyme disease syndrome (PTLDS), post-dengue fatigue, and post-Q-fever fatigue — do the same immune/mitochondrial clusters emerge?
- **PRDX2 mechanistic follow-up:** Peroxiredoxin-2 up-regulation in both LC and ME/CFS points to increased ROS in immune cells; assess whether ROS scavenger treatment normalizes PBMC proteome and functional readouts.
- **HLA-E discordance:** HLA-E up in LC vs. down in ME/CFS — is this a disease-stage phenomenon (early post-viral immune evasion vs. chronic exhaustion)? Would longitudinal sampling show HLA-E decreasing as LC progresses?
- **Relationship to viral persistence:** Cross-reference the 17 SARS-CoV-infections-pathway proteins with known SARS-CoV-2 interactome data to identify which are direct viral interaction partners vs. downstream immune responders.
- **Integration with transcriptome/methylome:** The same group has published ME/CFS transcriptome and methylome data; integration of the LC proteome with those datasets would reveal whether protein-level changes are driven by transcription or post-transcriptional regulation.
- **Complement Komaroff2023 and Choutka2022:** This paper provides the protein-level molecular evidence base for the cross-PAIS convergence claimed at the symptom/biology level by cite:Komaroff2023; together they anchor the project's cross-PAIS shared failure mode hypothesis.
