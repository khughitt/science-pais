---
id: "concept:biological-frailty"
kind: "concept"
title: "Biological frailty / subclinical pre-infection ill-health"
status: "active"
created: "2026-06-21"
updated: "2026-06-21"
ontology_terms: []
source_refs: []
related:
- patch-definition:menopause-pais-causal-dag
- patch-definition:compound-boundary-conditions-interaction-dag
---

# Biological frailty / subclinical pre-infection ill-health

Non-SES subclinical ill-health / accumulated physiological deficit (inflammaging, depleted naïve-T pools,
sarcopenia, mitochondrial dysfunction). In the **menopause DAG** it is a common cause of earlier menopause
AND higher LC susceptibility AND lower survival: dual role — **confounder** (frailty → menopause, frailty →
PAIS) and **selection/competing-risk** (frailty → survival selection; conditioning on cohort membership
induces left-truncation/M3a). Handled via selection model + sensitivity, not primary adjustment (t029 Q3).

Variable in the t014/t023 menopause-PAIS causal DAG v2 (`patch-definition:menopause-pais-causal-dag`).

**Compound-boundary DAG usage (t111):** here frailty is instead a **baseline host-modifier** (a
multi-level stratifying exposure, tool `treatment` placeholder) whose *hypothesized* route is depletion of
`concept:immune-homeostatic-reserve`; it retains its survival-selection parenthood. The reuse extends, not
redefines, the node.
