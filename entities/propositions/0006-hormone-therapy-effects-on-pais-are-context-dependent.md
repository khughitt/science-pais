---
id: "proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent"
kind: "proposition"
title: "Hormone-therapy effects on PAIS, if present, are route/dose/timing/indication-dependent"
status: "active"
claim_layer: "causal_effect"
identification_strength: "observational"
proxy_directness: "indirect"
supports_scope: "hypothesis_bundle"
measurement_model:
  observed_entity: "observational associations between exogenous-hormone-therapy exposure (HRT/COCP) and infection outcomes, in this corpus only on acute-COVID and symptom-predicted endpoints"
  latent_construct: "the causal effect (and its heterogeneity by route/dose/timing/indication/comorbidity) of hormone therapy on post-acute PAIS"
  measurement_relation: "the observed associations are indirect proxies for the latent PAIS effect — separated from it by outcome window (acute vs post-acute), outcome type (predicted vs measured), and unmeasured exposure detail (route/dose/timing/indication)"
  known_failure_modes:
    - "healthy-user / indication bias (HRT and COCP are prescribed to non-exchangeable populations)"
    - "menopause/PAIS symptom-overlap ascertainment on symptom-predicted outcomes"
    - "acute-to-post-acute transport failure (an acute-infection association need not hold for post-acute persistence)"
    - "missing route/dose/timing/indication collapses heterogeneous exposures into one variable"
discusses:
  - frame: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    role: "background"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways"
  - "topic:menopause-sex-hormones-and-pais-risk"
  - "interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test"
  - "interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage"
  - "evidence-line:0037-costeira2021-hrt-cocp-divergence-acute-supports-hormone-therapy-context-dependence"
  - "task:t019"
  - "task:t045"
source_refs:
  - "paper:Averyanova2022"
  - "paper:Costeira2021"
created: "2026-06-21"
updated: "2026-06-25"
---

# Proposition: Hormone-therapy effects on PAIS, if present, are route/dose/timing/indication-dependent

## Claim

Hormone-therapy effects on PAIS, **if present, are route-, dose-, timing-, indication-, and comorbidity-dependent** rather than uniformly protective or harmful. The claim is about the *heterogeneity* of any HRT effect, not its average sign.

## Evidence Summary

Two independent weak/proxy lines, both short of a direct PAIS-outcome test:

- `paper:Averyanova2022` (`evidence-line:0014`) supplies indirect biological plausibility for route- and timing-dependent hormone effects on immune, endothelial, and hemostatic systems — analogical support for *why* an HRT effect would be heterogeneous.
- `paper:Costeira2021` (`evidence-line:0037`) supplies an empirical instance of that heterogeneity: within one large cohort, HRT and COCP — two estrogen-containing therapies — associate in **opposite directions** with predicted acute COVID (HRT OR 1.32 vs COCP OR 0.87), with route/dose/indication unavailable. This is an **acute, symptom-predicted** outcome, so it is proxy-only for PAIS and vulnerable to (though Costeira2021 does not itself test) menopause-symptom-overlap ascertainment.

The **t019 audit** (`interpretation:0008`) found **no admissible direct HRT→post-acute-PAIS test anywhere in the corpus** — every hormone-therapy datum is acute-COVID, self-selected survey, or clinical-management recommendation. The **t045 Neuhouser2024 WHI triage** (`interpretation:0020`) preserves that verdict: WHI published a postmenopausal-women long-COVID risk-factor screen, but HRT/MHT is not reported as an exposure or estimate. As cited, this proposition is therefore confirmed in content but remains **more prediction than established result**, and its disposition is that HRT evidence enters PAIS work as clinical-screening / measurement-confound context, not causal evidence.

## Caveats

Thinly evidenced, and the t019 audit (`interpretation:0008`) established the thinness is a **genuine evidence gap**, not an oversight: no cohort has tested HRT exposure (route/dose/timing/indication) against a post-acute PAIS outcome. Observational HRT–PAIS associations are dominated by healthy-user and indication biases, so an apparent uniform protective or harmful effect is the expected artifact this proposition warns against. Both current lines are **weak/proxy**; neither licenses an effect-sign estimate. `background` role: it refines but does not constitute `hypothesis:0005` (excluded from the bundle's belief conjunction). The "test it" path runs through `task:t039` (All of Us prescription records) and the UKB primary-care HRT-prescription option, using active-comparator/new-user designs to break indication bias.
