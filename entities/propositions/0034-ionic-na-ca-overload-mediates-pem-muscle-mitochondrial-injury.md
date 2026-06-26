---
id: proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
type: proposition
title: Sodium and calcium overload mediate the step from hypoperfusion to PEM muscle
  mitochondrial injury
status: active
claim_layer: mechanistic_narrative
identification_strength: structural
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: skeletal-muscle intracellular sodium imaging, inferred Na/H and
    Na/Ca exchange behavior, calcium-overload markers, and subsarcolemmal mitochondrial
    injury
  latent_construct: ionic mediation of hypoperfusion-to-mitochondrial-injury in PEM
    muscle
  measurement_relation: sodium/calcium and injury readouts are indirect mediator proxies;
    support requires exercise-timed co-variation and ordering across the proposed
    cascade
  known_failure_modes:
  - elevated sodium may be a downstream marker of muscle stress rather than a mediator
  - calcium overload is currently inferred rather than directly measured in human
    PAIS muscle
  - single-group mechanistic synthesis may overfit heterogeneous biopsy and imaging
    findings
discusses:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
related:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- question:0011-mitochondrial-basis-of-pem
- proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
- proposition:0035-pem-muscle-lesion-is-self-perpetuating
- evidence-line:0087-scheibenbogen2024-na-ca-cascade-weakly-supports-h0006-p3
source_refs:
- paper:Scheibenbogen2024
created: '2026-06-26'
updated: '2026-06-26'
review_state:
  last_reviewed: '2026-06-26'
  last_review_note: 'No change: claim honestly self-labels weakest/model-heavy, single-source
    (Scheibenbogen2024), with calcium overload explicitly inferred-not-measured. ROS/q0016
    dependency lives at the P4 self-perpetuation node (0035), not the Na/Ca mediator
    step, so q0016 link belongs on 0035 not here. No drift.'
---
# Proposition: Sodium and calcium overload mediate PEM muscle mitochondrial injury

## Claim

In the h0006 cascade, exertion under hypoperfusion drives anaerobic metabolism and proton handling,
raising intracellular sodium through Na/H exchange; sodium loading then reverses Na/Ca exchange, causing
calcium overload that injures subsarcolemmal mitochondria. This is **P3 / ionic mediator** of
`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`.

## Evidence Summary

The current support is **weak and model-heavy** (`evidence-line:0087`). Scheibenbogen2024 summarizes the
Wirth/Scheibenbogen AIMM model and cites a 23Na-MRI anchor for elevated intracellular skeletal-muscle
sodium in ME/CFS, with sodium inversely associated with handgrip strength. It also notes biopsy patterns
the authors interpret as consistent with subsarcolemmal mitochondrial vulnerability.

## Caveats

This is the weakest core leg. The full Na/H -> Na loading -> NCX reversal -> Ca overload -> mitochondrial
injury chain has not been demonstrated end-to-end in human PAIS muscle under a provoked PEM protocol.
Direct human calcium overload measurement in the PAIS context is absent in the current corpus, and the
review evidence comes from the same group that proposed the model.

## Measurement Model

The decisive measurement would pair provoked exercise with serial skeletal-muscle intracellular sodium
and calcium markers, mitochondrial injury markers, and symptom kinetics, ideally showing the ionic shift
precedes or co-varies with post-PEM OXPHOS/SDH decline. 23Na-MRI alone supports the sodium-loading step
but not the full mediator chain.
