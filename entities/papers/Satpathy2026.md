---
id: paper:Satpathy2026
kind: paper
title: 'Single-cell profiling of innate and adaptive immune dysregulation in Long COVID'
status: active
ontology_terms:
  - long COVID
  - single-cell RNA sequencing
  - immune dysregulation
  - T cell exhaustion
  - NK cell dysfunction
  - B cell activation
  - monocyte differentiation
  - PBMC immunophenotyping
  - antigen persistence
dataset_usage: []
datasets: []
source_refs:
- cite:Satpathy2026
related:
- topic:long-covid-immune-dysregulation
- topic:biomarkers-and-objective-endpoints
- topic:shared-failure-mode-across-pais
- topic:mecfs-long-covid-convergence
- question:0001-shared-molecular-signature-across-triggers
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- paper:Klein2023
created: '2026-06-20'
updated: '2026-06-20'
---
# Single-cell profiling of innate and adaptive immune dysregulation in Long COVID

- **Authors:** Sarthak Satpathy, Sean Jordan, Mojtaba Bakhtiari, Jannah Elchommali, Denis Ohlstrom, Siddhartha Mantrala, Ching-Yao Yang, Lahiri Nooka, Tiffany A. Walker, Manoj Bhasin
- **Year:** 2026
- **Journal:** bioRxiv (preprint)
- **DOI:** 10.64898/2026.06.04.730206
- **BibTeX key:** Satpathy2026
- **Source:** Full-text PDF (papers/pdfs/2026_Satpathy_single-cell-immune-dysregulation-long-covid.pdf), read 2026-06-20.

## Key Contribution

This study provides a comprehensive single-cell RNA sequencing (scRNA-seq) map of immune dysregulation in Long COVID (LC), profiling 156,478 PBMCs from 20 LC patients and 18 recovered COVID-19 controls (RC). Across all four major immune compartments — B cells, monocytes, CD4/CD8 T cells, and NK cells — the authors document a convergent picture of persistent multi-compartment immune dysfunction consistent with sustained antigen exposure. The headline findings are: (1) naive B cells are chronically activated via IL-4R and BCR signaling; (2) monocytes adopt heightened interferon signaling and migratory states with impaired myeloid differentiation; (3) CD4+ central memory T cells are held in quiescence (BACH2/LEF1 programs) while CD8+ effector memory T cells display chronic exhaustion signatures; and (4) NK cells are terminally differentiated with high cytotoxicity yet compromised regulatory function, particularly in severe LC, where AP-1-driven inflammation is the dominant innate signature. The study links symptom severity to a specific innate immune axis: NK cell depletion/dysfunction and CD14+ monocyte inflammation correlated with higher symptom load, while patients with milder disease retained metabolically resilient, functionally competent NK cells.

## Methods

**Study population and design.** Cross-sectional case-control study. 38 African American adults aged ≥50 years were recruited from Grady Memorial Hospital, Atlanta, GA between December 2023 and December 2024. Participants had confirmed prior SARS-CoV-2 infection (RT-PCR). Long COVID group (N=20): new or worsening persistent cognitive symptoms for ≥3 months. Recovered COVID group (N=16, used as RC throughout; abstract and methods cite 18 RC; note: 83,934 cells captured from LC, 72,544 from RC, totalling 156,478). The cohort was 100% African American and well-matched on age (mean 57.9 vs 59.8 years), sex (~78% vs 90% female), comorbidities, vaccination status, acute illness severity, and number of prior COVID-19 infections. Time since initial infection ranged from 7 to 53 months. Ethics approval: Emory University IRB (IRB5939).

**Neurocognitive and symptom assessment.** 38-item Long COVID symptom review plus validated ePROs: PROMIS v2.0 Cognitive Function, Modified Fatigue Impact Scale (MFIS), CESD, GAD-7, PCL-C. Telephone-based neurocognitive battery from NACC Uniform Data Set (HVLT-I/D, MOCA-ATTN, OT-B, CogMental). LC patients showed significantly worse performance across memory, attention, executive function, and global cognition domains; greater fatigue impact (MFIS 37.9 vs 21.3, P=0.029) but no significant difference in depression, anxiety, or PTSD scores.

**Single-cell library preparation and sequencing.** PBMCs isolated by Ficoll-Paque density gradient (Cytiva). scRNA-seq libraries prepared with 10x Genomics CellPlex kit (1000261) for sample multiplexing via cell multiplexing oligos (CMOs); cDNA amplified with Next GEM Single Cell 3' v3.1 kit (10x Genomics, 1000268); sequenced on Novaseq S4 PE100 (Illumina). Platform: scRNA-seq (3' gene expression); no CITE-seq protein panel is described.

**Computational pipeline.** Raw FASTQ files aligned to GRCh38 with Cell Ranger v6.1.2. Count and CMO matrices analyzed in R (v4.2.2) with Seurat (v4.0.4). Quality filters: >200 unique genes, >600 UMI reads, <20% mitochondrial UMIs. Doublets marked with doubletFinder (3.5% doublet rate assumed). Clustering: Louvain on top 10 PCs, UMAP visualization. Cell type annotation: marker-based + Azimuth reference mapping. Differential abundance: MiloR (k-nearest neighbor approach, negative binomial GLM, spatial FDR < 0.10). Differential expression: Wilcoxon rank-sum (adjusted P < 0.10, avg log2FC > 0.25, percent expression > 25%). Gene regulatory network inference: pySCENIC (SCENIC) with hg38_refseq-r80 motif database and GRNBoost2; high-confidence regulons filtered by presence in >80% of runs, target genes in >90% of runs. Gene set enrichment: ssGSEA (escape Bioconductor package, P < 0.01). Non-negative matrix factorization: geneNMF package. Cell communication: CellChat. Viral repertoire: Kraken2 (v2.1.2) + mg2sc metagenomic pipeline on non-human-aligned reads.

**Subclustering.** T/NK compartment: CD4+ (5 TCM clusters, multiple TEM clusters), CD8+ (TEM, naïve), NK (FCER1G+, NFKB1+ populations), Tregs, NK/T hybrids, proliferative NK. B-cell compartment: naive (61.85%), memory (31.99%), atypical (4.84%). Myeloid compartment: CD14+ monocytes (77.15%), CD16+ monocytes (21.02%), cDC2 (1.66%).

## Key Findings

**Overall immune landscape.** Seven major PBMC populations identified by UMAP: CD4+ T cells (32.74%), CD8+ T cells (20.53%), B cells (11.02%), NK cells (9.99%), CD14+ monocytes (18.54%), CD16+ monocytes (6.07%), platelets (<1%). Broad compositional proportions were similar between LC and RC; differences were concentrated within-compartment at the subcluster level.

**B cell compartment — chronic activation via IL-4R/BCR signaling.**
- Naive B cells in LC enriched in IL4+, IGLC1+, IGLC2+ clusters versus ZEB1+ naive cluster predominant in RC (P<0.05).
- LC naive B cells showed elevated FCRL1, BANK1, TCL1A, IL4R (log2FC >1.5, FDR<0.0001) and IGHM (log2FC>1, FDR<0.0001); pathways enriched: antigen receptor-mediated signaling (FOXP1, IGHM, SKAP1, MEF2C, PDE4D), IL4-IL13 signaling (FOS, IL4R, JUNB), cytokine signaling (CAMK2D, FOS, IL4R, JUN, JUNB, LTB).
- IL4R+ naive B cells interpreted as evidence of ongoing antigen exposure driving aberrant chronic B cell activation; BCR signalosome formation (FCRL1), TLR pathway engagement (BANK1), and downstream memory B cell generation are proposed downstream consequences.
- RC naive B cells showed elevated NFKB1 activity and ZEB1 regulon enrichment — suggesting more homeostatic B cell signaling.
- Recovered COVID participants showed higher immunoglobulin isotype utilization diversity, suggesting more robust and resolved B cell responses.

**Myeloid compartment — heightened migration and impaired differentiation.**
- Differential abundance revealed distinct CX3CR1+CD16+, CX3CR1-CD16+, IL1B+RETNlo CD14+, PDIA3+RETNhi CD14+, and DDIT4+PDIA3+CD14+ monocyte subpopulations between groups.
- CX3CR1+ non-classical monocytes enriched in LC expressed SKAP2, CX3CR1, HDAC9, MNDA (avg log2FC >1.5, P<0.001) — genes linked to immune cell migration, integrin signaling, and type I interferon responses.
- IL1B+RETNlo CD14+ classical monocytes (enriched in LC) showed elevated cytokine signaling genes (CD36, CXCL8, IRS2, JUN, NFKBIA, S100A12, CD14) and neutrophil degranulation markers. Interferon signature in this cluster: CCR1, CCR2, CXCL8, IL1B, STAT2 (distinct from STAT1/STAT3 seen in recovery-associated DDIT4+PDIA3+ cluster).
- DDIT4+PDIA3+CD14+ monocytes (enriched in RC): expressed MX1, KDM3A, RUNX3 (involved in myeloid differentiation); also showed phosphoinositide metabolism and FLT3/RAS/PI3K pathway enrichment (linked to inflammation resolution).
- ATF3 regulon (negative feedback regulator of inflammatory genes) highly enriched in LC monocyte clusters; E2F3 regulon (differentiation-associated) depleted.
- Summary: LC monocytes adopt a migratory, pro-inflammatory phenotype with impaired terminal differentiation.

**T cell compartment — quiescence in central memory, exhaustion in effector memory.**
- CD4+ TCM: LC enriched in LEF1+FHIT+ and ITGB1+INBP4B+ TCM clusters (BACH2 and LEF1 regulon enrichment) — BACH2 suppresses differentiation into effector memory; LEF1 promotes T cell stemness and quiescence. RC enriched in PIK3R1+FTH1+ and SNHG7+CIRBP+ TCM clusters with CREM regulon (cytokine production regulator, supports homeostatic differentiation).
- CD8+ TEM: LC cells showed elevated ST6GAL1, THEMIS, S100A11 — THEMIS suppresses effector function (dysfunctional/regulatory state); S100A11 linked to exhaustion phenotypes. RC TEM showed elevated IFIT1, IFIT2, IFIT3, DDIT3 — interferon-stimulated gene signature consistent with effective antiviral response and inflammation resolution.
- Elevated CEBPG and REL transcription factor activity in RC effector T cells supports immune homeostasis; absent in LC.
- Summary: A functional dichotomy — LC maintains central memory quiescence (failure to differentiate into effectors) while effector memory populations undergo chronic exhaustion.

**NK cell compartment — terminal differentiation, cytotoxicity without regulation.**
- FCER1G+ NK cluster (enriched in LC): elevated FCER1G, PRF1, GZMA, ACTB, PNC1, NKG7 — terminally differentiated cytotoxic profile; increased exhaustion and apoptosis scores.
- NFKB1+ NK cluster (enriched in RC): expressed NFKB1, NFKBIA, NFKBIZ, RELB — homeostatic NF-κB signaling that coordinates T cell recruitment and immune resolution.
- NK cell abundance inversely correlated with symptom load across LC patients (intra-cohort analysis); severe LC patients showed higher NK exhaustion and apoptosis scores without cell cycle differences — indicating terminal dysfunction and cell death rather than impaired proliferation.
- Severe LC: NK cells enriched for JUND, FOS, IRF1 regulons (inflammatory/stress-responsive); less severe LC: CEBPD enrichment in NK cells (metabolic fitness marker).
- CD14+ monocytes in severe LC: TNF-α/NF-κB, IFN-γ, AP-1 pathways enriched; in mild LC: phosphoinositide metabolism and FLT3/RAS/PI3K (inflammation resolution).
- AP-1-mediated chronic inflammation in both NK cells and CD14+ monocytes constitutes the innate severity axis.

**Cell-cell communication — galectin and prostaglandin signaling.**
- Galectin-mediated signaling from monocytes to NK cells (LGALS9 ligand → P4HB receptor on FCER1G+ NK cells): exclusively in LC; proposed to drive terminal NK differentiation and limit regulatory capacity.
- B cells in LC show increased FCER2 expression; ITGAM receptor markedly elevated on both FCER1G+ and NFKB1+ NK cells in LC — this ligand-receptor interaction likely promotes chronic NK cytotoxicity without immune clearance.
- SELPLG-mediated signaling from FCER1G+ NK cells to naive B cells: exclusively in LC; may represent a novel cross-talk axis affecting B cell regulation and trafficking.
- Metagenomic analysis detected consistent enrichment of Retroviridae and Poxviridae in LC samples at both abundance and expression levels — suggesting viral reservoir involvement, though no significant difference was found in Coronaviridae or Herpesviridae levels in peripheral blood.

## Relevance

This study is directly relevant to the core PAIS research agenda at multiple levels.

**question:0001 (shared molecular signature across triggers).** The paper provides the most granular single-cell decomposition of LC immune dysregulation to date, identifying recurrent programs — B cell IL4R/BCR chronic activation, monocyte interferon/migratory phenotype, T cell exhaustion-quiescence dichotomy, NK terminal dysfunction — that closely parallel immune patterns in chronic viral infections (hepatitis B/C, EBV). Whether these programs constitute a shared attractor state across PAIS triggers (ME/CFS, PTLDS, post-dengue) remains to be tested, but the transcriptional architecture is now specified at cell-type resolution.

**hypothesis:0003 (immune-exhaustion feedback).** The T cell and NK findings provide direct mechanistic support: CD8+ TEM express THEMIS and S100A11 (suppression of effector function), CD4+ TCM are locked in BACH2/LEF1-driven quiescence (failure to convert to effectors), and NK cells show terminal exhaustion with high apoptosis scores in severe disease. The combination of exhausted effectors and quiescent central memory creates a self-reinforcing deficiency in antigen clearance — consistent with the immune-exhaustion feedback loop hypothesis.

**hypothesis:0001 (shared dysregulated attractor).** The convergence of dysregulation across four immune compartments, driven by gene programs also seen in chronic viral infection, supports the attractor-state model. The AP-1 chronic inflammation signature (NK + monocytes) represents a potential identifiable hallmark.

**question:0006 (JAK-STAT / IL-6: driver vs. marker).** The monocyte interferon data is relevant: two distinct IFN programs coexist in LC (CCR1/CCR2/CXCL8/IL1B/STAT2 in IL1B+RETNlo CD14+ monocytes vs. STAT1/STAT3 in recovery-associated cluster), supporting interferon as a disease-driving axis rather than purely a recovery marker. ATF3 regulon enrichment in the LC monocyte clusters may be a negative-feedback mechanism attempting — and failing — to dampen chronic inflammatory signaling.

**Cohort note.** The study is exclusively African American adults aged ≥50, a demographic underrepresented in LC immunological research. Findings may not generalize across ancestry or age groups. Case definition: new/worsening cognitive symptoms persisting ≥3 months post-confirmed SARS-CoV-2 infection. This is a cognitively-defined LC subpopulation, not a general LC cohort.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| BACH2/LEF1-driven CD4+ TCM quiescence | immune exhaustion feedback (hypothesis:0003) | Quiescence prevents effector generation; reinforces antigen persistence |
| THEMIS / S100A11 CD8+ TEM exhaustion | immune exhaustion feedback (hypothesis:0003) | Effector suppression markers mirror chronic infection exhaustion |
| FCER1G+ NK terminal differentiation | immune exhaustion feedback (hypothesis:0003) | Cytotoxic but regulatory-function-impaired; apoptosis-driven depletion in severe LC |
| IL4R+ naive B cell chronic activation | antigen/pathogen persistence (hypothesis:0002-adjacent) | Elevated IL4R, BANK1, FCRL1 consistent with ongoing antigen exposure |
| Monocyte interferon / migratory phenotype | shared innate activation program | SKAP2/CX3CR1/HDAC9 axis; parallels monocyte activation in other PAIS |
| AP-1 inflammation (NK + CD14+ monocytes) in severe LC | severity biomarker | JUND/FOS/IRF1 in NK; TNF-α/NF-κB/AP-1 in monocytes; correlates with symptom load |
| Galectin-9 (LGALS9→P4HB) monocyte→NK signaling | immune crosstalk driving dysfunction | LC-exclusive; candidate therapeutic target |
| Metagenomic Retroviridae/Poxviridae enrichment | viral reactivation hypothesis | Peripheral blood only; tissue reservoir cannot be excluded |

## Limitations

1. **Small sample size.** N=20 LC, N=16–18 RC; modest power for subgroup comparisons and within-LC severity stratification. Differential abundance and expression findings should be considered preliminary.
2. **Cross-sectional design.** No pre-infection baseline; cannot distinguish whether immune profiles precede LC or are driven by it. Time since infection varied widely (7–53 months), though the authors report similar mechanisms across LC durations.
3. **Cohort specificity.** 100% African American adults aged ≥50 from a single hospital. Findings may not generalize across ethnicity, age, or recruitment setting. African Americans are at higher risk for LC and may have distinct immune trajectories.
4. **Cognitive/neurocognitive case definition.** LC defined by cognitive symptoms; participants showed prominent neurocognitive impairment. This is a specific LC subphenotype; extrapolation to fatigue-predominant or cardiopulmonary LC subpopulations requires caution.
5. **Peripheral blood only.** Tissue-resident immune responses and potential viral reservoirs are not captured. The authors note that metagenomic analysis of peripheral blood may underdetect tissue-sequestered viral particles.
6. **No TCR sequencing.** The inciting antigen and degree of antigen-driven clonal expansion cannot be characterized; T cell receptor diversity and clonotype data were not reported.
7. **Exhaustion markers inferred from transcriptomics.** NK and T cell exhaustion scoring was gene-expression-based (signatures from Bi et al.); functional validation assays (cytotoxicity, proliferation, cytokine secretion) were not performed.
8. **Viral metagenomics is exploratory.** Enrichment of Retroviridae and Poxviridae in LC peripheral blood is intriguing but not validated; no significance threshold or identity-level characterization reported in the main text.
9. **scRNA-seq platform.** 3' gene expression only (10x Genomics); no surface protein (CITE-seq) measurement, limiting resolution for immunophenotyping of protein-defined subsets.
10. **Preprint.** Not yet peer-reviewed as of June 2026.

## Model / Tool Availability

No standalone software tool or trained model is released. Analytical pipelines used publicly available packages: Seurat, pySCENIC, MiloR, CellChat, Kraken2, geneNMF, escape (all standard Bioconductor/GitHub tools).

Raw sequencing data accession was not specified in the main text or methods as read; a GEO or SRA accession number is not reported in the portions of the paper reviewed. Data availability should be confirmed from the published version or supplementary materials. [UNVERIFIED — no accession number found in main text]

## Follow-up

**Papers to read:**
- Klein et al. 2023 (Nature 623, 139-148) — cited as ref 40 in this paper; immune profiling of LC with some overlapping findings; already noted in allowed list as paper:Klein2023.
- Yin et al. 2024 (Nat Immunol 25, 218-225) — T cell dysregulation and uncoordinated adaptive immune response to SARS-CoV-2 in Long COVID; cited here as a key prior study on T cell exhaustion.
- Peluso et al. 2024 (Semin Immunol 72, 101873) — systems analysis of innate and adaptive immunity in LC; ref 37, cited as supporting evidence for antigen persistence theory.
- Woodruff et al. 2023 (Nat Commun 14, 4201) — chronic inflammation, neutrophil activity, and autoreactivity splits in Long COVID.

**Questions this raises for the project:**
- Do the BACH2/LEF1 CD4+ TCM quiescence programs and THEMIS/S100A11 CD8+ TEM exhaustion signatures appear in ME/CFS or PTLDS cohorts with comparable transcriptomic profiling? (directly relevant to question:0001)
- Is the galectin-9 (LGALS9→P4HB) monocyte-to-NK signaling axis present in other PAIS, and can it be targeted therapeutically?
- Does the severity-stratified AP-1 innate signature (NK + CD14+ monocytes) qualify as an objective biomarker endpoint? (relevant to topic:biomarkers-and-objective-endpoints)
- What antigen(s) sustain the IL4R/BCR B cell activation program? TCR sequencing and antigen-specific B cell repertoire analysis would be the logical next step.
- How do findings from this majority-female, exclusively African American, cognitively-defined cohort compare to predominantly white or mixed-ancestry LC cohorts with fatigue-predominant phenotypes?
