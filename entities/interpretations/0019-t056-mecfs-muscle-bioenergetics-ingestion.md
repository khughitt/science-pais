---
id: interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion
type: interpretation
title: "t056: ME/CFS has muscle-endpoint bioenergetic abnormalities, but the Appelman-type cross-trigger lesion remains unfilled"
status: active
source_refs:
  - paper:Jones2012
  - paper:Wong1992
  - paper:Brown2015
  - paper:Bizjak2024
related:
  - task:t056
  - question:0011-mitochondrial-basis-of-pem
  - hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality
  - proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
  - proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
  - evidence-line:0075-mecfs-muscle-bioenergetics-supports-0030
  - evidence-line:0076-mecfs-muscle-endpoint-data-disputes-clean-pem-endpoint-dichotomy
  - evidence-line:0077-bizjak2024-cross-trigger-muscle-biopsy-disputes-simple-same-lesion-reading
  - discussion:0004-pem-shared-muscle-lesion-vs-endpoint-contingency
created: '2026-06-25'
updated: '2026-06-25'
input:
  - paper:Jones2012
  - paper:Wong1992
  - paper:Brown2015
  - paper:Bizjak2024
prior_interpretations:
  - interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
  - interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
relations: []
---

<!-- Mode: CONCEPTUAL / LITERATURE. Input is an interim literature-ingestion pass for task:t056; no new pipeline output. -->

# Interpretation: t056 - ME/CFS muscle bioenergetics beside Appelman2024

## Verdict

**[~] partial positive / endpoint-narrowing.** The premise that there is **no ME/CFS muscle-endpoint datum** was too strong. Existing ME/CFS/CFS literature contains real muscle-local bioenergetic abnormalities under exercise or contraction-like stress, especially Jones2012's repeated-exercise 31P-MRS acidosis/recovery abnormality. That updates the h0006-A1 vs h0008-M3 collision in h0006's favor at the level of **localization**: long-COVID PEM is not the only PAIS context with objective muscle bioenergetic pathology.

But the decisive A1 cell is still not filled. None of the ME/CFS studies is the same endpoint family as Appelman2024: no published ME/CFS arm has pre/post-CPET muscle biopsy measuring OXPHOS capacity, SDH/Complex II activity, fiber-type shift, immune infiltrate, amyloid/myopathic injury, and 24 h post-exertional kinetics under a harmonized long-COVID protocol. So the honest update is not "shared Appelman lesion confirmed"; it is "ME/CFS muscle pathology exists, and the remaining gap is endpoint equivalence, not total absence."

## Findings

1. **Jones2012 is the best t056 hit.** In 18 CDC-1994 CFS patients and 12 sedentary controls, repeated exercise with 31P-MRS found a normal-PCr-depletion subgroup that developed excess intramuscular acidosis after comparable work and had nearly four-fold prolonged pH recovery. Resting pH was similar, so the signal is provoked/recovery-phase rather than a static resting abnormality.

2. **Wong1992 provides an older in-vivo anchor.** During 31P-NMR gastrocnemius exercise, CFS patients reached exhaustion faster and had lower ATP at exhaustion despite broadly similar qualitative pH/phosphocreatine trajectories. The signal is weaker and older, but it supports the idea that working skeletal muscle is a real endpoint in CFS.

3. **Brown2015 gives a muscle-cell contraction-response mechanism.** CFS-derived skeletal-muscle cultures failed to increase AMPK phosphorylation and glucose uptake after electrical pulse stimulation while preserving insulin-stimulated glucose uptake. This is not in-vivo PEM, but it is hard to explain as pure effort or deconditioning.

4. **Bizjak2024 is the cross-trigger caution.** CFS and post-COVID syndrome both show muscle mitochondrial abnormalities, but not the same phenotype: post-COVID shows a complex-I/OXPHOS emphasis, while CFS has more progressed morphological/cristae abnormalities. This supports muscle involvement and simultaneously warns against collapsing triggers into a single identical lesion.

## Graph Updates

- New `proposition:0030` captures the local claim: ME/CFS has exercise/contraction-provoked skeletal-muscle bioenergetic abnormalities.
- `evidence-line:0075` supports `proposition:0030` from the consolidated ME/CFS muscle-bioenergetics body.
- `evidence-line:0076` weakly disputes the over-clean `proposition:0011` dichotomy ("ME/CFS whole-body vs long-COVID muscle") from ME/CFS exercise/contraction muscle-endpoint data.
- `evidence-line:0077` separately records Bizjak2024's direct CFS/post-COVID muscle-biopsy comparison: muscle is a shared domain, but the same lesion is not yet demonstrated. `proposition:0011` should stay supported, but now contested and narrower.

## Implications

**For h0006:** this is a real positive interim update for the muscle-localization/A1 side. It should be cited in h0006's Supporting Evidence and in the promotion-criterion note. However, h0006 should not promote: P2/P3 (ischemic/ionic upstream mechanism) remain untested here, and the cross-trigger Appelman-style muscle lesion is not demonstrated.

**For h0008-M3:** endpoint contingency still matters, but the previous example is less one-directional. Endpoint choice can now **hide potential convergence** as well as manufacture divergence: if one compares ME/CFS whole-body CPET against long-COVID muscle biopsy, the triggers look different; if one reads the ME/CFS muscle 31P-MRS/cell/biopsy literature beside Appelman2024, they look more convergent but still not endpoint-equivalent. M3 remains a live measurement critique, not a settled biological refutation of h0006.

**For q0011:** the provoked-state interpretation strengthens. Resting-state bioenergetics remain discordant, but exercise/contraction/recovery endpoints in ME/CFS repeatedly expose abnormalities.

## Residual Gap

The decisive experiment remains a harmonized ME/CFS + long-COVID muscle-endpoint study: same exertional provocation, pre/immediate/24-48 h muscle biopsy, OXPHOS and SDH/Complex-II activity, fiber-type composition, ionic markers, immune infiltrate, myopathic injury, and matched recovered/healthy controls. t056 moves the prior from "missing ME/CFS muscle endpoint" to "missing endpoint-harmonized cross-trigger equivalence."
