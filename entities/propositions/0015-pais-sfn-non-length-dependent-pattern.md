---
id: proposition:0015-pais-sfn-non-length-dependent-pattern
type: proposition
title: The PAIS small-fiber lesion is disproportionately non-length-dependent
status: active
claim_layer: structural_claim
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: paired proximal and distal intraepidermal nerve fiber density, scored against site-specific normative reference distributions
  latent_construct: non-length-dependent small-fiber structural involvement in PAIS
  measurement_relation: paired-site IENFD is treated as a direct structural readout; the NLD classifier uses site-specific z-score deficit comparison rather than a raw proximal:distal ratio
  known_failure_modes:
  - distal-only sampling is structurally blind to NLD patterning
  - site-specific normative datasets and biopsy-processing protocols can shift absolute abnormality rates
  - modality expansion beyond sensory ENFD changes prevalence and must not be conflated with this pattern claim
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
updated: '2026-06-25'
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

`literature_evidence`, **coded via `task:t049`** (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`).
The discriminating methodology is established (norm-referenced proximal vs distal IENFD on paired biopsy),
but P2 is **thinly documented**: the only clean paired-site non-length-dependent fraction is
`evidence-line:0041` (`paper:Limongelli2026` — 33% NLD on paired calf+thigh, **but post-*vaccine***);
`evidence-line:0042` (`paper:Oaklander2022`) adds weak, non-independent support via distal≈proximal
near-parity *without* a per-patient NLD classification. The largest study (`paper:Joseph2021`) was
distal-only and **cannot assess P2**. The non-length-dependent pattern is therefore **asserted more than
measured** — the least-supported leg, and the central methodological gap behind `question:0004`.

## Caveats

This is the most measurement-fragile leg: the non-length-dependent claim **requires proximal-plus-distal
sampling that many SFN studies omit**, so apparent length-dependence in the literature may be a sampling
artifact rather than true distribution (`topic:measurement-ascertainment-artifacts-in-pais`). If, under
standardized paired-site biopsy, the lesion proves **length-dependent and indistinguishable from
metabolic/idiopathic SFN**, this proposition fails and the "distinct ganglionopathy" reading of
`hypothesis:0007` collapses. Conditional on P1 (`proposition:0014`): if no lesion exists, the
distribution question is moot.

**Now formally contested as a measurement artifact (2026-06-25).** The h0008-M2 scope-criticism is wired
as `evidence-line:0071` (`dispute_scope: generalization`, weak): the NLD pattern is **only assessable under
paired-site sampling**, so its visibility is a protocol choice. The largest cohort (Joseph2021,
distal-only) is structurally blind to it; where assessed the support is off-target (Limongelli2026
post-*vaccine*) or group-level (Oaklander2022, Novak2026), so the **well_supported** grade overstates what
paired-site, per-subject, post-infectious measurement has shown. This is the same modality/scoring-breadth
mechanism as the SFN-prevalence 0%→91% swing in `interpretation:0014` (M2's flagship instance), applied to
spatial *pattern* [@Novak2026]. `pre-registration:0003` is the formal h0007/P2 adjudicator for this proposition.

## Measurement Model

Operationalized from paired skin biopsies (e.g. distal leg vs proximal thigh/trunk) scored against
**site-specific normative distributions**: each site's IENFD (and SGNFD) is converted to a z-score or
percentile relative to that site's normal range, and the pattern counts as **non-length-dependent** when
**proximal abnormality is disproportionate to distal abnormality** (e.g. proximal z-deficit ≥ distal
z-deficit, or proximal-but-not-distal abnormality). A raw proximal:distal density ratio is *not* used,
because absolute IENFD differs by site and a raw ratio would conflate normal anatomy with pathology.
Direct structural readout (`proxy_directness: direct`); the load-bearing requirement is *protocol*
(paired-site sampling with site-specific norms), not proxy interpretation.
