---
id: evidence-line:0058-mcclune2025-borrelia-pg-tissue-persistence-bioactive-supports-0022
type: evidence-line
title: "McClune2025 shows Borrelia peptidoglycan persists in tissue post-clearance\
  \ and is biologically active — moderate support for fragment persistence"
status: active
stance: supports
target: proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
source: paper:McClune2025
strength: moderate
independence: independent
independence_group: mcclune2025-borrelia-pg-liver-reservoir
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
source_refs:
- paper:McClune2025
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: McClune2025 shows Borrelia peptidoglycan persists in tissue post-clearance and is biologically active — moderate support for fragment persistence

## What this line shows

McClune2025 (*Sci Transl Med*) demonstrates, in BALB/cJ mice, that polymeric *Borrelia burgdorferi*
peptidoglycan (pPG^Bb) accumulates in the **liver** (Kupffer cells *and* hepatocytes) and **persists for
weeks to months** after delivery or live infection — remaining >10-fold above background at 2 weeks and
still detectable at 4 weeks — whereas peptidoglycan from *E. coli*, *S. aureus*, and *D. radiodurans*
clears within 48 h. Persistence is therefore a property of the fragment's degradation-resistant chemistry
(the G-G-anhM terminal glycan contributes), not a generic PAMP behaviour. Crucially, the retained
fragment is **biologically active**: it drives liver-proteome remodelling, sustained serum AST/ALT
elevation (outlasting the detectable PG signal), TLR1/TLR2-signalling dysregulation, and **downregulation
of PBMC energy-metabolism genes** (TCA cycle / electron transport), with CCL19 and IL-23 upregulated.
This **directly supports `proposition:0022`** (degradation-resistant fragments persist post-clearance and
are bioactive) — it is the single strongest demonstration in the project that a non-viable pathogen
fragment can establish a persistent, bioactive tissue reservoir.

## Why it is independent

`independent` under `independence_group: mcclune2025-borrelia-pg-liver-reservoir`. It is a distinct
pathogen (Borrelia), compartment (liver), and assay (r-mAb2G10 PG ELISA + fluorescent tracking) from the
SARS-CoV-2 plasma-antigen line (`evidence-line:0059`, Peluso2024). The two lines persist *different*
fragment classes in *different* pathogen systems, so their agreement on the persistence claim is genuine
cross-pathogen corroboration, not shared-source. (It is also methodologically distinct from the disputing
PTLDS antibiotic-retreatment line `evidence-line:0060`, which is interventional/clinical, not a
persistence measurement.)

## Caveats / scope

`direct_test`, **moderate** — strong *within* its system but bounded as support for a pathogen-agnostic
human claim: (1) the persistence/bioactivity demonstration is a **mouse model**, and **no validated PTLDS
mouse model exists** — the dysregulated pathways "could generate" a PTLDS-like phenotype but behavioural/
symptom outcomes were not measured; (2) Kupffer/hepatocyte retention kinetics used **immortalized cell
lines**; (3) the PBMC energy-metabolism transcriptomics used **healthy-donor** cells stimulated ex vivo,
not PAIS-patient cells; (4) the human-tissue evidence (pPG^Bb in 27/30 Lyme-arthritis synovial fluids
after antibiotics) is a small, cross-sectional cohort; (5) the Long COVID proteome overlap (p = 0.00038)
is a molecular-signature convergence, not a demonstration that the same reservoir mechanism operates in
SARS-CoV-2 PAIS. The line establishes **persistence + bioactivity**, not causation of human chronic-illness
symptoms — that gap is carried by `question:0002` and h0002's still-untested discriminating predictions [@McClune2025].
