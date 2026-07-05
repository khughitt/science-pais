---
id: "evidence-line:0011-mishra2020-adjustment-attenuation-supports-confounder-decomposition"
kind: "evidence-line"
title: "Mishra2020/Costeira2021 adjustment attenuation supports the confounder-decomposition requirement"
status: "active"
stance: "supports"
target: "proposition:0004-female-reproductive-stage-excess-requires-confounder-decomposition"
source: "paper:Mishra2020"
strength: "moderate"
independence: "independent"
independence_group: "acute-covid-hormone"
evidence_role: "background_constraint"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0004-female-reproductive-stage-excess-requires-confounder-decomposition"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
source_refs:
  - "paper:Mishra2020"
created: "2026-06-21"
updated: "2026-06-21"
---

# Evidence Line: Mishra2020/Costeira2021 adjustment attenuation supports the confounder-decomposition requirement

## What this line shows

`paper:Mishra2020` (with Costeira2021) shows menopausal/hormone-proxy associations **attenuating after adjustment** for age, severity, comorbidity, route, and indication — direct empirical evidence that the crude reproductive-stage association is confounded, which is the core of `proposition:0004`.

## Why it is independent

Acute-COVID cohorts, `independence_group: acute-covid-hormone` (same studies as `evidence-line:0004`, retargeted: there a weak dispute of the threshold effect, here moderate support for the identification requirement).

## Caveats / scope

`background_constraint`, moderate: demonstrates confoundedness in the *acute* setting; the inference that the same confounding applies post-acute is a transfer, not a measurement. It motivates, and is formalized by, the back-door analysis over `patch-definition:menopause-pais-causal-dag`.
