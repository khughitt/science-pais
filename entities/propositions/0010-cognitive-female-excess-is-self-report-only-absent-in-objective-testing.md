---
id: "proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing"
type: "proposition"
title: "The PAIS cognitive female-excess is confined to self-reported complaints and is absent in objective neuropsychological testing"
status: "active"
claim_layer: "empirical_regularity"
identification_strength: "observational"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    role: "background"
related:
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "question:0018-objective-vs-subjective-cognition-dissociation-in"
  - "proposition:0005-menopause-pais-symptom-overlap-is-a-measurement-process"
  - "interpretation:0003-t018-subphenotype-sex-reproductive-stage"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "task:t018"
source_refs:
  - "paper:DelgadoAlonso2023"
  - "paper:Bland2024"
  - "paper:Cheetham2023"
created: "2026-06-22"
updated: "2026-06-22"
---

# Proposition: The PAIS cognitive female-excess is self-report-only, absent in objective testing

## Claim

In post-acute COVID, the female excess in the **cognitive** subphenotype ("brain fog") is a property of **subjective self-report**, not of **objective neuropsychological performance**. Women report more memory/executive complaints, but where cognition is tested objectively the sex signal disappears, and subjective complaint dissociates from objective deficit — the subjective channel tracking **fatigue/affect** while the objective deficit tracks **infection/ongoing-symptom status**. This is an `empirical_regularity` locating the female cognitive excess on a **measurement channel** (subjective vs objective); it does **not** claim there is no objective cognitive deficit in long COVID (there is), only that the *female excess* is not in it.

## Evidence Summary

- **Subjective female-skew + objective sex-null, with fatigue mediation** — DelgadoAlonso2023 (n=170, WHO criteria): women report more subjective memory complaints (FLEI 26.65±6.54 vs 23.04±8.41, p=0.004) but show **no sex difference on objective tests**, and **fatigue is the dominant mediator** (indirect β≈−0.317) between objective and subjective cognition. See `evidence-line:0021`.
- **Subjective and objective cognition are uncorrelated** — Bland2024 (n=162; PCS vs recovered vs naïve): CFQ↔Cognitron r≈−0.07 (p=0.161); the subjective complaint loses COVID-group significance once fatigue+stress are covaried (F=0.56, p=0.575) while the **objective deficit remains COVID-linked** (F=4.61, p=0.011). See `evidence-line:0022`.
- **The objective deficit is real and symptom-status-linked, not sex-linked** — Cheetham2023 (controlled-longitudinal, n≈3,335): objective accuracy deficit scales with ongoing-symptom status (largest for ≥12-week non-recovered, β≈−0.22 SD), is absent in the recovered, and sex enters only as a non-significant adjustment covariate. Background constraint. See `evidence-line:0023`.

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0005`. The dissociation is **COVID-specific** in this evidence base; other triggers were not tested at the subjective/objective level. The objective sex-null is **direct** in DelgadoAlonso2023 and Bland2024 but **inferred** in Cheetham2023, which did not run a sex-stratified objective analysis (the absence of a reported sex×deficit interaction there is a *gap*, not a positive null) — hence Cheetham is weighted as a background constraint, not a direct sex-contrast line. Confounds: reverse causation and ascertainment cannot be excluded (women are more care-seeking and more likely to report complaints); the subjective measures (FLEI, CFQ) are affect-sensitive. The standing project question `question:0018` asks whether this objective/subjective dissociation generalises beyond COVID. This proposition concerns the **cognitive** domain only and is one instance of the broader measurement-channel pattern that `interpretation:0003` reads across subphenotypes.
