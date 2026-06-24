---
id: proposition:0014-pais-small-fiber-structural-lesion-ienfd
type: proposition
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
- paper:Limongelli2026
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

`literature_evidence`, **not yet deposited as graph evidence-lines** (ingestion is `task:t049`). Corpus-
resident summaries already lean toward P1: `paper:Limongelli2026` reports skin-biopsy small-fiber
neuropathy with immune correlates in post-acute SARS-CoV-2 syndrome, and `paper:Walitt2024` deep-
phenotyped post-infectious ME/CFS including autonomic/small-fiber assessment. The broader empirical seed
includes SFN reported in long COVID and ME/CFS and small-fiber/autonomic involvement in PTLDS — e.g.
Oaklander et al. 2022 (*Neurol Neuroimmunol Neuroinflamm* 9(3):e1146; not yet a corpus paper entity). The
listed `source_refs` are summaries the claim leans on, not yet structured support/dispute edges, so coded
support remains **thin and provisional until `task:t049` lands**.

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
