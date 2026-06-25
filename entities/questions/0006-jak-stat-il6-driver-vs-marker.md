---
id: question:0006-jak-stat-il6-driver-vs-marker
type: question
title: Is persistent JAK-STAT/IL-6 signaling a proximal driver of post-acute chronicity
  (reversible by inhibition) or a downstream marker, and is the axis shared beyond
  SARS-CoV-2?
status: active
ontology_terms:
- JAK-STAT
- IL-6
- inflammation
- therapeutics
datasets: []
source_refs:
- cite:Aid2025
- cite:Ganesh2022
related:
- topic:long-covid-immune-dysregulation
- topic:therapeutics-and-clinical-trials
- hypothesis:0003-immune-exhaustion-feedback
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- pre-registration:0004-jak1-inhibitor-driver-vs-marker
- interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration
- interpretation:0016-t054-abrocitinib-trial-status-snapshot
- task:t054
created: '2026-06-11'
updated: '2026-06-25'
---

# Is persistent JAK-STAT/IL-6 signaling a proximal driver of post-acute chronicity (reversible by inhibition) or a downstream marker, and is the axis shared beyond SARS-CoV-2?

## Summary

Persistent JAK-STAT/IL-6 signaling is one of the most reproducible inflammatory signatures in long COVID (Aid2025; IL-6 elevated in 61% of PASC in Ganesh2022). This question asks whether that signaling is a *proximal driver* of post-acute chronicity — whose pharmacological inhibition resolves symptoms — or a downstream *marker* of an upstream lesion, and whether the axis is shared across PAIS beyond SARS-CoV-2.

## Why It Matters

- Decides whether JAK inhibitors / IL-6 blockade are a rational PAIS therapeutic class; a JAK1-inhibitor trial (NCT06597396) is the direct test for long COVID.
- If unanswered, anti-cytokine trials may target an epiphenomenon, and cross-PAIS therapeutic transfer (to ME/CFS, post-Q-fever) cannot be justified.

## Current Evidence

- Supporting: Aid2025 shows persistent JAK-STAT/IL-6/IFN/complement activation >180 days with no circulating virus and frames it as a failed negative-feedback loop and a therapeutic target; Ganesh2022 finds durable IL-6 elevation (often discordant with CRP/ESR). The persistent-activation state is now coded as `proposition:0025` (supported).
- Conflicting / gaps: causal direction is untested (driver vs marker) — this is the open core, coded as `proposition:0026` (untested, `speculative`); bulk assays cannot identify the cell source (Aid2025); no cross-PAIS pathway-level comparison exists, so generalizability beyond SARS-CoV-2 is unknown. **Ryan2022's IFN-I *suppression* no longer "complicates" the picture** — t047 (`interpretation:0012`) reconciled it as the *type-I antiviral-effector* arm of a dissociated IFN signature (vs Aid2025's persistent *type-II/inflammatory* arm), so it is not a contradiction.
- **Standing discriminating test REGISTERED (t047; screened t054):** `pre-registration:0004` (data-gated) commits the driver-vs-marker decision rule on the abrocitinib JAK1-inhibitor RCT **NCT06597396** — symptom + pathway co-suppression -> driver (upward on `proposition:0026`/h0003); pathway suppression without symptom benefit -> marker (disputing/falsifier). Registry snapshot 2026-06-25: trial `ACTIVE_NOT_RECRUITING`, primary completion 2026-03-27 actual, study completion 2026-09-30 estimated, `hasResults: false`; standing verdict remains `[?]` inconclusive-for-coverage. The public endpoint list includes hsCRP but not a JAK-STAT/IL-6 pathway score, so G2 target engagement must be checked in the eventual paper/supplement.

## Thoughts

- Best current interpretation: JAK-STAT/IL-6 is at minimum a robust state marker and a plausible proximal node; the feedback-failure framing (Aid2025) makes it a credible driver candidate, pending the inhibitor trial.
- Major uncertainty: which cell population sustains the signal, and whether inhibition reverses symptoms or merely suppresses a marker while the upstream lesion (antigen, autoimmunity) persists.

## Connections to Project

- Related hypotheses: `hypothesis:0003-immune-exhaustion-feedback`, `hypothesis:0001-shared-dysregulated-attractor`.
- Required data or analyses: results of JAK1-inhibitor RCT with symptom + pathway co-endpoints; single-cell profiling to localize the IL-6/JAK-STAT source; cross-PAIS pathway-activity comparison.
- Priority level: P1 — a near-term, directly testable driver-vs-marker question with a registered trial.

## Related

- Topic notes: `topic:long-covid-immune-dysregulation`, `topic:shared-failure-mode-across-pais`.
- Article notes: Aid2025, Ganesh2022, Ryan2022, Talla2023.
- Methods/Datasets: NCT06597396 (JAK1 inhibitor); Olink/SomaScan proteomic cohorts.
