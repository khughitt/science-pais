---
id: "proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode"
kind: "proposition"
title: "The objective correlates of post-exertional malaise are trigger- and endpoint-specific, not a single shared whole-body bioenergetic-recovery failure across PAIS triggers"
status: "active"
claim_layer: "empirical_regularity"
identification_strength: "observational"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0001-shared-dysregulated-attractor"
    role: "background"
related:
  - "question:0015-does-pem-requirement-improve-cross-study-comparability"
  - "question:0001-shared-molecular-signature-across-triggers"
  - "question:0011-mitochondrial-basis-of-pem"
  - "interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation"
  - "interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands"
  - "evidence-line:0036-maestri2025-pem-symptom-resolved-proteome-but-severity-unadjusted-confirms-gap"
  - "proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality"
  - "evidence-line:0076-mecfs-muscle-endpoint-data-disputes-clean-pem-endpoint-dichotomy"
  - "evidence-line:0077-bizjak2024-cross-trigger-muscle-biopsy-disputes-simple-same-lesion-reading"
  - "interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion"
  - "task:t056"
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "task:t025"
  - "task:t044"
source_refs:
  - "paper:Keller2014"
  - "paper:Gattoni2025"
  - "paper:Appelman2024"
  - "paper:Maestri2025"
  - "paper:Jones2012"
  - "paper:Bizjak2024"
created: "2026-06-22"
updated: "2026-06-25"
---

# Proposition: Objective PEM correlates are trigger- and endpoint-specific, not one shared failure mode

## Claim

Post-exertional malaise (PEM) is shared as a **symptom label** across ME/CFS and long COVID, but its **objective physiological correlate is not yet shown to be one shared, endpoint-invariant failure mode**. In ME/CFS the best-validated hallmark remains a **whole-body** bioenergetic-recovery failure — a reproducible day-2 decrement in VO₂/work-rate on two-day cardiopulmonary exercise testing (2-day CPET). PEM-enriched long-COVID patients do **not** reproduce that whole-body signature in the small Gattoni2025 cohort, yet they **do** show objective post-exertional pathology at the **peripheral-muscle** level (worsened mitochondrial oxidative phosphorylation after provoked PEM). The t056 ME/CFS muscle-bioenergetics pass now narrows this claim: ME/CFS also has muscle-endpoint abnormalities (`proposition:0030`), so the contrast is not "ME/CFS whole-body only vs long-COVID muscle only." The honest claim is endpoint-harmonization: same symptom, overlapping muscle-local evidence, but no demonstrated Appelman-equivalent cross-trigger muscle lesion under one protocol.

## Evidence Summary

- **ME/CFS — whole-body 2-day-CPET decrement (the positive reference arm)** — Keller2014 (Fukuda ME/CFS) shows a **13.8% day-2 VO₂peak decline** under confirmed maximal effort on both days (RER ≥ 1.1 unchanged), against a healthy/deconditioned test–retest reproducibility of ≤7% (r ≥ 0.95); 50% reclassified to a more impaired Weber–Janicki category on day 2. This is the established objective whole-body signature that operationalises PEM in ME/CFS and excludes deconditioning. See `evidence-line:0026`.
- **Long COVID — whole-body signature does not transfer** — Gattoni2025 (n=15 long COVID, 80% mDSQ-PEM) finds **no significant day-1 vs day-2 change** in gas-exchange threshold, VO₂peak, or peak work rate (all p > 0.05): subjective PEM is prevalent while the ME/CFS whole-body decrement is absent. See `evidence-line:0027`.
- **Long COVID — but objective pathology appears at the muscle level** — Appelman2024 (n=25 long COVID vs 21 recovered controls; PEM a required inclusion criterion; before/after exercise-biopsy) shows reduced mitochondrial **OXPHOS capacity**, a glycolytic fiber-type shift, and myopathic features that **worsen the day after** provoked PEM, with deconditioning ruled out by matched maximal effort. The objective long-COVID PEM lesion is real but sits at a **different endpoint** (peripheral skeletal muscle) than the ME/CFS whole-body CPET signature. See `evidence-line:0028`.
- **Long COVID — a fourth, blood-proteome endpoint (weak)** — Maestri2025 (STOP-PASC, n=152, Olink Explore HT 5400-plex) finds PEM carries a **symptom-resolved** plasma-protein association (↓IL1RL1/ST2, ↓IL1R2 — soluble IL-1/IL-33 decoy receptors) **distinct** from the fatigue/cardiovascular signature (↑leptin, ↑F7, ↑F12) and dyspnea (↓CD38). This extends the "PEM correlate is specific, not one shared signal" reading to the circulating proteome within a single trigger. Held **weak**: the per-symptom models are univariate and adjusted only for batch plate (no overall-severity covariate), so the PEM signal is not separated from general severity — a near-miss on the decisive `question:0015` test, not a passing of it. See `evidence-line:0036`, `interpretation:0007`.
- **ME/CFS — muscle-endpoint abnormalities already exist (weak criticism of the clean dichotomy)** — t056 (`interpretation:0019`) found Jones2012/Wong1992 31P-MRS exercise abnormalities and Brown2015 contraction-stimulated skeletal-muscle-cell abnormalities. This does **not** refute the endpoint-specific claim, because these endpoints are not Appelman2024-equivalent, but it disputes the stronger "ME/CFS whole-body vs long-COVID muscle" reading. See `proposition:0030` and `evidence-line:0076`.
- **Cross-trigger muscle biopsy — muscle domain overlaps, same lesion not shown** — Bizjak2024 directly compares CFS and post-COVID syndrome muscle biopsy and finds abnormalities in both groups, but with different mitochondrial functional/morphological emphasis. This weakly disputes both a one-sided muscle-domain contrast and a naive same-lesion convergence claim. See `evidence-line:0077`.

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0001`: this **constrains** the shared-dysregulated-attractor frame — it shows the attractor, if shared, is not uniform at the objective bioenergetic level — rather than offering a rival mechanism. Bounding limitations: (1) the long-COVID whole-body **null is weak** — Gattoni2025 is n=15, almost certainly underpowered to exclude a small day-2 decrement, uses retrospective mDSQ rather than provocation-confirmed PEM, has no PEM-negative or ME/CFS arm, and 40% of the cohort was aerobically deconditioned (`evidence-line:0027` carries this); a true zero and a missed ME/CFS-sized effect are not yet distinguishable. (2) The arms come from **different cohorts, protocols, and case definitions** (Fukuda/CDC CFS vs WHO long COVID), so the cross-trigger contrast is between-study, not within one harmonised design — exactly the within-cohort comparison that `question:0015`/`task:t025` want and that **does not yet exist** in the literature. (3) Whole-body CPET, 31P-MRS acidosis recovery, in-vitro contraction signaling, resting biopsy respirometry, and post-PEM muscle biopsy measure **different things**. After t056, the proposition is **contested**: endpoint-specific divergence remains the best explanation of the published cross-trigger mismatch, but the ME/CFS muscle-bioenergetics literature shows that muscle involvement is not long-COVID-specific and that harmonized endpoint choice could reveal more convergence than the original three-arm contrast implied. The standing question `question:0015` reads PEM-requirement as the highest-yield coherence criterion; this proposition qualifies that: PEM-requirement improves *within-trigger* coherence but does not guarantee *cross-trigger* biological exchangeability.
