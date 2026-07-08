---
reviews:
  - plan:0010-crosspais-pathway-response-rank-estimation
  - entities/plans/0010-crosspais-pathway-response-rank-estimation.md
date: "2026-07-08"
overall: WARN
---

# Pipeline Review: t117 cross-PAIS pathway-response rank estimation (plan:0010)

- **Reviews:** `plan:0010-crosspais-pathway-response-rank-estimation` (+ its WP1-verified `dataset:` corpus)
- **Date:** 2026-07-08
- **Overall:** WARN

## Summary

This is an unusually honest, well-structured data-analysis plan: it freezes a rotation-invariant estimand,
pre-locks the LODO/LOCO pass/fail *procedure* (the discipline is real, though the threshold *values* are not
yet calibrated — Finding A), treats correlated-artifact bias as first-class admissibility, and — via a real
WP1 record-verification pass — has surfaced a **provisional** negative result (public single-trigger blood
data appear unable to deliver a q0050-grade, long-COVID-out-surviving rank). It earns credit for that — but
**that ceiling is calibration-contingent, not yet binding**: it currently rests on the unsourced
`min_contrasts=6` gate (Finding A), so it must not be cited as a settled or deliverable-grade result until the
Finding A/B calibration is done. But the review finds **two HIGH conceptual gaps the plan does not flag**: (1) the headline "LC-out
non-identifiable" ceiling rests on an **unsourced `min_contrasts=6` threshold that is not `interpretation:0037`-grounded**
(t116 grounds *arm count K≥3*, under which LC-out is admissible-but-underpowered, not non-identifiable) —
a borderline-circular, threshold-driven conclusion; and (2) the plan's primary statistic is a **rank
estimator (SVD/parallel-analysis)**, whereas t116 characterized the power of a **different** statistic (the
structural SD-of-off-diagonal-concordances test), so "mapping R onto the t116 R-regime grid" is **not yet
justified** and lacks the parameter-free calibration t116 itself exemplifies. A third substantive gap: the
strict matrix **mixes blood compartments** (whole blood / PBMC / sorted monocytes), so a shared cross-trigger
axis could be **cell-composition shift**, not shared pathway biology — a confound the artifact battery does
not catch. None invalidate the estimand; all should be closed before the workflow is built.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | WARN | Stage-3b thresholds (`min_triggers/contrasts/platforms`, R-band ±1, subspace-angle cutoff) are chosen, not sourced; the headline finding hinges on the unsourced `min_contrasts=6`; the "~1000-set" universe resolution (load-bearing per t116) is asserted, not shown |
| Assumption audit | WARN | Compartment heterogeneity (WB/PBMC/sorted monocytes) → shared axis may be cell-composition shift, not pathway biology; cross-platform NES comparability assumed |
| Data availability | WARN | Corpus resolves to entities; most `verified: true` / `landing-confirmed` / `last_reviewed: 2026-07-08`; **staging deferred to WP0 (retrieval-probe exception — OK)**; but `consumed_by: plan:0010` backlinks not yet written (WP0 task) |
| Identifiability | WARN | q0050-grade target honestly reported unreachable, re-scoped target reachable; **but the "non-identifiable" strength is threshold-driven** (see Finding A) — the defensible claim is "low-power/wide-CI", weaker than stated |
| Reproducibility | WARN | Inherits plan:0003 seed + version-pin discipline; but the **new estimators'** determinism (parallel-analysis permutation seed, CV-SVD fold seed, BicMix MCMC seed/chains/convergence) is unspecified |
| Validation criteria | WARN | QA checkpoints inherited; **no positive/calibration control that the rank battery recovers a known injected R** (t116 had parameter-free calibration; this plan needs the analogue); no scale/resource run named |
| Scope check | PASS (note) | Squarely in-scope (PAIS cross-trigger synthesis, feeds q0050/h0001); **but omits the project's designated non-infectious stress-test (GWS/FM read-across, D-003)** for the Q-D attractor-vs-generic-manifold question |
| Integration boundaries | WARN | "Reuse plan:0003 machinery verbatim" understates a large per-deposit harmonization surface; and the rank estimator ≠ the t116 structural statistic (Finding B) — the grid mapping is an unvalidated boundary |
| Manifest completeness | WARN | Datapackage discipline inherited from plan:0003, but a `datapackage.json` for the t117 rank-estimation outputs (matrix + R estimates + stability profiles) is not explicitly required |

## Detailed Findings

### Finding A — the headline LC-out ceiling is threshold-driven and not t116-grounded (Dim 1 + Dim 4, HIGH)

The plan's binding result — "LC-out leaves ~4 contrasts < the ≥6 floor → **non-identifiable** → strict result
capped at hypothesis-grade" — is the most decision-relevant claim in the document. It rests on the Stage-3b
gate `min_contrasts=6`, which the plan **sets itself** and does **not** source. `interpretation:0037` grounds
a different quantity: the binding levers are **arm count K≥3** and feature resolution (~1000 sets); "per-arm N
is not the binding constraint." Under a t116-faithful gate (**≥3 arms/triggers**), the LC-out fold retains
**4 triggers ≥ 3 → admissible**. The honest statement is therefore weaker than "non-identifiable": LC-out
estimates a shared-subspace rank from **4 single-trigger columns with no within-trigger replication**, which is
**low-power with a wide confidence interval** — not structurally unreachable. As written, the plan **defines
the gate and the gate drives the headline** (borderline circular), and the specific verdict flips with an
unsourced constant (at `min_contrasts=4`, LC-out is borderline-admissible).

**Recommendation:** re-ground the admissibility gate in `interpretation:0037` (K≥3 arms + ~1000-set features)
rather than a hand-set contrast count; report the LC-out conclusion as a **sensitivity curve over the
threshold and over per-fold power** (parallel-analysis CI width), not a binary identifiability verdict. The
qualitative conclusion ("public data cannot *robustly* pin the cross-PAIS rank once LC is removed") likely
survives — but it must be shown to survive, not asserted via `min_contrasts=6`. **Until that calibration is
done the WP1 ceiling is provisional** and must not be cited as a binding or deliverable-grade negative result
(this is the governing qualifier for the Summary and Finding E, and it revises the strength of the claim in
commit `fef2f1c` / the plan's WP1 corpus-readiness section from "non-identifiable" to "low-power, pending
calibration").

### Finding B — the rank estimator is not the statistic t116 characterized; the grid mapping is unvalidated (Dim 6 + Dim 8, HIGH)

Stage 3 makes the **effective rank R** (parallel analysis / cross-validated SVD) the primary readout, and
Stage 5 **maps that R onto "the t116 R-regime grid."** But t116/`interpretation:0037` never studied a rank
estimator: it varied R as a *generative* parameter and measured the **power of a structural single-shared-axis
statistic (the SD of off-diagonal pairwise concordances)**. There is no result in t116 that a rank
*estimator* recovers the generative R at achievable K/N — so the plan's central bridge ("estimate R → read
off the t116 GO/NO-GO") is a **procedure substitution that has not been validated**. This is also the missing
positive control: t116's credibility came from a *parameter-free calibration* (concordance SD vs 1/√(P−1)
matching the t035 run); this plan reports no analogous check that its battery returns the right R on data of
known rank.

**Recommendation:** either (i) adopt t116's **structural single-factor-adequacy statistic** as the
confirmatory primary (it is what the grid was built for, and what interp-0037 tells q0050 to pre-register),
relegating SVD-rank to a descriptive companion; or (ii) **calibrate the rank battery against t116's own
generative model** — inject matrices at known R (2, 4, 8) with matched concordance and arm-bias, confirm the
battery recovers R (and its CI) at the corpus's real K/N — *before* any real-data R is mapped to the grid.
Option (ii) is the cheaper and more informative addition and mirrors the t116 calibration ethos.

### Finding C — compartment heterogeneity is an unmodeled biological confound (Dim 2, HIGH)

The strict matrix mixes **whole blood, PBMC, and sorted monocytes** (QFS `gse130353`). A shared cross-trigger
axis can then be a **cell-composition-shift axis** (neutrophilia / lymphopenia / monocyte activation) — a
genuine, reproducible expression signal that is **not** disease-pathway biology and that the artifact battery
does **not** catch: platform-LOO cannot separate compartment from trigger when a rare trigger has exactly one
compartment (drop the monocyte set and you drop Q-fever entirely), and housekeeping/GC negative-control sets
don't flag composition shift because it is real regulation, not a technical artifact. This is arguably the
single most likely benign explanation for a low-rank cross-PAIS signal.

**Recommendation (multi-pronged — deconvolution alone is insufficient).** Cell-fraction estimation is only
meaningful for **whole blood (and partially PBMC)**; it **cannot** be run on the sorted-monocyte QFS deposit
and **cannot** make monocyte-only NES directly comparable to whole-blood/PBMC NES. So the control must be
structural, not just statistical: (i) **compartment-stratified rank estimates** (estimate R within each
compartment stratum and compare); (ii) a **"drop sorted-compartment" (and ideally a WB/PBMC-only primary)
sensitivity** — the low-rank conclusion must survive removing the sorted compartment; (iii) where
deconvolution *is* valid (WB, PBMC), report R **before and after composition adjustment** with a composition
axis as a named nuisance/negative-control dimension. A shared axis that dissolves under composition adjustment,
or that only appears when compartments are pooled, is a blood-count/compartment signature, not an attractor.
Consider making **WB/PBMC-only the primary matrix** and treating sorted-compartment deposits as a separate
stratum.

### Finding D — the project's designated non-infectious stress-test (GWS/FM) is omitted (Dim 7, MEDIUM)

`specs/scope-boundaries.md` (D-003) names **Gulf War Syndrome / fibromyalgia as "the single best external test
of the attractor's trigger-agnostic claim"** and PACVS as read-across. The plan's specificity layer uses
*acute-infection* decoys but omits this designated *non-infectious* read-across — yet it is exactly the lever
for `interpretation:0037`'s Q-D identifiability ceiling (infection-specific attractor vs generic-sickness
manifold). If the learned PAIS blood subspace is **equally recovered by non-infectious GWS/FM**, that is strong
evidence it is a generic fatigue/sickness manifold, not an infection-specific attractor.

**Recommendation:** add GWS/FM (and if available PACVS) as a **separate non-infectious specificity matrix /
read-across analysis** — **not** a free-form column appended to the primary matrix, which would relax the very
compartment/platform discipline this review demands elsewhere (Finding C, F). It must pass the **same
admissibility gates** as the primary corpus (blood-bulk, public, downloadable, sample-level case-vs-control)
and be run through the **same uniform DE→enrichment over the same pinned universe**, then compared to the PAIS
subspace as a distinct object. Scored as a discriminating test of infection-specificity: if the learned PAIS
subspace is equally recovered by gated, uniformly-processed non-infectious GWS/FM, that is strong evidence for
a generic fatigue/sickness manifold over an infection-specific attractor (Q-D).

### Finding E — WP1 may (after calibration) already be the deliverable; weigh the cost of Stages 2–6 (Dim 4, MEDIUM)

WP1 has surfaced a **provisional, calibration-contingent** negative result whose strength depends on
Finding A (it currently rests on the unsourced `min_contrasts=6` gate — it is *not yet* an established
ceiling). **If, and only if, the Finding A/B calibration confirms it**, that negative result — "not robustly
estimable from public data, here is the corpus-readiness ceiling + the interp-0037 amendment" — is a
defensible t117 deliverable on its own, and building the full pipeline (stage 10 deposits → harmonize → rank
battery → sparse FA → artifact adjudication) to produce a heavily-caveated **hypothesis-grade descriptive R**
would be a large effort for little marginal value. So the cost question is real, but it is *downstream of*
Finding A, not independent of it.

**Recommendation:** insert an explicit **decision gate after Finding A/B are resolved**: is the descriptive R
(plus the GWS/FM specificity test and artifact adjudication) worth the staging + harmonization cost, or is the
WP1 finding + a scoped calibration the t117 deliverable? If proceeding, de-scope to the cheapest path that
yields the descriptive R + the Q-D specificity test.

### Finding F — "reuse plan:0003 machinery" understates the harmonization surface (Dim 8, MEDIUM)

plan:0003's preprocessing is **dataset-specific** (MMSEQ `log_mu` near-zero antimode filter for GSE130353;
U133A∪B combine for GSE14577). The t117 corpus spans salmon TPM/counts, DESeq/CPM tables, Illumina microarray,
and MMSEQ across three compartments and ≥5 sequencers. Each deposit needs its own ingest/normalization/gene-id
path, and NES comparability across e.g. sorted-monocyte-MMSEQ vs PBMC-salmon vs PBL-microarray is **assumed,
not shown**. "Reuse verbatim" hides most of the real engineering.

**Recommendation:** specify a **per-deposit ingest contract** and an **NES-comparability gate** in WP2 — e.g.
the two same-tissue LC RNA-seq deposits should produce concordant NES on a matched contrast before any
cross-compartment comparison is trusted.

### Finding G — provenance backlinks and rank-output manifest (Dim 3 + Dim 9, LOW)

`consumed_by: plan:0010` backlinks are not yet on the datasets (WP0 names this), and no `datapackage.json` is
specified for the rank-estimation outputs. Both are deferred/acceptable but should be named as DoD items.

## Recommendations (priority order)

1. **Resolve the estimator/statistic mismatch (Finding B)** — calibrate the rank battery against t116's
   generative model (or adopt t116's structural statistic) before any grid mapping. Highest-leverage: it is
   the bridge the whole q0050 consequence rides on.
2. **Re-ground the LC-out ceiling (Finding A)** — replace `min_contrasts=6` with a t116-grounded (K≥3) gate +
   a threshold/power sensitivity curve; downgrade "non-identifiable" to "low-power/wide-CI" unless the sim
   calibration says otherwise.
3. **Add the cell-composition control (Finding C)** — deconvolution + composition-adjusted R; the leading
   benign rival for a low-rank signal.
4. **Add the GWS/FM specificity read-across (Finding D)** — the project's own designated test of infection-specificity / Q-D.
5. **Decide scope (Finding E)** and **specify per-deposit ingest + NES-comparability (Finding F)**; pin the
   new estimators' seeds/convergence and the rank-output datapackage (Findings G, Repro/Manifest).

## Strengths

- **Intellectual honesty is the plan's defining feature.** It pre-registers the LODO/LOCO pass/fail
  *procedure* before seeing folds — a real methodological discipline, though the credit is for the procedure,
  not the threshold *content*, which is still uncalibrated (Finding A) — self-reports the long-COVID dominance,
  and — via a real WP1 pass — surfaces a (provisional) negative result rather than burying it. The two-matrix
  verdict rule (strict vs ME/CFS-sensitivity, with hypothesis-grade demotion) is exactly right.
- **WP1 was executed against real records, not asserted** — and it did work: it demoted two deposits on the
  ≥4-week floor (removing influenza and chikungunya), corrected GSE251872 (12v15, not 17v21), and caught
  GSE224615's missing per-sample matrix. Design specifics are now record-checked, not `[UNVERIFIED]`.
- **Artifact-as-rival is first-class**, correctly importing the t116 pipeline-review's correlated-bias finding
  as an admissibility criterion rather than cleanup.
- **The estimand is rotation-invariant and the sparse-FA instrument is correctly relegated** to a
  replication-gated secondary — the plan resists the temptation to over-model n≈15–40 contrasts.

## Disposition

Overall **WARN** — a sound, honest design with no invalidating defect, but with two HIGH conceptual gaps
(estimator↔t116-statistic mismatch; threshold-driven headline) and one HIGH confound (compartment/composition)
that should be closed before the WP0 workflow is built. Recommended path: address Findings A–C (and add the
Finding D specificity test) as plan amendments, then re-review the amended Stage 3/5 before committing to
staging.

## Re-review (2026-07-08, post-amendment — plan commit `4776934` + consistency follow-up)

The plan was amended to fold in Findings A–G. Re-checking the affected dimensions:

| Finding | Status | Resolution in `plan:0010` |
|---|---|---|
| A — threshold-driven LC-out headline | **Resolved (procedurally)** | Fold-admissibility gate re-grounded to **K≥3 triggers only** (t116); `min_contrasts`/`min_platforms` demoted to reported **power covariates**; the binary "NON-IDENTIFIABLE" headline **withdrawn** and reframed as an admissible-but-low-power fold whose verdict is a **WP3 power/CI curve**. Residual is *execution*: WP3 must actually produce the curve; until then the ceiling is explicitly **provisional**, consistently across Readiness / Stage 3b / WP1-finding / AC. |
| B — estimator ≠ t116 structural statistic | **Resolved** | New **Stage 3c** calibrates the battery against t116's generative model at the corpus K/N *before* any grid placement (Stage 5 hard-gated on it); the **t116 structural single-axis statistic** is carried as a confirmatory co-primary; new Key decision 6. Residual dependency: Stage 3c presumes interp-0037's generative model is re-implementable — reasonable, but a real WP3 prerequisite. |
| C — compartment/composition confound | **Resolved** | **WB/PBMC-only primary** (G1); sorted-monocyte QFS held as a **separate compartment stratum**; three-pronged control (stratified R + drop-sorted + composition-adjusted R where deconvolution is valid) in the artifact battery and WP4. |
| D — non-infectious GWS/FM read-across | **Resolved (scoped)** | New **WP4b**: a separate, identically-gated GWS/FM (±PACVS) specificity matrix, same uniform pipeline; open question #4 tracks deposit availability; note-only fallback if no admissible deposit (gates not relaxed). |
| E — WP1 may be the deliverable | **Addressed** | Explicit **decision gate** in WP6 *after* the Finding A/B calibration, sequenced downstream of A (not independent of it). |
| F — harmonization surface understated | **Addressed** | WP2 now carries a **per-deposit ingest contract** + a **same-tissue NES-comparability gate** before cross-compartment comparison is trusted. |
| G — backlinks + rank-output manifest | **Addressed** | `consumed_by` backlinks + `datapackage.json` + per-estimator seeds are now WP0 DoD + AC items. |

**New interaction surfaced by the re-review (Finding A × Finding C).** Making the primary matrix WB/PBMC-only
(Finding C) removes the sorted-monocyte QFS deposit — the *only* Q-fever trigger — from the primary matrix,
dropping the WB/PBMC strict-primary from 5 to **4 documented triggers** and the **LC-out fold to exactly 3
triggers (PI-ME/CFS, Ebola, Lyme)** — right at the t116 K=3 identifiability floor. This *tightens* rather than
breaks the low-power story (one fewer LC-out column), and the plan's Corpus / WP1-finding / Stage 3b arithmetic
were reconciled to state it explicitly. It does mean the WB/PBMC LC-out fold is at the **minimum admissible K**,
so the WP3 power curve is now doing even more load-bearing work — worth watching, not a defect.

**Re-review disposition:** the three HIGH findings are **closed at the plan level**; what remains is genuinely
*execution* (Stage 3c calibration, the WP3 LC-out power curve, WB/PBMC-only rank runs, a GWS/FM deposit
search). No new blocking defect. The plan is ready for **WP0 workflow build** on the understanding that the
provisional WP1 ceiling is not citable as settled until Stage 3c + the WP3 power curve land.
