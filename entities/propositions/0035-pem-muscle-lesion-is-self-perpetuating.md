---
id: proposition:0035-pem-muscle-lesion-is-self-perpetuating
type: proposition
title: PEM muscle mitochondrial-perfusion injury forms a self-perpetuating lesion
status: active
claim_layer: mechanistic_narrative
identification_strength: structural
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: serial muscle OXPHOS/SDH, ROS, perfusion, ion-handling, and recovery-time readouts after standardized exertion
  latent_construct: self-perpetuating muscle mitochondrial-perfusion injury loop that sustains delayed and slow-to-resolve PEM
  measurement_relation: repeated post-exertion worsening and delayed normalization are indirect proxies for positive feedback; causal support requires longitudinal persistence or targeted reversal
  known_failure_modes:
    - one-time post-exercise worsening can reflect transient injury without self-maintaining feedback
    - systemic immune or CNS loops may drive recurrence while muscle remains downstream
    - delayed recovery may arise from endpoint timing rather than a persistent local lesion
discusses:
  - hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
related:
  - hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
  - hypothesis:0001-shared-dysregulated-attractor
  - question:0011-mitochondrial-basis-of-pem
  - proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
  - proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
  - proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
  - evidence-line:0088-scheibenbogen2024-aimm-feedback-weakly-supports-h0006-p4
source_refs:
  - paper:Scheibenbogen2024
created: '2026-06-26'
updated: '2026-06-26'
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
or response to a targeted intervention.

## Measurement Model

Load-bearing evidence would be a longitudinal pre/post/24-48 h/recovery muscle time-course showing that
ionic stress, mitochondrial dysfunction, and perfusion impairment reinforce each other and predict PEM
duration. Interventions that improve perfusion or ion handling and normalize the muscle trajectory would
provide stronger causal evidence.
