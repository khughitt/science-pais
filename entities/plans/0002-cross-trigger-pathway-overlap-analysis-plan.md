---
type: plan
id: plan:0002-cross-trigger-pathway-overlap-analysis-plan
title: "Analysis plan: cross-trigger pathway-overlap reanalysis (GSE14577 + GSE130353) for q0001 (t035)"
date: 2026-06-20
created: "2026-06-20"
updated: "2026-06-20"
related:
  - question:0001-shared-molecular-signature-across-triggers
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
  - hypothesis:0001-shared-dysregulated-attractor
  - discussion:0002-cross-pathogen-pais-signature-convergence
  - paper:Gow2009
  - paper:Raijmakers2019
  - task:t035
status: ready-with-caveats
skills_loaded:
  - id: data-expression
    reason: ingesting/QA two public transcriptomic deposits before a cross-platform comparison
  - id: data-expression-microarray-qa
    reason: GSE14577 is Affymetrix U133A/B microarray (probe-to-gene, normalization scale)
  - id: data-expression-bulk-rnaseq-qa
    reason: GSE130353 is bulk RNA-seq (MMSEQ gene estimates — scale verification, counts-vs-not)
  - id: statistics-power-floor-acknowledgement
    reason: tiny per-group n; null interpretation must be guarded
  - id: statistics-bias-vs-variance-decomposition
    reason: platform + compartment + sex bias could be confused with shared signal
  - id: statistics-sensitivity-arbitration
    reason: multiple gene-set DBs, enrichment methods, and a negative-control contrast need a pre-committed rule
---

# Analysis plan: cross-trigger pathway-overlap reanalysis (GSE14577 + GSE130353) for q0001 (t035)

## Analysis Question

Does a **pathway-level transcriptomic signature** recur across two *distinct* post-infective-fatigue
triggers — post-viral CFS (GSE14577) and Q-fever fatigue syndrome (GSE130353) — **above chance and
specific to fatigue rather than to past infection exposure**? This is the cheapest available empirical
probe of `hypothesis:0001` (shared dysregulated attractor) and directly adjudicates it against the
finite-repertoire-coincidence null in `question:0017`. It is explicitly **hypothesis-generating**, not
the decisive ≥3-trigger harmonized test (which does not exist).

## Related Hypotheses / Inquiries / Tasks

- `hypothesis:0001-shared-dysregulated-attractor` — the claim under test (pathway-level convergence).
- `question:0001-shared-molecular-signature-across-triggers` — parent question.
- `question:0017-deflationary-alternatives-vs-shared-pathophysiology` — the coincidence/ascertainment nulls this scores against.
- `discussion:0002-cross-pathogen-pais-signature-convergence` — prior provenance audit; head-to-head molecular designs uniformly fail a shared *positive* signature.
- `task:t035` — the work item (seed-stage boundary crossed by explicit user authorization 2026-06-20, this bounded public reanalysis only).

## Data Inputs and Provenance

| Dataset | Trigger | Platform | Compartment | Groups (n) | Scale | Retrieval |
|---|---|---|---|---|---|---|
| **GSE14577** (Gow2009) | post-viral CFS (Fukuda) | Affymetrix U133A (GPL96) + U133B (GPL97) | **PBMC** | HC 7, PI-CFS 8 — **all male** | log2 intensities (VALUE ~6–8) | `family.soft.gz` (series_matrix 404s; data lives in SOFT) |
| **GSE130353** (Raijmakers2019) | post-bacterial QFS + idiopathic CFS | RNA-seq (MMSEQ gene estimates) | **isolated monocytes** | HC 10, CFS 10, QFS 10, **QS (seropositive-recovered) 10** | MMSEQ estimates — **not raw counts** | per-sample `*.gene.mmseq.txt.gz` + `GSE130353_RAW.tar` |

Both are public, downloaded via `science datasets download geo:<id>` into gitignored `data/raw/`.
Provenance (accession, source paper, platform, retrieval date) registered at
`doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md`. **Galbraith2011 arrays remain
`[INACCESSIBLE]`** (private; declined on reproducibility grounds) — this analysis is their public
substitute.

## Required Input Inspection

Confirmed during planning (2026-06-20):

- **GSE14577**: 30 GEO samples = 15 patients × 2 chips (U133A + U133B); 7 HC + 8 PI-CFS; sex = all
  Male; SOFT sample tables present with `ID_REF\tVALUE`, log2-scale. U133A and U133B cover *different*
  probe sets → must be combined per patient at the gene level (union after probe→gene collapse).
- **GSE130353**: 40 samples, 10 per group (HC/CFS/QFS/QS); cell type = Monocytes; series-matrix data
  table is **empty** → expression must come from the per-sample MMSEQ supplementary files.

Still to verify **at ingest** (preprocessing gate, not a readiness blocker):

1. **MMSEQ unit/scale** — open one `*.gene.mmseq.txt.gz`; confirm which column is the expression
   estimate and whether it is log-scale posterior mean / FPKM-like. Run the universal scale check
   (min/max/integer-like). MMSEQ ≠ counts → **count-based testing (DESeq2/edgeR) is out of scope**;
   use continuous limma. (Halt-on if scale is unverifiable.)
2. **Gene identifier axes** — U133 probes → symbol/Ensembl via GPL96/GPL97 annotation; MMSEQ gene IDs
   (resolve to Ensembl/symbol). Harmonize both to a canonical gene id; symbols are display-only.
3. **Independent-unit check** — GSE14577: collapse the two chips into one record per patient (15
   patients, not 30 arrays). GSE130353: one library per donor (40 donors).
4. **Sex** — GSE130353 metadata does **not** report sex; record as unmeasured (cannot match
   GSE14577's male-only restriction).

## Preprocessing / Normalization Checks

- **GSE14577**: inherit depositor log2 intensities (state normalization as a limitation; no raw CEL
  reprocessing). Probe→gene **median collapse** (per microarray-qa); drop multi-gene probes; union
  U133A+B gene universe per patient. Per-sample log2-median / IQR QC (flag outliers > 1 SD from cohort
  median). PCA coloured by group + chip; chip is a known structural factor (A vs B cover different
  genes) — handled by gene-level union, not modelled as batch.
- **GSE130353**: assemble per-donor MMSEQ gene matrix; log-transform if not already; filter genes with
  near-zero estimate across most donors (do **not** detection-filter asymmetrically across groups —
  filter on the full cohort, log the mask). PCA coloured by group; no batch metadata available → if
  batch dominates biology, downgrade (see vetoes).
- **No cross-dataset merge of expression values.** Platform/compartment differences make a probe/gene
  matrix merge indefensible (per data-expression "cross-platform aggregation"). Comparison happens at
  the **pathway-enrichment** layer only (strategy 1: within-dataset test → aggregate).
- Every decision logged to a `cohort_audit.json` sidecar per dataset (raw→filtered counts, collapse
  method, normalization status, dropped genes/samples + reasons).

## Independent Unit and Denominator

- **Within-dataset DE unit:** patient/donor (GSE14577: 8 vs 7; GSE130353: 10 vs 10 per contrast).
- **Cross-trigger claim unit:** the **cohort** — and there are only **two**. The shared-signature
  generalization rests on 2 independent cohorts, which caps it at exploratory regardless of how many
  genes/pathways are tested. Genes and pathways are **not** independent units for the cross-trigger
  verdict (guards against the high-dimensional-screen inflation in power-floor-acknowledgement).
- Enrichment-overlap denominator: the set of gene sets tested in **both** datasets (intersection of
  testable pathways), fixed before computing overlap.

## Estimand and Primary Metric

- **Per-contrast estimand:** moderated-t / NES ranking of pathway enrichment for each of
  PI-CFS-vs-HC (GSE14577), QFS-vs-HC (GSE130353, primary fatigue), CFS-vs-HC and QS-vs-HC (GSE130353).
- **Primary metric:** **direction-concordant pathway overlap** between PI-CFS-vs-HC and QFS-vs-HC —
  count and identity of gene sets significantly enriched (GSEA FDR < 0.05, pre-committed) in **both**
  with the **same NES sign**, tested against chance by Fisher's exact test on the shared testable-set,
  with Jaccard reported. **Continuous companion:** Spearman correlation of NES across *all* shared
  testable pathways (uses the full ranking, not just the FDR-passing tail).
- **Specificity filter (defines the headline set):** a concordant pathway is **fatigue-specific shared**
  only if it is **not** reproduced in QS-vs-HC (see arbitration). Pathways shared but also present in
  QS are labelled `exposure_sequela`.

## Model / Test Assumptions

- **DE:** limma moderated-t per dataset on continuous expression (log2 intensities; log-MMSEQ).
  Same model form both datasets (`~ group`); no covariate adjustment available (sex constant/unknown;
  age absent). limma's normality/variance assumptions are reasonable on log-scale continuous values;
  empirical-Bayes shrinkage is the small-n mitigation.
- **Enrichment:** **GSEA (fgsea)** on the full limma-t ranking — preferred over ORA at this n because
  it needs no per-gene significance cutoff (per power-floor: avoid pretending each gene test is
  standalone). Gene sets: MSigDB **Hallmark** (primary), with **Reactome** and **GO-BP** as
  measurement sensitivities; restricted a priori to the immune, oxidative-stress, mitochondrial, and
  apoptosis modules named in t035 plus the unrestricted Hallmark run.
- **Assumption that could break the comparison:** that pathway-level enrichment is comparable across a
  PBMC microarray contrast and a monocyte RNA-seq contrast. Each contrast is **internally
  cell-type-matched** (cases vs same-compartment HC), so compartment differences are differenced out
  *within* contrast; the cross-dataset object compared is enrichment *results*, not expression. This is
  the design's load-bearing assumption — stated, not assumed away.

## Power Floor or Resolution Limit

- **Per-gene DE:** at n = 8 vs 7 and 10 vs 10, only large standardized effects reach FDR < 0.05; the
  minimum detectable per-gene effect far exceeds plausible post-infectious fold-changes. Hence we do
  **not** threshold genes — GSEA aggregates the whole ranking, trading per-gene resolution for
  pathway-level power.
- **Cross-trigger resolution:** with **2 cohorts**, the analysis can surface a *suggestive* concordant
  signature but **cannot confirm** a shared mechanism, and a **null is non-arbitrating** (cannot
  exclude a real shared signature given platform + compartment + power limits). Verdict ceiling:
  *suggestive, needs the ≥3-trigger test*. Negative ceiling: *unresolved/non-arbitrating*, never
  "evidence against shared biology."
- Multiplicity: FDR within each contrast (BH across pathways); overlap defined only on FDR-passing
  sets; the chance baseline (Fisher) accounts for the shared testable-set size.

## Bias vs Variance Risks

| Error term | Source | Shrinks with | Diagnostic | Mitigation |
|---|---|---|---|---|
| Sampling variance | 8–10 donors/group | more donors (unavailable) | limma SE / GSEA p | empirical-Bayes shrinkage; pathway aggregation; label exploratory |
| **Platform bias** | microarray vs RNA-seq | nothing | NES-concordance scatter | compare at enrichment level only; never merge matrices |
| **Compartment bias** | PBMC vs isolated monocyte | nothing | cell-type-marker pathway leakage | within-contrast cell-type matching; scope verdict to "monocyte-inclusive" pathways |
| **Sex bias** | GSE14577 male-only; GSE130353 sex unknown | nothing | — | unmeasured; carry as limitation; cannot adjust |
| **Exposure (not fatigue) bias** | past *Coxiella* exposure | nothing | **QS-vs-HC negative control** | veto pathways reproduced in QS (`exposure_sequela`) |
| MMSEQ estimate bias | model-based expression vs counts | nothing | scale check at ingest | continuous limma; no count-based inference |
| Batch (GSE130353) | no batch metadata | nothing | per-cohort PCA | veto if batch dominates biology |

Compute (more permutations/bootstraps) shrinks **none** of the concerning terms — they are bias, not
variance. Stated explicitly so a narrow GSEA p-value is not misread as strong evidence.

## Sensitivity Arbitration (pre-committed)

**Primary:** direction-concordant Hallmark GSEA overlap between PI-CFS-vs-HC and QFS-vs-HC, FDR < 0.05.

**Mandatory sensitivities (verdict stands only if these run):**
1. **QS negative-control veto** — recompute the shared set after removing pathways with QS-vs-HC NES
   same-sign and |NES_QS| ≥ 0.5·|NES_QFS|. Headline set = post-veto.
2. **Gene-set-DB sensitivity** — repeat with Reactome and GO-BP; a pathway *theme* (e.g. oxidative
   stress, innate/IFN, mitochondrial, apoptosis) must recur across ≥2 DBs to count as robust.
3. **Enrichment-method sensitivity** — ORA on FDR-passing genes as a cross-check on GSEA.
4. **Second fatigue contrast** — CFS-vs-HC (idiopathic) within GSE130353: does the GSE14577 overlap
   hold for QFS only, or also for idiopathic CFS?

**Decision table (labels produced mechanically):**
- `shared_suggestive` — primary overlap exceeds chance (Fisher p < 0.05), survives QS veto, and a
  pathway theme recurs across ≥2 gene-set DBs. (Ceiling verdict — "suggestive, needs ≥3-trigger test".)
- `fragile` — overlap exceeds chance but collapses under DB or method sensitivity.
- `exposure_confounded` — shared set is largely eliminated by the QS veto (signal is *Coxiella*
  exposure sequela, not fatigue). Directly corroborates Raijmakers2019's caution.
- `compartment_confounded` — shared pathways are dominated by monocyte/PBMC cell-type-marker sets.
- `null_nonarbitrating` — no above-chance overlap; **does not** support the coincidence null given the
  power/bias ceiling — reported as unresolved, feeds q0017 as "existing public data cannot adjudicate".
- `batch_confounded` / `model_inadequate` — GSE130353 PCA batch-dominated, or limma diagnostics fail.

Post-hoc analyses (any not listed above) are labelled post-hoc and excluded from the verdict.

## Required Output Artifacts

- `data/processed/<gse>/` per dataset: `cohort_audit.json`, gene-collapsed expression `.parquet`,
  `per_sample_metrics.tsv`, `pca_diagnostic`, probe/gene-collapse log; a `datapackage.json`.
- A **QA report per processed matrix** (`results/.../qa_report.md`) with the structural/distribution
  split (structural: unique donor key, required group labels present, allowed group codes, gene-id
  resolved; distribution: log2-median/IQR ranges, gene-universe size, % missing) — the same
  wired-in-checkpoint discipline as t037, applied here.
- Per-contrast limma tables + ranked gene lists; fgsea results per contrast/DB; the overlap table with
  QS-veto annotations; NES-concordance scatter (GSE14577 vs GSE130353); the mechanical verdict label.
- A results markdown synthesizing into `question:0001` / `hypothesis:0001` / `question:0017`.

## Aspect-contributed Sections

The `computational-analysis` aspect is **not** declared in `science.yaml`, though `code/` will now
hold a real workflow. Recommend enabling it (it wires QA-checkpoints and DAG-validation into the
pipeline) when execution starts — the t037 convention (build-fatal, two-severity, config-driven QA)
applies to this pipeline's processed matrices too. Flagged, not auto-added.

## Readiness Decision

**ready-with-caveats.** Both datasets are public, retrieved, and confirmed usable; contrasts are
well-defined; a built-in specificity control (QS) exists; methods (per-dataset limma → GSEA →
direction-concordant overlap with QS veto) are specified with a pre-committed arbitration rule. No
hard blocker remains — the open items (MMSEQ scale verification, gene-id harmonization) are ingest-time
preprocessing gates, not methodology blockers. The caveats below **bound the claims, not the
validity**, and are consistent with t035's hypothesis-generating framing.

Next step before code: a **light pre-registration** (`/science:pre-register`) locking the arbitration
rule above (primary contrast, FDR threshold, QS-veto fraction, DB/method sensitivities, verdict
labels) — important even for an exploratory analysis to prevent post-hoc story selection, then
`/science:plan-pipeline` for orchestration.

## Known Limitations To Carry Forward

1. **Two cohorts only** → exploratory ceiling; cannot confirm a shared mechanism; null is non-arbitrating.
2. **Platform heterogeneity** (U133A/B microarray vs MMSEQ RNA-seq) → comparison valid only at the
   pathway-enrichment layer; no expression-matrix merge.
3. **Compartment mismatch** (PBMC vs isolated monocytes) → shared signal scoped to monocyte-inclusive
   pathways; cell-type-marker leakage is a named veto.
4. **Sex** — GSE14577 male-only; GSE130353 sex unreported → unmeasured confound, unadjustable.
5. **MMSEQ estimates ≠ counts** → continuous modelling only; count-based inference out of scope.
6. **Depositor normalization inherited** (no raw CEL/FASTQ reprocessing) → scale comparability stated
   as a limitation.
7. **QS veto is the specificity backbone** — a shared signature that does not survive it is an
   exposure sequela, not evidence for `hypothesis:0001`.

## Feedback Reflection

The plan-analysis template and the expression + statistics leaves fit this cross-platform, cross-
compartment, tiny-n case well; the sensitivity-arbitration leaf was decisive for turning the QS group
into a pre-committed veto rather than a post-hoc caveat. No friction worth a feedback item.
