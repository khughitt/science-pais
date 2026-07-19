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

- **Structural formalization (t111, 2026-07-18, corrected 2026-07-19; `patch-definition:compound-boundary-conditions-interaction-dag`).**
  An **unidentified causal sketch** under `hypothesis:0020` (not an identified or evidence-bound DAG). Its
  surviving substantive point is structural: it recasts the "superadditive **vs** distinct routes" framing as a
  **false binary**. The two focal pairs are *two candidate (hypothesized) structures*: **frailty × immunosuppression**
  as a **shared-bottleneck** conjecture and **pregnancy × MCAS** as a **distinct/opposite-signed-route** conjecture
  — neither demonstrated (Vinson2024/Hammel2023 are single-population *associations* that never measure reserve;
  Bruno2024 is a *coded-diagnosis* dissociation, not mechanism; Wolff2023 is atopy not MCAS, and Augustin is
  post-infection so grounds no pre-infection arrow). Load-bearing consequences that DO survive: (1) **structure
  alone cannot fix the interaction sign** — a shared bottleneck can be super-additive (threshold) *or* a
  ceiling/sub-additive (reserve floored); sign is scale-and-dose-response, not structural. (2) **"Superadditive"
  must name a scale** — prefer standardized cumulative-incidence risks / risk differences at a fixed horizon, with
  RERI only for justified binary contrasts (AP/synergy-index are unstable under opposite-signed effects), and the
  additivity→sufficient-cause reading needs extra confounding+monotonicity assumptions. (3) **Interaction
  confounding is stricter and selection is the dominant threat** — {age, comorbidity} block only the *drawn*
  back-doors (a real set adds indication, drug class/duration, utilization, vaccination, era, detection, acute
  treatment…); U keeps it non-identifiable; and any clinic/convenience cohort (plus the documented-infection /
  survival / participation conditioning every PAIS study makes) manufactures spurious interaction. Also: the
  estimand is **descriptive stratum heterogeneity**, not a `do()` on non-manipulable host states; phenotype must
  be resolved; cohort requirements + D-004 block are in the DAG. The formal toolchain did **not** verify any of
  this (the pgmpy exporter emits an empty model) — the identification claims are hand-derived.

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
