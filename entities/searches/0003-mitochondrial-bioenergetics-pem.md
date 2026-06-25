---
type: search
title: 'Literature search: mitochondrial / bioenergetic dysfunction and post-exertional
  malaise (t005)'
status: active
created: '2026-06-20'
updated: '2026-06-20'
id: search:0003-mitochondrial-bioenergetics-pem
related:
- task:t005
- question:0011-mitochondrial-basis-of-pem
- topic:mecfs-long-covid-convergence
- topic:biomarkers-and-objective-endpoints
- topic:thromboinflammation-and-endothelial-dysfunction
- hypothesis:0001-shared-dysregulated-attractor
---

# Search: mitochondrial / bioenergetic dysfunction and post-exertional malaise (t005)

## Search Focus

Survey the **bioenergetic basis of post-exertional malaise (PEM)** in ME/CFS and
long COVID — the project's most under-covered yet most central mechanism. Target
sub-areas:

1. Skeletal-muscle bioenergetics / mitochondrial dysfunction (Appelman muscle-biopsy
   PEM; Tomas, Missailidis respirometry).
2. Two-day cardiopulmonary exercise test (2-day CPET) as an objective PEM signature
   (reduced VO2 / workload at ventilatory threshold on day-2 retest; Snell, Stevens,
   Keller, Davenport, Workwell group).
3. Metabolomics / lipidomics of PEM (Naviaux hypometabolic "dauer"; Germain; Hoel
   [already in corpus]).
4. Specific molecular mechanisms: WASF3 / mitochondrial fragmentation (Hwang 2023
   PNAS), itaconate shunt, redox / NAD+, microclots impeding oxygen delivery.
5. Post-exertional immune / transcriptomic changes.
6. **The deconditioning-vs-pathology counter-explanation** (treated as a first-class
   coverage item, per task).

Grounded in `question:0011-mitochondrial-basis-of-pem` and
`topic:mecfs-long-covid-convergence`.

## Query Set

Thirteen OpenAlex `works` queries (broad → mechanism → methods → alternative →
coverage-gap top-ups). Candidate counts are the OpenAlex `meta.count` for each.

| # | Type | Query | Count |
|---|---|---|---|
| q1 | broad-conceptual | post-exertional malaise mitochondrial bioenergetic ME/CFS long COVID | 123 |
| q2 | mechanism (muscle bioenergetics) | skeletal muscle bioenergetics mitochondrial dysfunction long COVID exercise chronic fatigue | 645 |
| q3 | methods (2-day CPET) | two-day cardiopulmonary exercise test CPET ventilatory threshold chronic fatigue post-exertional malaise | 70 |
| q4 | methods (metabolomics) | metabolic features chronic fatigue syndrome metabolomics hypometabolism | 121 |
| q5 | mechanism (muscle-biopsy PEM) | muscle biopsy post-exertional malaise long COVID mitochondria amyloid exercise intolerance | 30 |
| q6 | mechanism (WASF3) | WASF3 mitochondrial respiration fatigue chronic fatigue syndrome | 21 |
| q7 | mechanism (respirometry) | Seahorse respirometry mitochondrial function ME/CFS chronic fatigue cellular bioenergetics | 9 |
| q8 | mechanism (muscle respiration) | mitochondrial respiration muscle biopsy ME/CFS oxidative capacity Tomas Newton | 21 |
| q9 | methods (2-day CPET validity) | discriminative validity metabolic CPET chronic fatigue syndrome Snell VanNess | 47 |
| q10 | **alternative (deconditioning vs pathology)** | deconditioning versus pathophysiology exercise intolerance long COVID chronic fatigue not explained by deconditioning | 152 |
| q11 | coverage top-up (microclots/O2) | amyloid fibrin microclots oxygen delivery long COVID endothelial hypoxia | 55 |
| q12 | coverage top-up (invasive CPET) | invasive cardiopulmonary exercise test preload failure systemic oxygen extraction long COVID Systrom | 14 |
| q13 | coverage top-up (post-exertional transcriptomics) | post-exertional malaise gene expression transcriptomic immune cell exercise provocation long COVID ME/CFS | 23 |

## Sources and Run Metadata

- **OpenAlex `works`** was the primary discovery engine (13 queries; broad queries
  >=30 candidates each). Queried via the `WebFetch` tool against
  `api.openalex.org` because **Bash network egress is denied in this sandbox**
  (direct `curl` to OpenAlex/PubMed was blocked).
- **PubMed E-utilities**: attempted but blocked — the PubMed web endpoint returned a
  reCAPTCHA and the `curl` E-utilities path is sandbox-blocked. Author lists, venues
  and years for Core-now items were instead **verified individually via OpenAlex
  single-work lookups** (`/works/doi:...`). All DOIs below are real and verified.
- **WebSearch / MEpedia / Open Medicine Foundation**: `fallback-web`, used only to
  establish the provenance of the **itaconate-shunt hypothesis** (see Coverage Notes).
- Date window: last ~12 years (2014-2026) plus seminal earlier work; emphasis on the
  provoked-state (exercise-challenge) literature.
- ~46 unique candidates surfaced; 32 retained and ranked after dedup
  (DOI > PMID > normalized-title; preprint versions collapsed into the published DOI).

## Ranked Results

| Rank | Citation | Year | Source IDs | Tier | Why it matters |
|---|---|---|---|---|---|
| 1 | Appelman et al., *Nat Commun* — muscle abnormalities worsen after PEM in long COVID | 2024 | DOI 10.1038/s41467-023-44432-3 | **Core now** | Definitive before/after exercise-provoked **muscle-biopsy** PEM study: post-PEM mitochondrial (succinate dehydrogenase) failure, glycolytic + fiber-type shift, amyloid/capillary changes, local tissue necrosis. Most direct PEM-bioenergetics evidence in long COVID. |
| 2 | Wang et al. (Hwang group), *PNAS* — WASF3 disrupts mitochondrial respiration in ME/CFS | 2023 | DOI 10.1073/pnas.2302738120 | **Core now** | The named **Hwang 2023** WASF3 paper: ER-stress-induced WASF3 impairs mitochondrial supercomplex assembly + respiration; a tractable molecular mechanism for exercise intolerance. (First author Ping-yuan Wang; senior author Paul M. Hwang.) |
| 3 | Naviaux et al., *PNAS* — Metabolic features of chronic fatigue syndrome | 2016 | DOI 10.1073/pnas.1607571113 | **Core now** | Seminal hypometabolic **"dauer"** metabolomics: broad downregulation across sphingolipid/phospholipid/purine/mitochondrial pathways resembling a conserved cell-danger/torpor state. Founding framing for the bioenergetic-PEM hypothesis. |
| 4 | Joseph et al. (Systrom group), *CHEST* — Exercise pathophysiology in ME/CFS and PASC | 2023 | DOI 10.1016/j.chest.2023.03.049 | **Core now** | **Invasive CPET** directly arbitrating the deconditioning-vs-pathology debate: preload failure + impaired peripheral O2 extraction (tissue/mitochondrial), not a deconditioning-only ceiling. |
| 5 | Germain et al., *JCI Insight* — Disrupted metabolomic response/recovery after maximal exercise in ME/CFS | 2022 | DOI 10.1172/jci.insight.157621 | **Core now** | Provoked-state metabolomics: failed metabolite **recovery trajectory** after exercise; candidate provoked PEM biomarker. |
| 6 | Keller et al., *J Transl Med* — Inability to reproduce VO2peak indicates functional impairment | 2014 | DOI 10.1186/1479-5876-12-104 | **Core now** | Foundational **2-day CPET** result: day-2 failure to reproduce VO2/workload at peak and at ventilatory threshold — the objective physiological PEM signature. |
| 7 | Vu et al., *Cell Rep Med* — Single-cell immune transcriptomics at baseline and after symptom provocation in ME/CFS | 2024 | DOI 10.1016/j.xcrm.2023.101373 | **Core now** | Post-exertional **single-cell transcriptomics**: maps how CPET provocation reshapes immune-cell programs, linking PEM to the immune arm of the bioenergetic model. |
| 8 | Fluge et al., *JCI Insight* — Impaired pyruvate dehydrogenase function in ME/CFS | 2016 | DOI 10.1172/jci.insight.89376 | Relevant next | PDH-block hypothesis: a specific, testable bioenergetic bottleneck shunting metabolism off oxidative ATP. |
| 9 | Missailidis et al., *IJMS* — Isolated Complex V inefficiency in ME/CFS lymphocytes | 2020 | DOI 10.3390/ijms21031074 | Relevant next | Named **Missailidis** Seahorse/respirometry work: isolated Complex V inefficiency + compensatory respiratory hyperactivation. |
| 10 | Tomas et al., *Sci Rep* — Substrate utilisation of cultured muscle cells in CFS | 2020 | DOI 10.1038/s41598-020-75406-w | Relevant next | Named **Tomas** myotube respirometry: altered substrate utilisation + AMPK/glucose-uptake response. |
| 11 | Keller et al., *J Transl Med* — Cardiopulmonary + metabolic responses during 2-day CPET in ME/CFS | 2024 | DOI 10.1186/s12967-024-05410-5 | Relevant next | Recent large 2-day CPET dataset translating the day-2 O2-consumption deficit into impairment classification. |
| 12 | Bizjak et al., *IJMS* — Muscle mitochondria in CFS vs post-COVID | 2024 | DOI 10.3390/ijms25031675 | Relevant next | Directly tests the **shared-vs-trigger-specific** bioenergetic question (q0011 core) by comparing muscle mito function/morphology across triggers. |
| 13 | Scheibenbogen et al., *J Cachexia Sarcopenia Muscle* — Skeletal-muscle disturbance in post-COVID and ME/CFS | 2024 | DOI 10.1002/jcsm.13669 | Relevant next | Authoritative review consolidating shared skeletal-muscle bioenergetic/microvascular lesion. |
| 14 | Holden et al., *J Transl Med* — Systematic review of mitochondrial abnormalities in ME/CFS | 2020 | DOI 10.1186/s12967-020-02452-3 | Relevant next | Documents historical **inconsistency** of ME/CFS mitochondrial findings — the key evidence-maturity caveat. |
| 15 | Nelson et al., *J Transl Med* — Diagnostic sensitivity of 2-day CPET in ME/CFS | 2019 | DOI 10.1186/s12967-019-1836-0 | Relevant next | Test characteristics needed to judge 2-day CPET as an objective PEM endpoint. |
| 16 | Stevens et al., *Front Pediatr* — CPET methodology for exertion intolerance in ME/CFS | 2018 | DOI 10.3389/fped.2018.00242 | Relevant next | Named **Stevens** (Workwell) methods/standardization backbone for reproducible 2-day CPET. |
| 17 | Vermeulen et al., *J Transl Med* — Decreased oxygen extraction during CPET in CFS | 2014 | DOI 10.1186/1479-5876-12-20 | Relevant next | Tissue-level O2-extraction deficit — evidence the lesion is peripheral/mitochondrial, not central. |
| 18 | Bouquet et al., *PLoS ONE* — Whole-blood transcriptome/virome after CPET-induced PEM | 2019 | DOI 10.1371/journal.pone.0212193 | Relevant next | Earlier post-CPET molecular readout of PEM; complements Vu2024. |
| 19 | Baraniuk, *IJMS* — CSF metabolomics-lipidomics of PEM and serine pathway in ME/CFS | 2025 | DOI 10.3390/ijms26031282 | Relevant next | CNS-bioenergetic dimension of provoked PEM (serine/one-carbon). |
| 20 | Molnar et al., *GeroScience* — Mitochondrial dysfunction in long COVID (review) | 2024 | DOI 10.1007/s11357-024-01165-5 | Relevant next | Heavily cited review of redox/NAD+/ATP mechanisms + therapeutic candidates in long COVID. |
| 21 | Nunes et al., *Pharmaceuticals* — Hyperactivated platelets + fibrinaloid microclots in ME/CFS | 2022 | DOI 10.3390/ph15080931 | Relevant next | The **microclots → oxygen-delivery impairment** mechanism (links thromboinflammation topic). |
| 22 | McGregor et al., *Diagnostics* — PEM associated with hypermetabolism/purine deregulation in ME/CFS | 2019 | DOI 10.3390/diagnostics9030070 | Relevant next | Closest peer-reviewed anchor for the **itaconate-shunt** sub-area (see Coverage Notes). |

(Peripheral-monitor candidates — Wirth2024, Davenport2019, Glass2025, Charlton2024,
Haunhorst2024, VanCampen2020, Mantle2024, Saito2024, Sweetman2020, Shankar2025 — are
in the JSON, ranks 23-32. They are retained for monitoring but not queued for reading
now.)

## Priority Reading Queue

1. **Appelman2024** (muscle-biopsy PEM, long COVID) — the central new evidence.
2. **Wang2023** (WASF3/Hwang, ME/CFS) — named molecular mechanism.
3. **Naviaux2016** (hypometabolic dauer) — founding metabolomic frame.
4. **Joseph2023** (Systrom invasive CPET) — resolves deconditioning-vs-pathology.
5. **Germain2022** (provoked metabolomics) — candidate provoked PEM biomarker.
6. **Keller2014** (2-day CPET) — objective physiological PEM signature.
7. **Vu2024** (post-exertional single-cell transcriptomics) — immune arm of PEM.

## Coverage Notes and Gaps

Coverage audit against the task sub-areas:

- **Muscle bioenergetics / mitochondrial dysfunction** — covered (Appelman2024,
  Tomas2020, Missailidis2020, Bizjak2024, Scheibenbogen2024, Holden2020).
- **2-day CPET objective PEM signature** — covered well (Keller2014, Keller2024,
  Nelson2019, Stevens2018, Vermeulen2014, VanCampen2020, Davenport2019). The named
  **Snell** does not appear as first author in the retained set; the Workwell 2-day
  protocol is represented through Stevens2018 / Keller2014/2024 (same group). A
  Snell/VanNess first-author primary (the original 2-day-CPET reliability paper)
  could be pulled in a follow-up if a Snell-specific citation is wanted.
- **Metabolomics / lipidomics of PEM** — covered (Naviaux2016, Germain2022,
  Baraniuk2025, Fluge2016; Hoel2026 already in corpus).
- **WASF3 / mitochondrial fragmentation** — covered (Wang2023/Hwang).
- **Itaconate shunt** — **partial / important nuance.** The task attributes this to
  "Comhaire", but the itaconate-shunt hypothesis for ME/CFS is from **Robert Phair &
  Ronald Davis (Open Medicine Foundation)** and currently exists primarily as
  conference talks / OMF materials, **not** a single indexed peer-reviewed primary
  paper. The closest peer-reviewed anchor is **McGregor2019** (purine/hypermetabolism
  metabolomics), which the hypothesis builds on. No "Comhaire" itaconate ME/CFS paper
  was found in OpenAlex or web search. Flag: the itaconate-shunt mechanism is at
  **hypothesis (pre-publication)** maturity — represent it as such.
- **Redox / NAD+** — covered at review level (Molnar2024, Mantle2024 CoQ10,
  Shankar2025 PNAS oxidative stress). Thinner on primary provoked-state redox data.
- **Microclots impeding oxygen delivery** — covered (Nunes2022; ties to
  `topic:thromboinflammation-and-endothelial-dysfunction`).
- **Post-exertional immune/transcriptomic changes** — covered (Vu2024 single-cell,
  Bouquet2019 whole-blood).
- **Deconditioning-vs-pathology debate (explicit coverage item)** — covered via
  **Joseph2023 invasive CPET** (preload failure + impaired O2 extraction = a
  pathophysiological, not deconditioning-only, signature) and **Vermeulen2014**
  (peripheral O2-extraction deficit). The day-2 CPET literature (Keller2014/2024,
  Nelson2019) is itself the strongest deconditioning-counter because deconditioning
  does **not** predict a *worse* day-2 retest. This debate remains genuinely open and
  should be carried as a standing caveat: small Ns, assay inconsistency (Holden2020),
  and the difficulty of fully controlling for activity level.

Residual gaps for a future pass:
- A **Snell/VanNess** first-author 2-day-CPET reliability primary (if a Snell-specific
  citation is required).
- **Primary itaconate-shunt** evidence (watch OMF / Phair output; currently no indexed
  primary).
- **NAD+/redox provoked-state primaries** (vs review-level coverage).
- Direction-of-effect reconciliation: ME/CFS hypometabolic phenotype (Naviaux2016) vs
  *up*-regulated/compensatory mitochondrial readouts (Missailidis Complex V
  hyperactivation; Peppercorn2023 in corpus) — a substantive unresolved tension noted
  in `topic:mecfs-long-covid-convergence`.

## Recommended Next Actions

| Priority | Action | Rationale | Command |
|---|---|---|---|
| P1 | Read **Appelman2024** | Central muscle-biopsy PEM evidence; populate stub | `/science:research-papers` |
| P1 | Read **Wang2023** (WASF3/Hwang) + **Joseph2023** (Systrom invasive CPET) | Named mechanism + the deconditioning-vs-pathology arbiter | `/science:research-papers` |
| P1 | Read **Naviaux2016** + **Germain2022** | Hypometabolic frame + provoked metabolomic biomarker | `/science:research-papers` |
| P2 | Read **Keller2014** + **Vu2024** | Objective 2-day-CPET PEM signature + post-exertional immune transcriptomics | `/science:research-papers` |
| P2 | New task: chase a **Snell/VanNess** 2-day-CPET reliability primary + monitor **itaconate-shunt** for a first peer-reviewed primary | Two named-but-unindexed targets from the task brief | `science tasks add` |
| P2 | Feed the **direction-of-mitochondrial-change tension** (hypometabolic vs compensatory-hyperactivation) into `question:0011` as an open sub-question | Substantive unresolved discordance touching q0011 and the convergence topic | edit `question:0011` |
| P3 | Update `topic:mecfs-long-covid-convergence` and `topic:biomarkers-and-objective-endpoints` with the 2-day-CPET + Appelman muscle-biopsy evidence once read | Strengthens objective-endpoint and convergence narratives | `/science:research-topic` |

## Run provenance

Machine-readable candidate list + dedup/provenance/tier: [`2026-06-20-mitochondrial-bioenergetics-pem.json`](../../doc/searches/2026-06-20-mitochondrial-bioenergetics-pem.json).
