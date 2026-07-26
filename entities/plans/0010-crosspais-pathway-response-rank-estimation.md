---
id: "plan:0010-crosspais-pathway-response-rank-estimation"
kind: "plan"
title: "Analysis plan: learn the reproducible effective rank of the cross-PAIS blood pathway-response subspace from primary data (t117, q0050 Q-C gate)"
status: "active"
created: "2026-07-07"
updated: "2026-07-08"
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
  - "dataset:msigdb-2024-1-hs-hallmark-reactome-rank-universe"
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

> **✅ t117 COMPLETE (2026-07-09) — deliverable `interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed`.**
> WP0–WP4b + WP6 are DONE; all acceptance criteria are met; WP5 (sparse-FA) is left unbuilt as moot (its
> replication gate cannot pass under the fail-closed finding — see WP5). **Outcome (fail-closed):** the public
> single-trigger PAIS corpus does **not** identify a cross-trigger pathway-response rank at its operating point
> (off-diagonal concordance −0.064 ≤ sampling floor 0.033; Stage-3c calibration `pass=false`), so **no R is
> placed on the t116 grid**. Descriptive R (strict 2 / sensitivity 3) is reported non-grid; the GWS/FM
> read-across is `partially_recovered_indeterminate`; artifact controls fail (`limited_or_nonarbitrating`).
> This is the empirical answer to `interpretation:0037`'s Q-C and reinforces the `question:0050` go/no-go: the
> public route cannot settle the R regime — only a purpose-built K≥3 harmonized cohort can. Status kept
> `active` (the project reserves `archived` for shelved/abandoned plans; this one delivered).

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

**Design: active. WP1 record-verification: COMPLETE (2026-07-08). Execution (Stage 2+): gated on the
WP0 workflow build + data staging — AND bounded by the corpus-readiness ceiling below.** The WP1
verification pass (record-checks against GEO/SRA/FigShare) is done: it corrected specifics, demoted two
deposits (`gse224615` G4, `gse68310` floor), deferred one (`prjna1184005` G4), demoted both floor-gated
provisionals (`gse68310`, `prjna1001790` — removing influenza and chikungunya as strict triggers), and
finalized the strict matrix at **~10 contrasts / 5 triggers** *(WP1 admissibility tally; the runtime-built
strict matrix is **7 columns / 3 triggers** — SARS-CoV-2, PI-ME/CFS, Lyme — after further deposits failed
staging/QA)* (see *Corpus* + *WP1 corpus-readiness finding*). What remains before a verdict: **staging** the matrix-ready deposits (download + checksum +
datapackage via the WP0 workflow), then Stages 2–6. **The provisional scientific result of WP1 is the LC-out
low-power ceiling**: the strict matrix appears unable to produce a q0050-grade (LC-out-surviving) rank, so the
downstream run is scoped to a *descriptive/hypothesis-grade* R + the artifact adjudication + the adjacent
ME/CFS question — not a q0050 GO/NO-GO. **This ceiling is calibration-contingent, not yet binding** (review
Finding A): its current strength rests on the Stage-3b `min_contrasts=6` gate, which is hand-set, not
`interpretation:0037`-grounded; under a t116-faithful gate (K≥3 triggers) LC-out is *admissible but
underpowered* (4 single-trigger columns, wide CI), not *non-identifiable*. WP3 must convert the binary
"non-identifiable" verdict into a **threshold/power sensitivity curve** before the ceiling is cited as
settled (see Stage 3b + WP1 corpus-readiness finding, both re-grounded 2026-07-08). (`status: active` reflects
the *design*; this section is the execution gate and the honest — now explicitly provisional — ceiling on
what the run can claim.)

**Post-review amendments (2026-07-08).** This plan was critically reviewed
(`doc/reviews/0010-crosspais-pathway-response-rank-estimation-pipeline-review.md`, overall WARN). Four
findings are folded in below: **A** (re-ground the LC-out gate in t116's K≥3, report a power curve not a
binary verdict — Readiness decision, Stage 3b, WP1 corpus-readiness finding); **B** (the SVD rank estimator
is *not* the statistic t116 characterized — add a t116-generative calibration of the battery, and adopt
t116's structural single-axis statistic as a confirmatory co-primary, before any grid mapping — Stage 3/3c/5,
WP3); **C** (the strict matrix mixes blood compartments — make WB/PBMC-only the primary matrix, add
compartment-stratified + drop-sorted + composition-adjusted R — G1, artifact controls, Stage 4/5, WP4); **D**
(add the project's designated non-infectious GWS/FM read-across as a separate, identically-gated specificity
matrix — triangulation layers, WP4b). These are conceptual/scope hardening, not a change to the frozen
estimand.

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
| G1 Compartment | **Primary matrix is whole-blood / PBMC bulk only** (review Finding C). **Sorted-leukocyte deposits (e.g. sorted-monocyte QFS `gse130353`) are a *separate compartment stratum*, not pooled into the primary rank matrix** — a shared cross-trigger axis across mixed compartments can be a cell-composition shift, not pathway biology, and cannot be composition-adjusted the same way. Muscle / other tissue → separate triangulation. | hard for primary |
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
- **Compartment / cell-composition control** (review Finding C — a *biological* rival the platform/negative-set
  controls do **not** catch, because composition shift is real regulation). Three prongs, because deconvolution
  alone is insufficient across a mixed-compartment corpus: (i) **compartment-stratified R** — estimate R within
  each compartment stratum (WB, PBMC, sorted) and compare, since NES is not directly comparable across
  compartments; (ii) **drop-sorted-compartment sensitivity** — the low-rank conclusion must survive removing the
  sorted stratum (and WB/PBMC-only is the *primary* matrix per G1); (iii) where deconvolution is valid (WB, and
  partially PBMC — **not** sorted monocytes), estimate leukocyte fractions and report R **before and after
  composition adjustment**, with the composition axis carried as a named nuisance/negative-control dimension. A
  shared axis that dissolves under composition adjustment, or that appears *only* when compartments are pooled,
  is a blood-count/compartment signature, not an attractor.
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
- **Non-infectious read-across (GWS/FM)** — the project's designated infection-specificity stress-test
  (review Finding D; `entities/specs/0001-scope-boundaries-for-health-post-acute-infection.md` D-003 names Gulf War Syndrome / fibromyalgia as "the single
  best external test of the attractor's trigger-agnostic claim", with PACVS as a further read-across). Built
  as a **separate non-infectious specificity matrix**, held to the **same admissibility gates** as the primary
  corpus (blood-bulk WB/PBMC, public, downloadable, sample-level case-vs-control) and computed through the
  **same uniform DE→enrichment over the same pinned universe**, then compared to the PAIS subspace as a
  distinct object — **not** a free-form column appended to the primary matrix (which would relax the very
  compartment/platform discipline enforced elsewhere). This is the direct lever on the t116 Q-D identifiability
  ceiling (infection-specific attractor vs generic-sickness manifold): if the learned PAIS blood subspace is
  **equally recovered by non-infectious GWS/FM**, that is strong evidence for a generic fatigue/sickness
  manifold, not an infection-specific attractor. See WP4b.

## Corpus (WP1-verified 2026-07-08)

WP1 verified every registered deposit against its public GEO/SRA/FigShare record (5 parallel record-checks;
per-deposit findings live in each `dataset:` entity). The result below is the **finalized, record-checked**
corpus — not the discovery-sweep guess. Two deposits demoted, one deferred, both floor-gated provisionals
demoted; several `[UNVERIFIED]` specifics corrected.

**Strict-primary matrix — WP1-verified, blood-bulk, downloadable per-sample matrix, ≥4 wk floor, documented trigger.** WP1 finalized ~10 contrasts / 5 documented triggers; the post-review G1 amendment (Finding C) then moved sorted-monocyte QFS to a **separate compartment stratum**, so the **WB/PBMC primary matrix is 4 triggers** (LC, PI-ME/CFS, Ebola, Lyme), with QFS entering compartment-stratified R only:
- Long COVID (6 matrix-ready): `gse226260-longcovid-pbmc` (**CORRECTED at WP1b-a-rest — the "≈46 LC vs rich convalescent+healthy controls, 2-platform batch, strongest" catalogue was wrong**: the expr matrix is SINGLE-platform and mixes the PASC cohort with a disjoint 142-sample acute-severity cohort; staged as PASC vs NOPASC = **28 vs 8 subjects** [72 vs 14 samples] with an infected-nonPASC-convalescent, SMALL control arm — see WP2 + config), `gse270045-longcovid-mecfs-wholeblood` (19 LC+ME/CFS vs 17 healthy — **clean**), `scilifelab-28832492-longcovid-pbmc` (60 vs 50, controls are **infected-recovered** — scores well on G3; FigShare-API matrix), `gse251849-longcovid-pbmc-cognitive` (11 vs 12, small — subgroup n 5–7), plus two **heavy-caveat keeps**: `gse267625-longcovid-wholeblood` (matrix public but **no external control** — contrast must be built *within-cohort* in WP2; longitudinal), `gse228320-longcovid-wholeblood-pulmonary` (matrix public but the contrast is a **DLCO pulmonary-severity axis within ARDS survivors**, not fatigue-dominant LC — LOO-drop).
- PI-ME/CFS (1): `gse251872-pime-cfs-pbmc` — **corrected to 12 cases vs 15 healthy** (the "17 vs 21" was total enrollment); bulk PBMC; 2 sequencing platforms → batch covariate.
- Q-fever/QFS (1) — **compartment stratum, not primary** (post-review G1, Finding C): `gse130353-qfs-cfs-monocytes` *(previously verified/staged; **sorted monocytes** — held as a separate compartment stratum, no longer pooled into the WB/PBMC primary rank matrix; enters compartment-stratified R only).*
- Post-Ebola (1): `gse143549-post-ebola-wholeblood` — 26 survivors vs 33, ~23 mo, downloadable CPM matrix.
- Post-Lyme (1): `gse63085-post-lyme-pbmc` — clears the floor via the **V5 6-month** post-treatment arm; not PTLDS-symptom-selected (unselected timecourse).

**Demoted / deferred by WP1 (out of the primary matrix):**
- `gse224615-longcovid-wholeblood` — **demoted (G4)**: no downloadable per-sample matrix (DEG summary only), RNA-seq control arm only n≈9. DEG-level triangulation at most.
- `prjna1184005-longcovid-pbmc` — **deferred (G4)**: SRA raw-reads only, 14 samples, split/window unverifiable → needs the pinned quantification path first.
- `gse68310-post-influenza-wholeblood` — **demoted**: no ≥4-wk persistently-symptomatic sample (latest within-illness = day 21, expression back to baseline by then). **Removes influenza as a strict trigger**; usable only as an acute-decoy.
- `prjna1001790-post-chikv-wholeblood` — **demoted**: sequenced post-acute = day-21 (~3 wk, below floor), no day-90 transcriptome, chronic-vs-recovered contrast, raw-FASTQ-only. **Removes chikungunya as a strict trigger**; candidate for an adjacent chronification-predictor triangulation.

**ME/CFS sensitivity additions (WP1-verified):**
`gse128078-mecfs-wholeblood` (14 vs 11, whole blood, FPKM matrix; multi-timepoint → WP2 collapse),
`gse16059-mecfs-twins-pbl` (**44 discordant MZ twin pairs**, PBL microarray; WP2 must model within-pair
correlation), `gse14577-pi-cfs-pbmc-microarray` *(previously verified; cohort-level post-viral, male-only)*.
All `onset_certainty: unknown-per-subject`.

**Flagged inaccessible (note-only, never sourced):** Dubbo/DIOS (EBV+RRV+QFS, recovered controls — the
highest-value deposit, author-request), PTLDS dbGaP phs002795 (gated), SARS-1 (Zhao et al., request-only),
CHIKGene Réunion (no resolvable public accession), Raijmakers QFS multi-omics (request).

## WP1 corpus-readiness finding (2026-07-08) — decision-relevant

The finalized strict matrix is **~10 contrasts across 5 documented triggers, ~8 of them long COVID**, and
**each non-LC trigger (PI-ME/CFS, QFS, Ebola, Lyme) contributes a single contrast** with no within-trigger
replication. **The post-review G1 amendment (Finding C) moves sorted-monocyte QFS to a separate compartment
stratum**, so the **WB/PBMC primary matrix carries 4 triggers** (LC, PI-ME/CFS, Ebola, Lyme). Removing long
COVID from the WB/PBMC primary therefore leaves **~3 contrasts across 3 triggers** (PI-ME/CFS, Ebola, Lyme).

**Provisional, calibration-contingent — not a settled non-identifiability verdict (review Finding A).** The
LC-out fold retains **3 triggers ≥ 3** — so under the re-grounded (t116-faithful) admissibility gate it is
**still admissible, but now at the K=3 identifiability floor and even lower-power** (3 single-trigger columns),
*not* "non-identifiable." (The QFS→stratum move under Finding C tightens, rather than breaks, the low-power
story: it removes a fourth column from the LC-out fold, so the case that the WB/PBMC primary cannot *robustly*
pin the rank once LC is removed is strengthened — but it remains a power/CI claim to be **shown** in WP3, not a
structural impossibility.) The earlier "< ≥6-contrast floor → NON-IDENTIFIABLE"
headline rested on the hand-set `min_contrasts=6` gate, which is **not `interpretation:0037`-grounded** (t116
grounds arm count K≥3, not a contrast count) — so that binary verdict is **withdrawn** pending the Stage-3c
calibration + the WP3 LC-out **power/CI curve**. The defensible statement today is weaker: *LC-out estimates a
cross-PAIS rank from 4 single-trigger columns with no within-trigger replication — low-power, wide-CI, likely
unable to robustly pin the rank once LC is removed, but this must be **shown** by the power curve, not asserted
from a contrast floor.* The two provisional deposits that could have restored trigger diversity (influenza,
CHIKV) **both demoted** on the floor, so **there is no public rescue of the contrast count** — but note that,
because the gate is triggers not contrasts, this does not by itself change the K=4 admissibility.

**Consequence for q0050 (qualitative, likely to survive calibration).** Even re-grounded, the qualitative
conclusion is expected to hold: **existing public single-trigger blood-bulk transcriptomes are unlikely to
deliver a q0050-grade, LC-out-surviving cross-PAIS rank estimate** — but this is now framed as a
low-power/wide-CI ceiling to be **demonstrated in WP3**, not a structural impossibility. Whether it rises to a
citable negative result is **gated on Stage 3c/WP3** (review Finding A/B); until then it is provisional.

Regardless of how the ceiling resolves, the strict matrix can still yield (a) a *descriptive, LC-inclusive* R
+ stability profile (hypothesis-grade), and (b) the artifact-vs-biology (and compartment) adjudication; the
ME/CFS-sensitivity matrix answers the *adjacent* question; and the GWS/FM read-across (WP4b) answers the Q-D
infection-specificity question. If WP3's LC-out power curve confirms the low-power ceiling, it
**strengthens, on data, the case that the harmonized prospective co-enrollment cohort (q0050) is necessary**,
matching the suspicion in `interpretation:0036`/`interpretation:0037`. Partial mitigations (deriving >1
contrast per dataset where subgroups/timepoints allow; adding the ME/CFS sensitivity arm) raise the *contrast*
count and thus per-fold power, but **do not restore non-LC trigger diversity** (the K≥3 identifiability lever),
so they help the CI without changing LC-out admissibility. This finding — as a **calibration-contingent
provisional ceiling**, not a settled verdict — is carried to WP6 and to `question:0050`.

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

### Stage 3 — Rank estimation (rotation-invariant primary) + t116 structural co-primary
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

**t116 structural statistic as confirmatory co-primary (review Finding B).** The SVD/parallel-analysis rank
estimator above is **not** the statistic `interpretation:0037` characterized: t116 varied R as a *generative*
parameter and measured the power of a **structural single-shared-axis statistic — the SD of off-diagonal
pairwise concordances** — so mapping an estimated R onto "the t116 R-regime grid" is a procedure substitution
that must be justified, not assumed. Therefore the **t116 structural single-axis-adequacy statistic is
computed as a confirmatory co-primary** alongside R (it is what the grid was built for and what t116 tells
q0050 to pre-register), and R is read against the grid **only after** the Stage-3c calibration below confirms
the battery recovers a known generative R at the corpus's real arm count / N. Where the two disagree
(low structural SD but moderate SVD rank, or vice-versa), the disagreement is reported as first-class evidence
about attractor-vs-repertoire, not reconciled away.

### Stage 3c — Rank-battery calibration against the t116 generative model (pre-grid, review Finding B)
Before any real-data R is placed on the t116 grid, **calibrate the battery on synthetic matrices drawn from
t116's own generative model** (`interpretation:0037`): inject pathway × contrast matrices at **known rank
R ∈ {2, 4, 8}** with matched off-diagonal concordance and arm-count bias, at the **real corpus's K (triggers)
and per-contrast N**, and confirm the estimators recover R and a well-calibrated CI — and that the structural
co-primary lands in the correct t116 regime band. This is the positive/calibration control the plan otherwise
lacks (t116's own credibility came from a parameter-free concordance-SD calibration; this is its analogue).
**A grid placement (Stage 5) is not emitted unless Stage 3c passes**; if the battery cannot recover R at the
corpus's real K/N, that is itself the finding (the corpus cannot identify the rank), reported in place of a
grid verdict. All synthetic-generator params live in `config.yaml` with the estimator seeds.

### Stage 3b — LODO/LOCO operationalization (pre-locked pass/fail)
Resampling stability is evidence only if its decision rule is fixed **before** seeing the folds. For every
leave-one-dataset-out (LODO) and leave-one-condition-out (LOCO) fold:

1. **Fold admissibility (structural gate) — re-grounded in t116 (review Finding A).** The **only
   `interpretation:0037`-grounded identifiability threshold is arm count: a fold is *non-identifiable* iff the
   remaining matrix retains `< 3 distinct triggers` (K<3)** — the t116 shared-axis requirement. Contrast count
   and platform count are **power dimensions, not identifiability gates**: a fold with K≥3 but few
   contrasts/one platform is **admissible-but-low-power** (wide CI), *not* non-identifiable. The earlier
   hand-set `min_contrasts=6` / `min_platforms=2` thresholds are **demoted from binary gates to reported power
   covariates** — they parameterize a **power/CI curve**, they do not by themselves declare a fold
   uninformative. A K<3 fold is reported as **non-identifiable** and excluded from pass/fail (stated
   explicitly, no silent drop); a K≥3-but-underpowered fold is **scored with its CI width and
   parallel-analysis power flag attached**, not excluded.
2. **Pass/fail on admissible folds.** **PASS** iff the artifact-adjusted R point estimate stays within
   **±1 of the full-corpus R AND within the same t116 regime band** (low ≈2–4 vs high ≥8) **and** the
   leading shared subspace is stable (principal angle between full-corpus and fold subspaces below a
   config'd cutoff). **FAIL** iff an admissible fold moves R across the t116 regime boundary.
3. **The long-COVID-out (LC-out) fold is a first-class, separately reported result** — not one fold among
   many — because LC supplies ~8 of ~13 columns. Under the re-grounded gate LC-out retains **≥ 3 triggers →
   admissible** (WB/PBMC primary: PI-ME/CFS, Ebola, Lyme = 3, at the K=3 floor after QFS moves to the
   compartment stratum per Finding C), so it is **not** declared "non-identifiable"; it is an
   **admissible-but-low-power** fold (3 single-trigger columns, no within-trigger replication) whose verdict is
   read off a **power/CI curve**,
   not a binary gate (review Finding A). If LC-out passes with a CI that stays inside one t116 regime, the
   low-rank conclusion is **robust**. If the LC-out parallel-analysis null band overlaps the observed leading
   eigenvalue, or the R CI spans the low/high regime boundary, the low-rank conclusion is labelled
   **conditional on long-COVID inclusion → hypothesis-generating, not q0050-grade** — the same demotion the
   two-matrix rule applies to sensitivity-only findings, but now **demonstrated by the fold's own power
   profile** rather than asserted from a hand-set contrast floor.
4. **Rare-trigger-out folds** (Ebola-out, Lyme-out, PI-ME/CFS-out in the WB/PBMC primary; QFS-out applies to
   the compartment-stratified estimate, not the WB/PBMC primary, per Finding C) retain all of LC and are
   typically admissible; a robust low-rank claim must **PASS every admissible rare-trigger-out fold**.

Config lives in `config.yaml`, committed before any fold is scored, with each parameter's **role** explicit:
`min_triggers=3` is the **identifiability gate** (t116 K≥3); `contrasts`/`platforms` counts are **power
covariates** attached to each fold's CI (not binary gates — review Finding A); R-band `±1`, subspace-angle
cutoff, and the parallel-analysis power rule are the pass/fail parameters. The Stage-3c calibration params
(injected R set, concordance/arm-bias, corpus K/N) live here too.

### Stage 4 — Sparse latent instrument (replication-gated, secondary)
The primary R stays rotation-invariant. A **sparse Bayesian factor model** (BicMix/SFAmix family;
ARD / spike-and-slab) is added as a **scoped, replication-gated** cross-check, never the primary readout,
for three specific jobs:
- shrinkage-based **active-factor-count** cross-check of R;
- **sparse contrast-loadings** to distinguish an **attractor** factor (dense across triggers) from
  **trigger/platform-specific** factors;
- **sparse feature-loadings** for artifact attribution (which sets carry a shared axis).
Deep disentanglement (sparse VAEs) is **deferred** — n≈15–40 contrasts cannot support it.

### Stage 5 — Artifact adjudication + t116-grid placement (gated on Stage 3c)
Run the full Stage-"artifact controls" battery (platform-LOO, **compartment/composition control**,
negative-control sets, recovered-control specificity, off-diagonal SD). **Separate biology-shared from
artifact-shared — and compartment-shared (review Finding C) — before reading R.** Then, **and only if Stage 3c
calibration passed** (review Finding B — otherwise no grid verdict is emitted, the calibration failure is the
result), map the surviving R + uncertainty **and the t116 structural co-primary** onto the **t116 R-regime
grid** (`interpretation:0037`): does the estimate land in the arbitrable low-rank regime (q0050 GO with the
t116 conditions), the non-arbitrating high-rank regime (q0050 NO-GO / redesign), or straddle? The grid verdict
is reported jointly for the rank estimator and the structural statistic; a divergence between them is carried
forward, not averaged.

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

### Key decision 4 — artifact *and compartment* controls gate the estimate
Platform-LOO, negative-control sets, recovered-control specificity, off-diagonal concordance SD, **and the
compartment/composition control (review Finding C)** are **admissibility criteria**, run before biological
interpretation. Two rivals are named for any low-rank finding: a **correlated shared artifact** (t116) and a
**cell-composition-shift axis** across mixed blood compartments — the latter is why the primary matrix is
WB/PBMC-only with sorted deposits held as a separate stratum.

### Key decision 5 — "non-arbitrating" is scoped to the achievable test family, not literally "any N"
The t116 high-rank regime is **non-arbitrating at achievable arm counts under this pathway-vector
structural-test family** — *not* literally at any N. This plan adopts that scoped wording. **Downstream
correction owed:** `interpretation:0037` and `question:0050` currently say "at ANY N"; this must be softened
to the scoped phrasing when those entities are next edited (tracked in Open Questions).

### Key decision 6 — the rank estimator must be calibrated to t116 before the grid is read
The SVD/parallel-analysis rank estimator is **not** the statistic t116 characterized (review Finding B). No
real-data R is placed on the t116 grid until the battery is calibrated against t116's generative model
(Stage 3c), and the **t116 structural single-axis statistic is carried as a confirmatory co-primary**. The
grid bridge is validated, not assumed.

## Work packages

### WP0 — Workflow skeleton, corpus link-through, config — **DONE 2026-07-08**
- Scaffolded `code/workflows/t117-crosspais-rank/` (`Snakefile` + `config.yaml` + `README.md`), the
  self-contained-subdir sibling of `t116-power-bias-floor/`. **Reuses** the shared `code/workflows/envs/`
  (`r-bioc.yaml` limma+fgsea Bioconductor stack) via `../envs/…`; `fgsea_enrich.R` is reused verbatim, and
  `limma_de.R` **only for the two-arm `~ group` contrasts** — the corpus's platform-batch, twin-paired,
  within-cohort-longitudinal, and continuous-severity-axis contrasts need a WP2 model extension, declared now
  as a per-contrast **`de_models` model contract** in `config.yaml` (`stock_ok: true|false` per contrast) so
  the divergence is deliberate, not a silent `~ group` fallback. `config.yaml` originates **all** design parameters (nothing
  hard-coded in rules): pinned universe hash slot, **per-estimator seeds** (parallel-analysis permutation,
  CV-SVD fold, split-half, bootstrap, BicMix MCMC seed/chains/convergence), the LODO/LOCO fold spec with
  **each param's role** (`min_triggers=3` identifiability vs `contrasts`/`platforms` power covariates, Finding
  A), the **Stage-3c calibration generator** (injected R∈{2,4,8}, concordance/arm-bias, corpus K/N), the
  **structural co-primary** (off-diagonal concordance SD, Finding B), the **artifact + compartment control**
  block (Finding C), the **GWS/FM specificity** block (Finding D, `enabled: false` until a deposit is found),
  and the **compartment map** (WB/PBMC primary vs sorted stratum).
- The **Snakefile wires the full DAG** (acquire → results/grid + datapackage; 73 jobs over 15 contrasts) with
  fail-early stub bodies per work package; `calibration_3c` gates `grid_placement`; the sorted stratum + acute
  decoys are consumed by `artifact_adjudication` (no silently-dropped config columns).
- Wrote `consumed_by: plan:0010-…` onto all **18** corpus/universe `dataset:` entities so Dimension-3 review
  resolves.
- **DoD (met):** `uv run --frozen snakemake -s code/workflows/t117-crosspais-rank/Snakefile -n all` resolves
  the complete DAG; envs are the shared already-locked `plan:0003` stack (reused, not re-solved); every corpus
  dataset carries a `consumed_by` backlink; the `datapackage` rule emits `results/…/datapackage.json` (matrix
  + R estimates + stability profiles).

### WP1 — Corpus verification + staging (the "verify details / explanatory power" pass) — **readiness gate** — *record-verification DONE 2026-07-08; pinned+checksummed acquisition DONE 2026-07-08; per-deposit parse = WP1b*
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
- **Acquisition executed (2026-07-08):** the pinned+checksummed staging is implemented and run. Every
  GEO/FigShare deposit's raw payload was downloaded and **verified against a LOCKED sha256**
  (`config.acquisition`, reusing `code/scripts/fetch_url.py`; empty hash or mismatch ⇒ HALT — the same
  fail-early discipline as plan:0003 WP1). 14 deposits staged (`acquire_payload`/`acquire_deposit`); the two
  reused deposits (QFS `GSE130353`, PI-CFS `GSE14577`) carry their identical t035 hashes. The **single pinned
  universe** was materialized per the **universe decision** (below) and re-verified (`build_universe` →
  `verify_universe`, sha256 `2a782ac5…9b07b`, reproducible on rebuild). The **SRA-only CHIKV decoy salmon
  path is wired** (`config.salmon`, env `../envs/salmon.yaml`) so the DAG resolves; the index build + FASTQ
  retrieval + quant + the day-21 run/group split are **deferred to WP1b** (reference hash HALT-guarded).
- **Universe decision (2026-07-08):** the single pinned universe = **Hallmark ∪ Reactome** (1153 sets,
  15–500 filter; GO:BP dropped so its ~4200 highly-overlapping ontology terms cannot inflate apparent
  low-rank structure — the shared-artifact confound the artifact battery guards against). Materialized from
  the two hash-locked plan:0003 clean-base `.rds` by `code/scripts/combine_universe.R` as
  `dataset:msigdb-2024-1-hs-hallmark-reactome-rank-universe` (derived; parent =
  `dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe`). Stage-2 references now resolve to this
  materialized universe.
- **DoD:** each admitted deposit has a verified entity + **staged (acquired+hashed) raw payload** + datapackage
  (✅); every provisional deposit is promoted or demoted with the decision recorded (✅); the finalized strict
  trigger/contrast/platform counts are written (✅). **Remaining before the gate fully closes:** per-deposit
  parse (`stage_matrix`, WP1b) turning each verified raw payload into the uniform gene matrix + sample sheet
  + QA. **No downstream WP (2+) runs until WP1b closes.**

### WP1b — Per-deposit parse → the uniform expression contract — *framework + tranches 1/(b)/(c)/(a)/(a2 tar trio)/(a-rest) DONE 2026-07-08 — 11 deposits PASS; only (d) salmon + gse267625/gse143549 remain*
The executable form of **review Finding F** (per-deposit ingest contract), pulled forward from WP2 so the
downstream matrix builds on a real contract, not an assumption.
- **WP0 semantic wiring confirmed/completed first (the pre-parse gate):** (a) the sensitivity rank matrix is
  **nested** — `MATRIX_COMPOSITION` composes it as *strict columns + the 3 ME/CFS additions* (12 cols), not an
  ME/CFS-only matrix; (b) `calibration_3c` depends on the **real** assembled strict matrix + grouping + structural
  stats (it cannot "pass" independent of the observed matrix and still unlock the grid); (c) the per-contrast DE
  model specs are **explicit** in `de_models`, and each now declares the exact `covariates` (platform / pair /
  dlco / subject+timepoint) the sample sheet must carry — so parsers build the right sheet, not a `~ group` default.
- **Brutally uniform output contract (`code/scripts/stage_matrix.py`, config `parse:` block):** every deposit
  emits exactly `expr.gene.tsv.gz` (Ensembl-gene × retained samples) + `sample_sheet.tsv` (sample, group, +
  declared covariates) + `clean.qa.pass` + `stage_matrix.qa.json`. The QA json is the per-deposit ingest
  contract: source payload (hash/url/kind), parser + handler, gene-id namespace (source → Ensembl, version-strip,
  duplicates collapsed + policy), expression scale (declared vs observed, `continuous_only` flag), samples
  retained/dropped + reasons + per-group counts, duplicate handling, and contrast eligibility (arms + de_model
  covariate coverage). Fail-early: an unresolved namespace / scale mismatch / missing group source / uncovered
  covariate HALTs — never a fabricated label or partial output.
- **Tranche 1 parsed + PROVEN on real data (`matrix` handler):** `gse251849_lc` (62710 Ensembl genes × 23; 11
  LongCOVID vs 12 pooled Control+Convalescent; group from column-name prefixes) and `scilifelab_lc` (60669 × 110;
  60 PAT vs 50 CTL; group from the companion `SamplesPC.txt`). Both surfaced that the depositor "counts" are
  **salmon/RSEM estimated counts** (fractional, ~78–85% integer) → a distinct `estimated_counts` scale class
  (continuous, limma-only), the same imprecise-label nuance t035's G2 check caught for MMSEQ `log_mu`.
- **Metadata-payload gap (decision-relevant finding):** for **most** GEO deposits the case/control mapping is
  **not in the expression supplement** that WP1 staged — it lives in the GEO **series-matrix / SOFT** metadata,
  which was not acquired. Each such deposit's `parse:` block is `status: deferred` naming its **exact** blocker
  (a metadata payload to add to acquisition, or a symbol/RefSeq→Ensembl harmonization map), so Finding F is an
  executable contract, not a guess.
- **Tranche (b) — shared gene-id identity contract DONE (2026-07-08):** `code/scripts/build_gene_id_map.R` builds
  the symbol/alias/RefSeq → Ensembl-gene map from the **same** annotation authority the gene sets used
  (org.Hs.eg.db, pinned 3.22.0) and the **same** `first` multimap policy as `genesets_reference.R` — so identity
  is **commensurable by construction**, not coincidence (this is what prevents a "parsed but not comparable"
  failure). `stage_matrix.py` hash-verifies the map and **fails closed**: map-rate < `min_map_rate` or a
  wrong-namespace fraction > `max_mixed_namespace_frac` marks the contrast **ineligible** rather than emitting a
  thin matrix. Proven on real ids: `gse270045` symbol 83% ✓, `gse128078` RefSeq 90% ✓, **`gse143549` gene_name
  56% → fails closed** (NOVEL/non-coding rows). The guardrail also fails closed on a **mostly-ambiguous** map
  (of the mapped ids, the fraction whose source resolves to ≥2 ENSG > `max_ambiguous_mapped_frac`) — the map
  carries a per-id `n_targets` so this is enforced per deposit, not just as a global census. **b·pin DONE
  (2026-07-08):** the canonical map was built by the pinned org.Hs.eg.db **3.22.0** r-bioc env
  (`build_gene_id_map --use-conda`), is **deterministic** (identical sha256 `d07f65bd…` on rebuild), and its
  hash is committed in `harmonization.map_sha256` + re-verified before use (tampered hash HALTs) — non-Ensembl
  parsing is now **reproducibly consumable**.
- **Per-deposit status after (b) — three distinct cases, not "group-only":**
  - `gse270045` (symbol 83% ✓): gene-id resolved; group **RESOLVED in tranche (a)** — see below.
  - `gse128078` (RefSeq 90% ✓): gene-id **identity** resolved; quantitative aggregation stays **sensitivity-only**
    (isoform-FPKM→gene `sum` approximately additive, `scale_caveat`); group **RESOLVED in tranche (a)** — see below.
  - `gse143549` (gene_name 56% ✗): **still gene-id-blocked** — fails the map-rate guardrail; staging its
    series-matrix metadata alone will **not** unlock the Ebola column (needs a cleaner symbol source / coordinate
    lift first), then group. **Deprioritized** per the reviewer.
- **Tranche (c) — microarray handlers DONE (2026-07-08):** the microarray deposits reach the uniform contract via
  a **compose-the-t035-chain** architecture: dedicated Snakemake rules run the parse→harmonize→collapse scripts as
  upstream producers (probe→gene needs the **platform** annotation `.db`, which can't live in the pure-Python
  `stage_matrix`), and a new **`prebuilt`** `stage_matrix` handler ADOPTS the resulting gene matrix + inline group
  into the 4 uniform outputs — so `stage_matrix` stays the SOLE producer of `expr.gene.tsv.gz`. Both deposits carry
  case/control **inline** (no extra metadata payload), so both **PASS**:
  - **`gse14577` (PI-CFS sensitivity, U133A∪B):** t035 chain reused **verbatim** (`parse_gse14577.py` →
    `harmonize_gse14577.R` [hgu133a/b.db, already pinned] → `collapse_probes.R`), group from the `patient_key`
    prefix. **PASS: 18371 genes × 15 patients (8 PI-CFS vs 7 HC), log2.** No env change.
  - **`gse16059` (discordant-twin ME/CFS, GPL570):** new generic `parse_series_matrix.py` + `harmonize_microarray.R`
    (probe→Ensembl via **hgu133plus2.db**, added to the pinned r-bioc env — an annotation-only, NES-neutral add) →
    `collapse_probes.R`. Group `diagnonsis`[sic] `unaffected→control`, `CFS→case`, **`ICF` excluded**; `twin_pair`
    carried as the block covariate. **PASS: 20338 genes × 76 samples (32 CFS vs 44 unaffected; 12 ICF dropped),
    log2**, probe-map 79% (GPL570). *Repro note: the `r-bioc.conda-lock.yml` postdates hgu133plus2.db and needs a
    `conda-lock` regen (tool absent this session) — the pinned `=3.13.0` yaml is the source of truth meanwhile.*
- **Tranche (a2) — per-sample `tar` trio DONE (2026-07-08):** the RAW.tar deposits carry **no group in the tar**,
  so handler code alone can't PASS them (reviewer's ledger caution, confirmed). Built a **generic `parse_tar`**
  (each member = one sample; `(member_gene_col, member_value_col)` name-or-positional → that sample's column, keyed
  by `sample_id_regex`; within-member dup-collapse under `member_agg`; then the same Ensembl collapse as
  `parse_matrix`) + a **`parse_geo_soft.py`** SOFT sibling; the metadata-sheet wiring is now selected by
  `metadata_format` (`series_matrix` → `parse_geo_metadata`; `soft` → `parse_geo_soft`) and decoupled from the expr
  handler. All three **PASS**:
  - **`gse130353` (post-Q-fever fatigue, monocytes; MMSEQ `log_mu`):** group from SOFT `subject status` via
    parenthetical-code regex `\(QFS\)`/`\(QS\)` (**`Fatigue Syndrom` alone mis-matches both QFS and CFS**); HC + CFS
    drop. **PASS: 56625 × 20 (10 QFS case / 10 QS infected-recovered control), map_rate 1.0, 0 NaN cells, scale
    `log_mu` PASS (limma-only).** *Compartment stratum per G1 — enters compartment-stratified R only.*
  - **`gse63085` (Lyme/PTLDS, cufflinks FPKM; 97 PBMC members):** arm **and** visit selected by the series-matrix
    `time` characteristic (`\(V5\)` = 6-mo post-treatment → case, `^control$` → control; Lyme V1/V2 drop as
    unmapped). **PASS: 20214 × 42 (29 Lyme-V5 case / 13 control), symbol map 86%, 0 NaN cells across 97 members.**
  - **`gse251872` (PI-ME/CFS PBMC; 27 members, 2 seq platforms):** value column named per-sample (`S###`) →
    positional `member_value_col: 2`; series-matrix URL 404s (multi-platform) so group comes from the family SOFT
    **title** (`, HV,` control / `PI-ME/CFS` case — sex 12M/15F is a coincidental count, not the group); `platform`
    batch covariate carried. **PASS: 18369 × 27 (12 case / 15 control), map_rate 1.0, scale=counts PASS.**
  - **Fail-closed guardrails added (review of a1):** duplicate metadata join keys HALT; covariate completeness gates
    on `notna()` (a `NaN`→`"nan"` string no longer passes); ragged GEO characteristic rows HALT.
- **Post-tranche hardening (project self-review, 2026-07-08):**
  - **(#1) Arm-partition guard** in `stage_matrix.resolve_groups`: a declared contrast **arm** that captures **0
    samples** HALTs, naming the dead selector — the too-loose sibling pattern that empties the other arm via
    first-match-wins (the `gse130353` QFS/CFS substring trap) is now caught structurally at group-resolution time,
    not left to surface as a REVIEW-verdict mis-attribution downstream. Enforced per-**arm**, so legitimate
    multi-selector arms (`gse251849` control = `^Control` ∪ `^Convalescent`) pass. Per-selector capture counts are
    recorded in `stage_matrix.qa.json` (`samples.group_resolution`). Also fixed a false-HALT in the a1 dup-key
    guard: `NaN`/blank join keys are non-joinable rows (they match no expr column) and are dropped as such
    (recorded, `n_nonjoinable_keys_dropped`), not mis-flagged as ambiguous duplicates — restores the clean 1:1 join
    on `scilifelab` (6 blank `SampleName` rows). All 9 ready deposits re-verified PASS; a QFS/CFS-trap unit check
    confirms the guard HALTs.
  - **(#3) Cross-deposit QA reconciliation** (`reconcile_qa.py` + Snakefile `reconcile_qa` rule): rolls every ready
    deposit's `stage_matrix.qa.json` into one sheet
    (`results/…/reconciliation/stage_matrix.reconciliation.{tsv,json}`) surfacing the pre-rank heterogeneity —
    **5 distinct expression scales** (`counts`/`estimated_counts`/`fpkm`/`log2_intensity`/`log_mu`), 4 gene-id
    namespaces (all → `ensembl_gene`), arm balance (236 case / 212 control across 9), gene-count spread
    (18369–62710), + a `warnings` list. `scale_heterogeneity` is flagged explicitly: deposits pool only at the NES
    level, so mixed scales are admissible **iff** each deposit's DE contrast absorbs its own scale — the sheet makes
    that assumption reviewable. Standalone QA target (not in `rule all`).
  - **(#2) DEFERRED to a task:** config-schema validation of each `parse:` block at DAG-load (a typo'd knob today
    silently defaults). Tracked in `tasks` for before the `a-rest` deposit count climbs.
- **Tranche (a) — series-matrix group metadata (series-matrix pair DONE, 2026-07-08):** the RNA-seq deposits whose case/control
  lives ONLY in the series-matrix `!Sample_*` header get that header staged as a **second acquisition payload**
  (pinned sha256, verified hash-stable across fetches), parsed by a new **`parse_geo_metadata.py`** into
  `series_metadata.samples.tsv`; `stage_matrix`'s `sheet` group_source **joins it to the expr columns** and applies
  the deposit's `level_map`/`group_regex` (raw condition → arm). Two group-blocked deposits now **PASS**:
  - **`gse270045` (LC, WB):** join expr cols = the `sample_id` characteristic; group = **title-regex** ("Healthy
    Control"/"Long Covid" — there is NO disease-state characteristic). **PASS: 24036 genes × 36 (19 LC / 17
    healthy), symbol map 83%.** **Data finding:** the `_LC_counts` file is a MISNOMER — fractional EM/pseudo-align
    gene counts (1e-8..5e4, library-size-varying column sums), so the `estimated_counts` scale check now tests the
    real invariant (non-negative + count magnitude), not an integer-fraction proxy that wrongly rejected heavily-
    fractional EM matrices (tranche-1 `gse251849`/`scilifelab` re-verified unchanged).
  - **`gse128078` (ME/CFS sensitivity, WB):** join = `title`; group = `disease_state` (ME/CFS/Control);
    subject+timepoint carried as covariates for the WP2 timepoint collapse. **PASS: 22424 genes × 99 samples
    (55/44 = 14 ME/CFS vs 11 control subjects), RefSeq 90%. SENSITIVITY-ONLY** (FPKM `scale_caveat`).
- **Tranche (a-rest) — the deposits needing MORE than series metadata (DONE 2026-07-08):** investigation showed
  the catalog's premises were wrong for all three; corrected in the SAME tranche (Explicit > Defensive). Two now
  **PASS**, one stays deferred with a sharpened blocker:
  - **`gse226260` (LC, PBMC) — CATALOG CORRECTED, PASS:** first catalogued as "2-platform, ≈46 LC vs rich
    controls, strongest". On inspection the combined expr matrix is **single-platform** (all 228 cols GPL24676;
    the 103 GPL34284 samples are ABSENT — the `~ platform + group` model was degenerate) and mixes the **PASC
    cohort (86 samples)** with a **disjoint 142-sample acute-severity cohort** (no `pasc status` → dropped).
    Group + subject/timepoint come from the **family SOFT** (2-platform → the plain series-matrix URL 404s), via
    `parse_geo_soft`; join = `title` (== expr col). Staged as **PASC vs NOPASC** (`level_map`): **24203 ENSG ×
    86 (72 PASC / 14 NOPASC = 28 vs 8 SUBJECTS)**. de_model corrected to `~ group` (no platform term) with
    subject+timepoint carried for the WP2 one-contrast-per-subject collapse. **control_type =
    infected-nonPASC-convalescent** (NOT rich/healthy); SMALL control arm flagged. (Gene space: 17345 rows carry
    a BLANK id — unlabeled features, unmappable → dropped; hence the soft map_rate 0.58, not a symbol-lookup fail.)
  - **`gse228320` (LC, WB) — CATALOG CORRECTED, PASS:** first catalogued continuous-`~ dlco`-only. Titles
    actually carry a **binary `control`/`sequela`** label AND continuous DLCO. Staged as the **two-arm
    control-vs-sequela** column (stock `~ group`); DLCO carried in the sheet for a **later severity-axis
    sensitivity**, not the primary contrast (per user decision — keep the primary matrix in the case/control
    contract, don't block on continuous-design machinery). The expr id `MC1_N` is EMBEDDED in the free-text title,
    so `stage_matrix` grew an optional **`sample_col_regex`** join-key extractor (leaves the original column intact
    so the same title still supplies the group). **60683 ENSG × 50 (18 sequela / 32 control).**
  - **`gse267625` (LC, WB) — STAYS DEFERRED (sharpened blocker):** the deposited metadata carries **NO
    case/control or symptom label** — only subject id (`AA*`/`VV*` prefix), timepoint (3 mnd / 12 mnd), all
    WT/untreated. A within-cohort contrast cannot be defined without inferring phenotype from an unlabeled prefix
    (an artifact risk). Deferred until the **GSE267625 publication** is read as a deliberate contrast-definition
    step — not a metadata-only guess. `gse143549` remains gene-id-blocked (56% < 0.60), deprioritized.
- **Remaining WP1b tranche:** only **(d)** the salmon/CHIKV decoy quant path (`salmon_gene_matrix`: index build +
  FASTQ retrieval + day-21 run/group split) + `gse267625` (pending its paper) + `gse143549` (gene-id). Priority per
  the reviewer was **b → c → a**; b, c, a series-matrix pair, a2 tar trio, and a-rest are all DONE — **11 deposits
  now PASS the uniform contract** (326 case / 258 control across 5 expression scales; see the reconciliation).
- **DoD:** every deposit has an executable `parse:` contract; each admitted deposit produces the 4 uniform
  outputs with a PASS `stage_matrix.qa.json`; each deferred deposit HALTs naming its blocker. **No WP (2+) runs
  until every strict/sensitivity contrast is parsed (or explicitly demoted).**

### WP2 — Uniform DE→enrichment → pathway × contrast matrix — **DONE 2026-07-08**
- **Scale-aware DE (`code/scripts/de_ranklist.R`, t117-owned — NOT a mutation of the shared t035
  `limma_de.R`):** the corpus spans **5 expression scales**, and the stock script lmFits DIRECTLY (correct
  only for already-log data). review Finding F, made executable: de_ranklist produces ONE ranking statistic
  (limma moderated-t) for EVERY deposit so the NES vectors stay commensurable — `counts`/`estimated_counts`
  → `limma::voom` (logCPM + precision weights, library-size norm; edgeR/TMM deliberately avoided so the
  NES-sensitive r-bioc env is not re-solved — the cross-deposit rank estimand is insensitive to the
  within-deposit TMM-vs-libsize choice); `fpkm`/`cpm` → `log2(x+1)` → lmFit; `log_mu`/`log2_intensity` →
  lmFit direct. `fgsea_enrich.R` reused **verbatim** over the single pinned Hallmark∪Reactome universe
  (1153 sets). Expression never merges across datasets — deposits meet only at the NES level.
- **Per-contrast model contract executed (config `de_models`):** the three `stock_ok:false` / special
  contrasts are handled by config-declared extensions in de_ranklist (no silent `~ group` fallback):
  `gse251872` → `~ platform + group` (case coef read by name); `gse16059` → `~ group` +
  `duplicateCorrelation(block=twin_pair)` (consensus 0.40); `gse226260` + `gse128078` → **longitudinal
  collapse** (`collapse_to: subject` — average each subject's timepoints to one pseudo-sample on the
  model-ready scale, THEN `~ group`; unit = subject, no pseudo-replication) per the plan's "collapse BEFORE
  limma". Unit counts match the corpus (gse226260 28 vs 8 subjects; gse128078 14 vs 11; gse251872 12 vs 15).
  **Two fail-closed hardenings (review Findings 2, 3):** for non-collapse models the voom mean-variance
  weights are estimated against the **same covariate-adjusted design** `lmFit` uses (built *before* `voom`,
  so a batch term is visible to the trend — matters for `gse251872`'s platform term); and a **rank-deficient /
  non-estimable design HALTs** (as does an all-NA case coefficient) rather than emitting a thin ranked list.
- **Two matrices assembled (`code/scripts/assemble_matrix.py`):** strict = **1153 gene_sets × 7 built
  columns** (of 9 declared — `gse267625` + `gse143549` **recorded as `omitted_columns` with their blocker**,
  never silently dropped); sensitivity (nested) = **1153 × 10** (strict + the 3 ME/CFS additions). QFS
  sorted stratum + acute decoys are correctly excluded from both rank matrices (they feed WP4 adjudication).
- **NES-comparability — a BEST-PAIR concordance SCREEN (not a proof every column is comparable).**
  Spearman over ALL 1153 sets was near-zero/negative for the same-tissue LC pairs (PBMC −0.15..0.00; WB
  +0.18) — a **noise-dilution artifact** of the ~700 near-zero-NES pathways, NOT genuine discordance. On the
  **enriched subset** (|NES|≥1.5 in either deposit) the best-matched same-tissue LC pairs concord:
  **PBMC `gse226260`~`scilifelab` ρ=+0.42 (verdict `best_pair_only`); WB `gse270045`~`gse228320` ρ=+0.50
  (verdict `concordant`)**. `concern` fires only if a group's *best* pair fails `min_concordance=0.20`
  (genuine harmonization failure) — here it is **false**. BUT the screen is explicit that PBMC is
  `best_pair_only`: **`gse251849` (n=11 vs 12, 0 BH<0.05) concords with NEITHER sibling (0.068 / −0.028) and
  is carried to WP3 as a `wp3_loo_candidate`** (leave-one-out sensitivity column) — it is flagged, never
  quietly passed (review Finding 1). So harmonization is verified *for the powered same-tissue pairs*; the
  lone underpowered LC PBMC column is held as a known discordant.
- **WP2 power finding (decision-relevant, feeds WP1 low-power ceiling):** per-deposit marginal DE power is
  **highly uneven** — `gse270045` 6081 BH<0.05, `gse63085` 515, `gse14577` 341, `scilifelab` 109,
  `gse226260` 52, but **five deposits return 0 BH<0.05** (`gse251849`, `gse228320`, `gse251872`,
  `gse128078`, `gse16059`). The rank estimand runs on NES (coordinated shifts), not marginal DEGs, so a
  0-DEG deposit still yields a NES vector — but `gse251849` (n=11 vs 12, 0 DEG) is genuinely uninformative
  and does NOT concord even on enriched sets (flagged `low_signal`). This uneven-power picture is the
  deposit-level face of the WP1 LC-out low-power ceiling and is carried to WP3's power/CI curve.
- **DoD (met):** one reproducible, QA-gated pathway × contrast matrix per matrix (strict, sensitivity) with
  condition/trigger/platform/compartment grouping + omitted-column ledger + comparability report; the
  same-tissue NES-comparability check passes on the informative subset (its all-set dilution is documented,
  not hidden). Run: `snakemake … --use-conda -- data/processed/t117/matrix/{strict,sensitivity}.pathway_by_contrast.tsv`.

### WP3 — Rank estimation battery + stability + t116 calibration — **DONE 2026-07-08**
- **Battery (`code/scripts/rank_battery.py` + shared `rank_estimators.py`):** three rotation-invariant
  estimators — Horn **parallel analysis** (per-column-permuted null; the **primary**, CI-bearing,
  calibration-validated estimator), **Owen-Perry bi-cross-validation SVD**, and **split-half**
  subspace-stability (contiguous-run principal-angle rule) — plus a row-**bootstrap CI** on the PA R and
  a participation-ratio effective dimension. `rank_estimators.py` is the **single source** both the battery
  and the calibrator import (Finding B: calibrated == applied procedure). Rank estimators run on the
  **common complete-case** row set (rows complete across all columns → fold subspaces are comparable);
  the **structural co-primary** (t116 off-diagonal Spearman-concordance SD) uses the pairwise-complete
  original data.
- **Result — descriptive R (LC-inclusive), both matrices LOW-rank but FRAGILE:**
  - **Strict (1153×7, 3 triggers): R_primary = 2** (PA sv 45.4/32.9 > null; bootstrap CI **[2,2]**;
    bicv=5 **flagged uninformative** — error monotone to the feasible ceiling; split-half=1). Regime =
    **low [2,4]**.
  - **Sensitivity (1153×10, 4 triggers): R_primary = 3** (PA passes 3; bootstrap CI **[3,4]**). Regime = low.
  - **LODO/LOCO fragility:** strict — dropping either strong LC deposit (`gse226260`/`scilifelab`)
    collapses R to 1 (FAIL); **every LOCO fold is non-identifiable** (only 3 triggers, LC=5 cols → dropping
    any trigger leaves 2). Sensitivity — only **lyme-out PASSes**; mecfs-/pi-mecfs-/LC-out all FAIL
    (subspace angle > 20°). So the low-rank is **not** stable under leave-one-out.
  - **LC-out (first-class):** **strict = NON-IDENTIFIABLE** (retains only PI-ME/CFS + Lyme = 2 triggers,
    below the t116 K≥3 floor — Ebola omitted at WP1b, QFS is the sorted stratum); **sensitivity =
    identifiable but FAIL** (R→2, angle 24.5°). Under the two-matrix rule this is **hypothesis-generating,
    not q0050-grade** — demonstrated on data, not asserted.
- **Structural co-primary DIVERGES from the SVD rank (first-class, plan Stage 3).** Both matrices show a
  **near-zero mean off-diagonal concordance (strict −0.064, sensitivity −0.031) with a HIGH SD
  (0.249 / 0.267)** — the **heterogeneous** (finite-repertoire-like, `question:0017`) signature, **NOT** the
  t116 single-attractor signature (low SD + high mean). The SVD says "low-rank ≈2–3"; the structural
  statistic says "no homogeneous shared axis." This divergence is reported, not reconciled.
- **Stage 3c calibration (`code/scripts/calibration_3c.py`) — FAILS, and the failure IS the finding
  (fail-closed, review Finding B / Key decision 6).** A **three-arm** design against t116's own generative
  model at the real K/per-column-N: (0) an **α=0 estimator self-check** (clean rank-R, no bias); (1) a
  strong-signal **positive control** (ρ=0.45, t116 arm-bias 0.60); (2) the **operating-point** arm matched
  to the real off-diagonal concordance. **Two INDEPENDENT grounds for no grid** (both recorded additively
  in `calibration.pass`): **(1) estimator-vs-corpus-width limit** — on the clean α=0 signal the battery
  **only weakly recovers R=2** (R̂≈1, within the ±1 tol but **CI coverage 0.54 ≪ 0.90 → under-covered**) and
  **does not recover R=4** (R̂≈1) from K=7 columns → a rotation-invariant SVD rank estimator cannot cleanly
  resolve rank ≥2 of a t116 nonneg-loading repertoire at this corpus **width**, so the SVD→t116-grid
  substitution is **not licensed at K=7**; **(2) corpus at its operating point** — the matched arm sits at
  the concordance **sampling floor** (real ρ −0.064 ≈ 0 < 1/√(P−1)=0.033 → kappa→0, no shared signal to
  identify), which alone (independent of ground 1) means no rank is identifiable. `calibration.pass` carries
  `pass=false`; **WP6 grid placement is fail-closed on it — no t116-grid verdict may be emitted.**
- **Compartment-stratified R (Finding C):** strict PBMC (5 cols) R=2, WB (2 cols) R=1; sensitivity PBMC
  (6 cols) R=3, WB (3 cols) R=1. Full composition-adjustment/deconvolution is WP4.
- **DoD (met):** R point estimate + bootstrap CI per matrix from **≥3 rotation-invariant estimators**, the
  **structural co-primary** SD, **LODO + LOCO reported separately**, the **LC-out contrast-count power/CI
  curve** + first-class LC-out fold, compartment-stratified R, and a **Stage-3c calibration pass/fail
  record** (FAIL → no grid). Run:
  `snakemake … --use-conda -- results/t117-crosspais-rank/rank/{strict,sensitivity}.rank.json results/t117-crosspais-rank/calibration/calibration.pass`.
- **Decision-relevant consequence.** WP3 **demonstrates on data** the WP1 provisional low-power ceiling
  (now no longer provisional for the rank claim): the existing public single-trigger blood-bulk corpus
  **cannot deliver a q0050-grade, LC-out-surviving cross-PAIS rank** — both because its cross-contrast
  concordance is at the noise floor and because its column width (K=7/10) cannot resolve rank ≥2 on the
  t116 grid. The descriptive low-rank + the SVD-vs-structural divergence are hypothesis-grade. This
  **strengthens, on data, the case that q0050's harmonized prospective co-enrollment cohort is necessary.**

### WP4 — Artifact + compartment adjudication — **DONE 2026-07-08**
- **Battery (`code/scripts/artifact_adjudication.py`):** reuses the WP3 battery **verbatim** (imports
  `rank_battery` + `rank_estimators` — composition, so every within-stratum / pooled / platform-drop R is the
  identical procedure the headline R used). Consumes the WP3 rank/structural outputs + grouping + the
  assembled matrix + the buildable sorted-stratum NES. Emits `{matrix}.compartment_stratified.json` and
  `{matrix}.adjudicated.json`. Unavailable prongs are recorded **note-only with the exact blocker**, never a
  silent skip or fabricated adjustment (Explicit > Defensive).
- **Every stratum/drop is held to the SAME K≥3 identifiability rule as the LODO/LOCO folds** (review WP4
  Finding 1): a <3-trigger stratum is **non-identifiable** — its R is reported for reference but is **not
  interpretable**, and it cannot establish (or refute) invariance. This is what keeps the underpowered controls
  from being read as decisive.
- **Compartment/composition control (Finding C), three prongs:**
  - **(i) compartment-stratified R** (deconvolution-free composition control): **strict PBMC R=2 (3 triggers,
    identifiable) vs WB (1 trigger, NON-identifiable, R=1 uninterpretable); sensitivity PBMC R=3 (3 triggers) vs
    WB (2 triggers, non-identifiable) vs PBL (1 col).** In both matrices **only the PBMC stratum clears K≥3**,
    so **compartment invariance is NOT ESTABLISHED** (`compartment_invariance_status: not_established`) — a
    cell-composition-shift rival can be **neither confirmed nor refuted**; this is an **underpowered control,
    not evidence of entanglement** (corrected from the first pass, which over-claimed "R differs → entangled").
  - **(ii) drop-sorted sensitivity** (strict): the primary is already WB/PBMC-only (G1), so R_drop-sorted ==
    primary R=2; **pooling the sorted QFS stratum keeps R=2 but rotates the leading subspace 26.7° (> the 20°
    cutoff)** → pooling perturbs the subspace, the **on-data justification for holding sorted out** (the pooled
    matrix has ≥3 triggers, so this rotation test is identifiable). (Sensitivity: not applicable — no sorted
    stratum.)
  - **(iii) composition adjustment (CIBERSORTx-LM22 deconvolution): note-only deferred** — needs a gated
    signature tool + per-sample re-DE; the pooled NES matrix cannot be composition-adjusted post-hoc. Prong (i)
    is the available deconvolution-free composition control (here underpowered).
- **Artifact controls:**
  - **Platform-LOO:** **strict is single-platform (rnaseq) → `untestable_single_platform`**: the low-rank
    **cannot be shown platform-independent** (a limitation carried to the grid). **Sensitivity (2 platforms):**
    drop-microarray R=3 **survives** (8 rnaseq cols, 4 triggers — identifiable); **drop-rnaseq is
    NON-identifiable** (2 microarray cols, 2 triggers < K=3), so its low R is **untestable, not a "collapse"**
    → `platform_invariance_status: partial` (survives the one identifiable drop; the other cannot be tested).
  - **Recovered-control specificity (directional, not magnitude):** the shared subspace defined by the
    case-vs-**naive** columns (strict r=2 from 4 naive cols, 3 triggers) is **NOT strongly present in the
    case-vs-recovered columns** — mean projection fraction **0.09 < min 0.30** (vs the in-sample naive 0.71;
    random-direction null ≈0.002). **Conservative reading:** this supports only *the naive-defined subspace is
    weakly present in the recovered-control contrasts* — it does **not** by itself prove the axis is
    "infection-history"/"case-vs-healthy" (the reference is in-sample; the recovered columns differ by
    dataset/control composition). (Same verdict on sensitivity.)
  - **No artifact floor was subtracted** (review WP4 Finding 2): the pinned Hallmark∪Reactome universe carries
    no housekeeping/platform/GC-confounded rows to subtract (set-based subtraction **note-only deferred**, needs
    a WP2 universe re-run). The **only null applied is the parallel-analysis per-column-permuted null**, which
    controls **random cross-column structure ONLY** — it is a **`random_structure_null_floor`, NOT an artifact
    floor** (it does not subtract correlated platform/batch/control-type/composition artifacts). R_primary
    counts the 2 SVs above it; the off-diagonal-SD sampling floor (0.033) is reported alongside.
  - **Acute-decoy specificity: note-only deferred** for **both** matrices — both decoys unbuildable (GSE68310
    parse-deferred; CHIKV salmon-deferred WP1b-d); recorded per-decoy with its blocker.
- **Result — the adjudication does NOT rescue the low-rank as a robust attractor, and the available controls
  are underpowered/incomplete.** `artifact_controls_pass = false` → `interpretation_status =
  limited_or_nonarbitrating` for both matrices: compartment invariance **not established** (only PBMC
  identifiable), platform invariance **untestable** (strict) / **partial** (sensitivity), the naive shared
  subspace **weakly present** against recovered controls, and no set-based / composition / acute-decoy artifact
  floor is available. The R point estimate (strict 2 / sensitivity 3) is the **random-structure-null-adjusted**
  R_primary, **not** a clean artifact-adjudicated estimate. This coheres with the structural heterogeneity
  (mean≈0, high SD) and the Stage-3c FAIL — the descriptive low-rank is **neither confirmed as compartment/
  platform-invariant nor refuted**; it is not q0050-grade and not cleanly biologically readable.
- **DoD (met):** R point estimate + compartment-stratified R + drop-sorted sensitivity + platform-LOO +
  recovered-control specificity reported per matrix, each held to the K≥3 identifiability rule, with an explicit
  `artifact_controls_pass` / `interpretation_status` the WP6 grid placement must consume (Finding 3), and every
  unavailable control (set-based negative controls, CIBERSORTx composition adjustment, acute-decoy specificity)
  recorded note-only with its blocker.

### WP4b — Non-infectious specificity read-across (GWS/FM) — review Finding D — **DONE 2026-07-09**
- **Discovery sweep (resolves Open Question #4).** Three blind parallel sweeps (GWI, fibromyalgia, PACVS +
  other non-infectious) against GEO/ArrayExpress/SRA/literature, each adjudicated against the **same
  admissibility gates** as the primary corpus. Outcome: **NOT the note-only branch — multiple admissible
  public deposits exist** across two independent non-infectious triggers and both platforms. Adjudicated
  panel (config `specificity_readacross.candidates`; each a `dataset:` entity):
  **fibromyalgia (idiopathic)** — `GSE221921` (96 FM/93 HC, PBMC RNA-seq — **flagship**), `GSE67311`
  (70/70, WB microarray); **Gulf War Illness (chemical)** — `E-MEXP-2069` (9/11, PBMC microarray),
  `GSE286345` (44/40, PBMC RNA-seq, *admissible-pending* a GWI/FM co-carry check); **IEI (environmental)** —
  `GSE182503` (17/21, PBMC microarray). FM sorted-neutrophil sets (`GSE334369`/`GSE229750`) are a separate
  sorted stratum (held out, G1). **PACVS: no admissible public blood transcriptome exists** (serum/
  autoantibody field; the one GEO hit is embargoed with a spurious label) → a **note-only gap**, gates not
  relaxed.
- **Separate non-infectious specificity column, NEVER pooled.** The flagship rides the **same** uniform
  DE→enrichment over the **same** pinned universe as the primary corpus (config `matrix: specificity` — a tag
  absent from `MATRIX_COMPOSITION` and the adjudication extras, so it enters no rank matrix and no artifact
  control), then is **projected onto the learned PAIS subspace** (`gws_fm_specificity.py`). Flagship built
  end-to-end (`GSE221921`: RAW.tar 189 per-sample members → 96/93, log-normalized-TPM `log2_intensity`
  scale, symbol→Ensembl map 86%, NES over the 1153-set universe). *(Infra: closed a latent reproducibility
  gap — `acquire_payload` now emits the `origin.json` provenance sidecar `stage_matrix` requires, so a fresh
  acquire of any deposit stages reproducibly, not just deposits carried over from the WP1 run.)*
- **Result — the PAIS subspace is PARTIALLY recovered by non-infectious fibromyalgia (`exploratory_flagship`,
  not `validated_specificity`).** The FM case-vs-control column projects **0.045** of its variance onto the
  strict PAIS rank-2 subspace. **Above chance** is established by an **empirical row-permutation null**
  (null mean 0.0025, p95 0.0074, **empirical p = 0.0005** over 2000 permutations of the FM column across
  pathways — the analytic isotropic floor r/P=0.0025 is reported for orientation only, not as calibrated
  specificity; review Finding 3). The **replication ceiling is the trigger-INDEPENDENT leave-one-*trigger*-out
  projection** (review Finding 1 — column-LOO would let a held-out long-COVID column reuse the other LC
  columns), averaged **per-trigger not per-column** (follow-up review Finding — 5 of 7 strict columns are
  SARS-CoV-2, so column-weighting understates the ceiling at 0.16 vs the per-trigger mean **0.24**): FM sits
  at **0.185× the trigger-weighted trigger-LOO mean**. Verdict **`partially_recovered_indeterminate`**:
  **neither cleanly infection-specific** (FM is well above its permutation null) **nor a full generic-sickness
  manifold** (FM is well below a trigger-held-out PAIS trigger). **Sharper caveat surfaced by trigger-LOO:**
  that ceiling is itself **heterogeneous (per-trigger 0.11 SARS-CoV-2 / 0.27 PI-ME/CFS / 0.35 Lyme), with the
  long-COVID-out projections LOW** — i.e. the PAIS subspace is **not even trigger-general within PAIS**
  (coheres with the Stage-3c FAIL / heterogeneous structural co-primary), so FM's partial recovery is read
  against a weak, non-trigger-general baseline, not an absolute specificity claim. That baseline is moreover
  **under-identified**: with 3 strict triggers each leave-one-trigger-out reference is built from only 2
  triggers, below the K≥3 floor (`trigger_loo_identifiability_pass: false`).
- **Update (2026-07-09b) — 2nd non-infectious column built (`GSE67311`) + reverse projection implemented.**
  The FM whole-blood-microarray column (60 FM/68 HC, `hugene11sttranscriptcluster.db` chain) was built and
  the **reverse projection** (build U from the non-infectious columns, project PAIS) implemented. Outcome:
  **not a clean replication** — two confounds surfaced. **(a) Compartment/platform confound:** WB-microarray
  FM recovers the PAIS subspace at **0.234** (0.965× ceiling) vs the PBMC-RNAseq flagship's **0.045** — a ~5×
  same-condition gap tracking compartment (strict corpus = 5 PBMC + 2 WB), so the high WB recovery is
  plausibly blood composition, not FM biology. **(b) Reverse under-resolved at 2 columns:** rank-matched
  ceiling caps at r_eff=1 < PAIS R=2 → `under_resolved_need_more_noninfectious_columns` (the reverse analogue
  of the K=2 degeneracy); a 3rd+ cross-condition, compartment-matched column is required. Read-across stays
  **`exploratory_flagship`** with an explicit compartment confound + under-resolution gate.
- **Update (2026-07-10) — 3rd non-infectious column built (`E-MEXP-2069` GWI PBMC), reverse FULL-RANK.**
  The compartment-matched GWI column (9/11, PBMC, HG-U133 Plus 2.0, baseline arm; raw CEL → **pure-R RMA**,
  limma normexp + limma quantile + `medpolish`, because affy/preprocessCore threaded C fails on this host with
  `pthread_create()=22`; → 20,338 genes) lifts the reverse projection to **`r_eff = min(R=2, n_noninf−1=2) = 2`**
  (`identifiability_pass=true`), resolving the 2-column under-resolution. **Reverse verdict:
  `noninfectious_axis_not_reproducible_indeterminate`** — the leave-one-non-infectious-out ceiling is LOW
  (0.053), so even across FM and GWI the non-infectious axis does not reproduce (PAIS recovers U 0.072 > ceiling,
  ratio 1.37): no coherent generic-non-infectious manifold exists to test against. **The GWI column also
  disentangles the forward confound:** being PBMC (compartment-matched) it still recovers **0.213** — like the
  WB-microarray FM (0.234) and ~5× the PBMC-RNAseq FM flagship (0.045), so the forward gap tracks **PLATFORM
  (microarray 0.224 vs RNA-seq 0.045), NOT compartment** and NOT condition (tiny-N microarray recovers high;
  large-N RNA-seq does not) — a technical confound. Both results reinforce `exploratory_flagship` and neither
  licenses `validated_specificity`; the next lever remains the purpose-built K≥3 cohort (`question:0050`).
- **DoD (met):** a GWS/FM specificity readout (subspace-recovery fraction vs random-null and held-out-PAIS
  references) emitted at `results/…/specificity/gws_fm.json`, with the admissible panel + queued replication
  (`GSE67311`/`E-MEXP-2069`/`GSE286345`) + the PACVS note-only gap recorded; carried to WP6 and
  `question:0050`. Non-infectious-deposit *availability* is no longer a gap; the **weak-U_ref** caveat is.

### WP5 — Sparse-FA instrument (replication-gated) — **NOT BUILT (moot under fail-closed) 2026-07-09**
- Fit BicMix/SFAmix; cross-check active-factor count; classify attractor vs trigger/platform-specific
  factors; sparse feature-loadings for artifact attribution. Report only where it replicates the Stage-3
  R within tolerance.
- **Disposition:** the replication gate **cannot pass**. Stage-3c demonstrated the corpus does not identify a
  rank at its operating point (off-diag concordance −0.064 ≤ floor 0.033; injected ranks not recovered) and
  the SVD battery is width-limited at K=7 — so a sparse-FA active-factor count has nothing stable to replicate
  *to*, and any decomposition would be reported non-replicating/secondary and non-load-bearing. Building it
  would not change the t117 verdict (`interpretation:0038`, fail-closed). Left unbuilt; revisit only if the
  q0050 K≥3 cohort lifts the corpus above the identification floor.
- **DoD (waived):** a secondary factor-count + attractor/specific decomposition, flagged secondary — waived as
  moot; the failure is recorded here and in `interpretation:0038` (Limitations).

### WP6 — t116-grid placement + interpretation + doc corrections — **DONE 2026-07-09**
- **Decision gate (review Finding E) — RECORDED (`interpretation:0038`, User Questions).** Stage-3c confirmed
  the low-power ceiling, so the decision was taken: the **full descriptive analysis is retained and reported as
  the t117 deliverable**, but framed as a **DEMONSTRATION of the identification ceiling + supporting non-grid
  readouts**, not a grid verdict. Rationale: the descriptive pass produced three decision-relevant results the
  lean (WP1-only) alternative would have missed — the empirical Q-C answer (corpus concordance ≤ floor), the
  GWS/FM specificity read-across, and the artifact/compartment adjudication. **No further staging/harmonization
  of the public single-trigger corpus is warranted** (the ceiling is corpus-intrinsic); the next lever is the
  q0050 K≥3 cohort.
- **Grid placement is FAIL-CLOSED.** Stage 3c FAILED (`calibration.json: pass=false`, two independent grounds),
  so no R was placed on the t116 grid. The interpretation reports the descriptive R (strict 2 / sensitivity 3)
  and the structural co-primary (off-diag concordance −0.064 ≤ floor 0.033, SD 0.249) explicitly non-grid, the
  q0050 GO/NO-GO consequence (fundable-with-conditions; public data cannot substitute), the two-matrix verdict
  (q0050-grade R = strict; sensitivity = hypothesis-generating), and the GWS/FM read-across
  (`partially_recovered_indeterminate`). The scoped "achievable arm counts, not any N" wording was landed in
  `interpretation:0037` and `question:0050`.
- **DoD (met):** `interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed` answers t117 + the q0050
  consequence + the Q-D/GWS-FM specificity read-across; the Finding-E scope decision is recorded; the two
  "any N" corrections landed in 0037 + q0050.

## Non-Goals

- Confirming or refuting a shared attractor (h0001) — R is a **design parameter**, not the verdict.
- Any absolute-magnitude / fold-scale claim — rank/subspace geometry only.
- Pooling expression across datasets, or pooling omics layers into one matrix.
- Relying on author-request-only or gated data (analysis-ineligible; note-only).
- Running the q0050 cohort or the ≥3-trigger harmonized test.

## Acceptance Criteria

- [x] **(WP0, 2026-07-08)** Every corpus input resolves to a `dataset:` entity with `consumed_by: plan:0010-…`
      (all 18 written); strict vs sensitivity vs stratum vs decoy membership and `onset_certainty` recorded per
      deposit in `config.yaml`.
- [x] **WP1 record-verification pass (2026-07-08)** set `access.verified` per deposit (or demoted it),
      replacing the `[UNVERIFIED]` specifics with confirmed values; **every floor-/SRA-provisional deposit
      resolved** (both demoted); strict matrix finalized at ~10 contrasts / 5 triggers *(admissibility tally;
      runtime-built = 7 columns / 3 triggers after further staging/QA attrition)*. Staging (download)
      remains pending WP0. Surfaced the LC-out low-power ceiling as a **provisional, calibration-contingent**
      result (not binding — review Finding A; to be demonstrated by the WP3 power curve).
- [x] **(WP3, 2026-07-08)** LODO/LOCO carry **pre-locked pass/fail semantics** (Stage 3b): the
      identifiability gate is **K≥3 triggers only** (t116-grounded — review Finding A), with
      contrast/platform counts as **reported power covariates, not binary gates**; non-identifiable (K<3)
      folds excluded from pass/fail; a fixed R-band + regime + subspace-angle PASS rule; and the **LC-out
      fold reported first-class as a power/CI curve** (strict LC-out = non-identifiable at 2 triggers;
      sensitivity LC-out = identifiable-but-FAIL → hypothesis-generating).
- [x] **(WP3, 2026-07-08)** **Stage 3c calibration (review Finding B):** the rank battery is calibrated
      against t116's generative model at the corpus's real K/per-column-N via a three-arm design
      (α=0 self-check + strong-signal positive control + operating-point matched arm). **Result — two
      INDEPENDENT grounds for no grid** (additively recorded): (1) on a clean α=0 signal the battery only
      weakly recovers R=2 (R̂≈1, under-covered: CI coverage 0.54) and does not recover R=4 → the SVD→t116-grid
      bridge is not licensed at the corpus width K=7/10; (2) the real concordance is at the sampling floor →
      no rank identifiable at the operating point. `calibration.pass=false`, **no grid placement**
      (fail-closed). The **t116 structural single-axis statistic is reported as a confirmatory co-primary**
      and diverges from the SVD rank.
- [x] **(WP2, 2026-07-08)** One reproducible, QA-gated pathway × contrast matrix per matrix (strict = 1153×7
      built of 9, sensitivity = 1153×10), computed by a single harmonized scale-aware DE→enrichment
      (`de_ranklist.R` voom/log2/direct → `fgsea_enrich.R`) over the pinned Hallmark∪Reactome universe;
      deferred columns (`gse267625`, `gse143549`) recorded as `omitted_columns`; same-tissue LC
      NES-comparability **best-pair screen** on the enriched subset (WB `concordant` ρ=0.50; PBMC
      `best_pair_only` ρ=0.42 with `gse251849` discordant → carried to WP3 `wp3_loo_candidates`).
- [x] **(WP3, 2026-07-08)** R is reported with uncertainty from **≥3 rotation-invariant estimators**
      (parallel analysis [primary, bootstrap CI], bi-cross-validation SVD, split-half) + participation
      ratio, and its **leave-one-dataset-out and leave-one-condition-out** stability profiles are reported
      **separately** (strict R=2 CI[2,2], sensitivity R=3 CI[3,4]; both LC-inclusive, both LOO-fragile).
- [x] **(WP4, 2026-07-08)** The artifact-control battery (platform-LOO, negative-control sets,
      recovered-control specificity, off-diagonal SD) **and the compartment/composition control** (review
      Finding C: WB/PBMC-only primary, compartment-stratified R, drop-sorted sensitivity, composition-adjusted R
      where deconvolution is valid) are reported, each held to the **K≥3 identifiability rule** used by the
      LODO/LOCO folds. **Result — `artifact_controls_pass = false` / `interpretation_status =
      limited_or_nonarbitrating`:** compartment invariance **NOT established** (only the PBMC stratum clears
      K≥3; WB/PBL non-identifiable), platform invariance **untestable** (strict single-platform) / **partial**
      (sensitivity: drop-microarray survives, drop-rnaseq non-identifiable), and the naive shared subspace is
      **weakly present** in case-vs-recovered (projection 0.09 < 0.30, conservative reading only). The R point
      estimate (strict 2 / sensitivity 3) is the **random-structure-null-adjusted** R_primary — **no artifact
      floor was subtracted** (set-based negative controls, CIBERSORTx composition adjustment, and acute-decoy
      specificity are all **note-only deferred** with their blockers).
- [x] **(WP4b, 2026-07-09) Non-infectious specificity read-across (review Finding D):** the discovery sweep
      found admissible public deposits (fibromyalgia `GSE221921`/`GSE67311`, GWI `E-MEXP-2069`/`GSE286345`,
      IEI `GSE182503`; PACVS = note-only gap, none public). The FM flagship (`GSE221921`, 96/93 PBMC RNA-seq)
      was built through the same pipeline and projected onto the strict PAIS subspace: **recovery 0.045,
      above its row-permutation null (empirical p=0.0005) but only 0.185× the trigger-independent
      (leave-one-trigger-out, per-trigger-weighted) PAIS ceiling (0.24) → `partially_recovered_indeterminate`**
      (neither infection-specific nor a full generic-sickness manifold), read under the weak-U_ref caveat (the
      trigger-LOO ceiling is itself heterogeneous, LC-out low → subspace not trigger-general, and
      under-identified: 3 triggers → 2-trigger references, `trigger_loo_identifiability_pass: false`).
      `exploratory_flagship`; the rest of the panel is queued replication.
- [x] **(WP6, 2026-07-09)** The two-matrix verdict rule is applied (`interpretation:0038`): the q0050-grade R
      comes from the **strict** matrix (R=2, band `low`, `artifact_controls_pass=false`); the **sensitivity**
      R=3 (K=10) is labelled **hypothesis-generating**; the adjacent ME/CFS question is answered separately and
      does not feed the q0050 grade.
- [x] **(WP6, 2026-07-09)** R + uncertainty (rank estimator **and** structural co-primary) are **NOT** placed on
      the t116 R-regime grid — Stage 3c FAILED (`calibration.json: pass=false`), so grid placement is
      **fail-closed** (the pre-locked "only after Stage 3c passes" rule); the descriptive R + structural
      co-primary are reported non-grid, with the explicit q0050 GO/NO-GO consequence (fundable-with-conditions).
- [x] **(WP0, 2026-07-08)** Reproducibility: per-estimator seeds (parallel-analysis permutation, CV-SVD fold,
      split-half, bootstrap, BicMix MCMC seed/chains/convergence) are pinned in `config.yaml`, and the
      `datapackage` rule emits `results/…/datapackage.json` (implementation deferred to WP6).
- [x] **(WP6, 2026-07-09)** The scoped "non-arbitrating at achievable arm counts under this test family"
      wording is carried into `interpretation:0037` and `question:0050`: the 2-arm / mean-concordance
      non-arbitration is kept as genuinely *any N* (structurally undefined / blind by construction), while the
      high-rank finite-repertoire non-arbitration is scoped to achievable arm counts (≤6 arms), not literally
      any N.

## Open questions

1. **SRA quantification pin.** `prjna1184005`, `prjna1001790` need a raw-read → gene-count path; pin the
   quantifier + reference so their NES vectors are comparable to the GEO-matrix deposits. *Lean: salmon +
   pinned transcriptome, documented as a platform axis for the artifact battery.*
2. **Microarray deposits in a mostly-RNA-seq matrix** (`gse68310`, `gse16059`, `gse14577`) — platform is a
   known shared-axis risk; these are LOO-conditional and feed the platform-LOO control directly.
3. **Longitudinal/paired contrast policy** (`gse267625`, `gse16059`) — define the single representative
   contrast per subject/timepoint in WP2 to avoid pseudo-replication inflating apparent rank.
4. **GWS/FM deposit availability (WP4b feasibility, review Finding D) — RESOLVED 2026-07-09.** The discovery
   sweep found **multiple admissible** public, downloadable, sample-level non-infectious blood-bulk WB/PBMC
   case-vs-control deposits (fibromyalgia `GSE221921`/`GSE67311`, GWI `E-MEXP-2069`/`GSE286345`, IEI
   `GSE182503`), so the read-across is a **real object, not a note-only gap** — the FM flagship is built and
   projected (`partially_recovered_indeterminate`). Only **PACVS** has no public deposit (note-only gap,
   gates not relaxed). Remaining open sub-questions are now execution items, not feasibility: (a) resolve the
   `GSE286345` GWI/FM co-carry before building it; (b) the queued microarray deposits need probe→gene
   annotation adds (`hugene11sttranscriptcluster.db` for `GSE67311`, Agilent for `GSE182503`); (c) the
   reverse projection needs ≥2 non-infectious columns.

## Notes on reusable infrastructure

The rank-estimation battery (parallel analysis + CV-SVD + split-half + blocked LODO/LOCO over a
pathway × contrast matrix) and the artifact-control battery are **`reusable: true`** — liftable to any
cross-condition pathway-overlap rank question in `health-immunity` / `pan-disease`, and a candidate for
commons promotion once stabilized. Stage-2 reuses `plan:0003`'s limma→fgsea + `qa_checkpoint.py` verbatim.
