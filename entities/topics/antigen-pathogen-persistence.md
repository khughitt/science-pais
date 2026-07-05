---
id: topic:antigen-pathogen-persistence
kind: topic
title: Antigen and Pathogen Persistence as a Driver of Chronic Post-Infectious Illness
status: active
ontology_terms:
- antigen persistence
- viral reservoir
- pathogen-associated molecular pattern
- peptidoglycan
- spike protein
- TLR2
- chronic immune activation
- post-acute infection syndrome
datasets: []
related:
- topic:shared-failure-mode-across-pais
- topic:long-covid-immune-dysregulation
- immunity:research-question:immune-homeostasis-and-dysregulation
source_refs:
- cite:Peluso2024
- cite:McClune2025
- cite:Skevaki2025
- cite:Morroy2016
- cite:Hanson2023
- cite:Vreeman2025
- cite:Peluso2024b
created: '2026-06-11'
updated: '2026-06-11'
---
# Antigen and Pathogen Persistence as a Driver of Chronic Post-Infectious Illness

## Summary

Antigen or pathogen-fragment persistence is the most mechanistically attractive candidate for a *pathogen-agnostic* PAIS driver: residual antigen could chronically stimulate immune cells, sustaining the non-resolving inflammation documented in the immune-dysregulation literature even after replicating pathogen is cleared. The evidence is strongest for direct detection of persisting material — SARS-CoV-2 spike/S1/nucleocapsid in plasma months to >1 year post-infection (Peluso2024), and Borrelia peptidoglycan accumulating in tissue after bacterial clearance with a molecular signature overlapping long COVID (McClune2025). What is *not* established is the causal link to symptoms: Peluso2024 explicitly declines to test symptom association, and no interventional study has yet shown that clearing antigen resolves illness. The mechanism is therefore promising but not settled, and its cross-pathogen generality is the key open question.

## Key Concepts

**Direct antigen detection in long COVID.** Peluso2024 (Simoa digital ELISA, 171 pandemic-era + 250 pre-pandemic participants) detects SARS-CoV-2 spike, S1, and nucleocapsid in plasma of ~25% of survivors across timepoints up to 14 months, with antigen burden correlating with acute severity. Skevaki2025 reports spike detectable in ~60% of long COVID patients up to 12 months and frames immune-privileged reservoirs (gut, thyroid, CNS) as the persistence compartments [@Peluso2024; @Skevaki2025].

**Pathogen-fragment persistence beyond viruses.** McClune2025 shows polymeric *Borrelia burgdorferi* peptidoglycan (pPG^Bb) uniquely accumulates in murine liver for weeks-to-months after clearance — retained by Kupffer cells and hepatocytes via unusual G-G-anhM glycan chemistry — driving liver proteome change, AST/ALT elevation, PBMC energy-metabolism suppression, and a signature overlapping long COVID patients (p=0.00038). Morroy2016 invokes an analogous "immunomodulatory complex" hypothesis for Q-fever fatigue syndrome (non-viable *Coxiella* DNA/antigen impairing macrophage clearance). Hanson2023 argues for enterovirus tissue reservoirs (gut VP1/RNA) as the persistence source in classical ME/CFS [@McClune2025; @Morroy2016; @Hanson2023].

**Antigen as an integrin agonist / fibrosis driver.** Vreeman2025 establishes that SARS-CoV-2 spike acts as an αvβ6-integrin agonist activating TGF-β; combined with tissue spike persistence this creates a testable link from antigen persistence (mechanism 1) to organ-level fibrotic failure (mechanism 4).

**Antigen persistence as the "necessary but maybe not sufficient" node.** Peluso2024b (Cell review) places viral persistence first among seven upstream drivers and identifies the *absence of a validated surrogate biomarker* of antigen/immune-activation burden as the single biggest bottleneck to PAIS therapeutic development.

## Current State of Knowledge

### What the evidence supports

- Pathogen-derived material genuinely persists after apparent clearance in at least two PAIS: SARS-CoV-2 antigen in plasma (Peluso2024, Skevaki2025) and Borrelia peptidoglycan in tissue (McClune2025).
- Persisting fragments are biologically active: pPG^Bb alters host proteome and suppresses PBMC energy metabolism, with overlap to long COVID signatures (McClune2025); spike can activate TGF-β via integrins (Vreeman2025).
- A structurally analogous "residual non-viable fragment impairing immune resolution" mechanism is independently proposed for viral, bacterial, and spirochaetal triggers (Peluso2024, McClune2025, Morroy2016, Hanson2023), giving the persistence hypothesis cross-pathogen reach.

### What is contested or unresolved

- **Causality.** No study links antigen burden to symptom severity prospectively, and Peluso2024 deliberately stops short of it. Antigen could be an epiphenomenon of slower clearance rather than a driver.
- **Interventional test missing.** The decisive experiment — does antigen clearance (e.g. nirmatrelvir/ritonavir in RECOVER-VITAL) rescue symptoms — has not returned a clear positive; if antigen drives illness, clearance should attenuate it.
- **Generality unproven.** Whether SARS-CoV-2, EBV, and Coxiella exploit the same tissue-macrophage "sink" as Borrelia (McClune2025's prediction) is untested.
- **Enterovirus reservoir replication.** Hanson2023 notes no full enterovirus genomes recovered and limited independent replication at scale.

### Tensions between papers

Hanson2023 argues for trigger-specific (enterovirus) persistence in classical ME/CFS and explicitly cautions against conflating it with post-COVID illness — a tension with the pan-PAIS "shared persistence mechanism" framing of McClune2025 and Morroy2016. The persistence model also competes with pure-autoimmunity and pure-tissue-damage explanations covered in the dysautonomia/autoimmunity topic; for PTLDS specifically, Wester2024 argues persistence may act *through* autoimmunity rather than directly.

## Controversies and Open Questions

- Does plasma/tissue antigen burden predict symptom severity and recovery within and across PAIS (Peluso2024, McClune2025)?
- Do other PAIS pathogens (SARS-CoV-2, EBV, Coxiella) accumulate in tissue-resident macrophages via the Kupffer-cell mechanism McClune2025 describes?
- Is TLR2 (for peptidoglycan) or integrin/TGF-β (for spike) the required transduction step linking persisting antigen to metabolic/fibrotic dysfunction?
- Is a quantifiable antigen-persistence index the validated surrogate endpoint the field lacks (Peluso2024b)?

## Relevance to This Project

Antigen persistence is the leading candidate for the pathogen-agnostic *initiating* node in the shared-failure-mode question (`topic:shared-failure-mode-across-pais`) and the upstream driver of the inflammatory signatures in `topic:long-covid-immune-dysregulation`. It directly motivates hypothesis `0002` (tissue-macrophage antigen-fragment reservoir as a cross-PAIS initiator) and bears on hypothesis `0001` by supplying a concrete mechanism that could either *seed* the attractor or *sustain* it. Links to `immunity:research-question:immune-homeostasis-and-dysregulation` for the chronic-antigenic-stimulation biology.

## Key References

- Peluso2024 — Simoa detection of persisting SARS-CoV-2 antigen in ~25% of survivors to 14 months; declines to test symptom link.
- McClune2025 — Borrelia peptidoglycan persists in liver post-clearance; host-proteome/metabolic effects overlapping long COVID.
- Skevaki2025 — spike detectable in ~60% of LC to 12 months; immune-privileged reservoir framing.
- Morroy2016 — Q-fever immunomodulatory-complex (non-viable fragment) hypothesis.
- Hanson2023 — enterovirus tissue-reservoir hypothesis for classical ME/CFS; cautions against over-generalization.
- Vreeman2025 — spike as αvβ6 integrin agonist activating TGF-β (persistence → fibrosis link).
- Peluso2024b — viral persistence as first upstream driver; surrogate-biomarker absence as key bottleneck.
