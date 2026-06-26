---
id: question:0011-mitochondrial-basis-of-pem
type: question
title: What is the mitochondrial/bioenergetic basis of post-exertional malaise, and
  is it shared across PAIS?
status: active
ontology_terms:
- post-exertional malaise
- mitochondrial dysfunction
- bioenergetics
- oxidative metabolism
- ME/CFS
- post-acute infection syndrome
datasets: []
source_refs:
- cite:Che2025
- cite:Bateman2023
- cite:Hanson2023
- cite:Naviaux2016
- cite:Germain2022
- cite:Walitt2024
- cite:Appelman2024
- cite:Wang2023
- cite:Joseph2023
- cite:Keller2014
- cite:Scheibenbogen2024
- cite:Syed2025
- cite:Baraniuk2025
- cite:Shankar2025
- cite:Saito2024
- cite:Huang2024
- cite:McGregor2019
- cite:Gattoni2025
- cite:Jones2012
- cite:Wong1992
- cite:Brown2015
- cite:Bizjak2024
related:
- topic:mecfs-long-covid-convergence
- topic:biomarkers-and-objective-endpoints
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion
- proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality
- pre-registration:0005-harmonized-provoked-muscle-endpoint
- task:t058
- paper:McGregor2019
- paper:Jones2012
- paper:Wong1992
- paper:Brown2015
- paper:Bizjak2024
created: '2026-06-11'
updated: '2026-06-26'
---

# What is the mitochondrial/bioenergetic basis of post-exertional malaise, and is it shared across PAIS?

## Summary

Post-exertional malaise (PEM) — a delayed, disproportionate worsening of symptoms after physical or cognitive exertion — is the most distinctive and disabling feature of ME/CFS and a core feature of long COVID. A leading hypothesis is that PEM has a mitochondrial/bioenergetic basis: impaired oxidative ATP production, a shift toward inefficient anaerobic metabolism, and a failure to recover bioenergetic homeostasis after exertion. This question asks what that bioenergetic lesion actually is, and — critically for the project — whether it is *shared* across PAIS triggers (a convergent failure mode) or trigger-specific.

## Why It Matters

- Determines whether PEM can be given an objective, provoked bioenergetic biomarker (a measurable exertion-recovery deficit) suitable as a diagnostic and trial endpoint, and whether metabolic/mitochondrial-targeted therapies are rational.
- If unanswered, PEM remains defined by self-report, exertion-based trials lack objective endpoints, and the project cannot tell whether bioenergetic failure is a shared PAIS mechanism or a coincidental convergence of symptoms.

## Current Evidence

- Supporting: Che2025 directly probes the provoked state with a standardized cardiopulmonary exercise challenge plus pre/post multi-omics, finding a heightened innate-immune response coupled to secondary metabolic and mitochondrial failures forming a self-reinforcing loop manifesting as fatigue and PEM — the most mechanistically explicit bioenergetic-PEM model in the project's literature. Bateman2023 (clinical/neurobiology review) establishes impaired energy production and PEM as defining ME/CFS features and frames ME/CFS as commonly post-infectious, situating the bioenergetic lesion within the PAIS frame.
- Conflicting / cautionary: Hanson2023 argues classical ME/CFS is enterovirus-specific and explicitly cautions against conflating post-COVID illness with classical ME/CFS — directly challenging the "shared across PAIS" half of this question and warning that an apparently common PEM bioenergetic signature could mask trigger-specific biology. Mitochondrial-dysfunction findings in ME/CFS have historically been inconsistent across studies and assays.
- **Direction-of-effect discordance (added 2026-06-20, from the t005 reading pass):** the literature does not agree on which *way* the resting bioenergetic lesion points (see the dedicated sub-question below). Naviaux2016 reports a resting *hypometabolic* "dauer" state (≈80% of diagnostic metabolites decreased); Missailidis et al. 2020 and Peppercorn2023 instead report *compensatory respiratory hyperactivation*/inefficiency (e.g. isolated Complex V inefficiency with elevated respiration); while Germain2022 and Walitt2024 find **no global resting hypometabolism / no basal mitochondrial dysfunction** at all, with the deficit appearing only in the *provoked* (post-exertional) state. Appelman2024 (long-COVID muscle) shows reduced OXPHOS at baseline that *worsens* after PEM with a selective post-exertional fall in succinate-dehydrogenase activity, and Wang2023 supplies a candidate primary molecular lesion (ER-stress-induced WASF3 blocking respiratory-supercomplex assembly → ~50% lower Complex IV → glycolytic shift).
- **New compartment + oxidative-stress evidence (2026-06-20 PDF batch):** the bioenergetic lesion is now documented across additional compartments. **Muscle:** Scheibenbogen2024 frames ME/CFS as an "acquired ischemic mitochondrial myopathy" (hypoperfusion → Na⁺/Ca²⁺ overload → mitochondrial damage), extending the Appelman2024 muscle finding into a vascular-bioenergetic vicious-cycle model. **CNS:** Baraniuk2025 finds a CSF serine-folate one-carbon block with a *blunted/inverted* metabolite response to submaximal exercise — a central-compartment correlate of provoked metabolic incompetence. **Mechanism review:** Syed2025 (NIH/Hwang lab, the WASF3 group) surveys the evidence and explicitly declines to settle primary-vs-secondary, while endorsing the *provoked* direction as the basis of PEM. **Oxidative-stress axis:** Shankar2025 (PNAS, within-study LC vs ME/CFS head-to-head) adds elevated lymphocyte ROS + reduced mitochondrial ATP + lower SOD2 as a *shared* mechanism, and Saito2024 reports reduced plasma ATP in LC-with-CFS; Huang2024 (UK Biobank NMR, n=1,194) adds a lipoprotein-dominant, sex-specific energy-metabolism signature. None of these resolves the resting set-point discordance below, but they broaden the *provoked/tissue* pole (muscle + CNS) and add oxidative stress as a candidate upstream driver of the mitochondrial deficit.
- **t025 cross-trigger endpoint constraint (2026-06-22; `interpretation:0004`, `proposition:0011`):** the strongest new update is not a new molecular signature but a localization constraint. Keller2014 anchors the ME/CFS whole-body 2-day-CPET decrement; Gattoni2025 finds that this whole-body signature does **not** transfer in a small PEM-enriched long-COVID cohort; Appelman2024 shows long-COVID PEM nevertheless has an objective peripheral-muscle OXPHOS lesion after provocation. Current reading: the provoked bioenergetic deficit is real, but its measurable endpoint is trigger- and compartment-specific. This weakens a "single shared whole-body bioenergetic failure" reading while preserving the possibility of a shared attractor expressed through different tissue/channel readouts.
- **t056 ME/CFS muscle-bioenergetics update (2026-06-25; `interpretation:0019`, `proposition:0030`):** the "no ME/CFS muscle endpoint" premise is too strong. Jones2012 (repeat exercise 31P-MRS) shows excess intramuscular acidosis and delayed pH recovery; Wong1992 shows lower ATP at exhaustion during in-vivo 31P-NMR exercise; Brown2015 shows impaired contraction-stimulated AMPK/glucose uptake in CFS-derived skeletal-muscle cells; Bizjak2024 shows muscle mitochondrial abnormalities in CFS/post-COVID but non-identical phenotypes. This strengthens the provoked/tissue pole for ME/CFS and narrows the remaining cross-trigger gap to endpoint equivalence: no ME/CFS Appelman-type pre/post-PEM muscle OXPHOS/SDH biopsy time-course yet.

## Thoughts

- Best current interpretation: there is credible evidence for a provoked bioenergetic/mitochondrial component to PEM (Che2025, Appelman2024, Keller2014), and PEM is a shared *symptom* across PAIS (Bateman2023), but whether the underlying lesion is biochemically and physiologically exchangeable across triggers is unproven and actively contested (Hanson2023, Gattoni2025, `proposition:0011`).
- Major uncertainty: whether the bioenergetic deficit is a primary mitochondrial defect, a secondary consequence of immune activation/microvascular dysfunction, or both; and whether a provoked exercise-challenge signature replicates across triggers and cohorts.

## Open sub-question (2026-06-20): which direction does the bioenergetic lesion point?

A substantive, unresolved tension runs through the mitochondrial-PEM literature: studies
disagree on the *direction* of the core abnormality.

| Pole | Representative evidence | Compartment / state |
|---|---|---|
| **Resting hypometabolic suppression** | Naviaux2016 (~80% of diagnostic metabolites decreased; conserved "dauer"/torpor framing); McGregor2019 NoPEM group (serum hypoxanthine lowest in the chronically quiescent, non-episode arm — potentially the deepest resting depletion state) | Plasma metabolome, **at rest** |
| **Compensatory hyperactivation / inefficiency** | Missailidis 2020 (isolated Complex V inefficiency with elevated respiration); Peppercorn2023 (direction-discordant analytes vs long COVID); McGregor2019 PEM group (hypermetabolic urinary metabolite excretion during active PEM — emergency mobilization analogous to exercise-induced hypermetabolism) | Lymphocytes/lymphoblasts, at rest; urine during active PEM episode |
| **No resting defect — deficit is provoked only** | Germain2022 (modest resting difference; divergence escalates after exercise, worst in the 24 h recovery window); Walitt2024 (no basal mitochondrial dysfunction in PI-ME/CFS) | Plasma / multi-system, **provoked** |
| **Provoked worsening at the tissue level** | Appelman2024 (muscle OXPHOS reduced at baseline and *worse* after PEM; selective post-PEM SDH/Complex II fall; amyloid is **extravascular**, refuting capillary-occlusion); Jones2012 (ME/CFS repeat-exercise 31P-MRS excess acidosis and delayed pH recovery); Wong1992 (lower ATP at exhaustion); Brown2015 (impaired contraction-stimulated AMPK/glucose uptake in CFS muscle cells); Joseph2023 (invasive CPET: impaired peripheral O₂ *extraction*) | Skeletal muscle / whole-body, provoked or contraction-modeled |

These are **partly reconcilable** as resting-vs-provoked, compartment (blood/lymphocyte vs
muscle), and cohort/sex-composition differences rather than flat contradictions. The most
defensible current reading: the **resting** set-point is genuinely discordant across cohorts
and assays, whereas the **provoked** (post-exertional) state more consistently shows a
*worsening* oxidative/recovery deficit. If so, the diagnostic and mechanistic signal lives in
the provoked state (2-day CPET — Keller2014; invasive CPET — Joseph2023; post-exercise
metabolomic recovery — Germain2022), and a static resting "hypometabolism vs hyperactivation"
framing is the wrong axis. This sub-question should be resolved before any single resting
bioenergetic biomarker is proposed as a PEM endpoint.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (bioenergetic failure as a node in a self-sustaining attractor).
- Required data or analyses: standardized two-day CPET / exercise-challenge studies with paired pre/post multi-omics (metabolomics, proteomics, immune stimulation) across >=2 triggers (long COVID, ME/CFS) with matched recovered controls; pathway-level comparison to test for shared versus trigger-specific bioenergetic signatures.
- Priority level: P2 — central to PEM operationalization and the shared-mechanism question, but depends on demanding provoked-challenge cross-trigger datasets.

`pre-registration:0005` now fixes the strongest version of that required study for the muscle endpoint:
LC + ME/CFS under one exertional protocol with serial muscle biopsy/physiology and central/peripheral
decomposition. Until such a vehicle exists, q0011 remains unresolved for same-lesion cross-trigger
equivalence.

## Related

- Topic notes: `topic:mecfs-long-covid-convergence`, `topic:biomarkers-and-objective-endpoints`, `topic:shared-failure-mode-across-pais`.
- Article notes: Che2025, Bateman2023, Hanson2023, McGregor2019.
- Methods/Datasets: cardiopulmonary exercise testing (CPET, two-day protocols); pre/post-exertion metabolomics and proteomics; ex-vivo immune-stimulation assays.
