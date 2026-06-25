---
id: question:0008-formalize-vicious-cycle-attractor-model
type: question
title: Can the mutually reinforcing vicious-cycle model of PAIS be formalized as a
  dynamical-systems or causal-graph hypothesis that makes discriminating predictions
  distinguishing chronification from recovery?
status: active
ontology_terms:
- dynamical systems
- attractor state
- causal model
- homeostasis
datasets: []
source_refs:
- cite:Komaroff2025
- cite:Trautmann2025
- cite:Komaroff2023
- cite:Perevaryukha2021
- cite:Wang2007
- cite:Xie2010
- cite:WangHuLiao2014
related:
- topic:shared-failure-mode-across-pais
- interpretation:0024-t011-delayed-viral-dynamics-models
created: '2026-06-11'
updated: '2026-06-25'
---

# Can the mutually reinforcing vicious-cycle model of PAIS be formalized as a dynamical-systems or causal-graph hypothesis that makes discriminating predictions distinguishing chronification from recovery?

## Summary

The "mutually reinforcing physiological vicious cycles" framing (Komaroff2025, Komaroff2023) and the "self-sustained inflammatory loops" model (Trautmann2025) are the project's leading conceptual account of why PAIS persists and resists single-target therapy. But as stated they are largely qualitative. This question asks whether the model can be formalized as a dynamical-systems or causal-graph hypothesis that makes *discriminating* predictions separating chronification from recovery — i.e. turning an appealing metaphor into a testable theory.

## Why It Matters

- A formal model would predict which interventions (and which combinations) can escape the attractor, directly guiding combination-therapy trial design, and would make the "stable attractor" claim falsifiable.
- If unanswered, the vicious-cycle framing remains unfalsifiable narrative, unable to discriminate among competing single-mechanism hypotheses (antigen, autoimmunity, exhaustion) or to justify multi-target intervention.

## Current Evidence

- Supporting: Komaroff2025 specifies candidate reinforcing nodes (antigen/nucleic-acid persistence, autoantibody-mediated autonomic dysfunction, mitochondrial/energetic impairment) and predicts no single-target intervention suffices; Komaroff2023 maps seven interacting domains; Trautmann2025 predicts patients with more co-active loops are more severe and more treatment-refractory; Che2025 provides multi-pathway, exercise-worsened data consistent with self-reinforcement.
- Modeling substrate (t011): Perevaryukha2021, Wang2007, Xie2010, and WangHuLiao2014 show that delayed
  immune feedback, initial perturbation, threshold regimes, stability switches, and Hopf bifurcation are
  established tools for within-host viral dynamics. They are useful mathematical scaffolds for this
  question, but not PAIS evidence: their state variables are active-infection virus/immune variables, not
  post-acute immune-autonomic-metabolic loop nodes.
- Conflicting / gaps: no published study integrates biomarker panels covering all proposed loop axes in one cohort to test co-occurrence vs severity; the models do not yet specify the *sign and strength* of edges needed for a true bistable/attractor formalism; causal priority among nodes is unassigned (Komaroff2023).

## Thoughts

- Best current interpretation: the vicious-cycle account is biologically motivated and consistent with the data, but currently lacks the quantitative edge specification required for discriminating predictions (e.g. existence of a separatrix, hysteresis, multi-node intervention thresholds).
- t011 narrows the formalization path: borrow the delay/stability/bifurcation machinery from viral
  DDE/ODE models, but replace the state vector with PAIS loop nodes and fit against longitudinal recovery
  vs chronification data.
- Major uncertainty: whether longitudinal multi-omic data show the hallmarks of a true attractor (bistability, hysteresis, critical slowing) versus monotonic decay, and which nodes are causal vs reactive.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (this question is its formalization/falsification path).
- Required data or analyses: longitudinal multi-axis biomarker cohorts; causal-graph/DAG construction; dynamical-systems fitting (test for bistability, critical slowing) against recovery vs chronification trajectories; loop-co-occurrence vs severity test.
- Priority level: P1 — converts the project's organizing conjecture into a testable, computational form.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`, `topic:mecfs-long-covid-convergence`.
- Article notes: Komaroff2025, Trautmann2025, Komaroff2023, Che2025.
- Methods notes: `interpretation:0024-t011-delayed-viral-dynamics-models`; Perevaryukha2021, Wang2007,
  Xie2010, WangHuLiao2014.
- Methods/Datasets: candidate longitudinal multi-omic PAIS cohorts; latent-transition modeling (Gusinow2026) as an empirical state-structure anchor.
