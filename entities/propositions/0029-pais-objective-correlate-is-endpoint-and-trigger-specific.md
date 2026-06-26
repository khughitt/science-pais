---
id: proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
type: proposition
title: A PAIS phenotype's objective correlate is endpoint- and trigger-specific, so
  endpoint choice can manufacture or hide an apparent shared mechanism
status: active
claim_layer: structural_claim
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- topic:measurement-ascertainment-artifacts-in-pais
- proposition:0017-pais-sfn-cross-trigger-convergence
- proposition:0015-pais-sfn-non-length-dependent-pattern
- evidence-line:0070-novak2026-standardized-protocol-scope-criticism-disputes-0017
- evidence-line:0071-joseph2021-distal-only-sampling-scope-criticism-disputes-0015
- proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality
- interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion
- evidence-line:0076-mecfs-muscle-endpoint-data-disputes-clean-pem-endpoint-dichotomy
- evidence-line:0077-bizjak2024-cross-trigger-muscle-biopsy-disputes-simple-same-lesion-reading
- discussion:0004-pem-shared-muscle-lesion-vs-endpoint-contingency
- task:t056
- task:t058
- pre-registration:0005-harmonized-provoked-muscle-endpoint
source_refs:
- paper:Appelman2024
created: '2026-06-24'
updated: '2026-06-26'
---
# Proposition: A PAIS phenotype's objective correlate is endpoint- and trigger-specific, so endpoint choice can manufacture or hide an apparent shared mechanism

## Claim

Subject = the objective correlate of a named PAIS phenotype (e.g. post-exertional malaise); predicate =
*is contingent on*; object = the specific objective **endpoint** and **trigger** chosen to measure it —
such that the *choice* of endpoint can itself **manufacture or hide** an apparent cross-trigger shared
mechanism. This is the **M3 core proposition** of
`hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent`. It is a
`structural_claim` about how endpoint selection interacts with cross-trigger inference, distinct from M1
(self-report→objective attenuation) and M2 (between-study ascertainment scatter): M3 says that **even
among objective endpoints**, picking one can decide whether triggers look the same or different.

## Evidence Summary

`literature_evidence`. **M3 currently rests on a single clean instance** and is the least-supported of the
three core propositions:

- **`proposition:0011`** (via `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`)
  — the ME/CFS whole-body **two-day-CPET** PEM decrement does **not** transfer to long COVID at that
  endpoint, *even where a long-COVID muscle OXPHOS lesion exists* (Appelman2024). The "shared PEM
  mechanism" therefore appears or disappears depending on whether the chosen objective endpoint is
  two-day CPET or muscle bioenergetics — the defining M3 pattern.

- **t056 narrowed the PEM instance rather than resolving it** (`interpretation:0019`,
  `proposition:0030`). ME/CFS already has muscle-endpoint bioenergetic abnormalities (31P-MRS acidosis
  recovery, contraction-stimulated muscle-cell signaling, resting biopsy mitochondrial abnormalities).
  That means M3's PEM example is not a clean "ME/CFS whole-body vs long-COVID muscle" split. It is a
  stronger endpoint-harmonization warning: heterogeneous muscle endpoints can make the same triggers look
  either convergent or divergent, and the Appelman-type cross-trigger biopsy time-course still has not
  been run.

The `task:t055` audit (`interpretation:0015`) coded this claim `ENDPOINT-CONTINGENT` and noted it is the
*only* determinate M3 instance in the corpus; it is also an objective-origin claim that is nonetheless
artifact-consistent, which is why the audit rejected a clean "objective ⇒ survives" rule.

## Caveats

**Single-instance / fragile.** Unlike M1 (`proposition:0027`, 4 supporting instances) and M2
(`proposition:0028`, 2+ instances), M3 is asserted on **one phenotype (PEM)**. It is a genuine structural
pattern but is **not yet a regularity** — a second independent instance (a different PAIS phenotype whose
cross-trigger sameness flips with endpoint choice) is needed before belief should rise above
fragile/speculative.

**SFN is now wired as M3's second-phenotype reach (2026-06-25) — a criticism edge, not yet a confirmed
instance.** M3's bearing on the SFN substrate is formalized as `evidence-line:0070` (disputing the
standardized-substrate reading of `proposition:0017`, the cross-trigger-convergence claim), with the
M2-flavored sampling-artifact companion `evidence-line:0071` (disputing `proposition:0015`, the
non-length-dependent pattern). These make M3's challenge to the SFN legs belief-bearing (both props are now
`contested`), but they **do not add support to M3 itself**: a *confirmed* second instance requires a
standardized cross-trigger paired-site biopsy to actually reveal that SFN cross-trigger sameness flips with
protocol. `pre-registration:0003` is the standing h0007/q0004 vehicle for that design class; it is
scientifically adjacent to h0008-M3 but not a formal h0008 `commits_to` target. Until such a vehicle runs,
M3 stays **single-instance / fragile**, now with its reach explicitly spanning two phenotypes (PEM via
`proposition:0011`; SFN via the `0070`/`0071` criticism edges) rather than one. The structural parallel —
h0008 as the systematic adversary of both peripheral-substrate candidates (h0006 PEM, h0007 SFN), each
adjudicated by the same class of standardized cross-trigger study — is laid out in `discussion:0004`.
Conditional scope: M3 governs cross-trigger
*sameness* inferences, not single-cohort case-vs-control claims.

**t056 caveat (2026-06-25).** The PEM instance is now more nuanced than the original audit statement:
ME/CFS muscle-endpoint data exist, but are not endpoint-equivalent to Appelman2024. This does not add a
new independent M3 support line, because it is the same PEM phenotype and still lacks a harmonized
cross-trigger protocol. It does make the M3 claim more precise: endpoint choice can **hide possible
convergence** as well as manufacture apparent divergence.

**t058 pre-registration (2026-06-26).** `pre-registration:0005` now commits the prospective adjudication
rule for this PEM instance: a harmonized LC+ME/CFS provoked muscle-endpoint protocol. Same-lesion
convergence would weaken M3 for PEM; trigger- or endpoint-specific results would strengthen it. Until a
vehicle clears the gates, this remains data-gated and no belief update is made.
