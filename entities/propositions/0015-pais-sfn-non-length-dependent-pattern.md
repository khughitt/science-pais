---
id: proposition:0015-pais-sfn-non-length-dependent-pattern
type: proposition
title: The PAIS small-fiber lesion is disproportionately non-length-dependent
status: active
claim_layer: structural_claim
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- question:0004-convergent-small-fiber-neuropathy-substrate
- topic:measurement-ascertainment-artifacts-in-pais
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0016-pais-sfn-autoimmune-causation
- task:t049
source_refs:
- paper:Limongelli2026
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: The PAIS small-fiber lesion is disproportionately non-length-dependent

## Claim

Where the PAIS small-fiber lesion (`proposition:0014`) is present, its anatomical distribution is
disproportionately **non-length-dependent** — *proximal* small-fiber abnormality disproportionate to
*distal* abnormality, after adjusting for the fact that raw fiber density differs by body site —
rather than the distal-predominant length-dependent gradient typical of metabolic/idiopathic SFN.
Subject = the PAIS small-fiber lesion; predicate = *follows*; object = a non-length-dependent spatial
distribution. This is a `structural_claim` about **lesion pattern**, and
it is the discriminating leg of `hypothesis:0007`: a non-length-dependent pattern implicates a
**ganglionopathy / immune-mediated mechanism** (dorsal-root- or autonomic-ganglion cell-body targeting)
and is what would distinguish this substrate from primary/metabolic SFN. It thereby motivates the
autoimmune-causation claim P3 (`proposition:0016`).

## Evidence Summary

`literature_evidence`, **not yet deposited as graph evidence-lines** (`task:t049`). The discriminating
methodology is established: **norm-referenced proximal vs distal IENFD** on paired skin biopsy
distinguishes length-dependent neuropathy from non-length-dependent ganglionopathy, so the claim is
*operationally testable* wherever proximal-plus-distal sampling is performed. `paper:Limongelli2026`
supplies a corpus-resident SFN skin-biopsy anchor in post-acute SARS-CoV-2 syndrome, but it is cited as
a **P1-level lesion anchor that does not by itself settle the distribution question** (it is not a
paired-site distribution study). Whether PAIS cohorts actually show the non-length-dependent pattern at
elevated rates is **not yet established in the corpus** — most studies sample distal sites only and
cannot address it. Coded support is currently absent pending ingestion.

## Caveats

This is the most measurement-fragile leg: the non-length-dependent claim **requires proximal-plus-distal
sampling that many SFN studies omit**, so apparent length-dependence in the literature may be a sampling
artifact rather than true distribution (`topic:measurement-ascertainment-artifacts-in-pais`). If, under
standardized paired-site biopsy, the lesion proves **length-dependent and indistinguishable from
metabolic/idiopathic SFN**, this proposition fails and the "distinct ganglionopathy" reading of
`hypothesis:0007` collapses. Conditional on P1 (`proposition:0014`): if no lesion exists, the
distribution question is moot.

## Measurement Model

Operationalized from paired skin biopsies (e.g. distal leg vs proximal thigh/trunk) scored against
**site-specific normative distributions**: each site's IENFD (and SGNFD) is converted to a z-score or
percentile relative to that site's normal range, and the pattern counts as **non-length-dependent** when
**proximal abnormality is disproportionate to distal abnormality** (e.g. proximal z-deficit ≥ distal
z-deficit, or proximal-but-not-distal abnormality). A raw proximal:distal density ratio is *not* used,
because absolute IENFD differs by site and a raw ratio would conflate normal anatomy with pathology.
Direct structural readout (`proxy_directness: direct`); the load-bearing requirement is *protocol*
(paired-site sampling with site-specific norms), not proxy interpretation.
