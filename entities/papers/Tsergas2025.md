---
id: "paper:Tsergas2025"
kind: "paper"
title: "Why scientists are rethinking the immune effects of SARS-CoV-2"
status: "active"
paper_kind: "news-feature"
ontology_terms:
- immune-exhaustion
- viral-persistence
- t-cell-biology
- post-acute-infection-syndrome
- long-covid
dataset_usage: []
source_refs:
- cite:Tsergas2025
related:
- hypothesis:0003-immune-exhaustion-feedback
- hypothesis:0002-tissue-reservoir-antigen-fragment
- hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais
- hypothesis:0001-shared-dysregulated-attractor
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- question:0064-sars-cov-2-population-level-subclinical-immune
created: "2026-07-10"
updated: "2026-07-10"
---

# Why scientists are rethinking the immune effects of SARS-CoV-2

<!--
- **Authors:** Nick Tsergas (freelance journalist)
- **Year:** 2025
- **Journal:** BMJ
- **DOI:** 10.1136/bmj.r1733
- **BibTeX key:** Tsergas2025
- **Source:** PDF
- **Note:** Journalistic news feature (secondary reporting); commissioned and externally peer reviewed by BMJ. All specific quantitative claims are [UNVERIFIED] pointers to the underlying primary literature, not independently verified data.
-->

## Key Contribution

A BMJ-commissioned news feature arguing that the "immunity debt" hypothesis — the idea that pandemic
precautions created immunological naivety explaining post-pandemic infection surges — is insufficient and
increasingly contradicted by evidence of lasting SARS-CoV-2-driven immune disruption. The piece surveys
expert opinion and cites five key primary studies to frame a nascent scientific consensus: SARS-CoV-2
may be leaving durable immune "scars" — T-cell exhaustion, epigenetic bone-marrow reprogramming, and
viral persistence — that elevate infection risk beyond the long-COVID subset, potentially at a
population scale.

## Methods

This is a secondary journalistic work: expert interviews plus narrative synthesis of primary literature
(cited refs 1–15). No primary data or analysis. The paper should be read as a structured pointer to
underlying primary studies and as a record of the current state of the scientific debate, not as
independent evidence for any specific claim. All numerical figures below are
[UNVERIFIED] and drawn from the primary sources the article cites.

**Key primary studies cited (with citeability for this project):**

| Citation in feature | Primary paper | Relevance to project |
|---|---|---|
| Pedroso et al. (J Leukoc Biol 2024) | T-cell exhaustion + senescence during SARS-CoV-2, even after mild infection; strongest in CD8+ | Supports `hypothesis:0003` exhaustion loop; links to EBV/VZV suppression |
| Cai, Xu, Xie, Al-Aly (Lancet Infect Dis 2025) | 830 000 veterans: higher bacterial/viral/fungal infections in COVID-positive year following; higher sepsis risk vs influenza-admitted | Population-level immune vulnerability signal |
| Cheong et al. (Cell 2023) | Epigenetic reprogramming of bone-marrow stem cells; changes persisting ≥1 year; skewing toward hypersensitivity/inflammation | Antigen-independent innate maintenance route for `hypothesis:0003` (already in h0003 notes as Cheong2023) |
| Peluso et al. (Sci Transl Med 2024) | Viral RNA in gut tissue 2 years post-infection; T-cell activity co-localises with SARS-CoV-2 RNA by PET imaging | Core `hypothesis:0002` support (Peluso2024 already in project) |
| Bernal & Whitehurst (Virus Res 2023) | EBV reactivation >2× rate in COVID+ vs COVID− patients [UNVERIFIED exact fold] | Supports `hypothesis:0015` (EBV reactivation as consequence) |
| Bhavsar et al. (Open Forum Infect Dis 2022) | [UNVERIFIED] 15% higher herpes zoster risk in ≥50-year-olds post-COVID-19 | Secondary latent-virus reactivation signal; consistent with CD8+ exhaustion |
| Gregory et al. (JAMA 2025) | Invasive group A strep: biggest year-on-year increase 2021→2022, after US precautions mostly lifted | Contradicts pure immunity-debt timing explanation |
| Wang et al. (Open Forum Infect Dis 2024) | >4000 viral cases in Ontario: higher bacterial co-infection in COVID-19 vs influenza or RSV recovery [UNVERIFIED age/setting matching caveat noted] | Quantitative signal for disrupted innate defence |

## Key Findings

**On immunity debt:**

- The immunity-debt theory predicts a uniform, temporary rebound across all pathogens once precautions
  lifted — but invasive group A strep infections [UNVERIFIED] saw their largest increase 2021→2022
  (after US precautions lifted) and remained abnormally high subsequently, inconsistent with a
  time-limited catch-up.
- [UNVERIFIED] Infants and toddlers admitted with rare infections since 2022 were too young to have
  experienced pandemic precautions and thus could not have accumulated an "immunity debt" — but were
  likely exposed to SARS-CoV-2 (Jeimy, clinical anecdote).
- Rates of bacterial co-infection are disproportionately elevated in COVID-19 recovery compared to
  influenza or RSV recovery [UNVERIFIED; Wang 2024 study caveat on age/setting matching].

**On T-cell exhaustion:**

- Wolfgang Leitner (NIAID chief, Innate Immunity Section) describes SARS-CoV-2 as linked to
  "indiscriminately high" T-cell killing, analogising to measles immune amnesia (measles depletes
  memory B cells; SARS-CoV-2 may do something analogous with T cells). He explicitly frames this as
  his hypothesis rather than established fact.
- [UNVERIFIED per underlying Pedroso2024] Brazilian cohort: COVID-19 triggered "a sharp rise in T
  cell exhaustion and cellular ageing," strongest in CD8+ T cells — the subset that suppresses latent
  viruses like EBV and VZV. Effects seen even after mild infection; comparator group was limited.
- Akiko Iwasaki (Yale): "clinically significant reductions in circulating T cells" seen at the
  cellular level even in non-hospitalised patients.

**On viral persistence and epigenetic imprinting:**

- [UNVERIFIED per underlying Peluso2024] UCSF PET imaging study found viral RNA in gut tissue 2
  years post-infection; T-cell activity co-clustered with SARS-CoV-2 RNA sites — a likely marker
  of viral persistence driving ongoing T-cell activation and potentially exhaustion.
- [UNVERIFIED per underlying Cheong2023] Cell study: SARS-CoV-2 can reprogram bone-marrow
  haematopoietic stem/progenitor cells (HSPCs), leaving epigenetic changes persisting ≥1 year,
  skewing immune cells toward hypersensitivity and inflammation. Mechanism not confined to
  long-COVID subset.

**On reactivation of latent viruses:**

- EBV reactivation observed at [UNVERIFIED] >2× the rate in COVID+ vs COVID− patients (Bernal2023).
- [UNVERIFIED] 15% higher herpes zoster risk in ≥50-year-olds after COVID-19 diagnosis (Bhavsar2022).
- Jeimy notes the conceptual framework already exists from measles (immune amnesia) and HIV (CD8+
  depletion → latent virus reactivation): "the plausibility is there, the precedent is there."

**On the debate's sociology:**

- Ashish Jha (former WH COVID coordinator) publicly rejected the immune-disruption hypothesis in
  early 2024 and reaffirms that view: "I have seen zero evidence to support that." He attributes
  expert concern to those lacking domain expertise.
- Jeimy attributes reluctance to acknowledge immune damage to fear of the health and economic
  implications: "Nobody wants to be the one that says 'yes, covid-19 causes disability' [beyond
  long covid]."
- Gasperowicz: "the burden of proof has flipped: instead of showing that something is safe, we're
  asked to prove harm."
- Tim Henrich (UCSF): "we've shown immune dysfunction post covid, including signs of exhaustion and
  inflammation in people without symptoms" and "at the population level, we are probably living with
  more inflammation on a day-to-day basis than we were before."
- Iwasaki: the non-long-COVID recovered population ("convalescent controls") may carry subtle
  but persistent immune differences vs healthy pre-COVID controls — and "the entire world is pretty
  much the convalescent control."

## Relevance

This feature directly addresses the **immunity-debt vs immune-dysregulation debate**, which is a
central deflationary alternative to the project's positive hypotheses. Key linkages:

**`hypothesis:0003` (immune exhaustion feedback loop):** The piece is the most accessible secondary
synthesis of the T-cell exhaustion argument. Pedroso2024 (CD8+ exhaustion/senescence even after mild
COVID), Cai2025 (population-level infection vulnerability), and Cheong2023 (HSPC epigenetic
reprogramming as antigen-independent maintenance route) are all cited here and are already part of
h0003's evidence structure. The feature collects expert voice support for the exhaustion mechanism.

**`hypothesis:0002` (tissue reservoir / viral persistence):** Peluso2024 — already in project as
core h0002 evidence — is cited here in the context of explaining why T-cell exhaustion may be
ongoing: T cells accumulate where viral RNA persists, consistent with antigen-driven exhaustion.

**`hypothesis:0015` (EBV reactivation as consequence, not cause):** The feature's framing exactly
matches h0015's organizing conjecture: EBV reactivation is presented as a *consequence* of depleted
CD8+ surveillance, not an independent causal mechanism. It strengthens the consequence-framing
indirectly via analogy to measles and mechanism reasoning.

**`hypothesis:0001` (shared dysregulated attractor):** The population-level inflammation
claim ("we are probably living with more inflammation than before," Henrich) and the non-uniform
cross-pathogen vulnerability pattern are consistent with the shared attractor model — different
downstream outputs from a shared upstream immune-state shift.

**`question:0017` (deflationary alternatives):** Immunity debt is the specific deflationary
alternative challenged here. The article marshals the strongest current counter-evidence without
conducting a systematic review; it is useful as a secondary curation of the immunity-debt
falsification evidence, pointing to the primary studies that should be read to fill the
`question:0017` evidence audit.

## Project Framework Mapping

| Feature Concept | Project Concept | Notes |
|---|---|---|
| "Immunity debt" (catch-up exposure deficit) | Deflationary alternative to immune-dysregulation | Challenged by non-uniform rebound pattern and timing argument |
| "Immune reset" / "immune amnesia" | Shared dysregulated attractor; exhaustion loop (h0003) | Project formalizes this as a maintenance feedback, not merely a reset event |
| T-cell exhaustion (CD8+, CD4+) | `proposition:0025` (co-occurrence of exhaustion + activation) | Exhaustion seen even without long COVID; potentially population-wide |
| Viral persistence driving T-cell clustering | `hypothesis:0002` tissue-reservoir + antigen persistence | PET-based co-localisation is a direct prediction of h0002 |
| HSPC epigenetic reprogramming | `topic:innate-immune-memory-trained-immunity-in-pais`; Cheong2023 | Antigen-independent maintenance route already noted in h0003 |
| EBV/VZV reactivation post-COVID | `hypothesis:0015` (EBV as consequence) | Feature's framing = EBV reactivation is a downstream readout of T-cell failure |
| Population-level chronic inflammation | Novel framing not yet formalized in project | Suggests a new project question (see Follow-up) |
| "Immunity debt" burden-of-proof inversion | Sociological note on publication/policy bias | Relevant to `question:0017` evidence-quality asymmetry discussion |

## Limitations

- Secondary reporting, not primary data. All specific numbers, effect sizes, and study details are
  [UNVERIFIED] and must be traced to underlying primary papers before being entered into the
  project's evidence graph.
- Expert quotes are journalistic summaries; Leitner explicitly frames his T-cell-scar hypothesis as
  his own speculation.
- Selection bias in which studies are cited: the article argues a position (immunity disruption over
  immunity debt); it includes Jha's dissent but does not conduct a balanced systematic evidence
  survey.
- Wang 2024 Ontario cohort: acknowledged limitation that study groups weren't matched by age or
  clinical setting.
- Pedroso2024 Brazilian study: limited comparator group.
- The article conflates two distinct claims: (1) SARS-CoV-2 causes immune changes in all infected
  people; (2) those changes elevate population-level infection risk. The first has more support; the
  second is largely extrapolation.

## Model / Tool Availability

N/A — news feature; no datasets or models released.

## Follow-up

**Primary papers to read next (cited here but not yet in project):**

- **Cai, Xu, Xie, Al-Aly (Lancet Infect Dis 2025)** — The ~836,913-veteran cohort study is the
  strongest population-level signal for elevated infection-diagnosis rates post-COVID. **Now intaken as
  `paper:Cai2025`** (t124): among veterans **not hospitalized during acute COVID**, positive-COVID vs
  test-negative RR 1·17 outpatient-infection / 1·46 respiratory / 1·41 subsequent hospital-admission for
  infection; a *separate* hospitalized COVID-vs-influenza sub-cohort showed infection-admission RR 1·24,
  sepsis 1·35, antimicrobial use 1·23. Held as a consequence-side, clinically-ascertained signal
  consistent with — not proof of — the `hypothesis:0003` exhaustion loop.
- **Pedroso et al. (J Leukoc Biol 2024)** — Direct T-cell exhaustion/senescence data even after
  mild COVID; the most direct primary support for the exhaustion arm of `hypothesis:0003`.
- **Gregory et al. (JAMA 2025)** — Invasive group A strep timing analysis; most powerful
  counter-argument to pure immunity-debt framing.

**Questions raised for the project:**

- Does SARS-CoV-2 cause measurable subclinical immune changes at population scale beyond the long-COVID
  subset? (see `question:0064`)
- What is the minimum evidence threshold to distinguish immunity-debt vs immune-disruption as the
  dominant explanation for post-pandemic infection patterns? (feeds `question:0017`)
- Is the Iwasaki "whole world as convalescent control" framing testable — i.e., are there
  prospective cohort data comparing pre-vs-post-2020 immune baselines in the same individuals or
  in matched controls who escaped infection entirely?
