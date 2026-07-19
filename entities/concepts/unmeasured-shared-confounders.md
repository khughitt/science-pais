---
id: "concept:unmeasured-shared-confounders"
kind: "concept"
title: "Unmeasured shared confounders"
status: "active"
created: "2026-06-19"
updated: "2026-06-19"
ontology_terms: []
source_refs: []
related:
- patch-definition:menopause-pais-causal-dag
- patch-definition:compound-boundary-conditions-interaction-dag
---

# Unmeasured shared confounders

Latent common causes outside the measured set: socioeconomic status, prior EBV/autoimmunity, genetic/HLA
risk, health behaviours. An open back-door threatening identifiability. In the **menopause DAG** it is a
common cause of reproductive stage and PAIS.

Variable in the t014 causal DAG (`patch-definition:menopause-pais-causal-dag`).

**Compound-boundary DAG usage (t111):** here U is drawn as a common cause of **all four host-modifiers**
and PAIS. Its interaction-specific role is what makes the compound estimand non-identifiable by adjustment,
and the relevant sensitivity parameter is U's strength as a common cause of *both* modifiers (driving a
spurious modifier–modifier association) — not a single-effect E-value. The reuse extends the node's
parenthood; it does not redefine it.
