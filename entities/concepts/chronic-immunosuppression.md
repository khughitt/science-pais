---
id: "concept:chronic-immunosuppression"
kind: "concept"
title: "Chronic immunosuppression (pharmacologic or disease)"
status: "active"
created: "2026-07-18"
updated: "2026-07-18"
ontology_terms: []
source_refs: []
related:
- patch-definition:compound-boundary-conditions-interaction-dag
- question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
---

# Chronic immunosuppression (pharmacologic or disease)

Pre-infection immunosuppressed state — solid-organ-transplant regimens (calcineurin/mTOR inhibitors, mycophenolate), B-cell depletion (anti-CD20), other biologic DMARDs, or a disease exhaustion baseline (HIV). A **host-modifier (candidate effect modifier)** in the compound-boundary DAG (`patch-definition:compound-boundary-conditions-interaction-dag`, question:0057).

Its PAIS-relevant routes are two-fold and both point the *same* direction (more PASC, not less — the Vinson2024 SOT paradox): it depletes the shared **immune homeostatic reserve** and, via impaired humoral/T-cell clearance, raises **persistent antigen/fragment burden** (`concept:persistent-antigen-fragment-burden`; Chavatza2025 rituximab compartmentalized persistence). Because it shares the reserve bottleneck with `concept:biological-frailty`, the two form the DAG's **shared-bottleneck** focal pair.
