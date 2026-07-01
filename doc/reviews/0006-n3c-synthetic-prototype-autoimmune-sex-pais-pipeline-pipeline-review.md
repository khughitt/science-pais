# Pipeline Review: N3C synthetic-tier prototype (autoimmune × sex × PASC)

- **Reviews:** `plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline`
- **Date:** 2026-07-01
- **Overall:** WARN — no hard blocker to starting **WP0–WP1**, but **two design decisions must be made before WP2** (deterministic matching + shim boundary; and modeling the synthetic slice as a verifiable artifact). Methodology is inherited from `plan:0005` and was not relitigated.

## Summary

The plan is a well-structured design with genuinely good instincts (severity walled off from E1, disclosure-portable outputs, "no coefficient is interpretable" stated three times). The weaknesses are all at **engineering boundaries**, exactly where the user asked to look: the `ohdsi_shim` dual-runtime claim is under-specified and hides a real non-determinism risk in matching; per-stage output schemas/manifests are absent; the dataset entity does not structurally encode the "synthetic slice only" scope; and two WP definitions-of-done ("all eight strata resolve on synthetic data") will mislead. None of these require throwing the plan away — they are edits to WP DoDs plus two decisions to lock before writing `s1_cohort.py`.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | WARN | Windows (45 d, 365 d) inherited from plan:0005/Hill; **SDC threshold unsourced** and provisional |
| Assumption audit | PASS (inherited) | Estimand/confounding locked in plan:0005; the *new* plan:0006 assumption ("one shim = portable") is under-justified → routed to Dim 3/8 |
| Data availability | **FAIL** | `dataset:n3c-recover-longcovid` is `verified: false`, **no `access.exception`**, **no `datapackage`/`local_path`** for the synthetic slice; mixed-tier umbrella entity does not model the consumed public slice |
| Identifiability | PASS | Linear DAG synthetic-OMOP → outputs is fully connected |
| Reproducibility | WARN→FAIL | **No matching seed**, no version pinning (duckdb/spark/statsmodels), no environment lock; idempotency asserted but no mechanism |
| Validation criteria | WARN | Per-WP DoDs present and WP9 has a real scale/resource run (good); but "strata resolve on synthetic data" conflates two different checks |
| Scope check | WARN | `specs/scope-boundaries.md` defers "primary computational pipelines … until past seed stage"; design-only + synthetic is borderline-in (precedent: `plan:0003` pipeline) — flag, don't block |
| Integration boundaries | **FAIL** | Shim distributed↔local handoff undefined; no per-stage output schemas → the crux engineering risk |
| Manifest completeness | WARN | No `datapackage.json` for pipeline outputs; no per-stage schema contract |

## Detailed Findings

Prioritized. **[BLOCKER-WP2]** = must resolve before writing cohort/matching code; **[SHOULD-FIX]** = fold into the WP before its DoD is claimed; **[NIT]**.

### [BLOCKER-WP2] F1 — `ohdsi_shim` is not a free portability guarantee; matching is non-deterministic across engines
One abstraction over duckdb (single-node, deterministic row order) and Foundry/PySpark (distributed, **non-deterministic ordering unless a total order + seed is imposed**) does **not** make "the same code produce the same result." 1:5 matching selects/orders rows; on Spark the matched sets can differ run-to-run and differ from duckdb. Secondary divergences: SQL-dialect gaps (date arithmetic, `QUALIFY`, window fns), null-in-join / `NOT IN` semantics, and the fact that **`s6_estimate.py` cannot be Spark code at all** — log-binomial/RERI run in statsmodels on a *collected* pandas frame. So the shim boundary is real and must be drawn: heavy joins (s1–s5) in a SQL-portable layer, **`COLLECT` to pandas at a defined aggregation point**, estimation local in both environments.
- **Fix:** (a) specify a **deterministic matching algorithm** — total-order sort on a stable key + seeded tie-break (hash of person_id + seed), tested for cross-engine identity on a shared fixture; (b) document the **shim contract** explicitly: which stages are set-based/distributed vs which run on collected pandas, and where the collect boundary is; (c) restrict the portable layer to a **known-common SQL subset** (or use an OHDSI-style templated SQL dialect translator) rather than raw duckdb/Spark SQL.

### [BLOCKER-WP2 / data-governance] F2 — the synthetic slice is not modeled as a verifiable, stageable artifact
The design's scope discipline ("synthetic slice only, enclave siblings out of scope") is **only in prose**. The dataset entity is a single `access.level: mixed`, `verified: false` record with no `access.exception`, no `siblings`, and no `datapackage`/`local_path`. Per the review's Data-Availability gate this is a FAIL, and it means "no umbrella-entity leakage" is not *structurally* guaranteed — nothing stops a later stage from pointing at a Limited-tier table.
- **Fix (this is literally WP0's job — do it first):** either (a) split a granular sibling `dataset:n3c-recover-longcovid-synthetic` with `access.level: public/registration`, `datapackage`/`local_path` to the acquired synthetic OMOP package, and `verified: true` + `verification_method` + `last_reviewed`; **or** (b) add an `access.exception: {mode: scope-reduced, decision_date, followup_task: t079}` to the existing entity plus a `local_path` to the synthetic package. Option (a) is cleaner and matches the layout-v3 granular-sibling pattern.

### [SHOULD-FIX] F3 — "each stratum resolves to ≥1 concept on synthetic data" is the wrong check (and will misfire)
Synthetic N3C is statistically generated: rare autoimmune concepts (myositis, vasculitis) may have **zero synthetic patients** for reasons unrelated to codelist correctness, and concept co-occurrence is not preserved. A DoD keyed on patient hits will **falsely fail** valid codelists and **falsely reassure** on the ones that do hit.
- **Fix:** decouple two checks — (i) **vocabulary validity**: every code resolves in the OMOP `CONCEPT`/`CONCEPT_ANCESTOR` tables (portable, meaningful); (ii) **patient hit count on synthetic data**: recorded as a *mechanism smoke-test only*, explicitly allowed to be zero. Real cell counts are a WP0-punch-list / enclave item, not a synthetic acceptance gate.

### [SHOULD-FIX] F4 — WP1 partially depends on BC-3 for four strata; the DoD hides it
WP1 claims all eight strata are bundled, but Sjögren / vasculitis / myositis / autoimmune-thyroid codelists are `[UNVERIFIED]` (BC-3 open). WP1 *can* legitimately ship **draft** lists for the confirmed strata (SLE/RA/IBD/MS) with provenance + checksums, but it cannot honestly claim the four unconfirmed ones are done.
- **Fix:** WP1 DoD = "confirmed strata bundled as draft; the four unconfirmed strata **stubbed with an explicit BC-3 dependency marker** in `BUNDLE.lock`." Bundle `status: draft-unreviewed`; BC-3 sign-off gates *use for a real estimate*, not prototyping. (This keeps the WP1→BC-3 dependency visible instead of silently absorbed.)

### [SHOULD-FIX] F5 — no per-stage output contract / manifest → drift risk (the user's Q6)
Stages are described as scripts with prose DoDs but **no declared output schema** (grain, key columns, dtypes) and **no `datapackage.json`** for the outputs. This is exactly how multi-stage pipelines drift.
- **Fix:** add a per-stage **output-schema contract** (a small schema file or a `manifest.yaml` per stage declaring table grain + columns + join keys), validated at stage exit; emit a `datapackage.json` for the final output tables (Dim 9). Make s1→s7 boundaries assert their upstream's declared schema on entry.

### [SHOULD-FIX] F6 — the E1 severity-exclusion guard must assert at the model-input level, not the join level (the user's Q7)
"Fails if severity is joined into the E1 set" is weaker than the claim needs. Severity can leak via a derived covariate or a hospitalization-derived proxy without a literal join.
- **Fix:** the guard asserts on the **exact feature/column set handed to the E1 estimator** — `assert severity_cols.isdisjoint(set(E1_design_matrix.columns))` — **and** maintains a small denylist of severity-derived proxies checked against the E1 design matrix. Test it with a red-team fixture that deliberately tries to sneak a severity proxy in and confirms the guard trips.

### [SHOULD-FIX] F7 — "one output layer clears both N3C and OpenSAFELY SDC" only holds under the *stricter* policy
N3C and OpenSAFELY use **different** small-cell rules (N3C commonly masks counts below a larger threshold; OpenSAFELY = redact ≤7 then round-to-5). A single layer is portable only if it applies the **most conservative** of the target policies (max threshold, then rounding), or is parameterized per target.
- **Fix:** `disclosure.yaml` carries per-target profiles; default profile = **max(threshold), coarsest rounding**; mark the N3C value **PROVISIONAL** pending rule confirmation (WP0). Keep the threshold **only** in config — the suppression **test must be parameterized** (assert the mechanism, never a magic N). *(This makes building the SDC layer before confirming the exact N3C number safe — F-answer to the user's Q4: yes, safe, because the value is config and provisional and the test is mechanism-level.)*

### [SHOULD-FIX] F8 — reproducibility primitives unspecified
No seed (matching!), no pinned versions, no environment lock, and idempotency is asserted without a mechanism.
- **Fix:** pin the matching **seed** in `windows.yaml`/config; pin duckdb/PySpark/statsmodels versions; define idempotency as "deterministic given `BUNDLE.lock` + `windows.yaml` + input snapshot id"; record the input snapshot id in outputs.

### [NIT] F9 — temporal-window boundary rules under-specified
Same-day events (autoimmune dx *on* index date; severity *on* day 0; reinfection inside the acute window) need explicit inclusive/exclusive rules, or exposure<severity<outcome can be silently violated at the edges.
- **Fix:** state boundary conventions in `windows.yaml` (e.g. exposure strictly `< index`; severity in `[index, index+28d]`; PASC window `≥ index+Nd`) and unit-test the edges.

### [NIT] F10 — scope-boundary note
`specs/scope-boundaries.md` defers primary computational pipelines until past seed stage. This plan is design-only + synthetic (no real analysis), and `plan:0003` set precedent for design-stage pipeline plans at seed stage — so it reads in-scope, but the execution of a *real-tier* run later would cross the line and should be re-checked against scope at that point.

## Recommendations

1. **Before WP2:** lock F1 (deterministic matching + explicit shim/collect boundary) and F2 (model the synthetic slice as a verifiable artifact — do it as WP0's first act). These are the two that get expensive after code exists.
2. **Fold into the relevant WP DoDs before claiming them done:** F3 (vocab-vs-patient check split), F4 (WP1 draft + BC-3 stubs), F5 (per-stage schema + datapackage.json), F6 (guard at model-input level), F7 (strictest-policy SDC + provisional value).
3. **Config hygiene:** F8 (seed + version pins + idempotency definition), F9 (window boundary rules).
4. **Proceed:** WP0–WP1 can start now with F2/F3/F4 folded in; **do not write `s1_cohort.py` (WP2) until F1 is decided.** BC-3 codelist work can run in parallel but WP1's shape (F4) should be fixed first.

## Strengths

- Severity structurally separated from E1 (F6 sharpens an already-correct instinct).
- "Synthetic run validates plumbing, never a coefficient" stated repeatedly — the single most important framing, and it's right.
- Disclosure-portable-from-stage-one and a versioned, checksummed concept-set bundle are good hygiene.
- WP9 includes a real scale/resource run rather than declaring done on fixtures.
- Vaccination built both adjusted and unadjusted — carries the plan:0005 caveat into code.
