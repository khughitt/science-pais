---
id: patch-definition:menopause-pais-causal-dag
type: patch-definition
title: Menopausal transition and PAIS risk (t014 causal DAG)
status: active
created: "2026-06-19"
updated: "2026-06-19"
project: post-acute-infection
ontology_terms: []
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0007-mechanism-of-female-predominance-in-pais
- topic:menopause-sex-hormones-and-pais-risk
- task:t014
source_refs: []
content_preview: Causal DAG for the total effect of menopausal transition on failed post-infectious recovery, with explicit confounder/mediator/collider role pre-declaration.
file_path: entities/patches/menopause-pais-causal-dag.md
focal: hypothesis:0005-reproductive-stage-immune-homeostatic-margin
scope_set:
- scope: local
neighborhood_policy:
  name: local-closure-v1
  version: local-closure-v1
  max_depth: 2
patch_type: inquiry
inquiry:
  profile: causal
  status: sketch
  treatment: concept:menopausal-transition-reproductive-stage
  outcome: concept:pais-outcome
  boundary_roles:
  - ref: concept:menopausal-transition-reproductive-stage
    role: BoundaryIn
  - ref: concept:chronological-age
    role: BoundaryIn
  - ref: concept:sex-assigned-at-birth
    role: BoundaryIn
  - ref: concept:pregnancy-history
    role: BoundaryIn
  - ref: concept:pais-outcome
    role: BoundaryOut
  flow_edges:
  - subject: concept:chronological-age
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:chronological-age
    predicate: causes
    object: concept:cardiometabolic-comorbidity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:chronological-age
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:hormone-therapy
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:menopause-pais-symptom-overlap
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:cardiometabolic-comorbidity
  - subject: concept:hormone-therapy
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:menopause-pais-symptom-overlap
    predicate: causes
    object: concept:hormone-therapy
  - subject: concept:pregnancy-history
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:pregnancy-history
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:cardiometabolic-comorbidity
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:cardiometabolic-comorbidity
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:cardiometabolic-comorbidity
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:immune-dysregulation
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:immune-dysregulation
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:thromboinflammation-and-endothelial-dysfunction
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:menopause-pais-symptom-overlap
    predicate: causes
    object: concept:clinic-attendance
  - subject: concept:pais-outcome
    predicate: causes
    object: concept:clinic-attendance
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:pais-outcome
  unknowns:
  - concept:unmeasured-shared-confounders
  assumptions:
  - ref: pop-natal-female
    statement: Target population is natal females; menopausal transition is undefined otherwise, so sex assigned at birth is a population-definition given rather than a within-analysis exposure. The broader female-vs-male predominance contrast (q0007) is a separate estimand not addressed by this DAG.
  - ref: clinic-collider
    statement: Clinic attendance is a COLLIDER of menopause-driven symptom overlap and PAIS. Post-infection-clinic samples (Stewart2024-type cohorts) condition on it by construction; conditioning on it opens a spurious menopause-PAIS path and must be avoided. Do-not-condition.
  - ref: total-effect-mediators
    statement: Under the primary (total-effect) estimand, sex hormone levels, immune dysregulation, thromboinflammation/endothelial dysfunction, and acute infection severity are MEDIATORS of the menopausal-transition effect and are left UNADJUSTED. A severity-controlled direct effect would additionally condition on acute infection severity.
  - ref: comorbidity-time-split
    statement: Cardiometabolic comorbidity has a time-split role - pre-infection baseline comorbidity is a CONFOUNDER (adjust); menopause-incident comorbidity is a MEDIATOR (do not adjust for the total effect). The single node is a simplification that a measured analysis must resolve by timing relative to menopause and infection.
  - ref: ht-confounding-by-indication
    statement: Hormone therapy is subject to confounding by indication and healthy-user bias; observational HT-PAIS contrasts are not interpretable as the HT causal effect without a target-trial / new-user design (t019).
---

# Inquiry: Menopausal transition and PAIS risk (t014 causal DAG)

## Summary

Causal DAG (sketch) for **task t014**, operationalizing
`hypothesis:0005-reproductive-stage-immune-homeostatic-margin` and
`question:0013-reproductive-stage-failed-immune-recovery-after-infection`.

**Primary estimand (locked):** the *total effect* of **menopausal transition
(reproductive stage)** on the **PAIS outcome** (failed post-infectious recovery).
Adjust **age** only; **sex assigned at birth** is handled by population restriction
(natal females). Leave **sex hormones, immune dysregulation,
thromboinflammation/endothelial dysfunction, and acute infection severity**
unadjusted as mediators. Never condition on **clinic attendance** (collider).

> **Corrected by `/science:critique-approach` (2026-06-19).** An earlier draft of
> this summary also adjusted **baseline cardiometabolic comorbidity**. pgmpy
> back-door analysis showed comorbidity is **not** a confounder of the *total*
> effect (it is not a parent of menopausal transition), so adjusting it
> over-adjusts a mediator descendant (M-bias risk). The unique minimal sufficient
> set is **`{age}`** under natal-female restriction. Baseline comorbidity is
> retained only as a **sensitivity arm** contingent on a future
> `comorbidity → menopause-timing` edge (DAG v2, t023). See
> `doc/inquiries/menopause-pais-causal-dag-critique.md`. The frontmatter
> `flow_edges` and the `comorbidity-time-split` assumption are unchanged and
> already consistent with this correction.

This matches h0005's organizing conjecture: menopause is **not** posited as a
direct cause of PAIS, but as a threshold-shifter acting *through* hormone-driven
immune, endothelial, and autonomic pathways.

## Node role pre-declaration (per t014)

| Node | Role w.r.t. menopause → PAIS | Handling |
|---|---|---|
| Chronological age | Confounder (dominant) | Adjust |
| Sex assigned at birth | Population-definition given | Restrict population (natal females) |
| Sex hormone levels | Mediator (first line) | Do not adjust (total effect) |
| Hormone therapy | Mediator + confounded-by-indication intervention | Separate target-trial estimand (t019) |
| Pregnancy history | Competing reproductive-stage exposure | Covariate / separate exposure |
| Cardiometabolic comorbidity | Mediator (incident) of total effect; would be a confounder only **if** a `comorbidity → menopause-timing` edge existed | **Not adjusted** for the total effect (critique: over-adjustment); baseline comorbidity only as a sensitivity arm (DAG v2, t023) |
| Immune dysregulation | Mediator | Do not adjust (total effect) |
| Thromboinflammation / endothelial dysfunction | Mediator | Do not adjust (total effect) |
| Acute infection severity | Mediator | Do not adjust (total effect); condition only for direct effect |
| Menopause-PAIS symptom overlap | Ascertainment / measurement | Model misclassification; do not treat as biology |
| Clinic attendance | **Collider** | **Do not condition** (selection bias) |
| Unmeasured shared confounders | Latent confounder (open back-door) | Identifiability threat — see critique |

## Notes

- Built via the inquiry patch-definition layout (layout v3); causal edges are
  authored as `flow_edges` with `predicate: causes` and materialized to the
  `inquiry/<slug>` named graph by `science graph build`.
- Next: `/science:critique-approach menopause-pais-causal-dag` for adversarial
  review of identifiability, the comorbidity time-split, and the unmeasured-
  confounder back-door; then `/science:plan-analysis` (t016) to turn the locked
  estimand into a pre-registerable adjustment set against a measured cohort (t015).
