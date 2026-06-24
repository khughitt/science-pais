---
id: proposition:0027-pais-group-differences-attenuate-under-objective-re-measurement
type: proposition
title: Apparent PAIS group differences attenuate toward null or reverse under objective
  trigger-matched re-measurement (channel-direction regularity)
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
- proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- proposition:0008-female-excess-concentrates-in-post-acute-persistence
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- topic:measurement-ascertainment-artifacts-in-pais
source_refs:
- paper:Walitt2024
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Apparent PAIS group differences attenuate toward null or reverse under objective trigger-matched re-measurement (channel-direction regularity)

## Claim

Subject = an apparent PAIS group difference (sex, trigger, case-vs-control, or reproductive-stage)
**established in a self-report or mixed-ascertainment channel**; predicate = *attenuates toward null or
reverses under*; object = objective, trigger-matched, ascertainment-controlled re-measurement of the
**same construct**. This is the **M1 core proposition** of
`hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` —
an `empirical_regularity` over the project's own corpus of group-difference findings, not a claim about
PAIS pathophysiology. It asserts a **directional regularity** (self-report inflates; objective
re-measurement deflates or flips), and it is deliberately scoped to differences *whose establishing
channel is self-report or mixed* — it does **not** claim the objective channel is itself clean (that is
the province of M2 `proposition:0028` and M3 `proposition:0029`, which show objective-origin claims can
still be ascertainment-inflated or endpoint-contingent).

## Evidence Summary

`literature_evidence`, carried by `evidence-line:0066` and aggregated by the `task:t055` audit
(`interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences`). In that audit the
**self-report-/mixed-origin cut attenuated or decomposed 4/4** (all four instances, no survivors):

- **`proposition:0010`** (cognition) — the cleanest and only *same-cohort* instance: Walitt2024 reports
  increased subjective cognitive complaints across five domains with **no** group difference on 15
  objective neuropsychological tests, in one cohort.
- **`proposition:0009`** (dysautonomia) — the apparent PAIS-amplified female skew dissolves once the
  baseline ~5:1 POTS sex ratio is netted out (baseline-carried, not PAIS-amplified).
- **`proposition:0001`** (reproductive-stage threshold) — the menopause-specific long-COVID signal
  attenuates to null **within age band** (Shah2025: menopausal RR 1.42 ≈ non-menopausal 1.45). *This is
  the fourth row of the 4/4 cut.*
- **`proposition:0008`** (the crude post-acute female excess) — does not survive as a *uniform* biological
  excess; under subphenotype decomposition it is channel-structured
  (`interpretation:0003-t018-subphenotype-sex-reproductive-stage`).

The direction-reversal limb of M1 is corroborated by the **mirror/bounding case** `proposition:0012` (the
*objective* vascular hard-endpoint signal runs male-biased, opposite to the self-report female excess) —
but, as a robust objective effect, that proposition is counted under the bounded-exception register B and
is **not** one of the 4/4 M1 instances above.

## Caveats

The support is **retrospective, project-internal, and small-n**; only the cognition instance
(`proposition:0010`) is a within-cohort objective re-measurement, while the others infer attenuation by
comparing *different* cohorts — itself an M2-type ascertainment confound this regularity is meant to
police. The regularity is therefore `observational` and currently rests on a **single aggregating audit**
(`interpretation:0015`), so its belief should remain fragile/speculative until a prospective same-cohort
re-measurement (h0008 promotion criterion #2, `pre-registration:0003`) is run. The claim is **bounded**:
genuine objective trigger-matched differences exist and survive (register B: `proposition:0012`,
`proposition:0013`, `proposition:0025`); M1 governs only the self-report-/mixed-origin subpopulation.
