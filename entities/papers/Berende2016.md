---
id: paper:Berende2016
kind: paper
title: Randomized Trial of Longer-Term Therapy for Symptoms Attributed to Lyme Disease
  (PLEASE)
status: active
paper_kind: ''
ontology_terms:
- post-treatment Lyme disease syndrome
- PTLDS
- antibiotic retreatment
- randomized controlled trial
- antigen persistence
- post-acute infection syndrome
- health-related quality of life
- Borrelia burgdorferi
- ceftriaxone
- doxycycline
- clarithromycin
dataset_usage: []
source_refs:
- cite:Berende2016
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- proposition:0020-antigen-clearance-rescues-established-pais
- question:0002-antigen-clearance-rescues-symptoms
- interpretation:0011-t046-antigen-clearance-trials-ingestion
- topic:antigen-pathogen-persistence
created: '2026-06-24'
updated: '2026-06-24'
---
# Randomized Trial of Longer-Term Therapy for Symptoms Attributed to Lyme Disease (PLEASE)

- **Authors:** Anneleen Berende, Hadewych J.M. ter Hofstede, Fidel J. Vos, Henriët van Middendorp, Michiel L. Vogelaar, Mirjam Tromp, Frank H. van den Hoogen, A. Rogier T. Donders, Andrea W.M. Evers, Bart Jan Kullberg
- **Year:** 2016
- **Journal:** New England Journal of Medicine, vol. 374, no. 13
- **DOI:** 10.1056/NEJMoa1505425
- **BibTeX key:** Berende2016
- **Source:** Europe PMC abstract + user-supplied design detail; LLM knowledge for widely-known quantitative specifics. PDF access blocked (HTTP 403); Unpaywall confirms OA copy exists at nejm.org but is agent-inaccessible.

## Key Contribution

The PLEASE trial is the largest randomized controlled trial of antibiotic retreatment for established post-treatment Lyme disease syndrome (PTLDS). In the Netherlands, 281 patients with persistent symptoms attributed to Lyme disease all received 2 weeks of open-label IV ceftriaxone (a shared induction phase), then were randomized to 12 additional weeks of oral doxycycline, oral clarithromycin plus hydroxychloroquine, or placebo. The primary outcome — SF-36 physical-component summary (PCS) score at the end of the 14-week total treatment period — did not differ among the three arms. Longer-term antibiotic therapy provided no additional benefit over placebo. Critically, all three arms improved from baseline, meaning the trial compares "more antibiotic vs less antibiotic" rather than "antibiotic vs no antibiotic"; the ceftriaxone induction confounds any interpretation of natural recovery.

## Methods

**Design.** Randomized, double-blind, placebo-controlled three-arm trial conducted in the Netherlands (ClinicalTrials.gov NCT01207739). All participants received open-label IV ceftriaxone for 2 weeks, then were centrally randomized 1:1:1 to 12 weeks of: (1) oral doxycycline, (2) oral clarithromycin plus hydroxychloroquine, or (3) matching oral placebo.

**Population.** Adults with persistent symptoms attributed to Lyme disease, defined as either (a) temporal relation to confirmed Lyme disease, or (b) positive IgG or IgM immunoblot for *Borrelia burgdorferi*. N = 281 randomized; 280 included in the modified intention-to-treat analysis (86 doxycycline, 96 clarithromycin/hydroxychloroquine, 98 placebo).

**Primary outcome.** Health-related quality of life measured by the SF-36 (RAND-36) Physical-Component Summary (PCS) score at the end of the treatment period (week 14). Scale range 15–61; higher scores indicate better quality of life.

**No antigen-clearance biomarker was measured.** The trial did not assay for residual *Borrelia* antigen, peptidoglycan fragments, or any other marker of pathogen persistence or antigen clearance before, during, or after treatment. Whether additional antibiotics modified any pathogen-derived molecular signal was therefore not tested.

## Key Findings

**Primary outcome: null.** SF-36 PCS mean scores at week 14 did not differ significantly among the three arms (P = 0.69):
- Doxycycline: 35.0 (95% CI 33.5–36.5)
- Clarithromycin/hydroxychloroquine: 35.6 (95% CI 34.2–37.1)
- Placebo: 34.8 (95% CI 33.4–36.2)

Pairwise differences: doxycycline vs. placebo 0.2 (95% CI −2.4 to 2.8); clarithromycin/hydroxychloroquine vs. placebo 0.9 (95% CI −1.6 to 3.3). Neither difference approaches clinical significance.

**Outcome also null at subsequent visits** (P = 0.35).

**All arms improved from baseline.** In every group, SF-36 PCS increased significantly from pre-randomization baseline to week 14 (P < 0.001). Because all participants received ceftriaxone before randomization, this within-arm improvement cannot be attributed to the randomized phase; it likely reflects regression to the mean, placebo response to the shared induction, and/or a modest response to ceftriaxone itself.

**Adverse events.** Four serious adverse events considered drug-related occurred during the 2-week open-label ceftriaxone phase; no serious drug-related adverse event occurred during the 12-week randomized phase. Adverse event rates were otherwise similar across arms.

## Relevance

**To `proposition:0020` (clearing antigen rescues established PAIS): weakly disputes, but uninterpretable.** This trial joins the long-COVID antiviral retreatment nulls (STOP-PASC, PAX-LC, outSMART-LC; `evidence-lines:0053–0055`) as cross-pathogen evidence that established-disease retreatment does not rescue symptoms. The shared pattern — treatment vs. extended treatment = no differential benefit — runs across SARS-CoV-2 and spirochaetal triggers and is the Borrelia-arm of the broader "late clearance doesn't rescue" signal.

**The null is uninterpretable for the same structural reason as the LC antibiotic trials.** No residual *Borrelia* antigen or peptidoglycan fragment was measured. The hypothesis requires that (a) antigen persists, (b) the antibiotic actually cleared it, and (c) clearance translated to symptom change. The trial tested only (c) — and only via the weak proxy that "more antibiotic = less antigen than less antibiotic." It never established target engagement. Per `interpretation:0011` and `discussion:0003`, a trial that does not demonstrate antigen clearance cannot adjudicate whether clearing antigen helps.

**The shared ceftriaxone induction further constrains interpretation.** The comparison is "2 weeks IV + 12 weeks oral antibiotic" vs "2 weeks IV + 12 weeks placebo," not "antibiotic vs. none." Both arms received a substantial antibiotic load. If 2 weeks of IV ceftriaxone already maximally suppressed replicating organisms (or already maximally cleared whatever antigen was clearable), additional oral therapy would be redundant regardless of whether antigen drives symptoms.

**Provides cross-pathogen support for the fixed-risk-factor-at-onset reconciliation.** The treatment-null + baseline-improvement pattern is consistent with the `proposition:0021` reading: antigen-load effects may be fixed at illness onset and become non-operative once a self-sustaining chronic state (cf. `hypothesis:0001`) is established. The Borrelia null is the bacterial-trigger echo of the SARS-CoV-2 antiviral nulls.

**Connects to `question:0002`.** The trial adds a second pathogen class (spirochaetal) and a methodologically strong three-arm RCT design to the "interventional tests exist and are null, but are uninterpretable" body of evidence characterizing that question.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Persistent Lyme disease symptoms | PTLDS as a PAIS | Canonical example of the shared PAIS phenotype; bacterial trigger |
| Additional oral antibiotics vs placebo | Proxy for antigen clearance (indirect) | Antibiotic administration ≠ demonstrated antigen clearance |
| Null on SF-36 PCS primary | Disputes `proposition:0020` (weak, uninterpretable) | Same structural limitation as LC antiviral nulls |
| Shared IV ceftriaxone induction | Complicates "antibiotic vs none" framing | All arms received substantial antibiotic exposure before randomization |
| No antigen biomarker | Target-engagement failure | No baseline antigen positivity confirmed, no clearance demonstrated |

## Limitations

1. **No antigen-clearance biomarker.** The defining methodological gap: whether extended antibiotics altered *Borrelia* antigen, peptidoglycan, or any persistence marker was not assessed. This is the same target-engagement failure that makes the LC antiviral nulls uninterpretable (`evidence-line:0054`, PAX-LC). A trial without an antigen endpoint cannot test whether clearing antigen rescues symptoms.

2. **Shared ceftriaxone induction.** The control arm is not a true antibiotic-naive comparator. The comparison is "more vs. less antibiotic," not "antibiotic vs. none." Any clearance effect achievable by antibiotic therapy may have been obtained during the 2-week IV induction; the 12-week oral comparison tests only whether incremental oral dosing adds benefit. A pre-treatment to post-treatment design without the ceftriaxone induction would be a more discriminating test of the antigen-clearance hypothesis.

3. **No enrichment for antigen-positive patients.** Enrollment was based on clinical diagnosis and serology, not on confirmed presence of residual *Borrelia* antigen or ongoing infection markers. An unknown fraction of participants may not have carried the antigen the retreatment was intended to clear. Parallel to STOP-PASC, where no baseline SARS-CoV-2 RNA was detectable.

4. **Case-definition heterogeneity.** The eligible population included both patients with temporally confirmed prior Lyme disease and those with only positive serology (IgG or IgM immunoblot), a broader definition that likely includes serologic positivity coincidental to the symptom syndrome. This inflates heterogeneity in the trial population and dilutes any effect that would apply only to true post-Borrelia sequelae.

5. **All-arms-improve confound.** The significant within-group improvement from baseline to week 14 in all arms — including placebo — complicates the interpretation of "treatment failure." Regression to the mean, placebo effects of the IV ceftriaxone induction, and natural PTLDS trajectory are indistinguishable. The trial demonstrates no *differential* benefit of additional antibiotics, but this is not equivalent to demonstrating that antibiotics are ineffective for the symptom syndrome.

6. **Primary outcome is patient-reported HRQoL.** SF-36 PCS captures broad physical well-being and is appropriate for this patient-centered question, but is subject to response shift and does not distinguish symptom subdomain changes that might be present in specific areas (e.g., fatigue, pain, cognitive function) that cancel at the composite level.

## Model / Tool Availability

None.

## Follow-up

- **Add `evidence-line:0058` (or next available)** against `proposition:0020` to formally encode this Borrelia-arm null in the project evidence graph — closing the gap flagged in `interpretation:0011` ("Borrelia/Coxiella clearance arm is unfilled").
- **Other PTLDS retreatment trials** (Klempner2001, Krupp2003, Fallon2008) form the full Borrelia-arm set; all should be ingested together to complete the cross-pathogen "late clearance doesn't rescue" pattern against `proposition:0020`.
- **Design implications for `question:0002`.** An admissible test of the antigen-clearance hypothesis for PTLDS would require: baseline antigen positivity confirmed (e.g., *Borrelia* peptidoglycan or DNA in tissue or plasma), demonstrated post-treatment clearance, and a symptom endpoint — analogous to the target-engagement admissibility gate being enforced for the LC antiviral trials (`interpretation:0011`).
- **Cross-pathogen generality check.** The Borrelia null + LC antiviral null + Q-fever immunomodulatory complex literature together provide the multi-pathogen "established disease retreatment is null" signal. If the fixed-risk-factor-at-onset reconciliation is correct, the same pattern should hold across all PAIS triggers where cleared infection still leaves residual antigen.
