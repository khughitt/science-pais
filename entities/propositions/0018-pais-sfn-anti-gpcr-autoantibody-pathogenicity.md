---
id: proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
type: proposition
title: Functional anti-GPCR autoantibodies are pathogenic for the PAIS small-fiber/autonomic
  lesion (not merely an epiphenomenal marker)
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
discusses:
- frame: hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
  role: background
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- proposition:0016-pais-sfn-autoimmune-causation
- question:0009-functional-autoantibodies-drive-dysautonomia
- task:t006
source_refs:
- paper:Stein2025
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Functional anti-GPCR autoantibodies are pathogenic for the PAIS small-fiber/autonomic lesion

## Claim

Functional anti-GPCR autoantibodies (β-adrenergic / muscarinic) are **pathogenic** for the PAIS
small-fiber/autonomic lesion — i.e. they causally produce or sustain small-fiber dysfunction/loss —
rather than being an **epiphenomenal marker** of immune activation that travels with the lesion without
causing it. Subject = functional anti-GPCR autoantibodies; predicate = *causally damage / dysregulate*;
object = autonomic and sensory small fibers. This is the **mechanism-specific** auxiliary route under the
core immune-mediation claim (`proposition:0016`): it is one way — not the only way — that core claim
could be true. It is the single weakest link in `hypothesis:0007`.

## Evidence Summary

`literature_evidence`, **coded via `task:t049`** (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`) —
and the **weakest leg**. The only coded support is `evidence-line:0048` (`paper:Stein2025`, weak/proxy:
anti-GPCR β2-AR autoantibody selection + depletion-associated autonomic improvement, but β2-AR reduction
did **not** predict response). Critically, the strongest *causal* autoantibody evidence (`paper:deSa2026`,
`evidence-line:0045`, coded against `proposition:0016`) targeted **non-GPCR** antigens (MED20/USP5) and did
**not** recapitulate the autonomic axis — so anti-GPCR-specific pathogenicity *of small fibers / the
autonomic lesion* remains essentially unproven. `task:t006` should seek anti-GPCR evidence on the
autonomic axis specifically.

## Caveats

`proxy_directness: indirect` — serum autoantibody titer indexes the candidate mechanism, it does not
measure fiber damage. The proposition is acutely exposed to **reverse causation / epiphenomenon**:
autoantibodies are common after infection and may be a bystander of immune activation. Passive-transfer
evidence (deSa2026) addresses general neurological symptoms, not the small-fiber lesion of P1/P2, so a
gap remains between "autoantibodies cause symptoms" and "autoantibodies cause *this lesion*." If
seropositivity does not track lesion severity and antibody removal does not alter lesion trajectory
(`proposition:0019`), this route fails — **without** necessarily falsifying core immune mediation
(`proposition:0016`), which a non-antibody immune mechanism could still satisfy.

## Measurement Model

**Functional anti-GPCR autoantibody assays** — β1/β2-adrenergic and M3/M4-muscarinic receptor
antibodies via cell-based functional (receptor-activation) or binding assays — as the exposure; the
causal readout is (a) a titer/seropositivity ↔ small-fiber-severity correlation and, decisively, (b)
passive-transfer or antibody-depletion experiments showing the small-fiber phenotype tracks the
antibody. Identification is strongest from the interventional/transfer designs, not from cross-sectional
seroprevalence.
