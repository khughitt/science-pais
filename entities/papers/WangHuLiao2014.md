---
id: paper:WangHuLiao2014
kind: paper
title: Stability and Hopf bifurcation for a virus infection model with delayed humoral
  immunity response
status: active
ontology_terms:
- viral dynamics
- humoral immunity
- immune response delay
- Hopf bifurcation
- stability analysis
dataset_usage: []
source_refs:
- cite:WangHuLiao2014
related:
- task:t011
- question:0008-formalize-vicious-cycle-attractor-model
created: '2026-06-25'
updated: '2026-06-25'
---
# Stability and Hopf bifurcation for a virus infection model with delayed humoral immunity response

## Key Contribution

Delayed humoral-immunity viral model deriving threshold conditions for infection-free, infected-without-
immunity, and immune-active states, and showing when humoral immune delay can generate Hopf bifurcation.

## Methods

- **Model type:** within-host viral dynamics with delayed humoral immune response.
- **Analysis:** Lyapunov functionals, LaSalle invariance, local stability, and Hopf bifurcation.
- **Thresholds:** uses reproduction-style threshold parameters to classify equilibrium behavior.
- **Source status:** triaged from DOI/Crossref metadata, indexed abstract, and citation context; full
  text was not locally available during t011.

## Key Findings

- If the basic viral threshold is below the clearance cutoff, the uninfected equilibrium is globally
  asymptotically stable.
- Intermediate threshold conditions stabilize infection without effective immunity.
- Delayed humoral response can destabilize the immune-active equilibrium and generate oscillatory
  dynamics.

## Relevance

Useful for `question:0008` because it distinguishes threshold-governed regimes and delayed feedback
instability, both central to making the PAIS attractor idea quantitative.

## Limitations

- Humoral viral-control model, not a multi-axis PAIS model.
- Does not represent non-viral triggers, antigen fragments, dysautonomia, metabolism, PEM, or recovery
  trajectories.
- Best used as mathematical scaffold, not as evidence for h0001.
