---
id: "inquiry-doc:menopause-pais-causal-dag"
type: "doc"
title: "Causal DAG: menopausal transition and PAIS risk (t014)"
status: "sketch"
source_refs:
- patch-definition:menopause-pais-causal-dag
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- task:t014
created: "2026-06-19"
updated: "2026-06-19"
---

# Causal DAG: menopausal transition and PAIS risk (t014)

Sketch-stage causal inquiry built for **task t014**, operationalizing
`hypothesis:0005-reproductive-stage-immune-homeostatic-margin` and
`question:0013`. The machine-readable model lives in the inquiry patch
`entities/patches/menopause-pais-causal-dag.md` (13 variables, 31 `scic:causes`
edges) and materializes into the `inquiry/menopause-pais-causal-dag` named graph.

## Locked primary estimand

**Total effect** of **menopausal transition (reproductive stage)** on the
**PAIS outcome** (failed post-infectious recovery), in a **natal-female**
target population.

- **Adjust (confounders):** chronological age. (Sex assigned at birth is handled
  by population restriction to natal females.)
  > **Corrected by critique (2026-06-19):** the original draft also adjusted
  > baseline cardiometabolic comorbidity. pgmpy back-door analysis shows
  > comorbidity is **not** a confounder of the *total* effect in this DAG (it is
  > not a cause of menopausal transition); adjusting it over-adjusts a mediator
  > descendant. The unique minimal sufficient set is **`{age}`** under
  > natal-female restriction. Baseline comorbidity is retained only as a
  > *sensitivity arm* contingent on a `comorbidity → menopause-timing` edge.
  > See `menopause-pais-causal-dag-critique.md`.
- **Do NOT adjust (mediators):** sex hormone levels, immune dysregulation,
  thromboinflammation/endothelial dysfunction, acute infection severity.
- **Never condition (collider):** clinic attendance.
- **Identifiability:** **not identifiable by adjustment alone** while unmeasured
  shared confounders (U) are latent — requires measured proxies for U and/or
  E-value bounding (see critique).

This encodes h0005's conjecture that menopause is not a direct cause of PAIS but
a threshold-shifter acting *through* hormone-driven immune, endothelial, and
autonomic pathways. A **severity-controlled direct effect** (additionally
conditioning on acute severity) is the planned secondary estimand.

## Diagram

![t014 causal DAG](assets/menopause-pais-causal-dag.png)

DOT source: [`assets/menopause-pais-causal-dag.dot`](assets/menopause-pais-causal-dag.dot)
(regenerate the PNG with `dot -Tpng`).

Legend: blue = treatment, red = outcome, yellow = confounder (adjust),
green = mediator (do-not-adjust), orange = mixed confounder/mediator
(time-split), grey note = ascertainment, purple hexagon = collider
(do-not-condition), dashed = latent/unmeasured.

## Node roles (pre-declared per t014)

| Node | Role w.r.t. menopause → PAIS | Handling |
|---|---|---|
| Chronological age | Confounder (dominant) | Adjust |
| Sex assigned at birth | Population-definition given | Restrict to natal females |
| Sex hormone levels | Mediator (first line) | Do not adjust (total effect) |
| Hormone therapy | Mediator + confounding-by-indication | Separate target-trial estimand (t019) |
| Pregnancy history | Competing reproductive-stage exposure | Covariate / separate exposure |
| Cardiometabolic comorbidity | Baseline = confounder, incident = mediator | Time-split; adjust baseline only |
| Immune dysregulation | Mediator | Do not adjust |
| Thromboinflammation / endothelial dysfunction | Mediator | Do not adjust |
| Acute infection severity | Mediator | Do not adjust (condition only for direct effect) |
| Menopause-PAIS symptom overlap | Ascertainment / measurement | Model misclassification |
| Clinic attendance | **Collider** | **Do not condition** |
| Unmeasured shared confounders (U) | Latent confounder | Identifiability threat |

## Validation (sketch)

`science inquiry validate menopause-pais-causal-dag`:

- `boundary_reachability` **pass**, `no_cycles` **pass**, `causal_acyclicity` **pass**, `target_exists` **pass**.
- `orphaned_interior` **warn** (2): `clinic_attendance` (deliberate sink collider) and `unmeasured_shared_confounders` (exogenous latent root). Both expected.
- `identifiability` / `adjustment_sets` **skipped** — pgmpy not installed. To be run in critique.

## Key open issue for critique-approach

The **unmeasured shared confounders (U)** node (SES, prior EBV/autoimmunity,
genetic/HLA risk, health behaviours) is drawn as a common cause of both
treatment and outcome. As drawn, the total effect is **not identifiable by
back-door adjustment on observed variables alone** — adjusting age + baseline
comorbidity does not block the U path. This is the central tension to resolve in
`/science:critique-approach`: either (a) argue U is negligible/blocked by proxies,
(b) restrict to a within-person or sibling/discordant design, or (c) accept the
estimand as partially identified and bound it. The collider (clinic attendance)
and the comorbidity time-split are the other two priority targets for adversarial
review.

## Next steps

1. `/science:critique-approach menopause-pais-causal-dag` — adversarial review of identifiability (U back-door), the clinic-attendance collider, and the comorbidity time-split; export to pgmpy for back-door adjustment sets.
2. `/science:plan-analysis` (t016) — turn the locked estimand into a pre-registerable adjustment set against a measured cohort (t015).
