---
type: plan
id: plan:2026-06-19-menopause-pais-total-effect-analysis-plan
title: "Analysis plan: total effect of menopausal transition on PAIS risk (t016)"
date: 2026-06-19
created: "2026-06-19"
updated: "2026-06-19"
related:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - patch-definition:menopause-pais-causal-dag
  - task:t016
  - task:t015
  - task:t017
  - task:t020
status: not-ready
skills_loaded:
  - id: statistics-bias-vs-variance-decomposition
    reason: confounding (latent U) is the dominant error term and cannot be shrunk by sample size — must be separated from sampling variance explicitly
  - id: statistics-sensitivity-arbitration
    reason: multiple pre-committed adjustment sets, E-value bounding, and a collider-exclusion negative control whose disagreement changes the verdict
  - id: statistics-power-floor-acknowledgement
    reason: the perimenopause-vs-menopause contrast (t020) and a non-clinic population cohort risk subgroup underpowering; a null must be distinguished from non-arbitration
  - id: statistics-survival-and-hierarchical-models
    reason: PAIS outcome is naturally time-to-recovery (or persistence-at-follow-up) and any pooled estimate is multi-cohort, requiring a frailty/random-intercept structure
---

# Analysis Plan: total effect of menopausal transition on PAIS risk (t016)

This plan operationalizes the **locked total-effect estimand** from the t014
causal DAG (`inquiry:menopause-pais-causal-dag`) into a pre-registerable
observational analysis, incorporating every correction surfaced by the
adversarial critique (`doc/inquiries/menopause-pais-causal-dag-critique.md`).

It is a **design-stage** plan. The analytic design is locked, and as of the
2026-06-19 updates the **cohort-identification gate is resolved**: t015 identified
**UK Biobank** as the admissible primary vehicle (population-based, low-collider,
pre-infection baseline, questionnaire menopause staging) — see the addendum to
*Blocking Checks* below. The readiness verdict remains **not-ready** for a narrower
reason: the analysis is not yet pre-registerable because UKB data is not in hand and
the **U-proxy / outcome measurement schema (t017)** is still open. The exposure-side
gate **t020** is now design-resolved
(`doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md`). The
remaining blocking checks map to existing tasks, not new duplicates.

## Analysis Question

In natal females, does **reproductive stage (premenopausal → perimenopausal →
postmenopausal), assessed at the time of acute infection**, causally raise the
risk / delay the resolution of a post-acute infection syndrome (PAIS)?

This is the *total* effect — deliberately **through** the hormone-driven immune,
endothelial, and autonomic mediators, consistent with h0005's conjecture that
menopause is a threshold-shifter, not a direct cause.

## Related Hypotheses / Inquiries / Tasks

- **Hypothesis:** `h0005` reproductive-stage immune homeostatic margin (primary);
  the reverse-direction proposition (PAIS → HPG axis) is **out of scope** here and
  belongs to `t021`, kept separate to preserve acyclicity.
- **Question:** `q0013` reproductive-stage failed immune recovery; `q0007`
  female-predominance is a *different* estimand (male-vs-female), not this one.
- **Inquiry:** `menopause-pais-causal-dag` (locked estimand + critique).
- **Tasks:** `t016` (this plan) · `t015` (cohort) · `t017` (measurement schema) ·
  `t020` (exposure window) · `t008` (pre-infection-baseline cohort catalogue).

## Data Inputs and Provenance

No data acquired yet. The plan specifies what an **admissible** input must be:

| Requirement | Why (DAG/critique) | Task |
|---|---|---|
| **Population-based** sampling frame (cohort, registry, biobank) | Clinic samples condition on the `clinic_attendance` collider by construction → manufactured association | t015, t008 |
| **Pre-infection baseline** with reproductive stage staged *at infection* | Post-hoc staging lets PAIS perturb the HPG axis and contaminate the exposure (reverse causation) | t008, t020 |
| Natal-female restriction recorded | Population-definition given; menopause undefined otherwise | t017 |
| Age at infection | The single load-bearing confounder (minimal sufficient set) | t017 |
| **U-proxy battery:** SES, prior EBV serostatus, autoimmune history | Promote from latent U to measured proxies to partially close the back-door | t017 |
| Acute severity, vaccination/reinfection era, calendar period/variant | Mediator (severity) + candidate confounder of mediator paths (era) | t017 |
| Baseline cardiometabolic comorbidity, timestamped vs menopause | Needed only for the sensitivity arm (see Estimand) | t017 |
| Outcome: PAIS status + time-to-resolution by a **stated case definition** | WHO vs CDC vs Fukuda/CCC/ICC change apparent prevalence (AGENTS.md) | t017, t002 |

Provenance must reach `datapackage.json` grade before execution (frictionless).

## Required Input Inspection

1. **Sampling-frame audit** — confirm recruitment was *not* conditioned on
   symptomatic care-seeking. If any clinic/post-COVID-clinic recruitment exists,
   either exclude that stratum or model the selection explicitly. This is a
   **vehicle-admissibility gate**, not a covariate choice.
2. **Exposure-timing audit** — verify reproductive stage is fixed at/before the
   acute infection date for every participant; flag and quarantine post-hoc-staged
   records.
3. **Outcome case-definition audit** — one declared definition; record it; do not
   silently pool incompatible definitions across sub-cohorts.
4. **U-proxy completeness** — quantify missingness of SES / EBV / autoimmune
   history; missing-not-at-random here directly weakens identification.
5. **Independent-unit / clustering audit** — one row per participant; identify the
   study/site grouping for the hierarchical layer.

## Preprocessing / Normalization Checks

- **Reproductive-stage operationalization (t020 — now specified):** UKB **cannot**
  apply STRAW+10 directly (no prospective cycle data; **no FSH/AMH** in the panel;
  oestradiol floor-censored), so the exposure is a **projected reproductive stage at
  infection** — a decision-tree derivation from baseline questionnaire + age, with a
  per-woman forward-projection survival model and an explicit misclassification model
  + quantitative bias analysis. Three pre-committed tiers: (1) projected ordinal
  stage [primary], (2) probabilistic latent stage [honest interval], (3) binary
  post-vs-not [negative-control operationalization only — it misclassifies the
  perimenopausal at-risk window]. The pre-baseline (2006–2010) design converts most
  of the menopause↔PAIS symptom-overlap threat from *differential* to
  *non-differential* misclassification. Full spec:
  `doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md`.
- **Comorbidity time-split:** split into pre-infection *baseline* (candidate
  confounder) vs menopause-incident (mediator). A single untimed comorbidity
  variable is inadmissible for the sensitivity arm.
- **Hormone-therapy handling:** HT is a mediator + confounded-by-indication; it is
  **not** adjusted in the total-effect analysis. (The HT causal contrast is a
  separate target-trial estimand — t019.)
- **Era harmonization:** code calendar period / variant / vaccination era for the
  mediator-path confounding sensitivity.

## Independent Unit and Denominator

- **Independent unit:** individual natal-female participant with a confirmed (or
  serologically supported) acute infection and pre-infection baseline.
- **Denominator:** natal females in the population frame who had the acute
  infection — *not* those who presented to a clinic.
- **Grouping (hierarchical layer):** study / cohort / site as a random intercept
  (frailty) when pooling across data sources. Participants are nested in studies;
  studies are the borrowing-strength unit, **not** an inflated participant n.

## Estimand and Primary Metric

- **Primary estimand:** total effect of reproductive stage (ordinal:
  pre → peri → post, *at infection*) on PAIS outcome, in natal females.
- **Adjustment set: `{age at infection}` only.** (Sex-at-birth handled by
  population restriction.) This is the unique minimal sufficient set under the DAG
  assuming no unmeasured confounding — the critique's correction; **baseline
  comorbidity is dropped** from the primary set (it is not a parent of menopause,
  so adjusting it over-adjusts a mediator descendant and risks M-bias).
- **Do NOT adjust (mediators):** sex hormone levels, immune dysregulation,
  thromboinflammation/endothelial dysfunction, acute severity, HT.
- **Never condition (collider):** clinic attendance (enforced at the sampling-frame
  gate, not as a covariate).
- **Primary metric:** hazard ratio for time-to-PAIS-resolution (Cox/Weibull) **or**
  risk ratio for PAIS-present-at-fixed-follow-up (log-binomial), per outcome
  operationalization. Report on the log-HR / log-RR scale.
- **Secondary estimand:** severity-controlled *direct* effect (additionally
  conditioning on acute severity) — a different estimand, reported separately, not
  as a robustness check on the primary.

## Model / Test Assumptions

- **Identification:** the total effect is **not identifiable by adjustment alone**
  while U (SES, prior EBV/autoimmunity, genetic/HLA risk, health behaviours) is
  latent. The analysis is therefore explicitly a **partially-identified /
  sensitivity-bounded** design — the point estimate is interpretable only jointly
  with its E-value (see Sensitivity).
- **Survival assumptions:** time origin = acute-infection date; event =
  PAIS-resolution (or PAIS-onset, stated once); pre-specify the proportional-hazards
  check (Schoenfeld residuals, log-log plots). If PH fails, fall back to
  time-varying effects / RMST per the pre-committed rule, not a retained crossing-HR.
- **Hierarchical assumptions:** varying intercept by study before any varying
  slope; check group-level variance identifiability given the number of cohorts;
  non-centered parameterization if Bayesian and data-sparse.
- **Censoring:** check informative censoring by reproductive stage (e.g.
  differential loss-to-follow-up in postmenopausal strata).

## Power Floor or Resolution Limit

- **Floor stated before the run:** independent-unit n = natal females with
  baseline + infection + admissible (non-clinic) recruitment. Compute the minimum
  detectable log-HR/log-RR at α (two-sided 0.05, adjusted for the peri/post
  contrasts) and target power 0.8.
- **Biologically meaningful effect:** pre-declare the smallest reproductive-stage
  effect that would change h0005's standing (candidate: HR/RR ≈ 1.3 for
  post-vs-pre, to be fixed at pre-registration against the t015 literature).
- **Dominant risk — subgroup underpowering:** the peri-vs-post split (t020) divides
  an already sex-restricted, age-banded cohort into thin strata. A null in the
  perimenopause window is **non-arbitrating** unless its interval excludes the
  meaningful effect. Label such results `underpowered`, not "no effect."
- Do **not** count repeated visits or imputation draws as independent units.

## Bias vs Variance Risks

The defining feature of this analysis: **the dominant error term is bias, and no
amount of sample size removes it.**

| Error term | Source | Shrinks with | Diagnostic | Mitigation |
|---|---|---|---|---|
| **Confounding by U** | SES/EBV/genetic/behaviour common causes of stage & PAIS | *nothing observational* | E-value, U-proxy adjustment | proxies + bounding; downgrade to partial ID |
| Collider (clinic) selection | care-seeking conditioning | nothing — design flaw | sampling-frame audit | exclude clinic samples (gate) |
| Reverse causation | PAIS perturbs HPG axis | nothing — design flaw | exposure-timing audit | stage at infection (t020) |
| Outcome misclassification | menopause↔PAIS symptom overlap | better endpoints | objective biomarkers (topic:biomarkers) | differential-misclassification model |
| Sampling variance | finite participants | more participants | SE/CI/power | larger/ pooled cohort, hierarchical model |

Implication: throwing more participants at this question sharpens a possibly-biased
estimate. The plan's credibility rests on the **U argument**, not on n.

## Sensitivity Arbitration

Pre-committed rule (no post-hoc menu selection):

- **Primary verdict-bearing analysis:** `{age}`-adjusted total-effect HR/RR on a
  population (non-clinic) cohort, reproductive stage staged at infection.
- **Mandatory sensitivities (must run for the verdict to stand):**
  1. **E-value** for the point estimate and the CI limit nearest the null —
     report how strong an unmeasured U (on both stage and PAIS) would have to be to
     explain away the effect; compare against the strength of *measured* proxies as
     a benchmark.
  2. **U-proxy adjustment arm** — `{age, SES, prior-EBV, autoimmune-history}`;
     movement toward the null quantifies residual-confounding direction.
  3. **Collider negative control** — re-estimate within a *clinic-recruited*
     subsample (if any exists): a spurious association appearing there but absent in
     the population frame **confirms** the collider mechanism and vetoes any
     clinic-derived literature estimate.
- **Estimand-split (report both, do not average):** `{age}` vs
  `{age, baseline comorbidity}`. These answer different questions and the second is
  valid *only if* a `comorbidity → menopause-timing` edge is asserted (DAG v2,
  t023). Disagreement is reported as estimand-dependence, not reconciled.
- **Operationalization sensitivity:** STRAW+10 ordinal (primary) vs binary-menopause
  (secondary). Disagreement downgrades measurement confidence for the exposure.

```text
Primary verdict:
  supports_threshold_shift  if primary HR/RR away from null, E-value exceeds plausible-U benchmark, U-proxy arm robust
  fragile                   if primary away from null but E-value below benchmark OR U-proxy arm collapses it
  null_meaningful           if interval excludes meaningful effect AND power floor adequate
  unresolved/underpowered   if power floor inadequate (esp. peri window) or staging-at-infection unverifiable
Vetoes:
  collider_confounded       if effect present only in clinic subsample → reject as selection artifact
  reverse_contaminated      if exposure staged post-hoc → exposure inadmissible
```

## Required Output Artifacts

Per the survival/hierarchical skill, on execution emit
`results/<date>-menopause-pais-total-effect/model_qa/` with a `datapackage.json`:

```
input_manifest.json
analysis_dataset.parquet                 # one row per participant, U-proxies included
sampling_frame_admissibility.parquet     # clinic-exclusion + exposure-timing gate results
model_formula_or_config.yaml             # {age}-only primary; sensitivity arms enumerated
censoring_and_event_audit.parquet
survival_diagnostics.parquet             # Schoenfeld / log-log / PH decision
posterior_or_fit_diagnostics.parquet
sensitivity_results.parquet              # E-value, U-proxy arm, estimand-split, operationalization
qa_summary.md                            # independent unit, grouping, failed diagnostics, verdict label
```

## Aspect-contributed Sections

**hypothesis-testing.** The verdict feeds directly back to `h0005`: a
`supports_threshold_shift` label strengthens the reproductive-stage homeostatic-margin
conjecture; a `collider_confounded` or `reverse_contaminated` veto leaves h0005
unsupported-by-this-route and redirects effort to a within-person/discordant design.
Pre-register the confirmatory criterion before any cohort is unblinded.

**computational-analysis.** Execution orchestration (cohort harmonization →
staging → modeling → sensitivity) is non-trivial and should route through
`/science:plan-pipeline` once a cohort is admitted. The DAG-to-pgmpy export bug
(`fb-2026-06-19-001`) must be resolved or worked around so the adjustment set is
read from the materialized graph rather than re-authored by hand.

## Readiness Decision

**not-ready** — the analytic design is locked and internally consistent with the
critiqued DAG. As of 2026-06-19 the cohort-identification and pre-infection-baseline
gates are **resolved** (t015 → UK Biobank), so the original "no admissible dataset
exists" blocker no longer applies. The verdict stays **not-ready** for the narrower
reason that the analysis is not yet pre-registerable: UKB data is not in hand, and
the **U-proxy / UKB-outcome measurement schema (t017)** remains open. The exposure-side
gate (**t020**, reproductive-stage operationalization + misclassification model) is now
design-resolved. When t017 locks and access is in hand, the plan becomes
`ready-with-caveats` (carrying the limitations below) and `/science:pre-register` is
runnable.

## Blocking Checks Before Pre-Registration

These gate the pre-registration; each maps to an existing task (no duplicates):

| Blocking check | Vehicle-admissibility gate | Task |
|---|---|---|
| Identify ≥1 **population-based** (non-clinic) hormone-measured PAIS cohort | clinic-collider exclusion | ✅ **t015** (UK Biobank) |
| Confirm the cohort has **pre-infection baseline** + reproductive stage stageable *at infection* | reverse-causation exclusion | ✅ **t015** (UKB 2006–2010 baseline) |
| Finalize the minimum measurement schema incl. **U-proxy battery** (SES, EBV, autoimmune hx) | back-door partial closure | **t017** |
| Lock the **reproductive-stage exposure operationalization** (projected stage + misclassification model/QBA; STRAW+10 not directly applicable in UKB) | exposure definition | ✅ **t020** (design-resolved; internal validation deferred to input-QA) |
| Declare the single **PAIS case definition** for the outcome | outcome definition | ⚠️ **concept** resolved (t002); **UKB operationalization** open (t017) |

**Outcome case-definition — concept resolved by t002** (`topic:pais-case-definition-heterogeneity`):
adopt **WHO 2021 ≥3-month** as the primary outcome, operationalized with a
PEM-weighted instrument (RECOVER PASC index ≥12 or nearest available). Run the
analysis under three pre-committed definition operationalizations as a sensitivity
axis (folding into the Sensitivity Arbitration block): (1) WHO binary only (most
inclusive), (2) PASC index ≥12 (most PEM-sensitive), (3) WHO + functional-impairment
gate (SF-36 T<45). An effect stable across all three is *definition-stable*; an
effect present only under (1) likely reflects PEM-negative prolonged recovery rather
than attractor entry — which **changes the interpretation for h0005**.

This resolves the case-definition *concept*, but the **UKB operationalization
remains an open t017 measurement-schema gate, not a closed check**: per the t027
data-field spec (`doc/methods/2026-06-19-ukb-data-field-specification.md` §5.2), UKB
carries **no symptom-level PASC instrument** (definition 2 can only be approximated
from coded fatigue/PEM terms) and the **functional-impairment-gate fields
(definition 3) are unconfirmed**. So t017 must (a) verify which of the three
definitions UKB can actually compute from linked codes and (b) decide how to handle
the PEM-sensitivity shortfall — it cannot simply assume the cohort carries
symptom-level data.

**Vehicle resolved by t015** (`doc/searches/2026-06-19-hormone-menopause-pais-cohorts.md`):
**UK Biobank** is the primary vehicle — the only population-based, low-collider,
pre-infection-baseline (2006–2010) resource with female-inclusive,
questionnaire-staged menopause data (age at natural/surgical menopause + HRT) and
linked COVID/long-COVID outcomes. **Decisive measurement constraint:** baseline
**oestradiol is censored** by a 175 pmol/L assay floor and is unusable for
postmenopausal staging — so the treatment node is operationalized as
**questionnaire reproductive stage** (± usable baseline testosterone/SHBG), which
*confirms* the DAG's choice of reproductive stage (not serum estradiol) as the
treatment and routes the exposure-measurement burden to t020's misclassification
model. Triangulation/replication arms: **All of Us** (US, survey+EHR menopause),
**Lifelines** and **Generation Scotland** (population, questionnaire menopause, no
baseline assays); ONS-CIS and N3C are low-exposure triangulation only.
Note the ~decade baseline→infection gap and that the long-COVID outcome must be
researcher-engineered (questionnaire + GP/HES codes) under the t002 multi-definition
sensitivity axis. Nearest precedent: `paper:AlcaldeHerraiz2025` (UKB SHBG→long COVID).

The UKB **data-field basket** (menopause/HRT, age, U-proxies, COVID+HES/GP linkage,
engineered 3-definition long-COVID outcome) and **access plan** are now drafted in
`doc/methods/2026-06-19-ukb-data-field-specification.md` (t027) — this resolves the
*vehicle-field* uncertainty but adds an explicit **access gate** (UKB AMS
application not yet submitted; provisioning is weeks-to-months) that runs in
parallel with the design gates below.

The remaining **design** gate is now **t017** (U-proxy + UKB-outcome measurement
schema against UKB fields); the exposure gate **t020** is design-resolved
(`doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md` —
projected reproductive stage + misclassification model/QBA, its internal
repeat-assessment validation deferred to input-QA). Once t017 locks and a UKB access
decision is in hand, run `/science:pre-register` to fix the confirmatory criteria
above, then `/science:plan-pipeline` for execution orchestration.

## Feedback Reflection

- The plan-analysis template assumes a dataset is broadly in hand; for a
  **design-stage causal plan** (estimand locked, data not yet acquired) the
  "not-ready + blocking checks = existing tasks" pattern worked cleanly but is not
  explicitly described in the template. Logged as guidance feedback below.
- The collider-exclusion and reverse-causation gates are genuinely
  *vehicle-admissibility* gates (sample inadmissible), distinct from covariate
  choices — the template's framing of blocking checks as G-gates fit well.
