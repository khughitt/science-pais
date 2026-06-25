---
id: evidence-line:0071-joseph2021-distal-only-sampling-scope-criticism-disputes-0015
type: evidence-line
title: "M2 scope-criticism: the non-length-dependent pattern is only detectable under paired-site sampling; the largest cohort (Joseph2021) is distal-only and structurally cannot see it — disputes the measured-status of prop:0015"
status: active
stance: disputes
target: proposition:0015-pais-sfn-non-length-dependent-pattern
source: paper:Joseph2021
strength: weak
dispute_scope: generalization
independence: shared-source
independence_group: joseph2021-mecfs-icpet-sfn
evidence_role: model_criticism
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0015-pais-sfn-non-length-dependent-pattern
- proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring
- proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
- interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
- pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls
- question:0004-convergent-small-fiber-neuropathy-substrate
source_refs:
- paper:Joseph2021
created: '2026-06-25'
updated: '2026-06-25'
---
# Evidence Line: M2 scope-criticism — the non-length-dependent pattern is a sampling-protocol artifact risk

## What this line shows

This is the **h0008-M2 (`proposition:0028`) scope-criticism edge** that `proposition:0015`'s belief surface
was missing. `proposition:0015` (the non-length-dependent, NLD, pattern — the *discriminating* leg of
h0007) is graded **well_supported**, but its own prose calls it "asserted more than measured… the
least-supported leg," and the t055 audit (`interpretation:0015`) coded it **UNTESTED**. The reason is a
textbook M2 scoring-breadth problem: **the NLD pattern is only assessable when the biopsy protocol samples
proximal *and* distal sites**, so whether the pattern is *visible at all* is decided by protocol choice,
not biology.

- **The largest cohort cannot see it.** Joseph2021 (n=160, the largest ME/CFS skin-biopsy series) is
  **distal-only** (single lower-leg site) and therefore **structurally cannot assess length-dependence** —
  it contributes to the lesion-existence claim (`proposition:0014`) but is *blind* to P2 by design.
- **Where assessed, support is thin and protocol-heterogeneous.** The only clean per-patient NLD fraction
  is Limongelli2026 (33% NLD — but **post-vaccine**, not post-infectious); Oaklander2022 gives weak
  distal≈proximal near-parity with **no per-patient NLD classification**; Novak2026 gives only **group-level**
  proximal-not-lesser SGNFD, again not per-subject. So the well_supported grade aggregates one
  moderate-but-off-target line and two weak group-level lines into a claim the underlying studies do not
  individually license.

This is the M2 artifact in its purest form — the same modality/scoring-breadth mechanism that drove the
SFN-prevalence 0%→91% swing in `interpretation:0014` (M2's flagship instance), now applied to the *spatial
pattern* rather than the prevalence. Apparent length-dependence (or its absence) in the SFN literature may
be a **sampling artifact** rather than a measured distribution.

## Why it is independent

**Not independent.** `independence: shared-source`, `independence_group: joseph2021-mecfs-icpet-sfn` — it
is a methodological re-reading of the same Joseph2021 design that anchors the supporting lines for
`proposition:0014`/`0017`, used here to make the structural point that a distal-only protocol is blind to
P2. The criticism is a fact about sampling design, not a new cohort.

## Caveats / scope

`dispute_scope: generalization`, **weak.** This does **not** claim the lesion is length-dependent — that is the
*open* question. It disputes only the **measured-status** of `proposition:0015`: the NLD pattern is
currently asserted on protocol-heterogeneous, mostly group-level or off-target (post-vaccine) data, so its
well_supported grade overstates what paired-site, per-subject, post-infectious measurement has actually
shown. The decisive test is the data-gated `pre-registration:0003` (standardized paired-site IENFD/SGNFD
with site-specific norms and a primary-dysautonomia control arm). If, under that protocol, the lesion
proves length-dependent and indistinguishable from metabolic/idiopathic SFN, `proposition:0015` fails and
the "distinct ganglionopathy" reading of h0007 collapses; if the NLD pattern survives, it is confirmed as
measured rather than asserted.
