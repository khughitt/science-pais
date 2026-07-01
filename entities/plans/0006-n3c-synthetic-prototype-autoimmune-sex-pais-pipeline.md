---
id: "plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline"
type: "plan"
title: "Pipeline (prototype): N3C synthetic-tier skeleton for the autoimmune × sex × PASC estimand (t079/BC-2)"
status: "active"
created: "2026-07-01"
updated: "2026-07-01"
plan_kind: "pipeline"
related:
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - task:t079
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - dataset:n3c-recover-longcovid
  - paper:Hill2022
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
---

# Pipeline (prototype): N3C synthetic-tier skeleton for the autoimmune × sex × PASC estimand (t079/BC-2)

> Execution orchestration for `plan:0005`. This is a **prototype/design plan**, not a
> production run. The methodological readiness checks (estimands, independent unit, power
> floor, bias-vs-variance, sensitivity arbitration) are **already settled in
> `plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan`** and are **not
> re-decided here** — this plan only builds the runnable, enclave-portable skeleton.

## Purpose

Stand up the full analysis pipeline on the **N3C open synthetic tier** so that every stage
of `plan:0005` — cohort → exposure strata → covariates → severity mediator → PASC outcome →
E1/E2/E3 estimation → disclosure-portable diagnostics — **runs end-to-end and is portable to
the N3C real (Limited/enclave) tier** without logic changes. The guiding principle: **the
synthetic run validates plumbing, never a coefficient.** Synthetic N3C data carries no real
exposure–outcome signal, so no estimate produced here is interpretable; the deliverable is a
*correct, portable, disclosure-safe* pipeline plus a punch-list of what only the enclave can
confirm.

## Scope decomposition

**In scope (synthetic tier, runnable now):**
- Pipeline code for all six stages, written against OMOP CDM so it runs identically on
  synthetic and enclave data.
- A versioned concept-set / codelist bundle (autoimmune strata, PASC, severity, utilisation
  windows) as an immutable input.
- Estimand plumbing: E1 total, E2 controlled-direct, optional E3, sex × stratum interaction
  (RERI + multiplicative), site frailty.
- Disclosure-control-aware output layer (small-cell suppression + rounding) proven on
  synthetic outputs.

**Out of scope (deferred, still gated):**
- **Any interpretable estimate** — requires the real tier (reverse-causation-free signal).
  Deferred to the enclave run once N3C DUA/Limited access clears (remainder of BC-2).
- The **N3C real/Limited and De-identified tiers** — the mixed-access siblings of
  `dataset:n3c-recover-longcovid`; this plan consumes **only the open synthetic slice**.
- **OpenSAFELY replication** — BC-5 phenotype work first (`interpretation:0031`).
- Final codelist clinical review for the rarest strata — parallels **BC-3**; here we build
  the *mechanism*, not the clinically-signed-off list.

## Architecture

Portable OMOP-first layout; the same `src/` runs local-synthetic and enclave-Spark behind a
thin execution shim.

```
n3c-autoimmune-sex-pais/                      NEW  (prototype repo / enclave code-workbook mirror)
├── config/
│   ├── windows.yaml                          NEW  index/lookback/acute/PASC window offsets (versioned)
│   └── disclosure.yaml                        NEW  SDC params (suppress ≤ n, round-to-m) — enclave + OpenSAFELY portable
├── concept_sets/                              NEW  the versioned exposure/outcome/severity bundle (BC-1 input)
│   ├── autoimmune/{sle,ra,sjogren,vasculitis,myositis,ibd,ms,ai-thyroid}.csv   NEW
│   ├── pasc.csv  severity.csv  utilisation.csv                                 NEW
│   └── BUNDLE.lock                            NEW  checksums + source provenance (immutable)
├── src/
│   ├── io/ohdsi_shim.py                       NEW  one interface; duckdb(local-synthetic) | spark(enclave)
│   ├── s1_cohort.py                           NEW  index event, inclusion, 1:5 matching (+weighting alt)
│   ├── s2_exposure.py                         NEW  dated pre-index strata + pooling hierarchy
│   ├── s3_covariates.py                       NEW  age/sex/era/vax/comorbidity/utilisation/prior-infection
│   ├── s4_severity.py                         NEW  POST-index dated mediator (hosp/ICU/oxygen)
│   ├── s5_outcome.py                          NEW  computable PASC phenotype (U09.9 + phenotype)
│   ├── s6_estimate.py                         NEW  E1/E2/E3 + RERI + multiplicative + site frailty
│   └── s7_outputs.py                          NEW  disclosure-portable tables + diagnostics
├── run/                                       NEW  ordered driver (tool-agnostic; Snakemake/Make optional)
└── tests/                                     NEW  temporal-order + suppression unit tests on tiny fixtures
```

## Key decisions

### Key decision 1: Synthetic-tier-first, not wait-for-enclave
- **Chosen approach:** build and debug the entire pipeline on the open synthetic slice now.
- **Rejected alternative:** defer all pipeline work until the N3C DUA/Limited access clears.
- **Reason:** the synthetic tier lets us de-risk every stage's *mechanics* and portability at
  zero access cost, so enclave time is spent on results, not debugging.

### Key decision 2: OMOP-first with an execution shim (portability over local convenience)
- **Chosen approach:** write stage logic as OMOP-CDM queries behind `ohdsi_shim` so the same
  code runs on local synthetic (duckdb/pandas) and the enclave (Palantir Foundry / PySpark).
- **Rejected alternative:** prototype in local-only pandas idioms and re-port to Spark later.
- **Reason:** re-porting is where silent logic drift enters; one code path eliminates it.

### Key decision 3: Matched 1:5 as the reference design, weighting as a coded alternative
- **Chosen approach:** reproduce Hill's within-site 1:5 matching as the primary design.
- **Rejected alternative:** propensity-score weighting as primary.
- **Reason:** matching is the published, portable N3C precedent (`paper:Hill2022`); weighting
  is retained as a switch for the sensitivity arbitration, not the default.

### Key decision 4: Severity is a separately-built POST-index mediator, never a baseline covariate
- **Chosen approach:** `s4_severity.py` reads only acute-window (post-index) dated events and
  is excluded from the E1 adjustment set by construction.
- **Rejected alternative:** fold severity into the covariate table with everything else.
- **Reason:** the E1-total vs E2-controlled-direct distinction (the Boekel2023 lesson) is only
  safe if severity *cannot* accidentally enter the total-effect model — enforce it structurally.

### Key decision 5: Disclosure-portable outputs from stage one, not post-hoc
- **Chosen approach:** `s7_outputs.py` applies `disclosure.yaml` (suppress ≤ threshold, then
  round) to every emitted table, tested on synthetic outputs.
- **Rejected alternative:** produce raw outputs now, add suppression before enclave export.
- **Reason:** the same output layer must clear **N3C enclave review now and OpenSAFELY SDC
  later** — building it in means rare-cell suppression shapes the design (pooling decisions)
  from the start, not as a surprise at export.

### Key decision 6: Temporal ordering enforced by window config, not by analyst discipline
- **Chosen approach:** `config/windows.yaml` fixes index → lookback → acute → PASC offsets;
  each stage filters to its window programmatically.
- **Rejected alternative:** apply time filters ad hoc inside each script.
- **Reason:** exposure → severity → outcome ordering is the identification backbone; a config
  contract makes violations a test failure, not a code-review miss.

## Work Packages

### WP0: Synthetic-tier standup + access punch-list
- **Depends on:** `interpretation:0031` (vehicle locked). 
- **Entry point:** acquire the N3C synthetic OMOP data package; instantiate `ohdsi_shim` local
  backend.
- **Definition of done:** synthetic OMOP tables queryable via the shim; a written punch-list of
  what only the enclave/Limited tier can confirm (real utilisation coding, PASC phenotype
  coverage, true cell counts) filed against BC-2's real-tier remainder. Confirm the enclave
  runtime (Foundry/PySpark, OMOP CDM version) as an **open question**, not an assumption.

### WP1: Versioned concept-set / codelist bundle
- **Depends on:** WP0.
- **Entry point:** assemble OMOP concept sets for the eight autoimmune strata, PASC, severity,
  utilisation into `concept_sets/` with `BUNDLE.lock` (checksums + provenance).
- **Definition of done:** bundle loads, is immutable-by-checksum, and each stratum resolves to
  ≥1 concept on synthetic data. **Clinical sign-off of the rarest strata is explicitly BC-3, not
  this WP** — flagged, not silently assumed.
- **Reusable:** `true` — the concept-set bundle is the shared input for the enclave run and the
  OpenSAFELY translation (BC-5).

### WP2: Cohort construction
- **Depends on:** WP0, WP1.
- **Entry point:** `s1_cohort.py` — index SARS-CoV-2 event, inclusion (≥45 d post-index
  observation; sufficient pre-index observation for lookback), 1:5 within-site matching.
- **Definition of done:** a matched cohort table with matched-set IDs; the weighting alternative
  runs behind a flag; unit test confirms no member violates the observation windows.

### WP3: Exposure build
- **Depends on:** WP1, WP2.
- **Entry point:** `s2_exposure.py` — dated pre-index stratum indicators + the pooling hierarchy
  (organ-specific / systemic-rheumatic / genetic-risk-only) for strata below the power floor.
- **Definition of done:** per-patient stratum flags with onset strictly before index; a pooling
  report shows which strata collapse at synthetic cell counts (mechanism check only).

### WP4: Covariate build
- **Depends on:** WP2.
- **Entry point:** `s3_covariates.py` — age, sex, calendar/variant era, vaccination-at-index,
  baseline non-autoimmune comorbidity, **individual pre-index utilisation (encounter counts over
  a fixed lookback)**, prior-infection count.
- **Definition of done:** covariate table built; **vaccination carries the plan:0005 caveat** —
  produced in both a vaccination-adjusted and a vaccination-unadjusted variant (partly
  post-exposure); utilisation is individual-level (Hill's county proxy is *not* used).

### WP5: Severity mediator build
- **Depends on:** WP2.
- **Entry point:** `s4_severity.py` — acute-window (post-index) dated hospitalisation / ICU /
  oxygen.
- **Definition of done:** severity variable dated strictly after index and before the PASC
  window; a guard test fails if severity is ever joined into the E1 adjustment set.

### WP6: Outcome build
- **Depends on:** WP2.
- **Entry point:** `s5_outcome.py` — computable PASC phenotype (U09.9 + N3C phenotype), PASC
  ascertainment window per `windows.yaml`.
- **Definition of done:** binary PASC outcome with sensitivity variants (U09.9-only,
  phenotype-only) plumbed; case-definition provenance recorded (this is plan:0005's BC-5 for the
  N3C side).

### WP7: Estimation
- **Depends on:** WP3, WP4, WP5, WP6.
- **Entry point:** `s6_estimate.py` — E1 total (log-binomial → modified-Poisson/robust-SE
  fallback; severity excluded), E2 controlled-direct (severity at reference), optional E3
  mediation decomposition; sex × stratum interaction on **additive (RERI, primary) + multiplicative**
  scales; site random intercept / frailty.
- **Definition of done:** all estimators return without error on synthetic data and emit the
  E1/E2 pair as **distinct labeled estimands** (not a robustness pair); the fallback path is
  exercised by a forced-non-convergence fixture.

### WP8: Diagnostics + disclosure-portable outputs
- **Depends on:** WP7.
- **Entry point:** `s7_outputs.py` — per-stratum × sex cell counts, minimum detectable RR per
  stratum, positivity/overlap, E-value on E1, negative-control-outcome result; all through the
  `disclosure.yaml` suppress-then-round layer.
- **Definition of done:** every emitted table is disclosure-safe (no cell ≤ threshold survives);
  a suppression unit test proves rare autoimmune-stratum × sex cells are handled; outputs are
  structured to clear both N3C enclave review and OpenSAFELY SDC.

### WP9: Scale/resource + end-to-end validation
- **Depends on:** WP2–WP8.
- **Entry point:** run the ordered driver on the **largest available synthetic slice**.
- **Definition of done:** pipeline completes end-to-end; peak memory + wall-clock recorded;
  temporal-order and suppression tests green. **Acceptance is "runs, strata resolve, estimands
  compute, outputs disclosure-safe" — explicitly NOT any coefficient value.**

## Open questions

- N3C enclave runtime specifics (Foundry/PySpark version, OMOP CDM version, whether synthetic
  and Limited tiers share a schema) — confirm in WP0; affects `ohdsi_shim`.
- Does synthetic N3C include the RECOVER computable PASC phenotype, or only U09.9? Changes WP6
  fidelity.
- Fixed lookback length (365 d candidate) and the suppression threshold/rounding — inherited
  from plan:0005 / N3C policy; confirm exact N3C small-cell rule for `disclosure.yaml`.

## Non-Goals

- No interpretable effect estimate (synthetic data). No causal claim of any kind emerges here.
- No real-tier access work beyond filing the WP0 punch-list (rest of BC-2).
- No OpenSAFELY code (BC-5 gates it).
- No clinical sign-off of codelists (BC-3).

## Acceptance Criteria

- [ ] All six stages + output layer run end-to-end on the synthetic slice via one code path.
- [ ] Concept-set bundle is versioned/immutable; all eight strata resolve.
- [ ] E1 and E2 emit as distinct labeled estimands; severity structurally excluded from E1.
- [ ] Vaccination-adjusted and -unadjusted variants both produced.
- [ ] Interaction reported on additive (RERI) + multiplicative scales.
- [ ] Every output table passes the disclosure suppress-then-round layer (proven by test).
- [ ] Temporal-ordering guard tests green (exposure < severity < outcome).
- [ ] Peak memory + wall-clock recorded on the largest synthetic slice.
- [ ] WP0 punch-list of enclave-only confirmations filed against BC-2's real-tier remainder.
