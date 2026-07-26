# Pipeline Review: plan:0009 Task 3 — Naive MR comparator

- **Reviews:** `doc/plans/2026-07-05-plan0009-task3-naive-mr.md`
- **Parent plan:** `entities/plans/0009-wave1-mr-hormone-pilot.md` (review: `doc/reviews/0009-wave1-mr-hormone-pilot-pipeline-review.md`)
- **Predecessor increment:** `doc/plans/2026-07-04-plan0009-task2-hormone-instruments.md`
- **Date:** 2026-07-05
- **Overall:** PASS (3 minor recommendations; none blocking)

## Summary

A tight, well-scoped implementation companion that reuses the proven `plan:0007`
`harmonize_estimate.R` mechanics and the Task-2 `r-mr` env, with correctly
identified adaptations (EA/OA mapping, hormone estimand, KD1/KD3 + overlap
labels, six-way fan-out with an eligibility guard). Integration boundaries were
checked against the **real** Task-2 sidecar schema and outcome file and hold.
The four findings from the prior review pass are incorporated. Remaining items are
minor traceability/quality-flag improvements worth folding in before
implementation, not blockers.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | N/A | Inherited from parent `plan:0009` (passed). |
| Assumption audit | PASS | Overlap-bias assumption now labelled; direction of naive↔MRlap delta deferred to Task 5 (note). |
| Data availability | PASS | Inputs staged/gated under `plan:0009`; instruments derived by Task 2. |
| Identifiability | PASS | instruments+outcome → harmonise → estimate → manifest fully connected. |
| Reproducibility | PASS | WM seed + **now-enforced** `nboot`; TwoSampleMR 0.7.9 pinned via Task-2 sentinel; `r-mr` env reused. |
| Validation criteria | PASS | Real-data resource via `benchmark:`; guard fixture test added; estimator-output hard-stop. Minor: no harmonisation drop-rate flag. |
| Scope check | N/A | Inherited from parent `plan:0009` (passed). |
| Integration boundaries | PASS | EA/OA + `eligible_for_mr`/`eligibility_reasons` verified against real Task-2 output; outcome `pick()` resolver unchanged from the same-file plan:0007 use. |
| Manifest completeness | WARN | `naive_mr_results.json` lacks explicit dataset `entities` cross-refs; full `datapackage.json` rightly deferred to Task 5. |

## Detailed Findings

### Dimension 9 — Manifest completeness (WARN, minor)

`naive_mr_results.json` carries `plan`/`task` but no dataset `entities` list. The
full reproducible bundle (`datapackage.json` + provenance DAG) is explicitly
**Task 5's** deliverable per `plan:0009`, so a full manifest here is correctly out
of scope. **Recommendation:** add a cheap `"entities": ["dataset:ruth-2020-shbg-testosterone-gwas",
"dataset:covid19-hgi-longcovid-gwas"]` list to the aggregate manifest now, matching
Task 1's `staging_manifest.json` convention, so the naive results are traceable to
their inputs before Task 5 assembles the bundle.

### Dimension 6 — Validation criteria (PASS, one minor gap)

Real-data scale/resource is covered (the multi-GB outcome stream-extract is
benchmarked for `max_rss` + wall-clock), and the two safety gates are now exercised
by a fixture test rather than spot-checked. **Gap:** `harmonise_data(action = 2)`
can drop instruments (palindromic/ambiguous by EAF); the plan records `n_harmonised`
+ `dropped_snps` (non-silent) but never **flags** a high dropout. A stratum that
loses a large fraction at harmonisation would proceed silently on far fewer SNPs.
**Recommendation:** add a `quality_flags` entry (e.g. `high_harmonisation_dropout`
when `n_harmonised / n_instruments_input < 0.5`), mirroring Task 2's
`below_target_n` quality-flag pattern — informative, not a gate.

### Dimension 2 — Assumption audit (PASS, note)

The naive arm's core known-violated assumption — two-sample MR with **structural
sample overlap** (Ruth 100% UKB × HGI pooling UKB; see plan:0009-wave1-mr-hormone-pilot) biases the estimate toward the
confounded observational association — is now machine-labelled
(`sample_overlap_uncorrected` / `naive_comparator_only`). The plan does not state
the **expected direction/magnitude** of the naive↔MRlap delta, but that is
interpretive and belongs to Task 5's write-up; deferring it is appropriate. No
action required.

### Dimension 8 — Integration boundaries (PASS, note)

Verified against real artifacts: the instrument TSV header is
`SNP chr pos EA OA beta se eaf pval F` (drives the `EA`/`OA` `format_data` mapping),
and the Task-2 sidecar exposes `eligible_for_mr` (bool) + `eligibility_reasons`
(list) — exactly the guard's contract. **Note (non-blocking):** MR-Egger is
statistically unstable at very low instrument counts; irrelevant for the six real
strata (159–353 instruments, per the task:t089 Task-2 sidecars), but if the graceful path ever admits a 3–5 instrument
stratum, Egger output would be near-degenerate. The plan already frames wide/weak
estimates as informative, so this is acceptable as-is.

## Recommendations

1. **(Dim 9)** Add a `entities: [dataset:ruth-2020-shbg-testosterone-gwas,
   dataset:covid19-hgi-longcovid-gwas]` list to `naive_mr_results.json` for
   input-traceability (cheap; matches Task 1 convention).
2. **(Dim 6)** Add a `high_harmonisation_dropout` quality flag when a large fraction
   of instruments is lost at `harmonise(action=2)`, so a thin post-harmonisation set
   is surfaced, not silent.
3. **(Dim 2/note)** Leave the naive↔MRlap delta-direction discussion to Task 5, as
   planned — no change here.

## Strengths

- Integration boundaries validated against **real** Task-2 output and the actual
  outcome file, not assumed.
- Reproducibility is now airtight: WM seed **and** the previously-decorative `nboot`
  are both enforced and recorded resolved; env + TwoSampleMR pin reused from the
  Task-2 sentinel (no re-resolution drift).
- The eligibility guard + graceful `<3`-harmonised path correctly separate
  "technical fault → hard-stop" from "weak → informative", matching `plan:0009`'s
  Decision criteria, and are now fixture-tested.
- The KD1/KD3 + `sample_overlap_uncorrected` labels make every output
  self-describing as exploratory / non-primary / uncorrected — the naive estimate
  cannot be misread as an overlap-corrected primary result.
- Right-sized: a single probe-scoped increment that stops before MRlap (Task 4),
  preserving the naive↔corrected comparison the design turns on.
