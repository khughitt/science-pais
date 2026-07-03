---
title: 'Data-catalog expansion & open-data harvest — design'
status: draft-for-review
created: '2026-07-03'
updated: '2026-07-03'
see_also:
- decision:D-004
- decision:D-003
- task:t082
- hypothesis:0008-measurement-channel-and-ascertainment-bias
---

<!-- Non-entity design doc under doc/plans/. If graph-integration is wanted, promote
     to a typed entities/plans/ entry; until then it carries no `type:` so
     `science validate` does not treat it as a mis-homed plan entity. -->

# Data-catalog expansion & open-data harvest — design (DRAFT FOR REVIEW)

> **Status:** Design approved in principle (balanced phased program; lightweight
> connect-first machinery). Nothing here is implemented; no dataset entities were
> written, ingested, or linked. This awaits spec review before moving to an
> implementation plan. Adapted from the sibling multiple-myeloma effort
> (`~/d/cancer/cancer-types/multiple-myeloma/doc/plans/2026-07-02-data-catalog-expansion-design.md`),
> whose premise the PAIS grounding scan **inverts** (see §2).

## 1. Motivation (from the user)

The project keeps hitting walls where the deciding evidence sits behind gated data
(controlled-access population-scale EHR, credentialed cohorts, enclave-only
compute). `~/d/science` deliberately favors open, low-friction, third-party-
reproducible data. Rather than pay the gating tax, ask: **how much more can we do
with open data we already have or have not yet pulled in?** Widen the net (missing
PAIS cohorts; under-used modalities; genetic instruments; epidemiology/time;
pan-disease contrast; healthy-recovered references), and capture what we learn into
`~/d/science-commons` so sibling projects benefit.

## 2. What the terrain shows (grounding scan, 2026-07-03)

The scan **inverts the myeloma premise**. Numbers from a survey of
`entities/datasets/` (21 files), `entities/hypotheses/` (9), `entities/questions/`
(22), `core/decisions.md`, and `science.yaml`.

| | Multiple myeloma | **PAIS** |
|---|---|---|
| Catalog size | 255 dataset entities | **21** |
| Modality spread | near-monomodal (bulk RNA) | genuinely multi-modal, multi-disease |
| Binding constraint | **staging** (cataloged→runnable); gating ≈ irrelevant (5/255) | **gating on the highest-value questions**, plus a disconnected graph |
| Right reframe | "convert cataloged→runnable" | **"find open data that does the job the gated data can't"** |

Three findings reshape the premise:

**(a) Gating is shelving the sharpest questions.** Decision **D-004** (2026-07-01)
shelved the autoimmune × sex × PASC effect-modifier line because its binding gate
(BC-4: rare-stratum × sex power) needs population-scale *individual-level* EHR.
N3C is gated **and non-downloadable even at the synthetic tier** (enclave-only
Palantir compute); OpenSAFELY carries the same real-data gating (federated
code-to-data, only SDC aggregates leave) despite open code. Neither can produce
**third-party-reproducible** knowledge under `science.yaml`'s
`reproducibility_policy` (`bar: third-party-reproducible`, `unknown: halt`,
`below_bar: halt`), so the line was **shelved, not run**. The menopause line (t028)
is separately blocked on **UK Biobank** provisioning. These are not peripheral —
they are h0005, h0007, h0009, and q0007/q0013/q0019–q0022.

**(b) There is an open substitute the myeloma project never had.** **Open GWAS
summary statistics + Mendelian randomization.** Autoimmune-disease GWAS, HLA
associations, sex-hormone GWAS (SHBG, testosterone), and long-COVID GWAS
(COVID-19 HGI, GWAS Catalog, Open Targets, IEU OpenGWAS) are *fully public and
third-party-reproducible*. MR on summary statistics can attack reverse-causation
and sex-effect-modification — the exact things the shelved EHR work was for —
**without any enclave**. This is a genuine open vehicle for the shelved arm and
directly serves the genetic-autoimmune question.

**(c) The catalog is structurally disconnected.** There are **zero `dataset:` edges**
from any hypothesis or question — every dataset link is prose-only. So unlike MM
(where `prioritize --coverage` drove everything), a coverage scan is not yet
meaningful. A **connect** step is load-bearing here in a way it was not for MM.

Plus the genuinely thin links: **h0006** cites RECOVER only (single dataset);
**h0002/h0003** cite two datasets each; **h0007/h0008/h0009** cite **zero**.

**Reframe:** this is a genuine *discovery-and-connect* problem (not MM's *staging*
problem), with a distinctive high-payoff move — **open GWAS/MR + open epidemiology
as substitutes for the shelved gated-EHR arm** — that MM's cancer context did not
afford.

## 3. Tooling we build on (no new invention required)

The gap-driven arc already exists as `science:catalog-datasets`
(gap-scan → discover → verify → connect → prioritize → handoff), driven by the
`science dataset` CLI. Key surfaces:

- `science dataset prioritize --coverage` — the gap scan. **Only meaningful after
  Gate-0 connect (§4)**, since it needs `dataset:` edges to score coverage.
- `science dataset link <dataset> <target>` — wire datasets to Q/H (the Gate-0 tool).
- `science dataset verify-access` — sets origin/license/access metadata; the entry
  gate that feeds the reproducibility classification.
- `science dataset list [--include-gated]` — the entity lifecycle view.
- `/science:find-datasets` and `/science:catalog-datasets` — the discovery workers
  (LLM candidates + adapter search via `science datasets search`), **never yet run
  in this project**; the current 21-entity corpus was hand-authored from the
  literature `entities/searches/` and classified by t087.
- Commons: `science commons promote dataset --slug <slug>` once class-appropriate
  verification is done; project-local context stays in `overlays/datasets/<slug>.md`.

**Adapters that exist (discovery convenience, not a prerequisite):** GEO,
cBioPortal, ArrayExpress, SRA, Zenodo, Dryad, figshare, PhysioNet, Semantic Scholar.
These cover much Wave-2 modality work (GEO/ArrayExpress transcriptomics, PhysioNet
wearables, Zenodo/Dryad supplements). **GWAS/epidemiology/metabolomics sources have
no adapter** (GWAS Catalog, IEU OpenGWAS, Open Targets, MetaboLights/Metabolomics
Workbench, VEuPathDB/ClinEpiDB, Our-World-in-Data-style surveillance). Per the
myeloma demand-gated rule, the remedy is chosen by friction pattern:

- **one-off accession import** — a single known accession, no repeated search
  (most Wave-1 GWAS leads: HGI, a named autoimmune GWAS);
- **adapter** — repeated *search/discovery* friction across many accessions
  (IEU OpenGWAS and GWAS Catalog are the likeliest to eventually qualify);
- **ingestion recipe** — friction is in *staging/parsing*, not discovery
  (metabolomics matrices, surveillance time-series).

Decide per source in Wave 3 from the *actual* logged friction, not speculatively.

## 4. Proposed program — balanced, phased, open-data-first

User decisions locked at design time: **balanced phased program** (all three aims,
in waves; the ordering below is the recommendation the user delegated) and
**lightweight connect-first machinery** (no custom ledger/validator code — the
22-question corpus is hand-triageable; the myeloma YAML-ledger + Python validator
was justified by 185 Q/H targets and does not pay for itself at 1/12th the size).

### Gate-0 — Connect (before Wave 1; independently correct)

Author the missing `dataset:` edges from the 9 hypotheses + 22 questions to the 21
existing datasets via `science dataset link`, so `prioritize --coverage` produces a
real gap list. This is the PAIS-specific prerequisite MM did not need — it *creates*
the graph rather than cleaning it. Output: a coverage baseline, triaged **by hand
into a triage table appended to this doc** (or a sibling `doc/plans/` note if it
grows large) — no ledger code. Gate-0 is the recommended pilot:
it is lossless, independently useful, and shakes out the arc before any discovery.

### Wave 1 — Open substitutes for the gated arm

Lead wave: highest payoff, reopens the D-004 / t028 walls with reproducible data.
Discovery + verify + connect + **handoff** (no analysis — see §6):

| Class | Open-substitute discovery target | Serves |
|---|---|---|
| Sex × autoimmune causal identification | Autoimmune-disease GWAS, HLA associations, sex-hormone (SHBG/testosterone) GWAS, long-COVID GWAS (COVID-19 HGI) — MR-capable summary stats | h0005, h0007, h0009, q0007/q0013/q0019–q0022 |
| Infection / vaccination / PAIS dynamics | Open epidemiology + surveillance: variant-emergence timelines, vaccine-rollout timing, wastewater/case time-series, symptom-plus-time cohorts | h0004, **h0008** (measurement/ascertainment) |

MR/epidemiology are the two genetic/temporal modalities entirely absent from the
current catalog. **h0008** (the durable methodological residue of the shelved N3C
line) gains its first dataset citations here from open surveillance/ascertainment
data — a non-mechanistic (bias) hypothesis finally getting an open vehicle.

### Wave 2 — Thin-link repair + modality breadth

For each tenuous hypothesis, find ≥1 reproducible dataset so no belief rests on a
single cohort; fill under-used modalities:

| Target | Discovery aim |
|---|---|
| h0006 (RECOVER only) | Open muscle/exercise-physiology or PEM datasets (e.g. two-day CPET, muscle biopsy transcriptomics in ME/CFS) |
| h0002 / h0003 (two datasets) | Open immune-exhaustion / antigen-persistence transcriptomics or proteomics cohorts |
| h0007 (zero) | Open small-fiber-neuropathy / autonomic datasets (subject to t050 vehicle gating) |
| Modality breadth | Metabolomics (MetaboLights/Workbench), gut microbiome (SRA/ENA + curatedMetagenomicData), wearables/actigraphy (PhysioNet), Olink/proteomics |
| **Healthy-recovered reference** | Cohorts with a **recovered-control** arm — what "healthy post-COVID" looks like (open convalescent cohorts, recovered arms of longitudinal studies) |

### Wave 3 — Pan-disease contrast + commons capture + demand-gated adapters

- **Pan-disease / attractor-like contrast:** sepsis/PICS, post-treatment autoimmune
  states, and other persistent "attractor-like" phenotypes as **read-across per
  D-003** (stress-test h0001's shared-attractor claim; not counted as PAIS evidence
  without a stated bridge — see §5). Coordinate with `pan-disease` and the sibling
  `health-immunity` / `health-cycles` processes.
- **Commons capture:** promote reusable, verified datasets to `~/d/science-commons`
  (entity + datapackage + recipe); keep PAIS-local context in `overlays/datasets/`.
  Opportunistic throughout, consolidated here.
- **Adapters:** build one **only** for a source that proved load-bearing across ≥2
  gaps in Waves 1–2 (IEU OpenGWAS / GWAS Catalog are the leading candidates).

**Wave-1 hard checkpoint.** After the Wave-1 handoffs land, rerun
`prioritize --coverage`, record the coverage delta, and **only then** decide whether
Waves 2–3 proceed as scoped. If Wave 1 already lifts the blocked clusters, later
waves may shrink or re-weight.

## 5. Gates (reuse, don't reinvent)

- **Reproducibility gate (native).** Every new entry is classified under the
  existing `science.yaml` `reproducibility_policy`; `unknown` / `below-bar` → **halt**
  (do not catalog as usable). This is *why* Wave 1 leads with open GWAS/epi: they
  clear the `third-party-reproducible` bar the gated EHR cannot. PAIS already has
  this native gate, so no myeloma-style ad-hoc transportability ledger is built.
- **Read-across gate (D-003).** Non-PAIS-disease data (sepsis, autoimmune GWAS not
  drawn from a PAIS cohort, pan-disease contrast) enters as **contrast / boundary-
  monitor read-across per D-003**. It may *stress-test or contextualize* h0001, but
  may **not** be counted as PAIS evidence without a stated bridge assumption (what
  must hold for the non-PAIS result to transport to the post-infectious context).

## 6. Boundaries / non-goals (YAGNI)

- **Front-half only.** This effort ends at the `/science:plan-pipeline` handoff.
  Running Mendelian randomization, ingesting cohorts, or any analysis is
  **downstream and gated by t082** (the "no primary computational pipelines until
  past seed-stage" scope boundary). Wave descriptions list *handoff targets*, not
  staging or analysis work.
  - *Note:* a fully-open, low-friction MR vehicle is a clean candidate to **help
    resolve t082** (it is the cheapest possible reproducible analysis), but that is
    a separate decision, not assumed here.
- **Not re-cataloging the shelved gated EHR** (N3C / OpenSAFELY) — D-004 stands;
  revisit only if a downloadable de-identified individual-level or truly-open
  synthetic tier appears. UK Biobank remains a separate live credentialed vehicle
  (t028), not re-litigated here.
- **No ledger/validator code** (user decision): triage is hand-done in this design's
  companion notes; escalate to a structured ledger only if the gap list proves
  unmanageable.
- **No speculative adapters** — only post-hoc, demand-gated on logged friction (§3).
- This plan lives in `doc/plans/`; promote to a typed `entities/plans/` entry only
  if graph-integration is wanted later.

## 7. Mapping to the user's questions (coverage check)

| User question | Where addressed |
|---|---|
| Other PAIS datasets we're missing? | Wave 2 (thin-link repair) |
| Other disease datasets w/ persistent "attractor-like" phenotype? | Wave 3 (pan-disease contrast) |
| Under-utilized modalities? | Wave 1 (genetics, epidemiology) + Wave 2 (metabolomics, microbiome, wearables) |
| Datasets to test **alternative (non-PAIS)** hypotheses? | Wave 1 (h0008 measurement/ascertainment bias via open surveillance) |
| What "healthy post-COVID" looks like? | Wave 2 (recovered-control reference cohorts) |
| Genetic contributions to autoimmune response? | Wave 1 (GWAS/MR — the flagship) |
| Disentangle infection / vaccination / PAIS dynamics? | Wave 1 (epidemiology + time-series, variant/vaccine timing) |
| Pan-disease similarity to PAIS agents? | Wave 3 (pan-disease read-across) |
| What repos/sources; build adapters? | §3 (source list + demand-gated adapter rule) |
| Tenuous single-dataset links? | Gate-0 (surfaces them) + Wave 2 (repairs them) |
| Other health processes besides PAIS? | Wave 3 (commons capture seeds `health-immunity`, `health-cycles`, `pan-disease`) |

## 8. First concrete step (on approval)

Run **Gate-0 connect** as the pilot: author the `dataset:` edges, capture the first
`prioritize --coverage` baseline, and hand-triage the gap list into the triage
table (§4 Gate-0). Then a **Wave-1 discovery pilot on the GWAS/MR vehicle** — the
single highest-leverage open substitute — through the full arc (find → verify →
connect → handoff). That exercises the end-to-end arc on the highest-payoff item
before committing to the wider program, and produces the Wave-1 checkpoint delta.
