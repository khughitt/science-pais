---
id: interpretation:0035-t079-bc7-individual-utilisation
kind: interpretation
title: "t079/BC-7: individual-level utilisation buildable in both vehicles (replaces Hill's county proxy) — but it is a DUAL-ROLE variable (ascertainment confounder AND consequence of the autoimmune exposure), measured with vehicle-specific error; the ascertainment defence is bounded, not clean"
status: active
source_refs:
  - paper:Hill2022
  - cite:Williamson2020
  - cite:Andrews2022
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
  - interpretation:0034-t079-bc6-acute-severity-dateability
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - question:0007-mechanism-of-female-predominance-in-pais
created: "2026-07-01"
updated: "2026-07-01"
input: "BC-7 individual-utilisation buildability audit (2026-07-01): re-read of paper:Hill2022 (county physicians-per-1000 proxy + acknowledged ascertainment effect) against the native individual-level utilisation fields already recorded in dataset:n3c-recover-longcovid (OMOP visit_occurrence) and dataset:opensafely-longcovid (ehrQL clinical_events / consultations). No participant-level data accessed; no access gate for this check."
prior_interpretations:
  - interpretation:0034-t079-bc6-acute-severity-dateability
relations: []
---

<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (BC-7 of plan:0005 / task:t079). Utilisation-covariate
buildability + adjustment-role audit only; no participant-level data, no covariate execution. -->

# Interpretation: t079/BC-7 — individual-level utilisation

## Verdict

**Both vehicles natively build an individual-level pre-index encounter-count covariate from a
fixed lookback, so BC-7 clears the literal buildability gate and Hill2022's county-level
"physicians-per-1,000-residents" proxy is replaced by a per-patient measure — the third of
Hill's three gaps closed.** But the load-bearing result is what the covariate *is*, not that it
exists: individual utilisation is a **dual-role variable**. It is simultaneously **(a)** the
ascertainment-opportunity confounder the study must adjust — more healthcare contact → more
chances to be *coded* with both the autoimmune exposure and the PASC outcome, independent of true
biology (the h0008 mechanism BC-3 and BC-5 documented on the two channels) — **and (b)** a
**partial consequence of the autoimmune exposure itself**: autoimmune disease mechanically
generates encounters (monitoring, DMARD scripts, flares), so pre-index contact sits *on the
causal path* from the exposure. These two roles pull in opposite directions: **naive adjustment
over-adjusts away a legitimate part of the exposure's footprint (and can open a collider path);
non-adjustment leaves the ascertainment bias in.** So BC-7's real deliverable is not "utilisation
is available" but a **pre-committed adjustment-framing pair** (adjusted = ascertainment-control,
primary; unadjusted = biological-footprint, sensitivity) whose divergence is itself informative —
structurally identical to the E1↔E2 severity split (BC-6) and the vaccination-adjustment caveat
already in `plan:0005`. On top of that the covariate is measured with **vehicle-specific error**
(N3C undercounts out-of-network care; OpenSAFELY GP-complete but blind to private care) and its
meaning **drifts with pandemic-era telehealth / deferred care**. The honest conclusion: BC-7
confirms the **ascertainment defence is buildable but bounded** — a mitigation quantified by the
negative-control outcome and E-value, not a clean fix. This closes the h0008 loop: BC-3
(exposure), BC-5 (outcome), BC-6 (mediator) each showed the measurement channel shapes the
signal; BC-7 shows the *defence* against it is itself measurement-limited.

## Findings Summary — utilisation buildability per vehicle

| | N3C (`dataset:n3c-recover-longcovid`) | OpenSAFELY (`dataset:opensafely-longcovid`) |
|---|---|---|
| **Native field** | OMOP `visit_occurrence` (± `visit_detail`) counted per patient | ehrQL `clinical_events` / `consultations` per patient |
| **Covariate** | pre-index encounter counts by visit type (outpatient / ED / inpatient / telehealth) over a fixed lookback | pre-index GP-consultation counts over a fixed lookback |
| **Replaces** | Hill's county physicians-per-1,000 (area-level proxy) | (Hill's design substrate; individual from the start) |
| **Completeness** | **partial** — only care at N3C-contributing sites; out-of-network care invisible → differential undercount by insurance/geography | **near-complete for registered patients** (GP gatekeeper); misses private / out-of-NHS care |
| **Failure mode** | "low utilisation" conflates *truly low contact* with *care outside contributing sites* | "low utilisation" ≈ genuinely low GP contact (stronger), but private care and coding-behaviour vary by practice |

Both clear the gate; the **N3C undercount is the more serious differential-missingness** — the
very covariate meant to fix differential ascertainment is itself differentially observed in the
primary vehicle, which is why the defence is bounded rather than clean.

## The load-bearing finding — utilisation is a confounder AND a consequence of the exposure

Draw the paths BC-7 makes explicit, **distinguishing latent/true autoimmune disease `D` from the
recorded autoimmune diagnosis `E_obs` — the coded exposure the study actually uses.** Collapsing
`D` and `E_obs` into "autoimmune status" is exactly what makes utilisation look like one
ambiguous object; separating them makes the graph clean:

- **Measurement-machinery path — recorded exposure (`contact` is UPSTREAM of `E_obs`):**
  `contact → E_obs` and `contact → coded-outcome`. A healthcare encounter is *required* for true
  disease to become a **coded** diagnosis and for PASC to become a **coded** outcome, so
  higher-utilisation patients are more likely to have both *recorded*, inflating the apparent
  association independent of biology. Here utilisation is **upstream measurement machinery** — the
  path the covariate exists to block.
- **Disease-footprint path — true disease (`contact` is DOWNSTREAM of `D`):** `D → contact`. True
  autoimmune disease raises baseline healthcare use *because it is disease* (monitoring, DMARDs,
  flares), so utilisation is partly a **downstream footprint of `D`**; conditioning on it removes a
  slice of the exposure's real signature and, because contact has other causes, can turn the
  covariate into a **collider** (`D → contact ← other-causes → coded-outcome`).

So the dual role is not a paradox: **for the recorded exposure `E_obs`, utilisation is upstream
measurement machinery; for true disease `D`, it is a downstream disease footprint.** There is no
single adjustment correct for both roles — the same structure behind the `plan:0005`
vaccination-adjustment caveat and the E1/E2 severity split — but the graph is unambiguous once `D`
and `E_obs` are kept separate, which the pre-registration should state explicitly.
**Resolution (pre-register):**

1. **Split utilisation by care setting.** Use **pre-index OUTPATIENT / primary-care contact** as
   the ascertainment-opportunity adjuster in E1; keep **inpatient contact out of the E1 adjustment
   set** — inpatient use is severity-adjacent (a mediator, BC-6), so it must ride the F6 severity
   denylist, not the confounder set. Counting total encounters without this split would smuggle
   the mediator into the total-effect model.
2. **Pre-committed adjustment-framing pair.** Report E1 **utilisation-adjusted** (ascertainment-control
   framing, **primary**) and **utilisation-unadjusted** (biological-footprint framing, sensitivity);
   material divergence is a *finding* about how much of the association is ascertainment vs biology,
   not a nuisance to average away.
3. **Fixed PRE-index window only.** Build the covariate from a fixed pre-index baseline (candidate
   365 d, ≥1 qualifying encounter to establish observation); **never** post-index contact
   (post-index use is a consequence of both severity and PASC → over-adjustment / collider).
4. **Sharpen the negative-control-outcome spec.** Because `D → contact` raises utilisation
   *globally*, strict "autoimmune-independence" is too high a bar — autoimmune disease lifts
   contact for almost everything. The right constraint: the negative-control outcome must be
   **encounter-sensitive but neither autoimmune-specific nor mechanistically downstream of
   autoimmune disease** (not part of autoimmune monitoring/treatment), and its **baseline
   association with the autoimmune strata is then checked empirically** and discounted if non-null.
   Otherwise it absorbs true exposure signal and under-reports residual ascertainment bias. BC-7
   adds this constraint to the negative-control choice in `plan:0005`.

## Case-definition / window flag (per AGENTS.md)

- **Pre-index utilisation lookback** = a fixed offset (candidate **365 d** before index),
  explicitly a *fourth* named window alongside acute-severity (≤28 d, BC-6), survival/inclusion
  (≥45 d), and PASC ascertainment (≥90 d). All utilisation counting is **strictly pre-index** by
  construction.
- **Pandemic-era drift:** a 365 d pre-index window spans very different utilisation *regimes* by
  index date (a 2020 index sees pre-pandemic baseline; a mid-2021 index sees telehealth-surged /
  deferred-care baseline), so the covariate is entangled with calendar/variant era (already a
  covariate). Pre-commit era-interaction or within-era normalisation of the utilisation term.

## Evidence Quality

Feasibility-grade, fully durable, **no access gate**. The county-level proxy being replaced and
its acknowledged ascertainment effect are read directly from `paper:Hill2022` (in-hand); the
individual-level fields are the native OMOP `visit_occurrence` and OpenSAFELY ehrQL
`clinical_events`/`consultations` surfaces already recorded in the two dataset entities
(`cite:Williamson2020`, `cite:Andrews2022`). The load-bearing inference — that utilisation is a
confounder *and* a consequence of the autoimmune exposure — is a standard causal-structure
argument applied to the documented `autoimmune → higher-utilisation` fact, not a new empirical
claim.

## Sources (durable pointers)

Checked 2026-07-01.
- **County proxy being replaced + ascertainment acknowledgement:** `paper:Hill2022` (BMC Public
  Health 2023;23:2103, `doi:10.1186/s12889-023-16916-w`, PMID 37880596) — physicians-per-1,000
  county SDoH; authors state "having access to healthcare services increases the likelihood of
  diagnosis and/or treatment at a long-COVID clinic."
- **N3C individual utilisation:** OMOP CDM `visit_occurrence` / `visit_detail` (standard N3C
  enclave surface; `dataset:n3c-recover-longcovid`).
- **OpenSAFELY individual utilisation:** ehrQL `clinical_events` / `consultations` per patient
  (`dataset:opensafely-longcovid`; platform established `cite:Williamson2020`, `cite:Andrews2022`).

## Data Quality Checks

Structural utilisation-QA facts carried into `plan:0005`/`plan:0006`:
- **Dual role → split by setting.** Pre-index outpatient/primary-care contact = ascertainment
  adjuster (E1 confounder set); inpatient contact = severity-adjacent (F6 denylist, mediator side).
- **Adjustment-framing pair** (utilisation-adjusted primary / unadjusted sensitivity); divergence
  is a finding.
- **N3C differential undercount** (out-of-network care invisible) is the primary vehicle's key
  covariate-measurement weakness → the defence is bounded; quantify residual via negative control +
  E-value.
- **Negative control:** encounter-sensitive but **not autoimmune-specific and not mechanistically
  downstream of autoimmune disease** (not strict independence — `D` raises contact globally);
  baseline association with the strata checked empirically, or it absorbs true signal.
- **Era/telehealth drift** entangles the utilisation term with calendar era → era-interaction /
  within-era normalisation.
- **Strictly pre-index window** (candidate 365 d); post-index contact is over-adjustment.

## Proposition-Level Updates

None. BC-7 is a covariate-infrastructure / adjustment-role check; no `proposition:` gains or loses
an evidence-line.

## Hypothesis-Level Implications

- `hypothesis:0008` (measurement-channel / ascertainment) — BC-7 completes the loop and **qualifies
  the defence, not just the threat**. BC-3/BC-5/BC-6 showed the measurement channel shapes the
  apparent signal on exposure, outcome, and mediator; BC-7 shows the **primary analytic defence
  against that channel (individual-utilisation adjustment) is itself measurement-limited** — it is
  a dual-role variable, differentially undercounted in the primary vehicle, and era-entangled. So
  h0008's operational conclusion sharpens from "adjust for utilisation" to "the ascertainment
  defence is a **bounded mitigation** (adjustment-framing pair + a not-autoimmune-specific negative
  control + E-value), whose adequacy is *quantified, not assumed*." The negative-control and
  E-value results — not the utilisation adjustment alone — become the actual ascertainment arbiter.
- `question:0007` (female-predominance mechanism) — because autoimmune disease and higher
  utilisation are **both female-skewed**, the dual-role problem is itself sex-patterned; the
  utilisation-adjusted vs unadjusted divergence should be read *by sex*, since over-adjustment
  would preferentially attenuate the female-stratum estimate (folds into the BC-4/analysis stage).

## Evidence vs. Open Questions

**Settled (BC-7):** individual pre-index utilisation is buildable in both vehicles (OMOP
`visit_occurrence`; ehrQL `consultations`) → Hill's county proxy replaced; the covariate is
dual-role (`D`-footprint + `E_obs`-measurement-machinery) → split outpatient (E1 adjuster) vs
inpatient (mediator/denylist), adjustment-framing pair (adjusted primary / unadjusted sensitivity),
strictly pre-index window; negative control not-autoimmune-specific / not-downstream (baseline
association checked); N3C differential undercount + era drift acknowledged. **Still open:** **BC-4**
(sex × stratum × PASC cell counts — the binding unknown, and largely **access-gated** on the N3C
enclave) and **BC-2** (access verification). With BC-1/BC-3/BC-5/BC-6/BC-7 cleared, the
**literature-progressable design work is complete — but BC-4 remains an open design gate, not only
a counting exercise**: the observed counts can still force **stratum pooling**, **endpoint choice**
(the coded-primary is less sensitive → fewer cells), and **interaction-scale expectations**
(additive/RERI binds first). Its design consequences are simply unresolvable until the enclave
counts exist, so design feasibility is *not* fully settled — it is access-gated.

## New Questions Raised

- How large is the utilisation-adjusted vs unadjusted E1 divergence, and is it sex-patterned
  (does adjustment attenuate the female stratum more)? A large sex-patterned divergence would be
  direct evidence that part of the apparent female autoimmune→PASC excess is ascertainment, not
  biology. (Folds into BC-4/analysis on `task:t079`; no standalone `question:` reserved.)

## Limitations & Residual Uncertainty

- **The bound is unquantifiable at design stage.** *That* utilisation is a bounded defence is a
  structural certainty; *how* bounded (the size of the N3C undercount, the era drift, the residual
  after adjustment) is only measurable once cohorts and the negative-control/E-value results exist.
- **No single correct adjustment.** The dual-role tension has no design-stage resolution beyond the
  framing pair; which framing is "right" depends on the target (ascertainment-control vs
  biological-footprint), and the plan reports both by construction.
- **Vehicle-specific missingness models** (N3C out-of-network, OpenSAFELY private/practice-coding
  variation) are asserted qualitatively from platform structure, not measured.

## Updated Priorities

1. **The literature-progressable design work is complete; BC-4 remains an open design gate that is
   access-gated.** BC-1/BC-3/BC-5/BC-6/BC-7 are resolved. **BC-4 is not merely counting** — the
   observed sex × stratum × PASC cell counts can still force **stratum pooling**, **endpoint
   choice**, and **interaction-scale expectations** (additive/RERI binds first), so design
   feasibility is *not* fully settled; those consequences are just unresolvable until the enclave
   counts exist. `plan:0005` stays `not-ready`, blocked on access/execution for **BC-2** and on
   access-plus-design for **BC-4** — the natural next milestone is the BC-2 access track (or a BC-4
   scoping pass on published marginals) rather than another literature check.
2. **Propagate the utilisation lock into `plan:0006` WP4**: build the pre-index utilisation
   covariate **split outpatient vs inpatient**, emit **utilisation-adjusted and -unadjusted E1
   variants** (mirroring the existing vaccination pair), route inpatient contact to the F6 severity
   denylist, and pin the 365 d pre-index window in `windows.yaml`. WP stays code-gated (`t082`).
3. **Update `plan:0005`**: mark BC-7 resolved; add the dual-role (`D`-footprint vs
   `E_obs`-measurement) caveat + adjustment-framing pair to the E1 adjustment set; add the
   **not-autoimmune-specific / not-downstream + empirical-baseline-check** constraint to the negative-control
   spec; note the outpatient/inpatient split and the era/telehealth drift.
