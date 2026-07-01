---
id: "plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan"
type: "plan"
title: "Analysis plan: pre-existing autoimmune diathesis as a sex-conditioned effect modifier of long-COVID/PASC risk (t078)"
status: not-ready
created: "2026-06-30"
updated: "2026-07-01"
plan_kind: "analysis-plan"
related:
  - task:t078
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - hypothesis:0004-acute-severity-threshold
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0005-latent-to-overt-autoimmunity-conversion
  - question:0022-immune-state-displacement-mediator-vs-co-traveler
  - patch-definition:immune-state-shift-causal-landscape
  - paper:Hill2022
  - paper:Srivatsan2025
  - paper:Pfaff2022
  - paper:Thaweethai2023
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - dataset:all-of-us-covid
  - dataset:recover-adult
  - dataset:uk-biobank-covid
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
skills_loaded:
  - id: statistics-bias-vs-variance-decomposition
    reason: the dominant error term is differential ascertainment / confounding (both exposure and outcome are female-predominant and healthcare-contact-intensive), which does not shrink with sample size and must be separated from sampling variance
  - id: statistics-sensitivity-arbitration
    reason: two pre-committed adjustment sets (total-effect vs controlled-direct-effect), an E-value bound, a negative-control outcome for differential ascertainment, and a mediator-collider check whose disagreement changes the verdict
  - id: statistics-power-floor-acknowledgement
    reason: rare autoimmune strata (vasculitis, myositis, MS) crossed with sex risk empty/underpowered cells; a null in a stratum must be distinguished from non-arbitration
  - id: statistics-survival-and-hierarchical-models
    reason: PASC is naturally persistence-at-follow-up / time-to-onset, and any federated (N3C) or multi-vehicle pooled estimate needs a site random-intercept / frailty structure
---

# Analysis Plan: pre-existing autoimmune diathesis as a sex-conditioned effect modifier of long-COVID/PASC risk (t078)

This is a **design-stage** analysis plan. It **locks the target contrast** — two
explicitly-distinct estimands plus an optional mediation decomposition — and the
adjustment strategy, negative controls, and sensitivity-arbitration rules. It is
deliberately held at **`status: not-ready`**: no dataset is in hand, and execution
and pre-registration are gated on the dataset checks in *Blocking Checks Before
Pre-Registration*.

Reading of the two top cohort papers is complete (`paper:Hill2022`,
`paper:Srivatsan2025`) and **confirms the estimand is unreported**: no study gives a
sex-stratified pre-existing-autoimmune × long-COVID estimate with matched infected
controls and acute-severity + individual-utilization adjustment. Hill2022 demonstrates
the *design substrate* (N3C, 1:5 matched, computable PASC phenotype) but pools autoimmune
into one Charlson term, treats sex as a covariate, and proxies utilization at county
level. Srivatsan2025 is pointer-only, and its one matched cohort (Boekel2023) shows the
autoimmune→PASC association **attenuates to non-significant after severity adjustment** —
the observation that forces the total-vs-direct estimand split below.

## Analysis Question

Among individuals with a documented SARS-CoV-2 infection, does **pre-existing autoimmune
disease diagnosed before the index infection** raise the risk of long COVID / PASC, and
is that effect **modified by sex**? Acute-COVID severity is treated as a **mediator on the
h0004 path** (autoimmune → severe acute COVID → PASC), not merely a confounder, so the
question is deliberately posed as two estimands: the effect *including* the severity path
and the effect *net of* it.

## Related Hypotheses / Inquiries / Tasks

- `task:t078` — the triggering task (sex-conditioned autoimmune-diathesis effect modifier).
- `hypothesis:0005` (reproductive-stage homeostatic margin) and `question:0007`
  (female-predominance mechanism) — the sex-conditioning backbone.
- `hypothesis:0008` (measurement-channel / ascertainment meta-finding) — pre-committed as
  the dominant bias to defeat (see *Bias vs Variance Risks*).
- `hypothesis:0004` (acute-severity threshold) — the reason severity is a mediator, not a
  nuisance covariate; this plan's E2/E3 estimands are where the h0004 ⇄ autoimmune
  interaction is cashed out.
- `question:0005` (latent→overt autoimmunity) and `question:0022` (immune-state mediator
  vs co-traveler) — this is the effect-modifier arm feeding the causal-landscape sketch
  (`patch-definition:immune-state-shift-causal-landscape`).

## Data Inputs and Provenance

No dataset is in hand; this section states the **required dataset properties** and ranks
the candidate vehicles by whether each can support the estimand. Nothing here is an
assumed input — vehicle selection is itself a blocking check (BC-1).

**Required properties (any admissible vehicle must have all):**

1. A documented SARS-CoV-2 index event with a usable **infection/index date**.
2. **Pre-index diagnostic history** deep enough to establish autoimmune diagnosis *before*
   the index date (a real lookback window, not just prevalent-at-any-time coding).
3. **Autoimmune phenotype granularity** sufficient to resolve disease-specific strata
   (SLE, RA, Sjögren, systemic vasculitis, inflammatory myositis, IBD, MS, autoimmune
   thyroid) — not a single pooled "rheumatologic disease" term.
4. A **computable PASC/long-COVID outcome** (see *Estimand*).
5. **Acute-severity capture** (hospitalization/ICU/oxygen) time-stampable relative to the
   index date, so severity can be positioned as a post-exposure mediator.
6. **Individual-level healthcare-utilization** measures (encounter counts / baseline
   visit frequency), not an area-level proxy.
7. Enough **sex × autoimmune-stratum** cell counts to estimate an interaction (see *Power
   Floor*).
8. Sampling as close to **population-based** as possible (to blunt the h0008 ascertainment
   skew); clinic-ascertained samples are deprioritized.

**Candidate-vehicle ranking (to be verified in BC-1..BC-3, not assumed):**

1. **N3C (`dataset:n3c-recover-longcovid`) — PRIMARY (confirmed BC-1, 2026-07-01,
   `interpretation:0031`).** Hill2022 already proved it carries the matched design +
   computable PASC phenotype at millions-scale; EHR scale is what makes rare-stratum × sex
   cells estimable; individual-level utilization and pre-index ICD history are natively
   present (fixes two of Hill's three gaps). It also has the **most mature computable PASC
   outcome** and an **open synthetic tier to prototype on now**. Costs: US
   healthcare-seeking EHR → sampling-frame ascertainment skew; enclave-only compute;
   EHR-coded autoimmune/PASC noisy. **Prototype on the open synthetic tier now; real data is
   enclave-gated.**
2. **OpenSAFELY (`dataset:opensafely-longcovid`) — POPULATION-BASED REPLICATION (confirmed
   BC-1, 2026-07-01).** Near-whole-population England primary care (~58M; **realistically
   TPP-only ~24M now — EMIS research backend paused**), the strongest sampling frame for the
   h0008 concern, with dated pre-index autoimmune onset, dated SGSS index + SUS/HES/ICNARC
   severity, and per-patient GP-consultation utilisation. **Not primary:** coded long COVID
   is **severely and *differentially* under-recorded** (higher-utilisation patients, incl.
   autoimmune patients, are coded more) → a coded-only outcome carries outcome-side h0008
   bias; SDC (≤7, round-5) forces rare-cell pooling. Retained as the ascertainment arbiter
   (rule #4) **conditional on a non-coded-only PASC phenotype (BC-5)**.
3. **All of Us (`dataset:all-of-us-covid`) — diverse-population triangulation.** Offsets
   UKB/N3C skew; EHR + surveys, sex-stratifiable. Long-COVID phenotyping less mature than
   RECOVER; N smaller than N3C → rare strata likely underpowered. Best used to test whether
   the N3C estimate survives in a more representative frame.
4. **RECOVER-Adult (`dataset:recover-adult`) — phenotype-quality adjunct, not primary.**
   Best PASC outcome (PEM-weighted PASC index) but "limited" acute-severity capture, single
   cohort (tens of thousands → strata × sex underpowered), enrollment ≥3 mo post-infection
   (no pre-infection baseline; reverse-causation limit). Use to validate the outcome
   definition, not to carry the interaction estimand.
5. **UK Biobank (`dataset:uk-biobank-covid`) — pre-infection-baseline triangulation only.**
   Rare within-person pre-infection baseline, but healthy-volunteer + older-age skew and
   weak fatigue measurement; age-at-infection ≈52–83 distorts the sample. Secondary.

## Per-Input Data Profile

One row per candidate vehicle. Every field marked **[INSPECT]** is an inspection blocker
that must be resolved before any `ready` decision — for a design-stage plan they are the
substance of BC-1..BC-7, not blanks to ignore.

| Input | Encoding / file format | Row grain | Join cardinality | Missing-value sentinels | Provenance / source version | Checksum or immutable identifier |
|---|---|---|---|---|---|---|
| N3C + RECOVER-EHR | OMOP CDM in enclave (synthetic tier open) | 1 row / patient (+ encounter rows) | patient 1:N encounters | EHR absence ≠ negative [INSPECT] | covid.cd2h.org/dashboard/recover; release [INSPECT] | enclave dataset version [INSPECT] |
| OpenSAFELY | federated TPP/EMIS primary care | 1 row / patient | patient 1:N events | primary-care coding gaps [INSPECT] | opensafely.org; codelist versions [INSPECT] | no `dataset:` entity yet — BC-1 |
| All of Us | OMOP + surveys, Researcher Workbench | 1 row / participant | participant 1:N | survey skip-logic sentinels [INSPECT] | researchallofus.org controlled tier [INSPECT] | Workbench CDR version [INSPECT] |
| RECOVER-Adult | dbGaP / BioData Catalyst tables | 1 row / participant | participant 1:N visits | study-defined missing codes [INSPECT] | phs003463.v6.p5 (through 2025-12-05) | dbGaP accession phs003463.v6.p5 ✓ |
| UK Biobank COVID | UKB tabular field IDs | 1 row / participant | participant 1:1 | UKB special-value codes [INSPECT] | ukbiobank.ac.uk approved application | UKB field-basket ID [INSPECT] |

## Required Input Inspection

Before any modeling, on the selected vehicle:

1. **Exposure timing audit.** Confirm autoimmune diagnosis dates precede the index date;
   quantify how many "pre-existing" cases rely on a prevalent code with no dated onset, and
   set a minimum pre-index lookback (candidate: ≥365 d of observation with ≥1 encounter).
2. **Stratum resolvability.** Pull code counts per autoimmune stratum (SLE, RA, Sjögren,
   vasculitis, myositis, IBD, MS, autoimmune thyroid); flag strata below the power floor
   for pre-registered pooling rather than silent collapse.
3. **Severity time-stamping.** Verify hospitalization/ICU/oxygen events can be dated in the
   acute window (index → ~28 d) so severity sits *after* exposure and *before* the PASC
   ascertainment window — mandatory for its mediator role.
4. **Utilization measurability.** Confirm individual-level pre-index encounter counts exist
   (replacing Hill's county proxy).
5. **PASC phenotype provenance. LOCKED — BC-5 / `interpretation:0033`.** N3C primary = coded
   U09.9-or-LC-clinic (WHO-aligned ≥90 d); Pfaff ML phenotype = flagged sensitivity (utilisation
   is its top feature + an untested sex-specific error profile); RECOVER survey index = construct anchor only
   (not EHR-computable). OpenSAFELY primary = NICE 3-cluster coded pooled + diagnosis-only/any
   bracketing pair. Coding drift recorded: U09.9 from 2021-10-01 (calendar-time ascertainment);
   every EHR outcome utilisation-gated.
6. **Uninfected/comparison availability.** Confirm whether an uninfected arm exists or the
   design is PASC-vs-no-PASC among infected (Hill's design); this changes the estimand's
   reference set.

## Preprocessing / Normalization Checks

- Harmonize autoimmune strata to a **pre-registered ICD-10/SNOMED codelist** (versioned,
  committed before extraction) — the single largest lever on exposure misclassification.
- Define **index date**, the **acute severity window**, the **survival/observation inclusion
  window** (Hill's ≥45 d — a denominator filter), and the **PASC ascertainment window** (locked
  WHO-aligned **≥90 d**, distinct from the inclusion window — BC-5 separated these) as fixed
  offsets so temporal ordering (exposure → severity → outcome) is enforced by construction, not by
  post-hoc filtering. Report a CDC-aligned ≥28 d ascertainment variant.
- Define **variant era** and **vaccination status at index** as calendar/observed covariates.
- Build the **individual utilization** covariate from a fixed pre-index baseline window
  (e.g. 365 d) to avoid conditioning on post-exposure contact.
- Pre-specify handling of **immunosuppressive treatment** at index (a fork: it is part of
  the autoimmune exposure's biology *and* a potential separate effect — carry as a
  pre-registered secondary stratification, not a silent adjustment).

## Independent Unit and Denominator

- **Independent unit:** the individual patient, one qualifying index SARS-CoV-2 infection
  (first documented infection in the study window).
- **Denominator:** infected individuals meeting the index-event definition and a minimum
  post-index survival/observation window (candidate ≥45 d, matching Hill) with sufficient
  pre-index observation for the lookback.
- **Clustering:** patients nest in sites/data-partners (N3C) or practices (OpenSAFELY);
  the pooled estimate carries a site random intercept / frailty term. Matched designs keep
  the matched set as the conditioning unit.

## Estimand and Primary Metric

Three explicitly-labeled targets. **E1 and E2 are different estimands, not a robustness
pair** — reporting one as a "sensitivity check" on the other would be the exact error
Boekel2023 warns about.

- **E1 — TOTAL EFFECT (primary, confirmatory).** Effect of pre-existing autoimmune stratum
  *s* (vs no autoimmune diagnosis) on PASC risk, **adjusting for confounders but NOT for
  acute severity** (severity is a mediator; conditioning on it removes the h0004 path we
  want inside the total effect). Adjustment set: age, sex, calendar/variant era,
  vaccination at index (**partly post-exposure — see caveat in *Model Assumptions***),
  baseline non-autoimmune comorbidity, **individual healthcare
  utilization**, prior-infection count. Metric: **risk ratio** (log-binomial / Poisson with
  robust SE) and risk difference per stratum.
- **E2 — CONTROLLED DIRECT EFFECT (primary, confirmatory, distinct).** Effect of stratum
  *s* on PASC **with acute severity set to a reference level** — the autoimmune→PASC effect
  *not routed through* acute severity. Requires the mediator-outcome no-unmeasured-confounder
  assumption (flagged in *Model Assumptions*). Metric: CDE risk ratio.
- **E3 — MEDIATION DECOMPOSITION (optional, exploratory).** Total = natural direct +
  natural indirect (via severity), **only if** infection-date, severity timing, and dated
  pre-index autoimmune diagnosis are all clean enough to satisfy cross-world assumptions.
  Reported as NDE/NIE with proportion mediated; explicitly downgraded to exploratory.

**Focal effect-modification estimand (the point of t078):** the **sex × autoimmune-stratum
interaction**, reported on **both scales** — multiplicative (ratio of stratum RRs, female
vs male) and **additive (RERI)**, since additive interaction is the decision-relevant
form for effect modification. Sex-stratified estimates are reported for every stratum
regardless of interaction-test significance.

## Model / Test Assumptions

- **E1 total effect** identifies under no-unmeasured-confounding of the autoimmune→PASC
  relationship given the adjustment set (age, sex, era, vaccination, baseline comorbidity,
  utilization, prior-infection count) and correct exposure temporality.
- **Vaccination-adjustment caveat (named, not silent).** Vaccination at index is only
  partly a pre-exposure confounder. If pre-existing autoimmune diagnosis affected
  vaccination **eligibility or timing** (e.g. immunosuppressed patients prioritized,
  deferred, or hesitant), some of the vaccination variable is **post-exposure** relative to
  the autoimmune status, and adjusting for it can **block an exposure-driven prevention
  path** (autoimmune status → vaccination behavior → PASC) that arguably belongs inside the
  total effect. This may still be the correct choice for the **biological-susceptibility
  estimand** (asking whether autoimmune biology raises PASC risk *holding vaccination
  fixed*), but the two framings differ. Pre-commit: report E1 **with** vaccination adjusted
  (biological-susceptibility framing, primary) and carry an **unadjusted-for-vaccination**
  variant as a pre-registered sensitivity contrast; if they diverge materially, the
  vaccination-mediated path is itself a finding (parallels the E1-vs-E2 severity logic).
- **E2 CDE** additionally requires **no unmeasured mediator–outcome confounder** (a common
  cause of acute severity and PASC, e.g. frailty, biases the CDE and can induce
  collider bias when severity is conditioned on). This assumption is strong and is the
  main reason E2 is reported *alongside* E1, never *instead of* it.
- **E3** requires the stronger sequential-ignorability / cross-world assumptions; treated as
  exploratory.
- Log-binomial models may fail to converge at extreme risks → pre-committed fallback to
  modified-Poisson with robust variance.
- Multi-site pooling assumes exchangeable site effects (random intercept); heterogeneity is
  reported (τ², prediction interval), not averaged away.

## Power Floor or Resolution Limit

- The binding constraint is **cell count in rare-stratum × sex × PASC** combinations
  (vasculitis, myositis, MS in males especially). Pre-specify a **minimum informative cell
  size**; strata below it are **pooled per a pre-registered hierarchy** (organ-specific vs
  systemic-rheumatic vs genetic-risk-only), never silently dropped.
- A **null in an underpowered stratum is non-arbitration, not evidence of no effect** — the
  plan commits to reporting the achievable minimum detectable RR per stratum, and to
  labeling under-resolved strata explicitly.
- The **additive interaction (RERI)** is materially more data-hungry than the main effect;
  its power floor is stated separately and is expected to bind first.

## Bias vs Variance Risks

The dominant error is **bias, not variance** — larger N does not fix it (the
`statistics-bias-vs-variance-decomposition` rationale).

- **h0008 differential-ascertainment (pre-committed primary threat).** Autoimmune patients
  are higher-utilization → more encounters → **more opportunities to be coded with PASC**,
  independent of true risk. And autoimmune disease and PASC are **both female-predominant**,
  so a sex-pooled or sex-unadjusted association is confounded by construction. Defenses:
  individual-level utilization adjustment; a **negative-control outcome** that is
  ascertainment-sensitive but not mechanistically tied to autoimmune→PASC (to detect
  residual surveillance bias); and preference for **population-based sampling**
  (OpenSAFELY/All of Us) over clinic-ascertained.
- **Exposure misclassification** from prevalent-code-as-incident and pooled strata (Hill's
  gap) → managed by the dated-lookback rule and versioned codelists.
- **Mediator conditioning (E2).** Conditioning on severity can open a collider path
  severity ← U → PASC; carried as an explicit assumption + bias analysis, not ignored.
- **Immortal-time / index-date** artifacts from survival-window definitions → fixed offsets.

## Sensitivity Arbitration

Pre-committed rules for when analyses disagree:

1. **E1 vs E2 divergence is a finding, not a conflict.** A large total effect that shrinks
   under E2 is *evidence of severity mediation* (the Boekel2023 pattern), reported as such —
   not grounds to prefer either number.
2. **E-value** on the primary E1 estimate; if the E-value is below plausible
   utilization/frailty confounding strength, the estimate is declared **not
   ascertainment-robust**.
3. **Negative-control outcome** must be null; a non-null negative control **caps the
   credited effect size** via the observed bias.
4. **Population-based vs clinic-ascertained** vehicles disagreeing → OpenSAFELY arbitrates the
   **sampling-frame** contrast for the h0008 concern (pre-committed), **but not the outcome
   channel.** BC-5 (`interpretation:0033`) sharpened this: broadening beyond the coded outcome
   **reshapes — and may worsen — the differential-by-utilisation bias** (every long-COVID code is
   generated at an encounter; referral/symptom codes are *more* contact-dependent, pulling in more
   of the high-utilisation/autoimmune/female-enriched population), so **no** OpenSAFELY phenotype —
   coded-only or broad — is a clean outcome-side arbiter. OpenSAFELY's arbiter role is therefore
   limited to the sampling-frame axis and is **conditional on** running the coded-diagnosis-only vs
   coded-any **bracketing pair** plus pre-pandemic-utilisation adjustment and the negative-control
   outcome; the outcome-side gradient is handled analytically in both vehicles, not assumed away.
5. **Interaction scale disagreement** (multiplicative present, additive absent or vice
   versa) is reported on both scales; the additive/RERI result is primary for the
   effect-modification claim.

## Required Output Artifacts

- A locked **codelist bundle** (autoimmune strata, PASC, severity, utilization windows),
  versioned and committed before extraction.
- A **per-stratum × sex** table of E1 (RR + RD), E2 (CDE), and where run E3 (NDE/NIE),
  with cell counts and minimum detectable effects.
- The **interaction panel**: multiplicative ratio-of-RRs and additive RERI, with CIs.
- The **negative-control** result and **E-value** table.
- A **vehicle-feasibility memo** recording which candidate cleared BC-1..BC-7 and why the
  primary vehicle was chosen.
- Site-heterogeneity diagnostics (τ², prediction interval) for any pooled estimate.

## Aspect-contributed Sections

None. No project- or task-scoped analysis aspect (expression/genomics/etc.) applies; this
is an observational causal effect-modification design. The relevant methodology is carried
by the four loaded `statistics-*` leaves recorded in `skills_loaded`.

## Readiness Decision

**`not-ready`** (design-stage). The estimands (E1 total, E2 controlled-direct, E3 optional
mediation), the effect-modification target (sex × stratum, additive + multiplicative), the
adjustment strategy, the h0008 pre-commitment, the negative-control/E-value arbitration,
and the vehicle ranking are all **locked**. Execution and pre-registration remain gated on
the dataset checks below — no vehicle has been access-verified for the required autoimmune
granularity, severity timing, individual utilization, and stratum × sex cell counts.

## Blocking Checks Before Pre-Registration

Each becomes a `science tasks` blocker (created below). These are the vehicle-admissibility
gates the eventual data-gated pre-registration will reference by name.

- **BC-1 — Vehicle selection + OpenSAFELY discovery. ✅ RESOLVED 2026-07-01
  (`interpretation:0031`).** N3C = primary (mature computable PASC phenotype + open synthetic
  tier + rare-stratum scale); OpenSAFELY = pre-committed population-based replication
  (`dataset:opensafely-longcovid` created), **not primary** because coded long COVID is
  differentially under-recorded. All of Us = diverse triangulation.
- **BC-2 — Access verification.** Resolve the access path for the chosen vehicle (N3C
  enclave DUA / OpenSAFELY approval / All-of-Us Workbench); prototype on N3C synthetic tier.
- **BC-3 — Autoimmune stratum granularity. ✅ LARGELY RESOLVED 2026-07-01
  (`interpretation:0032`).** Both vehicles **support the eight planned disease-specific strata**
  with dated pre-index onset (fixes Hill's pooled-Charlson gap) — **7/8 clean, autoimmune-thyroid
  only partially resolved**: N3C via OMOP concept sets (SLE/RA/Crohn's/UC
  = OHDSI Phenotype Library cohorts #119/#196/#198/#201; rest author-built from SNOMED),
  OpenSAFELY via NHSD SNOMED refsets (Sjögren/myositis/vasculitis-subtype-union now confirmed).
  **Residuals:** (a) **autoimmune-thyroid** is the convergent weak stratum — isolable Graves but
  not autoimmune-*hypo*thyroid in either coding system → conservative Graves+Hashimoto-specific
  primary definition + all-cause-inclusive sensitivity stratum; (b) OMOP concept_ids unverified
  (→ `task:t081`); (c) three a-priori scoping decisions to pre-register (vasculitis union,
  autoimmune-thyroid specific-primary, myositis exclusions). Pooling hierarchy assigned:
  systemic-rheumatic {SLE, RA, Sjögren, vasculitis, myositis} / organ-specific {IBD, MS,
  autoimmune-thyroid} / genetic-risk-only tier is **not EHR-resolvable** (genotype modality,
  belongs to `question:0005`). Cell counts are BC-4, not BC-3.
- **BC-4 — Sex-interaction support.** Confirm sex × stratum × PASC cell counts clear the
  power floor for at least the systemic-rheumatic and organ-specific groups.
- **BC-5 — PASC case definition. ✅ RESOLVED 2026-07-01 (`interpretation:0033`).** N3C primary =
  **coded U09.9-or-LC-clinic** computable phenotype (Hill-replicable), WHO-aligned **≥90 d**
  ascertainment window (separated from the ≥45 d survival/inclusion window). The N3C **ML
  computable phenotype** (`paper:Pfaff2022`) is **demoted to a flagged sensitivity endpoint, not
  primary** — its top feature is outpatient visit rate (so the outcome is utilisation-gated by
  construction, the h0008 axis under study), with an untested sex-specific error profile on top
  (75% female training positives, sex excluded, no by-sex performance reported → a sex-proxy-leakage
  *risk*, not a verified bias). The utilisation argument alone justifies the demotion.
  The **RECOVER PASC index** (`paper:Thaweethai2023`) is **survey/PRO-only → not EHR-computable**;
  it is a construct anchor via `dataset:recover-adult`, never an N3C endpoint. OpenSAFELY primary =
  **NICE 3-cluster coded** (diagnosis+referral+assessment) pooled, with **coded-diagnosis-only vs
  coded-any** as a bracketing sensitivity pair; a symptom-temporal phenotype is exploratory-only
  (59% of coded cases lack a positive-test anchor; symptom-code PPV low). **Meta-finding:** every
  EHR PASC outcome is utilisation-gated on the outcome side → the ascertainment defence lives in the
  design (utilisation adjustment + negative control + bracketing pairs), not in a clean outcome.
- **BC-6 — Acute-severity measurement + timing.** Confirm severity events are dateable in
  the acute window so the mediator role is identified (gates E2/E3).
- **BC-7 — Individual-level utilization.** Confirm individual encounter-count covariate is
  buildable from a fixed pre-index window (replaces county proxy).

When BC-1..BC-7 clear, this plan moves to `ready-with-caveats` and routes to
`/science:pre-register` as a `data-gated` pre-registration whose G-gates are these BCs.

## Feedback Reflection

No template friction to report; the design-stage causal path and the menopause precedent
(`plan:2026-06-19-menopause-pais-total-effect-analysis-plan`) mapped cleanly onto this
estimand.
