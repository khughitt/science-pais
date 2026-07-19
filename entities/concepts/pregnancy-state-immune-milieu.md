---
id: "concept:pregnancy-state-immune-milieu"
kind: "concept"
title: "Pregnancy-state immune milieu (active gestation/peripartum)"
status: "active"
created: "2026-07-18"
updated: "2026-07-19"
ontology_terms: []
source_refs:
- cite:Bruno2024
related:
- patch-definition:compound-boundary-conditions-interaction-dag
- question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory
---

# Pregnancy-state immune milieu (active gestation/peripartum)

The immune remodeling of *active* pregnancy — expanded Tregs, Th2/IL-4/IL-10 polarization, suppressed
Th1/IFN-γ, complement and coagulation shifts — with rapid postpartum reconstitution, and therefore
**time-varying** (gestational week / postpartum day matter). **Distinct from `concept:pregnancy-history`/parity**
(a life-course staging input); this node is the transient gestational *state* at time of infection.

A **baseline host-modifier** in the compound-boundary DAG
(`patch-definition:compound-boundary-conditions-interaction-dag`, question:0040). The evidence is
Bruno2024, which measured **EHR-coded PASC components** (lower cognitive/fatigue, higher cardiac/thromboembolic
during pregnancy) — a *coded-diagnosis dissociation*, **not** a measurement of Tregs, Th1 biology, or mast-cell
mediation. So the drawn opposite-signed edges (a Treg/tolerance arm *dampening* the Th1/autoimmune route via
`concept:immune-dysregulation`; a preserved/amplified thrombovascular route via
`concept:thromboinflammation-and-endothelial-dysfunction`; a feed into `concept:th2-mast-cell-axis`) are a
**mechanistic interpretation** competing with differential coding/ascertainment and normal pregnancy
physiology — not established biology. With `concept:mast-cell-activation-hyperreactivity` it forms the DAG's
hypothesized **distinct/opposite-signed-route** structure — the case where compound exposure may redirect
*phenotype* rather than incidence.
