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
- paper:Klein2023
- paper:Limongelli2026
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
response). This proposition can be true via a non-antibody immune mechanism even if 0018 fails, and it
can be supported by 0019 even where the specific autoantibody target is unknown.

## Evidence Summary

`literature_evidence`, **not yet deposited as graph evidence-lines** (`task:t006` covers the functional-
autoantibody lit-search). Corpus-resident summaries the claim leans on: `paper:deSa2026` (a reported
*causal* link between autoantibodies and neurological symptoms in long COVID, e.g. IgG transfer),
`paper:Klein2023` (long-COVID immune profiling including autoantibody/serology features), and
`paper:Limongelli2026` (immune correlates of post-COVID SFN). These motivate immune mediation but the
detailed pathogenic mechanism is carried by the auxiliary propositions: anti-GPCR pathogenicity
(`proposition:0018`) and the immunomodulation response (`proposition:0019`, where `paper:Stein2025`'s
β2-AR-autoantibody immunoadsorption cohort lives). The bare immune-mediation claim therefore has
**suggestive but uncoded** support; a demonstrated fiber-damaging mechanism remains the open question.

## Caveats

Immune mediation is inferred indirectly (`proxy_directness: indirect`) — no single measurement reads it
off directly, so the claim rests on convergence of the auxiliary routes plus exclusion of
degenerative/metabolic causes. The deflationary account
(`question:0017-deflationary-alternatives-vs-shared-pathophysiology`) offers a non-autoimmune route to
the same symptoms. Because the claim is now the *bare* immune-mediation assertion, its failure modes are
narrower than the elastic original: it is **not** falsified merely because the anti-GPCR mechanism (0018)
fails, since a non-antibody immune mechanism would still satisfy it; it is weakened chiefly if **both**
auxiliary routes fail *and* a non-immune (e.g. metabolic/degenerative/deconditioning) account better fits
the lesion. Conditional on P1.

## Measurement Model

This proposition is not measured by a single instrument; it is supported through its two auxiliary
propositions, which carry the concrete measurement models: anti-GPCR autoantibody assays in
`proposition:0018` and the immunomodulation-response readout in `proposition:0019`. At this (core) level
the operational commitment is only that an **immune signature co-localizes with the lesion and that
non-immune causes are excludable**, with the stronger identification supplied by the interventional
route (0019).
