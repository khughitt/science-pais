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
---

# Hospitalization / acute-care ascertainment

Severe acute illness -> hospitalization -> cohort entry / detected PAIS. A **second selection collider** (parallel to clinic attendance): a common effect of acute severity and PAIS. Conditioning on a hospitalized/ascertained sample opens a spurious severity-PAIS path. **Do not condition.**

Variable in the t014/t023 menopause-PAIS causal DAG v2 (`patch-definition:menopause-pais-causal-dag`).
