---
id: synthesis:0001-shared-dysregulated-attractor
type: synthesis
title: "Synthesis: 0001-shared-dysregulated-attractor"
status: "active"
report_kind: hypothesis-synthesis
hypothesis: hypothesis:0001-shared-dysregulated-attractor
generated_at: 2026-06-24T19:16:12Z
source_commit: 05a785bf71096ea8cc4d486b93f3f920a481cd74
created: "2026-06-24"
updated: "2026-06-25"
provenance_coverage: partial
---

## State

`hypothesis:0001-shared-dysregulated-attractor` posits that long COVID, ME/CFS, PTLDS, post-dengue, post-Q-fever fatigue, and related syndromes converge on a single stable dysregulated attractor in immune-autonomic-metabolic space, reachable from many distinct infectious triggers. Status remains `proposed`; primary support derives from narrative and symptom-convergence literature (hypothesis frontmatter: Komaroff2023, Komaroff2025, Trautmann2025, Bai2023) rather than molecularly confirmed mechanism.

Two investigative threads constrain the hypothesis without refuting it. First, `interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating` returned a non-arbitrating null: NES rank-concordance between PI-CFS and Q-fever fatigue was anti-concordant (`rho = -0.563`, `p_perm = 0.949`) uniformly across six pair × database cells (Hallmark, Reactome, GO-BP). Because the test was underpowered (`2` cohorts, `n = 7-10/group`, cross-platform, cross-compartment), it is recorded only as a marginal downward nudge on demonstrability-so-far, not a verdict against the conjecture. Second, `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation` establishes that PEM's objective correlate is trigger- and endpoint-specific: the ME/CFS whole-body two-day CPET decrement (Keller2014) does not transfer to long COVID at that endpoint (Gattoni2025), while long-COVID PEM does carry a peripheral-muscle OXPHOS lesion (Appelman2024). This is formalized as `proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode`. A weak blood-proteome increment (IL1RL1/IL1R2) was added by `interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands` but is severity-unadjusted and held at weak. The organizing conjecture survives; a "single shared bioenergetic lesion" reading does not [@Keller2014; @Gattoni2025; @Appelman2024].

Decisive open tests: `question:0001-shared-molecular-signature-across-triggers` (harmonized ≥3-trigger multi-omics with full-recovery controls) and `question:0008-formalize-vicious-cycle-attractor-model` (bistability/hysteresis/critical-slowing against longitudinal data).

---

## Arc

The hypothesis originated from convergence-of-triggers observations: that symptom overlap across PAIS reflects shared physiology, not a coincidental repertoire of organ-system failures. Initial framing drew on narrative synthesis reviews (Komaroff2023, Komaroff2025, Trautmann2025) and cross-trigger symptom counts (Bai2023), leaving the attractor language qualitative and the deflationary rival (`question:0017-deflationary-alternatives-vs-shared-pathophysiology`) genuinely competitive.

Task `t001` executed the first literature-level cross-pathogen signature review, yielding a working model of "convergent domains, unproven shared molecules" and confirming that no harmonized ≥3-trigger multi-omics with full-recovery controls exists. The residual evidence gap was handed to `t033`, which deep-read Galbraith2011 (confirmed: gene-level negative across EBV/RRV/Q-fever), executed the post-dengue/QFS/post-SARS omics gap search (confirmed true vacuum for post-dengue; QFS partly closed by the Nijmegen cluster), and re-pointed the public-data reanalysis to `t035`.

The first empirical probe, `interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating`, ran against GSE14577 + GSE130353 in June 2026. The pre-registered locked resolution order halted at step 2 (uniform anti-concordance). Per the pre-committed asymmetric reading, status held at `proposed`; the run's concrete contribution was an empirical demonstration that 2-cohort, cross-platform, cross-compartment public data cannot adjudicate.

Concurrently, `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation` found that the within-cohort PEM-stratified molecular comparison does not exist in any accessible PASC cohort, and formalized the three-arm CPET dissociation as `proposition:0011`. `interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands` attempted route (a) toward a severity-adjusted PEM proteome contrast, found it blocked (STOP-PASC/Maestri2025 models severity-unadjusted; individual-level data gated), and added a weak blood-proteome anchor to `proposition:0011`.

Current epistemic position: cross-trigger convergence is supported at symptom and narrative review level; not yet at shared mechanism. The deflationary rival remains genuinely competitive.

---

## Research fronts

**Live questions:**

- `question:0001-shared-molecular-signature-across-triggers` — the decisive unanswered test; no harmonized ≥3-trigger multi-omics with full-recovery controls exists.
- `question:0008-formalize-vicious-cycle-attractor-model` — the attractor claim is qualitative; bistability/hysteresis/critical-slowing not yet tested against longitudinal data.
- `question:0017-deflationary-alternatives-vs-shared-pathophysiology` — coincidence-of-repertoire rival; explicitly not arbitrated by the t035 null.
- `question:0014-which-pais-case-definition-is-most-biologically-coherent` and `question:0015-does-pem-requirement-improve-cross-study-comparability` — upstream of any harmonized cross-trigger design; PEM's status as mechanism vs. severity marker is untested at the molecular level.
- `question:0016-oxidative-stress-upstream-driver-of-bioenergetic` and `question:0011-mitochondrial-basis-of-pem` — candidate loop-maintenance mechanisms, both open.

**Open tasks:**

- `t011` [P3, proposed] — Evaluate four quarantined viral-dynamics ODE papers as mathematical substrate for attractor formalization (`question:0008`).

**Knowledge gaps:** The `topic_gaps` slice for this hypothesis is empty. The `uncertainty_slice` returned no flagged uncertainty nodes specific to this hypothesis.
