---
id: "report:0006-bias-audit-deflationary-nulls-vs-shared-attractor"
kind: "report"
title: "Bias Audit: deflationary mechanism-specific nulls (h0015–h0018) scored against the shared-attractor thesis"
status: "draft"
source_refs:
- cite:Peluso2022
- cite:Chen2023
- cite:Hunt2024
- cite:Kell2022
- cite:Stussman2025
- cite:Twomey2020
- cite:Mateu2026
- cite:Altmann2023
related:
- theme:0001-deflationary-nulls-and-biomarker-vs-driver
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais
- hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker
- hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific
- hypothesis:0018-circulating-antigen-as-severity-biomarker-not-driver
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only
- question:0002-antigen-clearance-rescues-symptoms
- question:0049-two-day-cpet-multiomic-pem-assay-across-pais
- question:0054-ebv-reactivation-autoantibody-emergence-temporal-ordering
- task:t104
created: "2026-07-07"
updated: "2026-07-07"
---

# Bias Audit: deflationary mechanism-specific nulls (h0015–h0018) scored against the shared-attractor thesis

## Scope

Task **t104**: score the four 2026-07-06 mechanism-specific deflationary nulls — **h0015** (EBV
reactivation = consequence, not cause), **h0016** (fibrinaloid microclots = non-specific inflammatory
marker), **h0017** (PEM overdiagnosed via self-report), **h0018** (circulating antigen = severity
biomarker) — against the project's shared-attractor thesis (**h0001**), organized by
`theme:0001-deflationary-nulls-and-biomarker-vs-driver`. For each null, record the discriminating test and
the current evidence balance, and flag whether it is a **live threat** or an **already-bounded** null.

The task frames the deflationary wing as itself a bias-mitigation move (steelmanning nulls against the
constructive hypothesis wing h0001–h0009). So this audit has a second, meta object: **is the project
over-committed to the shared-attractor mechanism (confirmation bias), or has it built genuine machinery to
resist that?** — plus the mirror risk of *deflationary* over-commitment.

This is a focused scoring pass, not a whole-project audit; the general cognitive/methodological categories
below are assessed only insofar as they bear on the null-vs-thesis adjudication.

## Null Scoring Table (the t104 deliverable)

| Null | Claim (scoped) | Discriminating test | Test exists? | Current evidence balance | Verdict |
|---|---|---|---|---|---|
| **h0015** | EBV–LC association is downstream of acute severity + global immune activation, not an EBV-specific driver | Severity + immune-activation–**adjusted** association; EBV-vs-autoantibody temporal ordering (`q0054`) | **No** — full-adjustment cohort not done; ordering study not built | **Open/balanced.** Full adjustment never performed (Peluso2022 cross-sectional, severity-confounded); but a real causal route exists (EBV→MS molecular-mimicry precedent) | **LIVE** (both null and rival unproven) |
| **h0016** | Microclots are a generic inflammatory by-product; no LC-specific symptom prediction beyond general inflammation | Standardized-assay case–control vs **≥2 matched non-PAIS inflammatory** conditions + inflammation-adjusted symptom model | **No** — decisive matched-control study absent; assays non-standardized | **Leans deflationary on rigor** — the positive account (Kell2022) rests on case-series + non-standardized assays; Hunt2024 critical review finds the evidence base insufficient; microclots documented in sepsis/DIC/RA | **LIVE** (positive account not rigorously established — but see guardrail: weak positive ≠ confirmed null) |
| **h0017** | Self-reported PEM has low specificity; not a mechanistically discriminating PAIS feature | Objective multi-omic 2-day-CPET PEM assay across PAIS + non-PAIS (`q0049`) — specificity + self-report concordance | **No** — `q0049` assay does not exist (tracked; cf. t103/t100) | **Split.** "No objective basis" reading **already refuted** (Appelman2024 muscle pathology worsens post-PEM; Keller2014 reproducible CPET decrement). Self-report-specificity claim **live**: 67% self-report vs 5.9% objective CPET (Stussman2025); PEM-like in ~33% cancer fatigue (Twomey2020) | **PARTIALLY BOUNDED** (objective basis exists; self-report-specificity claim live) |
| **h0018** | *Plasma* antigenemia indexes acute severity, not symptoms (explicitly **not** a claim about tissue-reservoir antigen) | Antigen-clearance RCT (`q0002`) + paired **tissue** (not just plasma) antigen measurement | **No** — `q0002` RCT data-gated (same class as the abrocitinib/JAK trial) | **Plasma-driver reading under genuine threat** — Mateu2026 (blinded 2-yr) dissociates antigenemia from symptom count/type/titer, present in recovered; Altmann2023 adaptive-immunity null. Mixed literature (some cohorts report associations). Tissue-reservoir (h0002) correctly untouched | **LIVE + well-scoped** (strong on plasma; silent on tissue by design) |

**Bottom line:** all four nulls are **LIVE**, and **none is currently adjudicable** — every discriminating
test is prospective or data-gated, exactly like the rest of the project's decisive tests (abrocitinib, UKB,
q0002). The audit's present value is the *lean*, not a verdict: h0017's "no objective basis" strong form is
already dead; h0018's plasma claim currently has empirical support; h0016 leans deflationary only on the
*weakness of the positive account* (not on positive null evidence); h0015 is genuinely balanced.

## Convergence finding (answers the theme's open question)

`theme:0001` asks whether the mechanism-specific nulls **converge on a single deflationary reading or
fragment**. They do **both**:

- **By null-*structure* they fragment** — h0015 is reverse-causation, h0016 is non-specificity, h0017 is
  measurement/ascertainment, h0018 is severity-biomarker. The theme's guardrail against "collapsing layers"
  is correct: they have distinct discriminating tests and must not be lumped.
- **By deep *content* three of four converge on one axis** — h0015 (EBV = severity/immune-disruption
  readout), h0017 (self-reported PEM tracks general symptom burden), and h0018 (antigen = acute-severity
  index) all reduce to **"the marker indexes acute severity / global immune disruption rather than a
  specific chronic driver."** That is the same claim as **h0011** (severity predicts only objective organ
  sequelae, not chronic fatigue) and the **h0008** measurement-channel thesis. **Recommendation:** record
  this shared "severity-index confound" axis explicitly linking h0015/h0017/h0018 → h0011/h0008 — it is a
  genuine synthesis the per-null files miss. (h0016 is the outlier: pure non-specificity, no severity axis.)

## Cognitive Biases

### Confirmation Bias

- **Rating:** possible — but **strongly mitigated by design**
- **Evidence:** The project has built unusual institutional machinery *against* confirmation bias toward
  h0001: `q0017` tracks five deflationary accounts **with counter-evidence attached**; `theme:0001`
  elevates the null-first discipline to a first-class organizing frame; h0010–h0018 instantiate
  mechanism-specific nulls; and `pre-registration:0002` pre-commits an **asymmetry** so an underpowered
  null (t035) cannot masquerade as support for the deflationary account. The honest standing position —
  "convergence is supported at pathway level, not shared molecules — consistent with *both* a real attractor
  *and* coincidence-of-repertoire" — is the opposite of a confirmation-biased read. This is a genuine, not
  performative, mitigation. Residual risk is the **mirror**: over-committing to the *deflationary* side (see
  Sunk Cost / guardrail below), and the **author-independence** limit (see Author Independence).

### Anchoring

- **Rating:** not detected
- **Evidence:** The framing has *shifted* materially rather than anchoring: h0001 was reframed 2026-07-01
  from "single shared attractor" to "persistent immune-state displacement, degenerately realized," and the
  deflationary wing (h0010–h0018) was added *after* the positive wing, explicitly to stress it. Movement in
  both directions argues against anchoring on initial assumptions.

### Availability Bias

- **Rating:** possible
- **Evidence:** Discriminating tests cluster on a few familiar designs (severity-adjusted association,
  matched-control comparison, 2-day CPET, clearance RCT). These are the right tools, but note that three of
  four nulls default to the same "adjust for severity / global immune activation" move — reasonable, yet it
  means a single unmeasured-confounding failure (imperfect severity capture) would degrade three
  adjudications at once. Not a bias in claim selection, but a shared methodological dependency to track.

### Sunk Cost

- **Rating:** not detected (positive signal) — with one watch-item
- **Evidence:** No hypothesis is being pursued against its evidence; the nulls exist precisely to prevent
  sunk-cost commitment to h0001. Watch-item (mirror form): **h0016** currently "leans deflationary" largely
  because the *positive* account is methodologically weak (Hunt2024). The theme's own guardrail — "absence
  of a positive signal is not evidence for the null" — must be applied symmetrically: *weak positive
  evidence is not positive null evidence.* Do not let Hunt2024's "insufficient evidence" verdict harden into
  "microclots are confirmed non-specific."

### Process Bias

- **Rating:** likely (structural, not specific to this audit)
- **Evidence:** `git log` shows a **single contributor** (Keith Hughitt) and rapid single-analyst iteration
  (7 commits in ~14h; the entire h0010–h0018 wing authored in one 2026-07-06 pass). No external human review
  and effectively no cooling-off between generation and scoring. The deflationary structure partly
  substitutes for perspective diversity — but a same-session, same-model null-and-audit loop is *simulated*
  adversarialism, not independent review (see Author Independence).

## Methodological Biases

### Selection Bias

- **Rating:** not detected
- **Evidence:** Each null cites its strongest *disputing* evidence in-file (h0015: EBV→MS mimicry; h0016:
  Kell2022; h0017: Appelman2024/Keller2014; h0018: tissue-reservoir + associating cohorts). Inclusion of the
  rival's best case inside each null is the correct anti-selection discipline and is consistently applied.

### Survivorship Bias

- **Rating:** not detected
- **Evidence:** Null results are explicitly retained and even privileged (Altmann2023 null; the t035
  non-arbitrating null is logged as "cannot adjudicate," not discarded). The project records failed/negative
  designs rather than only surviving positives.

### HARKing

- **Rating:** not detected
- **Evidence:** The nulls are stated as *predictions with pre-specified falsifiers* before their
  discriminating data exist (all tests are prospective/data-gated), which is the anti-HARKing posture.
  `pre-registration:0002` pre-commits the null-scoring asymmetry. No pre-registration exists yet for the four
  specific adjudicating tests (q0002 RCT readout, q0049 assay, EBV full-adjustment, matched-control
  microclot) — a **pre-registration opportunity** when any becomes runnable, not a current violation.

### Multiple Comparisons / p-hacking Risk

- **Rating:** not applicable (no analyses run in this pass)
- **Evidence:** This is a literature-scoring pass; no statistical tests executed. Flag forward: when the
  severity-adjusted EBV and inflammation-adjusted microclot models *are* run, they carry researcher-degrees-
  of-freedom in the adjustment set (what counts as "global immune activation") — pre-specify those.

### Confounding

- **Rating:** possible (it is the *subject* of three nulls, not a flaw in them)
- **Evidence:** Acute-severity confounding is the explicit mechanism h0015/h0017/h0018 invoke. The risk is
  in the *adjudication*, not the hypotheses: "adjust for acute severity" is only as good as severity capture,
  and over-adjustment (severity as a mediator, not just confounder, on the causal-driver reading) can induce
  collider bias — the same structural trap the autoimmune-diathesis line hit (utilisation as dual-role
  confounder/mediator, interpretation:0035).

#### Confound Severity Matrix

| Confound | Severity | Fixability | Mitigation |
|---|---|---|---|
| Acute-severity mis/under-capture degrading the "adjust for severity" test (h0015/h0017/h0018) | HIGH | HARD | Pre-specify severity operationalization; report adjusted **and** unadjusted; treat severity as potential mediator (do not naively condition on the causal-driver reading) |
| "Global immune activation" adjustment set is analyst-defined (h0015) | MED | EASY | Pre-register the marker panel before the association model |
| Assay non-standardization inflating/deflating microclot signal (h0016) | HIGH | HARD | Blinded, standardized quantification is *part of* the discriminating test, not a covariate |
| CPET insensitivity mistaken for absent PEM (h0017) | MED | HARD | Use the q0049 multi-omic assay, not CPET alone; report assay sensitivity bounds |
| Plasma–tissue antigen conflation (h0018) | MED | HARD | Pair plasma with tissue measurement; hold the null to *plasma* scope (already done in-file) |

### Publication Bias

- **Rating:** possible
- **Evidence:** The nulls lean on high-visibility critical/null papers (Hunt2024, Mateu2026, Stussman2025,
  Altmann2023). These are the *correct* external anchors and partly satisfy corpus independence (below), but
  a contrarian pass can itself over-weight prominent skeptical papers just as a positive pass over-weights
  prominent positive ones. Balance is currently good (each null carries its disputing evidence); keep watch
  that "skeptical and well-cited" does not become its own availability shortcut.

### Agent Discovery Failure Traps

- **Rating:** possible
- **Evidence:** **No external grounding** is partly triggered — the four discriminating experiments do not
  exist, so every verdict rests on existing literature + internal reasoning; no benchmark or dataset can
  currently falsify any null. **Hard-question opt-out** is *avoided* (the nulls decompose the hard
  "is it real?" question into concrete adjudicating designs and log them as blockers rather than skipping).
  **Gene-set/label credulity** and **tail-hiding metrics** — not applicable (no analysis). The live trap is
  the first one: treating a literature-scored lean as an adjudication.

### Corpus Independence (Closure Check)

- **Rating:** possible (partially satisfied)
- **Artifacts under audit:** h0015, h0016, h0017, h0018, scored against h0001 / q0017.
- **Shared corpus:** overlapping PAIS literature — e.g. Peluso2022 anchors both the EBV *association* and its
  deflation; Appelman2024 appears in q0017 (against deconditioning) **and** in h0017 (disputing). The
  positive claims and their nulls draw substantially on one corpus.
- **Independent evidence sources:** partially present — each null anchors to an **out-of-positive-corpus**
  critical/null paper (Hunt2024, Mateu2026, Stussman2025, Altmann2023). But the **adjudicating experiments**
  (matched-control microclot, full-adjustment EBV, q0049 objective PEM, q0002 RCT) **do not yet exist**, so
  no held-out dataset can currently disconfirm any null.
- **Verdict:** Not HIGH-severity (external null-anchors give partial independence), but the audit **cannot
  falsify** any null by construction right now — it can only score leans. **Downgrade this audit's status
  from "adjudication" to "internally-consistent scoring."** The out-of-corpus benchmarks are the four
  prospective tests; until one lands, the nulls stay "internally consistent," not "validated/refuted."

### Author Independence (Self-Audit Check)

- **Rating:** likely (honest limitation)
- **Audit author = artifact author?:** Effectively yes. h0015–h0018 were authored by
  `explore-ideas:claude-opus-4-8`; this audit is run by the same model family in the same project lineage.
  The "adversarial" deflationary wing and the thesis it stresses were generated by the **same reasoning
  source**, and this scoring is one more step in that lineage.
- **Verdict:** Register as **"self-audit (internally consistent)"**, not "externally audited." The
  deflationary machinery is genuine and well-structured, but same-model null-generation is *simulated*
  adversarialism — it cannot substitute for an independent perspective. Recommend an out-of-lineage pass
  before any null's verdict is treated as externally validated: an independent reviewer, a different model,
  or (for the whole-thesis question) `/science:compare-hypotheses` run h0001 vs the deflationary bundle with
  the corpus split.

## Summary

- **Overall threat level (is the project confirmation-biased toward h0001?):** **LOW.** The deflationary
  machinery is real, applied, and well-guarded; the project's honest standing position explicitly refuses to
  read weak convergence as support. The genuine residual threats are not confirmation bias toward h0001 but:
  (1) **author/corpus independence** — the nulls, thesis, and this audit share a reasoning lineage and much
  of a corpus, so the audit scores leans but cannot falsify; (2) **all four discriminating tests are
  prospective** — nothing is adjudicable now; (3) the **mirror trap** — letting a weak positive account
  (h0016) or an underpowered null harden into confirmed deflation.
- **Top mitigations:**
  1. **Record the shared "severity-index confound" axis** linking h0015/h0017/h0018 → h0011/h0008 — the
     strongest synthesis this pass surfaced, currently unrepresented.
  2. **Downgrade verdicts to "internally-consistent scoring" and schedule an independent pass**
     (`/science:compare-hypotheses` h0001 vs the deflationary bundle, or an out-of-lineage reviewer) — the
     self-audit/corpus-closure limit.
  3. **Apply the guardrail symmetrically to h0016** — "weak positive evidence ≠ positive null evidence";
     hold it at "positive account not yet rigorously established," not "non-specificity confirmed."
- **Recommended next actions:**
  - Note h0017's "no objective basis" strong form as **already refuted** (Appelman2024/Keller2014) in the
    file's scoring — the live claim is narrowly self-report specificity.
  - Pre-register the severity/immune-activation adjustment set (h0015) and the standardized microclot assay
    protocol (h0016) *before* those data are touched, to pre-empt the researcher-degrees-of-freedom flagged
    in the confound matrix.
  - Keep each null at its exact scope (h0018 plasma-only; h0017 self-report-only) — currently done well;
    the risk is drift under summary pressure.
  - Treat the four adjudicating tests as the out-of-corpus benchmarks; surface any that becomes runnable
    (q0002 RCT readout, q0049 assay) as a promotion/retirement trigger per `theme:0001`'s Update Triggers.
