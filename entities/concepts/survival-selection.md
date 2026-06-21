---
id: "concept:survival-selection"
type: "concept"
title: "Survival selection / left-truncation"
status: "active"
created: "2026-06-21"
updated: "2026-06-21"
ontology_terms: []
source_refs: []
related:
- patch-definition:menopause-pais-causal-dag
---

# Survival selection / left-truncation

Selection node for survival into the study window (alive and enrolled at baseline/2020). Common effect of age, smoking, and frailty; cohort membership conditions on it, inducing left-truncation (M3a). **Do not condition** beyond what the design forces; handle via competing-risk/selection modelling and sensitivity.

Variable in the t014/t023 menopause-PAIS causal DAG v2 (`patch-definition:menopause-pais-causal-dag`).
