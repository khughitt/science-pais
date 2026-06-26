---
id: interpretation:0029-t060-cross-pais-ifn-jakstat-pathway-map
type: interpretation
title: "t060 - cross-PAIS IFN/JAK-STAT pathway map for q0006"
status: active
source_refs:
- paper:Aid2025
- paper:Ryan2022
- paper:EatonFitch2024
- paper:Che2025
- paper:Keijmel2016
- paper:Morroy2016
- paper:Patterson2024
- paper:Galbraith2011
related:
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0003-immune-exhaustion-feedback
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis
- evidence-line:0089-eatonfitch2024-mecfs-longcovid-exhaustion-panel-supports-cross-pais-axis
- task:t060
created: '2026-06-26'
updated: '2026-06-26'
input:
- paper:Aid2025
- paper:Ryan2022
- paper:EatonFitch2024
- paper:Che2025
- paper:Keijmel2016
- paper:Morroy2016
- paper:Patterson2024
- paper:Galbraith2011
prior_interpretations:
- interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration
relations:
- predicate: "sci:amends"
  target: "interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration"
---
# Interpretation: t060 - cross-PAIS IFN/JAK-STAT pathway map

## Verdict

**Verdict:** `[~]` partial cross-PAIS recurrence, not a shared-state proof. The LC evidence remains the
only coded full dissociated-signature state (`proposition:0025`: sustained IL-6/JAK-STAT/type-II-IFN/
complement tone plus blunted type-I antiviral-effector arm and exhaustion). Non-COVID PAIS evidence
supports a weaker statement: IFN/cytokine/exhaustion-axis abnormalities recur in ME/CFS and QFS, but the
assays and directions are not harmonized enough to claim the Aid2025/Ryan2022 LC state generalizes.

This pass mints `proposition:0036` as a **local q0006** proposition and codes one weak support line
(`evidence-line:0089`, EatonFitch2024). It does **not** alter h0003's core bundle or discharge the
driver-vs-marker test (`proposition:0026` / `pre-registration:0004`).

## Evidence Map

| Trigger / syndrome | Best evidence in corpus | q0006 reading |
|---|---|---|
| Long COVID | Aid2025 + Ryan2022 | Full LC dissociated-signature model: persistent inflammatory/type-II IFN/JAK-STAT tone plus type-I-effector blunting; descriptive state supported, causal driver untested. |
| ME/CFS | EatonFitch2024; Che2025 | Same-panel LC/ME/CFS NanoString supports broad IFN/cytokine/exhaustion overlap; Che2025 supports exercise-provoked immune exhaustion/dysregulation. Neither proves persistent JAK-STAT/IL-6 maintenance. |
| Q-fever fatigue syndrome | Keijmel2016; Morroy2016 | Coxiella-stimulated IFN-gamma elevation and IL-6/IL-2/IFN-gamma dysregulation support antigen-specific immune dysregulation, but not the LC JAK-STAT/IL-6 state. |
| PTLDS / chronic Lyme | Patterson2024; Bai2023 | Plasma cytokine hub evidence cuts both ways: LC and chronic Lyme are distinguishable, with different dominant hubs. This disputes identity of molecular state while leaving broad inflammatory recurrence possible. |
| Multi-trigger post-infective fatigue | Galbraith2011 | Head-to-head transcriptomics did not find a robust shared PBMC gene signature across EBV/RRV/Q-fever, warning against over-generalizing pathway recurrence from separate studies. |

## What Changed

EatonFitch2024 is now ingested because it directly addresses the missing cross-PAIS comparison:

- new `paper:EatonFitch2024`;
- new local `proposition:0036`;
- new `evidence-line:0089` supporting 0036 weakly;
- q0006/h0003/proposition notes updated to distinguish cross-PAIS recurrence from driver-vs-marker
  evidence.

## Why This Does Not Promote h0003

h0003's load-bearing uncertainty is causal: does JAK-STAT/IL-6/exhaustion maintain chronicity and reverse
with inhibition? t060 only addresses the **generalizability** half of q0006. Even a strong cross-PAIS
pathway recurrence result would not prove driver status. Conversely, Patterson2024 and Galbraith2011 mean
the cross-PAIS picture is not a simple "same signature everywhere" result.

## Next Useful Work

The highest-value follow-up is computational rather than another prose review: reanalyze public
transcriptomic/proteomic datasets with one locked pathway score set (Hallmark IL6-JAK-STAT3, IFN-alpha,
IFN-gamma, NF-kB/TNF, complement, exhaustion/checkpoint genes) across LC, ME/CFS, QFS, and PTLDS where
available. That should be kept separate from `t054`, which remains the interventional driver-vs-marker
readout.
