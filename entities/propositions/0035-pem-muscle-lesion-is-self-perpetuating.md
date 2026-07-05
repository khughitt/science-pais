---
id: proposition:0035-pem-muscle-lesion-is-self-perpetuating
kind: proposition
title: PEM muscle mitochondrial-perfusion injury forms a self-perpetuating lesion
status: active
claim_layer: mechanistic_narrative
identification_strength: structural
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: serial muscle OXPHOS/SDH, ROS, perfusion, ion-handling, and recovery-time
    readouts after standardized exertion
  latent_construct: self-perpetuating muscle mitochondrial-perfusion injury loop that
    sustains delayed and slow-to-resolve PEM
  measurement_relation: repeated post-exertion worsening and delayed normalization
    are indirect proxies for positive feedback; causal support requires longitudinal
    persistence or targeted reversal
  known_failure_modes:
  - one-time post-exercise worsening can reflect transient injury without self-maintaining
    feedback
  - systemic immune or CNS loops may drive recurrence while muscle remains downstream
  - delayed recovery may arise from endpoint timing rather than a persistent local
    lesion
  - the ROS limb of the loop may be a downstream consequence of mitochondrial failure
    rather than an upstream feedback driver (open in question:0016), in which case
    the loop does not close at the redox node
discusses:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
related:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- hypothesis:0001-shared-dysregulated-attractor
- question:0011-mitochondrial-basis-of-pem
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
- proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
- proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
- evidence-line:0088-scheibenbogen2024-aimm-feedback-weakly-supports-h0006-p4
source_refs:
- paper:Scheibenbogen2024
created: '2026-06-26'
updated: '2026-06-26'
review_state:
  last_reviewed: '2026-06-26'
  last_review_note: 't057: P4''s ROS feedback limb now points to question:0016''s
    directionality specification. Support requires temporal precedence or target
    engagement showing redox is an upstream/reciprocal driver of the provoked muscle
    trajectory, not only a downstream injury marker.'
---
# Proposition: PEM muscle mitochondrial-perfusion injury forms a self-perpetuating lesion

## Claim

Once established, the PEM-associated muscle lesion can maintain itself through feedback: mitochondrial
injury reduces ATP and raises ROS, impairing ion pumping and vascular function, which worsens perfusion
and further damages mitochondria. This is **P4 / self-perpetuation** of
`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` and the local-muscle version of the broader
`hypothesis:0001` attractor idea.

## Evidence Summary

Support is currently weak and synthetic (`evidence-line:0088`). Scheibenbogen2024 explicitly proposes an
acquired ischemic mitochondrial myopathy (AIMM) feedback loop, and Appelman2024's finding that exercise
worsens muscle OXPHOS/SDH/myopathic features in long COVID is compatible with exertion amplifying an
existing lesion rather than producing normal adaptation.

## Caveats

The corpus has not yet shown longitudinal self-maintenance of the lesion within individuals. A single
post-exercise worsening time point supports provoked aggravation, not chronic positive feedback. The
claim should therefore remain fragile until serial biopsy/imaging demonstrates persistence, recurrence,
or response to a targeted intervention. A further unresolved dependency is the **direction of the redox
limb**: P4 treats ROS as a feedback driver, but `question:0016` asks whether oxidative/redox stress is an
upstream driver of the PAIS bioenergetic lesion or a downstream consequence of mitochondrial failure. If
the latter, the proposed loop does not close at the redox node, so P4's strength is contingent on the
resolution of that question.

## Measurement Model

Load-bearing evidence would be a longitudinal pre/post/24-48 h/recovery muscle time-course showing that
ionic stress, mitochondrial dysfunction, and perfusion impairment reinforce each other and predict PEM
duration. Interventions that improve perfusion or ion handling and normalize the muscle trajectory would
provide stronger causal evidence.

Per `question:0016`, the redox limb specifically requires a directionality test. ROS/redox change should
either precede or independently predict later muscle OXPHOS/SDH decline, ion-handling/perfusion
impairment, and recovery time, or a redox-directed intervention should demonstrate target engagement and
downstream improvement. Redox normalization without muscle or PEM improvement would weaken this P4 limb.
