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
related:
- topic:mecfs-long-covid-convergence
- topic:biomarkers-and-objective-endpoints
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-11'
updated: '2026-06-20'
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

## Thoughts

- Best current interpretation: there is credible evidence for a provoked bioenergetic/mitochondrial component to PEM (Che2025) and PEM is a shared *symptom* across PAIS (Bateman2023), but whether the underlying bioenergetic lesion is biochemically the same across triggers is unproven and actively contested (Hanson2023).
- Major uncertainty: whether the bioenergetic deficit is a primary mitochondrial defect, a secondary consequence of immune activation/microvascular dysfunction, or both; and whether a provoked exercise-challenge signature replicates across triggers and cohorts.

## Open sub-question (2026-06-20): which direction does the bioenergetic lesion point?

A substantive, unresolved tension runs through the mitochondrial-PEM literature: studies
disagree on the *direction* of the core abnormality.

| Pole | Representative evidence | Compartment / state |
|---|---|---|
| **Resting hypometabolic suppression** | Naviaux2016 (~80% of diagnostic metabolites decreased; conserved "dauer"/torpor framing) | Plasma metabolome, **at rest** |
| **Compensatory hyperactivation / inefficiency** | Missailidis 2020 (isolated Complex V inefficiency with elevated respiration); Peppercorn2023 (direction-discordant analytes vs long COVID) | Lymphocytes/lymphoblasts, at rest |
| **No resting defect — deficit is provoked only** | Germain2022 (modest resting difference; divergence escalates after exercise, worst in the 24 h recovery window); Walitt2024 (no basal mitochondrial dysfunction in PI-ME/CFS) | Plasma / multi-system, **provoked** |
| **Provoked worsening at the tissue level** | Appelman2024 (muscle OXPHOS reduced at baseline and *worse* after PEM; selective post-PEM SDH/Complex II fall; amyloid is **extravascular**, refuting capillary-occlusion); Joseph2023 (invasive CPET: impaired peripheral O₂ *extraction*) | Skeletal muscle / whole-body, provoked |

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

## Related

- Topic notes: `topic:mecfs-long-covid-convergence`, `topic:biomarkers-and-objective-endpoints`, `topic:shared-failure-mode-across-pais`.
- Article notes: Che2025, Bateman2023, Hanson2023.
- Methods/Datasets: cardiopulmonary exercise testing (CPET, two-day protocols); pre/post-exertion metabolomics and proteomics; ex-vivo immune-stimulation assays.
