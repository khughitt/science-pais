---
id: paper:synthesis-2026-07-10-long-covid-intake
kind: paper
title: 'Cross-paper synthesis (2026-07-10 intake): ascertainment, immunity debt, immune
  imprinting, host reserve, and post-viral cardiovascular disease across 17 long-COVID/PASC papers'
status: active
paper_kind: review
ontology_terms:
- long COVID
- PASC
- ascertainment bias
- selection bias
- immunity debt
- immune imprinting
- original antigenic sin
- host reserve
- comorbidity
- sex differences
- thromboinflammation
- post-viral cardiovascular disease
- IP-10
- CXCL10
dataset_usage: []
source_refs:
- cite:Nilforoshan2026
- cite:Sudre2024
- cite:Kahlert2023
- cite:Hou2025
- cite:Munro2025
- cite:Park2025
- cite:Furgier2026
- cite:Tsergas2025
- cite:Mak2025
- cite:Crotty2026
- cite:Chaulagain2026
- cite:Russell2023
- cite:Azhir2026
- cite:Skaarup2023
- cite:Nitz2025
- cite:Vacharathit2025
- cite:Mead2025
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0004-acute-severity-threshold
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais
- hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver
- hypothesis:0020-host-immune-baseline-reserve-gate
- topic:measurement-ascertainment-artifacts-in-pais
- topic:population-boundary-conditions-and-effect-modifiers-in-pais
- topic:innate-immune-memory-trained-immunity-in-pais
- topic:menopause-sex-hormones-and-pais-risk
- topic:thromboinflammation-and-endothelial-dysfunction
- topic:antigen-pathogen-persistence
- topic:long-covid-immune-dysregulation
created: '2026-07-10'
updated: '2026-07-10'
---

# Cross-paper synthesis (2026-07-10 intake)

This note synthesizes a 17-paper intake batch across six sub-themes. It is organized
by theme rather than by paper: for each theme it states the shared finding, the
tensions between papers, and the combined implication for the affected hypotheses.
Papers are referenced by citekey. Three cross-cutting tensions are flagged explicitly
where they arise — (a) hormone-axis vs. X-chromosome-dosage accounts of female PASC
bias; (b) the scope-creep risk of the immunity-debt papers, which are PAIS-*upstream*;
and (c) the contested, conflict-of-interest-laden Mead2025 preprint, cited here only as
a claim-to-scrutinize, never as support.

## Scope note (read first)

Two of the six themes are not about PAIS mechanism at all. Theme 2 (immunity debt)
characterizes the post-pandemic *exposure landscape* — who enters the acute-infection
funnel and at what severity — and Theme 5's vaccine-side paper (Nitz2025) concerns
acute post-vaccination events, not persistent post-infection sequelae. Both are kept in
the batch as comparators and boundary cases, but their findings must not be re-read as
direct PAIS evidence. See tension (b) below.

## Theme 1 — Ascertainment / measurement bias in long-COVID estimates

**Papers:** Nilforoshan2026, Sudre2024, Kahlert2023, Hou2025.

**Shared finding.** The apparent magnitude and persistence of long-COVID is heavily
shaped by *how cases and controls are ascertained*, independent of any biology.
Nilforoshan2026 is the keystone: on 14.4 billion claims from 244.7M US patients, simply
switching the comparator from never-tested controls to PCR-*negative* controls (its
"test-based prospective design") drops the negative-control-outcome false-positive rate
from 53.1% to 4.1%, cuts attributable outcomes by 83.5% at 30–120 days and 98.2% at
120–360 days, and returns the population mean to baseline by ~1 year. A negative-control-
*exposure* analysis shows PCR-negative individuals themselves carry elevated long-term
risk that correlates (Spearman r=0.48) with the effects conventional designs attribute to
COVID — direct proof that shared care-seeking vulnerability, not infection, drives much of
the conventional signal. Hou2025 (429 studies, >2M cases) supplies the population-scale
corroboration: pooled "ever" prevalence 36% globally but US "ever" (29%) vs. "current"
(8.7%) prevalence differ ~3-fold on ascertainment frame alone, and I²=100% heterogeneity
means the pooled figure averages incomparable definitions. Sudre2024 localizes the
mechanism to the *individual*: 32.6% of long-illness cases were already symptomatic
pre-COVID (OR 2.14 for any baseline symptom), and baseline symptom burden predicts
post-COVID burden (+5.6% per symptom) — a pre-morbid/reporting-continuity channel.
Kahlert2023 exposes a subtler ascertainment trap: its variant gradient (wild-type aRR
2.81 > Alpha/Delta 1.93 > Omicron 1.29 n.s.) is confounded by unequal follow-up windows
(18.3 vs. 3.1 months), so "variant effect" partly encodes time-since-infection recovery.

**Tensions.** (i) Nilforoshan2026's population-return-to-baseline is a *mean* under a
deliberately conservative RR≥1.1 + Bonferroni threshold that by construction misses
RR 1.0–1.1 effects (plausibly fatigue, cognition) and does not stratify by severity,
vaccination, or subgroup — so it cannot exclude a real, small, chronically-affected
stratum. Sudre2024 pushes the opposite way: 67.4% of long-illness cases were pre-COVID
*asymptomatic*, which constrains any pure-ascertainment reading — most long illness is not
confounded baseline-symptom continuation. (ii) Sudre2024 and Kahlert2023 are entirely
self-report; Nilforoshan2026 is claims-coded (billing events, not validated phenotypes).
The batch therefore brackets long-COVID between two non-overlapping measurement channels
that agree on direction but disagree on residual magnitude.

**Combined implication.** Strongly strengthens **h0008** (measurement-channel/ascertainment
bias predictably shapes apparent group differences): Nilforoshan2026 is the single largest
quantification yet of the M2 ascertainment-inflation cut, and answers question:0039
(negative-control-outcome bounding) empirically — the conventional design's ~50% false-
positive rate on biologically implausible outcomes is the bound. It also strengthens
**h0010** (slow heterogeneous recovery gradient, not a stable chronic attractor): 369
conventional 2-year associations collapse to zero on the corrected design. But the RR≥1.1
floor and the Sudre2024 asymptomatic-majority result jointly caution against reading either
as "long-COVID is mostly artifact" — the correct reading is that *a large fraction of the
claimed 2-year burden is ascertainment*, with a residual real subset the design cannot see.

## Theme 2 — Immunity debt & altered post-pandemic disease dynamics (UPSTREAM of PAIS)

**Papers:** Munro2025, Park2025, Furgier2026; Tsergas2025 as debate framing.

**Shared finding.** Post-NPI resurgences of endemic pathogens are largely explained by
population-level susceptibility accumulation ("immunity debt"), not individual immune
damage. Munro2025 (SIRS model + multi-country surveillance) shows a simple seasonal-forcing
compartmental model reproduces the whole cycle — annual waves, pandemic absence, one large
post-NPI overshoot, damped return — with no extra mechanism, and explicitly separates
population immunity debt from individual immune dysfunction. Park2025 (7 seasons, Korean
national surveillance) refines the shape: the resurgence is *not* an overall burden increase
but a *redistribution of severe disease* toward age cohorts that missed exposure windows
(school-age children for influenza; toddlers for RSV). Furgier2026 (9-year French ITS, 7,390
mastoiditis cases) gives the sharpest instance: +71.7% post-NPI mastoiditis, concentrated in
under-5s, driven by a +628% S. pyogenes surge that outlasted the general iGAS wave; crucially,
complication and surgery rates per case were *stable* — the excess is volumetric, not
severity-shifted per case.

**Tensions.** (i) **This is the scope-creep tension (b).** Munro2025 and Park2025 explicitly
label their own work PAIS-*upstream*: they characterize the acute-exposure landscape, not
post-infectious sequelae. None of the three measures a PAIS outcome; every PAIS link
(post-RSV, post-GAS, post-streptococcal ARF/PANDAS) is *inferred* through the severity gate,
not observed. The batch's temptation is to treat "more severe first infections in naive
cohorts" as "more PAIS" — a two-step inference (immunity debt → higher acute severity →
higher PAIS via h0004) with no direct evidence yet. (ii) Tsergas2025 (a BMJ *news feature*,
all quantitative claims UNVERIFIED) frames the live scientific debate: it argues immunity
debt is *insufficient* and that SARS-CoV-2 leaves durable immune "scars" (T-cell exhaustion,
HSPC epigenetic reprogramming, viral persistence). Its strongest counter-datum — invasive
GAS peaking 2021→2022 *after* precautions lifted, and infants too young to have accrued any
debt — sits in direct tension with Munro2025's pure-debt account and with Furgier2026's
debt-framed interpretation of the *same* GAS surge. Furgier2026 itself hedges: it cannot
separate immunity gap from emergence of a tropism-shifted M1UK-like clone.

**Combined implication.** These papers *contextualize* rather than test the project's
hypotheses. They lend population-scale support to the reserve/severity gate as an
epidemiological phenomenon (**h0020**, **h0004**) — Furgier2026's under-5 age gradient
literally instantiates a baseline-reserve gate across birth cohorts — and Munro2025's SIRS
code is a concrete modeling asset for question:0008 (vicious-cycle attractor formalization)
and h0010's damped-return analogy. The imprinting redistribution in Park2025 is conceptually
adjacent to h0009. But the honest verdict is: the immunity-debt-vs-immune-disruption question
(Tsergas2025 / question:0017) is *unresolved in this batch*, and the batch supplies no direct
measurement of post-RSV/post-GAS PAIS incidence. Treat as upstream boundary conditions.

## Theme 3 — Immune imprinting / immunological memory

**Papers:** Mak2025, Crotty2026; Chaulagain2026 (X-linked axis, cross-references Theme 4).

**Shared finding.** Prior immune history durably shapes the *quality* of the response to a
new antigen, and can do so for decades. Crotty2026 (field-defining 2026 memory review)
supplies the mechanistic ceiling: the pertussis wP-vs-aP example shows infant priming fixes
CD4 T-helper phenotype (T_H1 vs T_H2/T_H17) for decades despite repeated boosters — the
clearest human demonstration that early priming sets a durable, correction-resistant immune
"set point." It also establishes that tissue-resident memory (T_RM/B_RM) requires *local*
antigen encounter, so vaccine-only hosts lack mucosal T_RM that infection-experienced hosts
have. Mak2025 (47 LC vs. 41 HC) is the direct PAIS instance of original antigenic sin: LC
patients have *reduced* SARS-CoV-2 S1-specific IgG/IgA but *elevated* IgG against the
homologous seasonal betacoronaviruses HKU1/OC43, plus an elevated IgM/IgG ratio (impaired
class switching) — a humoral response deflected toward conserved, suboptimal epitopes.

**Tensions.** (i) Mak2025's single most important confound is a blood-draw timing mismatch
(LC sampled at median 280 days vs. HC at 596 days), across which variant exposure and antibody
waning differ — the imprinting signal is inferential (antibody ELISAs, no B-cell clonotyping)
and cross-sectional, so it cannot establish that imprinting *preceded* LC rather than being
shaped by it. (ii) Mak2025 finds elevated N-specific IgG despite undetectable serum SARS-CoV-2
RNA — pulling toward h0002 (tissue reservoir shedding N) — while simultaneously finding
*no* significant EBV antibody elevation and no serum EBV DNA, which supports h0015. (iii)
Crotty2026 is vaccine-centric and explicitly does *not* study how PAIS itself alters memory —
its imprinting relevance to PAIS is analogical, not measured.

**Combined implication.** Imprinting becomes a credible **candidate attractor-entry gate for
h0001**: OC43/HKU1-imprinted B-cell memory outcompeting naive S1-specific B cells → weaker
SARS-CoV-2 clearance → antigen persistence → attractor entry. This is a *mechanistically
specified* route into the h0001 attractor and a testable predictor (does pre-COVID HKU1/OC43
serology predict PAIS? — question:0071). Crotty2026 grounds the durability premise of **h0009**
(post-infectious set-point shift): wP imprinting proves decades-long antigen-free set points
are biologically real in humans, and long-lived B_PC homeostatic proliferation is a prototype
antigen-independent maintenance mechanism (adjacent to the trained-immunity branch of h0003).
On **h0015 (EBV as epiphenomenon)**: Mak2025's null serum-EBV result is *consistent* support
but underpowered and blind to mucosal/tissue reactivation — do not over-weight it. Crotty2026
also surfaces a standing, unmeasured confounder for all PAIS epidemiology: hybrid vs.
vaccine-only vs. infection-only *immunity type* at time of infection, which shapes mucosal
T_RM and IgA and is rarely recorded.

## Theme 4 — Host baseline reserve & effect modifiers

**Papers:** Russell2023, Azhir2026, Sudre2024 (cross-references Theme 1); Chaulagain2026 (sex).

**Shared finding.** Pre-infection host state — comorbidity burden, physiological reserve,
sex — gates PAIS risk substantially independent of the acute insult. Azhir2026 is the
strongest single result (133,792-patient MGB EHR cohort): after comorbidity adjustment each
decade of age is *protective* (OR 0.94), and causal mediation shows comorbidity (Charlson
index) accounts for 145% of the crude age effect (inconsistent mediation — comorbidity's harm
masks age's direct protection), while acute severity mediates only 12%. The direct protective
effect of age vanishes after 65, where reserve mechanisms exhaust. Russell2023 supplies the
mechanistic vocabulary: a three-phase model with a *resistance vs. tolerance* distinction,
where total multimorbidity burden (not any single condition) is the dominant severity predictor,
most comorbidities act via reduced tolerance/reserve, and Mendelian randomization separates
causal (obesity → adipositis → pneumonitis) from confounded (T2D — not independently causal)
associations. Sudre2024's comorbidity gradient (68.6% of long vs. 49.5% of short illness carry
≥1 comorbidity) is the community-cohort echo.

**Tensions.** (i) Severity's role is *demoted but not deleted*: Azhir2026 has severity mediating
only 12% of the age effect (subordinate to reserve), yet hospitalization (OR 1.35) and
ICU (OR 1.93) remain independently elevated — so h0004 survives as a genuine-but-secondary term
rather than the primary gate. (ii) Reserve is measured only by proxy (Charlson index, comorbidity
counts) — blunt aggregates built for mortality, not immunological reserve; the project's desired
biological proxies (inflammatory tone, naive-T fraction) are untested here. (iii) Azhir2026's
Black-males-under-45 exception (positive age estimate regardless of comorbidity) may be an
ascertainment/stratification artifact — reserve and ascertainment (h0008) are entangled in EHR
data.

**Combined implication.** Azhir2026 + Russell2023 are the batch's strongest support for
**h0020 (host baseline reserve gate)**: they operationalize reserve, rank-order PASC risk by it,
and provide a causal decomposition showing reserve dominates acute severity — with an empirical
regime-transition anchor at age 65. This *reweights* **h0004**: severity is real (survives MR
and hospitalization ORs) but is the subordinate term to reserve in explaining population-level
risk. Azhir2026's reinfection PASC-HR escalation (1.35 → 2.11 → 3.00 across 1/2/3+ infections)
also feeds h0001 as a possible "immunological scarring" lowering the re-entry threshold. The
severity-mediation decomposition (12% severity vs. 145% comorbidity) is the batch's cleanest
quantitative statement of how to split the reserve gate from the severity gate.

**Tension (a) — hormone axis (h0005) vs. X-chromosome dosage.** Chaulagain2026 (Nature
Immunology review) is the batch's sex-difference keystone and it actively splits the project's
h0005 framing. It presents *two orthogonal axes*: (1) gonadal steroids (ER/AR/PR on immune
cells) — the molecular substrate h0005 assumes — and (2) sex-chromosome dosage (X-linked gene
dosage, XCI escape of TLR7/KDM6A, XIST). Critically, it states that **"there is limited evidence
supporting a role for gonadal steroids in PASC outcomes so far,"** and that the female PASC
signal is instead carried largely by X-chromosome-dosage effects (XIST upregulation in female
PASC immune cells; TLR7 biallelic expression), with the *male* PASC cardiovascular phenotype
linked to Y-gene loss (DDX3Y/UTY). This partially *contradicts* the hormone-mediated core of
h0005 (its Proposition 0002) even as the female-40–55 PASC peak it reports is consistent with a
perimenopausal-transition window. The batch therefore does not adjudicate the sex-bias mechanism
— it *bifurcates* it, and the two accounts make different, testable predictions (hormone-timing
vs. genetic-sex/XIST). This is the single most important unresolved mechanistic fork in the
batch and motivates a decomposition study (see recommendations). Note also Chaulagain2026's
"immunopathology-vs-reduced-immunity polarity" tool: sex effects *reverse direction* depending
on which failure mode drives severity — a conceptual instrument the project should adopt.

## Theme 5 — Post-viral cardiovascular disease (infection-side vs. vaccine-side)

**Papers:** Skaarup2023 (infection-side, influenza), Nitz2025 (vaccine-side, COVID vaccines).

**Shared finding.** Infection and spike-antigen exposure both perturb a common
thromboinflammatory / endothelial space. Skaarup2023 (influenza→CVD review) frames a
two-pathway model — influenza-specific direct vascular/myocardial effects (endothelial
invasion, plaque destabilization, ectopic-trypsin cardiomyocyte entry, viral RNA detected in
arterial walls) plus *generic* systemic effects (hypercoagulability, adrenergic biomechanical
stress, hypoxemia) — and concludes the systemic, non-influenza-specific pathway dominates
(the same CVD elevation occurs after S. pneumoniae, CMV, HSV). Nitz2025 (166-article review of
COVID-vaccine CV events) characterizes the vaccine side: mRNA myocarditis (young males, 2nd
dose, 32–147/million in 16–29y males) and adenoviral VITT (anti-PF4 autoimmunity, young females
on OCP) — all *acute*, resolving within weeks, with infection carrying ~5–6× the myocarditis
risk of vaccination (RR 15–18.5 vs. 2–3.2).

**Tensions.** (i) **Scope boundary — infection vs. vaccine.** Nitz2025 is emphatic that every
event in its corpus is acute (max onset 90 days, no follow-up beyond 185 days) — by definition
*not* PAIS, which requires >12-week persistence. The entire vaccine-CV literature is silent on
the persistence dimension that defines PAIS. So the shared "thromboinflammatory space" is real
mechanistically (both present spike; both can trigger myocarditis and coagulopathy) but the two
papers sit on opposite sides of the PAIS scope line: Skaarup2023 is even itself acute-phase-only
(it does not address post-acute influenza CVD). (ii) Mechanisms only partly overlap: VITT
(anti-PF4 → platelet-FcγR) is distinct from the fibrinaloid-microclot mechanism (h0016) and from
post-infection complement/endothelial thromboinflammation — conflating them would be an error.
(iii) Skaarup2023 carries a Sanofi funding conflict (vaccine-prevention framing) and rests
heavily on animal models.

**Combined implication.** These papers populate the **thromboinflammation-and-endothelial-
dysfunction** topic and lend cross-trigger support to **h0001** (CVD-risk mechanisms are
pathogen-nonspecific → convergent node) and to **h0004/h0020** (Skaarup2023's "straw that breaks
the camel's back" for reduced-reserve HF patients is a literal reserve gate). The
infection-vs-vaccination myocarditis asymmetry (~5–6×) is a usable quantitative anchor for the
acute-antigen-burden proposition (proposition:0021): natural infection is the stronger
homeostatic perturbation. But the batch delivers *no* post-acute vaccine-CV follow-up and *no*
post-acute influenza-CVD data — the persistence question that would make either paper true PAIS
evidence is unanswered. The project needs an explicit scope-boundary ruling on whether
vaccine-adverse-event reviews (Nitz2025, and the previously-noted Bellavite2026) belong here as
comparators or in a sibling project.

## Theme 6 — Cytokine persistence & mechanism

**Papers:** Vacharathit2025, Mak2025 (cross-references Theme 3).

**Shared finding.** A subset of clinically-recovered, mild, vaccinated individuals carry a
persistent post-infectious immune-state displacement. Vacharathit2025 (114 patients across five
waves, longitudinal to 6–8 months) is the direct evidence: IP-10/CXCL10 stays 7–10× above
pre-pandemic baseline for 6–8 months after *mild Omicron breakthrough* — a persistence unique to
Omicron (earlier waves returned toward baseline by the same timepoints). Mak2025's humoral
findings (Theme 3) are the antibody-compartment complement: elevated N-IgG with undetectable
serum RNA.

**Tensions.** (i) The signal is *dissociated from symptoms*: Vacharathit2025 finds persistent
IP-10 does *not* correlate with Long COVID symptom scores at any timepoint — so sustained IP-10
is either sub-clinical attractor activation, a benign footprint, or a vaccine-induced innate
priming epiphenomenon; the study cannot tell which. (ii) **Antigen-driven vs. sterile-innate is
unresolved by design.** Vacharathit2025 measures IP-10 (an IFN-γ/TBK1-IRF3-downstream chemokine
shared by cGAS-STING) but no cGAMP, phospho-TBK1, type-I IFN, ISGs, or viral antigen — so it
*cannot* distinguish a sterile-innate loop (h0019) from ongoing antigen stimulation (h0002).
Mak2025's elevated N-IgG-without-serum-RNA leans antigen-persistence (h0002); Vacharathit2025's
persistent-IP-10-in-mild-recovered-hosts leans sterile-innate (h0019); the two papers are
individually compatible with *both* mechanisms and jointly do not adjudicate. (iii) Both cohorts
are small (Mak2025 n=47/41 with a fatal timing confound; Vacharathit2025 Omicron n=30, 19 vaccine
permutations) — every subgroup claim is preliminary.

**Combined implication.** Supports the *existence* of a persistent displacement consistent with
**h0001** (sub-clinical attractor state below the symptom threshold) and is *compatible with but
does not confirm* **h0019** (sterile cGAS-STING/NLRP3 sensing). It cannot resolve h0019 vs. h0002
without the missing markers (cGAMP/pTBK1/ISG panel + antigen/viral-load measures) — this is the
batch's sharpest "one measurement away" gap. Two incidental signals warrant tracking:
Vacharathit2025's individual-level anti-CoV-229E-IgG↔symptom correlation (R≈0.5, no group-level
elevation) as a heterogeneous-dysregulation marker feeding h0009, and its mRNA-inclusive-vaccine
↔ lower-symptom association (coef −0.86) feeding the h0020 reserve-modifier / question:0012
prevention arm. Mak2025's inverse CMV-p65-IgG↔fatigue correlation (r=−0.53) is a novel,
unexplained reserve-adjacent signal needing replication.

## Cross-cutting note on Mead2025 (contested preprint — claim-to-scrutinize only)

Mead2025 ("Hybrid Harms Hypothesis": mRNA-spike persistence for 2–3 years amplifying subsequent
infection harms; a "Post-COVID Vaccination Syndrome" re-attributing much of PASC to vaccination)
is a **non-peer-reviewed Preprints.org advocacy document** whose authors are affiliated with
organizations that campaign against COVID mRNA vaccination, several having faced professional
disciplinary action. Its methods respect no evidence hierarchy (VAERS, ecological correlations,
single-case-report outliers cited as pharmacokinetics; the "2–3 year persistence" rests on one
immunocompromised case). It is included in this synthesis **solely as a catalogue of contested
claims to stress-test under question:0017**, never as support for any project belief. Its one
defensible residue — that *vaccination history is an underexplored confounder/modifier in PASC
cohorts* — is independently and legitimately raised by Crotty2026 (immunity type) and
Vacharathit2025 (vaccine platform), and should be pursued through *those* sources, not Mead2025.
Do not cite Mead2025 as primary evidence for antigen persistence (h0002), NLRP3 activation
(h0019), or microclots (h0016).

## Batch-level threads

- **Ascertainment and reserve are entangled.** h0008 (Theme 1) and h0020 (Theme 4) are not
  independent: EHR/claims reserve proxies (Charlson index, comorbidity counts) are themselves
  ascertainment-shaped, and care-seeking is the shared confounder Nilforoshan2026 isolates.
  Reserve-gate results (Azhir2026) inherit residual ascertainment risk.
- **"One measurement away" gaps recur.** The batch repeatedly stops just short of adjudication:
  Vacharathit2025 lacks the STING/antigen markers to split h0019 from h0002; Nilforoshan2026
  lacks severity/subgroup stratification to test the residual-chronic-fraction; Mak2025 lacks
  B-cell clonotyping to prove imprinting; Chaulagain2026 lacks a design that separates hormone
  from X-dosage. Several high-value tasks are single, well-specified follow-on measurements.
- **Upstream vs. mechanism discipline.** Themes 2 and (vaccine-side) 5 are exposure-landscape and
  acute-event papers. Their value is as boundary conditions and comparators; re-reading them as
  PAIS mechanism is the batch's main interpretive hazard.
