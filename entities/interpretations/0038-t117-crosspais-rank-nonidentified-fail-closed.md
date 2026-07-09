---
id: interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed
kind: interpretation
title: "t117/Q-C: the public single-trigger PAIS corpus does NOT identify a cross-trigger pathway-response rank at its operating point — descriptive R (strict 2 / sensitivity 3) is reported fail-closed (no t116-grid verdict); GWS/FM read-across partially-recovered-indeterminate; the low-power ceiling is now DEMONSTRATED from data, not only simulated"
status: active
source_refs:
  - results/t117-crosspais-rank/rank/strict.rank.json
  - results/t117-crosspais-rank/rank/sensitivity.rank.json
  - results/t117-crosspais-rank/calibration/calibration.json
  - results/t117-crosspais-rank/artifact/strict.adjudicated.json
  - results/t117-crosspais-rank/specificity/gws_fm.json
related:
  - task:t117
  - plan:0010-crosspais-pathway-response-rank-estimation
  - question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
  - question:0001-shared-molecular-signature-across-triggers
  - hypothesis:0001-shared-dysregulated-attractor
  - interpretation:0037-t116-power-bias-floor-shared-axis-sim
  - interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
  - interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
  - dataset:gse221921-fibromyalgia-pbmc
created: "2026-07-09"
updated: "2026-07-09"
input: "Uniform re-computation across the strict (1153×7 WB/PBMC) and sensitivity (10-column) cross-PAIS pathway×contrast matrices (Snakemake workflow code/workflows/t117-crosspais-rank/; DE→fgsea over a pinned Hallmark∪Reactome universe, NES pooled only at the gene-set level, expression never merged). Reads: the rank battery + structural co-primary (rank/*.rank.json), the Stage-3c t116 calibration (calibration/calibration.json), the artifact/compartment adjudication (artifact/strict.adjudicated.json), and the WP4b non-infectious GWS/FM specificity read-across (specificity/gws_fm.json). This is a rank/subspace-geometry estimand, NOT an empirical test of hypothesis:0001; R is a design parameter, not the verdict."
workflow_run: "t117-crosspais-rank"
prior_interpretations:
  - interpretation:0037-t116-power-bias-floor-shared-axis-sim
  - interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
relations:
  - predicate: "sci:amends"
    target: "interpretation:0037-t116-power-bias-floor-shared-axis-sim"
---

## Verdict

**[~] Fail-closed — the corpus does not identify a cross-PAIS pathway-response rank at its operating point, so NO t116 R-regime-grid verdict is emitted.** The strict WB/PBMC matrix (7 columns, 5 triggers) yields a descriptive rank point estimate **R = 2** (consensus of parallel-analysis 2 / BiCV-SVD 5 / split-half 1; estimator disagreement range 4), sensitivity (10 columns) **R = 3** — but the **Stage-3c calibration FAILED on two independent grounds** (`calibration.json: pass=false`), so these R values are **descriptive geometry only** and are NOT placed on the `interpretation:0037` t116 grid (Key decision 6: the grid bridge must be validated, not assumed).

The headline t117 deliverable is therefore **not an R value** but the **empirically demonstrated identification ceiling**: the real matrix's off-diagonal pairwise concordance is **mean −0.064, SD 0.249 over 21 pairs** — the mean is *at or below* the sampling floor `1/√(P−1) = 0.033`, so a t116 shared-axis structure injected at the matched concordance is negligible (κ→0) and **no injected rank is recovered** (R=2→R̂=0, R=4→R̂=0). This is the design-level low-power ceiling of `interpretation:0037` **confirmed from real data** — and it is the answer to that interpretation's own **Q-C** ("estimate the real cross-PAIS repertoire rank from existing single-trigger deposits").

The GWS/FM non-infectious read-across (WP4b, `exploratory_flagship`) returns **`partially_recovered_indeterminate`**, and the artifact/compartment adjudication returns **`interpretation_status: limited_or_nonarbitrating` (`artifact_controls_pass=false`)** — both consistent with, and consumed under, the fail-closed reading.

## Findings Summary

- **No identifiable low-rank shared axis at the corpus operating point (primary).** Structural co-primary: off-diagonal concordance mean **−0.064** (≤ floor 0.033), SD **0.249**, pairs spanning **−0.49 … +0.38**. This is a **heterogeneous ± (finite-repertoire-like) structure, NOT a single homogeneous shared axis** — precisely the `question:0017` null that mean-concordance is blind to, and the regime `interpretation:0037` flagged as non-arbitrating at achievable arm counts. *(strong, discriminating)*
- **Descriptive R = 2 (strict) / 3 (sensitivity), reported fail-closed.** The SVD/parallel-analysis rank estimator does not cleanly recover an injected rank at this corpus **width** (K=7): even on a clean rank-R signal at strong concordance, R=2 is only weakly recovered and **CI-under-covered (0.54 < target)**, R=4 is not recovered, R≥8 is non-identifiable (R≥K). The SVD-rank→t116-grid substitution (review Finding B) is **not licensed at K=7**. *(strong)*
- **Two independent grounds for no grid verdict.** (i) estimator-vs-corpus-width limit (above); (ii) corpus-at-operating-point non-identification (concordance ≤ floor). Ground (ii) holds regardless of the estimator and is the DEMONSTRATED ceiling. *(strong)*
- **GWS/FM read-across: partially-recovered-indeterminate.** Fibromyalgia PBMC RNA-seq (`GSE221921`, 96/93) projects **0.045** of its variance onto the strict PAIS rank-2 subspace — above its empirical row-permutation null (p=0.0005, 2000 draws) but only **0.185× the trigger-weighted leave-one-trigger-out PAIS ceiling (0.24)**. Neither cleanly infection-specific nor a full generic-sickness manifold. The ceiling is itself heterogeneous (per-trigger 0.11 SARS-CoV-2 / 0.27 PI-ME/CFS / 0.35 Lyme) and **under-identified** (`trigger_loo_identifiability_pass=false`: 3 triggers → 2-trigger references). *(exploratory_flagship — one non-infectious column; panel queued)*
- **Artifact/compartment controls FAIL.** `artifact_controls_pass=false` → `limited_or_nonarbitrating`: platform invariance untestable (single platform per column), compartment invariance not established, and the naive shared subspace does **not** persist in case-vs-recovered (0.09 < 0.30). No set-based negative-control / artifact floor was subtracted. *(strong constraint on any biological reading)*

## Evidence Quality

**Moderate for the design/identification conclusion; low (exploratory) for the descriptive R and the GWS/FM read-across.** The identification-ceiling conclusion rests on a pre-locked, calibrated simulation (Stage-3c, t116 generative model) plus the real matrix's own concordance geometry — both robust and mutually reinforcing. The descriptive R is a rotation-invariant estimator battery run with pinned seeds and reported with genuine uncertainty (disagreement range 4, CI under-coverage disclosed); it is honest but deliberately **not** load-bearing. The GWS/FM column is a single flagship deposit (the rest of the admissible panel is queued replication) projected onto a weakly-identified subspace, so it is `exploratory_flagship`, explicitly not `validated_specificity`.

## Data Quality Checks

- **NES pooled only at the gene-set level** over one pinned Hallmark∪Reactome universe; expression never merged across datasets (a Non-Goal honored). Strict = WB/PBMC bulk only; sorted deposits held as a separate stratum; the GWS/FM column passed the **same** admissibility gates as the primary corpus.
- **Reproducibility:** config-driven, per-estimator seeds pinned (`master_seed`, parallel-analysis permutation, CV-SVD fold, split-half, bootstrap), pinned+checksummed acquisition, `origin.json` provenance sidecars; canonical results regenerated via the Snakemake rules.
- **Complete-case rows:** strict structural co-primary on 905 complete-case gene sets (0 dropped-NA); GWS/FM projection on 805 rows usable (PAIS-complete AND FM non-NaN).
- **Calibration limitation disclosed:** the t116 shared-axis caricature produces positive-mean concordance only; the real matrix's ~0-mean/high-SD heterogeneous structure is a finite-repertoire regime the caricature does not reproduce — which is itself the point (the corpus is in the harder null).

## Proposition-Level Updates

- The proposition "a low-rank shared cross-PAIS pathway-response axis is recoverable from public single-trigger blood-transcriptome deposits" is **downgraded**: not recoverable at this corpus's operating point (concordance ≤ identification floor). The obstacle is **corpus-intrinsic** (signal at/below the sampling floor over K=5 triggers / 7 columns), not a tuning or estimator choice.
- "Per-arm N is the binding lever" — **further disconfirmed from the data side**: the binding constraint is arm count / trigger count and feature-space resolution, consistent with `interpretation:0037`; the strict corpus fails on trigger count and signal level, not sample depth.

## Hypothesis-Level Implications

- **`hypothesis:0001` (shared dysregulated attractor): neither licensed nor blocked.** R is a design parameter here, not a test of h0001. The result says the *public single-trigger corpus cannot arbitrate* shared-attractor vs finite-repertoire — the heterogeneous ± concordance is exactly the `question:0017` deflationary null, but the corpus lacks the identification power to distinguish it from a diffuse high-rank shared mechanism. Promotion of h0001 remains held against the q0017 bundle.
- **`question:0017` (deflationary alternatives): mildly favored descriptively, not decisively.** The finite-repertoire-like ±-heterogeneous geometry is what q0017 predicts; but under the demonstrated low power this is a *descriptive lean*, not an adjudication.

## Evidence vs. Open Questions

- **Q-C (was open in `interpretation:0037`) — now ANSWERED from data:** the real cross-PAIS repertoire, as sampled by this corpus, sits **at/below the identification floor** — a diffuse/heterogeneous regime, no recoverable low-rank shared axis at K=5 triggers. This is the cheapest-possible probe `interpretation:0037` asked for, and it returns "the public single-trigger route cannot settle the R regime." Recorded as a `sci:amends` edge onto 0037.
- **q0050 GO/NO-GO consequence:** **reinforced, unchanged in direction.** The t117 real-data ceiling confirms the simulation: fund only a **K≥3, ~1000-set-feature, structural-statistic, full-recovery-control** harmonized design. The public single-trigger corpus is **not** a substitute and cannot be made one by adding more such deposits (the ceiling is signal-level, not count-level, at fixed trigger diversity). The t035 two-cohort route stays closed.
- **Two-matrix verdict rule applied:** the q0050-grade R is the **strict** matrix (R=2, regime band `low`, `artifact_controls_pass=false`); the **sensitivity** R=3 (K=10, includes the ME/CFS-sensitivity columns) is **hypothesis-generating only**. The adjacent "does the ME/CFS-inclusive matrix change the rank" question is answered separately and does not feed the q0050 grade.

## New Questions Raised

- **Q-F (empirical, P3):** Would a **purpose-recruited K≥3 harmonized** cohort (COVID-19 + influenza + EBV, ~1000-set features) lift the off-diagonal concordance above the identification floor, or is the ≤-floor concordance a property of PAIS pathway-response geometry itself (genuinely diffuse)? This is the q0050 cohort's core deliverable and the only lever left after t117.
- **Q-G (methodological, P3):** Does the GWS/FM `partially_recovered_indeterminate` verdict survive the queued replication panel (`GSE67311` WB-microarray FM, `E-MEXP-2069` / `GSE286345` GWI, `GSE182503` IEI) and the reverse projection (build U from ≥2 non-infectious columns, project PAIS)? Only then does the infection-specificity read-across become `validated_specificity`.

## User Questions

- **Finding-E scope decision (recorded):** with Stage-3c confirming the low-power ceiling, was the full descriptive staging (WP1b–WP4b) worth its cost, or should the deliverable have been the WP1 finding + scoped calibration alone? **Decision: the full descriptive analysis is retained and reported as the t117 deliverable, but framed as a DEMONSTRATION of the identification ceiling plus supporting non-grid readouts — not a grid verdict.** Rationale: the descriptive pass produced three decision-relevant results the lean alternative would have missed — (a) the empirical Q-C answer (corpus concordance ≤ floor), (b) the GWS/FM specificity read-across, (c) the artifact/compartment adjudication — each of which sharpens the q0050 go/no-go. **No further staging or harmonization of the public single-trigger corpus is warranted**: the ceiling is corpus-intrinsic, so additional public deposits at fixed trigger diversity cannot lift it. The next real lever is the purpose-built K≥3 cohort (q0050), not more public data.

## Limitations & Residual Uncertainty

- **Fail-closed is a "cannot decide," not a "there is nothing."** t117 shows the public corpus cannot identify a rank; it does **not** establish that no shared axis exists. A genuine diffuse/high-rank shared mechanism and a q0017 coincidental finite repertoire are **observationally equivalent** at this corpus's signal level (the `interpretation:0037` identifiability ceiling, Q-D).
- **Descriptive R is width- and estimator-fragile.** K=7 is below the width at which the battery cleanly recovers even a clean injected rank; the reported R=2/3 should never be quoted as "the cross-PAIS rank."
- **GWS/FM is one deposit against a weak, under-identified ceiling.** The `0.185×` figure is read against a trigger-LOO ceiling built from 2 triggers (below the K≥3 floor); it is directional context, not a calibrated specificity fraction.
- **Artifact floor not subtracted.** With `artifact_controls_pass=false`, even the descriptive R is not artifact-adjudicated; any low-rank appearance could carry residual platform/composition structure.
- **PACVS read-across is a note-only gap** (no admissible public deposit); gates were not relaxed.

## Updated Priorities

- **Amend `interpretation:0037`** (via the `sci:amends` edge from this doc): Q-C is answered from real data (corpus concordance ≤ identification floor); and land the **scoped-"any N"** correction (Key decision 5) — the 2-arm and mean-concordance non-arbitration is genuinely *any N* (structurally undefined / blind by construction), while the **high-rank / finite-repertoire non-arbitration is scoped to achievable arm counts under this pathway-vector structural-test family (≤6 arms simulated), not literally any N**.
- **Amend `question:0050`** with the same scoped wording and the t117 empirical confirmation of the low-power ceiling; the go/no-go stays **fundable-with-conditions**, now with real-data backing for the "public data cannot substitute" clause.
- **Do not** place any t117 R on the t116 grid, run the sensitivity R into the q0050 grade, or open further public-corpus staging. The next investment is the q0050 K≥3 harmonized cohort or the WP4b queued-replication panel — not this corpus.
