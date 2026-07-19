---
id: "concept:hospital-ascertainment"
kind: "concept"
title: "Hospitalization / acute-care ascertainment"
status: "active"
created: "2026-06-21"
updated: "2026-06-21"
ontology_terms: []
source_refs: []
related:
- patch-definition:menopause-pais-causal-dag
- patch-definition:compound-boundary-conditions-interaction-dag
---

# Hospitalization / acute-care ascertainment

Severe acute illness -> hospitalization -> cohort entry / detected PAIS. A **selection collider** (parallel
to clinic attendance): a common effect of acute severity and PAIS. Conditioning on a hospitalized/ascertained
sample opens a spurious severity-PAIS path. **Do not condition.**

Variable in the t014/t023 menopause-PAIS causal DAG v2 (`patch-definition:menopause-pais-causal-dag`).

**Compound-boundary DAG usage (t111):** its parent set is *extended* — every host-modifier
(frailty, immunosuppression, pregnancy-state, MCAS) as well as severity and PAIS points into it, because
compound-boundary patients are differentially surveilled. Conditioning then induces a spurious
**modifier–modifier** association that biases the interaction term (the compound-selection collider), a
stronger threat than in the single-exposure menopause DAG. It is one of several selection nodes there
(alongside documented-infection detection, ~30-day survival, and participation).
