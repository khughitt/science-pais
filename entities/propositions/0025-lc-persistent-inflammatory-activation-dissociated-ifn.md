---
id: proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
type: proposition
title: 'Long COVID exhibits persistent inflammatory pathway activation with a dissociated
  IFN signature: sustained IL-6/JAK-STAT/type-II-IFN/complement tone plus a blunted
  type-I antiviral-effector arm, alongside CD8 exhaustion, beyond 180d with no circulating
  virus'
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0003-immune-exhaustion-feedback
related:
- hypothesis:0003-immune-exhaustion-feedback
- question:0006-jak-stat-il6-driver-vs-marker
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis
- topic:long-covid-immune-dysregulation
- task:t047
- task:t060
source_refs:
- paper:Aid2025
- paper:Ryan2022
created: '2026-06-24'
updated: '2026-06-25'
---
# Proposition: Long COVID exhibits persistent inflammatory pathway activation with a dissociated IFN signature: sustained IL-6/JAK-STAT/type-II-IFN/complement tone plus a blunted type-I antiviral-effector arm, alongside CD8 exhaustion, beyond 180d with no circulating virus

## Claim

Long COVID's peripheral-immune state, beyond 180 days and with **no circulating virus**, is a
**persistent inflammatory activation** with a **dissociated interferon signature**: sustained
IL-6/JAK-STAT/type-II-IFN (IFNγ)/complement tone coexists with a **blunted type-I antiviral-effector
arm** (ISGs MX1/OAS3/OASL), against a backdrop of CD8+ T-cell exhaustion. Subject = the post-180-day LC
peripheral-immune state; predicate = *is characterized by*; object = persistent inflammatory/JAK-STAT
activation + dissociated (type-II up / type-I-effector down) IFN + CD8 exhaustion. This is the
**descriptive-state conjunct** of `hypothesis:0003` — the loop's *inflammatory arm as observed*. It is
deliberately *not* the causal-loop claim (that the activation and exhaustion are coupled and *drive*
chronicity), which is carried separately by `proposition:0026` and is untested [@Aid2025; @Ryan2022].

The IFN dissociation is the resolution of the **Aid2025-vs-Ryan2022 tension** that `hypothesis:0003`
flagged: the two findings are not contradictory because they index **different IFN arms, contrasts,
compartments, and timepoints** (`interpretation:0012`). A persistent inflammatory/type-II IFN tone with a
tolerized type-I antiviral-effector arm is the *predicted* signature of exhausted innate sensing under
chronic stimulation — so both papers **support** this proposition rather than disputing each other.

## Evidence Summary

`literature_evidence`. Both coded lines **support** different facets of the dissociated signature; there
is no disputing line:
- **Support — moderate:** `evidence-line:0061` (`paper:Aid2025`) — two independent cohorts (discovery
  n=28 LC; RECOVER validation n=18 LC), PBMC bulk RNA-seq + Olink proteomics: IL-6/JAK-STAT/JAK1,
  type-II IFN (IFNγ), and complement pathways persistently enriched at >180 days (IL-6R protein validated
  by ELISA/MSD), co-occurring with CD8 exhaustion (PDCD1, IFI44) and no detectable plasma virus. This is
  the persistent-inflammatory-activation arm.
- **Support — weak/moderate:** `evidence-line:0062` (`paper:Ryan2022`) — longitudinal whole-blood RNA-seq
  (12/16/24 wpi): type-I antiviral-effector ISGs (MX1/OAS3/OASL) **specifically decreased in LC-clinic
  referrals** vs other convalescents, emerging only at the ~6-month bifurcation. Reconciled as the
  **dissociated type-I-effector arm** of the same state — *supporting*, not disputing, the persistent-
  perturbation/exhausted-sensing reading.

## Caveats

Both sources are **observational**, modest-n, **pre-vaccination / pre-Omicron** cohorts (Aid2025
discovery 72% unvaccinated, Ryan2022 entirely pre-vaccine) [@Aid2025; @Ryan2022], so generalizability to the current vaccinated/
Omicron LC population is unestablished. The two readouts are not strictly comparable: **PBMC** (Aid2025)
vs **whole blood** (Ryan2022, granulocyte/platelet-rich); **GSEA pathway enrichment** (broad IFN-signaling
machinery) vs **specific terminal ISG transcripts**; **LC-vs-recovered/healthy** (Aid2025) vs
**referral-vs-non-referral within convalescents** (Ryan2022). The dissociation reading is therefore an
inference *across* two designs, not a within-study demonstration that the same patients carry both arms
simultaneously — the discriminating confirmation would be a single cohort assaying both type-II tone and
type-I-effector ISGs longitudinally (`interpretation:0012` New Questions). The proposition is descriptive:
it asserts the *state*, not that the inflammatory arm **causes** symptoms (`proposition:0026`,
`question:0006`).

**Cross-PAIS boundary (t060, 2026-06-26).** Non-COVID PAIS pathway recurrence is now recorded separately
as `proposition:0036`. EatonFitch2024, Che2025, and QFS studies make the LC state more plausible as a
pathway family rather than a SARS-CoV-2-only artifact, but they do not directly support this proposition's
full LC-specific dissociated signature unless the same design co-measures sustained IL-6/JAK-STAT/type-II
IFN, blunted type-I antiviral-effectors, and exhaustion markers.
