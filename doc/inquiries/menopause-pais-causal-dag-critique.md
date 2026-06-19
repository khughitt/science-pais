---
id: "inquiry-doc:menopause-pais-causal-dag-critique"
type: "doc"
title: "Causal DAG critique: menopausal transition and PAIS risk (t014)"
status: "critiqued"
source_refs:
- patch-definition:menopause-pais-causal-dag
- inquiry-doc:menopause-pais-causal-dag
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- task:t014
created: "2026-06-19"
updated: "2026-06-19"
---

# Causal DAG Critique: menopausal transition and PAIS risk (t014)

**Inquiry:** `menopause-pais-causal-dag`
**Treatment:** menopausal transition (reproductive stage)
**Outcome:** PAIS outcome (failed post-infectious recovery)
**Reviewed:** 2026-06-19 (adversarial / discussant mode)

## Structural validation

`science inquiry validate` — `boundary_reachability` **pass**, `no_cycles`
**pass**, `causal_acyclicity` **pass**, `target_exists` **pass**;
`orphaned_interior` **warn** for `clinic_attendance` (intended sink collider)
and `unmeasured_shared_confounders` (intended exogenous latent). No structural
defects.

> **Tooling note:** `science inquiry export-pgmpy` emitted an **empty** edge
> list — it reads `scic:causes` from the `graph/causal` layer, but the inquiry
> patch materializer writes causal edges into the per-inquiry named graph. The
> identifiability analysis below was therefore run with pgmpy directly on the
> authored edge list (filed as `command:critique-approach` feedback).

## Identifiability assessment (pgmpy back-door, 13 nodes / 31 edges)

| Scenario | Result |
|---|---|
| **U latent (the real world)** | **No valid back-door adjustment set exists** — the total effect is *not identifiable* by covariate adjustment. |
| U hypothetically measured | Unique minimal set `{age, sex-at-birth, U}`. |
| No unmeasured confounding assumed | Unique minimal set **`{age, sex-at-birth}`**. |

Two consequences dominate the critique:

1. **Non-identifiability is the headline.** With any unmeasured common cause of
   reproductive stage and PAIS (SES, prior EBV/autoimmunity, genetic/HLA risk,
   health behaviours), adjustment cannot recover the effect. An observational
   menopause→PAIS estimate is only as credible as the argument that U is small
   or proxied.

2. **The locked adjustment set was wrong.** The estimand pre-declared "adjust
   age **+ baseline cardiometabolic comorbidity**." pgmpy shows baseline
   comorbidity is **not** on any back-door path of the *total* effect: in this
   DAG menopause's only parents are age, sex-at-birth, and U, so **age alone**
   (with sex-at-birth handled by population restriction) blocks all open
   back-door paths. Adjusting comorbidity is at best unnecessary and at worst
   harmful — see Structural Issues.

## Edge-by-edge review (selected challenges)

| Edge | Challenge | Verdict |
|---|---|---|
| menopause → sex hormones | Reverse causation? PAIS/illness can perturb the HPG axis (q0013 names the reverse direction). | **Real concern.** The DAG is unidirectional; the reverse arrow (infection/PAIS → reproductive axis) is a *separate proposition* (h0005 P-reverse, t021) and would create a cycle if naively added. Must be handled by temporal ordering (reproductive stage *at infection*), not a bidirectional edge. |
| menopause → symptom overlap → clinic ← PAIS | Selection. | **Confirmed collider** (see below). |
| age → menopause; age → PAIS | Is age's effect on PAIS fully direct, or via immunosenescence/comorbidity already modeled? | Edge is a coarse stand-in for residual age effects; acceptable but flag age as the single load-bearing confounder. |
| hormones → comorbidity → PAIS | Makes comorbidity a *mediator*, not a confounder. | Drives the over-adjustment finding. |
| acute severity → PAIS | Mediator vs. selection (severe acute → hospitalization → ascertainment). | Plausible second collider path not yet modeled (hospitalization). |

## Missing confounders / missing edges

- **comorbidity → menopausal timing** is *omitted*. Metabolic disease and
  smoking accelerate menopause; if this edge exists, baseline comorbidity
  *becomes* a genuine confounder and the adjustment set changes. The current
  "comorbidity is not a confounder" result is **conditional on this edge being
  absent** — a fragile assumption (see Sensitivity).
- **Hospitalization / acute-care ascertainment** is not modeled but is a second
  collider (severe acute illness → hospital → cohort entry → both severity and
  detected PAIS).
- **Prior EBV serostatus / autoimmunity** is folded into U; it is arguably
  measurable and could be promoted from latent to an observed proxy, partially
  closing the back-door.
- **Calendar period / variant / vaccination era** (a common cause of acute
  severity and of who is studied) is absent and may confound mediator paths.

## Structural issues

- **Collider bias (critical, by design of the data):** `clinic_attendance` is a
  common effect of menopause-driven symptom overlap and of PAIS. Post-COVID /
  post-infection **clinic samples condition on it by construction**
  (Stewart2024-type cohorts). Any analysis drawn from such a sample has *already*
  conditioned on the collider and will show a spurious menopause↔PAIS
  association even if none exists. This is the single most likely source of a
  false positive in the existing literature.
- **Over-adjustment / mediator-conditioning:** adjusting baseline cardiometabolic
  comorbidity conditions on a descendant of the `sex hormones → comorbidity`
  mediator, partially blocking the mediated component of the *total* effect.
  Comorbidity also has parents {age, hormones}; conditioning on it opens the
  non-causal path age ⇄ hormones (M-bias-like), only partly neutralized by also
  adjusting age. **Recommendation: drop comorbidity from the total-effect
  adjustment set.**
- **No collider conditioning in the recommended set** otherwise — good.

## Sensitivity analysis

| Assumption | If violated | Impact | Robustness |
|---|---|---|---|
| No unmeasured confounding (U negligible) | Effect non-identifiable; point estimate uninterpretable | **High** (conclusions can reverse) | Low — requires E-value / bounding or a design that breaks U |
| `comorbidity → menopause-timing` edge absent | Baseline comorbidity becomes a true confounder; must be adjusted | **Moderate** | Low — biologically plausible edge; test both adjustment sets |
| Reproductive stage measured *at infection* (temporal ordering holds) | If stage is measured post-hoc, reverse causation (PAIS→axis) contaminates exposure | **High** | Moderate — fixable by design (baseline staging) |
| Sample not conditioned on clinic attendance | If it is (clinic cohort), spurious association manufactured | **High** | Low for clinic samples; high for population cohorts |
| Symptom overlap = pure measurement (no biology) | If overlap shares biology with PAIS, outcome misclassification is differential by menopause | Moderate | Moderate — needs objective endpoints (topic:biomarkers) |

**Minimum surviving design:** a population-based (not clinic-based) cohort with
reproductive stage staged *at the time of acute infection*, age-adjusted only,
plus a measured proxy battery for U (SES, prior EBV, autoimmune history) and an
E-value sensitivity analysis bounding residual confounding.

## Overall assessment

| Dimension | Assessment |
|---|---|
| Completeness | **Warn** — missing comorbidity→menopause edge, hospitalization collider, calendar/variant node |
| Identifiability | **Fail (as drawn)** — non-identifiable with U latent; needs proxies/design/bounding |
| Evidence quality | **Warn** — edges are literature-plausible but uncurated (`unknown`/`none` on the two-axis model) |
| Structural validity | **Warn** — DAG is clean, but the *pre-declared adjustment set* over-adjusts; clinic samples embed collider bias |
| Temporal coherence | **Warn** — depends entirely on staging reproductive stage at infection |
| Sensitivity | **Low robustness** — conclusions hinge on U and on the comorbidity-timing edge |

## Recommendations (actionable)

1. **Correct the estimand's adjustment set:** total-effect adjustment is
   **`{age}`** under natal-female restriction (drop baseline comorbidity). Carry
   a second adjustment set `{age, baseline comorbidity}` only as a sensitivity
   arm tied to the `comorbidity → menopause-timing` edge.
2. **Treat non-identifiability explicitly in t016/plan-analysis:** pre-register
   an E-value / Rosenbaum-style bound for U, and promote prior EBV/autoimmunity
   and SES from latent U to measured proxies in the t017 schema.
3. **Exclude clinic-based samples** (or model the selection explicitly) in t015
   cohort screening; prefer population cohorts with pre-infection baselines (t008).
4. **Add the missing edges** (`comorbidity → menopause-timing`, hospitalization
   collider, calendar/variant) to a v2 of the DAG before specification.
5. **Keep reverse causation (P-reverse, t021) as a separate inquiry**, with
   exposure fixed at pre-infection reproductive stage to preserve acyclicity.

**Status:** inquiry marked `critiqued` — this records that adversarial review
occurred and found a Fail on identifiability and a correction to the adjustment
set; it does **not** indicate the approach passed.
