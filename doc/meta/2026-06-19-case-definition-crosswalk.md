---
id: "doc:case-definition-crosswalk-2026-06-19"
title: "PAIS case-definition & admissibility crosswalk — imported cohort papers (t024)"
created: "2026-06-19"
updated: "2026-06-19"
related:
  - topic:pais-case-definition-heterogeneity
  - task:t024
  - task:t001
  - task:t016
---

# PAIS Case-Definition & Admissibility Crosswalk (t024)

Per-paper extraction of the case definition, ascertainment frame, and
cross-study **admissibility** metadata for every paper entity under
`entities/papers/`. Operationalizes the t002 synthesis
(`topic:pais-case-definition-heterogeneity`) into the admissibility layer that
**t001** (cross-pathogen molecular-signature synthesis) needs before it can run,
and supplies the sampling-frame/collider flag that **t016** (menopause→PAIS
analysis plan) needs for cohort screening.

- **Machine-readable table:** [`2026-06-19-case-definition-crosswalk.tsv`](2026-06-19-case-definition-crosswalk.tsv)
  (71 rows × 12 columns).
- **Method:** each entity's full Methods/cohort text was read and coded against a
  fixed 12-field schema (condition, study type, case definition used, PEM
  required?, time threshold, functional-impairment requirement, recruitment
  frame, clinic-collider risk, t001 admissibility, notes) via a 6-way parallel
  extraction. Every field reflects only what the entity file states; absent
  information is coded `not-stated`/`unclear`, not inferred.

## Corpus composition (n = 71)

| Study type | n | | Condition | n |
|---|---|---|---|---|
| narrative-review | 23 | | long-COVID/PASC | 47 |
| cohort-prospective | 15 | | cross-PAIS | 9 |
| systematic-review/MA | 11 | | PTLDS | 4 |
| cohort-retrospective | 8 | | ME/CFS | 4 |
| cross-sectional | 7 | | post-dengue | 2 |
| case-control | 4 | | post-Q-fever / post-SARS / post-sepsis | 3 |
| case-series | 1 | | post-vaccine-SFN / post-COVID-IRD | 2 |
| animal / mechanistic | 2 | | | |

**35 of 71** are primary cohort-like studies (cohort/case-control/cross-sectional/
case-series); the other 36 are reviews, meta-analyses, or basic/animal work that
enroll no PAIS cohort. The corpus is **heavily long-COVID-weighted** — the
non-COVID PAIS arms (PTLDS, ME/CFS, post-dengue/Q-fever/SARS/sepsis) are thin,
which itself bounds any cross-*pathogen* synthesis (t001), based on the
[`2026-06-19-case-definition-crosswalk.tsv`](2026-06-19-case-definition-crosswalk.tsv) coding table.

## Finding 1 — definitional heterogeneity is the rule, named standards the exception

Among the **35 primary studies**, only **9 use a named standard case definition**;
the rest are **author-defined (17; 18 incl. the one RECOVER-index+author row)**,
self-report/symptom-based (6), or none-stated (3). (The all-corpus
`author-defined` count is 22 — the extra 4–5 are review/MA rows; the table below
is the all-71 tally, not the primary-subset.)

| Case definition used (all 71) | n |
|---|---|
| (NA — review/animal) | 23 |
| **author-defined** | 22 |
| self-report/symptom-based | 8 |
| **WHO-2021** | 7 |
| none-stated | 4 |
| NASEM-2024 / IOM-SEID-2015 / CCC-2003 / RECOVER-index / Fukuda+CCC / IDSA-PTLDS | 1 each |

Time thresholds for caseness scatter across **≥4wk (4), ≥8wk (4), ≥3mo (9),
≥6mo (11)** plus a long tail of EHR-index and study-specific windows. This
directly confirms the t002 thesis: cross-study variation is dominated by
definition and threshold choice, not biology. **t001 cannot pool these at face
value** — it must stratify or harmonize on definition.

## Finding 2 — PEM is almost never captured (the load-bearing gap)

**PEM is a required criterion in only 3 of 71 papers** — the two ME/CFS cohorts
(`Che2025` Fukuda+CCC with CPET-provoked PEM; `Hoel2026` CCC) and the
`Komaroff2023` ME/CFS review (IOM/SEID). Among the **15 t001-admissible cohorts,
only 2 require PEM** (both ME/CFS); the other 13 (all long-COVID) score PEM
`no`/`unclear`.

This is the t002 harmonization lever made concrete: the imported long-COVID
cohorts are **structurally unable** to support a PEM-positive-vs-negative
contrast (q0015) because they did not ascertain PEM. **t025** (PEM+ vs PEM−
molecular comparison) therefore cannot be served by the existing corpus and needs
a cohort with symptom-level PEM data (RECOVER/IMPACC raw, not these summaries).

## Finding 3 — clinic-collider risk is pervasive (the t014 DAG, in the data)

Of the **35 primary studies, 20 are high clinic-collider risk** (recruited via
post-COVID / specialty clinics or symptomatic care-seeking — conditioning on the
`clinic_attendance` collider from the t014 DAG), **12 medium**, and only **3 low**
(20+12+3 = 35; the all-71 TSV carries 36 non-NA collider scores — the extra one is
`Zeng2023`, a meta-analysis scored `medium`, which sits outside the primary-study
set). `Stewart2024` is confirmed as the collider exemplar (3 NHS post-COVID clinics, no
control group). The three low-collider primaries are all registry/EHR designs:
`Cai2024`, `Xie2024` (VA), and `Zheng2026` (FinnGen).

## Admissibility verdict for t001

| t001_admissible | n | Cohorts |
|---|---|---|
| **yes** | 15 | Cai2024, Xie2024, Talla2023, Aid2025, CerviaHasler2024, Cruz2025, George2022, Che2025, Peluso2024, Stahlberg2025, Zhang2022, Ozonoff2024, Hoel2026, Klein2023, Shah2025 |
| maybe | 13 | Ganesh2022, Rojas2022, Ryan2022, Gusinow2026, Limongelli2026, Salvucci2023, Peppercorn2023, Mishra2020, Stewart2024, Wang2026, Moldofsky2011, Rebman2026, Sun2025 |
| no | 43 | reviews / MA / animal / mechanistic / no-cohort |

Among the 15 admissible: **7 high / 6 medium / 2 low** collider risk. The two
low-collider admissibles (`Cai2024`, `Xie2024`) are both VA EHR cohorts that are
**~90–95% male** and use broad author-defined multi-outcome ICD indices rather
than a symptom-based PAIS definition. So even the "cleanest" admissible cohorts
trade collider safety for a hospitalization-conditioned, male-skewed,
non-symptom-based phenotype [@Cai2024; @Xie2024].

**Practical t001 guidance:** treat the 15 "yes" as the candidate pool but pool
**within definition family and within collider stratum**, reporting any
cross-study signal under the multi-definition sensitivity discipline from t002.
The non-COVID arms are too sparse (ME/CFS 2, PTLDS 0 admissible primary, post-SARS/
post-sepsis 0 admissible) for a genuine cross-*pathogen* test today — that gap is
a literature-search target, not an analysis the current corpus can support.

## Consequence for t016 (menopause→PAIS) — confirms `not-ready`

The t016 plan requires a **population-based (low-collider), natal-female,
hormone-measured** cohort with reproductive stage stageable at infection. Crossing
the crosswalk against those gates:

- **Low collider risk** narrows 71 → 3 (`Cai2024`, `Xie2024`, `Zheng2026`).
- **Natal-female-analysable** eliminates all three: Cai2024/Xie2024 are ~90–95%
  male VA cohorts; Zheng2026 is a registry DWAS with no biospecimens or hormone
  measures.
- **Hormone-measured** is satisfied by none of the low-collider set.

→ The imported corpus contains **zero** admissible cohort for the menopause
total-effect analysis. This independently **confirms the t016 `not-ready`
verdict** and sharpens **t015**: the search must specifically target a
*population/registry-based* cohort (not a post-COVID clinic) that is
female-inclusive with sex-hormone or menopausal-staging data — a combination no
paper in the present corpus satisfies. The female-inclusive cohorts that do exist
here (`Shah2025`/`Wang2026`, RECOVER women) are medium-collider and use binary
menopause variables (the t020 misclassification concern).

## Follow-ups surfaced

- The crosswalk is now the admissibility metadata **t001** was blocked on — t001
  can proceed to a *definition-stratified* design, but only within long-COVID;
  a cross-pathogen test remains literature-gated.
- **t025** (PEM+ vs PEM−) is confirmed un-serveable by the current corpus
  (PEM ascertained in 2 admissible cohorts, both ME/CFS) — needs external
  symptom-level data.
- **t015** gains a hard search specification: population/registry-based +
  female-inclusive + hormone/menopause staging — the empty cell this audit found.
- Consider a lightweight per-paper sidecar (or `science annotate`) so this
  admissibility coding is queryable from the graph rather than living only in this
  TSV.
