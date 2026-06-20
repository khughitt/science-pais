---
id: "pre-registration:0001-menopause-pais-total-effect"
type: "pre-registration"
title: "Pre-registration: total effect of reproductive-stage timing on long COVID in UK Biobank (menopause→PAIS)"
status: "committed"
committed: "2026-06-19"
mode: data-gated
spec: "entities/plans/2026-06-19-menopause-pais-total-effect-analysis-plan.md"
related:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - question:0007-mechanism-of-female-predominance-in-pais
  - patch-definition:menopause-pais-causal-dag
  - task:t016
  - task:t017
  - task:t020
  - task:t027
  - paper:AlcaldeHerraiz2025
commits_to:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
amendments:
  - date: "2026-06-19"
    ratified_by: "task:t029 (independent out-of-author review)"
    type: "pre-data amendment (not a fresh pre-registration)"
    change: >
      Primary adjustment set {age} → {age, smoking}, named the PRIMARY MEASURED
      adjustment set (NOT 'minimal-sufficient': no valid sufficient set exists while
      U is latent — see DAG critique). Smoking = baseline smoking history
      (never/former/current + pack-years/duration where available); baseline smoking is
      pre-infection but not necessarily pre-FMP, so it is a measured confounder, not a
      clean pre-menopause exposure. E-value benchmark and U-proxy arm redefined relative
      to the new primary set (U = unmeasured confounding BEYOND {age, smoking}).
    rationale: >
      Smoking is a measured strong common cause of earlier menopause and of
      long-COVID/COVID risk and mortality; sensitivity-only placement was an
      identification gap the bias audit missed. Reviewer ratified Q1 with the
      coding/wording modification above.
created: "2026-06-19"
updated: "2026-06-19"
---

# Pre-registration: total effect of reproductive-stage timing on long COVID in UK Biobank (menopause→PAIS)

**Target class.** Mixed, primarily **epistemic**. The epistemic commitment is an
interpretation rule for `h0005` (and the question `q0013` it answers): how to update
belief about reproductive-stage-as-immune-homeostatic-margin given the observed
effect. The operational portion is "run the **{age, smoking}**-adjusted total-effect
analysis (primary measured adjustment set; amendment Q1) on UK Biobank exactly as the
three design artifacts specify." `q0007` (male-vs-female
predominance) is a **different estimand** and is navigation context only — **not** a
commitment target.

**Execution-timing: `mode: data-gated`.** The vehicle (UK Biobank) is *identified
and admissible in principle* but **not provisioned**: a UKB AMS data-access
application is not yet submitted, and several field IDs await live confirmation. The
analysis is **design-complete but not executable**. Until an admissible, provisioned
vehicle clears the Vehicle-Admissibility Gate below, the standing verdict is
**`[?]` inconclusive-for-coverage** — this pre-reg produces **no `bears_on` belief
update** on h0005 until then. This is distinct from a null result (which would be
evidence).

**Lock inputs (the design is frozen against these):**
- Exposure: `doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md` §8 (t020)
- Outcome + covariates: `doc/methods/2026-06-19-ukb-outcome-and-uproxy-measurement-schema.md` §8 (t017)
- Vehicle / field basket / access: `doc/methods/2026-06-19-ukb-data-field-specification.md` (t027)
- Estimand / adjustment / arbitration: the t016 analysis plan (`spec` above)

> **Amendment APPLIED — ratified by t029 independent review (2026-06-19).**
> Source: `doc/methods/2026-06-19-confounder-open-questions-and-staged-amendment.md`.
> - **Q1 (applied):** primary adjustment set **`{age}` → `{age, smoking}`**, the
>   **primary measured adjustment set** (deliberately *not* "minimal-sufficient" — no
>   valid sufficient set exists while U is latent; see
>   `doc/inquiries/menopause-pais-causal-dag-critique.md`). Smoking = **baseline smoking
>   history (never/former/current + pack-years/duration where available)**; baseline
>   smoking is pre-infection but **not necessarily pre-FMP**, so it is a measured
>   confounder, not a clean pre-menopause exposure. E-value/U-proxy redefined vs the new
>   set (below).
> - **Q2 (deferred to DAG v2 / t023):** BMI stays **out** of the primary set — ambiguous
>   confounder-vs-mediator role; carried as a **sensitivity** covariate (baseline,
>   timing-split where possible); role fixed in DAG v2.
> - **Q3 (not promoted):** autoimmune-POI → confirmed-POI **quarantined/stratified** as a
>   distinct etiologic stratum (generic autoimmune-hx stays U-proxy); **frailty** →
>   selection/sensitivity model only; **parity** → staging input + DAG-v2 candidate, not
>   primary (avoids drifting to a reproductive-life-course estimand).
> - **Q4 (added):** **Mendelian-randomization triangulation arm** added under Exploratory
>   with a pleiotropy-/selection-robust guardrail battery — **triangulation only, not
>   confirmatory/co-primary**.

---

## Hypotheses Under Test

- **`h0005`** — reproductive-stage transitions alter the immune homeostatic margin and
  modify the risk of failed post-infectious recovery. The directional prediction:
  **lower estrogenic / later-reproductive-stage status → higher long-COVID risk /
  delayed resolution**, operating *through* hormone-driven immune, endothelial, and
  autonomic mediators (a threshold-shift, not a direct cause).
- **`q0013`** — does reproductive-stage transition change the probability of failed
  immune recovery after infection? This pre-reg is the UKB operationalization of that
  question, with the at-risk-window (peri) sub-question explicitly flagged as
  **UKB-underpowered** (see Feasibility).

---

## Feasibility Against Real Input Artifacts (pre-data, load-bearing)

Checked against the nearest precedent (`paper:AlcaldeHerraiz2025`, UKB long-COVID):

- **Cohort-age vs pandemic timing — the decisive constraint.** UKB baseline age is
  **40–69 (2006–2010)**; at infection (2020–2022) participants are **≈ 52–83**
  (precedent mean age-at-infection ≈ 66). With UK median natural menopause ≈ 51,
  **essentially all UKB natal females are postmenopausal at infection.**
  - *Premenopausal-at-infection* requires age < ~50 at infection → < ~37 at baseline
    → **below UKB's age-40 floor → ≈ 0 participants.**
  - *Perimenopausal-at-infection* (≈ 47–55) is a **thin sliver** of the youngest
    enrollees only.
  - ⇒ **The pre → peri → post-at-infection contrast is structurally near-unavailable
    in UKB.** The cohort aged out of the premenopausal window before the pandemic.
- **Consequence — the confirmatory exposure is reproductive-stage *timing*, not
  current stage.** The exposure with real variance in UKB is **age at menopause** and
  **time-since-menopause at infection** among a near-uniformly-postmenopausal cohort.
  This is the UKB-supportable realization of the locked "reproductive stage" estimand;
  the pre/peri-vs-post contrast is **routed to the younger triangulation cohorts**
  (All of Us, Lifelines) and is **exploratory** in UKB.
- **Effective n (order of magnitude, to be confirmed on provisioning).** Precedent LC
  cohort = 8,668 (positive PCR ∧ questionnaire), 2,751 cases. Natal-female restriction
  → ~4,000–4,500 women; female long-COVID rate is higher, so ~1,200–1,600 female
  cases — adequate for a **timing** exposure across the (post) cohort, but the
  **pre/peri cell ≈ 0**, confirming the reframe above.

**Design fix applied here (not deferred to post-data):** the **primary confirmatory
contrast is the reproductive-timing exposure**; the stage-at-infection ordinal is
demoted to an exploratory/triangulation contrast. This inversion is made pre-data
because the artifacts were inspected before thresholds were locked.

---

## Expected Outcomes

- **Primary (confirmatory):** earlier age at menopause / longer time-since-menopause
  at infection is associated with **higher** probability of WHO ≥90-day long-COVID,
  in natal females, adjusting for age at infection. Pre-declared **smallest
  meaningful effect: RR ≈ 1.3** comparing the earliest-vs-latest menopause-timing
  tertile (equivalently ≈ RR 1.10–1.15 per SD of the continuous timing exposure — to
  be fixed to one scale at provisioning, not both).
- **Why:** h0005's homeostatic-margin conjecture + the precedent's female-specific
  SHBG protection signal (AlcaldeHerraiz2025) + the hormone-immune/endothelial
  mechanisms reviewed under `topic:menopause-sex-hormones-and-pais-risk`. The effect
  is expected to be **modest** and **partially confounded** (U latent), hence the
  E-value discipline below.
- **Direction is the primary commitment; magnitude is secondary** given the
  partial-identification design.

---

## Decision Criteria

Epistemic framing — each result class moves belief on h0005 by a stated amount/direction
(not a kill-switch). Thresholds are on the **primary confirmatory** estimate (RR of
WHO ≥90-day long-COVID per reproductive-timing exposure, **{age, smoking}**-adjusted
[primary measured adjustment set], natal-female, UKB), read jointly with its mandatory
sensitivities.

**Moves belief TOWARD h0005 (`supports_threshold_shift`):**
- Primary RR away from null in the predicted direction (earliest-vs-latest tertile RR
  ≥ ~1.3, 95% CI excludes 1), **AND**
- **E-value** for the estimate (and the near-null CI limit) **exceeds** the
  measured-proxy benchmark — the strength of associations for proxies **beyond the
  primary {age, smoking} set** (SES/comorbidity/remaining-behaviour) — **AND**
- the **U-proxy adjustment arm** (adding those beyond-{age, smoking} proxies) does not
  collapse it toward the null, **AND**
- it is **definition-stable** across the *feasible* outcome definitions (def-1 primary
  + def-2 approximation), **AND**
- it **survives** response-selection IPW and is **directionally concordant** with the
  Route-B (HES-PACS) triangulation outcome.

**WEAKENS / `fragile` (belief barely moves or downgrades confidence):**
- Primary RR away from null **but** E-value below the proxy benchmark, **or** the
  U-proxy arm collapses it, **or** it appears only in Route A (questionnaire) and
  tracks response-propensity, **or** it is present only under one outcome definition.

**Moves belief AWAY from h0005 (downward update):**
- Primary RR consistent with null **with an adequate power floor** — i.e. the
  (QBA-bias-adjusted) interval **excludes the meaningful effect (RR 1.3)** — and this
  is definition-stable. A *powered* null is a real downward update on the
  reproductive-timing-as-threshold-shifter claim (it does not falsify h0005's broader
  mechanism set, which other estimands test).

**Vetoes (result is inadmissible, no update either way):**
- `collider_confounded` — effect present **only** in a selection-conditioned subsample
  (clinic/HES-selected or response-propensity stratum) and absent in the population
  frame → reject as selection artifact.
- `reverse_contaminated` — exposure staged post-hoc rather than from the pre-infection
  baseline. (Largely foreclosed in UKB by the 2006–2010 baseline design, but checked.)

---

## Null Result Plan

A null is **evidence weighted by commitment**, not a verdict on h0005.

- **Powered null** (QBA-adjusted interval excludes RR 1.3, definition-stable) →
  **downward** belief update on reproductive-stage *timing* as a long-COVID
  threshold-shifter in this population; redirect effort to within-person/discordant
  designs and to the mediator-specific (direct-effect) estimand.
- **Underpowered / attenuated null** (esp. any peri analysis, or where non-differential
  staging misclassification per t020 has attenuated the estimate) → **no update**;
  label `underpowered/attenuated`, route the at-risk-window contrast to the younger
  triangulation cohorts. The t020 QBA attenuation means even a "true" null must be read
  against the **bias-adjusted** interval, not the naive one.
- **Ambiguous** (sensitivities disagree) → report as **estimand-/operationalization-dependent**;
  do not average; escalate to `/science:discuss`.

**Power floor (locked):** the confirmatory timing analysis must clear the minimum
female-case count for 80% power at RR 1.3 (α two-sided 0.05); computed exactly on
provisioning (G3 below). A peri-stratum result is reported only if its own cell clears
the floor — otherwise it is `underpowered`, never `null_meaningful`.

---

## Suspicious/Unexpected Result Plan

- **"Too good":** a large peri-specific or timing RR (e.g. > 2.0), or an implausibly
  clean monotonic dose-response across thin cells.
- **Likely inflators:** (a) menopause↔PAIS **symptom-overlap** leaking into both
  exposure-proxy and outcome despite the pre-baseline design; (b) **questionnaire
  response selection** (sicker reproductive-timing strata more likely to respond);
  (c) thin-cell instability in peri; (d) residual age confounding if age modeled too
  coarsely.
- **Pre-committed checks before accepting any strong result:** Route-B (HES)
  triangulation; response-selection IPW; a **negative-control outcome** (an outcome
  not plausibly caused by reproductive-stage timing — e.g. an injury/accident code —
  should show null); E-value plausibility vs the proxy benchmark; ordinal-vs-binary
  and per-SD-vs-tertile concordance; per-cell n inspection.

---

## Known Limitations

This analysis **cannot**, even executed perfectly:
1. **Point-identify** the total effect — even with {age, smoking} measured, U (SES,
   prior EBV, genetic/HLA, residual behaviour beyond smoking) stays partly latent, so
   **no valid sufficient adjustment set exists** (per the DAG critique); {age, smoking}
   is the *primary measured* set, not a sufficient one, and the E-value bound is
   load-bearing.
2. Resolve the **pre/peri-vs-post** contrast in UKB (cohort aged out — Feasibility);
   that requires younger cohorts.
3. Deliver a **PEM-specific** verdict — UKB has WHO-symptom-level data but no
   PASC-index/PEM instrument (def-2 is an approximation; q0015/t025 under-served).
4. Compute the **SF-36 functional-gate** definition — not in UKB; **not pre-registered
   as computable** (a named substitute would be required to add it; none committed here).
5. Escape **decade-gap exposure misclassification** (t020 QBA bounds, not removes, it).
6. Generalize beyond UKB's **healthy-volunteer, >90% White, questionnaire-responding**
   subset without the IPW + triangulation arms.
7. Escape **left-truncation / survival-to-2020 selection** (added by bias audit
   `report:0001-bias-audit-menopause-pais-total-effect`). Every analyzed woman must
   have survived from the 2006–2010 baseline to her 2020–2022 infection (age ≈ 52–83).
   Because **earlier age at menopause is associated with higher all-cause/CV
   mortality**, the earliest-menopause-timing stratum — the high-risk end of the
   *exposure* — is differentially depleted *before* the time origin (a
   competing-prior-event / depletion-of-susceptibles structure, distinct from the
   post-infection competing-risk censoring already handled). Expected to bias the
   timing→long-COVID estimate **toward the null**, though the direction is not
   guaranteed. Add a competing-prior-event / age-at-menopause-survival sensitivity at
   execution; report the bias direction.
8. Fully de-select on **questionnaire-response propensity** (added by bias audit).
   The response IPW is built from **baseline** predictors, but propensity to complete
   the 2022–2023 questionnaire plausibly depends on *post-baseline* health (including
   incipient long-COVID). Baseline IPW cannot reweight on a 2022 health state, so the
   Route-A estimate is "in responders"; Route-B (HES-PACS) carries the de-selecting
   triangulation weight, not the IPW alone.

**Vehicle-scope concession (bias audit, anchoring finding).** UKB is the primary
vehicle for the reproductive-**timing** estimand, but it **cannot answer q0013's
motivating peri-window sub-question** — the cohort aged out of the premenopausal/peri
window before the pandemic (Feasibility §). The stage→timing reframe is therefore an
honest scope concession, not a silent substitution; the peri/at-risk-window contrast
is owned by the younger triangulation cohorts. When the feasible outcome definitions
or exposure scales disagree, the governing order is **def-1 (WHO ≥90d) over def-2
(approximation)** and **tertile-contrast over per-SD** before any `/science:discuss`
escalation — so the escalation clause is not an open forking path.

---

## Metric Selection Rationale

- **Primary metric: risk ratio (RR) via log-binomial (or log-Poisson with robust SE)
  regression** for WHO ≥90-day long-COVID **present** at the Health & Well-Being
  questionnaire. Rationale: the questionnaire is a **single cross-sectional snapshot
  (2022–2023)**, so time-to-resolution is not cleanly observable on Route A → a
  prevalence/risk contrast is the honest estimand. (Route B / HES supports a
  time-to-event HR as a secondary, where longitudinal codes permit.)
- This **diverges** from the t016 plan's "HR or RR" wording by committing to **RR as
  primary**, justified by the Route-A cross-sectional outcome — a feasibility-driven
  refinement, recorded here so interpret-results treats it as committed, not drift.
- **Known limitation:** RR at a single snapshot conflates incidence and persistence;
  the Route-B HR triangulation partially addresses this.

---

## Exploratory vs. Confirmatory

**Confirmatory (1 primary test):**
- Reproductive-timing exposure (age-at-menopause / time-since-menopause) → WHO ≥90-day
  long-COVID RR, **{age-at-infection, smoking}**-adjusted (primary measured set;
  amendment Q1), natal-female, UKB, Route A.

**Pre-specified mandatory sensitivities (robustness, not discovery — do not multiply-correct as independent tests):**
E-value bound; U-proxy adjustment arm (proxies beyond {age, smoking}, +EBV on the ~9.6k
Category-1307 subsample, reported with its own power floor); response-selection IPW;
Route-B (HES-PACS) triangulation; estimand-split **{age, smoking}** vs
**{age, smoking, baseline comorbidity}**; BMI sensitivity (baseline, timing-split where
possible — role deferred to DAG v2 per Q2); outcome-definition axis (def-1 primary,
def-2 approximation); ordinal-vs-binary / per-SD-vs-tertile.

**Exploratory (explicitly labelled, hypothesis-generating):**
- Stage-at-infection ordinal (pre/peri/post) contrast in UKB (peri ≈ underpowered).
- Severity-controlled **direct** effect (additionally conditioning on acute severity).
- Mediator-specific (SHBG/testosterone) analyses.
- Triangulation pre/peri contrast in All of Us / Lifelines (separate pre-regs/arms).
- **Surgical-menopause discriminating contrast** (t030;
  `doc/methods/2026-06-19-surgical-menopause-discriminating-contrast.md`): bilateral
  oophorectomy vs natural postmenopause, with the **age-at-surgery gradient**
  (pre- vs post-FMP oophorectomy) and **HRT-stratification** as the
  confounding-resistant signatures that separate **M1** (hormone-withdrawal) from
  **M2** (aging) / **M4** (SES). **Exploratory / triangulating only** — estimated on a
  separate stratum with surgical cases **excluded from the primary natural-timing
  estimand**; promotable to a verdict-bearing sensitivity only if surgical *indication*
  is adequately bounded (reviewer call, t029).
- **Mendelian-randomization triangulation arm** (Q4; ratified t029): MR of
  genetically-instrumented **age-at-natural-menopause (ANM) → long-COVID**, exogenous to
  SES/smoking/survival and so attacking M2/M4/M3a jointly. **Triangulation only — not
  confirmatory or co-primary.** Pre-committed guardrails: prefer **external ANM
  instruments**; ancestry/PC handling; **sample-overlap disclosure**; clumping;
  **Steiger directionality**; heterogeneity tests; leave-one-out; **MR-Egger**, weighted
  median/mode; and a **pleiotropy-focused analysis excluding or separately reporting
  immune / DNA-repair / MHC-adjacent instrument subsets**. The DNA-repair/immune-gene
  overlap is grounds to **down-weight** the MR verdict, not to drop the arm.

---

## Total Comparison Count

| Category | Count | Correction |
|---|---|---|
| Confirmatory tests | 1 | none needed (single primary); verdict rests on it + mandatory sensitivities |
| Pre-specified sensitivities | ~9 | interpreted as robustness/arbitration, not multiplicity (adds BMI sensitivity per Q2) |
| Exploratory tests | ~6+ | none (exploratory — reported with exploratory weight; adds MR triangulation per Q4) |
| **Total** | **~16** | confirmatory verdict is multiplicity-free; sensitivities/exploratory carry their own (reduced) evidential weight |

---

## Vehicle-Admissibility Gate (data-gated mode)

**Standing verdict while gated:** `[?] inconclusive-for-coverage` — no `bears_on`
update on h0005/q0013 until a provisioned vehicle clears **all** G-gates below. These
G-gates **are** the "Blocking Checks Before Execution" that `/science:plan-analysis`
reports for this committed pre-reg (defined once here; referenced there).

- **G1 — Access provisioned.** An approved UKB AMS application with the required return
  categories (COVID-test field 40100; HES; GP; death; Health & Well-Being
  questionnaire; Category-1307 serology; vaccination linkage) delivered to a UKB RAP /
  approved environment.
- **G2 — Field IDs confirmed live + out-of-corpus feasibility check.** Questionnaire
  item IDs (WHO-Delphi), EBV-subsample N (Category 1307), vaccination-linkage category
  confirmed on the Showcase (COVID-test field 40100 already verified). **Plus (bias
  audit `report:0001-...`):** because all feasibility/effective-n/SHBG claims currently
  rest on the single precedent `AlcaldeHerraiz2025`, the effective-n and selection
  profile must be cross-read against **≥1 second UKB long-COVID cohort** before the AMS
  basket is finalized — the live-Showcase confirmation + this second read together are
  the named out-of-corpus check that lifts the feasibility claims from "single-source"
  to "confirmed."
- **G3 — Power floor met.** Female-case count for the **timing** exposure clears 80%
  power at RR 1.3 (α 0.05) after natal-female restriction ∧ valid menopause-timing ∧
  questionnaire-response ∧ positive-PCR. (The pre/peri stratum is *not* required to
  clear it — it is exploratory by Feasibility.)
- **G4 — Sampling-frame admissibility.** Recruitment not conditioned on symptomatic
  care-seeking (population frame upheld); the questionnaire-response selection handled
  by restriction + IPW; Route-B available for triangulation.
- **G5 — Exposure-timing integrity.** Reproductive-timing exposure derivable from the
  **pre-infection (2006–2010) baseline**; post-hoc-staged records quarantined.
- **G6 — Outcome computability.** Def-1 (WHO ≥90d, Route A) computable; def-2 proxy
  constructable; def-3 either substituted with a *named* UKB functional proxy or
  formally dropped (not silently assumed).

A **spent** vehicle that fails any G-gate does not qualify; the standing verdict
remains `[?]` until one does. Tracked by a `status: blocked` task whose blocker is
this gate.
