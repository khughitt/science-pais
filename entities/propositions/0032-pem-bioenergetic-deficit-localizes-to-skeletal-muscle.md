---
id: proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
kind: proposition
title: PEM-relevant bioenergetic pathology localizes materially to skeletal muscle
status: active
claim_layer: structural_claim
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
related:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- question:0011-mitochondrial-basis-of-pem
- proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality
- proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
- proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
- discussion:0004-pem-shared-muscle-lesion-vs-endpoint-contingency
- interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion
- evidence-line:0083-appelman-joseph-t056-muscle-localization-supports-h0006-p1
- evidence-line:0084-walitt2024-central-resting-null-weakly-disputes-h0006-p1
source_refs:
- paper:Appelman2024
- paper:Walitt2024
created: '2026-06-26'
updated: '2026-06-26'
review_state:
  last_reviewed: '2026-06-26'
  last_review_note: 'No change: claim (''material site'', not ''only site'') is correctly
    narrower than the evidence; supports/disputes balance (0083 moderate / 0084 weak-generalization)
    matches the contested belief surface; caveats already flag endpoint non-interchangeability
    and primary-vs-secondary. Reviewed in conjunction with h0006 ROS/q0016 fix on
    the bundle.'
---
# Proposition: PEM-relevant bioenergetic pathology localizes materially to skeletal muscle

## Claim

Post-exertional malaise (PEM) is accompanied by objective pathology in skeletal muscle, and skeletal
muscle is a material site of the bioenergetic deficit rather than merely a passive recipient of central
fatigue or deconditioning. This is **P1 / localization** of
`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`.

The claim is deliberately narrower than "skeletal muscle is the only site" and broader than
`proposition:0030`: it admits long-COVID provoked muscle biopsy, invasive/exercise physiology, and ME/CFS
exercise/contraction muscle-bioenergetics as convergent localization evidence, while leaving causation to
P2/P3 (`proposition:0033`, `proposition:0034`).

## Evidence Summary

- **Support (`evidence-line:0083`).** Appelman2024 directly shows a long-COVID post-PEM skeletal-muscle
  lesion: reduced OXPHOS capacity, selective post-exertional SDH decline, glycolytic fiber shift, and
  exercise-exacerbated myopathic injury. Joseph2023 adds a provoked peripheral physiology frame
  (impaired O2 extraction / preload failure), and the t056 ME/CFS body (`proposition:0030`) shows
  exercise/contraction-linked muscle bioenergetic abnormalities in ME/CFS.
- **Dispute / constraint (`evidence-line:0084`).** Walitt2024's rigorously adjudicated PI-ME/CFS cohort
  emphasizes central effort-preference/autonomic circuitry and reports no basal PBMC mitochondrial
  dysfunction, resting-energy-expenditure difference, or classical muscle-fiber abnormality. This does not
  refute the provoked muscle claim, but it weakly disputes the stronger "primary muscle substrate" reading.

## Caveats

P1 is a localization proposition, not a full mechanism. It does not establish that hypoperfusion is
upstream, that Na/Ca overload mediates injury, or that the same muscle lesion is shared across long COVID
and ME/CFS under a harmonized protocol. It also remains endpoint-sensitive in exactly the sense captured
by h0008-M3 (`proposition:0029`): whole-body CPET, 31P-MRS, resting biopsy, post-PEM biopsy, and cell
culture contraction models are related but not interchangeable endpoints.

## Measurement Model

Direct muscle-local evidence includes provoked skeletal-muscle biopsy/respirometry/histology, muscle
31P-MRS during exercise/recovery, muscle-cell contraction-response assays, and invasive or NIRS-based
peripheral oxygen-extraction measures. Systemic blood metabolomics, PBMC mitochondrial assays, and central
imaging/catecholamine endpoints are relevant rivals or context but do not directly measure the muscle
lesion.
