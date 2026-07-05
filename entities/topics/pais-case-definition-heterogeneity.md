---
id: topic:pais-case-definition-heterogeneity
kind: topic
title: PAIS Case-Definition Heterogeneity and Harmonization
status: active
ontology_terms:
- case definition
- long COVID
- ME/CFS
- post-exertional malaise
- PASC
- cohort heterogeneity
- harmonization
- prevalence
- post-treatment Lyme disease syndrome
- post-intensive care syndrome
datasets: []
source_refs:
- cite:WHO2021LongCOVID
- cite:NASEM2024LongCOVID
- cite:Thaweethai2023
- cite:IOM2015MECFS
- cite:Carruthers2003CCC
- cite:Carruthers2011ICC
- cite:Fukuda1994
- cite:Sharpe1991
- cite:Aucott2013PTLDS
- cite:Morroy2016
- cite:Munblit2022PCCOS
- cite:PCCOS2023COMS
- cite:Choutka2022
- cite:Bai2023
- cite:Gross2024
- cite:Gross2025
- cite:Stephenson2024
related:
- topic:mecfs-long-covid-convergence
- topic:shared-failure-mode-across-pais
- topic:biomarkers-and-objective-endpoints
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0004-acute-severity-threshold
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0001-shared-molecular-signature-across-triggers
- question:0007-mechanism-of-female-predominance-in-pais
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- interpretation:0021-t026-pc-cos-adoption-policy
- interpretation:0025-t009-pediatric-long-covid-and-misc
- topic:pediatric-long-covid-and-misc
created: "2026-06-19"
updated: "2026-06-26"
---

# PAIS Case-Definition Heterogeneity and Harmonization

## Summary

Post-acute infection syndromes (PAIS) are studied under a large and inconsistent family of case definitions — at least six distinct definitions for ME/CFS alone, several competing operationalizations of long COVID, and largely informal or absent criteria for most non-COVID PAIS. A substantial fraction of the apparent cross-study variation in prevalence estimates (ranging from 5% to >50% for long COVID), phenotypic composition, and reported mechanistic signals is definitional and sampling-frame-driven rather than biologically real. The single most consequential definitional split is whether post-exertional malaise (PEM) is required: definitions that omit PEM enrich cohorts with non-specific fatigue of varied etiology and systematically attenuate the mechanistic signals this project's core hypotheses depend on. This topic catalogues the major definition families, quantifies the prevalence swing caused by switching between definitions, and develops recommendations for the two downstream consumers blocked on definitional clarity: task t001 (cross-pathogen molecular signature test) and task t016 (menopause-PAIS total-effect analysis plan) [@WHO2021LongCOVID; @NASEM2024LongCOVID; @Thaweethai2023; @Fukuda1994; @Carruthers2003CCC; @Carruthers2011ICC; @IOM2015MECFS].

## Key Concepts

### Long COVID / PASC definitions

**WHO 2021 Delphi definition (Post COVID-19 Condition).** Developed through a Delphi consensus of 265 patients, clinicians, researchers, and WHO staff (published October 2021, Lancet Infectious Diseases). Core text: symptoms occurring in individuals with a history of probable or confirmed SARS-CoV-2 infection, usually 3 months from the onset of COVID-19, with symptoms lasting at least 2 months and not explained by an alternative diagnosis. Key features: (a) uses "3 months from onset" as the time anchor rather than resolution of the acute illness, (b) requires symptoms to persist at least 2 months, (c) no specific symptom list required — symptoms are listed descriptively, (d) intended as a working clinical definition. No explicit PEM requirement; no severity/functional impairment threshold. The ≥3-month from onset, ≥2-month persistence rule is more permissive than it appears: a patient still symptomatic at 3 months may qualify even if they will eventually recover [@WHO2021LongCOVID].

**CDC post-COVID definition.** The CDC operationalization does not set a fixed time threshold in the same formal way as WHO; in practice CDC and NIH documentation has used ≥4 weeks of persistent or new symptoms following acute COVID-19, making it the most permissive common threshold. This captures "ongoing symptomatic COVID-19" (NICE terminology) which may include a large fraction of self-limited prolonged recovery.

**UK NICE (NG188) two-phase split.** NICE distinguishes (a) ongoing symptomatic COVID-19: symptoms 4–12 weeks from onset; and (b) post-COVID-19 syndrome: symptoms ≥12 weeks not explained by an alternative diagnosis. The umbrella label "long COVID" encompasses both, but the 4-week threshold (NICE) vs 3-month/12-week threshold (WHO) creates a systematic 2-month divergence in who qualifies, dramatically inflating the denominator under NICE/CDC relative to WHO.

**NASEM 2024 definition.** The National Academies of Sciences, Engineering, and Medicine (June 2024 report, "A Long COVID Definition: A Chronic, Systemic Disease State with Profound Consequences") defines Long COVID as an infection-associated chronic condition (IACC) occurring after SARS-CoV-2 infection that is present for at least 3 months as a continuous, relapsing and remitting, or progressive disease state that can present as singular or multiple symptoms and/or diagnosable conditions. Key features: (a) ≥3 months as a continuous or relapsing-remitting state — explicitly including episodic cases that were excluded by some prior operationalizations, (b) no laboratory confirmation required, (c) framed explicitly as an IACC, aligning terminologically with Komaroff2025, (d) no specific symptom list or PEM requirement. Intended to harmonize clinical documentation, research, surveillance, and patient access to benefits [@NASEM2024LongCOVID].

**RECOVER/PASC Research Index (Thaweethai et al., JAMA 2023, 329:1934–1946).** Developed prospectively in 9,764 participants (89% SARS-CoV-2 infected, 71% female, median age 47) at 85 US sites in the NIH RECOVER cohort. Used LASSO-penalized logistic regression comparing infected vs. uninfected controls to identify 13 discriminating symptoms; the PASC index score is computed from symptom presence/severity with weights derived from the regression. Loss/change of smell or taste and PEM carry the largest individual weights. A score ≥12 (on a 0–44 scale) corresponds to a prevalence of ~23% in the infected cohort. Key features: (a) controls-referenced design means the index captures excess symptom burden relative to the unexposed rather than absolute symptom presence, (b) PEM is explicitly and heavily weighted, making this the most PEM-sensitive of the major research tools, (c) designed for research enrollment rather than clinical diagnosis, (d) iterative refinement intended, including pediatric and other subgroup versions [@Thaweethai2023].

**RECOVER pediatric PASC indices.** The pediatric RECOVER work operationalizes the "iterative refinement"
clause rather than reusing the adult index. Gross2024 derives separate research indices for school-age
children (6-11 years) and adolescents (12-17 years), with school-age signals weighted toward cognition,
sleep, GI/pain/skin features and school refusal, and adolescent signals weighted toward smell/taste,
pain, fatigue/malaise, exertional tiredness, cognition, headache, and lightheadedness. Gross2025 extends
the framework to early childhood (0-5 years), where observable/proxy-reported appetite, sleep, cough,
congestion, and low-energy features dominate. These indices are for research characterization, not
clinical diagnosis, and they make pediatric PAIS explicitly age-stratified [@Gross2024; @Gross2025].

**Threshold divergence summary.** The ≥4-week (CDC/NICE early long COVID), ≥12-week (NICE post-COVID syndrome / WHO), and PASC index (controls-referenced, PEM-weighted) produce qualitatively different study populations. A simulation using population-based UK ONS data found prevalence estimates ranging from ~5% (strict symptom-plus-impairment threshold at 12 weeks) to ~30–35% (any self-reported symptom ≥4 weeks), a 6-fold range from definition alone [@Peluso2024b; @WHO2021LongCOVID; @Thaweethai2023].

### ME/CFS definitions

**Fukuda 1994 (CDC criteria).** The foundational research case definition: (a) clinically evaluated, unexplained, persistent or relapsing fatigue for ≥6 months that substantially reduces prior activity; (b) concurrent presence of ≥4 of 8 additional symptoms (impaired memory/concentration, sore throat, tender lymph nodes, myalgia, multi-joint pain, new headaches, unrefreshing sleep, post-exertional malaise). PEM is one of eight interchangeable optional symptoms — it is not required. No functional impairment threshold beyond "substantial." Exclusions: active medical or psychiatric conditions that could explain fatigue. Widely used in pre-2003 ME/CFS research; still the dominant definition in many large-scale observational studies and clinical trials. Its permissiveness creates a heterogeneous research population, blending PEM-driven ME/CFS with prolonged depression, deconditioning, and other unexplained fatigue states.

**Canadian Consensus Criteria 2003 (CCC).** Carruthers et al., published as a 2003 consensus document. Requires: (a) fatigue with substantial loss of function; (b) PEM/post-exertional fatigue, specifically the characteristic worsening with minimal exertion; (c) sleep dysfunction; (d) pain; (e) ≥2 neurological/cognitive manifestations; (f) ≥1 symptom from ≥2 categories of autonomic, neuroendocrine, and immune manifestations; (g) minimum duration 6 months (3 months in children). PEM is mandatory and explicitly defined as characteristic worsening with minimal exertion. Selects a smaller, more severely impaired subset than Fukuda; concordance studies in the same cohort typically show 71% of subjects meeting Fukuda also meet CCC. CCC was designed for both research and clinical use and is widely preferred by the ME/CFS research community over Fukuda for mechanistic studies [@Carruthers2003CCC].

**International Consensus Criteria 2011 (ICC / ME-ICC).** Carruthers et al., Journal of Internal Medicine 2011. Replaces "fatigue" as the central feature with post-exertional neuroimmune exhaustion (PENE): a characteristic pattern of energy depletion following minimal physical, cognitive, or emotional stress, with reduced functional capacity and prolonged recovery ≥24h. Removes the CFS label entirely, preferring "myalgic encephalomyelitis." Additional required domains: neurological impairments (≥3 of 9 symptoms), immune/gastrointestinal/genitourinary impairments (≥1 of 6), and energy production/transport impairments (≥1). No duration criterion beyond establishing the pattern. Selects the strictest subset: in the same cohort comparison, ICC identifies ~61% vs Fukuda's 79%. ICC patients show more severe functional impairment and higher rates of sudden onset vs gradual. Not yet in widespread clinical use [@Carruthers2011ICC].

**IOM/NAM 2015 — SEID (Systemic Exertion Intolerance Disease).** Institute of Medicine (now National Academy of Medicine) 2015 report "Beyond Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: Redefining an Illness." Proposed the name SEID to communicate the core feature to clinicians. Required criteria: (a) substantial reduction in prior activities for ≥6 months with fatigue; (b) PEM; (c) unrefreshing sleep; plus (d) cognitive impairment or orthostatic intolerance (at least one required; both at moderate/severe intensity with moderate/severe frequency ≥half the time). PEM is mandatory and explicitly emphasized as required. Designed for clinical diagnosis (lowering missed-diagnosis rates) as well as research. SEID term has not been widely adopted; ME/CFS remains dominant. Concordance: ~72% of Fukuda-classified patients meet SEID in the same cohort, similar to CCC [@IOM2015MECFS].

**Oxford criteria 1991 (Sharpe et al.).** The broadest and most criticized definition: six months of debilitating fatigue (mental and physical) as the only required feature; psychiatric exclusions specified but no requirement for PEM, sleep dysfunction, neurocognitive symptoms, or autonomic features. Developed for research by a psychiatric-oriented panel. Used extensively in the PACE trial (the largest ME/CFS treatment trial) and UK/European CBT/GET trials. The core problem: the Oxford criteria operationalize "medically unexplained fatigue" rather than ME/CFS as defined by any post-2003 criterion. This means Oxford cohorts likely contain a large proportion of patients with primary depression, anxiety, deconditioning, or other fatigue states responsive to behavioral treatment, diluting or washing out the PEM-specific biological signal. The US Agency for Healthcare Research and Quality concluded in its 2016 evidence review that Oxford-criteria studies should be excluded from clinical guidance because they cannot be assumed to identify the same population as CCC or IOM/SEID. The PACE trial's apparently positive CBT/GET outcomes are now attributed in part to this definitional broadness; when Oxford-criteria studies are excluded, effects for GET and CBT in ME/CFS disappear or reverse.

**PEM as the pivotal criterion.** PEM is absent from Oxford, optional in Fukuda, required in CCC and SEID, and the cornerstone of ICC (as PENE). Whether PEM is required is the single highest-yield variable distinguishing biologically coherent ME/CFS cohorts from contaminated ones. Mechanistically, PEM implies a failure of cellular energy replenishment after exertion, which underlies the mitochondrial dysfunction and immunometabolic abnormalities central to `hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0003-immune-exhaustion-feedback`, and `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`. A cohort lacking PEM-positive cases dilutes these signals toward null, biasing against detecting the shared attractor.

### Other PAIS definitions

**Post-Treatment Lyme Disease Syndrome (PTLDS).** The Infectious Diseases Society of America (IDSA) proposed an operational research case definition (Aucott et al., Int J Infect Dis 2013; PMID 23462300): (a) documented antibiotic-treated Lyme disease (erythema migrans or confirmed late Lyme); (b) ongoing fatigue, widespread musculoskeletal pain, or cognitive complaints; (c) functional impact (SF-36 composite T-score <45); (d) onset after treatment; (e) duration ≥6 months. No PEM requirement. The definition is applied presumptively — attribution to Borrelia is confirmed by prior treated infection, not by ongoing pathogen detection. The IDSA/ILADS definitional disagreement (whether untreated seronegative Lyme exists) creates a second layer of diagnostic uncertainty that contaminates PTLDS cohort composition.

**Q-fever fatigue syndrome (QFS).** No internationally uniform formal definition exists (Morroy2016 emphasizes this as the field's major limitation). The operationalization most commonly used (Dutch Q-Fever Follow-Up Study and related work): (a) serologically confirmed acute Q-fever (C. burnetii antibody titers); (b) severe fatigue absent before infection or significantly increased; (c) duration >6 months; (d) exclusion of alternative explanations. No PEM requirement. Prevalence ~20% at 12 months post-acute infection, declining but persisting in a minority. QFS is the clearest pre-COVID "controlled natural experiment" for post-bacterial PAIS because the Dutch 2007–2010 outbreak provided a large, well-dated, serologically confirmed exposed cohort with prospective follow-up [@Morroy2016].

**Post-dengue fatigue syndrome.** No formal international case definition; studies use varied duration cutoffs (typically 6 weeks to 6 months post-dengue) and varied severity thresholds. Attribution is serologically or clinically confirmed dengue. Prevalence estimates range widely (10–40%) partly because of the inconsistent duration cutoffs. Hertanti2025 and Conde2026 both meta-analyze post-dengue fatigue but use different primary-study inclusion criteria, contributing to the non-independence problem identified in the project's question files [@Hertanti2025; @Conde2026].

**Post-SARS syndrome.** Retrospectively defined, based on residual symptoms (fatigue, weakness, sleep disorder, dyspnea) in the 2003 SARS cohort. No prospective formal criteria; Moldofsky2011 describes objective polysomnographic abnormalities (alpha-delta sleep anomaly) in chronic post-SARS patients as an operationalized objective endpoint, but case ascertainment remains symptom-based and retrospective.

**Post-Intensive Care Syndrome (PICS).** Formally defined by a 2012 SCCM multi-stakeholder conference (Needham, Davidson et al., Critical Care Medicine 2012): "new or worsening impairment in physical, cognitive, or mental health status arising after critical illness and persisting beyond acute care hospitalization." Domains are physical (weakness, functional limitation), cognitive (memory, attention, processing speed), and psychiatric (anxiety, depression, PTSD). PICS specifically requires prior ICU admission; post-sepsis syndrome is the dominant cause but not the exclusive one. No time threshold beyond "persisting beyond discharge." PEM is not defined as a feature. PICS is conceptually distinct from other PAIS in being severity-gate-defined (ICU admission required) rather than infection-type-defined; this creates a different kind of selection bias.

**Post-sepsis syndrome.** A more recent term (Fleischmann-Struzek, Molecular Medicine 2020) for the long-term morbidities of sepsis survivors without requiring prior ICU admission. Features: immune dysregulation, cognitive impairment, physical deconditioning, increased infection susceptibility, cardiovascular sequelae. No formal consensus case definition widely adopted; overlap with PICS is substantial for severe sepsis. Attribution to sepsis (rather than to the underlying comorbid conditions that predisposed to sepsis) is mechanistically difficult. Included in the PAIS conceptual umbrella but studied separately from infection-only triggered syndromes.

---

## Comparison Table

| Definition | Condition | Year | PEM required? | Time threshold | Functional impairment requirement | Intended use | Key criticism |
|---|---|---|---|---|---|---|---|
| WHO Delphi (Post COVID-19 Condition) | Long COVID | 2021 | No | ≥3 months from onset, symptoms ≥2 months | None specified | Clinical + research | Broad; no impairment threshold; allows large heterogeneous cohorts |
| CDC post-COVID | Long COVID | 2020+ | No | ≥4 weeks | None specified | Clinical surveillance | Most permissive; includes normal prolonged recovery |
| NICE two-phase (NG188) | Long COVID | 2020 | No | Ongoing: 4–12 wk; Post-COVID syndrome: ≥12 wk | None specified | Clinical UK | Week-4 threshold inflates surveillance prevalence |
| NASEM 2024 | Long COVID | 2024 | No | ≥3 months (continuous or relapsing-remitting) | None specified | Clinical + research + access | No PEM requirement; broad; episodic cases included |
| RECOVER PASC index | PASC (research) | 2023 | Yes (high weight) | Symptoms at ≥6 months post-infection | Controls-referenced excess | Research enrollment | Not a binary clinical criterion; score-based; may exclude mild cases |
| Fukuda 1994 | ME/CFS | 1994 | Optional (1 of 8) | ≥6 months | Substantial functional reduction | Research + clinical | PEM optional; heterogeneous cohorts; poor biological coherence |
| CCC 2003 | ME/CFS | 2003 | Yes (mandatory) | ≥6 months (3 months in children) | Substantial loss of function | Research + clinical | More specific than Fukuda; not universally adopted |
| ICC / ME-ICC 2011 | ME (not CFS) | 2011 | Yes — PENE (core feature) | None beyond pattern established | Severe functional limitation implied | Research (strict) | Most restrictive; small identified populations; limited clinical uptake |
| IOM/SEID 2015 | ME/CFS | 2015 | Yes (mandatory) | ≥6 months | Yes, moderate/severe, ≥half the time | Clinical + research | Name not adopted; criteria clear but concordance with CCC ~72% |
| Oxford 1991 | "CFS" | 1991 | No | ≥6 months | Yes, physical + mental | Research (historical) | Fatigue-only; includes primary depression; PACE trial controversy; AHRQ recommends exclusion |
| PTLDS (IDSA/Aucott) | Post-Lyme | 2013 | No | ≥6 months post-treatment | SF-36 T-score <45 | Research | Requires documented treated Lyme; no PEM; ILADS definitional dispute |
| QFS (Dutch operationalization) | Post-Q-fever | ~2012 | No | >6 months | Severe fatigue | Research | No international consensus definition; serologic confirmation required |
| Post-dengue fatigue | Post-dengue | Variable | No | 6 weeks–6 months (variable) | Variable | Research | No formal criteria; highly variable across studies |
| PICS | Post-ICU (including sepsis) | 2012 | No | Beyond ICU discharge | Yes, cognitive/physical/psychiatric impairment | Clinical + research | ICU-admission gate; excludes non-ICU sepsis; different selection mechanism |

---

## Current State of Knowledge

### What the evidence supports

**Definitional variation causes large prevalence swings.** Applying different long COVID definitions to the same population can produce 6-fold variation in prevalence estimates (e.g., ~5% vs ~35% in UK ONS-based simulations). For ME/CFS, applying the same four definitions (Fukuda, CCC, ICC, SEID) to the same clinical cohort yields: Fukuda 79%, SEID 72%, CCC 71%, ICC 61% — a 29-percentage-point range within one cohort without any change in the underlying patients. This is the strongest possible demonstration that prevalence is co-determined by definition choice [@Fukuda1994; @Carruthers2003CCC; @Carruthers2011ICC; @IOM2015MECFS].

**PEM requirement determines biological cohort coherence.** Definition families that require PEM (CCC, ICC, SEID, RECOVER index) select qualitatively different patient populations from those that do not (Oxford, Fukuda without PEM, WHO/NASEM/NICE long COVID, PICS). The ICC patients show higher rates of sudden onset, more severe immune suppression, and different pathobiological profiles compared to Fukuda-only patients in the same cohort. The RECOVER PASC index's heavy weighting on PEM makes it the most biologically coherent of the long COVID research tools.

**Oxford criteria drove the PACE-trial treatment-effect artefact.** When AHRQ's 2016 systematic review stratified trial results by case definition, GET and CBT showed apparent benefit only in Oxford-criteria cohorts; this effect was absent or reversed in CCC/ICC-based cohorts. This is the clearest documented case of definition-driven treatment-effect distortion in medicine, with direct relevance to this project's mechanistic investigations: a PEM-negative cohort enrolled under Oxford criteria will show attenuated metabolic/immune response to exercise challenge (cf. Che2025) because it contains patients without that biology.

**Sampling-frame differences compound definitional differences.** The t014 DAG analysis for the menopause-PAIS study (and the broader AGENTS.md guidance) identifies clinic-attendance as a collider: clinic-recruited cohorts systematically over-represent severe, help-seeking patients relative to population-based cohorts, independent of which case definition is used. This sampling-frame heterogeneity is additive to definitional heterogeneity and cannot be resolved by definition harmonization alone.

**Symptom-level data collection enables post-hoc re-definition.** Several large cohorts (RECOVER, IMPACC, ORCHESTRA) collected granular symptom-level data, enabling researchers to apply multiple case definitions post-hoc. This is a methodological best practice that the field is converging on, even if not always implemented prospectively.

### What is contested or uncertain

**Which single definition is "best" for research.** No consensus exists. CCC is preferred by most ME/CFS researchers for mechanistic studies; the RECOVER PASC index is currently the leading research tool for long COVID; but these are not interchangeable, and it is unclear whether they capture the same biological population. The NASEM 2024 and WHO definitions prioritize clinical access and breadth; they are not optimized for mechanistic research and are explicitly acknowledged to produce heterogeneous cohorts.

**Whether PEM-negative PAIS is a real biological subtype.** A minority view holds that there may exist a genuine post-infectious fatigue syndrome distinct from ME/CFS-like PAIS, which would be correctly captured by broader definitions. If true, restricting all long COVID research to PEM-positive cases would miss a real post-infectious phenotype. The counterargument (and the position this project's hypotheses favor) is that PEM-negative post-COVID fatigue is biologically heterogeneous and mechanistically uninformative.

**Whether a unified cross-PAIS case definition is achievable.** The PAIS concept spans viral, bacterial, and protozoal triggers, highly variable acute-illness severity, different organ tropisms, and vastly different case-ascertainment contexts. A single operational case definition that applies across long COVID, ME/CFS, PTLDS, QFS, and PICS is probably not achievable; what may be achievable is a common PEM-anchored symptom-domain framework that allows mapping across conditions.

---

## Controversies and Open Questions

- Are PEM-negative prolonged fatigue post-COVID and PEM-positive ME/CFS-like long COVID biologically distinct, or is PEM a severity marker within one continuum?
- Does requiring PEM-by-validated-questionnaire (e.g. DePaul Symptom Questionnaire PEM subscale) produce more biologically coherent cohorts than self-report PEM, and if so, what is the effect on sample size and generalizability?
- Can a single PAIS case definition be mapped across long COVID, ME/CFS, PTLDS, QFS, and post-dengue in a way that is both practically implementable and biologically meaningful?
- Do case definition differences explain the apparent sex-ratio differences across PAIS: i.e., does female predominance vary with PEM requirement (PEM+ cohorts vs PEM-negative broad cohorts)?

---

## Definitional vs Biological Variation: Analytical Core

### Mechanism by which broad definitions attenuate mechanistic signals

The core problem for computational and mechanistic studies is that a broad, PEM-permissive definition enrolls a heterogeneous mixture of post-infectious phenotypes: (a) PEM-driven ME/CFS-like PAIS (the biologically coherent target of most mechanistic hypotheses), (b) non-resolving normal acute illness (slow convalescence), (c) primary depression or anxiety triggered or worsened by the acute infection, (d) deconditioning, (e) new-onset or exacerbated chronic conditions (thyroid disease, diabetes), and (f) symptom misattribution (attributing pre-existing symptoms to the infection). When these subgroups are pooled, molecular signals specific to group (a) are diluted. For the project's core hypotheses:

- **h0001 (shared dysregulated attractor):** The attractor state is anchored by immune-metabolic feedback loops specific to persistent post-infectious immune activation. Pooling with group (c) and (e) adds biological noise that may obscure shared cross-PAIS signatures — the primary output of t001.
- **h0004 (acute-severity threshold):** Severity-threshold effects (hospitalization predicting PAIS) will be strongest in PEM-positive cohorts where the attractor is engaged; they will be diluted in broad cohorts where severe and mild convalescences are pooled.
- **h0005 (reproductive-stage modifier):** If menopause modifies the probability of entering the dysregulated attractor state (rather than prolonged normal recovery), studying this hypothesis in a broad definition cohort contaminates the exposure-outcome relationship with outcome misclassification.

### Effect of definition on cross-study prevalence comparisons

The well-documented prevalence range for long COVID (5–35%) is largely a definitional artefact rather than reflecting biological variation across time and populations. The apparent decline in long COVID prevalence with Omicron and vaccination (observed in multiple cohorts) reflects both genuine biology (milder acute illness) and shifting definition usage (stricter application, symptom-level changes in newer variants). Disentangling these requires studies that apply multiple definitions in parallel to the same population, which few have done [@Peluso2024b].

### Crosswalk and harmonization proposals

**Symptom-level data as the harmonization substrate.** Collecting individual symptom data at standardized severity/frequency thresholds (rather than a single binary case/not-case variable) allows post-hoc application of any case definition and computation of the RECOVER PASC index. This is the single highest-leverage harmonization action available prospectively. Retrospectively, it is rarely achievable.

**Core outcome set — PC-COS.** The Post-COVID Core Outcome Set (PC-COS) project, led by Munblit et al. (Lancet Respiratory Medicine 2022), used an international Delphi consensus to identify the minimum outcome domains that should be measured in adult long COVID / post-COVID condition research and clinical practice. The adult COS is broader than the common shorthand of fatigue, breathlessness, cognition, and quality of life: it includes fatigue/exhaustion, pain, post-exertion symptoms, work/occupational and study changes, survival, recovery, and cardiovascular, respiratory, nervous-system, cognitive, mental, and physical functioning/symptom/condition domains. This is **not a case definition**; it is an outcome-harmonization tool complementary to WHO/NASEM/RECOVER case-definition work.

**PC-COS instrument status — adopt domains, not a fixed battery.** The follow-on Core Outcome Measurement Set (COMS; PC-COS Study Group 2023) reached full instrument consensus only for survival (time until death), recovery (Recovery Scale for COVID-19), and respiratory outcomes (mMRC Dyspnoea Scale). For the other nine domains, the paper provides preferred candidate instruments rather than consensus mandates: e.g. FAS/FSS/FACIT-F for fatigue, DePaul Symptom Questionnaire for post-exertion symptoms, CFQ/MoCA-Blind for cognition, BPI for pain, and SBQ-LC/SF-36/EQ-5D-5L/WHO-DAS as multidomain candidates. Project policy (`interpretation:0021`) is therefore to pre-specify PC-COS **domains** where computable while recording instrument choice and no-consensus caveats.

**Multi-definition reporting as sensitivity analysis.** A well-established practice in ME/CFS research (and increasingly in long COVID) is to report results under multiple case definitions simultaneously. When effect estimates are robust across all definitions (e.g., a biomarker elevation present under both Fukuda and CCC), the finding is more reliable. When estimates differ markedly across definitions, the result is definition-specific and cannot be generalized. This practice should be adopted as standard in this project's computational outputs.

**PAIS-agnostic symptom domains.** The project's h0001 (shared attractor) and t001 (cross-pathogen signature) would benefit from a definition approach that captures PEM, unrefreshing sleep, orthostatic intolerance, cognitive impairment, and immune activation as separate outcomes rather than a single binary PAIS variable, allowing each to be modeled as a dimensional endpoint.

**Pediatric domain reporting.** Pediatric PAIS work needs developmental function alongside symptom
domains: parent/proxy report, child self-report where age-appropriate, school attendance/refusal,
developmental milestones, and impairment/quality-of-life scales. CLoCk's 24-month data show why this
matters: broad symptoms remain common across infection-status groups, while consistently meeting an
impairment-aware PCC definition over time identifies a smaller and more meaningful chronic-illness target.

---

## Relevance to This Project

### Blocking effect on t001 (cross-pathogen molecular signature test)

The central methodological challenge for t001 is definitional non-comparability across long COVID (various), ME/CFS (various), PTLDS, and post-dengue cohorts. Any cross-study molecular comparison risks conflating definition-driven phenotypic differences with biologically meaningful cross-pathogen signals. The recommended approach for t001:

1. **Require PEM documentation as a minimum eligibility criterion** for all cohorts entered into the cross-pathogen comparison. This applies the CCC/ICC standard across all syndromes, accepting the sample-size reduction.
2. **Report results stratified by definition family** (PEM-required vs. PEM-optional) as a mandatory sensitivity analysis, following the sensitivity-arbitration framework established in t016.
3. **Use symptom-domain outcomes rather than binary PAIS** wherever individual symptom data are available.
4. **Flag and exclude Oxford-criteria-only cohorts** from mechanistic analyses, consistent with AHRQ guidance.
5. If cross-syndrome samples cannot be restricted to PEM-positive cases, **model PEM as a covariate or interaction** to recover the PEM-positive signal.

### Concrete recommendation for t016 (menopause-PAIS total-effect analysis)

The analysis plan (2026-06-19 plan entity) identifies "Declare the single PAIS case definition for the outcome" as a blocking check before pre-registration (task t017, t002). This synthesis provides the following recommendation:

**Primary outcome definition for t016: WHO 2021 (Post COVID-19 Condition), ≥3-month threshold, operationalized as a validated composite score (RECOVER PASC index ≥12 if the cohort is RECOVER-compatible, otherwise the most PEM-weighted symptom instrument available).**

Rationale:
- The WHO definition is the most widely implemented across population-based cohorts (enabling maximum compatibility with the population-based, non-clinic-recruited cohort requirement in t016's sampling-frame gate).
- Adding the RECOVER PASC index or a PEM-weighted instrument as the operationalization captures PEM, which is the biologically critical criterion for the hypothesis being tested (h0005: reproductive-stage immune homeostatic margin altering probability of entering the attractor state — the attractor being operationalized as PEM-positive PAIS, not non-specific prolonged fatigue).
- The WHO ≥3-month threshold reduces inclusion of self-limited convalescence.

**Mandatory operationalization sensitivity:**
- Sensitivity 1: WHO ≥12-week threshold alone (binary, no symptom scoring) — most inclusive.
- Sensitivity 2: RECOVER PASC index ≥12 if available — most PEM-sensitive and biologically restrictive.
- Sensitivity 3: Functional-impairment requirement added (e.g., SF-36 composite T-score <45, as per Aucott PTLDS operationalization) — excludes symptomatic but functioning cases.

If effect estimates are robust across all three operationalizations, the finding is definition-stable. If the effect appears only under the broad WHO binary definition and disappears under the PASC-index operationalization, this is a signal that the observed association may be driven by PEM-negative prolonged recovery rather than the dysregulated attractor state, which would change the interpretation relative to h0005.

This multi-operationalization approach aligns with the sensitivity-arbitration discipline already established in t016's analysis plan.

**On the question of a single declared definition:** the analysis plan requires one declared primary definition (not silently pooling incompatible definitions). That primary definition is WHO ≥3 months + RECOVER PASC index score ≥12 (or closest available validated PEM instrument). The WHO ≥3-month binary is the fallback primary if the cohort does not support scoring.

---

## Well-Established vs Uncertain: Summary

| Claim | Evidence level | Notes |
|---|---|---|
| Different definitions produce substantially different prevalence estimates in the same population | Consensus / well-established | Multiple within-cohort concordance studies; UK ONS data |
| PEM requirement improves biological coherence of ME/CFS cohorts | Well-supported, converging consensus | AHRQ 2016 review; Carruthers CCC/ICC; RECOVER index weighting; Che2025 |
| Oxford-criteria studies contaminate ME/CFS treatment-effect estimates | Well-established in clinical guideline bodies | AHRQ 2016; NICE 2021 did not recommend GET for ME/CFS |
| Clinic-recruited vs population-recruited cohorts differ beyond case definition | Supported (DAG, AGENTS.md collider analysis) | Sampling-frame heterogeneity is additive to definitional heterogeneity |
| A single case definition best represents the shared attractor biology | Contested | No head-to-head multi-omics comparison of PEM+ vs PEM- post-COVID cohorts exists |
| PEM-negative post-COVID fatigue is a distinct biotype | Uncertain / minority view | Not ruled out; relevant to whether Oxford-style definitions miss or correctly identify a separate syndrome |
| WHO 2021 / NASEM 2024 definitions are optimal for research | Uncertain | Both are broad by design; RECOVER index is more research-optimized |

---

## Key References

- **Fukuda et al. (1994)** — Annals of Internal Medicine 121:953–959. Foundational CDC CFS case definition; PEM optional.
- **Carruthers et al. (2003)** — J Chronic Fatigue Syndrome 11(1):7–115. CCC: first PEM-mandatory research definition for ME/CFS.
- **Carruthers et al. (2011)** — Journal of Internal Medicine 270(4):327–338. ICC: PENE as the core feature; strictest ME subset.
- **IOM (2015)** — "Beyond Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: Redefining an Illness." National Academies Press. PEM-mandatory clinical definition (SEID).
- **Sharpe et al. (1991)** — Journal of the Royal Society of Medicine 84(2):118–121. Oxford criteria: fatigue-only; widely criticized.
- **WHO (2021)** — "A clinical case definition of post COVID-19 condition by a Delphi consensus." Lancet Infectious Diseases 22(4):e102–e107. Standard clinical long COVID definition.
- **NASEM (2024)** — "A Long COVID Definition: A Chronic, Systemic Disease State with Profound Consequences." National Academies Press. ≥3 months, IACC framing.
- **Thaweethai et al. (2023)** — JAMA 329:1934–1946. RECOVER PASC index; 13 symptoms; PEM/smell/taste highest weighted.
- **Aucott et al. (2013)** — Int J Infect Dis 17(4):e223–e227. Operational PTLDS research definition.
- **Morroy et al. (2016)** — PLOS ONE 11(5):e0155884. QFS systematic review; absence of uniform definition.
- **Munblit et al. (2022)** — Lancet Respiratory Medicine 10(8):715–724. PC-COS: core outcome set for long COVID.
- **Choutka et al. (2022)** — Nature Medicine 28:911–923. Cross-pathogen PAIS framing; four mechanistic hypotheses.
- **Bai and Richardson (2023)** — Chronic Diseases and Translational Medicine 9(3):183–190. PTLDS vs ME/CFS symptom overlap.
