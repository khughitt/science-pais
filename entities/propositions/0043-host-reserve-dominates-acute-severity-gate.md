---
id: proposition:0043-host-reserve-dominates-acute-severity-gate
kind: proposition
title: Host baseline reserve dominates acute severity in gating PAIS risk
status: active
claim_layer: causal_effect
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: administrative EHR proxies — Charlson comorbidity index / comorbidity counts (reserve) and care-setting hospitalization/ICU (acute severity) — in a causal mediation decomposition
  latent_construct: pre-infection host immunological/physiological reserve as the dominant gate on PAIS risk, with acute severity subordinate
  measurement_relation: reserve and severity are both indirect billing-derived proxies; the 145%-vs-12% mediation split decomposes proxy-measured reserve against proxy-measured severity, so the direction is proxy-robust but the magnitude is proxy-conditional
  known_failure_modes:
  - Charlson under-captures sub-clinical immunological margin and over-weights mortality-salient conditions
  - care-setting severity is ascertainment-shaped and entangled with care-seeking (hypothesis:0008)
  - inconsistent mediation is sensitive to the adjustment set and unmeasured confounding
  - no pre-infection biological-reserve measure (inflammatory tone, naive-T fraction) is used
discusses:
- hypothesis:0020-host-immune-baseline-reserve-gate
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0004-acute-severity-threshold
source_refs:
- paper:Azhir2026
- paper:Russell2023
created: '2026-07-10'
updated: '2026-07-10'
---
# Proposition: Host baseline reserve dominates acute severity in gating PAIS risk

## Claim

Pre-infection host reserve — comorbidity burden and physiological/immunological margin — is the **dominant** term gating PAIS risk, with acute-illness severity a real but **subordinate** term. In a causal mediation decomposition, comorbidity accounts for ~145% of the crude age effect (inconsistent mediation: comorbidity's harm masks age's direct protection) while acute severity mediates only ~12%, and age's direct protective effect exhausts near 65. This is the forward reading of `hypothesis:0020` and reweights `hypothesis:0004` from primary to secondary gate.

## Evidence Summary

`paper:Azhir2026` (133,792-patient Mass General Brigham EHR cohort) is the strongest single result: after comorbidity adjustment each decade of age is *protective* (OR 0.94); causal mediation attributes 145% of the crude age effect to the Charlson comorbidity index vs. 12% to acute severity; the direct age-protection vanishes after 65, and reinfection escalates PASC hazard (1.35 → 2.11 → 3.00 across 1/2/3+ infections). `paper:Russell2023` supplies the mechanistic vocabulary — a resistance-vs-tolerance three-phase model in which *total multimorbidity burden* (not any single condition) dominates severity, most comorbidities act via reduced tolerance/reserve, and Mendelian randomization separates causal (obesity → adipositis → pneumonitis) from confounded (T2D, not independently causal) associations. Severity is demoted but not deleted: hospitalization (OR 1.35) and ICU (OR 1.93) remain independently elevated, so `hypothesis:0004` survives as a genuine secondary term.

## Caveats

Reserve is measured only by proxy (Charlson index, comorbidity counts) — aggregates built for mortality prediction, not immunological reserve; the project's desired biological proxies (inflammatory tone, naive-T fraction) are untested here. The mediation decomposition is observational and design-dependent (inconsistent mediation is sensitive to the adjustment set and to unmeasured confounding). Azhir2026's Black-males-under-45 exception (positive age estimate regardless of comorbidity) may be an ascertainment/stratification artifact, and reserve is entangled with ascertainment (`hypothesis:0008`) because EHR reserve proxies are themselves care-seeking-shaped. Identification is therefore `observational`; a clean test needs a pre-infection biological-reserve measure, not a billing-derived comorbidity index.

## Measurement Model

"Host reserve" is a latent construct operationalized here **indirectly** via the Charlson comorbidity index and comorbidity counts, and "acute severity" via care-setting (hospitalization/ICU) — both administrative proxies. The 145%-vs-12% mediation split is therefore a decomposition of *proxy-measured* reserve against *proxy-measured* severity, and the numeric shares inherit the proxies' construct error: Charlson under-captures sub-clinical immunological margin and over-weights conditions salient to mortality, and care-setting severity is ascertainment-shaped. The proposition's directional claim (reserve dominates severity) is robust to this proxy error in the observed data, but the *magnitude* (the specific 145%/12% figures) should be read as proxy-conditional, not as the true reserve/severity effect ratio.
