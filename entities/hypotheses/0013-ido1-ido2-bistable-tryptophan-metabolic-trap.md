---
id: hypothesis:0013-ido1-ido2-bistable-tryptophan-metabolic-trap
kind: hypothesis
title: IDO1-IDO2 kinetic imbalance creates a bistable tryptophan metabolic trap in PAIS-susceptible individuals
status: active
source_refs:
- cite:Kashi2019
- cite:Al-Hakeim2023
origins:
- type: assistant
  ref: explore-ideas-mechanism
related:
- question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal
- hypothesis:0001-shared-dysregulated-attractor
created: "2026-07-06"
updated: "2026-07-06"
added_by: explore-ideas:claude-opus-4-8:cand-mechanism-ido-tryptophan-bistable-trap
lens_views:
- lens: mechanism
  rationale: 'The IDO1-IDO2 system exhibits bistable kinetics: IDO1 undergoes substrate inhibition at high tryptophan concentrations, while IDO2 (the low-affinity backup enzyme) is inactivated by common polymorphisms in ~30% of the population. Mathematical modeling shows that a triggering elevation of tryptophan, combined with IDO2 loss-of-function, can drive the system into a self-sustaining pathological attractor persisting for months even after tryptophan inputs normalize. This mechanism is distinct from the PEM-centered metabolic framing and predicts genetic susceptibility (IDO2 genotype) that would stratify PAIS risk across triggers. It has not been tested in PTLDS, post-Q-fever, or post-sepsis cohorts. It is also distinct from the project''s existing IFN-driven tryptophan-malabsorption chain (question:0025): a cell-intrinsic enzymatic bistability with a genetic susceptibility axis, not gut malabsorption.'
  origin_ref: explore-ideas-mechanism
---
# Hypothesis: IDO1-IDO2 kinetic imbalance creates a bistable tryptophan metabolic trap in PAIS-susceptible individuals

## Organizing Conjecture

The IDO1–IDO2 tryptophan-degradation system can behave as a **bistable switch**. IDO1 undergoes
*substrate inhibition* at high tryptophan concentrations, and IDO2 — the low-affinity backup enzyme — is
inactivated by common loss-of-function polymorphisms in a substantial fraction of the population. In
individuals carrying inactivating IDO2 variants, a triggering elevation of tryptophan during acute
infection can push the system into a **self-sustaining pathological attractor** — high tryptophan, low
kynurenine, and depleted NAD⁺ precursors — that persists for months even after tryptophan inputs
normalize. The conjecture is that this cell-intrinsic "metabolic trap" is a **trigger-nonspecific**
route into PAIS with an explicit **genetic-susceptibility axis** (IDO2 genotype), distinct from the
IFN-driven gut-malabsorption chain the project already tracks.

## Proposition Bundle

### Core Propositions

- IDO1 exhibits substrate inhibition, so at elevated tryptophan its flux *falls* rather than rises.
- IDO2 loss-of-function polymorphisms remove the backup pathway in a substantial population fraction.
- The combination admits a **bistable** regime: a perturbation can lock the system in a high-Trp /
  low-Kyn / low-NAD⁺ state that persists after inputs normalize (mathematical-model prediction).
- The trap is **trigger-nonspecific** — it can be entered from any acute infection that transiently
  raises tryptophan, generalizing across PAIS.

### Supporting Or Auxiliary Propositions

- IDO2 genotype stratifies PAIS susceptibility (a testable genetic prediction absent from most cohorts).
- The mechanism is *distinct from* the IFN-I → tryptophan-malabsorption → serotonin-depletion chain of
  `question:0025`: a cell-intrinsic enzymatic bistability with genetic susceptibility, not gut
  malabsorption. The two make **opposite** predictions about the direction of the Trp/Kyn imbalance.

## Current Uncertainty

The hypothesis is a **mathematical-model conjecture** (the IDO "metabolic trap," proposed for ME/CFS),
not an empirically demonstrated attractor. The predicted bistable metabolite signature has not been
directly measured in PAIS cohorts, and the IDO2-genotype association is untested. Available human
metabolomics is cross-sectional endophenotyping, not longitudinal evidence of persistence/hysteresis.
Support is therefore literature-and-model only.

## Predictions

**Strong / discriminating:**

- PAIS cases carrying inactivating IDO2 variants show the paradoxical **high-tryptophan / low-kynurenine**
  pattern — the opposite direction to the IFN-driven low-Trp/high-Kyn signature predicted by
  `question:0025` — which cleanly separates the two mechanisms.
- The metabolite state persists **independent of concurrent inflammation markers** (evidence of an
  autonomous trap rather than an inflammation-driven readout).
- IDO2 loss-of-function genotypes are enriched among PAIS cases across multiple triggers.

**Weaker / corollaries:**

- NAD⁺-precursor depletion accompanies the trap state.
- Interventions that bypass the trap (e.g. downstream kynurenine-pathway or NAD⁺ repletion) shift
  symptoms, whereas tryptophan supplementation does not.

## Falsifiability

Confidence would be materially reduced if:

- PAIS cohorts show **normal** Trp/Kyn ratios, or the **IFN-type low-Trp/high-Kyn** direction, rather
  than the trap's predicted high-Trp/low-Kyn pattern (note: Al-Hakeim2023 already reports the low-Trp
  direction in long COVID — see Disputing Evidence).
- There is **no IDO2-genotype enrichment** in PAIS cases across triggers.
- The metabolite state tracks (is not decoupled from) concurrent inflammation, i.e. no evidence of an
  autonomous bistable attractor.
- Longitudinal metabolomics shows simple monotonic normalization with no hysteresis.

## Supporting Evidence

- **Kashi2019 (literature / mathematical model):** proposes the IDO1–IDO2 bistable tryptophan metabolic
  trap, driven by inactivating IDO2 variants, as an ME/CFS etiology — the core mechanism, but restricted
  to ME/CFS and untested across other PAIS triggers.
- **Al-Hakeim2023 (literature, cross-sectional):** a long-COVID endophenotype with disturbed
  tryptophan-catabolite metabolism maps onto CFS and affective burden — supports that the Trp–Kyn axis is
  symptom-relevant in PASC (see caveat below on *direction*).

## Disputing Evidence

- **Al-Hakeim2023 direction of effect:** reports **low tryptophan / elevated kynurenine** in long COVID —
  the IFN-driven pattern of `question:0025`, which is the **opposite** of the metabolic trap's predicted
  high-Trp / low-Kyn signature. It supports "the Trp–Kyn axis matters" but is in tension with the trap as
  the operative mechanism in long COVID specifically.
- No study has demonstrated the bistability (hysteresis / persistence-after-normalization) the hypothesis
  requires; the metabolic-trap model remains unconfirmed even in ME/CFS.

## Evidence Needed To Shift Belief

- **Most efficient upward:** PAIS metabolomics stratified by IDO2 genotype showing the high-Trp/low-Kyn
  trap signature in loss-of-function carriers, decoupled from inflammation.
- **Most efficient downward:** the same design showing no genotype effect, or the IFN-type direction.
- **Most discriminating next test:** a joint IDO2-genotype × longitudinal-Trp/Kyn design that can detect
  hysteresis and separate this route from the `question:0025` malabsorption chain.

## Related Work

- `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal` — the sibling/rival
  tryptophan route, making opposite directional predictions.
- `hypothesis:0001-shared-dysregulated-attractor` — parent frame; this is a candidate cell-intrinsic
  bistable realization of the attractor with an explicit genetic-susceptibility axis.
- Kashi2019 (ME/CFS metabolic-trap model), Al-Hakeim2023 (long-COVID tryptophan-catabolite endophenotype).
