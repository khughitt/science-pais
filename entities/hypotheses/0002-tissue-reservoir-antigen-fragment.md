---
id: hypothesis:0002-tissue-reservoir-antigen-fragment
type: hypothesis
title: A persisting pathogen-fragment reservoir in tissue-resident macrophages is
  a pathogen-agnostic initiator of chronic post-infectious illness
status: proposed
phase: active
source_refs:
- cite:McClune2025
- cite:Peluso2024
- cite:Morroy2016
related:
- topic:antigen-pathogen-persistence
- topic:shared-failure-mode-across-pais
- question:0002-antigen-clearance-rescues-symptoms
- discussion:0003-antigen-persistence-treatable-vs-fixed
- immunity:research-question:immune-homeostasis-and-dysregulation
- proposition:0020-antigen-clearance-rescues-established-pais
- proposition:0021-acute-antigen-burden-determines-pais-incidence
- interpretation:0011-t046-antigen-clearance-trials-ingestion
created: '2026-06-11'
updated: '2026-06-24'
---
# Hypothesis: A persisting pathogen-fragment reservoir in tissue-resident macrophages is a pathogen-agnostic initiator of chronic post-infectious illness

## Organizing Conjecture

A common *initiating* lesion across diverse PAIS is the failure of tissue-resident phagocytes (Kupffer cells, microglia, alveolar/other macrophages) to fully degrade pathogen-derived fragments that have unusual, degradation-resistant chemistry. The retained fragments form a persistent antigen reservoir that chronically engages innate sensing (e.g. TLR2 for peptidoglycan), suppresses cellular energy metabolism, and seeds the downstream dysregulation common to PAIS. Critically, the *duration of macrophage retention* — set by fragment chemistry and host clearance genetics — rather than initial pathogen load, determines who develops chronic illness. This makes antigen-fragment persistence a pathogen-agnostic *seed* that can light the shared attractor of hypothesis 0001 from triggers as different as Borrelia, SARS-CoV-2, and Coxiella.

## Proposition Bundle

### Core Propositions

- Degradation-resistant pathogen fragments persist in tissue after pathogen clearance and are biologically active (alter host proteome, suppress PBMC/cellular energy metabolism) — demonstrated for Borrelia peptidoglycan (McClune2025) and circulating SARS-CoV-2 antigen (Peluso2024).
- The persistence mechanism generalizes across pathogen classes: a structurally analogous "residual non-viable fragment evading clearance" mechanism is proposed for viral (SARS-CoV-2), bacterial (Coxiella), and spirochaetal (Borrelia) triggers (McClune2025, Peluso2024, Morroy2016).
- Retained fragment burden/duration, not initial pathogen load, is the proximal determinant of chronic-illness onset (McClune2025).

### Supporting Or Auxiliary Propositions

- Host polymorphisms in innate clearance/signaling (e.g. TLR1/TLR2) modulate fragment clearance rate and thereby PAIS risk (McClune2025).
- The fragment-driven PBMC transcriptomic signature overlaps the long COVID signature, linking a bacterial trigger to a viral PAIS at the molecular level (McClune2025).

## Current Uncertainty

- The tissue-macrophage reservoir mechanism is directly demonstrated only in a *mouse* Borrelia model (McClune2025); human tissue evidence is indirect (plasma antigen in Peluso2024; immunomodulatory-complex hypothesis in Morroy2016 is inferential).
- No study links fragment/antigen burden to symptom severity prospectively, and Peluso2024 explicitly declines the symptom test (see `question:0002`).
- Whether SARS-CoV-2, EBV, and Coxiella actually exploit the same Kupffer-cell/tissue-macrophage sink as Borrelia is McClune2025's prediction, not yet observed.
- **The interventional corollary is now formalized and coded (t046, 2026-06-24).** The hypothesis's two testable interventional claims are split into `proposition:0020` (clearing antigen *rescues established disease* — the reversibility reading) and `proposition:0021` (reducing antigen burden *at onset lowers incidence* — the fixed-risk-factor reading). 0020 is weakly disputed but **uninterpretable** (the established-disease trials never engaged the antigen target); 0021's *mechanism-agnostic* "acute intervention → lower incidence" claim is well-supported by metformin prevention RCTs, but its *antigen-specific* reading (the part that credits this hypothesis) is only **weakly/indirectly** supported (metformin's mechanism is antiviral-vs-metabolic ambiguous). Their treatment-null + prevention-positive signature is the empirical basis of the "antigen-as-fixed-risk-factor-at-onset, non-operative once self-sustaining" reconciliation (`discussion:0003`, `interpretation:0011`) — but h0002 stays `contested`, not `well_supported`.

## Predictions

**Strong / discriminating:**

- Other PAIS pathogens (SARS-CoV-2, EBV, Coxiella) will be found to deposit degradation-resistant fragments in tissue-resident macrophages, with liver/tissue proteome changes overlapping the pPG^Bb and long COVID signatures (McClune2025 prediction).
- Within a trigger, prospectively measured fragment-retention level (e.g. r-mAb2G10 ELISA for pPG^Bb at treatment completion) will predict subsequent chronic-illness diagnosis better than initial pathogen load.
- TLR2 (or relevant innate-receptor) blockade will abolish the fragment-induced metabolic suppression in PBMCs ex vivo.
- Host TLR1/TLR2 (and analogous) clearance-pathway variants will be enriched in non-recoverers across multiple PAIS.

**Weaker / corollaries:**

- Plasma/tissue antigen positivity will co-segregate with the type-I-IFN/neutrophil inflammatory PASC endotype (Talla2023 cluster) rather than the non-inflammatory subgroup.

## Falsifiability

Confidence would be materially reduced if:

- Sensitive tissue sampling in non-Borrelia PAIS finds no persisting pathogen fragments in macrophages despite chronic illness.
- Prospective cohorts show fragment/antigen burden does not predict chronicity and does not track symptom severity (a null for `question:0002`).
- Blocking the proposed innate transduction step (TLR2) leaves fragment-induced metabolic suppression intact, breaking the mechanistic chain.
- Antigen-clearing interventions in antigen-positive patients fail to improve symptoms even when administered early.

## Supporting Evidence

- **McClune2025 (empirical-data, mouse + human samples):** pPG^Bb persists in liver post-clearance via Kupffer-cell/hepatocyte retention; drives proteome change, AST/ALT, PBMC energy-metabolism suppression; molecular overlap with long COVID (p=0.00038). Strongest direct support.
- **Peluso2024 (empirical-data):** Simoa detection of persisting SARS-CoV-2 spike/S1/N in ~25% of survivors to 14 months; burden correlates with acute severity.
- **Morroy2016 (literature):** Q-fever immunomodulatory-complex hypothesis — non-viable Coxiella DNA/antigen impairing macrophage clearance.
- Vreeman2025 supplies a complementary persistence-to-damage mechanism (spike → αvβ6 → TGF-β).

## Disputing Evidence

- **Hanson2023:** argues enterovirus *reservoirs* (not macrophage-retained fragments) drive classical ME/CFS, and notes no full enterovirus genomes recovered — a different persistence model and a replication caveat.
- **Established-disease antigen-clearance trials are null** (now coded as `proposition:0020`'s evidence base via `interpretation:0011`): `evidence-line:0053` (Geng2024/STOP-PASC, 15-day NMV/r), `evidence-line:0055` (Peluso2026/outSMART-LC, anti-RBD mAb), with `evidence-line:0054` (Bhattacharjee2026/PAX-LC) showing NMV/r left circulating Spike unchanged. **Crucially these are weak and uninterpretable**, not disconfirming: none demonstrated antigen target-engagement, so — per `discussion:0003` — they **do not refute antigen persistence**. The Borrelia retreatment parallel is now ingested as a consolidated cross-pathogen line, `evidence-line:0060` (Klempner2001, Krupp2003/STOP-LD, Fallon2008, Berende2016/PLEASE) — four PTLDS antibiotic-retreatment RCTs with no durable symptom rescue, none measuring residual Borrelia antigen/peptidoglycan/DNA. This follows the same uninterpretable-null pattern, and arguably *sharper*: antibiotics kill replicating spirochaetes but cannot degrade degradation-resistant non-viable pPG^Bb fragments, so the vehicle is mechanistically incapable of clearing the hypothesized target. (Coded as one weak line, not four — same modality/trigger, not independent refutations — to avoid inflating the dispute on a still-untested claim.) The Coxiella/Q-fever retreatment parallel is not yet ingested.

## Evidence Needed To Shift Belief

- **Most efficient upward:** demonstration in ≥1 non-Borrelia PAIS that pathogen fragments persist in tissue-resident macrophages with an overlapping host signature, plus a prospective fragment-burden-predicts-chronicity result.
- **Most efficient downward:** negative tissue antigen findings in chronically ill patients, or a clean null in `question:0002`.
- **Also useful:** TLR2-dependence test ex vivo; host clearance-gene burden test across PAIS.

## Related Work

- `topic:antigen-pathogen-persistence` — the synthesis topic.
- `question:0002-antigen-clearance-rescues-symptoms` — the decisive interventional test.
- `hypothesis:0001-shared-dysregulated-attractor` — this fragment reservoir is a candidate *seed* of that attractor.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — chronic-antigenic-stimulation biology.
