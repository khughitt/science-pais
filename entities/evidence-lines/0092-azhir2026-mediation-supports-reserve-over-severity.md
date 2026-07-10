---
id: evidence-line:0092-azhir2026-mediation-supports-reserve-over-severity
kind: evidence-line
title: Azhir2026 mediation decomposition supports reserve dominating acute severity
status: active
stance: supports
target: proposition:0043-host-reserve-dominates-acute-severity-gate
source: paper:Azhir2026
strength: strong
independence: independent
independence_group: azhir2026-mgb-ehr-mediation
evidence_role: direct_test
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
source_refs:
- paper:Azhir2026
created: '2026-07-10'
updated: '2026-07-10'
evidence_type: literature_evidence
---
# Evidence Line: Azhir2026 mediation decomposition supports reserve dominating acute severity

## What this line shows

`paper:Azhir2026` (133,792-patient Mass General Brigham EHR cohort) provides a causal mediation decomposition directly testing whether reserve or acute severity dominates PASC risk. After comorbidity adjustment each decade of age is *protective* (OR 0.94); mediation attributes ~145% of the crude age effect to the Charlson comorbidity index (inconsistent mediation — comorbidity's harm masks age's direct protection) versus only ~12% to acute severity, and the direct age-protection exhausts near 65 [@Azhir2026]. This is a `direct_test` of `proposition:0043`'s core reserve-dominates-severity claim.

## Why it is independent

This line is a single-health-system EHR mediation study with a quantitative severity-vs-comorbidity decomposition. It is independent of `evidence-line:0093` (Russell2023), which supplies a mechanistic multimorbidity/Mendelian-randomization argument on different populations; the two share neither cohort nor method (mediation decomposition vs. MR + tolerance-model synthesis).

## Caveats / scope

`direct_test`, strong, but observational and proxy-mediated (see Measurement Model). Inconsistent mediation is sensitive to the adjustment set and unmeasured confounding; the Black-males-under-45 exception (positive age estimate regardless of comorbidity) may be an ascertainment/stratification artifact; and reserve proxies in EHR data are entangled with the care-seeking ascertainment channel (`hypothesis:0008`). Severity is demoted but not deleted — hospitalization (OR 1.35) and ICU (OR 1.93) remain independently elevated.

## Measurement Model

"Host reserve" is latent; Azhir2026 operationalizes it via the Charlson comorbidity index and "acute severity" via care-setting (hospitalization/ICU). The 145%-vs-12% mediation split is therefore a decomposition of *proxy-measured* reserve against *proxy-measured* severity: the directional conclusion (reserve dominates) is robust to this proxy error, but the specific magnitudes inherit the proxies' construct error (Charlson under-captures sub-clinical immunological margin; care-setting severity is ascertainment-shaped) and should be read as proxy-conditional.
