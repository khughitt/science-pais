---
id: proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring
type: proposition
title: Cross-study heterogeneity in PAIS prevalence and effect estimates is substantially
  explained by ascertainment and scoring choices rather than biology
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
- interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- topic:measurement-ascertainment-artifacts-in-pais
source_refs:
- paper:Novak2026
- paper:Shah2025
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Cross-study heterogeneity in PAIS prevalence and effect estimates is substantially explained by ascertainment and scoring choices rather than biology

## Claim

Subject = the cross-study heterogeneity in a PAIS phenotype's prevalence or effect estimate; predicate =
*is substantially explained by*; object = ascertainment and scoring choices — **case definition**,
**referral/selection enrichment**, and **endpoint/scoring breadth** — rather than by between-study
biological differences. This is the **M2 core proposition** of
`hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent`, an
`empirical_regularity` over the corpus. Its sharp, falsifiable form: **harmonizing** case definition +
scoring breadth + referral stream across studies of one phenotype **collapses** apparent cross-study
heterogeneity. It is distinct from M1 (`proposition:0027`): M2 concerns *between-study scatter* and can
apply even to **objectively-measured** phenotypes (an objective measurement is not automatically
ascertainment-clean).

## Evidence Summary

`literature_evidence`, aggregated by the `task:t055` audit
(`interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences`), in which the
**weak-ascertainment cut collapsed or attenuated 3/3**:

- **`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`** (the decisive instance, via
  `proposition:0014`) — an apparent **0%→91%** skin-biopsy SFN prevalence range across Oaklander2022 /
  Joseph2021 / Walitt2024 / Novak2026 decomposes into **modality breadth** (sensory ENFD → +sweat-gland
  SGNFD → +functional ESC, a >40-point swing on *identical* Novak2026 patients), **trigger** (LC > ME/CFS),
  and **cohort referral-enrichment**; within-trigger the referral cohorts are in fact concordant. The
  percentile-cutoff rule (QASAT vs ≤5th-percentile) was a *minor* driver.
- **`proposition:0001`** (reproductive-stage threshold) — the menopause-specific long-COVID signal
  attenuates to null **within age band** (Shah2025: menopausal RR 1.42 ≈ non-menopausal 1.45), a
  case-ascertainment/confounder-control instance.

The case-definition variants of this regularity are the open questions `question:0014` (which PAIS case
definition is most biologically coherent) and `question:0015` (does a PEM requirement improve cross-study
comparability). The HRT-evidence audit
(`interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test`) is an M2-adjacent instance that
reclassified an entire literature as ascertainment context.

## Caveats

**Collapse of heterogeneity ≠ absence of biology.** Where ascertainment is harmonized, a *residual real
signal can survive* — the SFN lesion-positive subset persists in referral cohorts under every metric
(`proposition:0014` is not weakened by M2; only its cross-study *magnitude/generality* is shown to be
ascertainment-sensitive). The regularity is `observational` and rests on a small number of worked cases
plus the single aggregating audit (`interpretation:0015`); belief should stay fragile until additional
phenotypes are harmonized. M2 is the mechanism by which an objective measurement (e.g. a biopsy count)
can still produce heterogeneous group estimates — so it bounds, rather than contradicts, the existence of
objective lesions.
