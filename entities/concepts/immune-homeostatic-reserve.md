---
id: "concept:immune-homeostatic-reserve"
kind: "concept"
title: "Pre-infection immune homeostatic reserve"
status: "active"
created: "2026-07-18"
updated: "2026-07-19"
ontology_terms: []
# source_refs intentionally empty: this is a conjectural construct (h0020) with no operational
# pre-infection measure and no study demonstrating any modifier acts through it.
source_refs: []
related:
- patch-definition:compound-boundary-conditions-interaction-dag
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0004-acute-severity-threshold
---

# Pre-infection immune homeostatic reserve

The "slack" in the immune system's capacity to mount, control, and *terminate* an inflammatory response and return to baseline — the reserve axis of `hypothesis:0020` (host-immune-baseline-reserve-gate), operationalizing the reserve term of `hypothesis:0004`'s severity threshold. No agreed operational pre-infection measurement exists yet (candidate proxies: baseline inflammatory tone, thymic output / naïve-T fraction, vaccine-response competence).

The **hypothesized** shared mediating bottleneck of the compound-boundary DAG (`patch-definition:compound-boundary-conditions-interaction-dag`, question:0057). The *conjecture* that `concept:biological-frailty` and `concept:chronic-immunosuppression` both deplete it is what would make them a shared-bottleneck pair — but no study measures this node, and the reserve→PAIS relation is unmeasured, so the convergence is asserted, not shown. **Load-bearing caveat:** convergence on this node does **not** by itself fix the sign of their interaction — that depends on the (unknown) shape of the reserve → lock-in map (a convex/threshold map near the tipping point yields super-additivity; a saturating/already-floored map yields a ceiling / sub-additivity) and on the scale on which interaction is measured. The node is a mediator: it is *not* conditioned on for the total joint effect, but conditioning on it is the mediation test of whether the interaction *runs through* the shared reserve.
