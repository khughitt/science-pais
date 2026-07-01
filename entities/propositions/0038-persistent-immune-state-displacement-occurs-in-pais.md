---
id: "proposition:0038-persistent-immune-state-displacement-occurs-in-pais"
type: "proposition"
title: "PAIS involve a persistent post-infectious immune-state displacement (descriptive)"
status: "active"
claim_layer: "empirical_regularity"
identification_strength: "observational"
proxy_directness: "indirect"
measurement_model:
  observed_entity: circulating cytokines, cell-subset frequencies and phenotypes, autoantibody panels, and blood/tissue transcriptomes
  latent_construct: the immune-system state / set-point (its persistent configuration after acute infection)
  measurement_relation: the latent state is inferred indirectly from these proxies; under degeneracy (proposition:0037) a real state shift may present through different proxies across cohorts
  known_failure_modes:
  - analyte-level heterogeneity across triggers/cohorts can mask a shared state shift
  - timepoint / variant / treatment confounding
  - absence of pre-infection baselines, so displacement is inferred from cross-sectional case-vs-control rather than within-person departure from set-point
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0001-shared-dysregulated-attractor"
    role: "background"
related:
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "hypothesis:0003-immune-exhaustion-feedback"
  - "patch-definition:immune-state-shift-causal-landscape"
  - "question:0022-immune-state-displacement-mediator-vs-co-traveler"
  - "paper:Klein2023"
  - "paper:Talla2023"
  - "paper:Sommen2026"
source_refs: []
created: "2026-06-30"
updated: "2026-06-30"
---

# Proposition: PAIS involve a persistent post-infectious immune-state displacement (descriptive)

## Claim

Across multiple PAIS triggers, the immune system is measurably held in an **altered
configuration** for months-to-years after acute infection — i.e. immune state is
**persistently displaced** from a normal/recovered set-point. This is a **descriptive**
(empirical-regularity) claim about the *existence and persistence* of an immune-state
shift. It asserts nothing about whether that shift **drives** symptoms (that is the
strictly separate causal-hub claim, `proposition:0039`) and nothing about a shared
*analyte* identity (`proposition:0037`).

## Evidence Summary

Representative (not exhaustive) anchors: `paper:Klein2023` (multimodal long-COVID immune
phenotyping months out), `paper:Talla2023` (persistent inflammatory/IFN tone in long
COVID), and `paper:Sommen2026` (a shared terminal-NK signature across post-COVID *and*
non-COVID post-infective fatigue). The evidence is observational and proxy-mediated (see
`measurement_model`): it establishes that *some* persistent immune alteration is detectable,
while the *specific* proxies differ by cohort — which is expected under the degeneracy
reading (`proposition:0037`) and does not undercut the descriptive claim.

## Caveats

`empirical_regularity` / `background`. Held at descriptive strength deliberately: most
support is cross-sectional and lacks pre-infection baselines, so "displacement" is inferred
from case-vs-control contrasts rather than within-person departure. **This proposition must
never lend its support to `proposition:0039`** — that immune state is *shifted* is not
evidence that it is the *driver*.
