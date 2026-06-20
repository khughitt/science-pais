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
| **GSE14577** (Gow2009) | post-viral CFS (Fukuda) | Affymetrix U133A (GPL96) + U133B (GPL97) | **PBMC** | HC 7, PI-CFS 8 — **all male** | log2 intensities (VALUE ~6–8) | expression in `family.soft.gz` (series_matrix 404s) |
| **GSE130353** (Raijmakers2019) | post-bacterial QFS + idiopathic CFS | RNA-seq (MMSEQ gene estimates) | **isolated monocytes** | HC 10, CFS 10, QFS 10, **QS (seropositive-recovered) 10** | MMSEQ estimates — **not raw counts** | expression in per-sample `*.gene.mmseq.txt.gz` (or `GSE130353_RAW.tar`) |

**Provenance state (do not overstate).** As of this plan, only the **metadata/structure** files have
been retrieved into gitignored `data/raw/` (`GSE14577_family.soft.gz`,
`GSE130353_family.soft.gz`, `GSE130353_series_matrix.txt.gz`) and inspected. The **expression payloads
are not yet provisioned**: GSE14577's intensity tables sit inside the (downloaded) SOFT but are
unparsed; GSE130353's 40 per-sample MMSEQ files are *listed in the SOFT* but **not downloaded**. The
registry (`doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md`) correctly still reads "candidate
datasets, not yet provisioned." Acquisition + hashing + scale-parse is a **blocking gate** (see
Readiness Decision), not yet discharged. **Galbraith2011 arrays remain `[INACCESSIBLE]`** (private;
declined on reproducibility grounds) — this analysis is their public substitute.

## Required Input Inspection

Confirmed during planning (2026-06-20):

- **GSE14577**: 30 GEO samples = 15 patients × 2 chips (U133A + U133B); 7 HC + 8 PI-CFS; sex = all
  Male; SOFT sample tables present with `ID_REF\tVALUE`, log2-scale. U133A and U133B cover *different*
  probe sets → must be combined per patient at the gene level (union after probe→gene collapse).
- **GSE130353**: 40 samples, 10 per group (HC/CFS/QFS/QS); cell type = Monocytes; series-matrix data
  table is **empty** → expression must come from the per-sample MMSEQ supplementary files.

Still to verify **at acquisition/ingest** — these are **blocking** (see Readiness Decision), not
optional polish:

1. **Acquire + hash the expression payloads** — download GSE14577's SOFT intensity tables (already
   local, unparsed) and **GSE130353's 40 per-sample MMSEQ files**; record SHA-256 per file in the
   datapackage. Until this runs, "usable" is *inferred from metadata*, not verified.
2. **MMSEQ unit/scale** — open one `*.gene.mmseq.txt.gz`; confirm which column is the expression
   estimate and whether it is log-scale posterior mean / FPKM-like. Run the universal scale check
   (min/max/integer-like). MMSEQ ≠ counts → **count-based testing (DESeq2/edgeR) is out of scope**;
   use continuous limma. **Halt-on** if scale is unverifiable.
3. **Gene identifier axes** — U133 probes → symbol/Ensembl via GPL96/GPL97 annotation; MMSEQ gene IDs
   (resolve to Ensembl/symbol). Harmonize both to a canonical gene id; symbols are display-only.
4. **Independent-unit check** — GSE14577: collapse the two chips into one record per patient (15
   patients, not 30 arrays). GSE130353: one library per donor (40 donors).
5. **Sex** — GSE130353 metadata does **not** report sex; record as unmeasured (cannot match
   GSE14577's male-only restriction).

## Preprocessing / Normalization Checks

- **GSE14577**: inherit depositor log2 intensities; **raw CEL reprocessing is deferred deliberately,
  not by oversight.** Gow2009 deposits raw CELs and its note recommends re-normalization *for
  cross-cohort harmonization* — but this design never pools GSE14577 expression with GSE130353
  (comparison is at the pathway-enrichment layer), and the per-contrast statistic is **GSEA on the
  within-dataset limma-t rank**, which is invariant to monotone per-sample normalization choices (RMA
  vs MAS5 vs the deposited matrix). So CEL reprocessing is low-value *for this rank-based estimand*.
  The bound it imposes: any *absolute-scale* or magnitude claim is out of scope, and a single-run RMA
  re-normalization is held as an **optional robustness check** (not mandatory) should the primary
  signal hinge on a small number of borderline sets. Probe→gene **median collapse** (per
  microarray-qa); drop multi-gene probes; union U133A+B gene universe per patient. Per-sample
  log2-median / IQR QC (flag outliers > 1 SD from cohort median). PCA coloured by group + chip; chip is
  a known structural factor (A vs B cover different genes) — handled by gene-level union, not modelled
  as batch.
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
  PI-CFS-vs-HC (GSE14577), QFS-vs-HC (GSE130353, primary fatigue), CFS-vs-HC (GSE130353), and the two
  specificity contrasts **QFS-vs-QS** (fatigue holding *Coxiella* exposure constant) and QS-vs-HC
  (exposure without fatigue).
- **Primary metric — NES rank concordance with a permutation null (NOT Fisher).** The verdict-bearing
  statistic is the **Spearman ρ of NES across the full shared testable gene-set universe** between
  PI-CFS-vs-HC and QFS-vs-HC. Its significance comes from a **sample-label permutation null**: permute
  group labels *within each dataset independently*, rerun limma→GSEA→NES vectors→ρ, and compute the
  one-sided p as the fraction of permuted ρ ≥ observed (B ≥ 2000, or exhaustive where the label space
  is small — C(15,8)=6435, C(20,10)=184k). This null **preserves gene-set correlation structure** (same
  sets) and the tested-set size, which a Fisher's-exact test over FDR-passing sets does *not* —
  MSigDB sets share genes, so Fisher treats correlated pathways as independent draws and is
  anti-conservative. **Demoted to descriptive only (not verdict-bearing):** the count/identity of
  FDR<0.05 direction-concordant sets, their Jaccard, and the Fisher statistic — reported for
  interpretability, never as the "above chance" test.
- **Specificity (revised — presence, not absence).** Fatigue-specificity is established by the
  **direct QFS-vs-QS contrast** (both groups *Coxiella*-exposed; the difference is fatigue): a shared
  pathway counts as fatigue-specific only if it carries **concordant signal in QFS-vs-QS**. The
  **QS-vs-HC** contrast is reframed as *exposure-confounding evidence* — if a "shared" pathway is also
  enriched in QS-vs-HC (exposure without fatigue), that is positive evidence it is a *Coxiella*-exposure
  sequela. "Not reproduced in QS-vs-HC" at n=10 is weak absence-of-evidence and is **no longer** the
  specificity criterion (it only contributes to the `exposure_confounded` label).

## Model / Test Assumptions

- **DE:** limma moderated-t per dataset on continuous expression (log2 intensities; log-MMSEQ).
  Same model form both datasets (`~ group`); no covariate adjustment available (sex constant/unknown;
  age absent). limma's normality/variance assumptions are reasonable on log-scale continuous values;
  empirical-Bayes shrinkage is the small-n mitigation.
- **Enrichment:** **GSEA (fgsea)** on the full limma-t ranking — preferred over ORA at this n because
  it needs no per-gene significance cutoff (per power-floor: avoid pretending each gene test is
  standalone).
- **Gene-set universe (to be locked verbatim in the pre-registration; defaults stated here):**
  MSigDB **release pinned** (default `2024.1.Hs`; the exact release hash is a pre-reg commitment);
  **size filter** `15 ≤ |set| ≤ 500` (fgsea minSize/maxSize); collections: **Hallmark (H, 50 sets)** =
  primary; **Reactome (C2:CP:REACTOME)** and **GO-BP (C5:GO:BP)** = DB sensitivities. The "restricted
  modules" are not ad hoc: a **pre-registered keyword→theme map** collapses enriched sets into themes
  {innate/IFN, oxidative-stress, mitochondrial/OXPHOS, apoptosis, adaptive/T-cell, other}; a theme is
  "shared" iff ≥1 set in it is direction-concordant in both datasets. The keyword→theme table and the
  pinned release are locked at pre-reg so the overlap denominator cannot drift post-hoc.
- **Permutation null implementation:** the within-each-dataset label permutation reruns the *entire*
  limma→GSEA chain (not just a gene shuffle), so the null inherits the real gene–gene and set–set
  correlation. Use the same pinned gene sets and size filter on every permutation. Report the null
  histogram of ρ alongside the observed value.
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
- Multiplicity: FDR within each contrast (BH across pathways) for the *descriptive* FDR-passing
  tallies. The verdict's chance baseline is **not** Fisher but the **sample-label permutation null**
  on the NES rank-concordance ρ, which calibrates against the actual gene-set correlation and
  tested-set structure (Fisher over correlated sets is anti-conservative — see Estimand).

## Bias vs Variance Risks

| Error term | Source | Shrinks with | Diagnostic | Mitigation |
|---|---|---|---|---|
| Sampling variance | 8–10 donors/group | more donors (unavailable) | limma SE / GSEA p | empirical-Bayes shrinkage; pathway aggregation; label exploratory |
| **Platform bias** | microarray vs RNA-seq | nothing | NES-concordance scatter | compare at enrichment level only; never merge matrices |
| **Compartment bias** | PBMC vs isolated monocyte | nothing | cell-type-marker pathway leakage | within-contrast cell-type matching; scope verdict to "monocyte-inclusive" pathways |
| **Sex bias** | GSE14577 male-only; GSE130353 sex unknown | nothing | — | unmeasured; carry as limitation; cannot adjust |
| **Exposure (not fatigue) bias** | past *Coxiella* exposure | nothing | **QFS-vs-QS** (specificity) + **QS-vs-HC** (exposure-confounding) | require concordant QFS-vs-QS signal; flag QS-vs-HC reproduction as `exposure_sequela` |
| **Gene-set correlation (test-calibration) bias** | overlapping MSigDB sets | — | permuted-ρ null histogram | sample-label permutation null (not Fisher) — this is calibration, not a variance term |
| MMSEQ estimate bias | model-based expression vs counts | nothing | scale check at ingest | continuous limma; no count-based inference |
| Batch (GSE130353) | no batch metadata | nothing | per-cohort PCA | veto if batch dominates biology |

Most of these are **bias**, not variance — more permutations/bootstraps shrink none of them, so a
narrow nominal GSEA p must not be read as strong evidence. The **one** thing the permutation null
*does* fix is test **calibration** under gene-set correlation (the anti-conservative-Fisher problem):
that is a mis-calibration of the null, not a reduction of sampling variance, and the permutation
budget B only sharpens the Monte-Carlo estimate of an already-correct null — it does not buy
independent-unit information.

## Sensitivity Arbitration (pre-committed)

**Primary:** NES rank-concordance ρ between PI-CFS-vs-HC and QFS-vs-HC over the pinned Hallmark
universe, **significance from the sample-label permutation null** (one-sided p_perm).

**Mandatory sensitivities (verdict stands only if these run):**
1. **QFS-vs-QS specificity (presence)** — the shared/concordant pathways must carry concordant signal
   in the direct QFS-vs-QS contrast (fatigue holding exposure constant). This is the specificity
   backbone, replacing the old "absent-in-QS" veto.
2. **QS-vs-HC exposure check** — if concordant pathways are *also* enriched in QS-vs-HC, label
   `exposure_sequela` (positive evidence of exposure-driven, not fatigue-driven, signal).
3. **Gene-set-DB sensitivity** — repeat ρ + permutation null with Reactome and GO-BP; a *theme* must
   recur across ≥2 DBs to count as robust.
4. **Second fatigue contrast** — CFS-vs-HC (idiopathic) within GSE130353: does the GSE14577 concordance
   hold for QFS only, or also for idiopathic CFS?

**Optional diagnostics (do NOT change the verdict; informative only):**
- **ORA** on a top-N / effect-size gene universe (not FDR-passing genes, which may be empty at this n
  for power reasons — an empty ORA must never produce `fragile`).
- Single-run RMA re-normalization of GSE14577 (the deferred-CEL robustness check).

**Decision table (labels produced mechanically):**
- `shared_suggestive` — p_perm < 0.05, QFS-vs-QS specificity holds, and a theme recurs across ≥2
  gene-set DBs. (Ceiling verdict — "suggestive, needs ≥3-trigger test".)
- `fragile` — p_perm < 0.05 but the concordance theme **does not** recur across ≥2 DBs (DB-sensitive).
  *Not* triggered by an empty ORA.
- `exposure_confounded` — concordant pathways fail QFS-vs-QS specificity and/or are reproduced in
  QS-vs-HC (signal tracks *Coxiella* exposure, not fatigue). Directly corroborates Raijmakers2019's
  caution.
- `compartment_confounded` — concordant pathways are dominated by monocyte/PBMC cell-type-marker sets.
- `null_nonarbitrating` — p_perm ≥ 0.05; **does not** support the coincidence null given the power/bias
  ceiling — reported as unresolved, feeds q0017 as "existing public data cannot adjudicate".
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

**ready-with-caveats** — where "ready" means **the design is methodologically sound and the data is
structurally confirmed** (group sizes, platforms, compartments, contrasts, and the existence of the
expression payloads are verified from the SOFT metadata). It does **not** yet mean the expression data
is provisioned: only metadata/structure files are local, and the GSE130353 MMSEQ payloads are
unretrieved (see Provenance state). The methods (per-dataset limma → GSEA → NES rank-concordance with a
permutation null, QFS-vs-QS specificity) are specified with a pre-committed arbitration rule. The
caveats below **bound the claims, not the validity**, consistent with t035's hypothesis-generating
framing.

### Blocking Checks Before Execution

These gate the *run*, not the plan; none is currently discharged:

1. **Acquisition + hash gate** — download GSE14577 intensity tables (parse from local SOFT) and the 40
   GSE130353 MMSEQ files; record SHA-256 per file; flip the registry from "candidate / not yet
   provisioned" to provisioned. Until done, "usable" stays *inferred*.
2. **MMSEQ scale-parse gate** — verify the expression-estimate column and scale (Halt-on if
   unverifiable); confirm continuous-limma applicability.
3. **Gene-id harmonization gate** — resolve U133 probes and MMSEQ ids to a shared canonical gene id;
   record the mapped/unmapped fractions.
4. **Pre-registration** (`/science:pre-register`) — lock the arbitration rule above: primary =
   NES-concordance permutation p; pinned MSigDB release + size filter + keyword→theme map; QFS-vs-QS
   specificity; DB/contrast sensitivities; ORA-as-diagnostic; verdict labels. Required even for an
   exploratory analysis to prevent post-hoc story selection.

Then `/science:plan-pipeline` for orchestration. (These four are tracked as t035 sub-work.)

## Known Limitations To Carry Forward

1. **Two cohorts only** → exploratory ceiling; cannot confirm a shared mechanism; null is non-arbitrating.
2. **Platform heterogeneity** (U133A/B microarray vs MMSEQ RNA-seq) → comparison valid only at the
   pathway-enrichment layer; no expression-matrix merge.
3. **Compartment mismatch** (PBMC vs isolated monocytes) → shared signal scoped to monocyte-inclusive
   pathways; cell-type-marker leakage is a named veto.
4. **Sex** — GSE14577 male-only; GSE130353 sex unreported → unmeasured confound, unadjustable.
5. **MMSEQ estimates ≠ counts** → continuous modelling only; count-based inference out of scope.
6. **Depositor normalization inherited** (raw CEL reprocessing deferred) → defensible because the
   estimand is a within-dataset GSEA *rank*, invariant to monotone per-sample normalization; the bound
   is that no absolute-scale/magnitude claim is in scope, and RMA re-normalization is an optional
   robustness check, not part of the primary.
7. **Specificity rests on the QFS-vs-QS *presence* contrast**, not on absence-in-QS-vs-HC (which is
   weak at n=10 and now only contributes the `exposure_sequela` label). A "shared" signature without
   concordant QFS-vs-QS signal is an exposure sequela, not evidence for `hypothesis:0001`.
8. **Overlap significance is permutation-calibrated, not Fisher** — Fisher/Jaccard over correlated
   MSigDB sets are descriptive only; the anti-conservative independence assumption is not used for the
   verdict.

## Feedback Reflection

The plan-analysis template and the expression + statistics leaves fit this cross-platform, cross-
compartment, tiny-n case well; the sensitivity-arbitration leaf was decisive for structuring the QS
group into a pre-committed specificity rule. **Revised 2026-06-20 after user code review** (six
findings): the original draft (a) used Fisher's exact over correlated MSigDB sets as the verdict test
(anti-conservative) — replaced by a sample-label permutation null on NES rank-concordance; (b) rested
specificity on absence-in-QS-vs-HC — replaced by the direct QFS-vs-QS presence contrast; (c) overstated
provenance ("downloaded/confirmed usable") when only metadata files were retrieved — added an
acquisition+hash blocking gate; (d) under-justified the deferred-CEL choice — now tied to GSEA rank
invariance; (e) left the gene-set universe unpinned — now a locked pre-reg parameter; (f) made ORA a
mandatory sensitivity that could falsely fire `fragile` — demoted to optional diagnostic. The lesson
worth carrying: at tiny n with correlated gene sets, the *calibration of the overlap null* is the
load-bearing methodological choice, and a "count of shared significant sets" framing invites an
independence assumption that does not hold.
