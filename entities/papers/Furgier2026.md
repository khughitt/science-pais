---
id: paper:Furgier2026
kind: paper
title: 'Sustained Increase in Pediatric Mastoiditis in the Post-COVID-19 Era: A 9-Year
  Interrupted Time-Series Analysis Based on National Data'
status: active
paper_kind: ""
ontology_terms:
- immunity gap
- immunity debt
- non-pharmaceutical interventions
- interrupted time-series analysis
- pediatric infectious disease
- Streptococcus pyogenes
- Streptococcus pneumoniae
- acute otitis media
- mastoiditis
- post-pandemic disease dynamics
- population-level immune susceptibility
dataset_usage: []
source_refs:
- cite:Furgier2026
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0020-host-immune-baseline-reserve-gate
- question:0058-immunity-debt-resurgence-waves-and-pais-incidence
- question:0059-immunity-debt-elevated-pais-risk-in-delayed
- question:0078-post-streptococcal-autoimmune-pais-post-npi-surge
created: '2026-07-10'
updated: '2026-07-10'
---
# Sustained Increase in Pediatric Mastoiditis in the Post-COVID-19 Era: A 9-Year Interrupted Time-Series Analysis Based on National Data

<!--
- **Authors:** Apolline Furgier, Romain Basmaci, Zaba Valtuille, Inès Fafi, Zein Assad, Léa Lenglart, Natacha Teissier, Charlotte Benoit, Emilien Chebib, Aurélie Bourmaud, François Angoulvant, Pierre Alex Crisinel, André Birgy, Naïm Ouldali, Manon Jaboyedoff
- **Year:** 2026
- **Journal:** The Journal of Pediatrics, Vol. 289, Article 114835
- **DOI/URL:** https://doi.org/10.1016/j.jpeds.2025.114835
- **BibTeX key:** Furgier2026
- **Source:** PDF
-->

## Key Contribution

Using 9 years of French national hospitalization data (2016–2024, n = 7390 pediatric mastoiditis cases), this interrupted time-series study demonstrates a sustained 72% above-expected increase in mastoiditis incidence in the post-NPI period (September 2022 – December 2024), following a 59% suppression during strict NPI. The surge is dominated by a +628% increase in *Streptococcus pyogenes*-attributed cases, which outlasted the broader invasive GAS (iGAS) wave and had not fully returned to baseline by end of 2024. The authors attribute the post-NPI overshoot to the combined effects of an immunity gap in NPI-era children (reduced natural exposure, possible diminished transplacental antibody transfer) and pathogen dynamics, particularly the selective resurgence of iGAS. Complication and surgery rates remained stable, indicating the excess burden is volumetric, not severity-shifted.

## Methods

**Study design:** Retrospective, population-based interrupted time-series (ITS) analysis.

**Data source:** French Programme de Médicalisation des Systèmes d'Information (PMSI) — a comprehensive national medico-administrative database covering all inpatient stays in public and private hospitals in France. Diagnoses coded using ICD-10; procedures using national Common Classification of Medical Procedures. Age-specific denominators from INSEE.

**Period and population:** January 1, 2016 – December 31, 2024; all hospitalized children under 18 years in France. Cases identified via ICD-10 mastoiditis codes as primary or related diagnosis; re-admissions within 2 months counted as one case.

**Four study periods (Oxford COVID-19 Government Response Tracker):**
- Pre-NPI: January 2016 – March 2020 (50 months; n = 3060)
- Strict NPI: April 2020 – July 2021 (15 months; stringency index ~75; n = 408)
- Light NPI: August 2021 – August 2022 (12 months; stringency index ~43; n = 716)
- Post-NPI: September 2022 – December 2024 (27 months; n = 3206)

**Primary outcome:** Monthly incidence of hospitalized mastoiditis per 100 000 children under 18.

**Secondary outcomes:** Incidence by age group (<2 years, 2–4 years, 5–9 years, 10–17 years); by causative pathogen (S. pneumoniae, S. pyogenes, S. aureus, H. influenzae, anaerobes/Fusobacterium); proportion of complicated cases (meningitis, intracranial abscess, thrombosis); proportion requiring surgery (mastoidectomy or neurosurgery).

**Statistical model:** Quasi-Poisson regression with periodic B-splines (4 degrees of freedom) to account for seasonality. Reference period (pre-NPI) used as counterfactual. Six sensitivity analyses including harmonic terms, segmented regression, negative binomial, principal-diagnosis-only coding, and combined NPI period definition.

**Control outcomes:** National incidence of hospitalized UTI (remained stable throughout) and proportion of microbiologically undocumented mastoiditis cases (also stable, ruling out changes in documentation practices as a major confounder).

## Key Findings

**Overall incidence:**
- Strict NPI: −58.9% (95% CI −68.2% to −46.9%, P < .001)
- Light NPI: −14.2% (95% CI −34.0% to +11.6%, P = .254 — not significant)
- Post-NPI: +71.7% (95% CI +26.4% to +133.3%, P = .001) vs. counterfactual without NPI

**Age-group breakdown (post-NPI increase):**
- 0–1 year: +79.3% (P = .004)
- 2–4 years: +112.3% (P = .001)
- 5–9 years: +55.6% (P = .045)
- 10–17 years: −3.2% (P = .902 — not significant)

The post-NPI overshoot is concentrated in the youngest children (under 5), consistent with an immunity gap effect specific to cohorts born during or shortly before the NPI period.

**Pathogen-specific incidence (post-NPI):**
- *S. pyogenes*: +627.8% (95% CI +269.1% to +1335.0%, P < .001) — most dramatic; remained elevated into winter 2024 even after the broader iGAS wave normalized in 2023–2024
- *S. pneumoniae*: +135.6% (95% CI +20.5% to +360.6%, P = .012)
- *H. influenzae*: +124.3% (95% CI −17.0% to +506.0%, P = .111 — not significant)
- *S. aureus*: −0.3% (P = .995 — stable)
- Anaerobes (including *Fusobacterium*): −78.6% (P = .127 — trending down)

*S. pyogenes* showed the sharpest NPI suppression (−84.3%) and the most explosive rebound, consistent with acquired-immunity dependence and the iGAS global resurgence of 2022–2023. The sustained elevation beyond the iGAS baseline recovery raises the possibility of emerging strains with increased mastoid tropism (authors cite the M1UK lineage as a precedent from UK iGAS data).

**Complications and surgery:**
- Proportion with complications (meningitis, intracranial abscess, thrombosis): stable across periods (13.1% overall; post-NPI 14.3%)
- Proportion requiring surgery: stable (18.1% overall; post-NPI 18.3%)
- The post-NPI mastoiditis burden is thus volumetric, not severity-shifted per case.

## Relevance

This paper is primarily an infectious-disease epidemiology study, not a PAIS mechanistic study, but it is directly relevant to the project on two levels:

**1. Immunity gap as a driver of downstream bacterial complications (h0004, h0020).**
The post-NPI mastoiditis surge provides a concrete, population-scale example of how NPI-driven immunity debt translates into elevated severe bacterial infections in children. The gradient by age (most pronounced under 5, absent in 10–17) directly instantiates `hypothesis:0020-host-immune-baseline-reserve-gate`: children born during the pandemic who lacked normal primary pathogen exposures are the most vulnerable stratum. The authors also invoke reduced transplacental antibody transfer from mothers with reduced pathogen exposures as an amplifying mechanism for the 0–1 year old cohort. This connects to `hypothesis:0004-acute-severity-threshold`: the immunity gap widens the pool of children susceptible to high-severity AOM, potentially pushing more infections over the threshold toward complications such as mastoiditis and — by extension — toward post-infectious sequelae.

**2. Streptococcus pyogenes surge as a potential PAIS pathway.**
The +628% iGAS-mastoiditis rebound is notable because *S. pyogenes* infections can trigger well-characterized post-streptococcal autoimmune syndromes: acute rheumatic fever (ARF), post-streptococcal reactive arthritis, PANDAS/PANS, and Sydenham's chorea. A post-pandemic cohort that experienced a compressed surge in first GAS exposures during a critical developmental window — with possibly attenuated immune regulation — may be at elevated risk for these post-infectious autoimmune complications. This represents an underexplored, pediatric-specific PAIS pathway that the project has not yet formalized.

**3. ITS methodology as a template.**
The quasi-Poisson ITS design — with pre-NPI counterfactual, four period definitions, UTI control outcome, and sensitivity analysis suite — is a methodological template directly applicable to other post-pandemic disease surveillance questions in the project, including questions about post-NPI PAIS incidence trends in registries.

**Links to existing entities:**
- `question:0058-immunity-debt-resurgence-waves-and-pais-incidence`: this paper provides direct epidemiological evidence for the GAS wave side of that question
- `question:0059-immunity-debt-elevated-pais-risk-in-delayed`: this paper supports the premise that delayed primary infection creates a severity-amplified post-NPI cohort
- `hypothesis:0004-acute-severity-threshold`: immunity gap → higher severity acute infections → complications; the mastoiditis data are a behavioral demonstration of this threshold effect
- `hypothesis:0020-host-immune-baseline-reserve-gate`: age-stratified severity gradient directly instantiates baseline immune reserve as a gate variable

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Immunity gap / immunity debt | Baseline immune reserve depletion at population level | Paper uses "immunity gap" loosely (reduced natural exposure); project should distinguish from individual immune-baseline reserve (h0020) |
| Post-NPI overshoot in <5 year olds | Pandemic-born cohort as the high-risk stratum | Consistent with h0020: these children never built primary immunity to GAS/Strep |
| Reduced maternal pathogen exposure → reduced transplacental antibody transfer | Passive immunity deficit amplifying innate naivety | Not yet formalized in project framework; connects to youngest age-group signal |
| S. pyogenes mastoiditis surge beyond iGAS baseline recovery | Possible emergence of tropism-shifted or virulence-enhanced GAS clones | Speculative in paper; M1UK analogy cited; would require genomic surveillance to confirm |
| Complication rates stable despite incidence surge | Volume × case-fatality model; severity per case unchanged | Useful calibration: immunity gap inflates incidence but may not alter individual case severity in a well-resourced healthcare system |
| UTI incidence as control outcome (stable) | Counterfactual / negative-control outcome for ITS validity | Methodological template for future project ITS analyses |

## Limitations

1. **ICD-10 coded diagnoses, not standardized clinical criteria.** Heterogeneity in case identification across hospitals. Sensitivity analysis using principal-diagnosis-only coding yielded similar results, partially mitigating this.

2. **Pathogen identification via hospital ICD-10 codes, not direct microbiology.** 82.5% of cases were microbiologically undocumented; causative pathogens in the remaining 17.5% are ICD-10-coded, which may reflect physician attribution rather than confirmed cultures. Under-ascertainment of some pathogens (Moraxella catarrhalis, *S. anginosus* group) is acknowledged.

3. **No genomic or strain-typing data.** Cannot determine whether the sustained S. pyogenes mastoiditis overshoot reflects an immunity gap mechanism, a clonal expansion of virulence/tropism-enhanced lineages (M1UK-like), or their combination. The M1UK hypothesis is explicitly raised but not tested.

4. **Amoxicillin shortage confound (November 2022 – March 2023).** Shorter antibiotic treatment durations for AOM in under-2-year-olds during the shortage may have contributed to early post-NPI mastoiditis excess. Authors note incidence remained elevated after the shortage resolved.

5. **Cannot disentangle immunity gap from pathogen evolution.** The two primary hypotheses (reduced host immunity vs. emergence of more virulent/tissue-tropic strains) are not separable with administrative data alone. This is the central mechanistic uncertainty.

6. **No direct PAIS outcome data.** The study endpoint is hospitalized mastoiditis, not post-infectious sequelae. The PAIS implication (especially for post-streptococcal syndromes) is an inference from pathogen identity and infection burden, not a measured outcome.

7. **French single-country data.** NPI timing and stringency, healthcare access, vaccination schedules (PCV13 at 2+1 since 2013), and iGAS epidemiology may not generalize directly to other countries.

## Model / Tool Availability

No computational models or software tools are released. Statistical analyses performed in R 4.2.2. National PMSI data access requires approval from the French National Commission on Information and Liberty (CNIL); the dataset is not publicly available. Age-specific population denominators from INSEE are publicly available.

## Follow-up

**Related papers to read next:**
- Lassoued et al. (2023) — iGAS surge in French children after NPI lifting, 15-year time-series (cited as ref 31; overlapping authorship with current study; provides the iGAS contextualization)
- Munro & House (2024) — cycles of susceptibility model formalizing immunity debt dynamics (cited as ref 39; already in project as `question:0058` source)
- Lenglart et al. (2024) — pediatric respiratory tract infection surge post-COVID and immunity debt concept (J Pediatr 284:114420; cited as ref 25)
- Cohen et al. (2023) — immunity debt: recrudescence of disease (Infect Dis Now; cited as ref 13; key conceptual reference for the immunity debt frame)

**Questions this raises for the project:**
1. Does the post-NPI S. pyogenes surge generate elevated pediatric post-streptococcal PAIS (ARF, PANDAS/PANS, reactive arthritis) that is not yet captured in PAIS surveillance? (→ new question)
2. Can the ITS quasi-Poisson design be adapted for surveillance of PAIS incidence trends in post-NPI national registry data?
3. Is there a quantifiable threshold of population-level immunity gap (e.g., proportion of seronegative individuals in a birth cohort) that predicts the magnitude of post-NPI disease overshoot?
