---
reviews: doc/plans/2026-07-05-plan0009-task4-mrlap.md
related:
  - plan:0009-wave1-mr-hormone-pilot
  - task:t089
---

# Pipeline Review: plan:0009 Task 4 — Canonicalization adapter + MRlap overlap correction

- **Reviews:** `doc/plans/2026-07-05-plan0009-task4-mrlap.md` (@ e4cfe31)
- **Date:** 2026-07-05
- **Overall:** **WARN** — execution-ready for its stated *exploratory-probe* goal
  under the KD1/KD3 ceilings. Two findings should land before any corrected
  estimate is *interpreted* (Dim 2 ancestry-mismatch caveat; Dim 6 LDSC-sanity
  floor); the rest are minor tightenings that can be folded during implementation.
  Consistent with the parent plan's WARN posture. The five prior findings
  (scale, `int_crosstrait`, transitive pins, temp-dir, IV floor) are materially
  addressed.

## Summary

A well-scoped implementation companion for the one increment carrying a genuinely
new mechanism (MRlap + its GenomicSEM cross-trait-LDSC engine). The highest-risk
integration seam — the canonicalization adapter's output schema vs MRlap's input
contract — was verified against the pinned MRlap source and is **correct**
(`a1`=effect/`a2`=other, `rsid`/`chr`/`pos`/`beta`/`se`/`N`, case-insensitive; MRlap
demands **total** N on the **observed** scale, exactly what the plan injects). The
remaining findings are scientific-interpretation guards (an ancestry-mismatch in
the outcome's LDSC step; a degenerate-LDSC-fit gap) plus small integration/ops
tightenings — none blocking for an exploratory, ancestry-flagged, non-primary probe.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | PASS | N/A-inherited from parent; Task-4 params all sourced — six Ruth N from GWAS Catalog (internally consistent), outcome total-N = Σ per-ancestry `sample_size`, MRlap/GenomicSEM/TwoSampleMR/ieugwasr pinned. |
| Assumption audit | **WARN** | **New:** MRlap's cross-trait LDSC uses the **EUR** `eur_w_ld_chr` reference against the **European-dominant (~85–90%) multi-ancestry** outcome → LD-reference/sample mismatch makes the outcome h²/cross-trait-intercept (hence the correction magnitude) ancestry-approximate. Not caveated. |
| Data availability | PASS | All inputs staged on disk + gate-passed at Task 1; `consumed_by` carries `plan:0009` + `task:t089` on all four datasets. Backlink uses the parent `plan:0009` id (not the per-doc stem) — consistent with the Task 2/3 precedent. |
| Identifiability | PASS | raw sumstats + LDSC ref → canonicalize → MRlap → aggregate → `mrlap_results.json`, fully connected; estimand deliberately non-primary (KD1) and the plan says so. |
| Reproducibility | PASS | Strong — MRlap+GenomicSEM `GithubSHA1` + TwoSampleMR/ieugwasr versions pinned & asserted; MR pruning/threshold params pinned; no Python `ldsc`. **Minor:** MRlap determinism (no seed) asserted only implicitly. |
| Validation criteria | **WARN** | Genome-wide MRlap scale/resource run is captured (`benchmark:` max_rss+wall-clock) — good. **Gaps:** (a) no LDSC-plausibility floor (a degenerate h²≈0 / \|rg\|>1 fit yields a "finite but garbage" correction that passes the non-finite hard-stop); (b) the ~4.4 GB canonicalization step has no `benchmark:`. |
| Scope check | PASS | N/A-inherited; within D-005/D-006 and `entities/specs/0001-scope-boundaries-for-health-post-acute-infection.md` (Ruth vehicle, same HGI outcome, no FinnGen). |
| Integration boundaries | PASS | **Verified:** MRlap input schema matches the adapter (`a1`=alt/effect, `a2`=ref, `rsid`/`N`/`beta`/`se`/`chr`/`pos`, case-insensitive; **total N, observed scale**). **Minor:** the naive-manifest join path (extract IVW from Task-3 `methods[]`) is underspecified. |
| Manifest completeness | WARN | `mrlap_results.json` carries params + `entities` + `resource` but is **not** a `datapackage.json` — deliberately deferred to Task 5, consistent with Task 3. |

## Detailed Findings

### Dim 2 — Assumption audit (WARN): EUR LD reference vs multi-ancestry outcome
MRlap runs cross-trait LDSC internally with the **EUR** `eur_w_ld_chr` reference.
The exposures (Ruth, European UKB) match it; the **outcome** `GCST90454541` is a
**European-dominant but ~10–15% non-European** meta (dataset:covid19-hgi-longcovid-gwas). LDSC assumes the LD reference
matches the GWAS sample, so the **outcome** h², single-trait intercept, and the
**cross-trait intercept** (`int_crosstrait`) — the very quantity driving the
overlap correction — are **ancestry-approximate**. This is a distinct, mechanistic
compounding of the KD1 flag (it bites the *correction machinery*, not just the
interpretation). **Recommend:** add a labelled caveat (e.g.
`ldsc_ancestry_mismatch: true` with a one-line note) to the per-stratum + aggregate
manifests, and state in Task 5 that the correction magnitude inherits an
outcome-side ancestry approximation. (The **total-N = 1,100,445** injection remains
correct: it is the precision-N of the multi-ancestry meta betas MRlap consumes.)

### Dim 6 — Validation (WARN): no LDSC-plausibility floor
The `run_mrlap.R` hard-stop rejects **non-finite** corrected estimates and 0-IV
runs, but a **degenerate/ill-converged LDSC fit** (h²_exp or h²_out ≤ 0, \|rg\| > 1,
or an implausibly large `int_crosstrait`/SE) can still produce a *finite* corrected
effect that silently passes. That is exactly the "green but wrong" failure the
scale/resource ethos warns about, one level up. **Recommend:** record the LDSC block
(already planned) **and** raise non-gating `quality_flags` when
`h2_exp <= 0 || h2_out <= 0 || abs(rg) > 1` (or MRlap emits a low-h²/convergence
warning) — a flag, not a gate (mirrors Task 2's `below_target_n` / Task 3's
`high_harmonisation_dropout` pattern), so a degenerate fit is surfaced beside the
number rather than propagated into it.

### Dim 6 — Validation (minor): canonicalization step has no resource capture
`run_mrlap` carries `benchmark:`, but `canonicalize_exposure`/`canonicalize_outcome`
(streaming ~4.4 GB of gz from the task:t089 staged payloads) do not. Memory is O(1) by streaming so RSS is not the
risk, but wall-clock on real data is worth a line. **Recommend:** add `benchmark:`
to the two canonicalize rules (cheap; matches the plan's own real-data-resource
posture).

### Dim 8 — Integration (minor): naive-manifest join underspecified
`aggregate_mrlap.py` pulls `comparison.naive_ivw {b,se,pval,or,nsnp}` from Task-3's
`naive_mr_results.json`, whose per-stratum record stores methods as a list
(`methods: [{method: "Inverse variance weighted", b, se, pval, or, nsnp}, …]`).
**Recommend:** name the exact extraction path (match `method == "Inverse variance
weighted"`; `nsnp` from that entry) and **hard-stop** if the IVW entry is
absent/renamed for a stratum — so the join fails loud rather than silently emitting
a null naive column.

### Dim 6 / ops (minor): pre-seed the naive manifest in the worktree
`aggregate_mrlap` depends on `NAIVE_MR_MANIFEST`, but `results/` is **not**
symlinked, so a fresh worktree lacks `naive_mr_results.json` → Snakemake rebuilds
it. The plan calls this "cheap re-aggregate," which holds **only** if the per-stratum
naive outputs on shared `/data` are mtime-fresh; an mtime skew would trigger a full
naive re-estimate (needing the **r-mr** env mid-run). **Recommend:** before Step 10,
copy `results/wave1-mr-hormone-pilot/naive_mr_results.json` from the main checkout
(it exists there from Task 3) into the worktree's `results/`, so the dependency is
satisfied deterministically with no naive rebuild.

### Dim 5 — Reproducibility (minor): assert MRlap determinism
MRlap's corrected-effect SE is analytic (no bootstrap), so the run should be
deterministic — but the plan doesn't state it. **Recommend:** a one-line
determinism note (or a run-twice-identical spot-check in Step 11); set/record a seed
only if the pinned MRlap turns out to use any sampling.

## Recommendations

1. **Before interpreting results:** add the `ldsc_ancestry_mismatch` caveat (Dim 2)
   and the LDSC-plausibility `quality_flags` (Dim 6) — the two findings that bear on
   whether a corrected number is trustworthy.
2. **During implementation (cheap):** name the naive-IVW extraction path + hard-stop
   (Dim 8); pre-seed the naive manifest into the worktree (ops); add `benchmark:` to
   the canonicalize rules and a determinism note (Dim 6/5).
3. **Keep the adapter schema as written** — it is verified against the pinned MRlap
   input contract; do not "improve" the column names.

## Strengths

- The single most dangerous seam (adapter schema → MRlap munge, incl. allele
  convention and total-vs-effective N) is **verified correct against the pinned
  source**, not assumed.
- The five prior findings are folded in cleanly; the scale reversal in particular
  turns a wrong "same-scale" claim into a precise two-axis (scale **and** instrument
  set) non-identity, with the one genuinely clean delta (MRlap observed→corrected)
  correctly isolated.
- Reproducibility is unusually tight for a GitHub-only tool stack: commit SHAs **and**
  transitive-engine versions pinned and asserted, closing the drift path MRlap's own
  `Imports` would otherwise leave open.
- The KD1/KD3 ceilings are carried as machine-readable labels that explicitly state
  overlap-correction does **not** lift them.
