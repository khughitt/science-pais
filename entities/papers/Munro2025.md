---
id: paper:Munro2025
kind: paper
title: "Cycles of Susceptibility: Immunity Debt Explains Altered Infectious Disease Dynamics Post-Pandemic"
status: active
paper_kind: review
ontology_terms:
- immunity debt
- immunity gap
- non-pharmaceutical interventions
- RSV
- group A Streptococcus
- SIRS model
- seasonal transmission
- population immunity
- post-pandemic epidemiology
dataset_usage: []
source_refs:
- cite:Munro2025
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- question:0008-formalize-vicious-cycle-attractor-model
created: '2026-07-10'
updated: '2026-07-10'
---

# Cycles of Susceptibility: Immunity Debt Explains Altered Infectious Disease Dynamics Post-Pandemic

<!--
- **Authors:** Alasdair P. S. Munro, Thomas House
- **Year:** 2025 (journal issue; online publication October 2024)
- **Journal:** Clinical Infectious Diseases
- **Volume/Issue/Pages:** 81(6):1173–1176
- **DOI:** 10.1093/cid/ciae493
- **BibTeX key:** Munro2025
- **Source:** PDF
-->

## Key Contribution

This Viewpoints article argues that the post-pandemic resurgences of endemic pathogens — primarily RSV and group A Streptococcus (GAS), but also adenovirus and Mycoplasma pneumoniae — are fully explained by "immunity debt": the accumulation of susceptible individuals during the NPI period, when suppressed pathogen circulation prevented the normal replenishment of infection-acquired population immunity. The paper presents a simple SIRS (Susceptible-Infectious-Recovered) model with seasonal oscillation in contact rates that reproduces the observed pattern — annual waves, complete pandemic absence, an exceptionally large post-NPI wave, then return to pre-pandemic dynamics — without invoking any additional mechanisms. Critically, the authors explicitly distinguish immunity debt (a population-level, pathogen-specific susceptibility accumulation) from immune system dysfunction (individual-level immune competence failure), rebutting commentators who have conflated the two.

## Methods

- **Narrative synthesis** of multi-country surveillance data for RSV (Japan, South Korea, Australia, New Zealand, Denmark, Belgium, UK, North America) and other pathogens (GAS, gastrointestinal adenovirus, Mycoplasma pneumoniae, influenza).
- **SIRS compartmental model** with four processes (infection, hospitalization, recovery, waning immunity) and annual oscillation in infectious contacts mimicking school holidays / seasonal factors. Interrupted by one year of significantly reduced contact rates. Model is intentionally stylized — not calibrated to specific pathogen data. Code publicly available at https://github.com/thomasallanhouse/covid19-incidence/blob/main/debt.ipynb.
- **UK secondary-care hospital surveillance data** (public, ONS-linked) showing percentage positivity for three respiratory viruses (RSV, influenza, COVID) from 2020 through 2024.
- The paper is a Viewpoints article; it contains no original epidemiological data collection.

## Key Findings

1. **Immunity debt explains RSV resurgences without additional mechanisms.** Post-NPI RSV surges (summer 2020/2021 in Southern Hemisphere; summer 2021 in UK/Europe; anomalously large or early 2021–2022 waves in North America and Japan) are parsimoniously explained by growth of the susceptible pool during NPI-suppressed periods. These surges preceded or were independent of COVID-19 exposure, ruling out direct SARS-CoV-2 immune effects.

2. **Testing-rate increases are insufficient to explain the excess.** While increased testing accounts for some observed case counts (e.g. a significant fraction in North America), it fails to explain: (a) anomalous seasonality (summer RSV in temperate climates); (b) surges in invasive disease (invasive GAS, empyema), which is always tested regardless of testing regime; (c) in Denmark, increased testing explained only 70% of the RSV excess.

3. **GAS and other pathogens show the same pattern.** The unprecedented December 2022 UK surge in invasive GAS disease (including empyema) is attributed to immunity debt in a pathogen whose invasive-disease testing is surveillance-complete and insensitive to clinical testing behavior. Mycoplasma pneumoniae showed an apparently global resurgence despite its usual 3–5-year inter-epidemic cycle.

4. **Influenza is a principled exception.** Influenza immunity wanes primarily through antigenic drift in the virus, not through simple antibody waning. NPI suppression of viral replication created an evolutionary bottleneck that reduced the rate of antigenic drift, partially preserving population immune match to circulating strains. Additionally, influenza vaccination in high-risk groups buffered any immunity gap. This mechanistic contrast with RSV (which undergoes no comparable antigenic shift) predicts and explains the relatively muted influenza resurgence post-NPI.

5. **SIRS model reproduces the qualitative cycle.** Even the simplest immunity-debt model — with no pathogen-specific calibration — generates: (a) stable annual hospitalization waves, (b) complete absence of disease during the NPI year, (c) a single very large post-NPI wave, then (d) damped oscillation returning toward pre-pandemic amplitude. The model output is compared to observed UK secondary-care data, where the qualitative agreement is illustrated for RSV.

6. **Regional variation is explained by NPI timing, not extra mechanisms.** New Zealand and Tokyo: complete 2020 absence then large 2021 resurgence. Belgium: 2020–2021 season merely delayed and flattened. UK: summer 2021 wave plus 2022–2023 resurgence. All patterns are consistent with different NPI timing and duration operating through the same immunity-debt mechanism.

## Relevance

**Direct relevance to the cycles project (cross-link):** This paper provides the mathematical and epidemiological grounding for seasonal susceptibility cycling using SIRS. Its core claim — that population immune state oscillates due to infection-acquired waning immunity interacting with seasonal exposure — is the foundational epidemiological model that the `cycles` peer project studies. The SIRS code (publicly available) is a resource for any formal dynamical modeling in that project.

**Relevance to PAIS risk (indirect but important for this project):**

- **Link to `hypothesis:0004-acute-severity-threshold`.** Immunity debt means large cohorts of immunologically naive individuals (children who were not exposed in infancy, and adults who missed typical adult re-exposure cycles) received primary or first-since-infancy RSV and GAS infections during resurgence waves. Primary adult RSV infection tends to be more severe than re-exposure, and invasive GAS in adults carries substantial morbidity. If acute illness severity gates PAIS risk (h0004), then immunity debt waves may have transiently elevated population-level PAIS incidence for RSV and GAS — distinct from long COVID but a possible source of unmeasured post-GAS and post-RSV PAIS burden.

- **Link to `hypothesis:0001` and `hypothesis:0010` (SIRS modeling).** The SIRS model structure used here — seasonal forcing, susceptible pool dynamics, waning immunity — is directly applicable to modeling PAIS dynamics at the population level (`question:0008-formalize-vicious-cycle-attractor-model`). The model shows that a simple compartmental framework can capture large-amplitude transient departures from steady-state, which is conceptually related to how the PAIS project models recovery dynamics. The model's "return to pre-pandemic dynamics" result is also relevant to hypothesis:0010 (gradient recovery hypothesis): the SIRS analogy suggests that large perturbations to susceptibility can dissipate over time through exposure-rebalancing, which is a population-level analog of the slow-recovery-gradient argument.

- **Conceptual precision for PAIS framing.** The paper's explicit rebuttal of "immunity debt = immune dysfunction" is a useful citation for disambiguating population-level susceptibility (epidemiological concept) from individual-level immune impairment (PAIS mechanism). This distinction is needed when referencing post-pandemic disease dynamics in the project's framing — immunity debt is a mechanism for increasing acute infection burden, not for causing immune failure in individuals who were previously infected.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Immunity debt / immunity gap | Population susceptibility accumulation (epidemiological context for PAIS burden) | Not a PAIS mechanism per se; modifies exposure burden and acute severity distribution |
| SIRS model seasonal cycling | Dynamical attractor / recovery gradient modeling (`question:0008`) | Methods contribution; model code available |
| Susceptible pool growth during NPIs | Naive-host subpopulation at elevated acute-severity risk | Links to `hypothesis:0004` (severity threshold gates PAIS) |
| Immunity debt ≠ immune dysfunction | PAIS ≠ immunity debt | Critical disambiguation; immunity debt operates at population level, PAIS at individual host level |
| GAS resurgence (invasive disease) | Post-GAS PAIS (post-streptococcal syndromes) | Paper documents resurgence; does not address post-GAS sequelae specifically |
| Influenza exception (antigenic drift) | Pathogen-specific immunity maintenance mechanisms | Relevant context for modeling immunity to specific PAIS-causing pathogens |

## Limitations

- **Viewpoints article, not primary research.** No original data collection or hypothesis testing; the SIRS model is stylized and uncalibrated to specific pathogens.
- **SIRS model is intentionally simplified.** It omits age structure (critical for RSV, where infant immunity dynamics differ from adult), spatial heterogeneity, multi-strain dynamics, and vaccine effects.
- **No PAIS outcomes tracked.** The paper does not measure or address post-RSV or post-GAS chronic sequelae; the PAIS connection is inferential and requires separate evidence.
- **Causal attribution is observational.** The surveillance data are compatible with immunity debt but cannot definitively rule out other explanations (e.g., pathogen evolution, NPI-driven behavior changes in healthcare-seeking).
- **Testing confounding is real but bounded.** The paper argues testing increases are insufficient to explain the excess, but the correction methods are imprecise, especially across different healthcare systems.
- **Influenza evolutionary bottleneck argument is plausible but unquantified.** The claim that reduced viral replication caused reduced antigenic drift is presented without formal evolutionary modeling or empirical antigenic characterization.

## Model / Tool Availability

SIRS immunity-debt model (Python/Jupyter):
- URL: https://github.com/thomasallanhouse/covid19-incidence/blob/main/debt.ipynb
- No calibration to specific pathogen data; intended as illustrative/stylized
- No license or hardware requirements noted [UNVERIFIED]

## Follow-up

- **For the cycles project:** Examine the model code and consider extension with age structure and pathogen-specific calibration.
- **For this project:** Assess whether post-RSV and post-GAS PAIS incidence increased following the 2021–2022 immunity debt resurgence waves (no literature currently in project).
- **Key next papers:** Baker et al. 2020 (PNAS; ref [1] in this paper) — original prediction of NPI impacts on endemic infection dynamics. Messacar et al. 2022 (Lancet; ref [3]) — pediatric endemic virus dynamics post-pandemic disruption.
- **Question raised:** Do immunity debt-driven first exposures in older children and adults carry elevated PAIS risk through the acute-severity-threshold mechanism? (see new question created from this paper)
- **Modeling note:** The SIRS model's qualitative behavior — large transient wave then damped return — is a useful comparison case for PAIS recovery trajectory models (`question:0008`, `hypothesis:0010`).
