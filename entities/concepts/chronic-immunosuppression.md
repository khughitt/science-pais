---
id: "concept:chronic-immunosuppression"
kind: "concept"
title: "Chronic immunosuppression (pharmacologic or disease)"
status: "active"
created: "2026-07-18"
updated: "2026-07-19"
ontology_terms: []
source_refs:
- cite:Vinson2024
- cite:Peluso2022a
- cite:Chavatza2025
related:
- patch-definition:compound-boundary-conditions-interaction-dag
- question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
---

# Chronic immunosuppression (pharmacologic or disease)

Pre-infection immunosuppressed state — **a heterogeneous bundle**, not one exposure: solid-organ-transplant
regimens (calcineurin/mTOR inhibitors, mycophenolate), B-cell depletion (anti-CD20), other biologic DMARDs,
or a disease exhaustion baseline (HIV). Because class, dose, duration, and underlying disease differ, any
"immunosuppression" exposure level must be specified before use. A **baseline host-modifier** in the
compound-boundary DAG (`patch-definition:compound-boundary-conditions-interaction-dag`, question:0057).

The PAIS evidence is **associational**: Vinson2024 found higher PASC in SOT recipients (N3C, aOR 1.48;
mycophenolate aOR 2.04) — the "SOT paradox" — and Peluso2022a ~4× PASC odds in HIV; Chavatza2025 documents
rituximab → impaired clearance → compartmentalized viral persistence. None measures immune reserve, so the
*conjecture* that this modifier acts by depleting the shared `concept:immune-homeostatic-reserve` (and, via
impaired clearance, raising `concept:persistent-antigen-fragment-burden`) is hypothesis:0020 P2, not a
demonstrated convergence. Paired with `concept:biological-frailty` it forms the DAG's hypothesized
**shared-bottleneck** structure.
