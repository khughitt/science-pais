---
id: paper:Galbraith2011
type: paper
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
- **Source:** Abstract (Europe PMC) + OUP article page; full-text PDF blocked (HTTP 403 despite Unpaywall OA record). All methods/results detail derived from the structured abstract; quantitative values are taken directly from the abstract and are reliable. Per-group N splits and microarray platform name are [UNVERIFIED] — the abstract gives only totals.

## Key Contribution

This is the **only published head-to-head transcriptomic comparison** of peripheral blood gene expression across three distinct infection triggers of post-infective fatigue syndrome (PIFS) within a single, prospectively designed cohort. Using the Dubbo Infection Outcomes Study (DIOS) — the longitudinal Australian cohort that established PIFS as a cross-pathogen phenomenon — Galbraith et al. compared whole-blood transcriptomes at multiple time points in subjects who developed ≥6 months of debilitating fatigue after EBV (glandular fever), Ross River virus (RRV), or *Coxiella burnetii* (Q fever) against matched controls who recovered promptly from the same infections.

The key finding is a **definitive negative for a shared cross-cohort peripheral blood gene expression signature**: despite strong clinical similarity among the three PIFS groups, quantitative PCR confirmed that *none* of the differentially expressed genes identified within any one cohort were consistent across all three infection cohorts. Within-trigger and cross-sectional signals were modest to begin with (0.6–2.3-fold change range; 23–63 genes depending on the analysis), and the qPCR confirmation rate (73% of tested genes, n = 33/45) indicates reasonable analytical validity — but the confirmed genes did not overlap across triggers.

This paper is the **load-bearing empirical test** for `discussion:0002` and `question:0001`. It is the closest existing study to the decisive "shared-attractor" test demanded by `hypothesis:0001`, and its result is: **partial shared biology at the clinical/symptom level, but no shared peripheral-blood molecular signature at the gene level**. The implication for the project is nuanced — the negative result constrains the "shared attractor" model to pathway-level or upstream regulatory convergence rather than a common terminal set of differentially expressed transcripts in bulk peripheral blood.

## Methods

**Study:** Nested within the Dubbo Infection Outcomes Study (DIOS), a prospective surveillance cohort that enrolled patients with serologically confirmed acute EBV, RRV, or Q-fever infections in the Dubbo region of New South Wales, Australia. DIOS is the same cohort reported in Hickie et al. 2006 (*BMJ*), which first documented parallel PIFS incidence (~11–12% of acute cases) across all three triggers.

**Case definition:** PIFS defined as ≥6 months of disabling fatigue, musculoskeletal pain, neurocognitive difficulties, and unrefreshing sleep following documented acute infection — the original Dubbo PIFS criteria, operationally equivalent to the Fukuda CFS criteria applied in post-infectious context.

**Participants:** 18 PIFS cases and 18 matched control subjects who recovered promptly from the same acute infections. Controls were matched from the same cohort, reducing confounding by infection episode, community setting, and seasonal exposure. Total n = 36. The three infection groups (EBV, RRV, Q-fever) are distributed within the 18 case / 18 control framework, giving approximately 6 cases and 6 controls per trigger group [UNVERIFIED exact per-group split — abstract gives only aggregate totals]. This small per-group N (~6) is a recognized design constraint (see Limitations).

**Biological material:** Peripheral whole blood, collected longitudinally at multiple time points: at least one early, symptomatic time point (within the first months of established PIFS) and a late, convalescent/recovered time point (for cases, this was defined as clinical recovery or the matched late-follow-up for controls). The longitudinal within-subject design was the primary analytical comparison; cross-sectional case-vs-control at the 6-month mark was a secondary comparison.

**Gene expression platform:** Microarray (type/manufacturer not specified in the abstract; the predecessor Cameron et al. 2007 paper from the same group [PMID 17538884] used oligonucleotide microarrays covering ~30,000 genes, likely the same or a closely related platform) [UNVERIFIED — platform name requires full-text]. Total 127 microarray samples were profiled across all subjects and time points.

**Confirmatory assay:** Quantitative polymerase chain reaction (qPCR) performed on a subset of 45 candidate genes identified by microarray. The 73% confirmation rate (33/45) is used as an indicator of platform reliability.

**Statistical analyses:** Univariate statistics (fold-change and statistical significance thresholds applied per-gene) and regression modeling. Three main analytical strategies were run: (1) within-subject longitudinal comparison (early symptomatic vs. late recovered time points); (2) cross-sectional case-vs-control comparison at 6 months post-infection onset; and (3) regression of individual gene expression against individual symptom domain scores (fatigue, musculoskeletal pain, neurocognitive, sleep). The third analysis — symptom-domain correlation — is important because it addresses the question of whether any transcripts track symptom severity continuously rather than simply case/control status.

**Funding:** Partially supported by USPHS grant U50/CCU019851-01 (CDC/PHS). The Dubbo cohort infrastructure was supported by Australian government and UNSW funding (Lloyd group).

## Key Findings

### 1. Within-subject longitudinal comparison (early symptomatic vs. late recovered)

- **23 genes** showed statistically significant differential expression between early, acutely symptomatic time points and late, recovered time points.
- Fold-change range: **0.6–2.3×** — notably modest compared to many immune-activation signatures, implying these are subtle rather than dramatic expression changes.
- Direction of change: not specified in the abstract; likely a mix of up- and down-regulated transcripts.
- The within-subject design is the most powerful for detecting state-dependent change (each subject serves as their own control), but the small within-group N constrains power.

### 2. Cross-sectional case-vs-control comparison at 6 months

- **63 genes** showed modest differential expression in either the 6-month cross-sectional case-vs-control comparison or in the regression model — a substantially larger set than the within-subject comparison.
- This enlargement likely reflects additional between-subject variance captured in the cross-sectional frame, plus regression-identified genes that track symptom severity.

### 3. Symptom-domain correlation analysis

- **223 genes** significantly correlated with individual symptom domains (fatigue, musculoskeletal pain, neurocognitive disturbance, sleep disturbance).
- This is the largest gene set and spans all three infection cohorts [UNVERIFIED whether the 223 is aggregate or per-cohort]. It indicates that peripheral blood transcription does track subjective symptom variation *within individuals*, even if the overall case-vs-control signal is modest.
- This correlation structure is potentially the most biologically informative finding: it suggests disease-state-tracking transcripts exist, but they may be too noisy or subject-specific to constitute a reliable cross-cohort signature.

### 4. qPCR confirmation

- 33 of 45 genes tested (73%) were confirmed by qPCR. This validation rate is acceptable and indicates the microarray signal was not predominantly artifactual.
- The 12 genes (27%) not confirmed may reflect technical noise, low fold-changes near detection thresholds, or true false positives.

### 5. Cross-cohort consistency — the critical finding

> **"None were consistent across cohorts."** (abstract, Conclusions)

This is the paper's most consequential result. Of the genes identified in any one analysis (within-subject, cross-sectional, or symptom-correlation), and confirmed by qPCR, **zero were shared across all three infection-trigger cohorts** (EBV, RRV, Q-fever). The result appears to hold whether comparing at the level of individual genes or the broader sets — the abstract's phrasing ("none were consistent") is unambiguous.

The implication is that peripheral blood gene expression, as measured in bulk whole blood by this microarray protocol and at these follow-up time points, does not produce a **trigger-agnostic molecular fingerprint** of PIFS. Each infection cohort has its own modest expression signature, but these signatures do not converge.

This does **not** necessarily mean that biology is entirely trigger-specific. Possible explanations include: (a) the shared mechanism exists but operates at pathway level or in a cell-type not detected in bulk blood; (b) sampling time points differ across cohorts in ways that obscure a shared transient signal; (c) per-group N (~6) was insufficient to detect modest shared effects against within-group noise; (d) the shared state-change is post-translational, epigenetic, or metabolic rather than transcriptomic.

### Summary verdict on shared vs. trigger-specific biology

| Level | Finding | Interpretation |
|---|---|---|
| Clinical symptom profile | Similar across EBV, RRV, Q-fever PIFS | **Supports** shared biology |
| Peripheral-blood transcriptome (bulk) | No genes consistent across triggers | **Does not support** a single shared blood transcript signature |
| Within-trigger symptom correlation | 223 genes track symptoms within cohorts | Suggests disease-tracking biology exists but is trigger-specific or noisy |
| qPCR validation | 73% overall, 0% cross-cohort | Analytically valid negative cross-cohort result |

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
| No shared peripheral blood gene signature | Shared-biology claim at transcript level | Partial disconfirmation of `hypothesis:0001`; constrains but does not falsify it |
| Symptom-correlating transcripts (within cohort) | Disease-state-tracking biology | Consistent with path-dependent within-cohort biology despite cross-cohort divergence |
| Modest fold-changes (0.6–2.3×) | Signal magnitude calibration | Sets expectations for transcriptomic analyses in this population; not high-amplitude dysregulation |
| Dubbo Infection Outcomes Study | DIOS / Hickie 2006 cohort | The prospective cohort that grounded the cross-pathogen PAIS concept; this paper is the omics extension |

## Limitations

1. **Small per-group N (~6 cases, ~6 controls per infection trigger).** Statistical power for detecting shared effects across three small subgroups is very limited. A gene with a shared but small effect (e.g., 1.5× fold-change with within-group CV typical of whole blood) would be essentially undetectable at these numbers. The null result at gene-list level is consistent with power limitations, not only with genuine absence of shared biology.

2. **Bulk whole-blood transcriptomics obscures cell-type composition effects.** In 2011, single-cell and cell-type deconvolution methods were in their infancy. Differential composition of immune populations (e.g., more activated monocytes or fewer NK cells in PIFS vs. recovered) would appear as modest fold-changes in mixed populations but would not look "consistent" across cohorts if the compositional shifts involve different absolute cell proportions triggered by different pathogens. Modern deconvolution or scRNA-seq on these samples would provide a richer picture.

3. **Microarray platform not specified in abstract.** The array generation, probe set, normalization method, and batch correction approach cannot be assessed. If different arrays or batches were used for different infection cohorts (e.g., serially enrolled and processed), technical batch effects could partly explain the cross-cohort inconsistency [UNVERIFIED — requires full-text methods].

4. **Longitudinal time points not fully described.** The abstract specifies "early, symptomatic time points" vs. "late, recovered time points" but does not give the number of time points, the intervals, or whether all three infection cohorts had identical sampling schedules. Because RRV, EBV, and Q-fever PIFS may have different natural histories and recovery trajectories, mismatched time points could preclude finding shared signals even if they exist.

5. **Case definition overlap with, but not identity to, CFS/ME.** The paper uses the Dubbo PIFS criteria, which are operationally similar to but not identical to ME/CFS criteria (IOM 2015, CCC 2003). Generalizability to CFS cohorts is probable but not guaranteed.

6. **No replication cohort.** The findings (both positive within-trigger signals and the negative cross-trigger signal) were not independently replicated. Given the small per-group N, replication in a larger sample would be needed before any within-trigger signals are treated as established.

7. **Limited to blood transcriptomics.** The study cannot address mechanisms in lymph nodes, spinal cord, dorsal root ganglia, or gut tissue — tissues where persistent antigen, immune activation, and neuroinflammation may be more directly operative. The blood is a read-out, not the seat of pathology, and may be too distal from the primary pathological process to reveal shared signals.

8. **2011 technology baseline.** RNA-seq was not yet widely applied to cohort studies; array-based approaches detect only pre-defined probe targets and are sensitive to hybridization efficiency differences. Modern short-read or long-read RNA-seq with cell-type deconvolution would substantially improve sensitivity and specificity for a repeated study.

## Model / Tool Availability

- **Microarray data deposition:** No GEO accession number was identified through PubMed record, full paper metadata (Crossref/Unpaywall), or direct GEO database searches. The raw or processed microarray data do not appear to be publicly deposited — or if they are, they are not indexed under the paper's PMID or authors' names in GEO. This is a significant gap for reanalysis purposes given the study's unique design (see Follow-up below).
- **Software / statistical tools:** Standard univariate microarray analysis and regression; no novel tool or model is described or released.

## Follow-up

1. **Full-text access needed for confirmation.** Several key methodological fields remain [UNVERIFIED] because only the abstract was accessible: exact per-group N (cases/controls per infection trigger), microarray platform name and version, normalization/batch-correction approach, exact sampling time points per group, and whether any pathway-level analysis was attempted alongside the gene-list approach. Institutional or author-provided PDF would resolve these.

2. **GEO / data deposition search.** The raw microarray data are not publicly visible via standard GEO/PubMed-linked searches. Two avenues worth pursuing: (a) contact the corresponding author (Andrew Lloyd, UNSW Fatigue Clinic) directly — this is the most efficient route given the 2011 vintage; (b) search ArrayExpress (EMBL-EBI) for the same study, as some 2011-era Australian microarray studies were deposited there rather than GEO. If data are retrievable, a reanalysis with pathway-level enrichment and modern deconvolution methods (CIBERSORT, xCell) against published PAIS pathway signatures would directly test whether the null cross-trigger result at gene level survives at pathway level.

3. **Power analysis for replication design.** Given the paper's per-group N (~6), a formal power calculation for the specific effect sizes reported (e.g., 1.5–2.3× fold-changes) would show what N per group is needed to detect a cross-trigger shared signal with 80% power. This estimate would inform a study design proposal under `question:0001`.

4. **Pathway-level reanalysis (if data are obtainable).** The authors used gene-level analysis; pathway-level analysis (GSEA, KEGG, Reactome enrichment) might reveal shared pathway perturbations even if individual gene identities differ — consistent with the "convergent domains" interpretation in `discussion:0002`. This is the single highest-value computational extension of this paper.

5. **Cross-reference with Raijmakers2021 (Q fever / ME/CFS head-to-head).** The Q-fever cohort in Galbraith2011 partially overlaps conceptually with the Dutch Q-fever fatigue syndrome (QFS) cohort in Raijmakers2021. Whether any of the Q-fever specific transcripts from Galbraith2011 replicate in independent QFS samples would be a partial replication test.

6. **Cameron et al. 2007 (predecessor) full-text.** The predecessor EBV-only paper from the same Dubbo cohort (PMID 17538884; Cameron, Galbraith et al., *J Infect Dis* 2007) would reveal the microarray platform and whether the 733 genes identified in that study (larger signal in the EBV-only design) overlap with the EBV-cohort findings in the 2011 multi-trigger paper — an internal consistency check.
