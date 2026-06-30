---
id: proposition:0016-pais-sfn-autoimmune-causation
type: proposition
title: The PAIS small-fiber lesion is immune-mediated (functional anti-GPCR autoantibodies
  / immunomodulation-responsive)
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: passive-transfer effects, autoantibody/immune signatures, and lesion response to immunomodulation
  latent_construct: immune-mediated causation or maintenance of the PAIS small-fiber lesion
  measurement_relation: immune mediation is inferred from convergence between lesion co-localization, immune perturbation, and interventional or transfer evidence rather than from a single direct assay
  known_failure_modes:
  - autoantibody signals may be epiphenomenal markers of immune activation
  - transfer evidence may reproduce neurological symptoms without reproducing the autonomic or biopsy lesion
  - trigger-specific immune mechanisms may not generalize across PAIS syndromes
discusses:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- question:0009-functional-autoantibodies-drive-dysautonomia
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0015-pais-sfn-non-length-dependent-pattern
- proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
- proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory
- topic:post-infectious-dysautonomia-and-autoimmunity
- task:t006
source_refs:
- paper:deSa2026
- paper:Walitt2024
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: The PAIS small-fiber lesion is immune-mediated (functional anti-GPCR autoantibodies / immunomodulation-responsive)

## Claim

The PAIS small-fiber lesion (`proposition:0014`, `proposition:0015`) is **immune-mediated** — caused or
maintained by an autoimmune process — rather than degenerative, metabolic, or deconditioning-driven.
Subject = an autoimmune process; predicate = *causally produces / sustains*; object = the peripheral
small-fiber lesion. This is a `causal_effect` / mechanistic claim and the **weakest leg** of
`hypothesis:0007`: it supplies the mechanism that the non-length-dependent pattern (P2) implicates.

The claim is deliberately scoped to the **bare immune-mediation** assertion. The two specific evidential
routes that were previously folded into one elastic "and/or" statement are now carried as **separate,
individually falsifiable auxiliary propositions**, each supporting (not constituting) this claim:
`proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity` (the anti-GPCR-autoantibody mechanism)
and `proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory` (the interventional
response). This proposition can be true via a non-antibody immune mechanism even if `proposition:0018` fails, and it
can be supported by `proposition:0019` even where the specific autoantibody target is unknown.

## Evidence Summary

`literature_evidence`, **coded via `task:t049`** (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`).
The claim is **split**: causally supported for long COVID and disputed for ME/CFS.
- **Support (strong, causal):** `evidence-line:0045` — `paper:deSa2026` passive-transfers long-COVID patient
  IgG to mice and reduces intraepidermal nerve fibers, demonstrating autoantibodies are *sufficient* to
  produce SFN. (Caveat carried below: its validated autoantigens were non-GPCR and it did not reproduce
  the autonomic axis.)
- **Dispute (weak):** `evidence-line:0046` — `paper:Walitt2024` found *no uniform autoantibody signal* in
  rigorously adjudicated PI-ME/CFS, arguing against a pan-PAIS autoimmune mechanism (underpowered, n=17).

So immune mediation is **trigger-specific in current evidence** (demonstrated for LC, absent in the best
ME/CFS cohort), not pan-PAIS. The detailed pathogenic mechanism is carried by the auxiliary propositions:
anti-GPCR pathogenicity (`proposition:0018`) and the immunomodulation response (`proposition:0019`, where
`paper:Stein2025`'s β2-AR-autoantibody immunoadsorption cohort lives). `paper:Klein2023` (LC immune
profiling) and `paper:Limongelli2026` (immune correlates of post-COVID SFN) remain supporting *context*
in the broader literature but are not coded as `proposition:0016`-targeted evidence-lines.

## Caveats

Immune mediation is inferred indirectly (`proxy_directness: indirect`) — no single measurement reads it
off directly, so the claim rests on convergence of the auxiliary routes plus exclusion of
degenerative/metabolic causes. The deflationary account
(`question:0017-deflationary-alternatives-vs-shared-pathophysiology`) offers a non-autoimmune route to
the same symptoms. Because the claim is now the *bare* immune-mediation assertion, its failure modes are
narrower than the elastic original: it is **not** falsified merely because the anti-GPCR mechanism (`proposition:0018`)
fails, since a non-antibody immune mechanism would still satisfy it; it is weakened chiefly if **both**
auxiliary routes fail *and* a non-immune (e.g. metabolic/degenerative/deconditioning) account better fits
the lesion. Conditional on P1.

## Measurement Model

This proposition is not measured by a single instrument; it is supported through its two auxiliary
propositions, which carry the concrete measurement models: anti-GPCR autoantibody assays in
`proposition:0018` and the immunomodulation-response readout in `proposition:0019`. At this (core) level
the operational commitment is only that an **immune signature co-localizes with the lesion and that
non-immune causes are excludable**, with the stronger identification supplied by the interventional
route (`proposition:0019`).
