---
id: topic:population-boundary-conditions-and-effect-modifiers-in-pais
kind: topic
title: Population Boundary Conditions and Effect Modifiers of PAIS Risk, Phenotype, and Mechanism
status: active
ontology_terms:
  - effect modification
  - host reserve
  - immune homeostatic margin
  - immunosuppression
  - ancestral diversity
  - LMIC
  - frailty
  - inflammaging
  - atopy
  - mast cell activation
  - pregnancy immune milieu
  - infectious mononucleosis
  - EBV host history
  - generalizability
datasets: []
source_refs:
  - cite:Hammel2023
  - cite:Vinson2024
  - cite:Jassat2023
  - cite:Bruno2024
  - cite:Hickie2006
  - cite:Wolff2023
origins:
  - type: user
related:
  - question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
  - question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse
  - question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
  - question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
  - question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory
  - question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
  - question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais
  - topic:measurement-ascertainment-artifacts-in-pais
  - topic:pediatric-long-covid-and-misc
  - topic:menopause-sex-hormones-and-pais-risk
  - topic:shared-failure-mode-across-pais
  - topic:long-covid-immune-dysregulation
created: "2026-07-07"
updated: "2026-07-07"
added_by: "llm:claude-opus-4-8:research-topic"
---
# Population Boundary Conditions and Effect Modifiers of PAIS Risk, Phenotype, and Mechanism

## Summary

The mainstream long-COVID and PAIS literature is dominated by studies of high-income, European-ancestry,
immunocompetent adults, usually excluding or underrepresenting immunosuppressed patients, pregnant
individuals, frail older adults, those with pre-existing atopic or mast-cell-activation disorders, and
populations from low- and middle-income countries (LMICs). This topic homes six open questions
(q0031, q0032, q0033, q0034, q0040, q0051) that each represent a **population boundary condition**: a
host state so different from the modal PAIS study population that it constitutes a mechanistic probe.
The organizing logic is effect modification — these populations stress-test whether the project's
proposed shared mechanisms (the attractor hypothesis h0001, the severity-threshold and host-reserve
model h0004, the reproductive-stage immune-margin model h0005, and the ascertainment-artifact frame h0008)
hold across the actual range of human immune context. Where they do not, the divergence is scientifically
informative. The evidence base specific to each population in the post-infectious context is, with few
exceptions, thin to absent — this topic is as much a gap-map as a synthesis.

**Scope note.** Two already-housed topics cover instances of the same boundary-condition logic: pediatric
long COVID (`topic:pediatric-long-covid-and-misc`) and menopause/sex hormones
(`topic:menopause-sex-hormones-and-pais-risk`). Both are cross-referenced here as prior instances of the
same pattern; their content is not repeated. This topic's distinct contribution is the *class-level*
synthesis of the six new strata and the cross-cutting threads connecting them.

---

## Key Concepts

### Effect modifier vs confounder vs mediator

A variable is an **effect modifier** (or interaction term) when the causal effect of the triggering
infection on PAIS outcome differs across strata of that variable. The six host states here are
*candidate* effect modifiers: they alter the biological substrate on which the post-infectious cascade
unfolds. Distinguishing them from confounders (which must be controlled) and mediators (which sit on the
causal path) requires pre-specified DAGs and, ideally, stratified analyses within trials or longitudinal
cohorts. Most existing evidence collapses these distinctions.

### Immune homeostatic margin / host reserve

A recurring construct across the boundary populations: the "slack" in the immune system's capacity to
mount, control, and terminate an inflammatory response and return to baseline. The concept operationalises
hypothesis h0004 (severity threshold above which post-infectious state becomes self-sustaining) and
hypothesis h0005 (reproductive-stage transitions narrow this margin). Frailty, chronic immunosuppression,
and pregnancy each shift this reserve in different directions and by different mechanisms, and are
therefore natural experiments for the construct.

### Ascertainment heterogeneity across boundary populations

Several of these populations have systematically different ascertainment. LMIC populations have less
post-COVID clinical infrastructure and fewer cohort studies. Immunosuppressed patients are often excluded
from trials. Pregnant individuals are excluded from most PAIS cohorts during or immediately after
pregnancy. Frail older adults may have baseline symptom burden that mimics PAIS criteria, leading to
both over-inclusion (symptom conflation) and under-diagnosis (low healthcare-seeking). This connects
directly to hypothesis h0008 (ascertainment bias shapes apparent group differences) and to
`topic:measurement-ascertainment-artifacts-in-pais`.

### The shared-mechanism generalizability test

If a proposed mechanism (e.g., persistent antigen-driven immune activation per h0002; trained-immunity
reprogramming per h0004/h0010; autoimmunity per h0009) is truly shared across PAIS triggers and
populations, it should be detectable — at different magnitudes — in boundary populations. Populations
where a mechanism is blocked (e.g., immunosuppression partially blocking immune-activation cascades) or
amplified (e.g., pre-primed mast cells in atopic/MCAS hosts; low-reserve immune systems in frail
individuals) allow mechanistic dose-response reasoning that mainstream homogeneous cohorts cannot provide.

---

## Current State of Knowledge

### A. Chronically immunosuppressed hosts (q0031)

**General immunology (well established; belongs in health-immunity, flagged here for context):** calcineurin
inhibitors, mTOR inhibitors, and mycophenolate mofetil suppress T-cell activation, clonal expansion, and
de-novo antibody generation. Anti-TNF and other biologic DMARDs variably suppress innate and adaptive
immunity. These agents reduce but do not eliminate T-cell and NK-cell effector functions.

**In the post-infectious/PAIS context (limited; contested):** The most informative current data come from
solid organ transplant recipients (SOTRs). Vinson et al. (2024), using the National COVID Cohort
Collaborative (N3C), found SOTRs had significantly higher PASC rates than non-immunosuppressed patients
(2.2% vs 1.4%; adjusted OR 1.48, 95% CI 1.09–2.01) after propensity-score matching [@Vinson2024]. This
**counterintuitive result** — higher PASC in immunosuppressed, not lower — is mechanistically important.
At least three non-exclusive explanations are in play: (1) impaired viral clearance leads to prolonged
or higher antigen burden, amplifying the persistence mechanism rather than blocking it; (2) baseline
immune dysfunction and comorbidity burden in the transplant population creates a lower homeostatic reserve
independent of immunosuppression; (3) mycophenolate mofetil was independently associated with PASC in
this cohort, possibly via impaired antiviral B-cell responses. None of these explanations has been tested
in a design with immunosuppression intensity as the primary exposure gradient.

**Biologic-DMARD populations** (patients with RA, IBD, psoriasis, MS) are partially studied by mechanism
class, and a t109 literature pass (2026-07-07) retires the "essentially unstudied" flag *for the B-cell-depletion
and HIV sub-strata specifically*, while it survives intact for the other agents:

- **Anti-CD20 (rituximab) — now has mechanism data.** Chavatza et al. (2025) found that 26/225 (11.6%)
  rituximab-treated autoimmune-rheumatic-disease patients developed *persistent-relapsing* SARS-CoV-2
  infection (median ~65 days, up to ~361), with hypogammaglobulinemia in ~68% of events and — most
  informatively — lower-respiratory viral persistence (BAL PCR-positive in ~70.6%, with ~32.1%
  BAL-positive/nasopharyngeal-negative discordance) [@Chavatza2025]. This is a clean mechanistic natural
  experiment: B-cell depletion → impaired humoral clearance → prolonged/compartmentalized antigen
  persistence. It directly instantiates the *impaired-clearance* explanation for the SOT PASC paradox and
  links to the project's antigen-persistence frame (h0002). Caveat: the endpoint is persistent-relapsing
  *infection*, not a chronic-symptom PAIS phenotype.
- **HIV (chronic immune-exhaustion baseline) — now has mechanism data.** Peluso et al. (2022, AIDS;
  citekey `Peluso2022a`) found people with HIV on ART had ~4-fold higher odds of PASC (OR ~4.01, 95% CI
  1.45–11.1; ~82.8% vs ~54.4%), coupled with an exhaustion/dysregulation signature — ~70% lower relative
  SARS-CoV-2-specific memory CD8+ T cells and higher PD-1+ SARS-CoV-2-specific CD4+ T cells [@Peluso2022a].
  HIV thus operates as a boundary probe of a pre-existing exhaustion baseline (relevant to h0003) rather
  than pharmacologic immunosuppression per se.
- **Still genuinely empty:** anti-TNF, anti-IL-6R (tocilizumab), and JAK-inhibitor populations have **no
  long-COVID mechanism data** — the evidence for these agents is confined to acute-severity outcomes and
  attenuated vaccine-antibody responses. "Immunosuppression as a graded exposure" therefore remains
  unstudied as such for the non-B-cell, non-HIV agents, despite the mechanistic specificity that makes them
  attractive natural experiments (each blocks a distinct pathway). This residual gap is the priority target.

**Critical design gap:** existing SOT studies lack (a) severity-matched immunocompetent controls with
fine-grained severity gradients, (b) immunosuppression-intensity gradients as a dose-response variable,
and (c) cross-drug class comparisons. All are needed to disentangle immunosuppression type from
comorbidity burden from prolonged antigen persistence.

**UNVERIFIED claim to flag:** one frequently cited figure is that ~35–49% of SOTRs with COVID-19 develop
PASC (from smaller self-report cohorts), but these figures lack matched controls and may substantially
reflect background symptom burden or ascertainment bias. The N3C figure (2.2%) using coded diagnosis is
more conservative and better controlled.

---

### B. LMIC and ancestrally diverse populations (q0032)

**Epidemiological burden (some evidence; mostly indirect):** Jassat et al. estimated that the long COVID
burden in LMICs is likely severe and substantially under-documented [@Jassat2023]. The Lancet commentary
notes that most COVID-19 cases occurred in LMICs, yet most long-COVID cohort data come from high-income
European and North American studies. A South African longitudinal cohort reported 39% of participants with
persistent symptoms at 6 months (cited in Jassat2023), but sample size, case definition, and control
comparator issues limit inference. The Global Burden of Disease analysis shows Eastern Sub-Saharan Africa
had the highest age-standardized years lived with disability attributed to COVID-19 of any GBD region in
2020-2021, consistent with disproportionate post-COVID burden.

**Ancestral diversity in GWAS (limited; methodologically relevant):** The long-COVID GWAS literature has
identified loci in the HLA-DQ/ABO region among the top multi-ancestry associations. These loci are
not population-specific, but allele frequencies and linkage-disequilibrium structure differ across
ancestries. GWAS instruments developed in European-ancestry cohorts may not port to other ancestral
contexts. This is an active methodological limitation of any MR-based analysis of long COVID. A
multi-ancestry meta-analysis (Chaudhary et al. / 23andMe, 2024 preprint — European 42,899 cases, Latinx
8,631, African-American 2,234) reports three genome-wide-significant loci — HLA-DQA1/DQB, ABO, and a
**BPTF–KPNA2–C17orf58** signal beyond the HLA/ABO pair — plus genetic correlations with ME/CFS,
fibromyalgia, and depression; notably FOXP4 rs9367106 was *not* significant here. **Maturity caveat:**
this is a *preprint*, and 23andMe participants are largely US-based self-report — it broadens *ancestral*
diversity but is **not** an LMIC cohort and does not close the LMIC-mechanism gap (see follow-up task to
check for a peer-reviewed version before relying on it).

**Tonic immune modifiers in sub-Saharan Africa (mechanistic hypothesis; essentially untested in PAIS
context):** Populations with high endemic helminth burden have chronically Th2/IL-4/IL-10-skewed immunity
and elevated IgE. HIV co-infection in southern and eastern Africa is associated with baseline immune
exhaustion and CD4 depletion. Malaria-endemic regions have altered innate immune priming. Each of these
creates a distinct immunological starting point from which the post-COVID cascade would unfold. Whether
helminth-driven Th2 skew is protective (dampening Th1/autoimmune PAIS mechanisms) or harmful (amplifying
mast-cell/allergic PAIS mechanisms) is unresolved. There are no published PAIS mechanism studies from
these populations.

**Definitional and healthcare-seeking confounds (strong caveat):** LMIC populations may have lower
healthcare access for post-COVID symptoms, lower likelihood of being diagnosed with long COVID under
Western criteria, and different background symptom burden. These are major potential confounders in any
apparent prevalence estimate.

---

### C. Frailty and pre-frailty (q0033)

**General geriatrics (well established in general medicine):** Frailty is a state of accumulated
physiological deficit characterized by exhausted physiological reserves across multiple systems, including
chronic low-grade inflammation ("inflammaging"), depleted naive T-cell pools, skeletal muscle atrophy
(sarcopenia), and mitochondrial dysfunction. These hallmarks overlap mechanistically with the proposed
PAIS substrate.

**In the PAIS context (limited; epidemiological rather than mechanistic):** Hammel et al. (2023) analyzed
frailty as a PASC risk factor in **245,857** US veterans (July 2021–February 2022) using the **31-item VA
Frailty Index** (a deficit-accumulation index derived from EHR data — *not* the Fried frailty phenotype)
and the VA COVID-19 Shared Data Resource [@Hammel2023]. Frailty was associated with a ~40% increase in
PASC risk (adjusted HR 1.40, 95% CI 1.35–1.47) and pre-frailty with a ~17% increase (aHR 1.17, 95% CI
1.11–1.19), compared with robust individuals. The association held across both the Delta and Omicron
periods. This is *consistent with* frailty being an independent PASC predictor — the key test for hypothesis
h0004 (the threshold/reserve model predicts that those with lower baseline reserve should cross the
self-sustaining threshold at lower acute severity). **Caveat (t109 verification, 2026-07-07):** whether the
adjustment set explicitly included *acute-illness severity* (hospitalization/oxygen) could **not** be
confirmed from the abstract (full text was agent-inaccessible); the strong "independent of severity" reading
that h0004 leans on therefore remains **[UNVERIFIED]** pending a full-text check of the covariate list.

**The bidirectional coupling hypothesis (plausible; essentially untested as a PAIS claim):** PAIS may
itself deepen frailty — the post-infectious state could accelerate inflammaging, exhaust residual immune
reserves, worsen sarcopenia, and deepen dysautonomia in individuals who were already pre-frail. This
bidirectional coupling is clinically important (PAIS could accelerate frailty trajectories) but requires
longitudinal frailty-score data from before, during, and after PAIS episodes — data that do not currently
exist in any PAIS cohort.

**Mechanistic overlap (speculative):** Frailty shares T-cell exhaustion signatures, elevated IL-6 and
TNF-alpha, mitochondrial dysfunction, and low NAD+ with proposed PAIS mechanisms. Whether frailty creates
a lower threshold for the PAIS attractor (h0001/h0004) or whether it is a background state that makes
the same mechanisms more apparent/severe is a distinction that existing data cannot answer.

**Ascertainment issue:** frail older adults are often excluded from post-COVID studies due to cognitive
impairment, inability to complete self-report instruments, or attribution of symptoms to pre-existing
conditions rather than COVID-19. This means the frailty-PAIS interaction is underestimated in the
published literature.

---

### D. Pre-existing atopy and mast-cell-activation disorders (q0034)

**General immunology (established; health-immunity context):** In atopic individuals, IgE is elevated
and mast cells are constitutively sensitized. In MCAS, mast cells degranulate in response to triggers
that would be sub-threshold in non-atopic individuals, releasing histamine, prostaglandins, leukotrienes,
and pro-inflammatory cytokines.

**In the PAIS context (limited; correlational for atopy, sparse for MCAS):** Wolff et al. (2023)
conducted a systematic review of prospective cohort studies and found allergic diseases were associated
with increased risk of long-COVID symptoms [@Wolff2023]. The pre-existing atopy → post-COVID mast-cell
activation route is mechanistically distinct from post-COVID-onset mast cell activation (which the
project treats as a consequence of PAIS, per hypothesis h0002 territory): in atopic/MCAS individuals,
mast cells are already primed *before* the triggering infection.

**The mechanistic inversion:** standard PAIS models treat mast cell activation as a downstream consequence
of persistent antigen or immune dysregulation. In pre-existing MCAS, this ordering is inverted —
mast cells are the upstream amplifier of what would otherwise be a moderate post-infectious immune
perturbation. This predicts that atopic/MCAS individuals may develop PAIS at lower acute-illness severity
thresholds, have distinct histamine/prostaglandin-dominated symptom profiles (urticaria, flushing,
GI symptoms, hyperadrenergic POTS), and potentially respond to different therapeutic targets than
non-atopic PAIS individuals.

**Evidence maturity:** the Wolff2023 finding is atopy-population level (asthma, rhinitis, eczema), not
MCAS specifically. Pre-existing diagnosed MCAS is rare and poorly ascertained in general cohorts. Whether
elevated IgE or atopy diagnosis prospectively predicts PAIS incidence, rather than just symptom
*profile*, is not established.

**First mediator-level signal (t109, 2026-07-07; low maturity).** The MCAS-long-COVID literature has been
predominantly symptom-survey and hypothesis (the Weinstock/Afrin thesis: MCA symptom burden in long COVID
matches diagnosed MCAS by pattern, but with *no* mediator measurement). One recent study begins to supply
actual mediator data: Augustin et al. (2025, Open Forum Infectious Diseases, conference abstract) reported
that post-COVID-syndrome patients (PCS+, n=21) vs PCS− (n=11) had elevated ileal activated mast cells
(CD117+CD25+, p<0.0001), higher **serum tryptase** (p=0.020) and zonulin (p=0.024), and higher **ileal
SARS-CoV-2 spike protein** (p=0.014) despite undetectable *serum* spike — tying mast-cell activation to
gut antigen persistence and barrier dysfunction. **Maturity caveat:** conference abstract, n=21, not yet a
full peer-reviewed paper; treat as hypothesis-supporting, not confirmatory. It is nonetheless the first
long-COVID cohort with a tryptase readout and the first to couple the MCAS strand to the antigen-persistence
frame (h0002). The mediator-confirmed, MCAS-diagnosed long-COVID cohort remains near-absent.

---

### E. Pregnancy and peripartum immune milieu (q0040)

**General reproductive immunology (established; health-immunity context):** Pregnancy involves dramatic
immune remodeling: expanded regulatory T cells (Tregs), Th2/IL-4/IL-10 polarization, complement
activation, elevated progesterone and estradiol, and suppression of Th1/IFN-gamma responses to protect
the semi-allogeneic fetus. The postpartum window is a rapid immune reconstitution period — Th1 responses
rebound, autoimmune relapses are common, and the immune system returns toward pre-pregnancy setpoints
within weeks to months.

**In the PAIS context (limited; paradoxical findings):** Bruno et al. (2024), in the RECOVER EHR cohort
analysis of 19 US health systems (females aged 18–49 with confirmed SARS-CoV-2), found that COVID-19
infection acquired during pregnancy was associated with *lower overall* PASC risk at 30–180 days compared
with infection outside pregnancy [@Bruno2024]. However, the profile was qualitatively different: pregnant
individuals had higher risk for cardiac/vascular PASC components (abnormal heartbeat aHR 1.67; thromboembolism
aHR 1.88) and lower risk for cognitive and fatigue-predominant components (malaise aHR 0.35; cognitive
problems aHR 0.39).

**Mechanistic interpretation (speculative but tractable):** The Th2/Treg-dominant pregnancy immune
milieu may suppress the Th1/autoimmune and neuroinflammatory PAIS pathways while leaving the
thrombovascular and cardiac pathways relatively unshielded. If so, pregnancy provides a natural experiment
dissociating mechanism: Th2/Treg-dependent PAIS mechanisms (autoimmunity, IFN-driven neuroinflammation)
should be suppressed during gestation, while complement-driven and vascular mechanisms should be
relatively unaffected or amplified. This would sharpen hypothesis h0005 (reproductive-stage immune margin)
into a mechanistically specific prediction.

**Timing-window hypothesis (from q0040 notes):** the third-trimester tolerance window versus the postpartum
immune-reconstitution window may produce categorically different PAIS risk profiles if infection timing
interacts with the current immunological stage. No existing study has stratified by gestational week or
postpartum day to test this.

**Ascertainment issues (important):** pregnant individuals were systematically excluded from many PAIS
cohorts, and postpartum women have a background of fatigue, sleep disruption, and musculoskeletal
symptoms that overlap with PAIS criteria. The RECOVER-EHR finding requires validation in a cohort with
prospective phenotyping and adequate postpartum follow-up.

---

### F. Prior symptomatic EBV mononucleosis as a host-history PAIS risk amplifier (q0051)

**General virology and immunology (established):** EBV establishes lifelong latency after primary
infection. Symptomatic primary EBV (infectious mononucleosis, IM) is associated with a larger initial
viral expansion, more intense CD8 T-cell response, and possibly a larger residual latent reservoir
compared with asymptomatic primary EBV seroconversion. The CD8 T-cell economy after symptomatic IM is
altered long-term: IM patients maintain an expanded EBV-specific CD8 pool that can occupy 1–5% of
circulating T cells decades later.

**IM as a PAIS trigger (well established for ME/CFS):** The Dubbo Infection Outcomes Study (Hickie et
al. 2006) prospectively followed 253 patients through primary infections with EBV, Coxiella burnetii,
or Ross River virus [@Hickie2006]. Approximately 11% developed CFS criteria by 6 months, with no
significant difference in rate across pathogens, but with baseline illness severity as the strongest
predictor. This established EBV-induced IM as a PAIS trigger (not just a risk factor), consistent with
the project's multi-trigger frame.

**The HOST-HISTORY question (untested):** q0051 asks a distinct question from whether IM *triggers*
PAIS: does a *past history* of symptomatic EBV IM increase the risk of PAIS after a *subsequent*
triggering infection such as SARS-CoV-2? The mechanism would run through altered immune set-point — a
larger EBV latent reservoir, altered CD8 economy, or immunological "scarring" from the primary IM —
that facilitates more vigorous EBV reactivation, creates a heightened pro-inflammatory substrate, or
depletes immune reserve needed for post-COVID recovery. Current evidence ([@Peluso2022] showing that
concurrent EBV reactivation modifies long-COVID likelihood) is consistent with but does not test this
upstream host-history axis.

**Distinction from h0015 (critical):** hypothesis h0015 posits that EBV reactivation is a *consequence*
of PAIS rather than a primary driver. q0051 is about a *pre-infection host-history* variable that is
upstream of any reactivation event. These are complementary, not competing: prior IM could predispose
to EBV reactivation post-SARS-CoV-2 (the h0015 route), while simultaneously marking an altered immune
set-point from the primary IM encounter that independently contributes. Both axes need to be measured
in the same study for disambiguation.

**Evidence maturity:** the IM → ME/CFS literature is solid. The prior-IM → long-COVID-risk question is
untested. Reliable classification of past symptomatic vs asymptomatic primary EBV requires either
historical clinical records or cohorts with pre-infection serologic follow-up (e.g. student health
services or military induction cohorts).

---

## Cross-Cutting Threads

### Thread 1: All six are probes of the immune homeostatic margin construct

The immune homeostatic margin is the biological substrate most directly relevant to hypothesis h0004
(severity threshold) and h0001 (dysregulated attractor). Each boundary population shifts this margin
differently:

| Population | Direction of margin shift | Predicted PAIS consequence |
|---|---|---|
| Frailty/pre-frailty | Reduced (depleted reserves) | Lower severity threshold to cross h0004 threshold |
| Chronic immunosuppression (SOT) | Altered in complex ways: suppressed activation but impaired clearance | Net higher PASC rate despite suppression; likely reflects impaired clearance + low reserve |
| Pregnancy (third trimester) | Th2/Treg dominant; Th1 suppressed | Redirected PAIS phenotype: vascular/cardiac pathway preserved, neuroinflammatory pathway suppressed |
| Atopy/MCAS | Mast-cell primed; low degranulation threshold | Lower symptom threshold; distinct histamine-driven symptom profile |
| Prior IM | Altered EBV reservoir/CD8 economy; possible lower reserve | Amplified reactivation → h0015 route; possible independent immune-set-point effect |
| LMIC/helminth co-infection | Th2/regulatory skew; possible low baseline IFN-I | Uncertainty: protective vs amplifying depending on mechanism |

This table is a mechanistic hypothesis matrix, not an evidence-graded summary. Most cells are
speculative extrapolations from general immunology, not from PAIS-specific data.

### Thread 2: Ascertainment differentials predict apparent null/weak results in these populations

Hypothesis h0008 predicts that apparent group differences in PAIS prevalence and severity are shaped
by measurement and ascertainment channel. For boundary populations:
- **Immunosuppressed:** often excluded from trials; when included, comorbidity confounding is high
- **LMIC:** lower clinical infrastructure for PASC diagnosis, lower case definition awareness, lower
  healthcare-seeking — likely downward bias on apparent PAIS burden
- **Frail:** symptom attribution to comorbidities masks PAIS ascertainment; low self-report reliability
- **Pregnancy/postpartum:** systematic exclusion from cohorts; background symptom burden overlaps PAIS
- **Atopy/MCAS:** MCAS is under-diagnosed in general populations; overlap between MCAS triggers and
  PAIS symptoms creates misclassification in both directions

These ascertainment gradients predict that current apparent null/weak findings for boundary populations
are likely underestimates. Any analysis comparing PAIS prevalence across these strata must model or
bound ascertainment differentials.

### Thread 3: Pediatric and menopause populations are already-housed instances of the same logic

The `topic:pediatric-long-covid-and-misc` and `topic:menopause-sex-hormones-and-pais-risk` topics each
document a distinct developmental/hormonal host state as a boundary condition for PAIS. The pediatric
case shows that developmental stage shifts symptom profile (separate RECOVER indices by age band),
ascertainment approach (proxy vs self-report), and likely mechanism engagement (less severe acute
disease, less baseline autoimmune substrate). The menopause case shows how a reproductive-stage
transition narrows immune homeostatic margin (h0005) and creates symptom-overlap ascertainment problems
(h0008). Both follow the same logical structure as the six populations in this topic — and demonstrate
that the boundary-condition frame is productive: it has already generated falsifiable predictions
(Shah2025 RECOVER female-sex excess; Gross2024/2025 age-stratified pediatric indices) that would not
have been visible from a homogeneous adult cohort.

### Thread 4: Generalizability of the shared-failure-mode hypothesis

The project's core frame (h0001) posits a shared dysregulated attractor reachable from multiple
triggers. If this is correct, the same attractor should be reachable across the boundary populations
described here — at different thresholds and with different phenotypic coloring. If it is not (e.g.,
if immunosuppressed SOTRs develop a qualitatively different post-COVID syndrome than immunocompetent
adults), that divergence constrains the shared-attractor claim. The boundary populations are therefore
essential for hypothesis h0001 testing, not merely an appendix to it.

---

## Controversies and Open Questions

1. **The SOT PASC paradox:** Why do immunosuppressed SOTRs have higher coded PASC rates than matched
   immunocompetent controls? Three competing explanations are live: (a) impaired antigen clearance
   amplifies persistence-driven PAIS; (b) comorbidity/reserve depletion rather than immunosuppression
   is the driver; (c) immunosuppressive drugs (mycophenolate) independently compromise antiviral
   responses. These are not mutually exclusive, but they have different intervention implications.

2. **Pregnancy as a mechanism dissector:** The lower overall PASC rate but differentially preserved
   vascular PASC in pregnancy is either the strongest natural-experiment evidence for Th1/autoimmune
   mechanisms in PAIS (suppressed during pregnancy) or a significant ascertainment artefact (pregnant
   individuals may attribute fatigue and cognitive symptoms to pregnancy rather than COVID). This
   ambiguity requires resolution before the mechanistic inference is used.

3. **Frailty bidirectionality:** Frailty predicts higher PASC risk. But does PAIS cause frailty
   progression? The directionality question requires pre-infection frailty scores, which are only
   available in a small number of longitudinal aging cohorts with COVID follow-up.

4. **LMIC Th2/helminth protective hypothesis:** There is a plausible prior that helminth-driven Th2
   skew might suppress the autoimmune and IFN-I-driven pathways in PAIS. But the same skew amplifies
   mast-cell-driven pathways. The net effect is unknown and may depend on which PAIS mechanism dominates
   in a given population, which itself is unknown for LMIC cohorts.

5. **Prior IM as confounder vs upstream modifier:** Current-reactivation studies (which link concurrent
   EBV serology to long COVID risk) may be confounded by prior symptomatic IM. Unless the prior-IM
   exposure is measured and adjusted for, the apparent concurrent-reactivation effect may include
   a host-history component that is upstream of any reactivation event.

---

## Relevance to This Project

### Links to core hypotheses

- **h0001 (shared attractor):** The boundary populations are the primary stress-test for whether the
  attractor is truly shared or is a high-income, immunocompetent-adult-specific phenomenon.
- **h0004 (severity threshold / host reserve):** Frailty, immunosuppression, and MCAS all directly
  test whether a lower host reserve reduces the acute-illness threshold needed to cross into the
  self-sustaining PAIS state. Pregnancy tests whether a Th2-shifted reserve changes the *type* of
  PAIS rather than just the incidence.
- **h0005 (reproductive-stage immune margin):** Pregnancy is the most acute and mechanistically
  characterized instance of reproductive-stage immune remodeling. It extends h0005 beyond the
  menopause axis to an orthogonal, peripartum axis.
- **h0008 (ascertainment-bias shapes apparent group differences):** The boundary populations are
  exactly the strata with greatest ascertainment heterogeneity. Any comparative PAIS prevalence
  across these strata should be treated as ascertainment-confounded until quantified.
- **h0015 (EBV reactivation as consequence, not cause):** q0051 adds a pre-infection host-history
  axis that h0015 does not currently address. Prior symptomatic IM could be upstream of both PAIS
  onset and EBV reactivation, confounding both the h0015 test and the concurrent-reactivation
  literature.

### Project-boundary note

General immune mechanisms of immunosuppression, helminth-driven Th2 regulation, atopy, and pregnancy
immunology belong in `health-immunity`. This topic homes only the *post-infectious clinical syndromes*
in these populations and uses the general immunology as context, not as the primary content.

---

## Data Gaps and What a Cohort Would Need

This is a gap-statement only. **Dataset discovery has not been run and is NOT part of this task —
it is a sync-gated follow-up (see tasks/active.md t097).** Population-specific covariate requirements
are noted here to scope that future search.

### Strata hardest to source from open/downloadable data

- **Immunosuppressed / biologic-DMARD populations:** require EHR linkage with medication records (drug
  class, dose, duration) and severity-matched controls. UK Biobank, N3C, and OpenSAFELY have coverage
  but are gated/non-downloadable and subject to the reproducibility constraint in decision D-004. Summary
  statistics from consortia analyses (e.g., through COVID-19 HGI) may be the only compliant route.
- **LMIC cohorts:** mostly exist only as preprints, single-site convenience samples, or non-downloadable
  government surveillance data. A Kenya SARS-CoV-2 longitudinal cohort and a South African cohort are
  referenced in the literature but access/download status is unverified.
- **Frailty + PAIS longitudinal:** requires pre-infection frailty scores, which exist only in established
  aging cohorts (e.g., ELSA, HRS, SHARE) that would need COVID follow-up waves. These are partially
  public but access conditions vary.

### Minimum covariate set for boundary-population analyses

Across all six populations, an analysis would need: (1) confirmed triggering infection (not
self-reported); (2) timing of infection relative to host-state (transplant vintage, gestational week,
frailty assessment date, prior IM date); (3) acute illness severity with objective measure; (4) case
definition for PAIS applied consistently; (5) background symptom burden baseline; (6) duration of
follow-up; and (7) ascertainment comparability between strata.

**D-004 transparency bar:** any dataset discovery under t097 must apply the project's
third-party-reproducibility standard (core/decisions.md D-004): gated or non-downloadable data sources
(N3C, OpenSAFELY, UKB individual-level records) are below-bar / not admissible as primary evidence
vehicles. Dataset candidates should be pre-screened for downloadability and public access before
inclusion in a dataset plan.

---

## Key References

- Vinson2024: N3C propensity-score-matched analysis of PASC in solid organ transplant recipients; establishes paradoxically higher PASC rate in immunosuppressed SOTRs (2.2% vs 1.4%, aOR 1.48); mycophenolate mofetil independently associated (aOR 2.04). (Originally mis-keyed as "Frontera2024" with corrupt identifiers; corrected 2026-07-07.)
- Hammel2023: frailty as a PASC risk factor in US veterans (N=245,857; Delta and Omicron) using the 31-item VA Frailty Index (deficit-accumulation, NOT Fried); frailty aHR 1.40 (95% CI 1.35–1.47), pre-frailty aHR 1.17. Whether acute-illness severity was in the adjustment set is [UNVERIFIED] from the abstract (full-text follow-up t113); do not assert "independent of severity" until confirmed.
- Jassat2023: Lancet commentary on long COVID as a hidden public health crisis in LMICs; documents research gap and high observed burden in South African cohort.
- Bruno2024: RECOVER EHR cohort analysis; COVID during pregnancy associated with lower overall PASC but higher cardiac/vascular PASC and lower cognitive/fatigue PASC — a mechanistically informative dissociation.
- Hickie2006: Dubbo Infection Outcomes Study; foundational prospective cohort establishing that EBV-induced IM (and other pathogens) precipitates CFS-equivalent post-infectious syndromes at ~11%, with illness severity as primary predictor.
- Wolff2023: systematic review of prospective cohorts; allergic diseases prospectively associated with increased long-COVID symptom risk — atopy as a pre-existing susceptibility factor.

## Suggested Follow-up Research Tasks

- **Lit search for boundary-population PAIS mechanism papers — DONE (t109, 2026-07-07).** The six anchors
  were seeded/verified as paper entities (surfacing and correcting a mis-keyed citation: Frontera2024 →
  Vinson2024, and a Hammel2023 sample-size/instrument error). New mechanism papers were added for the
  immunosuppressed stratum: Peluso2022a (HIV/exhaustion-baseline) and Chavatza2025 (rituximab/antigen-
  persistence). **Residual gaps confirmed empty:** no LMIC-based PAIS *mechanism* cohort; no long-COVID
  mechanism data for anti-TNF / anti-IL-6R / JAK-inhibitor agents; mediator-confirmed MCAS long-COVID
  cohorts near-absent (one n=21 conference abstract). Follow-ups spun out: seed Augustin2025/Weinstock2021
  (MCAS) and the Chaudhary2024 multi-ancestry GWAS (pending peer-reviewed version); full-text-verify the
  Hammel2023 covariate list to resolve the [UNVERIFIED] acute-severity-adjustment that h0004 leans on.
- **Find-datasets pass (sync-gated, separate task t097):** identify open/downloadable cohorts for each
  of the six boundary strata. Pre-screen for third-party reproducibility compliance per D-004. Flag any
  gated-source candidates for explicit authorization decision.
- **DAG for compound boundary conditions:** formalize the causal structure of co-occurring boundary
  states (e.g., frail + immunosuppressed; pregnant + atopic) to determine whether compound strata
  require joint-modifier analysis or can be decomposed. See also q0057.
