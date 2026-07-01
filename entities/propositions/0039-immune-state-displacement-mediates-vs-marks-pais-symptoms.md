---
id: "proposition:0039-immune-state-displacement-mediates-vs-marks-pais-symptoms"
type: "proposition"
title: "Persistent immune-state displacement mediates PAIS symptoms rather than merely marking another failed-recovery process"
status: "active"
claim_layer: "causal_effect"
identification_strength: "observational"
proxy_directness: "indirect"
measurement_model:
  observed_entity: immune-state proxies (as in proposition:0038) jointly with symptom/outcome measures, ideally under a target-engaging perturbation
  latent_construct: the causal (mediating) effect of the displaced immune state on PAIS symptom burden
  measurement_relation: mediation is currently unidentified; it requires an intervention with demonstrated target engagement plus a symptom + pathway co-readout, or (observational fallback) a longitudinal mediation design with the parallel vascular/metabolic/neural lesions measured
  known_failure_modes:
  - correlation of an immune proxy with symptoms does not establish mediation
  - an unmeasured parallel primary lesion (vascular/metabolic/neural) confounds the immune-symptom association
  - feedback loops (proposition:0041) make a single-timescale mediator-vs-marker verdict ill-posed
supports_scope: "hypothesis_bundle"
current_working_model: "unresolved: mediator vs marker/co-traveler"
discusses:
  - frame: "hypothesis:0001-shared-dysregulated-attractor"
    role: "background"
related:
  - "question:0022-immune-state-displacement-mediator-vs-co-traveler"
  - "question:0006-jak-stat-il6-driver-vs-marker"
  - "hypothesis:0003-immune-exhaustion-feedback"
  - "pre-registration:0004-jak1-inhibitor-driver-vs-marker"
  - "patch-definition:immune-state-shift-causal-landscape"
  - "paper:Liu2026"
source_refs: []
created: "2026-06-30"
updated: "2026-06-30"
---

# Proposition: Immune-state displacement mediates PAIS symptoms rather than merely marking another failed-recovery process

## Claim

The persistent immune-state displacement is a **causal mediator** of PAIS symptoms —
i.e. *moving* immune state would *move* symptoms — as opposed to being a **marker /
co-traveler** that merely indexes a distinct primary lesion (autonomic, vascular,
metabolic, or neural). This is the project's **causal-hub** claim and the focal estimand
of `question:0022`. It is **contested and currently unidentified**.

## Evidence Summary

Suggestive but non-decisive: `paper:Liu2026` shows patient IgG disrupting cellular
energetics across post-COVID and other post-infectious ME/CFS — a functional, transferable
immune effect consistent with mediation, but not a demonstration that reversing immune
state reverses the clinical syndrome. The **decisive** test is external and pending: the
abrocitinib JAK1 trial (`hypothesis:0003`, `pre-registration:0004`, NCT06597396), where
**symptom + pathway co-suppression** would evidence mediation and **pathway suppression
without symptom change** would evidence marker/co-traveler status. `question:0006` frames
the same driver-vs-marker split for a specific pathway.

## Caveats

`causal_effect` / `background`, held at **contested / unidentified**. This proposition
**must not inherit support** from `proposition:0038` (that immune state is *displaced*) —
the descriptive→causal slide is exactly the failure mode the reframe exists to prevent.
Note a deeper subtlety: under the maintenance loops (`proposition:0041`) "mediator vs
marker" may be ill-posed at a single timescale — a node can be both depending on phase —
which is why the dynamical treatment (`question:0008`) is a genuine dependency, not a
digression.
