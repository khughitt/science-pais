---
id: "concept:cardiometabolic-comorbidity"
kind: "concept"
title: "Cardiometabolic comorbidity"
status: "active"
created: "2026-06-19"
updated: "2026-06-21"
ontology_terms: []
source_refs: []
related:
- patch-definition:menopause-pais-causal-dag
- concept:baseline-cardiometabolic-comorbidity
- concept:incident-cardiometabolic-comorbidity
---

# Cardiometabolic comorbidity

Cardiovascular/metabolic disease; baseline component is a confounder, menopause-incident component is a mediator (time-split).

**Superseded in DAG v2 (t023):** this single node is split into
`concept:baseline-cardiometabolic-comorbidity` (confounder; gains the
`baseline -> menopause-timing` edge) and
`concept:incident-cardiometabolic-comorbidity` (mediator, downstream of the
hormone shift). The split is what makes the new confounder edge acyclic. This
node is retained for history and is no longer wired into the DAG `flow_edges`.

Variable in the t014 causal DAG (`patch-definition:menopause-pais-causal-dag`).
