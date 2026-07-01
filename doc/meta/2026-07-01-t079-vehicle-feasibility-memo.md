---
id: "doc:t079-vehicle-feasibility-memo-2026-07-01"
title: "Vehicle-feasibility memo (t079): BC-1→BC-7 for the autoimmune-diathesis × sex × PASC analysis"
created: "2026-07-01"
updated: "2026-07-01"
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
  - interpretation:0034-t079-bc6-acute-severity-dateability
  - interpretation:0035-t079-bc7-individual-utilisation
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - dataset:all-of-us-covid
  - dataset:recover-adult
  - dataset:uk-biobank-covid
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - question:0007-mechanism-of-female-predominance-in-pais
  - paper:Hill2022
---

# Vehicle-Feasibility Memo (t079)

This is the **vehicle-feasibility memo** required by
`plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan` (*Required Output Artifacts*).
It consolidates the seven blocking checks (BC-1→BC-7) into one decision record: **which
candidate vehicle cleared which gate, why N3C is primary, and what remains before the plan can
move to `ready-with-caveats` and pre-registration.** It synthesises the five per-BC
interpretations (`interpretation:0031`–`0035`); each row points back to its durable verdict.
No participant-level data was accessed in any BC — this is a design/feasibility pass.

## Headline decision

- **Primary vehicle: N3C** (`dataset:n3c-recover-longcovid`) — OMOP CDM, enclave-gated, with an
  **open synthetic tier to prototype on now**. Chosen for the most mature computable PASC
  phenotype (Hill-replicable), rare-stratum × sex **scale**, and native individual-level pre-index
  history. Cost carried: US healthcare-seeking EHR → sampling-frame ascertainment skew.
- **Population-based replication: OpenSAFELY** (`dataset:opensafely-longcovid`) — near-whole-population
  England primary care (realistically **TPP-only ~24M now**, EMIS research backend paused). Its
  role is **sampling-frame arbiter only**, not a second primary and **not** a clean outcome-side
  arbiter (BC-5).
- **Triangulation adjuncts:** All of Us (diverse population), RECOVER-Adult (survey-PRO construct
  anchor, not an interaction-carrying vehicle), UK Biobank (rare within-person pre-infection
  baseline, but healthy-volunteer/older-age skew).

**One-line verdict:** the estimand is feasible in principle on N3C with OpenSAFELY replication;
every design gate that literature/schema can settle **is settled**; the analysis is now gated on
**access/execution (BC-2)** and on **cell counts (BC-4)** — the latter still a *design* gate, not
mere counting (see the prominent caveat below).

## BC-1→BC-7 clearance ledger

| BC | Gate | Status | Verdict (one line) | Source |
|---|---|---|---|---|
| **BC-1** | Vehicle selection + OpenSAFELY discovery | ✅ resolved | N3C primary; OpenSAFELY population-based replication; All-of-Us triangulation | `interpretation:0031` |
| **BC-2** | Access verification | ⏸ held (execution-gated) | Prototype designed on N3C **open synthetic slice** (`plan:0006`); real-tier + code execution gated on `t080`/`t081`/`t082` | task notes; `plan:0006` |
| **BC-3** | Autoimmune stratum granularity | ✅ largely resolved | Both vehicles resolve the 8 disease-specific strata with dated pre-index onset (fixes Hill's pooled Charlson term); **7/8 clean, autoimmune-thyroid partial** (isolable Graves, not autoimmune-hypothyroid → exposure-channel h0008) | `interpretation:0032` |
| **BC-4** | Sex × stratum × PASC cell counts vs power floor | ⛔ **open — the binding unknown** | Not literature-progressable; access-gated on the N3C enclave. **Still a design gate** (can force pooling / endpoint / interaction-scale — see caveat) | — |
| **BC-5** | Computable PASC case-definition lock | ✅ resolved | N3C primary = coded U09.9-or-LC-clinic (WHO ≥90 d); Pfaff ML phenotype **demoted** (its top feature *is* the utilisation confound); RECOVER survey index = construct anchor only; OpenSAFELY = NICE 3-cluster coded + bracketing pair. **Every EHR outcome is utilisation-gated** (outcome-channel h0008) | `interpretation:0033` |
| **BC-6** | Acute-severity dateability (mediator role, E2/E3) | ✅ resolved | Severity **dateable enough to compute** E2/E3 (identification stays assumption-dependent); coarse hospitalisation-based mediator primary; ≥45 d survival filter → **E1 survivor-conditional** + acute death a competing risk (mediator-channel h0008) | `interpretation:0034` |
| **BC-7** | Individual-level utilisation covariate | ✅ resolved | Buildable in both (replaces Hill's county proxy); **dual-role** variable (true disease `D` footprint vs recorded `E_obs` measurement machinery) → outpatient-only adjuster + adjusted/unadjusted E1 pair; the **defence is bounded**, quantified by negative control + E-value | `interpretation:0035` |

**Scoreline:** BC-1, BC-3, BC-5, BC-6, BC-7 resolved; **BC-2 held** (access/execution);
**BC-4 open** (access-gated, binding).

## Vehicle scorecard against the eight required properties

From `plan:0005` *Data Inputs* — every admissible vehicle must carry all eight. `✓` strong,
`~` partial/caveated, `✗` weak. Verified in BC-1..BC-7 (read-only), not assumed.

| Required property | N3C (primary) | OpenSAFELY (replication) | Others |
|---|---|---|---|
| 1. Dated SARS-CoV-2 index | ✓ earliest positive test/dx | ✓ SGSS test date | AoU ✓ · RECOVER ~ (post-enrol) · UKB ~ |
| 2. Pre-index diagnostic history (lookback) | ✓ deep OMOP history | ✓ primary-care event dates | AoU ✓ · RECOVER ✗ (≥3 mo post-infection enrol) · UKB ✓ |
| 3. Autoimmune stratum granularity (BC-3) | ✓ 7/8 (thyroid partial) | ✓ 7.5/8 (NHSD refsets) | AoU ~ · others ~ |
| 4. Computable PASC outcome (BC-5) | ✓ coded primary (ML demoted) | ~ coded under-recorded, reshapes bias | RECOVER ✓✓ survey (construct anchor) |
| 5. Acute-severity timestampable (BC-6) | ✓ top rungs; oxygen soft | ✓ SUS/HES/ECDS/ICNARC/ONS; oxygen soft | RECOVER ✗ (limited) |
| 6. Individual-level utilisation (BC-7) | ✓ visit_occurrence (out-of-network undercount) | ✓ ehrQL consultations (GP-complete) | AoU ~ |
| 7. Sex × stratum cell counts (BC-4) | **? scale is the advantage — unresolved** | ~ SDC ≤7/round-5 + EMIS pause force pooling | RECOVER ✗ · UKB ✗ (small/old) |
| 8. Population-based sampling (h0008) | ✗ US healthcare-seeking EHR | **✓✓ near-whole-population — its headline advantage** | AoU ~ diverse · UKB ✗ volunteer |

The two rows that drive the split: **row 4** (N3C's mature computable outcome vs OpenSAFELY's
differentially under-recorded coded outcome) makes N3C primary; **row 8** (OpenSAFELY's
population frame) is exactly why it is retained as the sampling-frame replication arbiter. **Row
7 is BC-4 — the one unresolved cell**, and N3C's scale is the reason it is the best *candidate*
to clear it, not evidence that it does.

## The cross-cutting finding — h0008 operates on every channel, and so does its defence

The single most important synthesis result across BC-3/BC-5/BC-6/BC-7 is that
`hypothesis:0008` (measurement-channel / ascertainment) is **not a nuisance at the edges — it is
structural on all three arms of the estimand, and even the analytic defence against it is
measurement-limited:**

- **Exposure channel (BC-3):** autoimmune-thyroid is mis-captured (isolable Graves, not
  autoimmune-hypothyroid) → exposure misclassification.
- **Outcome channel (BC-5):** *every* EHR PASC outcome is utilisation-gated; the "most mature"
  ML phenotype bakes the utilisation confound into its very definition.
- **Mediator channel (BC-6):** the severity ladder degrades in its middle, and the survival
  filter selects on a consequence of the mediator.
- **The defence itself (BC-7):** individual-utilisation adjustment — the primary tool against all
  of the above — is a dual-role, differentially-measured, era-drifting covariate.

**Operational consequence (locked across the plans):** the study's validity does **not** rest on
finding a clean channel — none exists — but on **design defences whose adequacy is quantified, not
assumed**: individual pre-index *outpatient* utilisation adjustment (adjusted/unadjusted framing
pair, read by sex), a **not-autoimmune-specific / not-downstream negative-control outcome** (baseline
association checked), an **E-value** on the primary E1, bracketing sensitivity pairs, and
population-based replication for the sampling frame. This is the through-line the pre-registration
must foreground.

## Design decisions locked out of BC-1→BC-7 (carried into plan:0005 / plan:0006)

- **Exposure (BC-3):** 8 disease-specific strata as concept sets with dated pre-index onset;
  pooling hierarchy = systemic-rheumatic {SLE, RA, Sjögren, vasculitis, myositis} / organ-specific
  {IBD, MS, autoimmune-thyroid} / genetic-risk-only (not EHR-resolvable → `question:0005`); three
  a-priori scoping decisions to pre-register (vasculitis subtype-union, autoimmune-thyroid
  Graves+Hashimoto-specific primary, myositis exclusions).
- **Outcome (BC-5):** N3C primary = coded U09.9-or-LC-clinic (WHO-aligned ≥90 d); Pfaff ML =
  flagged sensitivity; OpenSAFELY = NICE 3-cluster coded pooled + coded-diagnosis-only/any
  bracketing pair.
- **Mediator (BC-6):** coarse dated hospitalisation-based severity primary (WHO-ordinal +
  oxygen = sensitivity); acute death a competing risk for E2/E3; **E1 explicitly survivor-conditional**
  with a competing-risk/composite-death sensitivity.
- **Utilisation (BC-7):** pre-index *outpatient* contact = E1 adjuster (inpatient → severity
  denylist); adjusted/unadjusted E1 framing pair (divergence read by sex); negative control
  not-autoimmune-specific / not-downstream.
- **Windows (four, non-interchangeable):** utilisation lookback (≤365 d pre-index) · acute-severity
  (index → ≤28 d) · survival/inclusion (≥45 d) · PASC ascertainment (≥90 d), with a buffer and pinned
  inclusive/exclusive + day-28-spanning-admission conventions.
- **Estimands:** E1 total (survivor-conditional), E2 controlled-direct, E3 mediation
  (exploratory); focal **sex × stratum interaction on additive (RERI, primary) + multiplicative**
  scales.

## ⚠️ BC-4 — the prominent remaining caveat (design, not just counting)

**BC-4 is the binding unresolved gate and it is not merely an arithmetic check.** It cannot be
progressed without N3C enclave access, and the observed **sex × stratum × PASC cell counts can
still change the design:**

- **Stratum pooling** — rare strata (vasculitis, myositis, MS, especially × male) may fall below
  the power floor and be forced into the pre-registered pooling hierarchy, changing *what
  contrasts are even reported*.
- **Endpoint choice** — the coded-primary PASC outcome is *less* sensitive than the demoted ML
  phenotype, so counts under the coded definition are the **conservative** power test; if they are
  too thin, the endpoint or its bracketing may shift.
- **Interaction-scale expectations** — the **additive interaction (RERI) is materially more
  data-hungry** than the main effect and is expected to bind first; BC-4 sets whether the focal
  sex × stratum interaction is estimable at all, or only the marginal per-stratum effects.
- **BC-6/BC-7 riders sharpen it** — the competing-risk handling of acute death further thins the
  most severe *exposed* cells, so the power test must run on the **competing-risk / survivor
  cohort**, not the raw cohort.

So "the literature-progressable design work is complete" is **not** "all design feasibility is
settled." BC-4's design consequences are real; they are simply unresolvable until the enclave
counts exist. Treat BC-4 as an open design gate, access-gated.

## Access / execution status

- **BC-2 held** (not failed): the N3C synthetic-tier prototype is *designed and reviewed*
  (`plan:0006`, `/science:review-pipeline` WARN with no hard blocker) but **execution is gated** on
  `t080` (N3C synthetic/enclave access), `t081` (OMOP/ATHENA vocabulary validity — resolves the
  standing `[UNVERIFIED]` OMOP concept_ids), and `t082` (the explicit seed-stage→build scope
  decision to write runnable pipeline code). Code home when approved = `code/n3c-autoimmune-sex-pais/`.
- `plan:0005` stays **`not-ready`**, now blocked **only on access/execution (BC-2) and on
  access-plus-design (BC-4)** — no open *literature* design question remains. When BC-2 and BC-4
  clear, the plan routes to `ready-with-caveats` → `/science:pre-register` as a `data-gated`
  pre-registration whose G-gates are these BCs.

## Residual `[UNVERIFIED]` / open items

- OMOP concept_ids for the N3C strata (ATHENA 403 during BC-3) → `t081`.
- Hill2022 exact pre-index lookback window (supplementary eMethods) — `[UNVERIFIED]`, not
  load-bearing for feasibility.
- U09.9 N3C-site adoption ramp; magnitude of the N3C out-of-network utilisation undercount and the
  oxygen-rung under-capture — all become BC-4-era measurements once cohorts exist.

## Bottom line

The autoimmune-diathesis × sex × PASC estimand is **feasible on N3C with OpenSAFELY replication**,
and it is **unreported in the literature** (Hill2022 has the design substrate but pools autoimmune,
treats sex as a covariate, and proxies utilisation — all three gaps now closed by BC-3/the
estimand/BC-7). The dominant risk is **not** power but **ascertainment**, which is structural on
all three channels (BC-3/5/6) and only boundedly defensible (BC-7) — so the pre-registration's
confirmatory strength lives in its **design defences and their quantification (E-value +
not-autoimmune-specific negative control + bracketing pairs + population-based replication)**, not
in any single clean measurement. The next real milestone is **access (BC-2 via t080–t082)**, at
which point **BC-4** — still an open *design* gate — can finally be measured.
