---
id: hypothesis:0002-tissue-reservoir-antigen-fragment
kind: hypothesis
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
- proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
- proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization
- proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load
- interpretation:0011-t046-antigen-clearance-trials-ingestion
- interpretation:0017-t053-h0002-promotion-audit
- interpretation:0028-t059-h0002-promotion-vehicle-hunt
- task:t052
- task:t053
- task:t059
created: '2026-06-11'
updated: '2026-06-25'
---
# Hypothesis: A persisting pathogen-fragment reservoir in tissue-resident macrophages is a pathogen-agnostic initiator of chronic post-infectious illness

## Organizing Conjecture

A common *initiating* lesion across diverse PAIS is the failure of tissue-resident phagocytes (Kupffer cells, microglia, alveolar/other macrophages) to fully degrade pathogen-derived fragments that have unusual, degradation-resistant chemistry. The retained fragments form a persistent antigen reservoir that chronically engages innate sensing (e.g. TLR2 for peptidoglycan), suppresses cellular energy metabolism, and seeds the downstream dysregulation common to PAIS. Critically, the *duration of macrophage retention* — set by fragment chemistry and host clearance genetics — rather than initial pathogen load, determines who develops chronic illness. This makes antigen-fragment persistence a pathogen-agnostic *seed* that can light the shared attractor of `hypothesis:0001` from triggers as different as Borrelia, SARS-CoV-2, and Coxiella.

## Proposition Bundle

### Core Propositions

The three core conjuncts are now coded as graph propositions (t052, 2026-06-24). The hypothesis is their
**conjunction** — it is only as strong as its weakest core conjunct — so it grades `speculative` until the
two *untested* pillars accrue evidence, even though the persistence pillar is now well-supported:

- **`proposition:0022` — persistence + bioactivity (SUPPORTED).** Degradation-resistant pathogen fragments
  persist in tissue after clearance and are biologically active (alter host proteome, suppress PBMC/cellular
  energy metabolism) — `evidence-line:0058` (McClune2025, moderate; Borrelia pPG^Bb mouse liver reservoir)
  + `evidence-line:0059` (Peluso2024, weak; SARS-CoV-2 plasma antigen). Grades `well_supported` *as a
  proposition*.
- **`proposition:0023` — cross-pathogen generalization (WEAK PARTIAL SUPPORT).** A structurally analogous
  tissue/macrophage fragment reservoir operates across Borrelia, SARS-CoV-2, and Coxiella-like triggers.
  `evidence-line:0072` (Goh2022) weakly supports the SARS-CoV-2 tissue/macrophage piece in an n=2
  long-COVID tissue case report, but it lacks the controlled host-signature test needed to establish the
  generalization; grades `speculative`.
- **`proposition:0024` — retained burden determines chronicity (UNTESTED / WEAKLY CONTESTED).** Retained
  fragment burden/duration predicts chronic-PAIS onset better than initial pathogen load — no prospective
  burden-vs-load cohort yet exists; no supporting line is coded. `evidence-line:0073`
  (BrandstetterFigueroa2025) weakly disputes the strong version by showing acute N-antigen burden predicts
  9-month long-COVID symptoms; grades `speculative`.

A fourth truth condition — that the innate-sensing/transduction step (e.g. TLR2) causally links fragment
burden to the metabolic/immune dysfunction — remains a **pre-registration target** (see Predictions: the
TLR2-blockade test), deliberately *not* minted as a fourth placeholder proposition since it does not change
the conjunctive grade and is cleaner to formalize when a test is designed.

### Supporting Or Auxiliary Propositions

- Host polymorphisms in innate clearance/signaling (e.g. TLR1/TLR2) modulate fragment clearance rate and thereby PAIS risk (McClune2025).
- The fragment-driven PBMC transcriptomic signature overlaps the long COVID signature, linking a bacterial trigger to a viral PAIS at the molecular level (McClune2025).

## Current Uncertainty

- The tissue-macrophage reservoir mechanism is directly demonstrated only in a *mouse* Borrelia model (McClune2025); human tissue evidence is indirect (plasma antigen in Peluso2024; immunomodulatory-complex hypothesis in Morroy2016 is inferential).
- No study links fragment/antigen burden to symptom severity prospectively, and Peluso2024 explicitly declines the symptom test (see `question:0002`).
- Whether SARS-CoV-2, EBV, and Coxiella actually exploit the same Kupffer-cell/tissue-macrophage sink as Borrelia is McClune2025's prediction, not yet observed.
- **The interventional corollary is now formalized and coded (t046, 2026-06-24).** The hypothesis's two testable interventional claims are split into `proposition:0020` (clearing antigen *rescues established disease* — the reversibility reading) and `proposition:0021` (reducing antigen burden *at onset lowers incidence* — the fixed-risk-factor reading). 0020 is weakly disputed but **uninterpretable** (the established-disease trials never engaged the antigen target) and is coded as a `background` corollary of this hypothesis. 0021's *mechanism-agnostic* "acute intervention → lower incidence" claim is well-supported by metformin prevention RCTs, but its *antigen-specific* reading is only **weakly/indirectly** supported (metformin's mechanism is antiviral-vs-metabolic ambiguous). Their treatment-null + prevention-positive signature is the empirical basis of the "antigen-as-fixed-risk-factor-at-onset, non-operative once self-sustaining" reconciliation (`discussion:0003`, `interpretation:0011`).
- **Belief-graph note (t051 fix, 2026-06-24).** `proposition:0021` is **deliberately not a belief-bearing member of this hypothesis** (it stays in `related:` for navigation but no longer `discusses` h0002). Reason: the hypothesis-belief rollup flattens *every* discussing proposition's evidence-lines into the hypothesis regardless of membership role, so leaving 0021 attached caused its two weak, *mechanism-agnostic* metformin lines to grade h0002 `well_supported (contested)` — over-crediting the antigen mechanism with prevention evidence equally consistent with the metabolic frames (h0001/h0004).
- **Belief-graph note (t052, 2026-06-24) — why h0002 honestly grades `speculative`.** The hypothesis bundle is a **conjunction over its core members** (weakest-link), and it **excludes** background/rival corollaries. t052 coded h0002's three prose core conjuncts as graph propositions: `proposition:0022` (persistence+bioactivity) is now `well_supported`, but `proposition:0023` (cross-pathogen generalization) and `proposition:0024` (retained-burden-determines-chronicity) are coded **with no supporting evidence-line** because they are genuinely untested predictions — so they grade `speculative` and the conjunction caps h0002 at **`speculative`**. This is the honest headline: *one pillar is now supported; the full pathogen-agnostic-initiator hypothesis remains unproven.* Three deliberate choices: (1) coding only the persistence pillar (`{0022}` as sole core) would have made h0002 grade `well_supported`, dishonestly letting "fragments persist" stand in for "initiator hypothesis is supported" — the same over-credit the t051 fix removed, via the bundle path instead of the flatten path; (2) `proposition:0020` (clearing antigen rescues established disease) stays **background, not core** — making it a core conjunct would assert reversibility is a *truth condition* of h0002, which the fixed-risk-factor reconciliation explicitly denies (late clearance can fail without refuting the *initiator* model); (3) a true `supported (contested)` headline is **structurally unreachable** here while any core conjunct is untested — the weakest-link rule caps the magnitude at the weakest pillar. **Promotion path:** a non-Borrelia tissue-reservoir result lifts 0023; a prospective burden-vs-load cohort lifts 0024; together those would carry h0002 toward an honest `supported`. (Note: the all-`discusses` evidence-*signal* surface may still tag h0002 `contested` because 0020's background disputes leak into that path; that tag is incidental — the load-bearing magnitude is the conjunctive bundle grade above.)
- **Belief-graph note (t053/t059, updated 2026-06-26) — promotion audits did not promote.** t053 found the closest
  available non-Borrelia tissue result (`evidence-line:0072`, Goh2022) and coded it as weak partial support
  for 0023, but it is an n=2 case report without controlled prevalence, degradation-resistant chemistry,
  host-signature overlap, or symptom/burden association. t053 also found no prospective retained-burden-
  vs-initial-load cohort for 0024; instead it coded `evidence-line:0073` (BrandstetterFigueroa2025) as weak
  model criticism because acute N-antigen burden predicts 9-month persistent symptoms. t059 re-screened the
  promotion path and found no new admissible vehicle: plasma antigen persistence and generic tissue
  persistence are not enough for 0023 unless they localize a clearance-resistant fragment to a macrophage/
  phagocyte reservoir with host-signature overlap, and no same-subject acute-load vs retained-burden
  prospective cohort exists for 0024. Net: h0002 remains `speculative`; the promotion path is narrower and
  better specified, not discharged.

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

- **McClune2025 (empirical-data, mouse + human samples):** pPG^Bb persists in liver post-clearance via Kupffer-cell/hepatocyte retention; drives proteome change, AST/ALT, PBMC energy-metabolism suppression; molecular overlap with long COVID (p=0.00038). Strongest direct support — now **coded as `evidence-line:0058` (moderate, supports `proposition:0022`)** (t052).
- **Peluso2024 (empirical-data):** Simoa detection of persisting SARS-CoV-2 spike/S1/N in ~25% of survivors to 14 months; burden correlates with acute severity — now **coded as `evidence-line:0059` (weak, supports `proposition:0022`)** (t052). Note both lines support the *persistence* conjunct (0022) only; they do **not** evidence the generalization (0023) or burden-determines-onset (0024) conjuncts, which is why h0002 stays `speculative`.
- **Goh2022 (case report):** SARS-CoV-2 nucleocapsid protein and viral RNA detected in appendix, skin, and
  breast tissue from two long-COVID patients 163 and 426 days after symptom onset, with nucleocapsid
  co-localizing with CD68-positive cells — now **coded as `evidence-line:0072` (weak, supports
  `proposition:0023`)**. This lifts the non-Borrelia tissue/macrophage arm from absent to weakly observed
  but does not establish the cross-pathogen reservoir mechanism.
- **Morroy2016 (literature):** Q-fever immunomodulatory-complex hypothesis — non-viable Coxiella DNA/antigen impairing macrophage clearance.
- Vreeman2025 supplies a complementary persistence-to-damage mechanism (spike → αvβ6 → TGF-β).

## Disputing Evidence

- **Hanson2023:** argues enterovirus *reservoirs* (not macrophage-retained fragments) drive classical ME/CFS, and notes no full enterovirus genomes recovered — a different persistence model and a replication caveat.
- **BrandstetterFigueroa2025 (prospective cohort):** detectable acute plasma SARS-CoV-2 nucleocapsid antigen
  predicts 9-month persistent long-COVID symptoms after adjustment (aOR 3.0, 95% CI 1.1-8.0), now **coded
  as `evidence-line:0073` (weak model criticism, disputes `proposition:0024`)**. Not a direct refutation:
  it lacks retained post-clearance burden measurement, but it keeps initial pathogen burden alive as an
  independent predictor.
- **Established-disease antigen-clearance trials are null** (now coded as `proposition:0020`'s evidence base via `interpretation:0011`): `evidence-line:0053` (Geng2024/STOP-PASC, 15-day NMV/r), `evidence-line:0055` (Peluso2026/outSMART-LC, anti-RBD mAb), with `evidence-line:0054` (Bhattacharjee2026/PAX-LC) showing NMV/r left circulating Spike unchanged. **Crucially these are weak and uninterpretable**, not disconfirming: none demonstrated antigen target-engagement, so — per `discussion:0003` — they **do not refute antigen persistence**. The Borrelia retreatment parallel is now ingested as a consolidated cross-pathogen line, `evidence-line:0060` (Klempner2001, Krupp2003/STOP-LD, Fallon2008, Berende2016/PLEASE) — four PTLDS antibiotic-retreatment RCTs with no durable symptom rescue, none measuring residual Borrelia antigen/peptidoglycan/DNA. This follows the same uninterpretable-null pattern, and arguably *sharper*: antibiotics kill replicating spirochaetes but cannot degrade degradation-resistant non-viable pPG^Bb fragments, so the vehicle is mechanistically incapable of clearing the hypothesized target. (Coded as one weak line, not four — same modality/trigger, not independent refutations — to avoid inflating the dispute on a still-untested claim.) The Coxiella/Q-fever retreatment parallel is not yet ingested.

## Evidence Needed To Shift Belief

- **Most efficient upward:** controlled demonstration in >=1 non-Borrelia PAIS that pathogen fragments
  persist in tissue-resident macrophages with an overlapping host signature, plus a prospective
  fragment-burden-predicts-chronicity result that out-predicts acute load.
- **Most efficient downward:** negative controlled tissue antigen findings in chronically ill patients, a
  prospective retained-burden-vs-initial-load study where acute load out-predicts retained burden, or a
  clean null in `question:0002`.
- **Also useful:** TLR2-dependence test ex vivo; host clearance-gene burden test across PAIS.

## Related Work

- `topic:antigen-pathogen-persistence` — the synthesis topic.
- `question:0002-antigen-clearance-rescues-symptoms` — the decisive interventional test.
- `hypothesis:0001-shared-dysregulated-attractor` — this fragment reservoir is a candidate *seed* of that attractor.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — chronic-antigenic-stimulation biology.
