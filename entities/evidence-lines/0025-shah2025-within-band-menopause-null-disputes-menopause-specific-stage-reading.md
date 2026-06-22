---
id: "evidence-line:0025-shah2025-within-band-menopause-null-disputes-menopause-specific-stage-reading"
type: "evidence-line"
title: "Shah2025 within-age-band menopause null disputes a menopause-status-specific reading of the reproductive-stage threshold"
status: "active"
stance: "disputes"
target: "proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold"
source: "paper:Shah2025"
strength: "weak"
independence: "independent"
independence_group: "shah2025-lc-risk"
evidence_role: "model_criticism"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold"
  - "evidence-line:0001-shah2025-midlife-female-long-covid-excess-supports-stage-threshold"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "interpretation:0003-t018-subphenotype-sex-reproductive-stage"
source_refs:
  - "paper:Shah2025"
created: "2026-06-22"
updated: "2026-06-22"
---

# Evidence Line: Shah2025 within-band menopause null disputes a menopause-status-specific stage reading

## What this line shows

Shah2025 is the only PAIS study that breaks the age/menopause collinearity *within* an age band. At ages 40–54 the female long-COVID excess is **near-identical** in menopausal (RR ≈ 1.42, 95% CI 0.99–2.03) and nonmenopausal (RR ≈ 1.45, 1.15–1.83) women. So the midlife female peak that `evidence-line:0001` reads as *supporting* `proposition:0001` is **age-linked, not attributable to menopausal status per se** — weak evidence *against* a **menopause-status-specific** mechanism for the reproductive-stage threshold (it favours an age/immunosenescence account over a menopausal-transition one). This is the machine-readable counterweight to `evidence-line:0001`'s age-band support.

## Why it is grouped with the supporting line

Same cohort and study as `evidence-line:0001` (RECOVER, Shah2025), so it shares `independence_group: shah2025-lc-risk`: it does **not** add an independent disputing cohort — it **partitions** what the single Shah2025 source says. The age-banded female excess (el:0001, `supports`) and the within-band menopause null (this line, `disputes`) are two readings of one study, deliberately kept in one group so the aggregator does not treat them as independent evidence on either side.

## Caveats / scope

`model_criticism`, **weak**: the menopausal-group RR has a wide CI crossing 1 (smaller n), menopausal status is self-reported, and a single cohort cannot fully separate age from the menopausal transition even within a band. This disputes the **menopause-specific** reading only; it leaves an **age/immunosenescence** reproductive-stage threshold (the broader form of `proposition:0001`) intact, and does not bear on the mediator-specific hormone lines (`evidence-line:0002`/`0003`).
