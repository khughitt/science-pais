---
id: interpretation:0011-t046-antigen-clearance-trials-ingestion
type: interpretation
title: 't046 antigen-clearance trials: established-disease clearance null-but-uninterpretable
  (no target engagement); acute-phase prevention positive; together they support the
  fixed-risk-factor-at-onset reconciliation, not refutation of antigen persistence'
status: active
source_refs: &id001 []
related:
- proposition:0020-antigen-clearance-rescues-established-pais
- proposition:0021-acute-antigen-burden-determines-pais-incidence
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- discussion:0003-antigen-persistence-treatable-vs-fixed
created: '2026-06-24'
updated: '2026-06-24'
input: *id001
prior_interpretations: []
relations: []
---

# Interpretation: t046 antigen-clearance trials — established-disease clearance null-but-uninterpretable; acute-phase prevention positive; net = fixed-risk-factor reconciliation, not refutation

## Verdict

**Verdict:** [~] Mixed/structured — three RCTs of antigen-clearing therapy in *established* long COVID
are null on clinical endpoints but **none demonstrated antigen target-engagement** (PAX-LC shows NMV/r
did not move Spike at all), so they only *weakly and uninterpretably* dispute the reversible-target
reading (`proposition:0020`); meanwhile two prevention RCTs show acute-phase metformin lowers PAIS
incidence (`proposition:0021`). The two readings together support the **antigen-as-fixed-risk-factor-at-
onset** reconciliation of `hypothesis:0002` — and explicitly **do not refute antigen persistence**.

## Findings Summary

This is a **formalization** pass (t046): no new papers ingested — the trials were already summarized and
synthesized in `discussion:0003`; this codes them as graph evidence. `hypothesis:0002` had
`claim_count=0`; it now carries two propositions with five evidence-lines.

| Paper | Vehicle | Result | Target engagement? | Line | Stance / strength |
|---|---|---|---|---|---|
| Geng2024 (STOP-PASC) | NMV/r 15d, established LC, n=155 | null primary + all PROMIS | **No** (no baseline stool RNA; no enrichment) | 0053 → 0020 | disputes / weak |
| Bhattacharjee2026 (PAX-LC) | NMV/r 15d immuno substudy, n=82 | null; Spike/Ab/PBMC unchanged | **Demonstrated failure** | 0054 → 0020 | disputes / weak (`model_criticism`) |
| Peluso2026 (outSMART-LC) | AER002 anti-RBD mAb single dose, n=36 | null primary + all secondaries | **No** (no clearance assay; tissue antigen scarce) | 0055 → 0020 | disputes / weak |
| Bramante2023 (COVID-OUT) | metformin acute, prevention, n≈1126 | LC incidence ↓~41% (HR 0.59) | n/a (prevention) | 0056 → 0021 | supports / moderate |
| Bramante2026 (ACTIV-6) | metformin acute, prevention, n=2983 | primary symptom endpoint missed; clinician-dx LC RR 0.50 | n/a (prevention) | 0057 → 0021 | supports / weak |

The decisive structural feature, inherited from `discussion:0003`: **no completed trial both (a)
demonstrated antigen clearance and (b) measured symptom change.** The established-disease nulls therefore
cannot adjudicate `proposition:0020` — they are broken tests of it, not disconfirmations.

## Evidence Quality

- **Independence:** all five are independent cohorts (distinct `independence_group`s). The three
  established-disease nulls also span two mechanistically unrelated clearance modalities (Mpro inhibitor
  ×2, neutralizing mAb ×1), so the null is not an artifact of one drug class. The two prevention positives
  are the same agent (metformin) in two independent trials — replication, not independence of mechanism.
- **Target-engagement axis is load-bearing:** the field's nulls divide into "drug given" vs "antigen
  cleared," and *no trial reached the second*. Bhattacharjee2026 is the proof: NMV/r left circulating
  Spike unchanged. This is why coding the nulls as `disputes` is done at **weak** strength with explicit
  `model_criticism` framing on 0054.
- **All interventional**, but the established-disease set is confounded by absent enrichment (~45–55% of
  participants antigen-negative at baseline) and short courses; the prevention set is confounded by
  mechanism ambiguity (antiviral vs metabolic).
- **`[UNVERIFIED]`/preprint load:** Bhattacharjee2026 and Peluso2026 are medRxiv preprints; both weak
  weightings already reflect this.

## Data Quality Checks

No data-quality concerns in the project graph. One methodological finding is itself a result and is now
encoded (per `discussion:0003`'s P1 follow-up): **a "target-engagement demonstrated?" attribute is the
load-bearing column when cataloguing anti-antigen trials** — without it, the current nulls get misread as
refuting antigen persistence. This is captured in 0054's `model_criticism` role and in `question:0002`.

## Proposition-Level Updates

- **`proposition:0020` (clearance rescues established disease)** — now **weakly disputed but
  mechanistically uninterpretable**. Three independent interventional nulls weigh against it, but every
  one failed to engage the antigen target, so the honest state is "the reversible-target reading has not
  been adequately tested," not "it is false." No supporting line exists. Expect a
  `belief.fragile-single-line`-style thinness flag — appropriate for a claim resting entirely on
  uninterpretable nulls.
- **`proposition:0021` (acute burden determines incidence)** — **moderately supported** by two
  independent prevention RCTs, tempered by (a) ACTIV-6's missed primary symptom endpoint and (b) the
  antigen-vs-metabolic mechanistic ambiguity of metformin. Supports the *fixed-risk-factor* reading
  directionally without proving the lever is antigen specifically.
- **The 0020↔0021 relationship is the epistemic payload:** treatment-null + prevention-positive is
  exactly the signature of antigen acting as a determinant *at onset* that becomes non-operative once the
  chronic self-sustaining state (`hypothesis:0001`) is established. This reconciles the evidence without
  discarding persistence.

## Hypothesis-Level Implications

For **`hypothesis:0002`** (tissue-reservoir antigen-fragment as a pathogen-agnostic initiator):

- It moves from `claim_count=0` (prose-only) to a **formalized, evidenced claim base** — the prose note
  "early antiviral trials have not clearly improved symptoms" is now coded as `evidence-line:0053`–`0055`
  with the crucial target-engagement caveat, exactly as t046 asked.
- The hypothesis is **neither promoted nor weakened**. The clearance nulls do not weaken it (broken
  tests); the prevention positives modestly *strengthen* the burden-at-onset proposition. h0002 stays
  `proposed`/`active`.
- Bhattacharjee2026's NMV/r-fails-to-clear-Spike result actively *favors* a tissue-reservoir / non-
  replicating-antigen model over active bloodstream replication — a small qualitative point in h0002's
  favor.
- **Borrelia/Coxiella clearance arm is unfilled:** the bacterial-trigger parallel (PTLDS antibiotic-
  retreatment nulls — Klempner2001, Krupp2003, Fallon2008, Berende2016/PLEASE) is **not yet in the
  repo**. Its pattern (retreatment does not durably rescue established PTLDS) would be the cross-pathogen
  echo of the LC antiviral nulls and belongs on `proposition:0020`. Flagged as a follow-up rather than
  fabricated here.

## Evidence vs. Open Questions

- **`question:0002` (does clearing antigen rescue symptoms?)** — materially advanced from "asserted, not
  formalized" to **coded and adjudicated as contested-but-untested**: the direct interventional tests
  exist and are null, but are uninterpretable for want of target engagement. The question is *not*
  answered; it is now precisely characterized — the missing experiment is an antigen-positive-enriched,
  clearance-demonstrated, symptom-endpoint trial.
- **`question:0012` (does prevention/antiviral reduce PAIS?)** — strengthened by the metformin prevention
  RCTs, now linked through `proposition:0021`.

## New Questions Raised

1. **Target-engagement as an admissibility gate (highest value).** Any future anti-antigen trial cited on
   `proposition:0020` should be required to demonstrate antigen clearance (plasma *and* tissue, pre/post)
   and to enrich for antigen-positive patients. Worth encoding as a methodological note on `question:0002`
   (parallel to the functional-vs-binding-assay gate added to `question:0009` in t006).
2. **Is metformin's PAIS-prevention antiviral or metabolic?** A prevention trial that measures acute
   viral-load reduction as a mediator would tell us whether `proposition:0021` is truly about *antigen*
   burden or about acute metabolic stress — disambiguating which of h0002 vs h0001/h0004 the prevention
   signal supports.
3. **Ingest the PTLDS antibiotic-retreatment literature** to fill the Borrelia clearance arm of
   `proposition:0020` (cross-pathogen generality of the "late clearance doesn't rescue" pattern).

## Limitations & Residual Uncertainty

- Five papers, all SARS-CoV-2; no bacterial/spirochaetal clearance evidence coded yet (the Borrelia
  parallel is flagged, not ingested). The verdict is robust on the *fault line* (no target engagement in
  established disease; prevention positive) but is not a systematic review of the antiviral-trial
  landscape (e.g. PREVAIL-LC/ensitrelvir, RECOVER-VITAL, Maraviroc/CCR5 trials remain to be tracked).
- Two of three null trials are preprints; the prevention mechanism is ambiguous. Weightings reflect this.
- `proposition:0020` rests entirely on uninterpretable nulls — its disputed status should not harden into
  "refuted" without a clearance-demonstrated trial.

## Updated Priorities

1. **Encode the target-engagement admissibility gate on `question:0002`** (and keep it visible on
   `proposition:0020`) so future nulls are not misfiled as refutations.
2. **Track the decisive trial design** — antigen-positive-enriched + clearance-demonstrated + symptom
   endpoint + a timing arm (early/transition vs established) — as the single experiment that adjudicates
   0020 vs the 0021 fixed-risk-factor reading. (This mirrors `discussion:0003`'s "Evidence Needed.")
3. **Add a follow-up task** to ingest the PTLDS antibiotic-retreatment trials for the Borrelia clearance
   arm of `proposition:0020`.
4. t046 is **complete** (trials formalized and adjudicated); the live gap is now external trial
   availability, not further coding of existing literature.
</content>
