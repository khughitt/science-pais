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
finalized the strict matrix at **~10 contrasts / 5 triggers** (see *Corpus* + *WP1 corpus-readiness
finding*). What remains before a verdict: **staging** the matrix-ready deposits (download + checksum +
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
  (review Finding D; `specs/scope-boundaries.md` D-003 names Gulf War Syndrome / fibromyalgia as "the single
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
- Long COVID (6 matrix-ready): `gse226260-longcovid-pbmc` (≈46 LC vs rich convalescent+healthy controls; 2-platform batch — **strongest**), `gse270045-longcovid-mecfs-wholeblood` (19 LC+ME/CFS vs 17 healthy — **clean**), `scilifelab-28832492-longcovid-pbmc` (60 vs 50, controls are **infected-recovered** — scores well on G3; FigShare-API matrix), `gse251849-longcovid-pbmc-cognitive` (11 vs 12, small — subgroup n 5–7), plus two **heavy-caveat keeps**: `gse267625-longcovid-wholeblood` (matrix public but **no external control** — contrast must be built *within-cohort* in WP2; longitudinal), `gse228320-longcovid-wholeblood-pulmonary` (matrix public but the contrast is a **DLCO pulmonary-severity axis within ARDS survivors**, not fatigue-dominant LC — LOO-drop).
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

### WP1b — Per-deposit parse → the uniform expression contract — *framework + tranche 1 DONE 2026-07-08*
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
  - `gse270045` (symbol 83% ✓): gene-id resolved; deferred on **group** (CCI/HP/S prefixes ambiguous — needs
    series-matrix metadata; not inferred from the 19/17 count match).
  - `gse128078` (RefSeq 90% ✓): gene-id **identity** resolved but **quantitative aggregation UNRESOLVED** —
    isoform-FPKM→gene `sum` is only approximately additive (recorded as `scale_caveat`; **sensitivity-only**
    unless re-quantified); also deferred on group.
  - `gse143549` (gene_name 56% ✗): **still gene-id-blocked** — fails the map-rate guardrail; staging its
    series-matrix metadata alone will **not** unlock the Ebola column (needs a cleaner symbol source / coordinate
    lift first), then group.
- **Remaining WP1b tranches:** **(a)** add the missing GEO
  series-matrix/SOFT metadata payloads to `acquisition` (re-pin hashes) so the group-blocked deposits
  (`gse226260`, `gse228320`, `gse267625`, group side of `gse270045`/`gse128078`) resolve — plus a cleaner
  identity source for `gse143549`; **(c)** microarray handlers (`series_matrix`, `soft` — reuse
  `collapse_probes.R` / `parse_gse14577.py`) for `gse16059`/`gse14577` and the per-sample `tar` handler (reuse
  `extract_gse130353.py`) for `gse130353`/`gse251872`/`gse63085`; **(d)** the salmon/CHIKV decoy quant path
  (`salmon_gene_matrix`). Priority per the reviewer: **b → c → a**.
- **DoD:** every deposit has an executable `parse:` contract; each admitted deposit produces the 4 uniform
  outputs with a PASS `stage_matrix.qa.json`; each deferred deposit HALTs naming its blocker. **No WP (2+) runs
  until every strict/sensitivity contrast is parsed (or explicitly demoted).**

### WP2 — Uniform DE→enrichment → pathway × contrast matrix
- Run Stage-2 machinery over all admitted contrasts on the pinned universe; emit the matrix + per-contrast
  QA. Longitudinal/paired one-contrast-per-unit policy applied.
- **Per-deposit ingest contract + NES-comparability gate (review Finding F):** each deposit gets an explicit
  ingest/normalization/gene-id path (salmon TPM/counts vs DESeq/CPM vs Illumina microarray vs MMSEQ span
  three compartments and ≥5 sequencers — "reuse plan:0003 verbatim" understates this). Before any
  cross-compartment comparison is trusted, the two same-tissue LC RNA-seq deposits must produce **concordant
  NES on a matched contrast** — a comparability check, not an assumption.
- **Per-contrast DE model contract (WP0 `de_models`):** the stock `limma_de.R` fits only `~ group`;
  `stock_ok: false` contrasts (`gse226260`/`gse251872` platform-batch → `~ platform + group`; `gse16059`
  twins → `~ group` blocked on `pair`; `gse267625` no-external-control → a within-cohort contrast WP2 must
  define; `gse228320` → continuous `~ dlco` severity axis) require the script to be **extended before the
  column is admitted** — the model contract is declared in `config.yaml` so this is a deliberate WP2 step.
- **DoD:** a single reproducible pathway × contrast matrix (+ condition/platform/**compartment** grouping
  metadata), QA-gated, for both strict and sensitivity matrices; the same-tissue NES-comparability check passes
  (or its failure is surfaced as a harmonization blocker).

### WP3 — Rank estimation battery + stability + t116 calibration
- **Stage 3c first (gating):** calibrate the battery on t116-generative synthetic matrices at known
  R ∈ {2,4,8} at the real corpus K/N; confirm recovery + CI calibration; **no grid placement downstream
  unless this passes** (review Finding B).
- Parallel analysis, CV/bi-cross-val SVD, split-half, LODO + LOCO on both matrices; **compute the t116
  structural single-axis statistic as a co-primary** alongside R; report R + uncertainty and the full
  stability profile.
- **Report the LC-out fold as a power/CI curve** over the contrast-count / power covariates, not a binary
  identifiability verdict (review Finding A); state whether the low-power ceiling is demonstrated.
- **Compartment-stratified R** (WB, PBMC, sorted) + drop-sorted sensitivity (review Finding C).
- **DoD:** R point estimate + interval per matrix (rank estimator **and** structural co-primary), with
  LODO/LOCO curves, the LC-out power curve, compartment-stratified R, off-diagonal SD, and a Stage-3c
  calibration pass/fail record.

### WP4 — Artifact + compartment adjudication
- Platform-LOO, negative-control sets, recovered-control specificity; subtract the artifact floor;
  re-report R.
- **Compartment/composition control (review Finding C):** WB/PBMC-only primary R; drop-sorted sensitivity;
  where deconvolution is valid (WB, partial PBMC — not sorted monocytes), report R before/after
  composition adjustment with the composition axis as a named nuisance dimension.
- **DoD:** artifact- **and composition-**adjusted R; explicit statement of how much of the shared structure
  survives each; whether the low-rank signal dissolves under composition adjustment or compartment stratification.

### WP4b — Non-infectious specificity read-across (GWS/FM) — review Finding D
- Assemble a **separate non-infectious specificity matrix** (Gulf War Syndrome / fibromyalgia blood-bulk
  WB/PBMC; PACVS if a public downloadable deposit exists) under the **same admissibility gates** as the
  primary corpus and the **same uniform DE→enrichment over the same pinned universe**; compute its
  pathway × contrast matrix as a distinct object.
- Project the PAIS subspace onto it (and vice-versa): quantify how much of the learned PAIS shared subspace
  is **recovered by non-infectious GWS/FM** — the direct test of the t116 Q-D infection-specific-attractor vs
  generic-sickness-manifold ceiling.
- **This WP is itself gated on a public, downloadable, sample-level GWS/FM deposit clearing the gates** — if
  none exists, record that as a note-only gap (do not relax the gates), mirroring the inaccessible-deposit
  discipline.
- **DoD:** a GWS/FM specificity readout (subspace-recovery fraction) or an explicit "no admissible
  non-infectious deposit" note; carried to WP6 and `question:0050`.

### WP5 — Sparse-FA instrument (replication-gated)
- Fit BicMix/SFAmix; cross-check active-factor count; classify attractor vs trigger/platform-specific
  factors; sparse feature-loadings for artifact attribution. Report only where it replicates the Stage-3
  R within tolerance.
- **DoD:** a secondary factor-count + attractor/specific decomposition, flagged secondary.

### WP6 — t116-grid placement + interpretation + doc corrections
- **Decision gate (review Finding E), after WP3 Stage-3c/LC-out power curve:** if the calibration confirms
  the low-power ceiling, decide whether the descriptive R + GWS/FM specificity + composition adjudication is
  worth the full staging/harmonization cost, or whether the **WP1 finding + the scoped calibration is itself
  the t117 deliverable**. Record the decision.
- Map R + uncertainty (rank estimator **and** structural co-primary) onto the t116 R-regime grid **only if
  Stage 3c passed**; state the q0050 GO/NO-GO consequence and the verdict under both matrices per the
  two-matrix rule, plus the **GWS/FM infection-specificity** result. Write the interpretation entity; carry
  the scoped "achievable arm counts" wording into `interpretation:0037` and `question:0050`.
- **DoD:** an `interpretation:` deliverable answering t117 + the q0050 consequence + the Q-D specificity
  read-across; the Finding-E scope decision recorded; the two "any N" corrections landed.

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
      resolved** (both demoted); strict matrix finalized at ~10 contrasts / 5 triggers. Staging (download)
      remains pending WP0. Surfaced the LC-out low-power ceiling as a **provisional, calibration-contingent**
      result (not binding — review Finding A; to be demonstrated by the WP3 power curve).
- [ ] LODO/LOCO carry **pre-locked pass/fail semantics** (Stage 3b): the identifiability gate is **K≥3
      triggers only** (t116-grounded — review Finding A), with contrast/platform counts as **reported power
      covariates, not binary gates**; non-identifiable (K<3) folds excluded from pass/fail; a fixed
      R-band + regime + subspace-angle PASS rule; and the **LC-out fold reported first-class as a power/CI
      curve** — a low-rank result that cannot power LC-out is demoted to hypothesis-generating.
- [ ] **Stage 3c calibration (review Finding B):** the rank battery is validated against t116's generative
      model at the corpus's real K/N (recovers known R ∈ {2,4,8} with calibrated CI) **before any grid
      placement**, and the **t116 structural single-axis statistic is reported as a confirmatory co-primary**.
- [ ] One reproducible, QA-gated pathway × contrast matrix per matrix (strict, sensitivity), computed by a
      single harmonized DE→enrichment over the pinned `msigdb-2024-1-hs-mapped-pais-gene-set-universe`.
- [ ] R is reported with uncertainty from **≥3 rotation-invariant estimators**, and its **leave-one-dataset-out
      and leave-one-condition-out** stability profiles are reported **separately**.
- [ ] The artifact-control battery (platform-LOO, negative-control sets, recovered-control specificity,
      off-diagonal SD) **and the compartment/composition control** (review Finding C: WB/PBMC-only primary,
      compartment-stratified R, drop-sorted sensitivity, composition-adjusted R where deconvolution is valid)
      are reported, and the artifact- and composition-adjusted R are stated.
- [ ] **Non-infectious specificity read-across (review Finding D):** a GWS/FM (± PACVS) matrix under the same
      gates + same pipeline is projected against the PAIS subspace (Q-D infection-specificity test), **or** an
      explicit "no admissible non-infectious deposit" note is recorded (gates not relaxed).
- [ ] The two-matrix verdict rule is applied: the q0050-grade R comes from the strict matrix; any
      sensitivity-only low-rank result is labelled hypothesis-generating; the adjacent ME/CFS question is
      answered separately.
- [ ] R + uncertainty (rank estimator **and** structural co-primary) are placed on the t116 R-regime grid
      **only after Stage 3c passes**, with the explicit q0050 GO/NO-GO consequence.
- [x] **(WP0, 2026-07-08)** Reproducibility: per-estimator seeds (parallel-analysis permutation, CV-SVD fold,
      split-half, bootstrap, BicMix MCMC seed/chains/convergence) are pinned in `config.yaml`, and the
      `datapackage` rule emits `results/…/datapackage.json` (implementation deferred to WP6).
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
4. **GWS/FM deposit availability (WP4b feasibility, review Finding D).** WP4b needs a *public, downloadable,
   sample-level* GWS or fibromyalgia blood-bulk (WB/PBMC) case-vs-control deposit clearing the same gates as
   the primary corpus. A discovery sweep for such a deposit is unstarted; if none is admissible the Q-D
   infection-specificity read-across becomes a note-only gap (gates not relaxed), not a free-form column.

## Notes on reusable infrastructure

The rank-estimation battery (parallel analysis + CV-SVD + split-half + blocked LODO/LOCO over a
pathway × contrast matrix) and the artifact-control battery are **`reusable: true`** — liftable to any
cross-condition pathway-overlap rank question in `health-immunity` / `pan-disease`, and a candidate for
commons promotion once stabilized. Stage-2 reuses `plan:0003`'s limma→fgsea + `qa_checkpoint.py` verbatim.
