---
id: proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
kind: proposition
title: Functional anti-GPCR autoantibodies are pathogenic for the PAIS small-fiber/autonomic
  lesion (not merely an epiphenomenal marker)
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: anti-GPCR serology, functional receptor-activation assays, autonomic-function correlations, and antibody-depletion or transfer readouts
  latent_construct: pathogenic anti-GPCR autoantibody contribution to PAIS small-fiber/autonomic injury
  measurement_relation: serum antibody measures are indirect mechanism proxies; pathogenicity requires tracking between antibody function or removal and the small-fiber/autonomic phenotype
  known_failure_modes:
  - binding ELISA positivity is non-specific in POTS and controls
  - functional autonomic correlations do not prove small-fiber structural injury
  - antibody reduction may not predict clinical or lesion response if antibodies are markers rather than drivers
discusses:
- frame: hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
  role: background
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- proposition:0016-pais-sfn-autoimmune-causation
- question:0009-functional-autoantibodies-drive-dysautonomia
- task:t006
- interpretation:0010-t006-functional-gpcr-autoantibody-ingestion
source_refs:
- paper:Stein2025
- paper:Kharraziha2020
- paper:Loebel2016
- paper:Hall2022
- paper:Schmitz2026
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

`literature_evidence`, **the weakest leg** — and now **contested** following the `task:t006` functional-
autoantibody ingestion (`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`; original
coding via `task:t049` / `interpretation:0009`). The validator flags this proposition
`belief.fragile-single-line` — the verdict flips on dropping any single line, the honest state of a thin
base. The coded lines, all on the **autonomic-function** axis:

- **Support — functional (the strongest):** `evidence-line:0049` (`paper:Kharraziha2020`, *moderate*) —
  functional FRET assay, α1-AR **activity** correlates with orthostatic-symptom severity (β=0.77, p=0.009,
  surviving ΔHR/ΔSBP). Off the canonical β/M targets and in POTS not PAIS, but the best *functional*
  correlational evidence.
- **Support — weak/binding or associational:** `evidence-line:0050` (`paper:Loebel2016` — ME/CFS β2/M3/M4
  binding-ELISA seroprevalence, no functional confirmation); `evidence-line:0052` (`paper:Schmitz2026` —
  long-COVID anti-GPCR↔HRV/BP, but its own in-vitro cardiomyocyte test was **null**); `evidence-line:0048`
  (`paper:Stein2025` — β2-AR-selected immunoadsorption, but β2-AR reduction did not predict response).
- **Dispute:** `evidence-line:0051` (`paper:Hall2022`, *moderate*, `model_criticism`) — standard binding
  ELISA scores 98% POTS / 100% healthy controls seropositive with no group difference; binding-ELISA
  seropositivity is non-specific. It **guts the binding-ELISA support without touching the functional-
  assay support** (0049) — the two do not cancel.

Two structural gaps remain decisive: (1) the strongest *causal* autoantibody evidence (`paper:deSa2026`,
`evidence-line:0045`, on `proposition:0016`) targeted **non-GPCR** antigens (MED20/USP5) and spared the
autonomic axis; (2) **no line links any anti-GPCR antibody to the small-fiber lesion** (`proposition:0014`/
`0015`) — every endpoint is autonomic *function*, so the antibody→*lesion* bridge this proposition asserts
is untested. That bridge is co-measurable in the `pre-registration:0003` G5 serology arm.

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
