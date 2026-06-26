---
id: question:0015-does-pem-requirement-improve-cross-study-comparability
type: question
title: Does requiring post-exertional malaise (PEM) in PAIS case definitions improve
  cross-study comparability of molecular and mechanistic findings?
status: active
ontology_terms:
- post-exertional malaise
- case definition
- cross-study comparability
- biomarker reproducibility
- ME/CFS
- long COVID
datasets: []
source_refs:
- cite:Che2025
- cite:Thaweethai2023
- cite:Carruthers2003CCC
- cite:Carruthers2011ICC
- cite:Fukuda1994
- cite:Peppercorn2023
- cite:Hoel2026
- cite:McGregor2019
- cite:Gattoni2025
- cite:Keller2014
- cite:Maestri2025
- cite:Appelman2024
related:
- topic:pais-case-definition-heterogeneity
- topic:mecfs-long-covid-convergence
- topic:biomarkers-and-objective-endpoints
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands
- interpretation:0027-t061-severity-adjusted-pem-vehicle-triage
- interpretation:0030-t070-recover-adult-q0015-controlled-access-gate
- dataset:recover-adult
- dataset:impacc-immunophenotyping-covid
- paper:Maestri2025
- paper:McGregor2019
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- task:t061
- task:t070
created: '2026-06-19'
updated: '2026-06-26'
---
# Does requiring post-exertional malaise (PEM) in PAIS case definitions improve cross-study comparability of molecular and mechanistic findings?

## Summary

PEM is the defining feature that most consistently differentiates biologically-characterizable ME/CFS from non-specific chronic fatigue and from prolonged normal post-illness recovery. It is mandatory in CCC, ICC, and SEID definitions for ME/CFS and is the highest-weighted symptom in the RECOVER PASC index for long COVID. The mechanistic basis (failure to replenish cellular energy after exertion, immune exacerbation post-exercise) is operationalizable via cardiopulmonary exercise testing (CPET) and worsened molecular profiles 24h post-exercise (Che2025). This question asks whether PEM-requirement is itself the key driver of cross-study reproducibility of molecular findings, beyond being a diagnostic enrichment criterion.

## Why It Matters

- If PEM requirement improves reproducibility, it should be adopted as a minimum criterion for t001's cross-pathogen signature work, even at the cost of sample size.
- If PEM requirement does not improve reproducibility (or worsens it by over-restricting the population), broader definitions are preferable.
- The mechanism is plausible (PEM-positive patients have an identifiable immune-metabolic failure mode; PEM-negative patients are heterogeneous), but direct evidence comparing PEM+ vs PEM- molecular profiles within the same study is limited.
- This question underlies the sensitivity-arbitration strategy proposed for t016's outcome operationalization.

## Current Evidence

- Supporting PEM as a molecular discriminator: Che2025 (exercise-challenge multi-omics in 56 ME/CFS) demonstrates that ≥7 pathobiological pathways worsen specifically after exercise in ME/CFS patients, suggesting PEM is a provokable, measurable state rather than a self-reported symptom; this is the most direct operationalization of PEM as a biological endpoint. Thaweethai2023 (RECOVER index) shows PEM discriminates PASC from recovered controls with one of the highest individual weights. Peppercorn2023 and Hoel2026 both study CCC-grade ME/CFS and find consistent immune/mitochondrial proteomic signatures, contrasting with the heterogeneous and sometimes null findings in Fukuda-grade cohorts.
- Closest existing within-cohort PEM-stratified template: McGregor2019 (Diagnostics) split 46 CCC-defined ME/CFS cases into PEM+ (n=35, active episode in past 7 days) vs NoPEM (n=11) and compared serum/urine NMR metabolomics across three groups (HC / NoPEM / PEM). PEM status correlated with serum hypoxanthine (purine salvage marker; r ≈ −0.35 for 7-day severity, −0.43 for 12-month frequency) and with urine methylhistidine and mannitol (PEM-selective), alongside a hypermetabolism + hypoacetylation signature. The NoPEM group showed paradoxically *lower* hypoxanthine than the active-PEM group, suggesting chronic quiescent depletion vs partial acute-episode release. This is the only study explicitly designed with the PEM-stratified three-group contrast. **Critical limitation:** no adjustment for overall illness/fatigue severity (the two ME/CFS groups had near-identical fatigue scores), so the PEM-group signal cannot be separated from a general severity marker. Single-platform targeted NMR (29 serum + 30 urine metabolites), small NoPEM n=11, non-standardized PEM instrument (pre-DSQ-PEM), cross-sectional.
- **Cross-trigger counterweight (Gattoni2025):** A 2-day CPET study in 15 long COVID patients (80% PEM-positive by mDSQ) found **no significant day-1 vs day-2 decrement** in gas exchange threshold, VO2peak, or peak work rate (all p > 0.05). This null stands in direct contrast to the well-replicated ME/CFS 2-day CPET result (day-2 GET/VO2 decrement). PEM-enriched long COVID patients are, on this validated bioenergetic assay, **not biologically equivalent to PEM-enriched ME/CFS patients**. This weakens — though does not refute — the assumption that requiring PEM documentation produces exchangeable, biologically coherent cohorts across different PAIS triggers. Limitations: n = 15 (underpowered for a null), no ME/CFS comparison arm, 40% of patients aerobically deconditioned (alternative explanation), and the 24h inter-test interval may not capture long COVID PEM kinetics.
- Against or qualifying: No published study has directly compared molecular (proteomic, metabolomic, immune-profiling) signatures in PEM+ vs PEM- subsets of the same cohort using the same platform with fatigue severity adjustment. McGregor2019 comes closest but lacks this control. The assumed superiority of PEM-required definitions for mechanistic studies rests on indirect inference (AHRQ evidence review for CBT/GET; case series; expert consensus). It is possible that PEM reflects severity rather than a distinct mechanism, in which case controlling for severity rather than requiring PEM might achieve the same biological enrichment.
- Conflicting: Talla2023 (RECOVER serum proteomics) identifies two inflammatory subgroups and a non-inflammatory subgroup in long COVID patients who may not all have PEM, suggesting molecular heterogeneity exists even within a broad long COVID definition — consistent with the PEM requirement improving coherence but not being the only driver.
- **t044 update (interpretation:0007, paper:Maestri2025, 2026-06-23):** The highest-feasibility route to *compute* the decisive severity-vs-PEM molecular test — convert STOP-PASC/Maestri2025's protein-vs-PEM regression (n=152, Olink Explore HT) to a severity-adjusted contrast — was attempted and **blocked**. Maestri2025 *does* map the plasma proteome onto PEM severity and finds a symptom-resolved signal (PEM ↓IL1RL1/IL1R2, distinct from the fatigue/cardiovascular ↑LEP/F7/F12 and dyspnea ↓CD38 signatures), but its models are **univariate proportional-odds regressions on each symptom's ordinal Likert severity, adjusted only for batch plate** — there is **no overall-severity covariate**, and with 110 proteins tracking a shared trend across ≥3 PROs the PEM signal is not separated from general severity. The individual-level matrix needed to refit with a severity covariate is gated ("Olink data available upon publication"; analysis repo 404 as of 2026-06). Net: the decisive test **remains uncomputable from public data**; a weak symptom-resolved increment was recorded (`evidence-line:0036` → `proposition:0011`). Reopen when STOP-PASC releases data, or pursue route (b) on RECOVER/IMPACC.
- **t061 update (interpretation:0027, 2026-06-26):** route (b) was triaged. No public runnable vehicle
  exists. STOP-PASC remains blocked (stated GitHub repo still 404); RECOVER-Adult is the best
  controlled-access route because it has participant-level symptom data and dbGaP/BioData Catalyst access
  paths, but it is not locally computable without a data-access request and omics-module confirmation;
  IMPACC/SDY1760 is controlled and multi-omic but hospitalized-only and not an admissible validated
  PEM-positive vs PEM-negative severity-adjusted vehicle on the currently documented phenotype surface.
- **t070 update (interpretation:0030, 2026-06-26):** RECOVER-Adult's current controlled-access release
  (`phs003463.v6.p5`) clears the phenotype side of the q0015 gate but not the molecular side. The public
  codebook exposes repeated PASC Symptoms fields, current PEM, and DePaul-style PEM bother/frequency/severity
  variables, and the release includes EHR, biospecimen-inventory, and wearable data. However, the public
  dbGaP surface does not expose selectable molecular datasets, and the March 2026 release notes do not
  identify released omics matrices joinable to the symptom rows. RECOVER-Adult remains the right DAR/scoping
  route, not yet a runnable severity-adjusted PEM molecular vehicle.
- **t025 synthesis (interpretation:0004, proposition:0011):** A three-pronged discovery sweep (PASC / ME/CFS PEM-stratified omics; PEM-vs-severity confound) confirms the within-cohort PEM+ vs PEM− molecular comparison this question needs **does not exist as of mid-2026** — it must be computed or commissioned, not found (McGregor2019 is the only true PEM-stratified omics design and it lacks severity adjustment). The sweep's substantive increment is `proposition:0011`: the objective correlate of PEM is **trigger- and endpoint-specific** — the ME/CFS whole-body 2-day-CPET decrement (Keller2014) does not transfer to long COVID (Gattoni2025) but a long-COVID lesion appears instead at the muscle level (Appelman2024). Net effect on this question: PEM-requirement plausibly improves *within-trigger* coherence but does **not** guarantee *cross-trigger* biological exchangeability, and the decisive severity-vs-PEM test remains unrun at the molecular level.

## Thoughts

- Best current interpretation: requiring PEM documentation, ideally by validated questionnaire (DePaul Symptom Questionnaire PEM subscale; DSQ-PEM) or provoked CPET, is the single highest-yield case-definition modification for biological coherence in ME/CFS and long COVID mechanistic studies. The evidence is indirect but consistent and supported by the mechanistic plausibility (energetic failure + immune exacerbation = distinguishable biological state).
- Major remaining uncertainty: the counterfactual — what molecular signatures would be found in a rigorously PEM-negative post-COVID cohort matched for severity? This experiment has not been done and would be the most informative next step.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (PEM is the operational proxy for the attractor state), `hypothesis:0003-immune-exhaustion-feedback` (PEM reflects immune exhaustion that worsens with activation), `hypothesis:h0011-mitochondrial-basis-of-pem` (mitochondrial failure underlies PEM).
- Required data or analyses: PEM+ vs PEM- proteomics/metabolomics comparison within a large RECOVER or IMPACC subsample; meta-regression of molecular effect size vs PEM prevalence across ME/CFS studies.
- Priority level: P2 — the answer would validate or challenge the PEM-requirement policy adopted in t001 and t016.

## Related

- Topic notes: `topic:pais-case-definition-heterogeneity`, `topic:biomarkers-and-objective-endpoints`, `topic:mecfs-long-covid-convergence`
- Article notes: Che2025, Thaweethai2023, Carruthers2003CCC, Carruthers2011ICC, Peppercorn2023, Hoel2026, Talla2023, McGregor2019, Gattoni2025, Keller2014, Appelman2024
- Methods/Datasets: DePaul Symptom Questionnaire (DSQ-PEM subscale); CPET as PEM provocation; RECOVER symptom-level data; IMPACC multi-omic data
