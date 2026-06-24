---
id: evidence-line:0067-t055-audit-m2-sfn-harmonization-supports
type: evidence-line
title: "t055 audit: SFN-prevalence cross-study heterogeneity decomposes into modality/trigger/referral (interp:0014) — supports M2"
status: active
stance: supports
target: proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring
source: paper:Novak2026
strength: moderate
independence: independent
independence_group: ''
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring
- interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
- interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
source_refs:
- paper:Novak2026
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: t055 audit — SFN-prevalence cross-study heterogeneity decomposes into modality/trigger/referral, supports M2

## What this line shows

The decisive **M2 instance** carried by the `task:t055` audit
(`interpretation:0015`), itself resting on the metric-harmonization re-analysis
(`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`). An apparent **0%→91%** skin-biopsy
SFN prevalence range across Oaklander2022 / Joseph2021 / Walitt2024 / Novak2026 decomposes into
**modality breadth** (on *identical* Novak2026 patients, sensory ENFD 48% → +sweat-gland SGNFD 67% →
+functional ESC 91% — a >40-point swing from scoring choice alone), **trigger** (LC > ME/CFS), and
**cohort referral-enrichment**; within-trigger the referral cohorts are concordant, and the percentile-
cutoff rule (QASAT vs ≤5th-percentile) was only a minor driver. This directly tests and supports M2
(`proposition:0028`): cross-study heterogeneity is substantially an ascertainment/scoring artifact.

This single line carries the audit's **whole M2 cut** (two retrospective instances), anchored to its
strongest case (Novak2026):
- **SFN scoring/referral** (above) — the within-subject 48→67→91% swing + cross-study referral
  decomposition, via `interpretation:0014`.
- **Reproductive-stage ascertainment** — Shah2025's menopause-specific long-COVID signal **attenuates to
  null within age band** (menopausal RR 1.42 ≈ non-menopausal 1.45), the audit's coding of
  `proposition:0001`: a second ascertainment-control instance from a distinct cohort/design.

## Why it is independent

`independent` as a cohort (Novak2026), but recorded as **one line, not two**: both M2 instances reach the
regularity only through the **single `task:t055` retrospective audit**, so they are inputs to one
aggregating analysis rather than two independent prospective tests of M2. One line keeps M2's belief
**fragile** and consistent with M1 (`evidence-line:0066`) and M3 (`evidence-line:0069`), each likewise a
single audit-cut line.

## Caveats / scope

`direct_test`, **moderate** — **collapse of heterogeneity ≠ absence of biology**: a residual SFN
lesion-positive subset survives in referral cohorts under every metric, so M2 bounds the *magnitude/
generality* of `proposition:0014` without negating the lesion's existence. Referral bias and the QASAT
metric apply (per `evidence-line:0063`). The line is an analytic re-reading of published methods-vs-rates,
not a new prospective harmonization, so it remains literature-grade. The Shah2025 instance attenuates only
the *menopause-specific* reading (an age/immunosenescence threshold stays live).
