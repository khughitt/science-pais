---
id: "plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline"
type: "plan"
title: "Pipeline (prototype): N3C synthetic-tier skeleton for the autoimmune × sex × PASC estimand (t079/BC-2)"
status: "archived"
created: "2026-07-01"
updated: "2026-07-01"
plan_kind: "pipeline"
related:
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - task:t079
  - task:t080
  - task:t081
  - task:t082
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
  - interpretation:0034-t079-bc6-acute-severity-dateability
  - interpretation:0035-t079-bc7-individual-utilisation
  - paper:Pfaff2022
  - dataset:n3c-recover-longcovid
  - dataset:n3c-recover-longcovid-synthetic
  - paper:Hill2022
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
---

# Pipeline (prototype): N3C synthetic-tier skeleton for the autoimmune × sex × PASC estimand (t079/BC-2)

> **⚠️ ARCHIVED 2026-07-01 (`core/decisions.md` D-004).** The N3C synthetic tier this pipeline builds
> on is **non-downloadable (enclave-only)**, so its "open prototype substrate" premise is false and
> the parent estimand (`plan:0005`) is shelved as infeasible-under-transparency-standards. This plan
> is **not to be executed.** Retained as **banked design** — the WP decomposition, the `ohdsi_shim`
> abstraction, and the disclosure-portable output pattern are reusable if a genuinely
> third-party-reproducible population-EHR vehicle ever appears.

> Execution orchestration for `plan:0005`. This is a **prototype/design plan**, not a
> production run. The methodological readiness checks (estimands, independent unit, power
> floor, bias-vs-variance, sensitivity arbitration) are **already settled in
> `plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan`** and are **not
> re-decided here** — this plan only builds the runnable, enclave-portable skeleton.
>
> **Execution status (2026-07-01): SHELVED / ARCHIVED** — see the banner above and `core/decisions.md` D-004. (Was: DESIGNED · REVIEWED · SYNTHETIC-SLICE-GOVERNED · execution-blocked, before the N3C synthetic tier was confirmed non-downloadable.)
> BC-2 is *not failed* — it is blocked at execution on two access gates and one scope decision,
> all filed as tasks: **t080** (N3C Enclave / synthetic-tier access → WP0), **t081** (OMOP Athena
> vocabulary → WP1 vocab-validity), **t082** (scope-boundary decision — writing runnable pipeline
> code is a seed-stage→build phase transition and must be an explicit decision, not t079 momentum).
> **No pipeline code (fixtures included) is written until t082 approves it.** If approved, the code
> home is **`code/n3c-autoimmune-sex-pais/`** (research-profile convention) — *not* `results/`, *not*
> an unanchored root `src/`. F1/F2 design decisions are resolved in-plan; F2's dataset artifact
> (`dataset:n3c-recover-longcovid-synthetic`) exists; the rest awaits the gates.

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
- Final codelist clinical review for the rarest strata — the **BC-3-derived real-estimate
  clinical-review follow-up** (BC-3's vocabulary clearance is done, `interpretation:0032`);
  here we build the *mechanism*, not the clinically-signed-off list.

## Architecture

Portable OMOP-first layout; the same `src/` runs local-synthetic and enclave-Spark behind a
thin execution shim. **Code home is `code/n3c-autoimmune-sex-pais/` (conditional on t082 scope
approval); nothing below is created until then.**

```
code/n3c-autoimmune-sex-pais/                 NEW  (prototype repo / enclave code-workbook mirror; gated on t082)
├── config/
│   ├── windows.yaml                          NEW  index/lookback/acute/PASC offsets + matching SEED + boundary rules (versioned)
│   └── disclosure.yaml                        NEW  per-target SDC profiles (n3c PROVISIONAL, opensafely); "clears both" = stricter (F7)
├── concept_sets/                              NEW  the versioned exposure/outcome/severity bundle (BC-1 input)
│   ├── autoimmune/{sle,ra,ibd,ms}.csv         NEW  confirmed strata — draft lists
│   ├── autoimmune/{sjogren,vasculitis,myositis,ai-thyroid}.csv  NEW  STUBS, bc3_gated:true (F4)
│   ├── pasc.csv  severity.csv  utilisation.csv                                 NEW
│   └── BUNDLE.lock                            NEW  checksums + provenance + per-stratum bc3_gated flags (immutable); status: draft-unreviewed
├── schemas/                                   NEW  per-stage output contracts (grain, columns, keys) — asserted at stage entry/exit (F5)
│   └── s1..s7.schema.yaml                     NEW
├── src/
│   ├── io/ohdsi_shim.py                       NEW  SQL-portable subset; duckdb(local) | spark(enclave); single named COLLECT boundary (F1)
│   ├── s1_cohort.py                           NEW  index event, inclusion, seeded total-order 1:5 matching (+weighting alt)
│   ├── s2_exposure.py                         NEW  dated pre-index strata + pooling hierarchy
│   ├── s3_covariates.py                       NEW  age/sex/era/vax(adj+unadj)/comorbidity/utilisation(outpatient adj+unadj; inpatient→severity denylist, BC-7)/prior-infection
│   ├── s4_severity.py                         NEW  POST-index dated mediator: coarse hosp/ICU primary, WHO-ordinal+O2 sensitivity, acute-death competing-event flag (BC-6)
│   ├── s5_outcome.py                          NEW  computable PASC phenotype (U09.9 + phenotype)
│   ├── s6_estimate.py                         NEW  COLLECT→pandas; E1/E2/E3 + RERI + multiplicative + frailty (local stats)
│   └── s7_outputs.py                          NEW  policy-driven SDC tables + diagnostics + datapackage.json (F5)
├── run/                                       NEW  ordered driver (tool-agnostic; Snakemake/Make optional)
└── tests/                                     NEW  cross-engine matching determinism, E1 design-matrix severity denylist,
                                                    window-boundary fixtures, parameterized suppression, schema-contract checks
```

## Key decisions

### Key decision 1: Synthetic-tier-first, not wait-for-enclave
- **Chosen approach:** build and debug the entire pipeline on the open synthetic slice now.
- **Rejected alternative:** defer all pipeline work until the N3C DUA/Limited access clears.
- **Reason:** the synthetic tier lets us de-risk every stage's *mechanics* and portability at
  zero access cost, so enclave time is spent on results, not debugging.

### Key decision 2: OMOP-first shim with an explicit distributed→collect boundary (not "one code path everywhere")
- **Chosen approach:** heavy set-based data assembly (s1–s6 cohort/exposure/covariate/severity/
  outcome joins) is written as an **OMOP-CDM SQL-portable subset** behind `ohdsi_shim`
  (duckdb local ↔ Spark enclave); estimation (`s6_estimate`) runs on a **collected pandas
  frame** in *both* environments, after a disclosure-safe size check. The shim guarantees
  portability **only** for the SQL-portable layer, and the collect boundary is a named,
  documented contract — not an implicit `.toPandas()` wherever convenient.
- **Rejected alternative:** treat the whole of `src/` as uniformly dual-runtime ("same code
  everywhere"), including estimation.
- **Reason:** log-binomial/RERI/frailty are statsmodels/R, which **cannot** run as Spark
  transforms; pretending otherwise hides the real boundary. F1 (review) — the honest contract
  is "distributed SQL builds analysis tables → collect (size-checked) → local stats," identical
  in synthetic and enclave, with the *only* enclave swap being an optional enclave-native stats
  engine later. See **Pre-WP2 blocking decisions**.

### Key decision 3: Matched 1:5 with a *deterministic, seeded, total-order* algorithm
- **Chosen approach:** reproduce Hill's within-site 1:5 matching, implemented as a
  **deterministic total-order selection** — candidates ordered by a stable key
  (`hash(person_id, seed)` + explicit tiebreak columns), seed pinned in config — so the matched
  sets are **identical across duckdb and Spark** and reproducible run-to-run.
- **Rejected alternative:** (a) propensity-score weighting as primary; (b) matching that relies
  on engine-default row order.
- **Reason:** Spark ordering is non-deterministic without a total order + seed, so naive
  matching would produce *different cohorts on the two engines* — silently breaking the
  portability claim (F1). Weighting is retained as a coded switch for sensitivity arbitration.

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

## Pre-WP2 blocking decisions

These two design decisions (review `doc/reviews/0006-...-pipeline-review.md`, F1 + F2) are
**expensive to fix after code exists** and **must be written and resolved before any cohort
code (`s1_cohort.py`, WP2) is started.** WP0–WP1 may proceed in parallel; WP2 may not begin
until both are settled.

**F1 — Deterministic matching + explicit distributed→collect boundary (KD2, KD3).**
- Matching is a **seeded total-order** algorithm (order by `hash(person_id, seed)` + declared
  tiebreak columns); seed pinned in `config/windows.yaml`. A cross-engine determinism test
  (same fixture → byte-identical matched-set IDs on duckdb and Spark) is a WP2 entry gate.
- The **shim contract** is documented: s1–s6 are SQL-portable/distributed; the pipeline
  **collects to pandas at a single named point** *after* a disclosure-safe size check; s6/s7
  stats run local (statsmodels/R) in both environments. No stage silently collects.

**F2 — Structural synthetic-slice dataset handling (WP0).** ✅ *entity created 2026-07-01.*
- The consumed data is now the granular sibling **`dataset:n3c-recover-longcovid-synthetic`**
  (`parent_dataset: dataset:n3c-recover-longcovid`, `access.exception: scope-reduced`), so the
  pipeline's input path resolves to a **synthetic-only artifact that cannot reference the
  Limited/enclave tiers.** **Still open (completes F2 in WP0):** acquire the synthetic OMOP
  package, set `local_path` + `verified: true` + `verification_method`, confirm the OMOP CDM
  version. Until `local_path` is populated the pipeline has no *stageable* input and WP2 cannot
  start.

## Work Packages

### WP0: Synthetic-tier standup + access punch-list  *(resolves F2)*
- **Depends on:** `interpretation:0031` (vehicle locked). 
- **Entry point:** acquire the N3C synthetic OMOP data package; instantiate `ohdsi_shim` local
  backend.
- **Definition of done:**
  1. **Structural synthetic-slice scoping (F2):** create/scope the input as
     `dataset:n3c-recover-longcovid-synthetic` (granular sibling, `local_path`/`datapackage` →
     the acquired synthetic package, `verified: true` + `verification_method` + `last_reviewed`)
     **or** add `access.exception: {mode: scope-reduced, followup_task: t079}` + `local_path` to
     the existing entity. The pipeline's input path resolves **only** to this artifact; the
     Limited/De-identified siblings are not reachable from any config value.
  2. Synthetic OMOP tables queryable via the shim; **schema/runtime confirmed** (OMOP CDM
     version; whether synthetic and Limited tiers share a schema) rather than assumed.
  3. A written **enclave-only punch-list** — real utilisation coding, PASC phenotype coverage,
     true cell counts, enclave stats engine — filed against BC-2's real-tier remainder.

### WP1: Versioned concept-set / codelist bundle  *(resolves F3, F4)*
- **Depends on:** WP0.
- **Entry point:** assemble OMOP concept sets for the autoimmune strata, PASC, severity,
  utilisation into `concept_sets/` with `BUNDLE.lock` (checksums + provenance).
- **Definition of done:**
  1. **Vocabulary validity is separate from patient hits (F3):** every code resolves in the
     OMOP `CONCEPT`/`CONCEPT_ANCESTOR` vocabulary (the portable, meaningful check). A
     synthetic-data **patient-hit count** is recorded as a smoke test only and is **explicitly
     allowed to be zero** for rare strata — a zero is not a WP1 failure.
  2. **Confirmed vs BC-3-gated strata (F4) — updated by `interpretation:0032` (2026-07-01):**
     BC-3 vocabulary verification is done — SLE/RA/IBD/MS **and** Sjögren/vasculitis/myositis now
     ship as **draft-confirmed** lists (OHDSI Phenotype Library cohorts #119/#196/#198/#201 for the
     first four; author-built-from-SNOMED for the next three). **Autoimmune-thyroid** stays flagged
     `bc3_gated: true` with the specific-vs-all-cause fork recorded in `BUNDLE.lock`. Three a-priori
     scoping decisions (vasculitis union, autoimmune-thyroid specific-primary, myositis exclusions)
     carried as bundle metadata. Bundle `status: draft-unreviewed`.
  3. Bundle loads and is immutable-by-checksum. **A separate real-estimate clinical-review gate
     (a BC-3-derived follow-up, *not* part of BC-3's clearance)** applies to the five author-built
     N3C strata (MS, Sjögren, vasculitis, myositis, autoimmune-thyroid): they need a clinical
     sign-off before use for a real estimate. BC-3 itself is resolved — vocabulary resolvability
     is cleared; this gate is a downstream prototyping→real-estimate step, not an open BC-3 item.
- **Reusable:** `true` — shared input for the enclave run and the OpenSAFELY translation (BC-5).

### WP2: Cohort construction  *(gated on F1)*
- **Depends on:** WP0, WP1, **and the F1 pre-WP2 decision (deterministic matching + shim
  boundary) being written and resolved.**
- **Entry point:** `s1_cohort.py` — index SARS-CoV-2 event, inclusion (≥45 d post-index
  observation; sufficient pre-index observation for lookback), 1:5 within-site matching via the
  **seeded total-order** algorithm (KD3).
- **Definition of done:** a matched cohort table with matched-set IDs; the weighting alternative
  runs behind a flag; **cross-engine determinism test passes** (same fixture → identical
  matched-set IDs on duckdb and Spark); unit test confirms no member violates the observation
  windows (inclusive/exclusive boundaries per `windows.yaml`).

### WP3: Exposure build
- **Depends on:** WP1, WP2.
- **Entry point:** `s2_exposure.py` — dated pre-index stratum indicators + the pooling hierarchy
  (organ-specific / systemic-rheumatic / genetic-risk-only) for strata below the power floor.
- **Definition of done:** per-patient stratum flags with onset strictly before index; a pooling
  report shows which strata collapse at synthetic cell counts (mechanism check only).

### WP4: Covariate build  *(BC-7 locked — `interpretation:0035`)*
- **Depends on:** WP2.
- **Entry point:** `s3_covariates.py` — age, sex, calendar/variant era, vaccination-at-index,
  baseline non-autoimmune comorbidity, **individual pre-index utilisation (encounter counts over a
  fixed 365 d lookback in `windows.yaml`), split by care setting (outpatient vs inpatient)**,
  prior-infection count.
- **Definition of done:** covariate table built; **vaccination carries the plan:0005 caveat** —
  produced in both a vaccination-adjusted and a vaccination-unadjusted variant (partly
  post-exposure); **utilisation is individual-level (Hill's county proxy is *not* used) and
  dual-role (BC-7):** the **pre-index *outpatient* count** is the E1 ascertainment adjuster and is
  emitted in **utilisation-adjusted and -unadjusted E1 variants** (mirroring the vaccination pair,
  divergence read by sex); the **inpatient count is routed to the F6 severity denylist** (mediator
  side, must not enter E1). All utilisation counting is strictly pre-index by construction.

### WP5: Severity mediator build  *(BC-6 locked — `interpretation:0034`)*
- **Depends on:** WP2.
- **Entry point:** `s4_severity.py` — acute-window (index → **≤28 d**, fixed upper bound in
  `windows.yaml`) dated events. **Primary mediator = coarse dated hospitalisation-based severity**
  (none / hospitalised-non-ICU / ICU-or-ventilation), which the synthetic OMOP schema dates
  crisply; a **finer WHO-style ordinal** adding the moderate/oxygen rung is a **flagged
  sensitivity mediator only** (that rung is differentially under-captured — BC-6). **Acute death
  is encoded as a competing event, not a row-drop** — the ≥45 d survival filter is the E1
  denominator device, but E2/E3 read a competing-risk-framed mediator so the survivor-only CDE
  is not silently conditioned on a downstream consequence of severity.
- **Definition of done:** severity variable dated strictly after index (≤28 d acute window) and
  before the PASC window with a **buffer** between them; **`windows.yaml` pins inclusive/exclusive
  boundary conventions and a day-28-spanning-admission rule** (assign by admission date, not
  discharge) so one long acute admission is neither split nor double-counted; a competing-event
  flag for acute death is emitted alongside the ordinal severity column; **the E1 guard asserts at
  the model-input level (F6)** — `severity_cols` (plus a maintained denylist of severity-*derived*
  proxies, e.g. hospitalisation-derived features, **and the acute-death competing-event flag**)
  must be disjoint from the exact column set of the E1 design matrix. A red-team fixture that tries
  to sneak a severity proxy into E1 must trip the guard.

### WP6: Outcome build  *(BC-5 locked — `interpretation:0033`)*
- **Depends on:** WP2.
- **Entry point:** `s5_outcome.py` — **primary = coded `U09.9`-or-LC-clinic** computable phenotype
  (Hill-replicable); PASC **ascertainment window WHO-aligned ≥90 d** in `windows.yaml`, kept
  **distinct from the ≥45 d survival/inclusion window** (BC-5 separated these).
- **Definition of done:** binary PASC outcome plumbed with pre-registered variants —
  **(i)** the **N3C-specific** coded bracketing pair **`U09.9-only` vs `U09.9-or-LC-clinic`** (the
  OpenSAFELY replication analog is `diagnosis-only` vs `all-three-clusters`, carried in
  plan:0005/BC-5, *not* here); **(ii) the Pfaff2022 ML phenotype (threshold 0.45) as a FLAGGED
  sensitivity endpoint**, with a code comment + manifest note recording that its top feature is
  outpatient visit rate (so the outcome is utilisation-gated by construction) **and** that it has an
  untested sex-specific error profile (75% female training positives, sex excluded, no by-sex
  performance) — a sex-proxy-leakage *risk*, not a verified bias — so it is **never the primary**
  here; **(iii)** a CDC-aligned ≥28 d window variant. The RECOVER survey PASC index is **out of
  scope** for N3C (not EHR-computable). Case-definition provenance recorded (this is plan:0005's
  BC-5 for the N3C side, now resolved).

### WP7: Estimation  *(honors the F1 collect boundary)*
- **Depends on:** WP3, WP4, WP5, WP6.
- **Entry point:** `s6_estimate.py` — the **distributed/SQL layer builds the analysis table**;
  the pipeline then **collects to pandas at the single named boundary, after a disclosure-safe
  size check**, and E1/E2/E3 estimation runs **local (statsmodels/R) in both synthetic and
  enclave** environments (F1). E1 total (log-binomial → modified-Poisson/robust-SE fallback;
  severity excluded), E2 controlled-direct (severity at reference), optional E3 mediation;
  **E1 is emitted labelled survivor-conditional with a competing-risk / composite-death
  sensitivity, and E2/E3 read the acute-death competing-event flag (BC-6/`interpretation:0034`)
  so both the total effect and the CDE are competing-risk-framed rather than silently conditioned
  on a downstream consequence of severity**; sex × stratum interaction on **additive (RERI,
  primary) + multiplicative** scales; site random intercept / frailty.
- **Definition of done:** the collect boundary is a single explicit call (no ad-hoc
  `.toPandas()` elsewhere); all estimators return without error on synthetic data and emit the
  E1/E2 pair as **distinct labeled estimands** (not a robustness pair); the fallback path is
  exercised by a forced-non-convergence fixture. *(An enclave-native stats engine is an optional
  later swap, recorded in the WP0 punch-list, not required for the prototype.)*

### WP8: Diagnostics + disclosure-portable outputs  *(resolves F7)*
- **Depends on:** WP7.
- **Entry point:** `s7_outputs.py` — per-stratum × sex cell counts, minimum detectable RR per
  stratum, positivity/overlap, E-value on E1, negative-control-outcome result; all through the
  policy-driven SDC layer.
- **Definition of done:** `disclosure.yaml` carries **per-target policy profiles** (N3C,
  OpenSAFELY) that differ; the layer applies the **stricter rule** (max threshold, coarsest
  rounding) whenever "clears both" portability is claimed. The N3C threshold value is marked
  **PROVISIONAL** pending WP0 confirmation and lives **only in config** — the suppression unit
  test is **parameterized on the mechanism, never a magic N**. Every emitted table is
  disclosure-safe under the active profile (proven by test), including rare autoimmune-stratum ×
  sex cells.

### WP9: Scale/resource + end-to-end validation
- **Depends on:** WP2–WP8.
- **Entry point:** run the ordered driver on the **largest available synthetic slice**.
- **Definition of done:** pipeline completes end-to-end; peak memory + wall-clock recorded;
  temporal-order and suppression tests green. **Acceptance is "runs, strata resolve, estimands
  compute, outputs disclosure-safe" — explicitly NOT any coefficient value.**

## Open questions

- N3C enclave runtime specifics (Foundry/PySpark version, OMOP CDM version, whether synthetic
  and Limited tiers share a schema) — confirm in WP0; affects `ohdsi_shim`.
- Does the synthetic tier carry U09.9 codes and LC-clinic visit types densely enough to smoke-test
  the WP6 primary phenotype? (BC-5 locked the *definition* — coded U09.9/clinic primary, Pfaff ML
  sensitivity, `interpretation:0033`; this is now only a synthetic-tier *density* question, resolved
  in WP0, not a definition question.) The Pfaff ML phenotype's published model artifact
  (`NCTraCSIDSci/n3c-longcovid`) is enclave-oriented — whether it runs on the open synthetic slice is
  a WP0 punch-list item.
- Fixed lookback length (365 d candidate) and the suppression threshold/rounding — inherited
  from plan:0005 / N3C policy; confirm exact N3C small-cell rule for `disclosure.yaml`.

## Non-Goals

- No interpretable effect estimate (synthetic data). No causal claim of any kind emerges here.
- No real-tier access work beyond filing the WP0 punch-list (rest of BC-2).
- No OpenSAFELY code (BC-5 gates it).
- No clinical sign-off of codelists (the BC-3-derived real-estimate clinical-review follow-up;
  BC-3's vocabulary-resolvability clearance is done, `interpretation:0032`).

## Acceptance Criteria

- [ ] **F2:** input resolves only to the verifiable synthetic artifact; no config value can reach the Limited/enclave tier.
- [ ] **F1:** cross-engine matching determinism test green (duckdb ≡ Spark matched-set IDs); single named COLLECT boundary, no stray `.toPandas()`.
- [ ] All six data stages + estimation + output layer run end-to-end on the synthetic slice.
- [ ] **F3:** concept-set bundle versioned/immutable; every code is **vocabulary-valid**; synthetic patient-hit counts recorded as a smoke test (zero allowed for rare strata).
- [ ] **F4:** confirmed strata (SLE/RA/IBD/MS) shipped as draft; the four unconfirmed strata stubbed `bc3_gated: true`; bundle `status: draft-unreviewed`.
- [ ] E1 and E2 emit as distinct labeled estimands; **F6:** severity (and its proxy denylist) disjoint from the E1 design matrix, proven by a red-team fixture.
- [ ] Vaccination-adjusted and -unadjusted variants both produced.
- [ ] Interaction reported on additive (RERI) + multiplicative scales.
- [ ] **F5:** each stage asserts its declared output schema; a `datapackage.json` manifest is produced for the outputs.
- [ ] **F7:** every output table passes the active SDC profile; "clears both" uses the stricter policy; threshold config-only + PROVISIONAL + mechanism-tested.
- [ ] **F8/F9:** matching seed + tool versions pinned; window-boundary (same-day / reinfection) fixtures green (exposure < severity < outcome).
- [ ] Peak memory + wall-clock recorded on the largest synthetic slice.
- [ ] WP0 punch-list of enclave-only confirmations filed against BC-2's real-tier remainder.
