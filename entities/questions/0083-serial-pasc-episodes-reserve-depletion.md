---
id: question:0083-serial-pasc-episodes-reserve-depletion
kind: question
title: Does serial PASC episode accumulation deplete physiological reserve in a dose-dependent,
  measurable way consistent with an immunological scarring model?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Azhir2026
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0004-acute-severity-threshold
created: '2026-07-10'
updated: '2026-07-10'
---

# Does serial PASC episode accumulation deplete physiological reserve in a dose-dependent, measurable way consistent with an immunological scarring model?

## Summary

Azhir2026 reports escalating hazard ratios for PASC sequelae with repeated SARS-CoV-2 infections (HR ~1.35 after first infection, 2.11 after second, 3.00 after three or more; citing Bowe et al. 2022). The authors propose this could reflect immunological scarring — each PASC episode induces durable changes in immune function or tissue integrity that lower the threshold for future PASC entry. This question asks whether this escalation represents genuine reserve depletion (a measurable, dose-dependent process) or is instead explained by unmeasured confounding by high-exposure, high-comorbidity individuals who are systematically re-infected.

## Why It Matters

- If serial PASC episodes causally deplete reserve, PASC transitions from a self-limited to a potentially progressive condition for a subset of patients — with profound implications for the project's attractor framing (`hypothesis:0001`) and for clinical guidance (particularly around infection prevention and early treatment in prior-PASC patients).
- Affects the reserve-gate model (`hypothesis:0020`): if PASC itself shifts the reserve axis, then the reserve is not a fixed pre-infection baseline but a time-varying quantity that deteriorates with PASC history, requiring dynamic modeling.
- Risk if unanswered: clinical nihilism or misplaced optimism — either under-prioritizing infection prevention in patients with prior PASC, or over-attributing re-infection severity to unmeasured confounders.

## Current Evidence

- **Supporting escalating risk (Bowe2022, cited in Azhir2026):** Hazard ratios for ≥1 PASC sequela rise from ~1.35 (first infection) → 2.11 (second) → 3.00 (three or more) in a large VA cohort. This dose-response shape is consistent with a causal reserve-depletion model.
- **ZhangRECOVEREHR2026 (in h0004):** Second SARS-CoV-2 infection associated with higher PASC diagnosis and PASC-related symptom/condition risk than first infection in pediatric Omicron-era EHR; direction consistent, but EHR coding prevents mechanism claims.
- **Conflicting — confounding by indication:** Individuals with frequent re-infections may be systematically higher-exposure (essential workers, immunocompromised, lower socioeconomic status) and may carry unmeasured comorbidities that simultaneously increase re-infection probability and PASC risk — creating the appearance of dose-response without genuine reserve depletion. The observational design of both Bowe2022 and Azhir2026 cannot distinguish these.
- **Conflicting — recency bias:** Vaccination uptake and variant-specific severity changed substantially across waves; later infections under Omicron carry different PASC risks. HR escalation may reflect earlier-era high-severity infection + later reinfection compounding rather than episode count per se.

## Thoughts

- The dose-response pattern (1.35 → 2.11 → 3.00) is sufficiently steep to warrant taking the immunological scarring hypothesis seriously, but the observational evidence is insufficient to distinguish causal reserve depletion from confounding by re-exposure frequency.
- The most parsimonious test would be a within-person longitudinal design measuring a reserve proxy (e.g., naïve-T fraction, CCI change, biological age clock acceleration) before first and between subsequent PASC episodes, to determine whether reserve shifts after PASC independent of new comorbidity accrual.
- The alternative — that each re-infection is a new independent draw at a fixed reserve level — predicts roughly constant HR across episodes (after severity adjustment), inconsistent with the observed escalation pattern.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (if PASC is a self-reinforcing state that lowers threshold for re-entry); `hypothesis:0020-host-immune-baseline-reserve-gate` (PASC as a source of dynamic reserve depletion); `hypothesis:0004-acute-severity-threshold` (threshold may shift downward after each PASC episode)
- Required analyses: Within-person longitudinal analysis of reserve proxy before and after PASC episodes, with acute severity adjustment; ideal design = paired biosampling at infection, PASC resolution, and re-infection. Negative-control outcome design (using non-PASC sequelae with known incidence) to bound confounding.
- Priority level: medium-high — this question directly determines whether PASC should be framed as a chronic progressive risk factor (not just a post-acute consequence), which would substantially change the project's intervention target framing.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`
- Article notes: `paper:Azhir2026`; Bowe et al. 2022 (Nat Med, 28: 2398–2405) — primary re-infection PASC data; `paper:ZhangRECOVEREHR2026`
- Methods/Datasets: VA Million Veteran Program / VA EHR (Bowe2022 dataset — not publicly available at individual level); RECOVER-EHR pediatric cohort (ZhangRECOVEREHR2026)
