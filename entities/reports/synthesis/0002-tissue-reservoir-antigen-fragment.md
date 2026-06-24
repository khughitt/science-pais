---
type: synthesis
title: "Synthesis: 0002-tissue-reservoir-antigen-fragment"
report_kind: hypothesis-synthesis
id: synthesis:0002-tissue-reservoir-antigen-fragment
hypothesis: hypothesis:0002-tissue-reservoir-antigen-fragment
generated_at: 2026-06-24T03:28:17Z
source_commit: eb1a5ca60ed1cd69451e2a3d9d6fa16da31fbfec
provenance_coverage: thin
---

## State

`hypothesis:0002-tissue-reservoir-antigen-fragment` is **proposed** and **active** with no resolved interpretations or propositions in the science graph. Its canonical claim — stated in the hypothesis frontmatter and body — is that tissue-resident phagocytes (Kupffer cells, microglia, alveolar macrophages) fail to degrade degradation-resistant pathogen-derived fragments, forming a persistent antigen reservoir that chronically engages innate sensing, suppresses cellular energy metabolism, and seeds downstream PAIS dysregulation.

The strongest direct evidence cited in the hypothesis file is a mouse-plus-human-sample study (McClune2025): Borrelia peptidoglycan (pPG^Bb) persists in liver via Kupffer-cell retention, drives proteome change and PBMC energy-metabolism suppression, and its transcriptomic signature molecularly overlaps the long COVID signature (p = 0.00038). Human plasma antigen persistence is reported for SARS-CoV-2 in roughly 25% of survivors at up to 14 months (Peluso2024, cited in the hypothesis), and a non-viable Coxiella DNA/antigen macrophage-clearance model is invoked for Q-fever (Morroy2016, cited in the hypothesis). All three citations come from the hypothesis file's `source_refs` and body text; none are currently registered as graph propositions or grounded in `.edges.yaml` edges.

The single registered open question is `question:0002-antigen-clearance-rescues-symptoms`: whether clearing persistent antigen rescues post-acute symptoms and thereby establishes antigen persistence as driver rather than epiphenomenon. This question has a claim count of zero, meaning no study in the graph has yet been coded as addressing it.

---

## Arc

Arc reconstruction is limited because this hypothesis has no `prior_interpretations` chains and no linked interpretations or tasks exist in the bundle.

The hypothesis was created on 2026-06-11 and appears to have been seeded in a single authoring pass: the organizing conjecture, proposition bundle, uncertainty notes, predictions, and falsifiability criteria are all present in the hypothesis file without recorded investigative steps preceding them. The framing draws together three source papers across three pathogen classes (Borrelia, SARS-CoV-2, Coxiella) to assert a pathogen-agnostic persistence mechanism, with McClune2025 supplying the mechanistic backbone and Peluso2024 and Morroy2016 offering analogical support.

No interpretation files record how the supporting evidence was evaluated, no tasks have been opened to pursue the predictions, and no graph edges have been encoded. The hypothesis therefore stands at the starting point of its arc: a structured conjecture with grounded source-paper claims and an open decisive-test question (`question:0002-antigen-clearance-rescues-symptoms`), but no analytical work deposited yet.

---

## Research Fronts

**Open question.** The single registered open question under this hypothesis is `question:0002-antigen-clearance-rescues-symptoms` (claim count = 0, no graph neighborhood). It asks whether antiviral or antigen-clearing interventions demonstrably rescue post-acute symptoms, which would shift the persistence association from epiphenomenon to driver. The hypothesis file notes that early antiviral trials in established long COVID have not clearly improved symptoms, weakening the "clearance rescues" corollary, but no study has been formally coded against this question.

**Empirical gaps.** The tissue-macrophage mechanism is directly demonstrated only in a mouse Borrelia model; human tissue evidence is indirect (plasma antigen in Peluso2024; inferential Coxiella model in Morroy2016). No study prospectively links fragment or antigen burden to symptom severity or chronicity onset. Whether SARS-CoV-2, EBV, and Coxiella exploit the same tissue-macrophage sink as Borrelia remains a prediction, not an observation.

**Prioritized experimental fronts** named in the hypothesis file: (1) TLR2-dependence test of fragment-induced metabolic suppression ex vivo; (2) prospective fragment-burden-predicts-chronicity cohort; (3) host clearance-gene (TLR1/TLR2 variant) burden test across PAIS triggers. No tasks have been opened for any of these.
