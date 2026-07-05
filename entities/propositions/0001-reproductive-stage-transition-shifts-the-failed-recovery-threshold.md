---
id: "proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold"
kind: "proposition"
title: "Reproductive-stage transition shifts the failed-recovery threshold governing PAIS risk"
status: "active"
claim_layer: "causal_effect"
identification_strength: "observational"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "question:0013-reproductive-stage-failed-immune-recovery-after-infection"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways"
  - "proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing"
  - "patch-definition:menopause-pais-causal-dag"
  - "pre-registration:0001-menopause-pais-total-effect"
source_refs:
  - "paper:Shah2025"
  - "paper:Silva2024"
  - "paper:Shahbaz2025"
  - "paper:Mishra2020"
  - "paper:Rebman2026"
  - "paper:Boneva2015"
created: "2026-06-21"
updated: "2026-06-26"
---

# Proposition: Reproductive-stage transition shifts the failed-recovery threshold governing PAIS risk

## Claim

Reproductive-stage transition (peri- to post-menopause) shifts the effective host-reserve / threshold term that governs whether an acute infection resolves, making the probability of **failed post-infectious recovery (PAIS) reproductive-stage-dependent** at a given infectious insult. This is the forward (P→) causal-effect reading of `hypothesis:0005`; it is stated neutrally as to the sign and magnitude of the effect, which the evidence is to settle.

## Evidence Summary

Current support is indirect and observational. Female sex is a reproducible long-COVID risk factor with the clearest excess in a midlife age band (`paper:Shah2025`), and two independent, non-UK-Biobank cohorts find lower gonadal steroids associated with greater long-COVID burden (`paper:Silva2024`, `paper:Shahbaz2025`). `paper:Boneva2015` adds a weak ME/CFS timing clue: early/surgical menopause is enriched in CFS, and hysterectomy/oophorectomy preceded CFS onset in 71% of the dated-surgery subset (`evidence-line:0081`) [@Boneva2015]. None of these isolates reproductive-stage *timing* from chronological age, surgical indication, gynecologic morbidity, or ascertainment. Acute-COVID analyses show menopausal/hormone proxies may not survive adjustment for age, severity, and comorbidity (`paper:Mishra2020`), and sex/menopausal status can act differently on acute presentation than on post-acute persistence (`paper:Rebman2026`) — both bounding a simple monotonic reading.

## Caveats

No hormone-measured longitudinal PAIS cohort yet isolates reproductive stage from age, acute severity, comorbidity, pregnancy, hormone therapy, and ascertainment. The supporting hormone associations are cross-sectional and **reverse-causation-ambiguous** — equally consistent with `proposition:0003` (infection perturbs the reproductive axis). Boneva2015 narrows that ambiguity for the surgical-menopause component, but it does not supply pre-infection natural-menopause or confirmed post-infection timing. Identification is therefore `observational`; the discriminating design is a directly-staged, hormone-measured longitudinal study. The committed UK Biobank analysis tests only the `{age, smoking}`-adjusted reduced form (`pre-registration:0001`), and can refute but not positively confirm the hormone-mediated mechanism (the t036 feasibility search, `report:0004`, found no off-the-shelf cohort for that positive test; live paths are `task:t038`/`task:t040`). Per-variable confounder/collider structure is derived from `patch-definition:menopause-pais-causal-dag`, not asserted here.
