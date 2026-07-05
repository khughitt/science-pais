---
id: paper:Galbraith2011
kind: paper
title: 'Peripheral blood gene expression in postinfective fatigue syndrome following
  from three different triggering infections'
status: active
ontology_terms:
- post-infective fatigue syndrome
- peripheral blood gene expression
- transcriptomic signature
- Epstein-Barr virus
- Ross River virus
- Coxiella burnetii (Q fever)
- Dubbo Infection Outcomes Study
- microarray
- longitudinal cohort
- cross-trigger comparison
dataset_usage: []
datasets: []
source_refs:
- cite:Galbraith2011
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- discussion:0002-cross-pathogen-pais-signature-convergence
created: '2026-06-20'
updated: '2026-06-20'
---
# Peripheral blood gene expression in postinfective fatigue syndrome following from three different triggering infections

- **Authors:** Sally Galbraith, Barbara Cameron, Hui Li, Diana Lau, Ute Vollmer-Conna, Andrew R. Lloyd
- **Year:** 2011
- **Journal:** The Journal of Infectious Diseases, vol. 204, no. 10, pp. 1632–1640
- **DOI:** 10.1093/infdis/jir612
- **PMID:** 21964398
- **BibTeX key:** Galbraith2011
- **Tier:** Core now
- **Source:** Full-text PDF (papers/pdfs/2011_Galbraith_peripheral-blood-gene-expression-postinfective-fatigue.pdf), read 2026-06-20 (supersedes earlier abstract-only read).

## Key Contribution

This is the **only published head-to-head transcriptomic comparison** of peripheral blood gene expression across three distinct infection triggers of post-infective fatigue syndrome (PIFS) within a single, prospectively designed cohort. Using the Dubbo Infection Outcomes Study (DIOS) — the longitudinal Australian cohort that established PIFS as a cross-pathogen phenomenon — Galbraith et al. compared PBMC transcriptomes (Lymphoprep-separated peripheral blood mononuclear cells) at multiple time points in subjects who developed ≥6 months of debilitating fatigue after EBV (glandular fever), Ross River virus (RRV), or *Coxiella burnetii* (Q fever) against matched controls who recovered promptly from the same infections.

The key finding is a **definitive negative for a shared cross-cohort PBMC gene expression signature**: despite strong clinical similarity among the three PIFS groups, no genes were consistently associated with illness across all three infection cohorts in any analysis. Within-trigger signals were modest (fold-change 0.6–2.3× in paired analysis, 0.6–2.4× in cross-sectional; 23 / 15 / 58 / 223 genes depending on the analysis method), and the qPCR correlation rate (73%, 33/45 genes) indicates acceptable array reliability — but analyses rerun on qPCR-confirmed genes found zero genes significantly consistent across cohorts at the 5% level. The only partial cross-cohort signal was CYBA (cytochrome b-245 alpha polypeptide), which reached adjusted significance in the longitudinal GEE model for 2 of 3 cohorts (EBV and Q fever), but not RRV.

This paper is the **load-bearing empirical test** for `discussion:0002` and `question:0001`. It is the closest existing study to the decisive "shared-attractor" test demanded by `hypothesis:0001`, and its result is: **partial shared biology at the clinical/symptom level, but no shared peripheral-blood molecular signature at the gene level**. The implication for the project is nuanced — the negative result constrains the "shared attractor" model to pathway-level or upstream regulatory convergence rather than a common terminal set of differentially expressed transcripts in PBMCs.

## Methods

**Study:** Nested within the Dubbo Infection Outcomes Study (DIOS), a prospective surveillance cohort that enrolled patients with serologically confirmed acute EBV, RRV, or Q-fever infections in the Dubbo region of New South Wales, Australia. DIOS is the same cohort reported in Hickie et al. 2006 (*BMJ*), which first documented parallel PIFS incidence (~11–12% of acute cases) across all three triggers.

**Case definition:** PIFS defined as ≥6 months of disabling fatigue, musculoskeletal pain, neurocognitive difficulties, and unrefreshing sleep following documented acute infection — the original Dubbo PIFS criteria, operationally equivalent to the Fukuda CFS criteria applied in post-infectious context.

**Participants:** 18 PIFS cases and 18 matched control subjects who recovered promptly from the same acute infections (matched by age, sex, and infection type). Total n = 36. Per-group composition differs by analysis:
- **Paired (within-subject) analysis:** 12 subjects met criteria (SOMA ≥3 at T1 and <3 at T4): **3 EBV, 4 RRV, 5 Q-fever** cases; matched controls used from the same infection groups.
- **Two-sample (cross-sectional at 6 months, T3):** 17 cases (**6 EBV, 5 RRV, 6 Q-fever**) and 11 controls (**5 EBV, 4 RRV, 2 Q-fever**). The control subset is smaller because fewer controls had blood samples available at the 6-month time point.
- **Longitudinal / correlation analyses:** all 36 subjects (18 cases + 18 controls), all available time points.

All subjects were white Australians. Mean age: cases 40 ± 18 years, controls 39 ± 16 years. Sex: 11 male / 7 female in both groups. Full subject-level demographics and symptom scores are in Table 1 of the paper. This small per-group N (effectively ~3–6 per trigger in most analyses) is a recognized design constraint (see Limitations).

**Biological material:** Peripheral blood mononuclear cells (PBMCs), not bulk whole blood. Blood was collected in the morning and transported to the lab within 6 hours; PBMCs were separated by Lymphoprep density gradient and cryopreserved in vapor-phase liquid nitrogen. Thawed PBMCs were lysed in Tri-reagent (Sigma-Aldrich) for RNA extraction. RNA quality was assessed by denaturing gel electrophoresis and Bioanalyzer (28S:18S ratio 1.8–2.0). Note: the PBMC isolation step means the expression profile reflects mononuclear cells (lymphocytes, monocytes) rather than granulocytes.

Blood was collected longitudinally at 3 or 4 time points per subject (Table 1): T1 (0–6 weeks post onset), T2 (6–12 weeks), T3 (3–9 months), T4 (>9 months, some >12 months). The initial sampling occurred within 6 weeks of illness onset (mean 4.2 ± 1.8 weeks). Subjects were recruited after the acute febrile phase, so T1 already reflects the early post-acute state, not the acute infection response. Total 127 microarray samples across all subjects and time points. For each subject, all samples were processed in a single run; arrays from a case and a control subject were run together to control for run-to-run effects.

**Gene expression platform:** Illumina **Sentrix HumanRef-8 v2 Expression BeadChip** (Illumina, San Diego, CA). Each BeadChip carries 8 arrays with **22,184 probes covering 18,203 unique genes**. Total 127 microarray samples profiled. Raw expression levels were log2-transformed and quantile-normalized (within-subject arrays normalized together for paired analysis; all 127 arrays normalized together for longitudinal and correlation analyses). Images analyzed with Beadstudio Gene Expression Module (Illumina). RNA amplification to biotin-labeled cRNA used the Illumina TotalPrep RNA Amplification Kit (Ambion). Arrays were stained with streptavidin-Cy3 and scanned on an Illumina scanner.

**Confirmatory assay:** Quantitative PCR (TaqMan assays on Applied Biosystems 7900HT Fast Real-Time PCR system; microfluidic cards in 384-well format; HighCapacity RNA-to-cDNA kit). Three housekeeping genes used for normalization: GAPDH, UBC (ubiquitin C), and YWHAZ (tyrosine monooxygenase). Ct values analyzed with DataAssist v2.0 (Applied Biosystems). 45 candidate genes were selected for qPCR based on ranking across the three analyses (see Selection strategy below). qPCR "confirmation" was defined as a significant microarray–qPCR ΔCt correlation (P < 0.10); 33/45 (73%) met this criterion. Note: this 73% rate measures array-qPCR technical concordance, not replication of differential expression per se. The differential expression and correlation analyses were then rerun using the 33 qPCR-concordant gene subset.

**Statistical analyses:** Four complementary strategies:
1. **Paired (within-subject) analysis:** Paired t-tests comparing T1 ("sick") vs. T4 ("well") for the 12 subjects with qualifying SOMA scores at both endpoints. Moderated t-statistics via Bioconductor limma; both unadjusted and Benjamini-Hochberg (BH) adjusted p-values.
2. **Two-sample (cross-sectional) analysis:** Two-sample t-tests comparing 17 PIFS cases vs. 11 recovered controls at T3 (~6 months). BH-adjusted p-values.
3. **Longitudinal analysis (GEE):** Logistic regression via generalized estimating equations (R package geepack), modeling probability of fatigue state (SOMA ≥3) as a function of gene expression, time point, infection type, age, and sex, with interaction terms for gene × infection type. All 36 subjects and all time points included. Tests for b8 = 0 (EBV), b8 + b9 = 0 (QF), b8 + b10 = 0 (RRV). Coefficients are log-odds ratios.
4. **Correlation analysis:** Pearson correlations between gene expression and PCA-derived symptom domain indices (fatigue, pain, mood, neurocognitive disturbance, overall severity) for each infection cohort separately. Overabundance assessed vs. 1,000 permutations.

For analyses 1–3, genes were ranked by p-value per infection, and those in the **top 2000 for all three infections** with consistent direction were selected — a cross-infection filter built into the primary analysis design. This filter is crucial: the "23 genes" in the paired analysis are genes that ranked in the top 2000 for EBV, RRV, and Q-fever simultaneously, not just genes significant in the combined analysis.

**Funding:** Partially supported by USPHS grant U50/CCU019851-01 (CDC/PHS). The Dubbo cohort infrastructure was supported by Australian government and UNSW funding (Lloyd group).

## Key Findings

### 1. Paired (within-subject) analysis: early symptomatic vs. late recovered

- **23 genes** were ranked in the top 2000 for all three cohorts and showed consistently up- or down-regulated direction across them.
- Fold-change range: **~0.6–2.3×** (direction: some up, some down-regulated in the early "sick" state relative to late "well").
- **No genes reached adjusted significance (BH-corrected p < 0.05).** The 23 genes are a nominal cross-cohort filter result, not FDR-corrected hits.
- Analysis based on 12 subjects (3 EBV, 4 RRV, 5 Q-fever) who had SOMA ≥3 at T1 and SOMA <3 at T4.
- The authors note the relative lack of variance in gene expression within subjects over ≥12 months (all differences <2.3-fold) as consistent with subjects being sampled post-acute-febrile phase, not mid-acute-infection; hence the absence of strong pro-inflammatory cytokine signatures is expected.

### 2. Two-sample (cross-sectional) analysis at 6 months

- **15 genes** showed consistent up- or down-regulation between PIFS cases and recovered controls at T3 (~6 months) across all three infection cohorts (top 2000 for each, consistent direction filter).
- Fold-change range: **~0.6–2.4×**.
- **No genes reached adjusted significance (BH-corrected p < 0.05).**
- Analysis based on 17 cases and 11 controls (reduced control N due to sample availability at T3).

### 3. Longitudinal (GEE) analysis across all time points

- **58 genes** had coefficient estimates of consistent sign across all three infections in the GEE model. Coefficient estimates (log-odds ratios) ranged widely from −18.6 to +19.1.
- **13 genes reached adjusted significance (BH-corrected p < 0.05)** in the longitudinal model.
- Of these 13, only **1 gene — CYBA (cytochrome b-245, alpha polypeptide)** — was associated with fatigue state in 2 of the 3 infective cohorts (EBV and Q fever; not RRV). This is the closest the paper comes to a cross-cohort signal, and it held at adjusted significance in only 2/3 triggers.

*Note on the "63 genes" in the abstract:* the abstract's "63 genes" in cross-sectional / regression analyses refers to the combined unique count from analyses 2 and 3 above (15 two-sample + 58 longitudinal − 10 genes common to both = 63 distinct genes). This is a union across the two analysis methods, not a single analysis result.

### 4. Symptom-domain correlation analysis

- Overabundance analysis identified that overall illness severity, fatigue, and neurocognitive disturbance were significantly correlated with gene expression for **EBV and Q-fever cohorts only** — not for the RRV cohort (which showed no statistically significant overabundance on any symptom domain).
  - Severity: p = .016 (EBV) and p = .044 (QF)
  - Fatigue: p = .017 (EBV) and p = .038 (QF)
  - Neurocognitive disturbance: p = .019 (EBV) and p = .023 (QF)
- Correlation tests (5% unadjusted) identified genes significantly correlated for both EBV and Q-fever: **96 genes** for severity, **93 genes** for fatigue domain, **106 genes** for neurocognitive disturbance.
- **223 total unique genes** significant across any symptom domain for EBV + QF (158 significant for 1 domain, 58 for 2 domains, 7 for all 3 domains). The 223 figure is the union across symptom domains for EBV and Q-fever only — not RRV, which had no overabundance.
- Correlation coefficients ranged from r = −0.61 to r = +0.63.
- Three genes reached adjusted significance for neurocognitive disturbance in the EBV group: **GAD2** (glutamate decarboxylase-2), **SIGLEC-1/CD169** (sialoadhesion-1), and **STYX** (serine/threonine/tyrosine interacting protein). None of these reached adjusted significance in the Q fever group.
- The absence of RRV overabundance is itself a cross-cohort inconsistency finding: the symptom-correlating gene expression signal exists for EBV and Q-fever but not RRV.

### 5. qPCR confirmation and reanalysis

**Gene selection for qPCR (45 genes):** A two-level selection process (Figure 1 in the paper):
- For paired, two-sample, and GEE analyses: genes in the top 2000 for all 3 infections selected first, then top 12/12/19 by mean rank across infections chosen (with 10 genes shared between two-sample and longitudinal).
- For correlation analysis: top 12 by mean rank for EBV + Q-fever for overabundant symptom domains.
- Final selection: 12 (paired) + 2 (two-sample only) + 10 (two-sample and longitudinal) + 9 (longitudinal only) + 12 (correlation) = 45 genes.

**qPCR concordance:** 33/45 (73%) showed significant microarray–qPCR ΔCt correlation at p < 0.10. This is a measure of technical concordance, not differential expression replication. Table 2 lists all 45 genes and their correlation/p-values.

**Reanalysis on 33 qPCR-confirmed genes:**
- **At 5% significance: zero genes** were significantly correlated for both EBV and Q-fever for severity, fatigue, or neurocognitive disturbance in the repeated correlation analysis.
- **At 10% (liberal) threshold: 6 genes** showed nominal significance in ≥2 cohorts: ACTA2, JUP, FANCE, SLC27A6, TSHZ2, LGALS3BP. However, some showed *discordant directions* across infections (e.g., FANCE up in EBV, down in RRV), undermining a coherent shared interpretation.
- The conclusion from qPCR reanalysis: **no genes confirmed as consistently and coherently associated with PIFS across ≥2 infection cohorts** at conventional significance.

### 6. Cross-cohort consistency — the critical finding

> **"The major finding reported here with the use of this comprehensive approach was that no genes were consistently associated with the illness."** (Discussion)

> **"Quantitative PCR confirmed 33 (73%) of 45 genes — none were consistent across cohorts."** (Abstract, Results)

This is the paper's most consequential result. The primary analytical design specifically searched for genes in the top 2000 for all three infections simultaneously — this cross-infection consistency filter was built in, not post hoc. Despite this, no genes emerged as reliably shared across EBV, RRV, and Q-fever PIFS at conventional significance. The qPCR reanalysis confirmed the negative: 0 genes at 5% across ≥2 cohorts; 6 genes at 10% with inconsistent directions.

The only exception is CYBA, which reached adjusted significance in the longitudinal model for EBV and Q-fever (but not RRV). The authors do not highlight this as a positive cross-cohort finding — it is mentioned descriptively and does not survive as a robust cross-trigger signal given the absence of RRV replication.

The implication is that peripheral blood gene expression, as measured in bulk whole blood by this microarray protocol and at these follow-up time points, does not produce a **trigger-agnostic molecular fingerprint** of PIFS. Each infection cohort has its own modest expression signature, but these signatures do not converge.

This does **not** necessarily mean that biology is entirely trigger-specific. Possible explanations include: (a) the shared mechanism exists but operates at pathway level or in a cell-type not detected in bulk blood; (b) sampling time points differ across cohorts in ways that obscure a shared transient signal; (c) per-group N (~6) was insufficient to detect modest shared effects against within-group noise; (d) the shared state-change is post-translational, epigenetic, or metabolic rather than transcriptomic.

### Summary verdict on shared vs. trigger-specific biology

| Level | Finding | Interpretation |
|---|---|---|
| Clinical symptom profile | Similar across EBV, RRV, Q-fever PIFS | **Supports** shared biology |
| PBMC transcriptome — paired (within-subject) | 23 genes nominally consistent; 0 FDR-significant | **Does not support** a shared transcript signature |
| PBMC transcriptome — cross-sectional at 6 months | 15 genes nominally consistent; 0 FDR-significant | **Does not support** a shared transcript signature |
| PBMC transcriptome — longitudinal GEE | 58 genes; 13 FDR-sig; CYBA in EBV + QF only | At most a partial EBV/QF signal (no RRV) |
| Symptom-correlating transcripts | 223 genes correlated with symptoms in EBV + QF; 0 in RRV | Trigger-specific symptom tracking exists; not shared across all 3 |
| qPCR reanalysis | 33/45 technically concordant; 0 at 5% across cohorts | Analytically valid negative cross-cohort result |

## Relevance

### Relationship to `hypothesis:0001` (shared dysregulated attractor)

This paper is the **single closest existing empirical test** of `hypothesis:0001` at the transcriptomic level. Its result is a **partial disconfirmation**: the clinical convergence across triggers is robust (same PIFS phenotype, same ~11% incidence, same duration), but the peripheral blood gene-expression layer does **not** reveal a shared molecular signature. This means `hypothesis:0001`'s claim of "a common final state" cannot be supported in peripheral-blood transcriptomics at the gene level from this evidence.

However, the partial disconfirmation does not falsify `hypothesis:0001` in full. The hypothesis allows that convergence occurs at a higher level of organization (regulatory networks, pathways, cell-type composition) rather than at individual transcript identity. The failure of bulk whole-blood microarray to detect a cross-trigger signature is compatible with convergence being:

- **Cell-type specific:** bulk blood averages over immune cell populations; if the shared signal lives in a rare population (e.g., exhausted T cells, activated monocyte subsets), microarray on bulk lysate would miss it.
- **Pathway-level:** shared activation of, e.g., interferon signaling or mitochondrial stress pathways could manifest through different effector genes in different infection contexts.
- **Regulatory/epigenetic:** shared DNA methylation, chromatin state, or non-coding RNA changes would be invisible to mRNA microarray.
- **Metabolic/proteomic:** shared metabolic bottlenecks (tryptophan-kynurenine, bioenergetics) would not appear in transcriptomics.

The project should therefore record this result as: **"no shared bulk-blood transcript signature in Dubbo PIFS, but this constrains rather than refutes `hypothesis:0001`"**, and flag that the decisive test requires pathway-level or multi-omic harmonization, not just a larger version of the same bulk microarray design.

### Relationship to `question:0001` (shared molecular signature across triggers)

Galbraith2011 answers a specific, bounded version of `question:0001`: *Is there a shared peripheral-blood transcriptomic signature across PIFS triggers in a small post-infective fatigue cohort?* The answer is **no, at gene-list level in bulk blood**. The broader question (shared pathway-level or multi-omic signature) remains unanswered. The paper does not resolve `question:0001` but tightens it: future searches should focus on pathways/modules, not individual transcripts, and on cell-type-resolved data, not bulk lysate.

### Relationship to `discussion:0002` (cross-pathogen PAIS signature convergence)

As noted in `discussion:0002`, this paper is one of only **three genuine head-to-head designs** in the relevant literature (with Raijmakers2021 and Patterson2024). It is the only one that ran a transcriptomic comparison across ≥3 distinct infection triggers in a *fatigue-phenotype positive* cohort with *full-recovery controls from the same infections*. Its negative cross-cohort finding should be highlighted whenever the matrix in `discussion:0002` is interpreted — the "supported" cells in the Cytokine/IFN rows for QFS/EBV/RRV derive from this paper and are **per-cohort** findings, not shared-across-cohorts findings.

### The full-recovery control design — a strength seldom noted

A feature of this study that distinguishes it from most CFS transcriptomic literature is that controls are **prospectively enrolled people who were exposed to the same infection and recovered promptly** — not healthy age-matched community controls. This design separates the PIFS transcriptomic state from the acute infection response per se, addressing a persistent confound in cross-sectional CFS studies. The lack of this control type is a major weakness in much of the CFS/ME-CFS blood transcriptomic literature (e.g., many studies use healthy volunteers as controls and cannot distinguish residual infection-related expression from PIFS-specific expression).

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PIFS (≥6 months debilitating fatigue post-infection) | PAIS / post-infective fatigue syndrome | Direct match; Dubbo criteria align with Fukuda CFS applied post-infectiously |
| Three distinct infection triggers (EBV, RRV, Q-fever) | Cross-pathogen PAIS comparison | Three of the project's named triggers; the paper is the only head-to-head transcript study across them |
| Matched full-recovery controls from same infection | PAIS vs. recovered comparison | Methodologically strong design; should be required standard for `question:0001` tests |
| No shared PBMC gene signature across triggers | Shared-biology claim at transcript level | Partial disconfirmation of `hypothesis:0001`; constrains but does not falsify it |
| Symptom-correlating transcripts (within cohort) | Disease-state-tracking biology | Consistent with path-dependent within-cohort biology despite cross-cohort divergence |
| Modest fold-changes (0.6–2.3×) | Signal magnitude calibration | Sets expectations for transcriptomic analyses in this population; not high-amplitude dysregulation |
| Dubbo Infection Outcomes Study | DIOS / Hickie 2006 cohort | The prospective cohort that grounded the cross-pathogen PAIS concept; this paper is the omics extension |

## Limitations

1. **Small per-group N (~6 cases, ~6 controls per infection trigger).** Statistical power for detecting shared effects across three small subgroups is very limited. A gene with a shared but small effect (e.g., 1.5× fold-change with within-group CV typical of whole blood) would be essentially undetectable at these numbers. The null result at gene-list level is consistent with power limitations, not only with genuine absence of shared biology.

2. **PBMC (not bulk whole-blood) transcriptomics obscures cell-type composition effects.** The study used Lymphoprep-separated PBMCs (lymphocytes + monocytes), excluding granulocytes. In 2011, single-cell and cell-type deconvolution methods were in their infancy. Differential composition of immune populations (e.g., more activated monocytes or fewer NK cells in PIFS vs. recovered) would appear as modest fold-changes in mixed populations but would not look "consistent" across cohorts if the compositional shifts involve different absolute cell proportions triggered by different pathogens. Modern deconvolution or scRNA-seq would provide a richer picture. Also, PBMC isolation itself excludes neutrophils, which are responsive to infection and may carry PIFS-relevant signals.

3. **Batch effects partially controlled but not fully eliminated.** The platform (Illumina Sentrix HumanRef-8 v2) and normalization (quantile normalization) are now confirmed from full text. A case and a control subject were run on the same BeadChip wherever possible, which controls for chip-to-chip variation within matched pairs but does not fully address batch effects across different infection groups enrolled at different times. Per-infection normalization strategies differed (paired analysis: within-subject normalization; two-sample and longitudinal: all 127 arrays normalized together), which may introduce subtle cross-analysis inconsistencies.

4. **Longitudinal time points partially mismatched across subjects.** Full text (Table 1) shows 3 or 4 time points per subject at T1 (0–6 weeks), T2 (6–12 weeks), T3 (3–9 months), T4 (>9 months / >12 months). Not all subjects had all four time points, and some had additional samples at the same time point (handled by using the array with the earlier SOMA score). Because RRV, EBV, and Q-fever PIFS may have different natural histories and recovery trajectories, mismatched time points and variable T4 intervals could obscure shared signals even if they exist. The paired analysis required SOMA ≥3 at T1 and <3 at T4, which selected only 12 of 18 cases.

5. **Case definition overlap with, but not identity to, CFS/ME.** The paper uses the Dubbo PIFS criteria, which are operationally similar to but not identical to ME/CFS criteria (IOM 2015, CCC 2003). Generalizability to CFS cohorts is probable but not guaranteed.

6. **No replication cohort.** The findings (both positive within-trigger signals and the negative cross-trigger signal) were not independently replicated. Given the small per-group N, replication in a larger sample would be needed before any within-trigger signals are treated as established.

7. **Limited to blood transcriptomics.** The study cannot address mechanisms in lymph nodes, spinal cord, dorsal root ganglia, or gut tissue — tissues where persistent antigen, immune activation, and neuroinflammation may be more directly operative. The blood is a read-out, not the seat of pathology, and may be too distal from the primary pathological process to reveal shared signals.

8. **2011 technology baseline.** RNA-seq was not yet widely applied to cohort studies; array-based approaches detect only pre-defined probe targets and are sensitive to hybridization efficiency differences. Modern short-read or long-read RNA-seq with cell-type deconvolution would substantially improve sensitivity and specificity for a repeated study.

## Model / Tool Availability

- **Microarray data deposition:** The paper contains no GEO, ArrayExpress, or other repository accession number. The "Supplementary Data" section (confirmed from full text, last page) directs readers only to supplementary tables at the JID online portal (http://www.oxfordjournals.org/our_journals/jid/), which consist of the four gene lists (Supplementary Tables 1–4 = ranked gene lists for paired, two-sample, longitudinal, and correlation analyses). These are gene lists, not raw array data. There is no data availability statement and no indication of any public deposit of the 127-array dataset. **Conclusion for task t033: no public data deposit exists as of the paper's publication; raw data are not accessible without contacting the authors (corresponding author: Barbara Cameron, b.Cameron@unsw.edu.au; senior author: Andrew Lloyd, UNSW).**
- **Software / statistical tools:** R (Bioconductor limma for moderated t-statistics; geepack for GEE); Beadstudio Gene Expression Module (Illumina) for raw data extraction; DataAssist v2.0 (Applied Biosystems) for qPCR Ct collation. No novel tools released.

## Follow-up

1. ~~Full-text access needed for confirmation~~ — **RESOLVED.** Full text read 2026-06-20. Platform (Illumina Sentrix HumanRef-8 v2, 18,203 genes), per-group N, sampling time points, normalization approach (quantile normalization, limma moderated t-statistics, GEE via geepack), and analytical strategies are all now documented above. No pathway-level analysis was performed alongside the gene-list approach — only gene-level univariate and GEE methods.

2. **GEO / data deposition: confirmed absent.** Full text contains no accession number and no data availability statement. Supplementary materials are gene lists only. To obtain raw data for reanalysis, contact Barbara Cameron (b.Cameron@unsw.edu.au) or search ArrayExpress under author names (Lloyd, Cameron, Galbraith). This is the definitive answer for task t033: no public deposit found; data must be requested from authors.

3. **Power analysis for replication design.** Given actual per-group N (3–6 per trigger in key analyses), a formal power calculation for the specific effect sizes reported (~1.5–2.3× fold-change in PBMC expression) would quantify what N per trigger group is needed to detect a cross-trigger shared signal with 80% power. This estimate would inform a study design under `question:0001`.

4. **Pathway-level reanalysis (if data are obtainable).** The study used gene-level analysis only; pathway-level analysis (GSEA, KEGG, Reactome enrichment on the per-trigger gene lists in Supplementary Tables 1–4) might reveal shared pathway perturbations even where individual gene identities differ. The supplementary gene lists are at least accessible for this purpose even without raw data.

5. **Cross-reference with Raijmakers2021 (Q fever / ME/CFS head-to-head).** The Q-fever PIFS cohort in Galbraith2011 overlaps conceptually with the Dutch QFS cohort in Raijmakers2021. Whether Q-fever-specific transcripts from Galbraith2011 (especially the 6 liberal-threshold qPCR candidates or the CYBA longitudinal hit) replicate in QFS samples would be a partial external replication test.

6. **Cameron et al. 2007 (predecessor) — platform now confirmed.** The 2011 paper uses Illumina Sentrix HumanRef-8 v2; the Cameron et al. 2007 EBV-only predecessor (PMID 17538884) is now confirmed to be from the same group and cohort. The 2007 paper reportedly identified 733 differentially expressed genes in the EBV-only design (larger signal with EBV-only focus); whether those 733 overlap with the EBV-cohort results in the 2011 multi-trigger paper would be an internal consistency check on what the multi-trigger cross-infection filter cost in sensitivity.
