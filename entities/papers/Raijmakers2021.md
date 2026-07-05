---
id: paper:Raijmakers2021
kind: paper
title: 'No signs of neuroinflammation in women with chronic fatigue syndrome or Q
  fever fatigue syndrome using the TSPO ligand [11C]-PK11195'
status: active
ontology_terms:
- chronic fatigue syndrome
- Q fever fatigue syndrome
- neuroinflammation
- TSPO PET imaging
- microglial activation
- head-to-head comparison
source_refs:
- cite:Raijmakers2021
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
created: '2026-06-20'
updated: '2026-06-20'
---
# No signs of neuroinflammation in women with chronic fatigue syndrome or Q fever fatigue syndrome using the TSPO ligand [11C]-PK11195

- **Authors:** Ruud Raijmakers, Megan Roerink, Stephan Keijmel, Leo Joosten, Mihai Netea, Jos van der Meer, Hans Knoop, Hans Klein, Chantal Bleeker-Rovers, Janine Doorduin
- **Year:** 2021
- **Journal:** Neurology Neuroimmunology & Neuroinflammation, 9(1):e1113
- **DOI:** 10.1212/NXI.0000000000001113
- **PMCID:** PMC8611501
- **BibTeX key:** Raijmakers2021
- **Tier:** Core now
- **Source:** XML full text via Europe PMC (OA)

## Key Contribution

This study used [11C]-PK11195 PET neuroimaging — the same TSPO radioligand as the only prior positive neuroinflammation study in CFS (Nakatomi et al. 2014) — to test for microglial/astrocyte activation in both chronic fatigue syndrome (CFS) and Q fever fatigue syndrome (QFS) against healthy neighborhood controls. No significant neuroinflammation signal was detected in either patient group. The paper is notable for including two distinct etiological groups (idiopathic CFS and a well-defined post-infectious fatigue syndrome) in the same imaging protocol, making it a head-to-head cross-trigger design that produced a shared null result.

## Methods

**Design:** Cross-sectional PET neuroimaging study with three groups matched on age and neighborhood.

**Participants:** All-female sample — CFS (n = 9), QFS (n = 10), healthy subjects (HS, n = 9). Age range 18–59 years. Exclusion criteria: current psychiatric diagnoses (Mini-International Neuropsychiatric Interview), active medication beyond paracetamol/oral contraceptives, recent vaccination.

**Case definitions:**
- CFS diagnosed by Fukuda 1994 criteria at Radboud University Medical Center with CIS fatigue severity score ≥ 40 and SIP-8 ≥ 700. Median illness duration 240 months (CFS was notably chronic). No confirmed acute Q fever in the past; Coxiella serology not tested.
- QFS diagnosed by Dutch national QFS guideline: fatigue ≥ 6 months with sudden onset linked to a confirmed symptomatic acute Q fever infection; Coxiella PCR negative at imaging; IgG titers ≥ 1:16 but no acute-illness serologic pattern; somatic/psychiatric causes excluded; functional impairment defined by CIS ≥ 40 and SIP-8 ≥ 700. Median illness duration 84 months.
- HS: CIS ≤ 35, SIP-8 ≤ 450.

**Imaging:** [11C]-PK11195 PET on Siemens Biograph mCT with simultaneous arterial blood sampling; 60-minute emission scan. T1-weighted MRI (Siemens MAGNETOM Prisma) acquired same day for anatomic co-registration. Regions of interest defined by the Hammers atlas.

**Quantification:** Two-tissue compartment model with metabolite-corrected arterial plasma as input function; nondisplaceable binding potential (BP_ND = k3/k4) calculated with coupled cortical fitting. This is more methodologically rigorous than the reference-tissue approach used by Nakatomi et al. (who used cerebellum as a reference region, which is not devoid of TSPO).

**Symptom measures:** CIS (fatigue severity subscale), SIP-8 (functional impairment), BDI-PC (depression), CDC CFS Symptom Inventory (concomitant complaints subscale).

**Power:** Sample size estimated from the large effect sizes reported by Nakatomi et al. (Cohen d 1.4–2.4 across brain regions); n = 9 was calculated as sufficient to detect the Nakatomi-scale effect at alpha = 0.05, power = 0.80.

**Statistics:** One-way ANOVA for group comparisons; Pearson correlations between BP_ND and questionnaire scores.

## Key Findings

**Primary (null) result:** No statistically significant differences in [11C]-PK11195 BP_ND were found in any brain region — cingulate (rostral anterior, caudal anterior, posterior), hippocampus, thalamus, midbrain, or pons — when comparing either CFS or QFS patients with healthy controls. Point estimates for both patient groups tended to be *lower* than HS rather than higher, the opposite direction of the Nakatomi 2014 finding.

**Symptom–BP_ND correlations (exploratory; small n, multiple comparisons):**
- QFS: CIS fatigue severity correlated positively with BP_ND in multiple frontal, temporal, and parietal regions (r = 0.64–0.83); CDC complaint score correlated positively with brainstem, cingulate, insula, amygdala, and pons (r = 0.64–0.71).
- CFS: CDC complaint score and CIS fatigue severity correlated *negatively* with BP_ND in the caudate nucleus (r = −0.73 and −0.78, respectively).
- HS: no significant correlations.

The divergent correlation direction (positive in QFS, negative in CFS) is a secondary observation of uncertain interpretation and should be treated with caution given the small sample sizes and high multiple-comparison burden.

**Illness duration difference:** CFS patients had significantly longer illness at time of scan than QFS patients (240 vs 84 months median, p = 0.01). CFS patients also showed greater functional impairment on SIP-8 (p = 0.02). Fatigue severity, depression scores, and CDC complaints did not differ significantly between patient groups.

## Relevance

This paper is directly relevant to the t001 cross-pathogen track and sits at the intersection of `hypothesis:0001-shared-dysregulated-attractor` and `question:0001-shared-molecular-signature-across-triggers`. Its relevance is primarily *constraining* — it argues against one specific candidate mechanism (TSPO-defined microglial/astrocyte neuroinflammation) being a shared biological substrate of CFS and QFS.

**Relation to hypothesis:0001 (shared dysregulated attractor):** Hypothesis:0001 proposes that distinct triggers converge on a shared, self-sustaining pathophysiological state. Neuroinflammation is one of the candidate maintenance loops listed in the attractor model. This paper's null result in both CFS and QFS is ambiguous for the hypothesis: the *shared* absence across two triggers is formally consistent with convergence (both groups are at the same negative outcome), but it does not demonstrate a shared *positive* mechanism — it is a shared null, not a shared signal. Importantly, it argues specifically *against* TSPO-defined neuroinflammation as an active loop node in either syndrome, weakening the neuroinflammation arm of the attractor model without addressing the other proposed loops (autonomic dysregulation, mitochondrial impairment, immune activation, reduced cerebral perfusion).

**Relation to question:0001 (shared molecular signature):** The study tests one imaging-based biomarker in two triggers and finds no shared positive signal. This is a single, negative, small-sample data point against a shared TSPO-neuroinflammation signature — it contributes evidence that neuroinflammation is not part of whatever shared molecular signature exists, if any.

**Methodological note on comparing to Nakatomi 2014:** The prior positive study that motivated this work used the cerebellum as a reference region in reference tissue modeling. The current study uses arterial plasma as input for a two-tissue compartment model — a gold standard approach. The authors argue that methodological differences (reference region vs. arterial input; inclusion of males with mixed-sex CFS cohort; shorter disease duration in Nakatomi et al.) may explain the divergent results. If the Nakatomi signal was an artifact of the reference-region method, then the current null result should be viewed as the more credible estimate.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| CFS (Fukuda 1994) | ME/CFS / idiopathic PAIS | Fukuda criteria; not ICC/CCC — important case-definition caveat |
| Q fever fatigue syndrome (QFS) | Post-infectious PAIS (confirmed trigger) | Gold-standard post-infectious design: confirmed acute Q fever with serology |
| [11C]-PK11195 BP_ND | TSPO neuroinflammation signal | Binding potential = proxy for microglial/astrocyte TSPO expression |
| No significant BP_ND elevation | Negative evidence for neuroinflammation loop | Disciplines the neuroinflammation cell of the cross-pathogen mechanism matrix |
| Divergent symptom–BP_ND correlations across groups | Within-PAIS heterogeneity | CFS vs QFS diverge in correlation direction despite overlapping symptoms |

## Limitations

1. **Small sample (n = 9–10 per group).** Power was estimated for detecting a Nakatomi-scale effect (Cohen d ≥ 1.4); it cannot rule out smaller effects. A true modest neuroinflammatory signal could be missed.

2. **All-female sample.** Chosen to control for sex effects in a small study; QFS is only ~52% female in the population. Results may not generalize to male patients. The all-female choice also means this study cannot test the sex-modulation hypothesis (authors note inflammatory responses and neuroinflammation are generally higher in males).

3. **First-generation TSPO ligand.** [11C]-PK11195 is less sensitive than second-generation ligands ([11C]-PBR28, [18F]-DPA-714). Fibromyalgia and Gulf War Illness showed neuroinflammation with [11C]-PBR28 in studies with similar designs, suggesting the more sensitive ligand might yield different results. [11C]-PK11195 is also subject to low signal-to-noise due to high non-specific binding.

4. **CFS heterogeneity and unknown infectious antecedent.** Coxiella serology was not tested in CFS patients; no data on whether an acute infection preceded CFS in any patient. The CFS group may be etiologically heterogeneous, potentially including individuals with and without a post-infectious origin, diluting any subgroup signal.

5. **Chronic disease state.** CFS patients had a median illness duration of 240 months (20 years). If neuroinflammation is a transient early-phase phenomenon that wanes (consistent with Hornig et al.'s cytokine findings), it may have resolved by imaging in both groups. The authors themselves raise this hypothesis — TSPO expression may cycle through phases, and both groups may be in a refractory low-expression period.

6. **Multiple comparisons in correlation analysis.** The secondary symptom–BP_ND correlations involve a large number of region × questionnaire combinations with n ≈ 9–10. Significant correlations should be interpreted as hypothesis-generating only.

7. **Cross-sectional design.** Cannot assess whether neuroinflammation was present during or shortly after the acute trigger phase, nor how it relates to longitudinal trajectories.

8. **No TSPO genotyping.** TSPO binding of second-generation ligands is strongly affected by the rs6971 polymorphism (Ala147Thr). Though [11C]-PK11195 affinity is reportedly less allele-dependent, genotype was not assessed.

## Model / Tool Availability

None. No computational model, software tool, or dataset deposit associated with this paper. Data available on request from the corresponding author.

## Follow-up

- **Nakatomi et al. 2014** (J Nucl Med 55:945–950) — the prior positive CFS PET study this work attempted to replicate; key methodological comparison target.
- **Albrecht et al. 2019** and **Younger et al.** — cited context for [11C]-PBR28 neuroinflammation findings in fibromyalgia and Gulf War Illness; relevant for assessing whether a more sensitive ligand would change conclusions.
- **Hornig et al.** — duration-stratified cytokine study in CFS suggesting immune signature wanes after ~39 months; relevant to interpreting the null in chronic-stage patients.
- A replication using [11C]-PBR28 with TSPO genotyping, broader n, and earlier disease stages (< 3 years) would be the definitive follow-up for this null.
- Consider whether a longitudinal early-versus-late design could test the waning-neuroinflammation hypothesis explicitly, which would bear directly on whether neuroinflammation is a transient initiating mechanism vs. a chronic loop in the attractor model.
