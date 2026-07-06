---
id: paper:Perevaryukha2021
kind: paper
title: A Continuous Model of Three Scenarios of the Infection Process with Delayed
  Immune Response Factors
status: active
ontology_terms:
- viral dynamics
- delay differential equation
- delayed immune response
- chronic infection
- bifurcation
dataset_usage: []
source_refs:
- cite:Perevaryukha2021
related:
- task:t011
- question:0008-formalize-vicious-cycle-attractor-model
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-25'
updated: '2026-06-25'
---
# A Continuous Model of Three Scenarios of the Infection Process with Delayed Immune Response Factors

## Key Contribution

Delay-differential infection model in which initial viral dose and delayed immune-response timing can
produce qualitatively different trajectories: efficient asymptomatic suppression, acute symptomatic
disease, chronic phase, or fatal outcome. Within the t011 quarantine set, this is the closest conceptual
analogue to the project's severity-threshold / failed-recovery framing.

## Methods

- **Model type:** delay differential equation with two immune-response time lags.
- **System represented:** within-host viral replication plus delayed host immune defense.
- **Use case:** theoretical scenario analysis, motivated by heterogeneous SARS-CoV-2 and HCV infection
  courses.
- **Outputs:** transitions between infection-course scenarios as viral dose and immune delay vary.

## Key Findings

- Infection course is modeled as state-dependent and path-dependent rather than a single monotonic
  trajectory.
- Variation in initial dose and immune-response timing can shift the modeled course from acute clearance
  toward chronic persistence or fatal progression.
- Asymptomatic infection is represented as rapid immune suppression after a short replication phase, with
  low-level persistence still possible in the model.

## Relevance

Useful for `question:0008` as a mathematical motif: delayed immune response plus initial perturbation can
generate discrete recovery/non-recovery regimes. It is **not** a ready PAIS attractor model because it
models active infection trajectories, not post-acute multi-axis immune-autonomic-metabolic loops after
pathogen clearance.

## Limitations

- The paper is a theoretical viral-infection model, not a PAIS cohort or fitted long-COVID/ME/CFS model.
- The state variables are centered on virus and immune response; they do not include autonomic,
  metabolic, vascular, gut, or neurocognitive loop nodes.
- It provides threshold/trajectory intuition but does not test bistability, hysteresis, or critical
  slowing in longitudinal PAIS data.
