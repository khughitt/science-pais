---
id: interpretation:0024-t011-delayed-viral-dynamics-models
type: interpretation
title: "t011: Delayed viral-dynamics ODE/DDE papers supply mathematical motifs, not a PAIS attractor model"
status: active
source_refs:
  - paper:Perevaryukha2021
  - paper:Wang2007
  - paper:Xie2010
  - paper:WangHuLiao2014
related:
  - task:t011
  - question:0008-formalize-vicious-cycle-attractor-model
  - hypothesis:0001-shared-dysregulated-attractor
  - topic:shared-failure-mode-across-pais
created: "2026-06-25"
updated: "2026-06-25"
input:
  - paper:Perevaryukha2021
  - paper:Wang2007
  - paper:Xie2010
  - paper:WangHuLiao2014
prior_interpretations:
  - interpretation:0023-t007-microbiome-gut-brain-axis
relations: []
---

<!-- Mode: METHODS TRIAGE. This pass evaluates quarantined mathematical-model papers as substrate for q0008; it deliberately adds no belief-bearing empirical evidence-lines. -->

# Interpretation: t011 - delayed viral-dynamics models as attractor substrate

## Verdict

**[~] Useful mathematical motifs; [-] not a ready PAIS model.**

The four quarantined papers belong in the project as modeling references, but only as *scaffold*. They
show how delayed immune response, initial perturbation, threshold parameters, stability switches, and
Hopf bifurcation can be formalized. That is directly relevant to `question:0008`: it moves the attractor
language from metaphor toward a tractable dynamical-systems vocabulary.

They do **not** constitute evidence for `hypothesis:0001`, and they should not be used as if PAIS has
already been modeled. All four are active-infection viral models, not post-acute cross-trigger models
with immune-autonomic-metabolic loop nodes.

## What Each Paper Contributes

| Paper | Useful motif | Why it is insufficient |
|---|---|---|
| Perevaryukha2021 | Initial dose + delayed immune response can shift trajectories among asymptomatic suppression, acute disease, chronic phase, and fatal outcome | Still centered on infection-course scenarios; not a fitted PAIS recovery/chronification model |
| Wang2007 | Immune-response delay can destabilize a viral model and produce Hopf bifurcation / oscillation | Oscillation in viral dynamics is not the same as a stable post-acute attractor basin |
| Xie2010 | Compact stability/Hopf analysis for delayed immune-response viral infection | Generic active-infection DDE; no PAIS state variables |
| WangHuLiao2014 | Humoral-delay model with threshold-governed equilibrium regimes and Hopf bifurcation | Humoral viral-control abstraction only; no multi-loop PAIS architecture |

## Implication for `question:0008`

The modeling path should **borrow the formal machinery, not the state vector**.

The t011 set points to a minimum formal vocabulary for PAIS:

- state variables for loop nodes, not just viral load: immune activation/resolution, autonomic tone or
  perfusion, metabolic/bioenergetic capacity, neuroinflammatory/CNS state, gut/barrier or antigen load;
- delayed feedback terms, because immune and physiological recovery are not instantaneous;
- threshold or separatrix structure, because h0001 predicts recovery-vs-chronification regimes rather
  than simple monotonic decay;
- explicit tests for bistability, hysteresis, critical slowing, and multi-node escape thresholds;
- empirical fitting to longitudinal PAIS cohorts, because formal bifurcation alone is not evidence.

## Implication for `hypothesis:0001`

No belief-band update is warranted. The papers make h0001 more formalizable, not more empirically true.
They provide a defensible route for rewriting the "shared dysregulated attractor" as a model class, but
the load-bearing tests remain untouched: cross-trigger molecular convergence, longitudinal
recovery-vs-chronification trajectories, and superiority of multi-node intervention over single-node
intervention.

## Boundary Decision

The quarantined papers should be retained as project-local modeling references because q0008 is a
project-native question. They should **not** be promoted as PAIS biology papers or used as evidence-lines
for any hypothesis until a PAIS-specific model is built or fitted.

## Next Modeling Step

Draft `pre-registration` or `plan` material for q0008 only after identifying a candidate longitudinal
dataset with repeated markers from at least two loop axes. A minimal runnable model could start with a
two- or three-node delayed feedback system and compare:

1. monotonic recovery model;
2. delayed-feedback oscillatory model;
3. bistable/separatrix model.

The discriminating output should be predictive fit to recovery vs chronification, not visual similarity
to a theoretical phase portrait.
