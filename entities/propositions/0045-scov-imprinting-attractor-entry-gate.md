---
id: proposition:0045-scov-imprinting-attractor-entry-gate
kind: proposition
title: Seasonal-coronavirus immune imprinting acts as an attractor-entry gate via
  impaired SARS-CoV-2 clearance
status: active
claim_layer: mechanistic_narrative
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0001-shared-dysregulated-attractor
related:
- hypothesis:0001-shared-dysregulated-attractor
source_refs:
- paper:Mak2025
- paper:Crotty2026
created: '2026-07-10'
updated: '2026-07-10'
---
# Proposition: Seasonal-coronavirus immune imprinting acts as an attractor-entry gate via impaired SARS-CoV-2 clearance

## Claim

Prior immune imprinting by the homologous seasonal betacoronaviruses HKU1/OC43 acts as a **mechanistically-specified attractor-entry gate** for `hypothesis:0001`: OC43/HKU1-imprinted B-cell memory outcompetes naive SARS-CoV-2 S1-specific B cells (original antigenic sin), deflecting the humoral response toward conserved, suboptimal epitopes, impairing SARS-CoV-2 clearance, prolonging antigen exposure, and thereby lowering the threshold for entry into the shared dysregulated attractor. It yields a testable predictor: pre-COVID HKU1/OC43 serology should predict PAIS risk.

## Evidence Summary

`paper:Mak2025` (47 long-COVID vs. 41 healthy controls) is the direct PAIS instance of original antigenic sin: LC patients have *reduced* SARS-CoV-2 S1-specific IgG/IgA but *elevated* IgG against homologous seasonal betacoronaviruses HKU1/OC43, plus an elevated IgM/IgG ratio (impaired class switching) — a response deflected toward conserved, suboptimal epitopes. `paper:Crotty2026` (2026 immunological-memory review) supplies the mechanistic ceiling and durability premise: the pertussis wP-vs-aP example shows infant priming fixes CD4 T-helper phenotype for decades despite boosters — a human demonstration that early priming sets a durable, correction-resistant immune set point — and it establishes that tissue-resident memory requires local antigen encounter (so imprinting shapes response *quality* long after priming).

## Caveats

Mak2025's central confound is a blood-draw timing mismatch (LC sampled at median 280 days vs. HC at 596 days), across which variant exposure and antibody waning differ; the imprinting signal is inferential (antibody ELISAs, no B-cell clonotyping) and cross-sectional, so it **cannot establish that imprinting preceded LC** rather than being shaped by it — the direction of the entry-gate arrow is unproven. Crotty2026 is vaccine-centric and does *not* study how PAIS alters memory; its relevance is analogical, not measured. The claim's identifying prediction (pre-COVID HKU1/OC43 serology → PAIS) has not been tested (`question:0071`). Identification is therefore `observational`.

## Measurement Model

"Imprinting" is a latent B-cell-repertoire property operationalized here **indirectly** through serum antibody ELISAs (S1-specific vs. HKU1/OC43-cross-reactive IgG/IgA titers and the IgM/IgG ratio), not through the direct readout (BCR clonotyping / affinity mapping showing recall of seasonal-coronavirus clones against SARS-CoV-2 antigen). Cross-sectional post-infection titers conflate three sources — pre-existing imprint, waning, and post-infection boosting — so elevated HKU1/OC43 IgG in LC is consistent with, but not diagnostic of, an entry-gating imprint. The discriminating measurement is **pre-infection** seasonal-coronavirus serology (or banked pre-COVID samples) linked to prospective PAIS outcome, ideally with clonotyping to show suboptimal-epitope recall; only that design converts this proxy-based mechanistic narrative into a directional causal test.
