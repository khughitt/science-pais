---
id: proposition:0014-pais-small-fiber-structural-lesion-ienfd
kind: proposition
title: PAIS autonomic patients have an objective small-fiber structural lesion (reduced
  IENFD)
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
- proposition:0015-pais-sfn-non-length-dependent-pattern
- task:t049
source_refs:
- paper:Oaklander2022
- paper:Joseph2021
- paper:Walitt2024
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: PAIS autonomic patients have an objective small-fiber structural lesion (reduced IENFD)

## Claim

In a substantial subset of post-acute-infection-syndrome (PAIS) patients with autonomic symptoms, a
**peripheral small-fiber structural lesion** is objectively present — measured *directly* as reduced
**intraepidermal nerve-fiber density (IENFD)** and/or reduced **sweat-gland nerve-fiber density
(SGNFD)** on standardized skin biopsy. Subject = PAIS patients with autonomic symptoms; predicate =
*exhibit*; object = a measurable reduction in cutaneous small-fiber density. This is a `structural_claim`
about the **existence of an end-organ lesion** — a real reduction in fiber density, not merely a
functional or self-reported state. Functional autonomic testing (QSART, autonomic reflex screen)
**corroborates** that the affected compartment is small-fiber/autonomic but is *not* itself a structural
measurement of the lesion (see Measurement Model). It is P1 of
`hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` and the existence claim on which
P2 (`proposition:0015`, the lesion's distribution) and P3 (`proposition:0016`, its causation) depend.

## Evidence Summary

`literature_evidence`, **coded via `task:t049`** (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`).
P1 is now supported across triggers, with one rigorous null:
- **Support:** `evidence-line:0038` (`paper:Oaklander2022` — long COVID, paired distal+proximal biopsy,
  62.5% distal IENFD abnormal) and `evidence-line:0039` (`paper:Joseph2021` — ME/CFS, 31% SFN, n=160,
  distal-only; the largest series).
- **Dispute:** `evidence-line:0040` (`paper:Walitt2024` — rigorously adjudicated NIH PI-ME/CFS, *no*
  small-fiber-density difference; n=17).
Additional context (post-vaccine PASC 90% reduced density; the PTLDS series 10/10) is summarized in
`interpretation:0009`. Net: **documented but prevalence is protocol- and cohort-sensitive**, not
established universal.

## Caveats

Reported SFN prevalence in long COVID and ME/CFS varies widely by biopsy protocol and case definition —
a `topic:measurement-ascertainment-artifacts-in-pais` concern: a fraction of the signal may be protocol-
or ascertainment-driven rather than a fixed lesion. The competing deflationary/deconditioning account
(`question:0017-deflationary-alternatives-vs-shared-pathophysiology`) holds that autonomic symptoms can
arise without a fixed peripheral lesion. The claim is deliberately bounded to *a substantial subset*,
not all PAIS autonomic patients, and says nothing yet about the lesion's distribution (P2) or cause (P3).

## Measurement Model

Two tiers, kept distinct:

- **Direct structural readouts** (load-bearing for this `structural_claim`): **IENFD** on standardized
  distal (and, for P2, proximal) skin biopsy and **SGNFD** on the autonomic (sudomotor) compartment, each
  read against established site-specific normative cutoffs. These directly index small-fiber density,
  hence `proxy_directness: direct`.
- **Functional corroboration** (objective but *not* structural): **QSART** and the **autonomic reflex
  screen** demonstrate small-fiber/autonomic *dysfunction* and localize the affected compartment, but do
  not measure fiber density and so cannot by themselves establish a structural lesion. They raise or
  lower confidence in the structural claim without being part of its truth conditions.

The inferential gap for P1 is therefore *not* measurement-to-construct (IENFD/SGNFD are direct); it is
lesion-to-symptom causation, which P3 (`proposition:0016`) carries.
