---
id: paper:Ramundo2025
kind: paper
title: 'Transcriptomic insights into early mechanisms underlying post-chikungunya
  chronic inflammatory joint disease'
status: active
ontology_terms:
- post-chikungunya chronic disease
- chikungunya virus
- transcriptomic signature
- chronic inflammatory joint disease
- LIFR signaling
- viral persistence
- neutrophil degranulation
- MHC class I antigen presentation
- lactoferrin
- matrix metalloproteinase
- microRNA regulation
- lncRNA
- predictive biomarker
dataset_usage:
- ref: dataset:prjna1001790-post-chikv-wholeblood
  role: analyzed
  overlap: full
source_refs:
- cite:Ramundo2025
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0001-shared-molecular-signature-across-triggers
- question:0092-arthralgia-vs-fatigue-pais-phenotype-attractor
created: '2026-06-20'
updated: '2026-07-26'
---
# Transcriptomic insights into early mechanisms underlying post-chikungunya chronic inflammatory joint disease

<!--
- **Authors:** Mariana Severo Ramundo, Guilherme Cordenonsi da Fonseca, Felipe Ten-Caten, Alexandra L. Gerber, Ana Paula Guimarães, Erika Regina Manuli, Marina Farrel Côrtes, Geovana Maria Pereira, Otavio Brustolini, Milena Gomes Cabral, Carolina Dos Santos Lázari, Patrícia Brasil, Clarisse da Silveira Bressan, Helder I. Nakaya, Gláucia Paranhos-Baccalà, Ana Tereza R. Vasconcelos, Ester Cerdeira Sabino
- **Year:** 2025
- **Journal:** Scientific Reports, vol. 15, article 6745
- **DOI:** 10.1038/s41598-025-86761-x
- **PMID:** 40000671
- **PMCID:** PMC11861634
- **BibTeX key:** Ramundo2025
- **Source:** Europe PMC full-text XML (OA; read 2026-07-26)
- **Tier:** Core now
-->

## Key Contribution

This paper reports a prospective whole-blood transcriptomic analysis (total RNA-seq + small RNA-seq) comparing CHIKV-infected patients who progressed to Post-Chikungunya Chronic Inflammatory Joint Disease (pCHIKV-CIJD) with those who fully recovered, using samples collected in the **acute (Day 0) and post-acute (Day 21)** phases — before the Day 90 outcome determination. The design is therefore genuinely **predictive**, not cross-sectional: transcriptomic signatures in the first 21 days of infection discriminate patients who will develop chronic joint disease at 90 days. The paper identifies early immune impairment — particularly in LIF receptor (LIFR) signaling, neutrophil degranulation, and MHC class I antigen presentation — as a mechanistic frame for why some patients fail viral clearance and progress to chronic arthritis. The miRNA layer (notably hsa-miR-98-5p upregulation → LIFR silencing) provides a post-transcriptional explanation and an estradiol-responsive sex-hormone link to the well-documented female predominance in pCHIKV-CIJD.

## Methods

**Cohort:** Prospective longitudinal cohort at the Evandro Chagas National Institute of Infectology (INI/FIOCRUZ), Rio de Janeiro; established 2019. Inclusion criterion: confirmed CHIKV (arbovirus symptoms + fever within 7 days of onset). Follow-up visits at Day 21 and Day 90. pCHIKV-CIJD case definition: persistence of joint symptoms AND signs of arthritis at Day 90 confirmed by **ultrasound imaging alteration** (synovitis). This is an objective case definition, not self-report alone.

**Participants:** 29 pCHIKV-CIJD cases, 25 non-pCHIKV-CIJD controls (selected from 47 who completed follow-up without chronification). Cohort characteristics were matched on age (pCHIKV-CIJD median 49.5 vs control median 43 years, p=0.31) and sex (25F:4M vs 22F:11M, p=0.08). The slight imbalance toward more female cases (86% vs 67%) reflects the known female risk factor but was not statistically significant. Total sample N ≈ 54.

**Covariates:** Age and sex were balanced by design as matching criteria. Acute illness severity was not formally modelled as a covariate in the differential expression analysis (not described as included in the edgeR model). No pre-infection baseline is available. Prior infection or vaccination history not reported.

**Sampling timepoints:** Two pre-chronicity windows — Acute phase (Day 0: day of inclusion, within 7 days of symptom onset) and Post-acute phase (Day 21: 21 days post-inclusion). Not all patients had samples at both timepoints; available N per phase/group is detailed in the paper's Fig. 7 flowchart.

**Platform:**
- Total RNA-seq: TruSeq Stranded Total RNA Library Prep + RiboZero Gold (Illumina), RIN > 7 or DV200 > 70%, input 500 ng; NextSeq 550 High Output Kit v2.5, 150 cycles, paired-end 2 × 75 bp.
- Small RNA-seq: TruSeq Small RNA Library Preparation Kit; NextSeq 550 High Output Kit v2.5, 75 cycles, single-end 75 bp.
- 98 libraries total; 12 pooled per run.

**Tissue / cell source:** Whole blood (not PBMC; granulocytes included). This means the neutrophil signal reflects total circulating neutrophil content, not a depleted fraction.

**Bioinformatics pipeline:**
- Alignment: STAR (v2.7) to GRCh38; featureCounts (Rsubread v2.4.3) for count matrices.
- Differential expression: edgeR (v3.32.1), FDR < 0.1, |log2FC| ≥ 0.5.
- Pathway enrichment: fGSEA (v1.16.0) against Reactome (v76), ranked by p-value × expression signal.
- Co-expression: CEMITool (v1.14.1).
- miRNA alignment: bowtie2 to miRBase release 22; edgeR for DE; validated targets from miRTarBase v8.0.
- Networks: Cytoscape; interactome restricted to miRNA–target pairs with experimentally validated interactions and inverted log2FC patterns.

**Multiple-testing correction:** FDR < 0.1 (Benjamini-Hochberg). This is more permissive than the conventional 0.05 threshold; given the small N, this is a standard trade-off for discovery but increases false positive risk. Findings should be considered exploratory until replicated.

**Data deposit:** NCBI SRA accession PRJNA1001790 (total and small RNA Fastq files). Analysis code: GitHub (https://github.com/ftencaten/pchikv_cijd_transcriptomics).

## Key Findings

### Acute phase (Day 0): 83 differentially expressed genes

35 up-regulated, 48 down-regulated in pCHIKV-CIJD vs controls (FDR < 0.1, |log2FC| ≥ 0.5). Long non-coding RNAs constitute 20.5% (17/83) of acute-phase DEGs.

Key down-regulated genes in future-chronic patients at the acute phase:

- **LIFR** (LIF receptor): log2FC = −2.12, FDR = 0.08. Encodes the receptor component of the LIF/gp130 complex, which activates JAK1/TYK2 → STAT4 phosphorylation → transcription of IL-6, IL-8, IL-1α, IL-1β, G-CSF. Reduced LIFR in acute pCHIKV-CIJD patients is interpreted as impairing pro-inflammatory antiviral signaling. Mechanistically reinforced by the miRNA layer (see below).
- **ZBTB16** (PLZF transcription factor): log2FC = −1.15, FDR = 0.06. Interferon-responsive transcription factor required for T-cell differentiation and function; reduction could impair IFN-driven antiviral gene expression and T-cell–mediated viral clearance.
- **DDIT4** (REDD1): log2FC = −0.75, FDR = 0.06. mTOR regulatory protein involved in cellular stress response and mTOR-independent autophagy; previously linked to osteoarthritis severity (lower REDD1 = more severe OA).
- **MMP8** (matrix metalloproteinase 8): prominent hub in co-expression module M13 (see below). Mouse studies show MMP8 deficiency leads to delayed neutrophil apoptosis and joint hyper-infiltration, worsening inflammatory arthritis.
- **LTF** (lactotransferrin / lactoferrin): hub in M13 module. Lactoferrin has anti-inflammatory and anti-apoptotic effects on chondrocytes (IL-1β-induced apoptosis protection) and has shown protective effects in murine rheumatoid and infectious arthritis models.

Note: The paper's abstract and most Results text render this gene as "LFT," which appears to be a typographic error throughout; the Introduction correctly writes "LTF," matching the standard HGNC gene symbol for lactotransferrin.

Key down-regulated GSEA pathways in pCHIKV-CIJD (all negative NES):
- Signaling by Interleukin (acute phase; includes LIFR, CCR2)
- Neutrophil Degranulation (both phases)
- Class I MHC-Mediated Antigen Processing and Presentation (both phases)
- Signal Transduction, Metabolism, Immune System, Developmental Biology (acute)

### Post-acute phase (Day 21): 458 differentially expressed genes

427 up-regulated, 31 down-regulated in pCHIKV-CIJD. The shift to predominant up-regulation is interpreted as a sustained / intensified immune response in patients progressing to chronic disease. LncRNAs dramatically increase, representing 65.1% (298/458) of post-acute DEGs (vs 20.5% at acute phase), suggesting a major role for lncRNA-mediated regulatory dysregulation in sustaining chronic immune activation. Enriched pathways: Signal Transduction, RNA Metabolism, Homeostasis, DNA Repair, Cell Cycle; continued down-regulation of Neutrophil Degranulation and MHC class I antigen presentation; down-regulation of class I HLA alleles (HLA-B, HLA-C, HLA-E, HLA-F).

### miRNA analysis

Acute phase: 55 differentially expressed miRNAs (21 up, 34 down). Post-acute phase: 73 DEMs (35 up, 38 down).

Key acute-phase miRNA–mRNA regulatory pairs (experimentally validated target interactions with inverted log2FC):
- **hsa-miR-98-5p** (↑, acute pCHIKV-CIJD) → **LIFR** (↓): validated by miRTarBase. hsa-miR-98-5p is estradiol (E2)-responsive; in vitro data show E2 induces miR-98-5p in breast cancer cells. This interaction provides a hypothesized sex-hormone mechanism for the female predominance in pCHIKV-CIJD (≥50% higher risk in women, 86% of the chronic cases in this cohort).
- **hsa-miR-4775** (↑) → **DDIT4** (↓): validated interaction; DDIT4 downregulation linked to mTOR dysregulation and diminished autophagy.
- **hsa-miR-25-3p** (↑) → **DDIT4** (↓)
- **hsa-miR-196a-5p** (↑) → **RTL8C** (↓)
- **hsa-miR-7-5p** (↑) → **ZP3** (↓)
- **hsa-miR-27a-3p** (↓) → **AP3B2** (↑); present in both acute and post-acute phases.
- **hsa-miR-484** (↓) → **GREB1L**, **LMOD3** (↑).

### Co-expression modules

13 modules detected (42–1095 genes). Three distinguish pCHIKV-CIJD from controls across both phases:

- **M3** (886 genes; higher in pCHIKV-CIJD): enriched for RNA metabolism, mitochondrial tRNA/rRNA processing. Elevated mitochondrial RNA metabolism could reflect stress-induced mitochondrial reprogramming in chronic patients.
- **M12** (46 hub genes; lower in pCHIKV-CIJD): enriched for histone demethylase (HDM) pathway. Reduced epigenetic remodeling capacity may contribute to sustained gene dysregulation.
- **M13** (42 genes, 5 hubs; lower in pCHIKV-CIJD): enriched for Neutrophil Degranulation, Antimicrobial Peptides, Activation of Matrix Metalloproteinases, and Collagen Degradation. Hub genes include **MMP8** and **LTF** — both implicated in joint protection; their down-regulation in future-chronic patients provides a pathway from early immune impairment to joint damage propagation.

## Relevance

### Connection to `hypothesis:0001` and the cross-trigger convergence claim

This paper fills the **post-chikungunya arbovirus cell** of the cross-pathogen signature matrix in `search:0002` and `discussion:0002`. The search entity grades the post-chikungunya leg as "Moderate ... but arthralgia-dominant." After reading the full text, that grading is **accurate and well-calibrated**. The paper adds a single-trigger, prospective transcriptomic study with a genuine predictive design — a stronger design than cross-sectional comparison — to the arbovirus column. However, its contribution to `hypothesis:0001` must be parsed carefully by mechanism:

**Immune-impairment elements (relevant read-across to h0001):** The failure of neutrophil degranulation, MHC class I antigen presentation, and LIFR-mediated IL-6 signaling in the acute phase of future-chronic patients overlaps with immune-impairment mechanisms implicated in fatigue-dominant PAIS (impaired antigen presentation also figures in ME/CFS and long COVID; neutrophil function is dysregulated across PAIS phenotypes). The viral persistence hypothesis — that early antiviral immune failure promotes prolonged viral presence, which sustains chronic inflammation — is structurally the same mechanism invoked in the antigen-persistence arm of h0001 (`hypothesis:0002`). This is a meaningful read-across.

**Articular/joint-specific elements (NOT evidence for the shared fatigue attractor):** MMP8, LTF, M13-module collagen degradation pathways, and the osteoarthritis/inflammatory arthritis literature connections are joint-specific biology. These mechanisms are NOT part of the fatigue-cognitive-autonomic phenotype that defines h0001's core cases (ME/CFS, long COVID, PTLDS). Using them as positive evidence for a shared PAIS attractor would inappropriately extend the convergence claim.

### The scope question: arthralgia-dominant vs fatigue-dominant PAIS

The chronic phenotype in this paper is pCHIKV-CIJD — defined by **joint inflammation confirmed by ultrasound-verified synovitis** at 90 days. Post-exertional malaise, cognitive impairment, and autonomic dysfunction (the hallmark features of fatigue-dominant PAIS) are not measured or reported. This is fundamentally an **inflammatory arthropathy**, not a neuro-immune-fatigue syndrome.

Under D-003, the trigger criterion passes: chikungunya is an unambiguous acute infection, and the chronic phenotype persists well beyond 90 days. So this is IN PRIMARY SCOPE as a PAIS case. The scope-boundaries spec lists PTLDS in-scope, and PTLDS includes arthralgic manifestations; post-chikungunya joint disease is analogous.

However, the phenotype distinction matters for how the paper bears on `hypothesis:0001`. The spec defines PAIS as a shared "failed recovery of immune and physiological homeostasis after acute infection," and h0001's organizing frame is a "persistent post-infectious immune-state displacement." A chronic arthropathy IS consistent with that frame — it is a persistent post-infectious immune failure. But if h0001 is to remain a non-trivial hypothesis (not just "any chronic inflammation after infection"), the phenotype scope matters:

**Recommendation:** Treat this paper as demonstrating that the **immune-impairment mechanisms** (early antiviral immune failure → viral persistence → chronic inflammation) operate in pCHIKV-CIJD, providing relevant read-across to the broader PAIS immune-failure frame. Do NOT count pCHIKV-CIJD transcriptomics as support for the **fatigue-attractor** specifically — the outcomes are different enough that conflating them risks making h0001 trivial. The appropriate formulation is: pCHIKV-CIJD and fatigue-dominant PAIS share a candidate upstream mechanism (early antiviral immune failure promoting viral persistence), but differ in which organ system bears the resulting chronic inflammatory burden (joints vs. neuro-immune-autonomic). Whether this shared upstream is sufficient to call them the "same attractor" is a question to resolve by testing whether the shared immune-impairment mechanism leads to overlapping downstream molecular state — the specific immune profiling of pCHIKV-CIJD patients (not done here) would be the test. In the meantime, the paper is valuable for the arbovirus trigger coverage and the viral-persistence-via-immune-failure mechanism, but should be graded conservatively for h0001's fatigue-attractor claim.

The `search:0002` grading of "Moderate ... but arthralgia-dominant" therefore remains correct and should be maintained.

### Connection to viral persistence / `hypothesis:0002`

The paper's central mechanistic hypothesis — that early LIFR/antigen-presentation failure promotes viral persistence, which sustains chronicity — directly reinforces `hypothesis:0002` (tissue reservoir / antigen-fragment persistence drives PAIS). Although the paper does not directly measure viral load longitudinally, the impaired MHC class I / neutrophil degranulation pathway link makes this a mechanistic candidate for the arbovirus equivalent of the antigen-persistence axis.

### Sex-hormone link

The E2 → hsa-miR-98-5p → LIFR axis is a novel molecular hypothesis for the female predominance in pCHIKV-CIJD, mechanistically connecting sex hormones to early antiviral immune impairment. This parallels (but is distinct from) the sex-hormone hypotheses in long COVID and ME/CFS (see `hypothesis:0005` and `question:0080`); whether the same miRNA-mediated axis operates in fatigue-dominant PAIS is worth exploring.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| pCHIKV-CIJD (>90 days, ultrasound-confirmed synovitis) | Post-acute infection syndrome (PAIS) — arbovirus trigger, arthralgia phenotype | Passes D-003; IN primary scope, but joint phenotype distinct from fatigue-dominant PAIS |
| LIFR down-regulation → reduced IL-6 signaling → impaired antiviral response | Immune impairment arm of viral persistence hypothesis | Mechanistically analogous to antigen/viral persistence in h0001/h0002 |
| hsa-miR-98-5p (E2-responsive) → LIFR silencing | Sex-hormone-mediated immune modulation | Connects to hypothesis:0005 sex-hormone frame; untested in fatigue PAIS |
| Neutrophil degranulation + MHC class I antigen presentation down at Day 0, Day 21 | First-line antiviral immune failure (predictive, early phase) | Relevant read-across to immune exhaustion/failure in ME/CFS and long COVID |
| M13 module (MMP8, LTF) down in pCHIKV-CIJD | Joint-specific cartilage / matrix metalloproteinase pathways | NOT shared with fatigue-PAIS attractor mechanisms; arthritis-specific |
| M3 module (RNA metabolism, mitochondrial tRNA/rRNA) up in pCHIKV-CIJD | Mitochondrial RNA stress response | Read-across to mitochondrial dysfunction axis in h0001; speculative without fatigue phenotyping |
| lncRNAs = 65% of DEGs at post-acute phase | Non-coding RNA regulatory dysregulation in PAIS | Novel arbovirus finding; lncRNAs relevant to PAIS are understudied |
| PRJNA1001790 whole-blood RNA-seq | Public dataset; cross-trigger reanalysis candidate | Valuable addition to the public post-infective-fatigue transcriptome inventory if phenotyping is added |
| Day 0/Day 21 sampling → Day 90 outcome | Prospective predictive design | Stronger evidence than cross-sectional; limits confounding by chronic disease state |

## Limitations

1. **Small N (29 cases, 25 controls).** Per-phase sample counts are further reduced by availability and quality filters. Combined with the FDR 0.1 threshold, the DEG list should be treated as hypothesis-generating; individual gene findings (especially those near FDR 0.1) are prone to false-positive inflation.

2. **Absence of replication cohort.** The authors explicitly acknowledge the lack of validation in an independent cohort due to unavailability of samples. All findings are single-cohort; replication in a separate CHIKV outbreak cohort is needed before these biomarkers or mechanisms can be treated as established.

3. **Phenotype is arthritis, not fatigue.** pCHIKV-CIJD is defined by joint inflammation + synovitis on ultrasound. Post-exertional malaise, fatigue severity, cognitive function, and autonomic symptoms are not measured. The relevance of findings to the fatigue-dominant PAIS attractor is therefore inferred, not demonstrated.

4. **No explicit covariate adjustment in DEG model.** The edgeR model description does not state that sex, age, or acute-phase severity were included as covariates, even though these were matching criteria. The slight sex imbalance (86% F in cases vs 67% F in controls, p=0.08) could contribute to differences in estradiol-responsive transcripts, including miR-98-5p; the reported sex-hormone mechanism therefore cannot be fully separated from residual sex-composition confounding.

5. **Whole blood, not cell-type-resolved.** Signals in whole blood conflate cell-type proportion changes (e.g., fewer neutrophils → lower degranulation transcripts) with per-cell transcriptional changes. The Neutrophil Degranulation pathway down-regulation could reflect neutropenia rather than neutrophil dysfunction. Cell-type deconvolution is not reported.

6. **No viral load measurement.** The viral persistence hypothesis is inferred from the transcriptomic pattern; direct viral RNA quantification in blood or tissue is not performed.

7. **FDR threshold of 0.1** is more permissive than conventional 0.05. Authors acknowledge this is a discovery-level study; all specific gene hits should be considered provisional.

8. **LTF vs LFT gene name inconsistency in the paper.** The paper's abstract and most Results text render the lactoferrin gene as "LFT," deviating from the standard HGNC symbol "LTF." The Introduction uses the correct symbol. This does not affect interpretation but should be noted for downstream reference to this gene.

## Model / Tool Availability

- **Analysis code:** GitHub repository (https://github.com/ftencaten/pchikv_cijd_transcriptomics); pipeline and scripts for total and small RNA processing.
- **Raw data:** NCBI SRA, accession PRJNA1001790 (Fastq files for all 98 libraries).
- No prediction model or clinical tool is released.

## Follow-up

- **Phenotype extension:** The most important follow-up for h0001 relevance would be re-analysing PRJNA1001790 data with fatigue/PEM phenotyping, or cross-comparing the acute-phase DEG signature with matched-timepoint signatures from post-COVID and post-EBV cohorts to test whether the immune-impairment pattern is shared.
- **Cell-type deconvolution:** Applying CIBERSORTx or similar to the PRJNA1001790 whole-blood RNA-seq would distinguish transcriptional from compositional differences in neutrophil degranulation pathways.
- **Chang et al. 2024 (PMID 38507338)** is a companion post-chikungunya cytokine/T-cell study in the same arbovirus arm; reading it alongside this paper would complete the arbovirus immune profile.
- **Sex-hormone / miRNA axis in fatigue PAIS:** whether hsa-miR-98-5p → LIFR silencing operates in long COVID or ME/CFS is testable against existing PBMC miRNA datasets.
- **Lactoferrin supplementation hypothesis:** The paper explicitly raises LTF supplementation as a potential intervention to reduce pCHIKV-CIJD progression. This is hypothesis-generating; no clinical data exist for CHIKV. Lactoferrin has been studied in post-COVID contexts; a cross-syndrome search would be informative.
- **Scope ruling for pCHIKV-CIJD:** `discussion:0002` item 3 calls for a decision on whether post-chikungunya arthritis data are in-scope for the fatigue-PAIS attractor. This reading supports the recommendation that pCHIKV-CIJD is IN primary scope as a PAIS case but should NOT be counted as positive evidence for the fatigue-attractor arm of h0001 specifically; it belongs in the "shared antiviral-failure mechanism" read-across rather than the "shared fatigue-state" convergence claim.
