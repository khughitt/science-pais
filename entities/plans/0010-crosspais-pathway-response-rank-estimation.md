---
id: "plan:0010-crosspais-pathway-response-rank-estimation"
kind: "plan"
title: "Analysis plan: learn the reproducible effective rank of the cross-PAIS blood pathway-response subspace from primary data (t117, q0050 Q-C gate)"
status: "active"
created: "2026-07-07"
updated: "2026-07-07"
related:
  - "task:t117"
  - "interpretation:0037-t116-power-bias-floor-shared-axis-sim"
  - "question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design"
  - "question:0017-deflationary-alternatives-vs-shared-pathophysiology"
  - "question:0001-shared-molecular-signature-across-triggers"
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "plan:0003-cross-trigger-pathway-overlap-pipeline"
  - "pre-registration:0002-cross-trigger-pathway-overlap"
  - "dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe"
  - "dataset:gse226260-longcovid-pbmc"
  - "dataset:gse224615-longcovid-wholeblood"
  - "dataset:gse267625-longcovid-wholeblood"
  - "dataset:gse270045-longcovid-mecfs-wholeblood"
  - "dataset:gse251849-longcovid-pbmc-cognitive"
  - "dataset:scilifelab-28832492-longcovid-pbmc"
  - "dataset:gse228320-longcovid-wholeblood-pulmonary"
  - "dataset:prjna1184005-longcovid-pbmc"
  - "dataset:gse251872-pime-cfs-pbmc"
  - "dataset:gse130353-qfs-cfs-monocytes"
  - "dataset:gse143549-post-ebola-wholeblood"
  - "dataset:gse63085-post-lyme-pbmc"
  - "dataset:gse68310-post-influenza-wholeblood"
  - "dataset:prjna1001790-post-chikv-wholeblood"
  - "dataset:gse128078-mecfs-wholeblood"
  - "dataset:gse16059-mecfs-twins-pbl"
  - "dataset:gse14577-pi-cfs-pbmc-microarray"
---

# Analysis plan: learn the reproducible effective rank of the cross-PAIS blood pathway-response subspace from primary data (t117)

## Purpose

`interpretation:0037` (the t116 power/bias-floor simulation) showed that the arbitrating power of the
≥3-trigger shared-axis test for `question:0050` is governed almost entirely by **one unknown**: the
**effective rank** of the cross-PAIS pathway-response overlap. A lumpy low-rank overlap (R≈2–4) is
rejectable against the finite-repertoire null at achievable arm count K; a homogeneous high-rank overlap
is structurally indistinguishable from a single shared attractor at the arm counts such a study can
realistically field. That rank is currently an **assumption** in the q0050 GO/NO-GO. This plan converts
it to a **data estimate**, without a new cohort, from existing single-trigger blood deposits.

Crucially, this plan does **not** lift a rank scalar from the literature. Consistent with the project's
skeptical-of-literature stance (`science` introduction: "skeptical by default… literature, data, and
causal provenance should be explicit"), we **learn the cross-PAIS pathway-response signatures ourselves
from primary data**, by uniform re-computation across as many relevant public deposits as we can
assemble, and treat **cross-dataset / cross-platform / cross-condition reproducibility as the primary
believability criterion**. A rank that only appears in one study, one platform, or one leave-out
configuration is not evidence; a rank that survives leave-one-dataset-out **and** leave-one-condition-out
resampling is.

## Estimand (frozen)

> **Estimate the reproducible effective rank of the cross-trigger PAIS pathway-response subspace from
> independently derived case-vs-control pathway-effect vectors, after uniform DE/enrichment over a pinned
> high-resolution gene-set universe, with dataset/platform leave-one-out stability as the primary
> believability criterion.**

The analysis object is a **pathway × contrast** matrix: one column per case-vs-control **contrast**
(the unit), each column a vector of pathway-effect scores (NES-like) computed by **one** harmonized
DE→enrichment pipeline over **one** pinned gene-set universe
(`dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe`, ~1000-set high-resolution scale per the t116
finding that this is what drops the required arm count to K≈3). The deliverable is an estimate of the
**effective rank R** of the shared column subspace, with uncertainty, mapped onto the t116 R-regime grid.

## What this plan is and is not

- It **is** a data-analysis plan: it consumes real public deposits and produces an empirical rank
  estimate + uncertainty + a t116-grid placement. (Contrast `plan:0003`, which is a pipeline-orchestration
  design for a *frozen* pre-registered verdict, and the t116 sim, which consumes no external data.)
- It is **not** the q0050 study, nor a mechanism claim. R is a **design parameter estimate**; it tells us
  whether the harmonized ≥3-trigger design can arbitrate at achievable arm counts, not whether a shared
  attractor exists.
- It does **not** re-decide the h0001/q0017 verdict machinery of `pre-registration:0002`. It reuses that
  machinery's DE→enrichment stages (limma→fgsea, the pinned universe, the QA-checkpoint discipline) as the
  uniform effect-vector computer, then adds a **rank-estimation** layer those plans do not have.

## Readiness decision

**Design: active. Execution: BLOCKED on WP1.** Every corpus deposit is a `candidate` with
`access.verified: false` and `[UNVERIFIED]` design specifics; **no rank estimation (Stage 2 onward) runs
until the WP1 verification + staging gate passes** — i.e. each admitted deposit's per-subject documented
onset, sampling window (≥4 wk floor), tissue/platform, per-sample-matrix downloadability (or pinned raw-read
quantification), and case-vs-control explanatory power are confirmed from the record, and the floor-/SRA-
provisional deposits are explicitly promoted or demoted. This plan is therefore **analysis-ready-to-verify,
not execution-ready**; WP1 is the readiness checkpoint and its exit is the point at which the strict trigger
count is finalized. (`status: active` reflects the *design*; the execution gate is this section.)

## Two-matrix design + verdict rule (locked)

Post-infectious attribution varies in certainty across the corpus. To keep the primary estimand clean
while still using the informative-but-looser ME/CFS evidence, the analysis runs on **two nested
matrices**, and the primary verdict is the one that survives both.

1. **Primary strict matrix** — contrasts with **per-subject documented infectious onset** only
   (`onset_certainty: documented`). This is the clean estimand: shared pathway-response rank across
   *identifiable* post-acute triggers. **The q0050-grade R estimate comes from this matrix.**
2. **Expanded ME/CFS sensitivity matrix** — the strict matrix **plus** probable-post-infectious ME/CFS
   blood-bulk deposits carrying an explicit `onset_certainty ∈ {cohort-level, unknown-per-subject}` flag.

**Verdict rule.**
- A **low-rank** conclusion (the decision-relevant, q0050-arbitrable outcome) is **stronger if it survives
  both matrices**.
- If low-rank appears **only after** adding the probable-PI ME/CFS deposits, it is **hypothesis-generating,
  not q0050-grade evidence** — reported as such, never promoted to the design GO/NO-GO.
- The sensitivity matrix additionally answers a **different but adjacent question**, reported separately:
  > *Does the learned PAIS blood-response subspace also capture clinically diagnosed ME/CFS that lacks
  > per-subject documented infectious onset?*

## Admissibility rubric (locked; tiering, not hard exclusion)

| Gate | Rule | Severity |
|---|---|---|
| G1 Compartment | **Primary matrix is blood-bulk only** (whole blood / PBMC / sorted leukocytes). Muscle / other tissue → separate triangulation, never pooled into the rank matrix. | hard for primary |
| G2 Exposure | Human; single documented trigger (strict matrix) or flagged probable-PI (sensitivity matrix); post-acute **persistent** sampling (≥12 wk target, **≥4 wk floor — HARD for the strict-primary matrix**). Deposits sampled *inside* the floor (early-convalescent) are **provisional/exploratory**, excluded from the strict trigger/K count, until WP1 verifies later post-acute *symptomatic* samples; otherwise they route to the early-convalescent decoy/specificity layer. | hard floor for primary |
| G3 Contrast | Case-vs-control at the sample level. **Recovered/full-recovery controls are SCORED heavily, not required.** | tiering (scored) |
| G4 Downloadable | A per-sample expression matrix is **public and downloadable**, **or** public raw reads are sufficient to compute one under a **pinned quantification path** (WP1). SRA-only deposits enter the primary matrix **only once that quantification is implemented and verified in WP1** (provisional until then). **Author-request-only and gated/enclave data are analysis-ineligible** (note-only; see `fb-2026-07-07-003`). | hard |
| G5 Metadata floor | Hard floor: case/control labels, trigger + case definition, sampling window, sample-level matrix, platform, tissue. Scored: age, sex, timing, severity, batch, meds, comorbidity. | mixed |
| G6 Interpretability | Single-platform rare-trigger contrasts are **included but flagged non-arbitrating for platform-independent biology**; the rank conclusion **must survive dropping them** (leave-one-out). | corpus-level |

## Artifact controls are first-class admissibility (not cleanup)

The t116 pipeline review established the **rival hypothesis** for any low-rank signal: a **correlated
(shared) batch/platform artifact** — a common axis present on every contrast because they share a
protocol/platform/normalization — mimics a genuine shared attractor and, at signal strength, drives the
false-"low-rank/attractor" rate to ~0.9 while collapsing off-diagonal concordance SD. Therefore the
following are **admissibility criteria for the R estimate**, evaluated before any biological reading:

- **Platform leave-one-out** — re-estimate R dropping each platform in turn (RNA-seq vs microarray;
  whole-blood vs PBMC vs sorted). A rank that collapses when a platform is removed is a platform axis, not
  biology.
- **Negative-control feature sets** — housekeeping / platform-associated / GC-content-confounded gene sets
  carried through the identical pipeline; shared structure among these is the artifact floor to subtract.
- **Recovered-control specificity** (directional, not magnitude) — where recovered/full-recovery-control
  contrasts exist (scored under G3), the non-recovery shared subspace must remain **detectably present in
  case-vs-recovered** contrasts and **not be fully explained by** the recovered-vs-healthy (infection-history)
  axis or an acute-decoy axis. We do **not** require case-vs-recovered to *exceed* case-vs-naive in
  magnitude — a healthy-control contrast can legitimately be larger because it also carries infection-history
  and non-recovery differences; the test is **subspace persistence/specificity**, not effect size.
- **Off-diagonal concordance SD** — reported alongside R as the t116 structural discriminator; a low SD
  with high mean concordance is the shared-artifact signature the review flagged.

## Triangulation layers (separate matrices, never pooled)

Bulk transcriptome is **the rank layer**. Other modalities are **separate triangulation matrices**,
computed and rank-estimated in parallel and compared for *consistency of R*, but never concatenated into
the primary matrix (different noise/coverage structure):

- scRNA **pseudobulk** (long-COVID ×N, WNV/sepsis/influenza) → its own pathway × contrast matrix.
- Proteomics / metabolomics deposits → their own matrices.
- PI-ME/CFS muscle, LC tissue → tissue triangulation.
- **Acute-infection decoys** (dengue, acute CHIKV/Zika, acute sepsis, acute COVID, Q-fever infection) →
  the **specificity layer**: the post-acute subspace should *not* be recovered by an acute-only decoy at
  the same rank.

## Corpus (registered candidates)

All strict-primary and sensitivity deposits below are registered as `dataset:` candidate entities
(`tier: evaluate-next` / `track`, `access.verified: false` pending WP1). Design specifics in those
entities are `[UNVERIFIED]` — WP1 verifies them from the record.

**Strict-primary matrix — public, blood-bulk, documented trigger, above the ≥4 wk post-acute floor (~13 contrasts, 5 triggers):**
- Long COVID (8): `gse226260-longcovid-pbmc`, `gse224615-longcovid-wholeblood`,
  `gse267625-longcovid-wholeblood`, `gse270045-longcovid-mecfs-wholeblood`,
  `scilifelab-28832492-longcovid-pbmc`, `gse251849-longcovid-pbmc-cognitive` — plus two LOO-conditional:
  `gse228320-longcovid-wholeblood-pulmonary` (pulmonary-phenotype-selected),
  `prjna1184005-longcovid-pbmc` (n≈7).
- PI-ME/CFS (1): `gse251872-pime-cfs-pbmc` (adjudicated).
- Q-fever/QFS (1): `gse130353-qfs-cfs-monocytes` *(catalogued)*.
- Post-Ebola (1): `gse143549-post-ebola-wholeblood`.
- Post-Lyme (1): `gse63085-post-lyme-pbmc` *(conditional — not PTLDS-symptom-selected; post-treatment window is above the floor)*.

**Provisional — floor-gated, NOT counted in the strict trigger/K total (promotable only if WP1 finds later post-acute *symptomatic* samples):**
- Post-influenza: `gse68310-post-influenza-wholeblood` (~3 wk convalescent window — *inside* the ≥4 wk floor; microarray). Absent later samples → routes to the early-convalescent **decoy/specificity** layer, not a primary arm.
- Post-CHIKV: `prjna1001790-post-chikv-wholeblood` (sampled ~day 21 — *inside* the floor; SRA-only). Absent later samples → routes to the early-convalescent **decoy/specificity** layer.

Counting an early-convalescent sample as post-acute would leak acute biology into the rank; hence their exclusion from the strict count (they also cost trigger diversity — influenza and CHIKV are the two triggers this removes from the primary matrix). Their entities keep `matrix: strict-primary` only as a *target* pending the WP1 timepoint check; the plan treats them as provisional here.

**ME/CFS sensitivity additions (undocumented/cohort-level onset):**
`gse128078-mecfs-wholeblood`, `gse16059-mecfs-twins-pbl`, `gse14577-pi-cfs-pbmc-microarray`
*(catalogued; cohort-level post-viral, male-only)*.

**Flagged inaccessible (note-only, never sourced):** Dubbo/DIOS (EBV+RRV+QFS, recovered controls — the
highest-value deposit, author-request), PTLDS dbGaP phs002795 (gated), SARS-1 (Zhao et al., request-only),
CHIKGene Réunion (no resolvable public accession as of 2026-07-07), Raijmakers QFS multi-omics (request).

**Corpus honesty note.** The strict matrix is long-COVID-dominated (~8 of ~13 columns) and, after the
floor exclusions, spans only **5 triggers**. Therefore **leave-one-condition-out is a primary readout, not
merely a robustness check** — with the LC-out fold as the decisive stress test (operationalized in
Stage 3b) — and the rank must not be an artifact of long-COVID over-representation. R is resolvable in the
**decision-relevant low range (≈2–4)**;
the corpus cannot cleanly resolve R≥8 (which is exactly the t116 "non-arbitrating" regime — a NO-GO
signal for q0050, not a failure of this analysis).

## Method

### Stage 1 — Corpus staging (reproducible, checksummed)
Stage each admitted deposit through a **pinned + checksummed Snakemake acquisition rule** (per project
convention; ad-hoc network is sandbox-blocked and non-reproducible). SRA-only deposits
(`prjna*`) require a **pinned raw-read quantification path** (salmon + a pinned transcriptome/index,
recorded as a platform axis for the artifact battery) and are **provisional until that path is verified in
WP1** (G4); FigShare/SciLifeLab deposits use a non-GEO staging path. Data payloads land under the
gitignored off-Dropbox `data/` symlink.

### Stage 2 — Uniform effect-vector computation (reuse plan:0003 machinery)
One harmonized DE→enrichment per contrast: **limma** moderated-t ranked gene list → **fgsea** NES over the
**single pinned universe** `dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe`. Same gene-id
harmonization (Ensembl canonical), same size filter, same seed discipline, same two-severity QA
checkpoints as `plan:0003`. Output: the **pathway × contrast** matrix (columns = contrasts, hierarchically
groupable by condition/trigger/platform). **Expression is never merged across datasets** — deposits meet
only at the NES level.

### Stage 3 — Rank estimation (rotation-invariant primary)
Estimate the effective rank of the shared column subspace with a **battery of rotation-invariant
estimators**, primary because R must not depend on a factor rotation:
- **Parallel analysis (Horn)** against a label-permuted null that preserves per-contrast marginals.
- **Cross-validated / bi-cross-validation SVD** (hold out sub-blocks of the matrix; rank = minimiser of
  held-out reconstruction error).
- **Split-half** subspace stability (principal-angle agreement between random half-corpus SVDs).
- **Resampling stability** — the believability core — with **hierarchical/blocked** resampling
  (unit = contrast; blocks = condition, then platform): **leave-one-dataset-out** AND
  **leave-one-condition-out** are reported **separately** (they are different perturbations given the
  long-COVID dominance), plus a naive-bootstrap comparator only as a lower-bound sanity check.

### Stage 3b — LODO/LOCO operationalization (pre-locked pass/fail)
Resampling stability is evidence only if its decision rule is fixed **before** seeing the folds. For every
leave-one-dataset-out (LODO) and leave-one-condition-out (LOCO) fold:

1. **Fold admissibility (structural gate).** A fold is *informative* only if the remaining matrix retains
   **≥3 distinct triggers, ≥6 contrasts, and ≥2 platforms** — the t116 K≥3 shared-axis requirement below
   which a rank is simply **not identifiable**. A fold failing any threshold is reported as
   **non-identifiable / uninformative** and is **excluded from pass/fail** — never scored as either — with
   the exclusion stated explicitly (no silent drop).
2. **Pass/fail on admissible folds.** **PASS** iff the artifact-adjusted R point estimate stays within
   **±1 of the full-corpus R AND within the same t116 regime band** (low ≈2–4 vs high ≥8) **and** the
   leading shared subspace is stable (principal angle between full-corpus and fold subspaces below a
   config'd cutoff). **FAIL** iff an admissible fold moves R across the t116 regime boundary.
3. **The long-COVID-out (LC-out) fold is a first-class, separately reported result** — not one fold among
   many — because LC supplies ~8 of ~13 columns. If LC-out is admissible **and** passes, the low-rank
   conclusion is **robust**. If LC-out is **inadmissible** (too few remaining contrasts/triggers) **or**
   **underpowered** (the parallel-analysis null band overlaps the observed leading eigenvalue), the
   low-rank conclusion is labelled **conditional on long-COVID inclusion → hypothesis-generating, not
   q0050-grade** — the same demotion the two-matrix rule applies to sensitivity-only findings.
4. **Rare-trigger-out folds** (Ebola-out, Lyme-out, QFS-out, PI-ME/CFS-out) retain all of LC and are
   typically admissible; a robust low-rank claim must **PASS every admissible rare-trigger-out fold**.

Every threshold (`min_triggers=3`, `min_contrasts=6`, `min_platforms=2`, R-band `±1`, subspace-angle
cutoff, parallel-analysis power rule) lives in `config.yaml` and is committed before any fold is scored.

### Stage 4 — Sparse latent instrument (replication-gated, secondary)
The primary R stays rotation-invariant. A **sparse Bayesian factor model** (BicMix/SFAmix family;
ARD / spike-and-slab) is added as a **scoped, replication-gated** cross-check, never the primary readout,
for three specific jobs:
- shrinkage-based **active-factor-count** cross-check of R;
- **sparse contrast-loadings** to distinguish an **attractor** factor (dense across triggers) from
  **trigger/platform-specific** factors;
- **sparse feature-loadings** for artifact attribution (which sets carry a shared axis).
Deep disentanglement (sparse VAEs) is **deferred** — n≈15–40 contrasts cannot support it.

### Stage 5 — Artifact adjudication + t116-grid placement
Run the Stage-"artifact controls" battery (platform-LOO, negative-control sets, recovered-control
specificity, off-diagonal SD). **Separate biology-shared from artifact-shared** before reading R. Then map
the surviving R + uncertainty onto the **t116 R-regime grid** (`interpretation:0037`): does the estimate
land in the arbitrable low-rank regime (q0050 GO with the t116 conditions), the non-arbitrating high-rank
regime (q0050 NO-GO / redesign), or straddle?

## Key decisions

### Key decision 1 — believability = cross-substrate reproducibility, not within-study p
R is accepted only to the extent it is **stable under leave-one-dataset-out and leave-one-condition-out**.
Within-one-study fit is not evidence. This is the whole reason for learning from many deposits rather than
citing a literature scalar.

### Key decision 2 — unit is the contrast; condition is a grouping, not the unit
The matrix is pathway × **contrast**; conditions/triggers are a **hierarchical grouping over columns**.
Leave-one-dataset-out ≠ leave-one-condition-out; resampling is **blocked/hierarchical**, not naive.
Longitudinal deposits (`gse267625`) and paired designs (`gse16059` twins) get an explicit
one-contrast-per-unit policy defined in Stage 2.

### Key decision 3 — bulk transcriptome is the rank layer; other omics are triangulation
scRNA-pseudobulk, proteomics, metabolomics, and tissue are **separate matrices** compared for consistency
of R, **never pooled** into the primary rank matrix.

### Key decision 4 — artifact controls gate the estimate
Platform-LOO, negative-control sets, recovered-control specificity, and off-diagonal concordance SD are
**admissibility criteria**, run before biological interpretation. The shared-artifact alternative is the
named rival for any low-rank finding.

### Key decision 5 — "non-arbitrating" is scoped to the achievable test family, not literally "any N"
The t116 high-rank regime is **non-arbitrating at achievable arm counts under this pathway-vector
structural-test family** — *not* literally at any N. This plan adopts that scoped wording. **Downstream
correction owed:** `interpretation:0037` and `question:0050` currently say "at ANY N"; this must be softened
to the scoped phrasing when those entities are next edited (tracked in Open Questions).

## Work packages

### WP0 — Workflow skeleton, corpus link-through, config
- Reuse the `plan:0003` Snakemake `envs/` (limma+fgsea+annotation Bioconductor stack) and
  `qa_checkpoint.py`; scaffold `code/workflows/t117-crosspais-rank/` with a single `config.yaml`
  (pinned universe hash, seed, estimator params, LOO/blocking spec, artifact-control set list).
- Reciprocally link every admitted `dataset:` to this plan (`science dataset link … consumed_by
  plan:0010-…`) so Dimension-3 review resolves.
- **DoD:** `snakemake -n` resolves; envs solve; every corpus dataset carries a `consumed_by` backlink.

### WP1 — Corpus verification + staging (the "verify details / explanatory power" pass) — **readiness gate**
- For each registered candidate: verify from the record the `[UNVERIFIED]` specifics (N, tissue, platform,
  window, per-sample matrix format, control type), confirm G4 downloadability, and **verify explanatory
  power for the variable of interest** (does a case-vs-control contrast even exist and separate?). Update
  the dataset entity: set `access.verified: true` + `last_reviewed`, or **demote** on failure.
- **Resolve every provisional deposit explicitly** (no default-in): for the **floor-gated** deposits
  (`gse68310`, `prjna1001790`) confirm whether later post-acute *symptomatic* samples exist → **promote**
  into the strict count, else **demote** to the early-convalescent decoy/specificity layer; for **SRA-only**
  deposits verify the pinned quantification path produces a per-sample matrix → promote, else hold.
  **Finalize the strict trigger/K count here.**
- Stage via checksummed acquisition rules (pinned SRA quantification where needed).
- **DoD:** each admitted deposit has a verified entity + staged matrix + datapackage; every provisional
  deposit is promoted or demoted with the decision recorded; the finalized strict trigger/contrast/platform
  counts are written (so Stage 3b admissibility thresholds can be checked against a real corpus). **No
  downstream WP runs until this gate closes.**

### WP2 — Uniform DE→enrichment → pathway × contrast matrix
- Run Stage-2 machinery over all admitted contrasts on the pinned universe; emit the matrix + per-contrast
  QA. Longitudinal/paired one-contrast-per-unit policy applied.
- **DoD:** a single reproducible pathway × contrast matrix (+ condition/platform grouping metadata),
  QA-gated, for both strict and sensitivity matrices.

### WP3 — Rank estimation battery + stability
- Parallel analysis, CV/bi-cross-val SVD, split-half, LODO + LOCO on both matrices; report R + uncertainty
  and the full stability profile.
- **DoD:** R point estimate + interval per matrix, with LODO/LOCO curves and off-diagonal SD.

### WP4 — Artifact adjudication
- Platform-LOO, negative-control sets, recovered-control specificity; subtract the artifact floor;
  re-report R.
- **DoD:** artifact-adjusted R; explicit statement of how much of the shared structure survives.

### WP5 — Sparse-FA instrument (replication-gated)
- Fit BicMix/SFAmix; cross-check active-factor count; classify attractor vs trigger/platform-specific
  factors; sparse feature-loadings for artifact attribution. Report only where it replicates the Stage-3
  R within tolerance.
- **DoD:** a secondary factor-count + attractor/specific decomposition, flagged secondary.

### WP6 — t116-grid placement + interpretation + doc corrections
- Map R + uncertainty onto the t116 R-regime grid; state the q0050 GO/NO-GO consequence and the verdict
  under both matrices per the two-matrix rule. Write the interpretation entity; carry the scoped
  "achievable arm counts" wording into `interpretation:0037` and `question:0050`.
- **DoD:** an `interpretation:` deliverable answering t117 + the q0050 consequence; the two "any N"
  corrections landed.

## Non-Goals

- Confirming or refuting a shared attractor (h0001) — R is a **design parameter**, not the verdict.
- Any absolute-magnitude / fold-scale claim — rank/subspace geometry only.
- Pooling expression across datasets, or pooling omics layers into one matrix.
- Relying on author-request-only or gated data (analysis-ineligible; note-only).
- Running the q0050 cohort or the ≥3-trigger harmonized test.

## Acceptance Criteria

- [ ] Every corpus input resolves to a `dataset:` entity with `consumed_by: plan:0010-…`; strict vs
      sensitivity membership and `onset_certainty` recorded per deposit.
- [ ] WP1 verification pass has set `access.verified` per deposit (or demoted it), replacing the
      `[UNVERIFIED]` specifics with confirmed values; **every floor-/SRA-provisional deposit is promoted or
      demoted** and the strict trigger/contrast/platform count is finalized before any Stage-2+ run.
- [ ] LODO/LOCO carry **pre-locked pass/fail semantics** (Stage 3b): a fold admissibility gate
      (≥3 triggers, ≥6 contrasts, ≥2 platforms) with non-identifiable folds reported and excluded from
      pass/fail, a fixed R-band + regime + subspace-angle PASS rule, and the **LC-out fold reported
      first-class** — a low-rank result that fails/cannot-power LC-out is demoted to hypothesis-generating.
- [ ] One reproducible, QA-gated pathway × contrast matrix per matrix (strict, sensitivity), computed by a
      single harmonized DE→enrichment over the pinned `msigdb-2024-1-hs-mapped-pais-gene-set-universe`.
- [ ] R is reported with uncertainty from **≥3 rotation-invariant estimators**, and its **leave-one-dataset-out
      and leave-one-condition-out** stability profiles are reported **separately**.
- [ ] The artifact-control battery (platform-LOO, negative-control sets, recovered-control specificity,
      off-diagonal SD) is reported, and the artifact-adjusted R is stated.
- [ ] The two-matrix verdict rule is applied: the q0050-grade R comes from the strict matrix; any
      sensitivity-only low-rank result is labelled hypothesis-generating; the adjacent ME/CFS question is
      answered separately.
- [ ] R + uncertainty are placed on the t116 R-regime grid with the explicit q0050 GO/NO-GO consequence.
- [ ] The scoped "non-arbitrating at achievable arm counts under this test family" wording is carried into
      `interpretation:0037` and `question:0050` (replacing "at ANY N").

## Open questions

1. **SRA quantification pin.** `prjna1184005`, `prjna1001790` need a raw-read → gene-count path; pin the
   quantifier + reference so their NES vectors are comparable to the GEO-matrix deposits. *Lean: salmon +
   pinned transcriptome, documented as a platform axis for the artifact battery.*
2. **Microarray deposits in a mostly-RNA-seq matrix** (`gse68310`, `gse16059`, `gse14577`) — platform is a
   known shared-axis risk; these are LOO-conditional and feed the platform-LOO control directly.
3. **Longitudinal/paired contrast policy** (`gse267625`, `gse16059`) — define the single representative
   contrast per subject/timepoint in WP2 to avoid pseudo-replication inflating apparent rank.

## Notes on reusable infrastructure

The rank-estimation battery (parallel analysis + CV-SVD + split-half + blocked LODO/LOCO over a
pathway × contrast matrix) and the artifact-control battery are **`reusable: true`** — liftable to any
cross-condition pathway-overlap rank question in `health-immunity` / `pan-disease`, and a candidate for
commons promotion once stabilized. Stage-2 reuses `plan:0003`'s limma→fgsea + `qa_checkpoint.py` verbatim.
