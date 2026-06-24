---
id: proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load
type: proposition
title: Retained fragment burden/duration predicts chronic PAIS onset better than initial
  pathogen load
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0002-tissue-reservoir-antigen-fragment
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- topic:antigen-pathogen-persistence
- proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
- task:t052
source_refs:
- paper:McClune2025
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Retained fragment burden/duration predicts chronic PAIS onset better than initial pathogen load

## Claim

The proximal determinant of who develops chronic post-infectious illness is **how much degradation-
resistant fragment is retained, and for how long** — *not* the initial pathogen load at acute infection.
Subject = retained-fragment burden/duration (set by fragment chemistry and host clearance genetics);
predicate = *predicts chronic-PAIS onset better than*; object = initial pathogen load. This is the
**risk-determinant conjunct** of `hypothesis:0002` — the claim that makes fragment *retention* (rather than
infection severity per se) the causal lever, and the one that, if true, reframes prevention/prognosis
around clearance kinetics. It is logically downstream of persistence (`proposition:0022`) and distinct
from it: 0022 says the fragment lingers and is bioactive; **0024 says the *quantity/duration* of that
lingering is the thing that determines chronicity.**

## Evidence Summary

**No supporting evidence is coded — this is an untested, prospective-design *prediction* of
`hypothesis:0002`, held at `speculative`.** McClune2025 supplies the *mechanistic motivation*
(fragment-retention duration, governed by glycan chemistry and Kupffer-cell handling, is the proposed
driver; host TLR1/TLR2 clearance variants are proposed modulators) but does **not** test the
burden-vs-load comparison: no cohort has measured retained-fragment burden at treatment completion and
shown it out-predicts initial pathogen load for subsequent chronic-illness diagnosis. Per
`hypothesis:0002`'s Predictions, the discriminating test is a prospective cohort with a fragment-retention
readout (e.g. r-mAb2G10 pPG^Bb ELISA at treatment completion, or a Simoa antigen index) versus an
acute-load measure, with chronic-illness diagnosis as the endpoint.

## Caveats

Coded with **no supporting evidence-line on purpose**, so the conjunctive roll-up of `hypothesis:0002`
reflects that this load-bearing risk-determinant claim is untested — keeping the hypothesis honestly
`speculative` rather than letting the supported persistence pillar (`proposition:0022`) carry it. Note the
near-relationship to the *prevention* evidence in `proposition:0021`: the metformin trials show an
acute-phase intervention lowers incidence, but they are **mechanism-agnostic** (antiviral vs. metabolic
unresolved) and say nothing about *fragment burden* as the lever — so 0021 must **not** be coded as
support here (that would re-introduce the t051 over-credit). Promotion path: a prospective
burden-predicts-chronicity result would be minted as a supporting evidence-line on this proposition.
