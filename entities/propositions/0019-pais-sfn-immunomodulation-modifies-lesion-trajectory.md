---
id: proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory
kind: proposition
title: Immunomodulation that lowers autoantibody burden improves the PAIS autonomic/small-fiber
  lesion trajectory
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- frame: hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
  role: background
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- proposition:0016-pais-sfn-autoimmune-causation
- proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
- question:0009-functional-autoantibodies-drive-dysautonomia
source_refs:
- paper:Stein2025
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Immunomodulation that lowers autoantibody burden improves the PAIS autonomic/small-fiber lesion trajectory

## Claim

Interventions that **lower autoantibody burden or dampen the autoimmune process** (immunoadsorption,
plasma exchange, IVIG, B-cell-directed therapy) **improve the trajectory** of the PAIS autonomic /
small-fiber lesion — autonomic-function measures and, ideally, IENFD/SGNFD recover or stop declining.
Subject = autoantibody-lowering immunomodulation; predicate = *causally improves*; object = the autonomic
/ small-fiber lesion trajectory. This is the **interventional** auxiliary route under the core
immune-mediation claim (`proposition:0016`) and the strongest available identification path for it: a
response to removing the immune driver is hard to explain on a purely degenerative/deconditioning
account.

## Evidence Summary

`literature_evidence`, **coded via `task:t049`** (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`).
The corpus anchor is `evidence-line:0047` (`paper:Stein2025`) — repeated **immunoadsorption** in β2-AR-AB-
elevated post-COVID ME/CFS (n=20): 70% responders, COMPASS-31 autonomic improvement sustained to 6 months.
**Proof-of-concept only:** uncontrolled (no sham; the RituxME open-label→RCT-null precedent), β2-AR
depletion did *not* predict response, and the endpoints are symptomatic/autonomic rather than a measured
small-fiber-lesion (IENFD/SGNFD) trajectory — so the **structural** claim this route underwrites is left
untouched.

## Caveats

`identification_strength: observational` — open-label/uncontrolled immunomodulation studies are heavily
exposed to **placebo, regression-to-the-mean, and selection** effects, and autoantibody-selected cohorts
risk confirming the premise by construction. The decisive design is a **randomized, sham-controlled trial
in a seropositive subset with a pre-specified lesion endpoint** (autonomic measures + IENFD/SGNFD), not
symptom scales alone. A positive symptomatic response without a lesion-trajectory change would support
immune mediation of *symptoms* but leave the **structural** lesion claim (P1/P2) untouched. Conversely, a
null here weakens both `proposition:0016` and `proposition:0018`.

## Measurement Model

Exposure = a defined autoantibody-lowering intervention with measured pre/post autoantibody titers;
outcome = **change in autonomic-function measures (e.g. COMPASS-31, QSART, tilt-table indices) and, where
biopsied, IENFD/SGNFD trajectory**, contrasted against a control/sham arm. The autoantibody-titer drop is
the mechanistic mediator linking this route to `proposition:0018`; the lesion-trajectory endpoint is what
ties it back to the structural claims P1/P2.
