---
kind: search
title: 'Literature/cohort search: hormone-measured & menopause-stageable PAIS cohorts
  (t015)'
status: active
created: '2026-06-19'
updated: '2026-06-19'
id: search:0001-hormone-menopause-pais-cohorts
related:
- task:t015
- task:t016
- task:t020
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- topic:menopause-sex-hormones-and-pais-risk
---

# Search: hormone-measured / menopause-stageable PAIS cohorts (t015)

## Search Focus

Find a cohort that can execute the **t016 menopause→PAIS total-effect analysis**.
The t024 crosswalk found **zero** admissible cohort inside the imported corpus,
so this search looks **outside** it — at population cohorts and biobanks — against
the hard spec: population/registry-based (low clinic-attendance-**collider** risk,
**not** post-COVID specialty clinics), **female-inclusive**, with **sex-hormone
labs** (estradiol/testosterone/SHBG/FSH/LH/AMH) **or** **menopausal-status
staging**, ideally a **pre-infection baseline** and longitudinal long-COVID
outcomes.

The unit of interest is the **cohort/data resource**, not the paper; the ranked
papers below are cohort-resource descriptors and the nearest existing
menopause/hormone × long-COVID analyses.

## Query Set

1. **Broad conceptual (OpenAlex):** `menopause sex hormones estrogen long COVID post-acute sequelae` — 230 works.
2. **Methods/measurement (OpenAlex):** `long COVID sex hormones menopause estrogen testosterone female` — 980 works.
3. **Cohort-capability web audit (two parallel agents):** US/international (RECOVER, IMPACC, All of Us, MGB/PMBB/BioMe biobanks, MY-LC, N3C, ZOE/COVID Symptom Study) and UK/European (UK Biobank, ONS-CIS, Lifelines, Generation Scotland, NAPKON) — per-cohort recruitment frame, female fraction, hormone/menopause variables, baseline availability, access pathway, verified via official data showcases + protocol papers.
4. **Precedent-analysis check:** existing menopause/HRT/hormone × long-COVID studies and their design flaws.

## Sources and Run Metadata

- **OpenAlex** `works` (broad discovery): 2 queries, 230 + 980 candidate counts; top ~50/40 inspected per query. Source = primary discovery.
- **Web audit** of official cohort data dictionaries / showcases and protocol papers (UK Biobank Showcase, ImmPort, dbGaP, ONS QMI, Lifelines/GS catalogues), DOIs/PMIDs verified. Source = `fallback-web` for cohort-capability fields the APIs don't cover.
- Date window: 2020–2026 (plus cohort-protocol papers back to 2013 for UKB/Lifelines/GS).

## Ranked Results

| Rank | Citation (short) | Year | Source IDs | Tier | Why it matters |
|---|---|---|---|---|---|
| 1 | Alcalde-Herraiz et al., *Nat Commun* — UK Biobank pre-infection SHBG & long COVID | 2025 | DOI 10.1038/s41467-025-62354-0 · PMID 40738888 | **Core now** | **Nearest existing analysis**: UK Biobank, *pre-infection* baseline hormone (SHBG) → long-COVID risk in females. Associational, did **not** test menopause/HRT/estradiol — the exact gap t016 fills. Proves the UKB vehicle works. |
| 2 | Pollack et al., *Front Rehabil Sci* — Female reproductive health impacts of Long COVID | 2023 | DOI 10.3389/fresc.2023.1122673 | **Core now** | Maps the reproductive-stage × long-COVID landscape, incl. menopause/menstrual-cycle effects; frames the exposure side of h0005/q0013. |
| 3 | Ballering et al., *Lancet* — Lifelines COVID-attributable persistent symptoms | 2022 | DOI 10.1016/S0140-6736(22)01214-4 · PMID 35934007 | Relevant next | Demonstrates the **Lifelines** population cohort + matched-control long-COVID outcome (the triangulation vehicle); female-excess signal. |
| 4 | Lott et al., *Nat Rev Endocrinol* — Sex hormones in SARS-CoV-2: players or confounders? | 2022 | DOI 10.1038/s41574-022-00780-6 | Relevant next | Directly frames the confounder-vs-mediator question central to the t014 DAG; informs U-proxy/measurement strategy. |
| 5 | Silva et al. (MY-LC sub-analysis) — testosterone in long COVID | 2024 | medRxiv 2024.02.29.24303568 · PMID 38496502 | Relevant next | The MY-LC testosterone finding (corrects a corpus mis-attribution to Klein2023); clinic-recruited (collider) — a cautionary contrast. |
| 6 | Costeira et al., *PLoS ONE* — Estrogen & COVID symptoms, COVID Symptom Study | 2021 | DOI 10.1371/journal.pone.0257051 · PMID 34506535 | Peripheral monitor | Already in corpus; ZOE app, acute outcome, paradoxical HRT (healthy-user bias) — the design trap to avoid. |
| 7 | Thaweethai et al., *JAMA* — RECOVER PASC index | 2023 | DOI 10.1001/jama.2023.8823 · PMID 37278994 | Peripheral monitor | The PEM-weighted outcome instrument adopted by the t016 plan; RECOVER cohort descriptor. |
| 8 | Tin Tin et al., *Br J Cancer* — UK Biobank sex-hormone assay characterization | 2021 | DOI 10.1038/s41416-021-01392-z · PMID 33864017 | Peripheral monitor | Documents UKB oestradiol 175 pmol/L floor + ¾-min imputation — the decisive measurement caveat for the exposure. |

(Discovery surfaced `230 + 980` candidates; the bulk are sex-hormone/immunity background reviews not specific to a usable long-COVID cohort and are not queued. The cohort-resource papers above are the load-bearing records.)

## Cohort admissibility audit (the actual deliverable)

Verdict against the t016 gates: **population-based · female-analysable · hormone-or-menopause-staged · pre-infection baseline · low collider**.

| Cohort | Frame / collider | Female | Hormone labs | Menopause staging | Pre-infection baseline | t016 verdict | Limiting factor |
|---|---|---|---|---|---|---|---|
| **UK Biobank** | Population, **low** | ~54% (~275k ♀) | testosterone + SHBG usable; **oestradiol censored** (floor 175 pmol/L) | **Yes** — age at menopause, HRT, menarche (questionnaire) | **Yes** (2006–2010, ~decade pre-infection) | **ADMISSIBLE (primary)** | Oestradiol unusable → exposure = questionnaire status (±SHBG/T); long COVID must be researcher-engineered (questionnaire+GP codes) |
| **All of Us** | National volunteer, low–moderate | 61.6% | Partial (EHR-ordered, sparse/informative-missing) | Yes (survey + EHR + age) | Partial (pre-2020 enrollees) | **PARTIAL (US primary/replication)** | Volunteer self-selection; sparse hormone labs (per-analyte N not extracted in this search); U09.9 ascertainment |
| **Lifelines** | Population, **low** | ~58% | Largely no (stored samples → add-on assay) | Yes (age at menopause, parity) | **Yes** (2006–2013) | **PARTIAL (replication)** | No baseline hormone assays; exposure = self-report menopause |
| **Generation Scotland** | Population/family, **low** | ~59% | No sex-hormone panel | Yes (age at menopause, HRT) | **Yes** (2006–2011) | **PARTIAL (replication)** | No hormone assays; thin long-COVID ascertainment (CovidLife3, ~5k) |
| **ONS COVID-19 Infection Survey** | Random address-based, **low** | ~53% | No (antibody only) | No (age-proxy only) | Partial/Yes | **TRIANGULATION** | No menopause/hormone data — age-proxied effect only |
| **RECOVER-Adult** | National, low–medium | 71–73% | **No** | Self-report **binary** only | Partial (ambidirectional) | **PARTIAL** | No hormone labs; crude binary menopause (Shah2025); weak temporal order |
| **MGB Biobank / PMBB / BioMe** | Hospital biobank, medium | ~57% (MGB) | Partial (EHR-ordered) | Code+age proxy only; validation not extracted in this search | No | **PARTIAL (US replication)** | Hospital-patient selection; no baseline; menopause by code/age |
| **IMPACC** | Hospitalized acute, medium (severity-selected) | ~39% | No | No | No (first sample acute) | **NOT ADMISSIBLE** | No exposure at all; acute immunophenotyping only |
| **MY-LC** | **Post-COVID clinic, high** | ~66% | No sex-hormone panel (Klein2023) | No | No | **NOT ADMISSIBLE** | Textbook clinic-attendance collider; no exposure; cross-sectional |
| **German NAPKON** | HAP/SUEP clinic **high**; POP lower | ~47% | No | Menopause staging not identified in this search | **No** | **NOT ADMISSIBLE (primary)** | No pre-infection baseline; high collider in hospital arms |
| **N3C** | EHR aggregation, medium–high | mixed | No | No | No | **TRIANGULATION (large-N only)** | EHR collider; no exposure depth |

## Coverage Notes and Gaps

- **No prior study has run a menopause→long-COVID *causal* analysis with a pre-infection baseline in UK Biobank or Lifelines.** This is open territory — t016 would be novel, not a replication. (Alcalde-Herraiz2025 is the closest, and it tested SHBG, not menopause/HRT.)
- **The oestradiol measurement gap is structural, not incidental:** every population cohort either censors postmenopausal oestradiol (UKB assay floor) or never assayed sex hormones (Lifelines/GS/ONS). The t016 exposure must therefore rest on **questionnaire reproductive staging** (age at menopause + HRT), reinforcing t020's STRAW+10/age-band operationalization and its misclassification model. This is consistent with the DAG treating *reproductive stage* (not serum estradiol) as the treatment node.
- **Long-COVID outcome ascertainment is the second universal weak point** in the population cohorts (code-only / questionnaire), pushing back to the t002 case-definition recommendation: engineer the outcome under the WHO≥3mo + multi-definition sensitivity axis already specified in the t016 plan.
- **ME/CFS / non-COVID PAIS with hormone data:** not surfaced as population resources here; cross-pathogen reproductive-stage analysis remains out of reach (consistent with t024's sparse non-COVID arms).
- Scope items covered: h0005 (reproductive-stage), q0013 (failed recovery), t020 (exposure window). Not covered by this search (by design): mechanistic/biomarker topics.

## Recommended Next Actions

| Priority | Action | Rationale | Command |
|---|---|---|---|
| P1 | **Adopt UK Biobank as the primary t016 vehicle** + draft the UKB data-field specification & application plan (fields 2724/3581/2814/3536/2714 menopause/HRT; 30850/30830 testosterone/SHBG; COVID + GP/HES linkage; engineered long-COVID outcome) | Only population, low-collider, pre-infection-baseline, menopause-staged resource; converts t016 from "no cohort" to a concrete data spec | new task (see below) |
| P1 | Read Alcalde-Herraiz2025 (UKB SHBG→long COVID) | Nearest precedent; its design + UKB long-COVID outcome engineering are directly reusable | `/science:research-papers` |
| P2 | Pre-register the UKB analysis with triangulation arms (All of Us / Lifelines) | Multi-cohort replication under the t016 sensitivity discipline; handles the absence of serum estradiol explicitly | `/science:pre-register` (after data spec) |
| P2 | Read Pollack2023 + Lott2022 | Frame exposure-side reproductive biology and the confounder-vs-mediator question for the DAG | `/science:research-papers` |
| P3 | Feed `oestradiol-unusable` + `questionnaire-staging` into t020 misclassification model | Exposure measurement is questionnaire-based across all vehicles | `science tasks` |

## Run provenance

Machine-readable candidate list + cohort audit: [`2026-06-19-hormone-menopause-pais-cohorts.json`](../../doc/searches/2026-06-19-hormone-menopause-pais-cohorts.json).
