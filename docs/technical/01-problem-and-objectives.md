# 1. Positioning, research aims and design constraints


## 1.1 The problem being solved


Traditional DFDs answer where information enters, moves, is transformed and is stored. A conventional DFD does not, without augmentation, capture why a feature is requested, which stakeholder approves it, when a development step occurs, how much work is performed, the resource capacity consumed, operational failure behavior, billing treatment, adoption obstacles or the evidence supporting each claim. Attempts to put all of these attributes directly onto a single drawing compromise both readability and semantic precision.


UL-xDFD therefore defines a graph-based, annotation-first domain model with reproducible projections. Its central methodological hypothesis is that cross-view links from business demand to data flows, implementation tasks, runtime resource use, costs and organizational evidence can improve the quality, reusability and explainability of engineering research. This hypothesis requires evaluation against strong baselines.


## 1.2 Explicit objectives

- O1. Represent data circulation with conventional DFD entities, processes, stores and directed flows.
- O2. Trace business hypotheses, value units, requirements, and lifecycle activities to implementation and runtime evidence.
- O3. Quantify distributions of data volume, request rate, execution demand, storage/network demand, cloud usage and project effort.
- O4. Map stakeholders, responsibilities, decision authority, culture measures and handoff constraints without extracting culture from topology.
- O5. Support DevOps/DevSecOps adoption diagnostics and prospective research, separating observed evidence from modeled conjecture.
- O6. Support scenario-based capacity planning, price reconciliation, cloud/project forecasting and multiobjective optimization.
- O7. Enforce validation, provenance, uncertainty, confidentiality, immutable baselines and interoperability.

## 1.3 Non-goals and irreducible limits


UL-xDFD is not an executable BPMN engine, resource simulator, static-code analyzer, human-culture sensor, threat certification, invoice ledger, lifecycle process standard or general proof of system correctness. It imports or references authoritative artifacts for these concerns. It cannot recover undocumented work, detect every malicious system behavior, simulate arbitrary concurrency accurately, or establish causal impact without a suitable study design.


## 1.4 Modeling principles

- Preserve DFD semantics; data movement is not causation, precedence or approval.
- One semantic graph, many projections; IDs persist across all views and snapshots.
- Minimize mandatory metadata at inception and progressively enrich at later maturity levels.
- Model the life cycle and the environment as separate axes; stage is not an element type.
- Use explicit measurement windows, scenario boundaries, value kinds, evidence grade and uncertainty.
- Treat missing, disputed and expired data as first-class states; never replace missing with zero.
- Separate cost recognition, attribution, work estimation, resource consumption and business value.
- Separate descriptive observations, forecast models, recommendations and observed outcomes.
- Keep source artifacts and owner approval traceable, with consent and minimal personal data.

---

[Documentation home](../../README.md) · [Technical reference index](README.md)
