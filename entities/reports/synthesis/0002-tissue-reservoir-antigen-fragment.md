---
id: synthesis:0002-tissue-reservoir-antigen-fragment
type: synthesis
title: "Synthesis: 0002-tissue-reservoir-antigen-fragment"
report_kind: hypothesis-synthesis
hypothesis: hypothesis:0002-tissue-reservoir-antigen-fragment
generated_at: 2026-06-24T19:16:12Z
source_commit: 05a785bf71096ea8cc4d486b93f3f920a481cd74
provenance_coverage: thin
---

## State

`hypothesis:0002-tissue-reservoir-antigen-fragment` is **proposed** and **active**, grading **speculative** at
the conjunctive-bundle level. Its canonical claim is that degradation-resistant pathogen-derived fragments
persist in tissue-resident macrophages (Kupffer cells, microglia, alveolar and other macrophages), forming a
reservoir that chronically engages innate sensing (e.g. TLR2), suppresses cellular energy metabolism, and
seeds the downstream dysregulation common across PAIS — pathogen-agnostically. The hypothesis is a
**conjunction** of three core propositions; it caps at the weakest member.

The persistence-and-bioactivity pillar (`proposition:0022`) is the one supported conjunct: Borrelia pPG^Bb
persists in liver via Kupffer-cell retention and suppresses PBMC energy metabolism with molecular overlap to
the long COVID signature (`evidence-line:0058`, McClune2025, moderate) and SARS-CoV-2 spike/S1/N is
detectable in roughly 25% of survivors at up to 14 months (`evidence-line:0059`, Peluso2024, weak). Both
lines evidence persistence only. The two distinctive pillars — cross-pathogen tissue/macrophage-reservoir
generalization (`proposition:0023`) and retained-fragment burden predicting chronicity over initial pathogen
load (`proposition:0024`) — carry **no supporting evidence-lines** (task:t052, 2026-06-24); they grade
speculative and hold the conjunction there.

The graph also surfaces `hypothesis:0002` as **contested**: the evidence signal registers support_count=2,
dispute_count=4. The four disputing lines are concentrated on `proposition:0020` (clearing antigen rescues
established PAIS), which is a **background corollary**, not a core conjunct. Three long-COVID
antigen-clearing RCTs are null on clinical endpoints (`evidence-line:0053` Geng2024/STOP-PASC,
`evidence-line:0054` Bhattacharjee2026/PAX-LC, `evidence-line:0055` Peluso2026/outSMART-LC), and a
consolidated PTLDS antibiotic-retreatment line (`evidence-line:0060`, covering Klempner2001, Krupp2003/STOP-LD,
Fallon2008, Berende2016/PLEASE) adds a bacterial-trigger parallel. Crucially, per
`interpretation:0011-t046-antigen-clearance-trials-ingestion`, **none of these trials demonstrated antigen
target-engagement** — PAX-LC showed NMV/r left circulating Spike unchanged — so they are uninterpretable
nulls, not disconfirmations. The honest contest-signal headline: four weak disputes on a background corollary
via broken tests; the persistence pillar itself is not disputed. The open decisive question is
`question:0002-antigen-clearance-rescues-symptoms`.

---

## Arc

Arc reconstruction is limited because interpretation:0011 carries no `prior_interpretations` chain and the
hypothesis was seeded in a single authoring pass on 2026-06-11 with no earlier interpretation record.

The hypothesis opened on 2026-06-11 as a structured conjecture drawing three source papers (McClune2025,
Peluso2024, Morroy2016) across three pathogen classes (Borrelia, SARS-CoV-2, Coxiella) into a
pathogen-agnostic persistence frame. At creation, `hypothesis:0002` had claim_count=0 — the entire
proposition bundle existed only as prose.

The first major investigative move was task:t046, which formalized the antigen-clearance trial literature as
graph evidence. `interpretation:0011-t046-antigen-clearance-trials-ingestion` (created 2026-06-24) ingested
five trials, coding the established-disease nulls as weak disputes on `proposition:0020` (not core) and the
two metformin prevention RCTs (`evidence-line:0056` Bramante2023/COVID-OUT, `evidence-line:0057`
Bramante2026/ACTIV-6) as weak support on `proposition:0021`. The structural finding was the
treatment-null-plus-prevention-positive pattern: consistent with antigen acting as a fixed risk factor at
onset that becomes non-operative once the chronic self-sustaining state is established — the
"fixed-risk-factor reconciliation" (`discussion:0003`).

The second move was task:t051, which added the Borrelia/PTLDS clearance arm (`evidence-line:0060`) and
decoupled `proposition:0021` from the hypothesis belief-graph to prevent mechanism-agnostic metformin
prevention lines from inflating the antigen-mechanism credit (interpretation:0011 records this correction).

The third move was task:t052 (2026-06-24), which coded h0002's three prose core conjuncts as graph
propositions. This resolved the hypothesis to its current honest state: one supported pillar
(`proposition:0022`), two untested pillars (`proposition:0023`, `proposition:0024`), conjunctive bundle
grades **speculative**. The contested signal on the all-discusses surface is incidental, not load-bearing.

---

## Research Fronts

**Open decisive question.** `question:0002-antigen-clearance-rescues-symptoms` remains unanswered and
precisely characterized: the existing antigen-clearing trials are null but uninterpretable for want of
target-engagement demonstration. Per `interpretation:0011-t046-antigen-clearance-trials-ingestion`, the
missing experiment is an antigen-positive-enriched, clearance-demonstrated, symptom-endpoint trial with a
timing arm (early/transitional versus established disease).

**Open tasks bearing on promotion.** task:t053 (proposed, P3) specifies the two promotion criteria for
moving h0002 out of speculative: (a) a non-Borrelia PAIS tissue-reservoir study demonstrating fragment
retention in tissue-resident macrophages with overlapping host signature — a supporting line on
`proposition:0023`; (b) a prospective cohort showing retained-fragment burden out-predicts initial pathogen
load for chronic-illness onset — a supporting line on `proposition:0024`. Also recorded as a pre-registration
target in the hypothesis file: TLR2-blockade ex vivo (innate-sensing/transduction step).

**Evidential fragility flag.** The graph gaps command returns `evidential_fragility(contested)` for
`hypothesis:0002`, matching the 2-support / 4-dispute signal. The disputed entity also flagged in that
output is `proposition:0020-antigen-clearance-rescues-established-pais`, which rests entirely on
uninterpretable nulls and should not harden to "refuted" absent a clearance-demonstrated trial.
`interpretation:0011` encodes a target-engagement admissibility gate on `question:0002` to prevent future
nulls from being misfiled as disconfirmations.
