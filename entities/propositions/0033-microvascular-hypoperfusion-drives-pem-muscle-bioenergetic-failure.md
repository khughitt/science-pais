---
id: proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
type: proposition
title: Microvascular hypoperfusion or endothelial dysfunction causally drives PEM
  muscle bioenergetic failure
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: provoked iCPET/NIRS peripheral O2 extraction, preload failure,
    muscle perfusion or capillary/oxygen-delivery readouts
  latent_construct: microvascular hypoperfusion or endothelial/dysautonomic extraction
    failure causally upstream of PEM muscle bioenergetic failure
  measurement_relation: delivery/extraction abnormalities are indirect proxies for
    causal hypoperfusion; causal support requires temporal ordering against muscle
    injury and PEM kinetics
  known_failure_modes:
  - extraction failure can reflect intrinsic mitochondrial utilization failure rather
    than upstream delivery failure
  - referral-enriched iCPET cohorts may not generalize to broader PEM-positive PAIS
  - absence of capillary obstruction does not exclude functional shunting or endothelial
    signaling abnormalities
discusses:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
related:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- question:0010-vascular-microclot-subphenotype
- question:0011-mitochondrial-basis-of-pem
- proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
- proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
- evidence-line:0085-joseph2023-peripheral-extraction-weakly-supports-h0006-p2
- evidence-line:0086-appelman2024-no-occlusion-weakly-disputes-simple-ischemic-p2
source_refs:
- paper:Joseph2023
- paper:Appelman2024
created: '2026-06-26'
updated: '2026-06-26'
review_state:
  last_reviewed: '2026-06-26'
  last_review_note: 'No change: claim_layer:causal_effect correctly encodes the assertion''s
    nature while identification_strength:observational + proxy_directness:indirect
    flag it is unidentified; the Appelman hyperoxic-OXPHOS tension (utilization vs
    delivery failure) is already carried by evidence-line 0086 and the first known_failure_mode.
    No drift.'
---
# Proposition: Microvascular hypoperfusion drives PEM muscle bioenergetic failure

## Claim

Microvascular hypoperfusion, endothelial dysfunction, dysautonomic shunting, or related oxygen-delivery
failure is causally **upstream** of PEM-associated skeletal-muscle bioenergetic failure. This is **P2 /
ischemic cause** of `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`.

The claim is about causal ordering, not mere co-occurrence: perfusion/extraction failure should precede
or drive the muscle energetic lesion, rather than being only another downstream manifestation of the same
systemic state.

## Evidence Summary

- **Support (`evidence-line:0085`).** Joseph2023 synthesizes invasive CPET evidence in ME/CFS and PASC:
  preload failure and impaired peripheral O2 extraction are objective provoked abnormalities incompatible
  with simple deconditioning and plausibly localize exertional limitation to delivery/extraction at the
  exercising periphery.
- **Dispute / constraint (`evidence-line:0086`).** Appelman2024 found intrinsic OXPHOS impairment in
  hyperoxic ex-vivo muscle assays and amyloid-containing deposits outside, not inside, capillaries; it did
  not find the simple capillary-occlusion/hypoxia pattern that a strong ischemic-microclot version would
  predict. This weakly disputes a simple ischemic-upstream account while leaving functional vascular or
  shunting mechanisms possible.

## Caveats

This proposition is weaker than P1. The corpus supports peripheral exercise physiology and vascular
plausibility, but does not yet show a time-ordered chain in which hypoperfusion causes the post-PEM
mitochondrial injury. It is therefore `proxy_directness: indirect`: iCPET extraction signatures and
biopsy oxygen-delivery negatives bear on the causal model but do not directly observe causation.

## Measurement Model

Load-bearing measurements would be simultaneous provoked muscle perfusion / oxygen-extraction / biopsy
time-course data, ideally showing that impaired delivery or extraction precedes mitochondrial injury and
tracks PEM severity. Static vascular markers, resting endothelial assays, or downstream muscle biopsy
alone are supportive but insufficient for this causal leg.
