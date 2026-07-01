---
id: "proposition:0041-feedback-maintenance-requires-dynamical-treatment-outside-dag"
type: "proposition"
title: "Feedback maintenance of the displaced immune state requires dynamical-systems treatment outside the acyclic DAG"
status: "active"
claim_layer: "structural_claim"
identification_strength: "structural"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0001-shared-dysregulated-attractor"
    role: "background"
related:
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "question:0008-formalize-vicious-cycle-attractor-model"
  - "patch-definition:immune-state-shift-causal-landscape"
  - "concept:immune-autonomic-feedback-loop"
  - "concept:immune-metabolic-feedback-loop"
  - "paper:Perevaryukha2021"
source_refs: []
created: "2026-06-30"
updated: "2026-06-30"
---

# Proposition: Feedback maintenance of the displaced immune state requires dynamical treatment outside the acyclic DAG

## Claim

The *maintenance* of the displaced immune state — the mutually reinforcing
**immune ⇄ autonomic** and **immune ⇄ metabolic** loops that keep the system displaced
after the trigger clears — is a set of **feedback cycles** that an acyclic causal DAG
**cannot represent**. Attractor stability, **bistability**, **hysteresis** (recovery
threshold ≠ onset threshold), and **critical slowing** are properties of a dynamical
system, not of a directed acyclic graph. Therefore these maintenance claims must be
formalized and tested with **time-indexed / dynamical-systems** methods, not by adding
arrows to the landscape sketch.

## Evidence Summary

This is a **structural / methodological** claim, not an empirical one. It is why the two
loop closures are carried as `sci:Unknown` nodes (`concept:immune-autonomic-feedback-loop`,
`concept:immune-metabolic-feedback-loop`) rather than as flow edges in
`patch-definition:immune-state-shift-causal-landscape`. The dynamical machinery for the
downstream test lives in `question:0008` (delay/stability/bifurcation tooling, e.g.
`paper:Perevaryukha2021`), which requires longitudinal recovery-vs-chronification data to
detect the attractor hallmarks. DAGs remain the right tool for the *directional /
confounding / mediation* sub-questions (e.g. the `proposition:0039` hub estimand); the two
representations are complementary, scoped to different questions.

## Caveats

`structural_claim` / `background`. Asserting that maintenance is dynamical does **not**
assert that a true attractor exists — bistability/hysteresis/critical-slowing are the
*predictions to be tested* (`question:0008`), and a longitudinal finding of simple
monotonic decay would disconfirm the attractor reading while leaving the descriptive
displacement (`proposition:0038`) intact.
