---
id: proposition:0044-female-pasc-bias-x-chromosome-dosage-rival
kind: proposition
title: Female PASC bias may be driven by X-chromosome dosage or XIST rather than gonadal-steroid
  timing
status: active
claim_layer: mechanistic_narrative
identification_strength: observational
proxy_directness: indirect
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
- proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways
source_refs:
- paper:Chaulagain2026
created: '2026-07-10'
updated: '2026-07-10'
---
# Proposition: Female PASC bias may be driven by X-chromosome dosage or XIST rather than gonadal-steroid timing

## Claim

The female excess in PASC may be carried largely by **sex-chromosome dosage** (X-linked immune-gene dosage, XCI escape of TLR7/KDM6A, XIST upregulation) rather than by **gonadal-steroid timing** (the ER/AR/PR-mediated hormone axis that `hypothesis:0005` and its propositions assume). This is a **rival / competing mechanism** to the hormone-axis account: it predicts a genetic-sex signal that does not track menopausal-transition hormone state, whereas the hormone account predicts an effect concentrated in the peri-/post-menopausal hormone-decline window.

## Evidence Summary

`paper:Chaulagain2026` (Nature Immunology review) presents two orthogonal axes and states that **"there is limited evidence supporting a role for gonadal steroids in PASC outcomes so far,"** attributing the female PASC signal instead largely to X-chromosome-dosage effects (XIST upregulation in female PASC immune cells; biallelic TLR7 expression), with the *male* PASC cardiovascular phenotype linked to Y-gene loss (DDX3Y/UTY). This partially contradicts the hormone-mediated core of `proposition:0002`, even as the female 40–55 PASC peak it reports remains consistent with a perimenopausal window. Chaulagain2026 also supplies an "immunopathology-vs-reduced-immunity polarity" tool: sex effects can *reverse direction* depending on which failure mode drives severity.

## Caveats

Chaulagain2026 is a review, not a design that separates genetic sex from hormone timing, so this proposition is a **rival hypothesis raised to parity, not a refutation** of the hormone axis: the 40–55 female peak is jointly consistent with both accounts. Evidence for the X-dosage mechanism (XIST/TLR7) is molecular and largely cross-sectional, and its causal link to the PASC *phenotype* is indirect. Identification is `observational`; neither axis is isolated in any hormone-measured, genetically-resolved longitudinal PAIS cohort.

## Measurement Model

The two rival mechanisms are only distinguishable through proxies that are usually confounded in observational data: the hormone axis is proxied by menopausal stage / measured E2-FSH-AMH, and the X-dosage axis by molecular readouts (XIST expression, TLR7 biallelic expression, XCI-escape gene dosage). Age, menopausal transition, and X-dosage all co-vary with female sex, so a female-PASC association alone (`proxy_directness: indirect`) cannot attribute causation to either axis. A **discriminating design** measures hormones and genetic-sex markers in the *same* subjects and tests whether the PASC signal tracks hormone state at fixed karyotype (favoring hormone timing) or tracks X-dosage/XIST at fixed hormone state (favoring genetic sex) — e.g., comparing surgically vs. naturally menopausal women at matched hormone levels, or Klinefelter/Turner-informative contrasts.

## Related Propositions

This proposition is a **RIVAL / competing account** to the hormone-axis bundle:

- `proposition:0001` (reproductive-stage transition shifts the failed-recovery threshold) — rival: attributes the female/midlife excess to hormone-timing state; this proposition attributes it to genetic-sex dosage.
- `proposition:0002` (reproductive-stage transition modifies immune-regulatory pathways) — **direct competitor**: proposition:0002 posits ER/AR/PR gonadal-steroid modulation as the substrate; Chaulagain2026 reports "limited evidence" for gonadal steroids in PASC and offers X-dosage/XIST as the alternative substrate.

Discriminating evidence: a hormone-measured, genetically-resolved cohort in which the PASC signal is regressed on hormone state and X-dosage jointly (see Measurement Model). Feeds the h0005-vs-X-dosage decomposition task (t125) and `question:0080`.
