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
> connect-first machinery), then **revised against a pipeline review** (2026-07-03,
> WARN) that corrected the Gate-0 premise (F1), the MR-estimand overclaim (F2), the
> scope gate (F3), and the handoff-artifact shape (F4). Nothing here is implemented;
> no dataset entities were written, ingested, or linked. This awaits final spec
> review before moving to an implementation plan. Adapted from the sibling
> multiple-myeloma effort
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
| Binding constraint | **staging** (cataloged→runnable); gating ≈ irrelevant (5/255) | **gating on the highest-value questions**, plus a capability-blind / sparsely covered graph |
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
and — with sex-stratified sumstats — sex-effect-modification, addressing a *subset*
of what the shelved EHR line was reaching for (a **narrower, different estimand**;
see the Wave-1 estimand rewrite in §4) **without any enclave**. This is a genuine
open vehicle for part of the shelved arm and directly serves the genetic-autoimmune
question.

**(c) The catalog is connected but capability-blind, and mostly uncovered**
*(corrected after the 2026-07-03 review — F1)*. Reach edges already exist on the
**dataset** side (`related:` → Q/H), even though the hypothesis/question bodies cite
datasets only in prose — e.g. `dataset:recover-adult` → q0007/q0013/q0015,
`dataset:gse130353-qfs-cfs-monocytes` → q0001/h0001/q0017,
`dataset:opensafely-longcovid` → h0008/q0007. So `science dataset prioritize
--coverage` **already runs**: of **31** Q/H targets, **9** have ≥1 dataset in reach
and **22** are `no-candidate`. Crucially, the 9 reached targets are **not** scored
runnable — they land on `missing-required-capabilities`, because **no dataset
declares `provided_capabilities` (20 validation warnings) and no reached target
declares `required_capabilities` (9 warnings)**.

So the connectivity blocker is **not** missing edges (my first-draft premise, now
retracted). It is two distinct problems: **(i)** absent capability metadata on the 9
reached targets, and **(ii)** a genuine discovery gap on the 22 `no-candidate`
targets — some of which are merely *unreconciled prose citations* to an existing
dataset (e.g. RECOVER is prose-cited by **h0006** but its `related:` edge is not
wired), and the rest true gaps. The thin-link hypotheses (**h0006**, **h0007**,
**h0009**) sit inside that no-candidate set. Note the review slightly inverted the
mix — the residual is *mostly* `no-candidate` (22) not `missing-capabilities` (9),
so discovery (Waves 1–3) remains warranted alongside the capability fix.

**Reframe:** two coupled problems, not one — **(a)** an *annotate-and-reconcile*
problem on the 9 reached targets (make coverage actionable), and **(b)** a genuine
*discovery* problem on the 22 uncovered targets, with the distinctive high-payoff
move being **open GWAS/MR + open epidemiology as (narrower-estimand) substitutes for
the shelved gated-EHR arm** — a move MM's cancer context did not afford.

## 3. Tooling we build on (no new invention required)

The gap-driven arc already exists as `science:catalog-datasets`
(gap-scan → discover → verify → connect → prioritize → handoff), driven by the
`science dataset` CLI. Key surfaces:

- `science dataset prioritize --coverage` — the gap scan. **Already runs** (edges
  exist, §2c); Gate-0 makes its rows *actionable* by adding capability metadata so
  reached targets resolve past `missing-required-capabilities`.
- `science dataset link <dataset> <target>` — wire datasets to Q/H; in Gate-0 used
  **only** to reconcile prose-only citations to existing datasets, not to blind-link.
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
was justified by a Q/H target corpus an order of magnitude larger and does not
pay for itself at 1/12th the size).

### Gate-0 — Reach & capability audit + baseline coverage (before Wave 1)

*Corrected from a first-draft "create missing edges" framing — the edges already
exist (§2c). Gate-0 is a three-part audit, all metadata authoring (no code,
consistent with the lightweight decision):*

1. **Reconcile** existing `related:` / `datasets:` refs — wire prose-only citations
   that point at a real dataset (e.g. RECOVER → h0006) with `science dataset link`.
   **Do not** blind-link across all 31 targets; only reconcile citations that are
   genuinely reaching.
   > **Correction (Gate-0 execution, 2026-07-03):** the "RECOVER → h0006" example did
   > **not** hold — every "recover" hit in h0006 is the plain-English word, not the
   > RECOVER cohort, and `recover-adult` lacks the muscle/mitochondrial assay to reach
   > h0006 regardless. h0006/h0002/h0003 are genuine-discovery gaps, not reconcilable.
   > See `doc/plans/2026-07-03-wave1-checkpoint.md`.
2. **Annotate capabilities** — add `provided_capabilities` to the 21 datasets and
   `required_capabilities` to the 9 reached targets, clearing the 20 + 9 validation
   warnings so coverage rows resolve to `covered-*` / true-`missing-*` meaningfully.
   **Define a tiny capability vocabulary first** (before touching any record) — if
   the fields are hand-authored ad hoc across 20+9 records, coverage matching gets
   noisy immediately. Proposed controlled fields (a dataset *provides* them, a target
   *requires* them; a target is `covered-runnable` only when the dataset provides a
   superset): **`assay`** (e.g. `bulk-rna`, `gwas-sumstats`, `olink`, `cytof`,
   `metabolomics`, `ehr-coded`, `survey-pro`, `wearable`), **`modality`**
   (`transcriptomics`, `genetics`, `proteomics`, `metabolomics`, `clinical-ehr`,
   `epidemiology`), **`cohort_design`** (`case-control`, `prospective-longitudinal`,
   `cross-sectional`, `summary-stats`, `meta-analysis`), **`trigger`** (`sars-cov-2`,
   `dengue`, `q-fever`, `ebv`, `mixed`, `n/a`), **`case_definition`** (e.g.
   `who-lc`, `cdc-lc`, `fukuda`, `ccc`, `icc`, `n/a`), **`outcome`** (`fatigue`,
   `pem`, `autoimmune-dx`, `dysautonomia`, `recovery-status`), and
   **`stratification`** (`sex`, `age`, `time-since-infection`, `severity`,
   `none`), plus role/trait discriminators so descriptive and causal-MR coverage
   don't collapse — **`analysis_role`** (`mr_exposure`, `mr_outcome`,
   `descriptive_covariate`) and **`trait`** (`long-covid`, `autoimmune-disease`,
   `sex-hormone-biomarker`). The value set is seeded here and extended only when a
   real dataset needs a term (recorded in the Gate-0 triage note). This convention is the single most
   leverage-adding part of Gate-0 — it is what makes the coverage scan trustworthy.
3. **Baseline coverage** — capture `prioritize --coverage --format json` as the
   pre-wave snapshot and hand-triage the `no-candidate` residual into a triage table
   (each target marked **reconcilable** — an existing dataset can be wired — vs
   **genuine-discovery**), appended to this doc.

**Acceptance criteria (Gate-0 done):** a committed capability-vocabulary note (the
seeded field/value set); zero `provided-missing` / `required-missing` capability
warnings on linked datasets/targets; every `no-candidate` target classified
*reconcilable* or *genuine-discovery* in the triage table; and a committed baseline
coverage JSON. Gate-0 is the recommended pilot: it is lossless,
independently useful, and shakes out the arc before any discovery.

### Wave 1 — Open substitutes for the gated arm

Lead wave: highest payoff, reopens the D-004 / t028 walls with reproducible data.
Discovery + verify + connect + **handoff** (no analysis — see §6).

**Estimand rewrite — required before discovery (F2).** Open GWAS/MR does **not**
reconstitute the shelved autoimmune-diathesis × sex × PASC *individual-level EHR
interaction* estimand (D-004); it substitutes a **different, narrower** one: the
causal effect of *genetic liability* to an autoimmune disease (or of a sex-hormone
biomarker) on a PAIS outcome, under instrumental-variable assumptions. What it
**can** address: reverse-causation direction (germline instruments are not caused by
the outcome) and — with sex-stratified or interaction summary statistics — whether
that genetic effect is modified by sex. What it **cannot** replace: the
population-scale prevalence-, utilisation-, and ascertainment-structured interaction
the EHR line targeted (that residue stays with **h0008**). So Wave 1 keeps **causal
MR** targets separate from **descriptive coverage** targets — they are not
interchangeable. Bridge assumptions to count an MR result as evidence for
h0005/h0007/h0009 or q0007/q0013/q0019–q0022, recorded per candidate at handoff
(§4a): instrument relevance + no horizontal pleiotropy (MR-Egger / weighted-median
sensitivity), no uncorrected sample overlap, ancestry-matched panels, an *a priori*
HLA include/exclude decision (the autoimmune signal is HLA-dense), and PAIS
case-definition comparability across the outcome GWAS. "Sex-effect modification" is
only testable where sex-stratified or interaction sumstats exist — a discovery
filter, not an afterthought.

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

### §4a — Candidate handoff contract (done-definition — F4)

A dataset candidate is "ready for `/science:plan-pipeline` handoff" only when every
field below is present, so wave outputs are comparable and reproducible. This is the
integration boundary between this catalog effort and any downstream analysis.

| Field | Requirement |
|---|---|
| dataset entity | exists under `entities/datasets/<slug>.md` |
| access | `verified: true` **or** a structured access-exception with route |
| `last_reviewed` | dated |
| source URL / accession | present and resolvable |
| reproducibility | class + Five-Safes controls per `science.yaml` policy; `unknown`/below-bar → **halt** |
| `provided_capabilities` | declared on the dataset (clears the Gate-0 warning) |
| target `required_capabilities` | declared on each reached Q/H |
| relation / backlink | `related:` edge wired dataset↔target |
| fit / limitation note | one paragraph: estimand scope + **bridge assumptions** (mandatory for MR and D-003 read-across candidates) |
| *(staged / commons-promoted only)* | datapackage path + SHA-256 hashes + provenance |

Discovery-worker outputs (`/science:find-datasets` search records under
`entities/searches/…`) carry their own source/version provenance so a candidate's
origin is reconstructable.

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

- **Front-half only.** This effort ends at the `/science:plan-pipeline` handoff;
  running Mendelian randomization, ingesting cohorts, or any analysis is downstream.
  Wave descriptions list *handoff targets*, not staging or analysis work. The
  governing boundary is **`entities/specs/0001-scope-boundaries-for-health-post-acute-infection.md`** ("primary computational
  pipelines deferred until past seed stage") — **not t082** (F3): t082 is
  specifically the *plan:0006 / N3C* code gate and is now `deferred` and effectively
  moot under D-004, so it does not cleanly govern a new open-data program. Before any
  Wave-1 MR or analysis code is written, resolve the **new scope decision** — *"open
  third-party-reproducible computational analyses after data-catalog expansion"*
  (filed as **t088**), referencing `entities/specs/0001-scope-boundaries-for-health-post-acute-infection.md`; that gate, not t082,
  governs MR code, cohort ingestion, and any runnable pipeline. t088 blocks
  **execution only** — Gate-0 and dataset cataloging/discovery proceed without it.
  - *Note:* a fully-open, low-friction MR vehicle is a strong *candidate argument*
    for that new decision (it is the cheapest possible reproducible analysis), but
    the decision is made explicitly, not assumed here.
- **Not re-cataloging the shelved gated EHR** (N3C / OpenSAFELY) — D-004 stands;
  revisit only if a downloadable de-identified individual-level or truly-open
  synthetic tier appears. UK Biobank remains a separate live credentialed vehicle
  (t028), not re-litigated here.
- **No ledger/validator code** (user decision): triage is hand-done in the Gate-0
  triage table; escalate to a structured ledger only if the gap list proves
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

Run the **Gate-0 reach & capability audit** as the pilot: reconcile prose-only
citations, annotate `provided_capabilities` / `required_capabilities` to clear the
20 + 9 validation warnings, capture the `prioritize --coverage` baseline, and
hand-triage the 22 `no-candidate` targets into the triage table (§4 Gate-0,
reconcilable vs genuine-discovery). Then a **Wave-1 discovery pilot on the GWAS/MR
vehicle** — the single highest-leverage open substitute — through the full arc (find
→ verify → connect → handoff per §4a), with the estimand-rewrite (§4 Wave 1) written
*before* discovery. That exercises the end-to-end arc on the highest-payoff item
before committing to the wider program, and produces the Wave-1 checkpoint delta. The
new open-analysis scope decision (§6) is a prerequisite only for *running* MR, not
for cataloging its vehicle.
