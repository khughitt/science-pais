# t139 — Step 2b: batch-adjusted learnability gate (Gate 1a-adj)

- **Date:** 2026-07-18
- **Task:** `task:t139` · **Scope:** D-008 feasibility packet, **Step 2b (pre-target)**
- **Pre-registration:** `doc/plans/2026-07-18-t139-frailty-projection-feasibility-preregistration.md` — **Amendment 2**
- **Workflow:** `code/workflows/t139-frailty/` (run: `snakemake -s …/Snakefile --use-conda -c1 step2b`)

**Verdict: INCONCLUSIVE (borderline). Step 3 is NOT cleared by this result.** No PAIS
projection, no target label was touched — this is a pre-target training-side gate.

## Why this gate exists (Amendment 2)

Step 2 surfaced a **submission-batch ↔ contrast confound**: all **5 frail + 3 of 6
healthy-old** training donors are the **F0xx** submission (GSM4750xxx); the other **3
healthy-old** are the later **OH** submission (GSM5684xxx), which is also deeper (~12k vs
2.5–8k cells). The frozen Gates 3–4 cannot detect a *training-side* batch signature (Gate 3b
tests target-local technicals; unrestricted Gate 4a permutations break batch exchangeability),
and a batch-derived inflammatory signature can be biologically coherent *and* transfer. So the
only change is the design matrix, `~ frailty` → `~ submission + frailty`, which identifies the
frailty coefficient chiefly from the **within-F0xx 5-frail-vs-3-old** contrast (OH is old-only
and loads on the submission term).

## Result

| quantity | value | bar | reading |
|---|---|---|---|
| Adjusted signature | 200 genes (178 up / 22 down) | — | still hits the cap |
| **Adjusted LODO** median pairwise Jaccard | **0.521** | ≥ 0.50 clears; < 0.30 NO-GO | **clears** — a frailty signal *is* learnable under adjustment |
| Adjusted LODO reproducible genes (freq ≥ 0.8) | 127 | ≥ 20 | clears |
| **Signed overlap vs frozen primary** (Jaccard) | **0.311** | ≥ 0.50 clears; < 0.30 NO-GO | **borderline** — just above the batch-driven NO-GO floor |
| Shared signed genes / primary size | **95 / 200** (union 305) | ≥ 20 shared | direction-concordance **1.00** among shared |

**The two findings together are the whole story:**

1. **A frailty signature survives submission adjustment** (adjusted LODO 0.521, 127 reproducible)
   — so the primary signal is **not pure batch noise**; there is a within-F0xx frailty axis. This is
   why the verdict is **not a hard NO-GO**.
2. **But the primary signature is materially reshaped by the confound** — only **95 of 200**
   primary genes survive adjustment (signed Jaccard 0.311, barely above the 0.30 batch-driven
   floor). **~105 primary genes were carried by the between-submission difference, not frailty.**
   That is exactly a borderline batch contribution ⇒ **INCONCLUSIVE**, not a clean pass.

### The headline cytokine panel is now confirmed non-adjudicating

Step 2's face-valid inflammaging headline (**CSF3, IL6** top of the primary) does **not** lead the
adjusted signature: the adjusted top up-genes are **HBB, HBA2, INHBA, CXCL3, CSF2, RHCG, IFNB1**.
**IL6 and CSF3 drop out of the adjusted top rank.** Worse, **HBB/HBA2 (hemoglobin) now top the
adjusted signature** — a classic erythroid/reticulocyte **composition-contamination** signal that
adjusting for the OH-carried variance exposes within F0xx. Per Amendment 2 the cytokine panel was
already declared **non-adjudicating face validity until this gate clears**; it did not clear.

## Decision (frozen rule, Amendment 2)

Adjusted-LODO clears **but** signed overlap-to-primary is in the borderline band `[0.30, 0.50)` ⇒
**INCONCLUSIVE (borderline)**. Under the frozen GO/NO-GO rule a borderline Gate 1a-adj **halts the
packet before Step 3** — Steps 3–5 do **not** run on this result, and **no D-008b** is drafted. The
frailty signal is neither cleanly transferable-worthy nor a hard batch artifact on public data at
5-frail-vs-6-old (5-vs-3 once submission is honoured).

This does not move any scientific credence (`commits_to: []`): it says the *method* cannot be
trusted cleanly on this training vehicle without either a within-batch design of adequate power or a
cleaner single-submission frailty cohort.

## What a further amendment would need (not executed — user's call)

- The obvious within-batch primary (5 frail vs **3** F0xx-old only, dropping OH) is **lower** power,
  not higher, and would need its own amendment + power justification; it is unlikely to rescue the line.
- A single-submission (batch-free) donor-labelled frailty scRNA/pseudobulk training cohort of
  adequate size would be the principled fix, if one exists in public data.
- Absent either, the honest reading is that the frailty boundary-stratum line **joins IM and atopy as
  not-clearing on public data**, and the t110 boundary-conditions program closes.

## Reproducibility

`results/t139-frailty-feasibility/{signature_adjusted.tsv, gate1a_adj_verdict.json,
signature_adjusted_provenance.json}`. Same pinned inputs, env (`envs/r-sc.yaml`), and seed as Step 2;
the **only** analytic change is the added `submission` covariate. Deterministic.
