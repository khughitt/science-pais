---
id: question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
kind: question
title: Compound boundary conditions — do co-occurring effect modifiers compound PAIS risk superadditively or via distinct mechanism routes?
status: active
ontology_terms:
  - effect modification
  - interaction
  - compound exposure
  - frailty
  - immunosuppression
  - MCAS
  - pregnancy
  - EBV history
datasets: []
source_refs: []
origins:
  - type: assistant
    ref: research-topic:population-boundary-conditions-and-effect-modifiers-in-pais
related:
  - topic:population-boundary-conditions-and-effect-modifiers-in-pais
  - question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
  - question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
  - question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
  - question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0020-host-immune-baseline-reserve-gate
  - patch-definition:compound-boundary-conditions-interaction-dag
created: "2026-07-07"
updated: "2026-07-18"
added_by: "llm:claude-opus-4-8:research-topic"
---
# Compound boundary conditions — do co-occurring effect modifiers compound PAIS risk superadditively or via distinct mechanism routes?

## Summary

The six boundary populations identified in `topic:population-boundary-conditions-and-effect-modifiers-in-pais`
are analyzed individually, but real patients often occupy multiple boundary strata simultaneously: a frail
SOT recipient is both immunosuppressed and frailty-depleted; a pregnant woman with pre-existing MCAS has
both Th2/Treg immune remodeling and constitutively primed mast cells; an elderly LMIC patient may be
simultaneously frail, helminth-exposed, and under-ascertained. Does compound boundary exposure compound PAIS
risk additively, superadditively (synergistically), or does it redirect mechanism routes in ways that might
be partially protective? This question formalizes the interaction structure that the single-stratum analyses
leave implicit.

## Why It Matters

- **Decision it affects:** whether analyses of boundary populations should include interaction terms for
  co-occurring modifiers (e.g., frailty × immunosuppression), and whether interventions should be targeted
  to compound-risk strata.
- **Risk if unanswered:** analyses treating each modifier as independent will be misspecified if compound
  exposures interact. Effect estimates from single-modifier studies will be non-portable to the
  multi-modifier real-world patient.

## Current Evidence

- No published study has formally tested interaction between co-occurring boundary conditions for PAIS.
- Frailty and immunosuppression co-occur in transplant recipients (Vinson2024 cohort), but frailty
  scoring was not reported; the N3C data includes comorbidity indices but not validated frailty phenotypes.
- Atopy and pregnancy co-occur commonly; the RECOVER EHR pregnancy analysis (Bruno2024) did not stratify
  by atopy/MCAS pre-existing status.
- LMIC populations with HIV co-infection and helminth burden are effectively compound boundary exposures
  (immune exhaustion + Th2 skew), but no PAIS mechanism data exist for this stratum.

## Thoughts

- **Best current interpretation:** compound modifier interactions are likely, but the direction and
  magnitude are unknown and potentially mechanism-specific. Frailty + immunosuppression probably compounds
  risk (additive or superadditive immune reserve deficit). Pregnancy + MCAS may be partially offsetting (Th2
  pregnancy suppression of some mast-cell triggers) or amplifying depending on the specific allergen/trigger.
- **Major uncertainty:** no existing PAIS cohort is powered or designed to test compound modifier
  interactions; this is a design aspiration rather than a near-term empirical question.

- **Structural formalization (t111, 2026-07-18; `patch-definition:compound-boundary-conditions-interaction-dag`).**
  A causal-sketch DAG under `hypothesis:0020` recasts the "superadditive **vs** distinct routes" framing as a
  **false binary**. The two focal pairs are *two different structures*: **frailty × immunosuppression** is the
  **shared-bottleneck** archetype (both deplete one `immune-homeostatic-reserve` node), and **pregnancy × MCAS**
  is the **distinct / opposite-signed-route** archetype (convergence on a Th2/mast-cell axis with pregnancy's
  Treg/tolerance arm dampening the Th1/neuro route while the thrombovascular route is preserved — Bruno2024).
  Three load-bearing consequences: (1) **the DAG cannot fix the interaction sign** — even the shared bottleneck
  can be super-additive (threshold) *or* a ceiling/sub-additive (reserve already floored); sign is a
  scale-and-dose-response property, not a structural one. (2) **"Superadditive" must name a scale** — mechanistic
  interaction = departure from **additivity**, so the estimand needs RERI/AP/synergy-index reported alongside the
  multiplicative product term. (3) **Interaction confounding is stricter and selection is the dominant threat** —
  {age, baseline-comorbidity} block the modifier–modifier back-door, U keeps it non-identifiable, and any
  clinic/convenience cohort conditions on the compound-selection collider (both modifiers → ascertainment),
  manufacturing spurious interaction. Pregnancy × MCAS additionally may redirect *phenotype* not incidence, so the
  outcome must be phenotype-resolved. Cohort deliverable and the D-004 gated-data block are recorded in the DAG.

## Connections to Project

- Related hypotheses: `hypothesis:0004-acute-severity-threshold` (compound modifiers lower the threshold
  further); `hypothesis:0001-shared-dysregulated-attractor` (compound modifiers test whether there is a
  common attractor or multiple distinct attractors for different modifier combinations).
- Required datasets: large multi-covariate PAIS cohorts with validated frailty, immunosuppression class,
  atopy/MCAS diagnosis, and reproductive-state data collected prospectively.
- Required analyses: interaction-term analysis or effect-measure modification tests within stratified
  cohorts; DAG construction to identify confounders vs mediators across joint modifier strata.
- Priority level: P4 (low near-term tractability; data for joint-modifier analysis do not currently exist;
  design-and-taxonomy value high for future cohort planning).

## Related

- Topic notes: `topic:population-boundary-conditions-and-effect-modifiers-in-pais`.
- Article notes: none yet — no papers directly address this question.
- Methods/Datasets: requires a large multi-morbidity post-COVID cohort with granular covariate data,
  validated frailty phenotyping, and pre-infection atopy/immunosuppression records.
