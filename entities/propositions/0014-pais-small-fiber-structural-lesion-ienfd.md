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
source_refs: []
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: PAIS autonomic patients have an objective small-fiber structural lesion (reduced IENFD)

## Claim

In a substantial subset of post-acute-infection-syndrome (PAIS) patients with autonomic symptoms,
**objectively reduced intraepidermal nerve-fiber density (IENFD) or autonomic small-fiber loss** is
present on standardized skin biopsy / autonomic testing. Subject = PAIS patients with autonomic
symptoms; predicate = *exhibit*; object = a measurable peripheral small-fiber structural deficit. This
is a `structural_claim` about the **existence of an end-organ lesion** — a real reduction in fiber
density, not merely a functional or self-reported state. It is P1 of
`hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` and the existence claim on which
P2 (`proposition:0015`, the lesion's distribution) and P3 (`proposition:0016`, its causation) depend.

## Evidence Summary

`literature_evidence`, **not yet coded as project evidence-lines** (ingestion is `task:t049`). The
empirical seed is skin-biopsy small-fiber neuropathy (SFN) reported in long COVID and ME/CFS and
small-fiber/autonomic involvement described in PTLDS — e.g. Oaklander et al. 2022 (*Neurol
Neuroimmunol Neuroinflamm* 9(3):e1146) found SFN the most common abnormality on systematic peripheral-
neuropathy evaluation of prolonged long COVID. Because none of these reports are yet deposited as
graph evidence-lines, the proposition currently has **thin coded support**; its support/dispute counts
should be read as provisional until `task:t049` lands.

## Caveats

Reported SFN prevalence in long COVID and ME/CFS varies widely by biopsy protocol and case definition —
a `topic:measurement-ascertainment-artifacts-in-pais` concern: a fraction of the signal may be protocol-
or ascertainment-driven rather than a fixed lesion. The competing deflationary/deconditioning account
(`question:0017-deflationary-alternatives-vs-shared-pathophysiology`) holds that autonomic symptoms can
arise without a fixed peripheral lesion. The claim is deliberately bounded to *a substantial subset*,
not all PAIS autonomic patients, and says nothing yet about the lesion's distribution (P2) or cause (P3).

## Measurement Model

The lesion is operationalized as **IENFD on standardized distal (and, for P2, proximal) skin biopsy**
per established normative cutoffs, supplemented by **QSART** and an **autonomic reflex screen** for the
autonomic small-fiber compartment. IENFD is treated as a *direct* structural readout of small-fiber
density (hence `proxy_directness: direct`); the inferential gap is not measurement-to-construct but
lesion-to-symptom causation, which P3 carries.
