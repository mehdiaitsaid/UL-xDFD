# 18. Conformance profiles, phased tooling roadmap and acceptance criteria




## 18.1 Independent implementation profiles


| Profile | Minimum required coverage | Permitted claim |
| --- | --- | --- |
| CORE-DFD | Typed P/S/X/F/B, hierarchy, scenario IDs, source status, core validation | Valid structural UL-xDFD model for declared scope |
| LIFECYCLE | CORE + business requirements, phases, roles and critical digital threads | Lifecycle traceability with declared coverage |
| ENG-CAPACITY | CORE + workload operators, benchmarks, technical constraints and scenarios | Engineering demand estimates within stated assumptions |
| FINOPS | ENG-CAPACITY + owner allocation, price/ledger sources, cost boundary, unit economics | Cost estimate/reconciliation for covered charges |
| DELIVERY-SECURITY | LIFECYCLE + CI/CD, test/security controls, operations, approvals | Evidence-qualified delivery/security diagnostic |
| ADOPTION-DIAGNOSTIC | LIFECYCLE + culture/organization evidence, incident/CI metrics, hard gates | Non-probabilistic scoped adoption diagnostic |
| RESEARCH-PREDICTIVE | All necessary validated inputs + frozen baselines + independent later outcomes | Prospective prediction results only after external validation |
| AI-INFERENCE | CORE+AI model service, prompt/context flow, token classes, model call evidence, provider/meters | Scoped AI inference usage and cost estimate (not task quality guarantee) |
| AI-AGENT | AI-INFERENCE+ agent/tool graph, autonomy, approval, traces, loop caps, delegation controls | Auditable agent topology and budget/risk diagnostic for stated use case |
| AI-RAG | AI-INFERENCE + corpora, ingestion/chunking/embedding/retrieval/refresh/reliability | RAG data lifecycle, capacity and per-use-case cost estimates |
| AI-TRAINING | CORE + versioned dataset, training/eval run, accelerator consumption, experiment logs | Estimated or observed ML training/fine-tune footprint |
| AI-ASSURANCE | AI-AGENT + threat/impact assessments, eval gates, independent testing, privacy and review | Evidence-qualified AI assurance; not certification or predictive task guarantee |


## 18.2 Implementable milestones


| Release | Deliverable | Exit evidence |
| --- | --- | --- |
| v0.1 — this draft | Metamodel; dictionary; reference schema, synthetic fixture; research protocol | Internal logic review, example validation |
| v0.2 — compiler | Strong validator, reference integrity, unit checks, text/diagram projections | Tests for 30+ positive/negative fixtures, reproducible reports |
| v0.3 — connectors | Source, OpenAPI/BPMN link, CI traces, OTel, FOCUS, evidence grading | Integration golden tests and privacy review |
| v0.4 — analytics | Workload propagator, cloud/project/CI costs, uncertainty, SLO rules | Comparison to controlled loads, invoices and estimates |
| v0.5 — decision | Cost/latency/risk Pareto optimizer; adoption diagnostic rules | Independent expert assessment and safe rollout pilots |
| v1.0 — research release | Pilot studies, reproducible benchmark, validated codebook | Inter-rater/coverage/forecast performance publication |
| Later — predictive | Multiorganization longitudinal outcomes, external calibration | Independent prospective evaluation before probability claims |


## 18.3 Minimum acceptance checklist

- The original DFD remains interpretable and hierarchically balanced.
- All listed relationship families are type-checked and visibly distinguished.
- Critical business requirements have a trace through data/process/code/deployment/evidence.
- At least normal, peak and degraded scenarios are represented for capacity-dependent conclusions.
- Every numeric field has unit, granularity, window, provenance and uncertainty/quality state.
- Every critical flow/process and material cost account has a responsible role or explicit unknown.
- All sourced cost totals reconcile to a known billing boundary and leave unmatched amounts disclosed.
- Security, data protection, quality and reliability gates are never bypassed by cost optimization.
- Readiness reports do not imply statistically calibrated adoption probability absent outcome evidence.
- A prospective experiment can freeze baseline and later outcomes without modifying t0.
- The system provides accessible text, legend, issue log, audit trail and confidentiality controls.
- Test fixtures reproduce all sample calculations and intentional validation failures.

## 18.4 AI conformance levels and release milestones


In addition to original profiles, five selectable AI profiles are defined in the amended conformance table: AI-INFERENCE, AI-AGENT, AI-RAG, AI-TRAINING, and AI-ASSURANCE. Profile assertion requires both structural checks and declared semantic evidence; the bundled draft schema validates only a strict structural subset and does not independently certify policy correctness, financial reconciliation or scientific validity.


| Research release | AI-specific deliverable | Exit criterion |
| --- | --- | --- |
| v1.0 proposal (this document) | Full metamodel, 12-view AI overlay, 15 AI families and 42 rules | Peer review and synthetic fixture validation |
| v1.1 language test suite | Schema 2020-12 extension, static semantics, migration tests | Positive/negative AI fixtures and deterministic validation |
| v1.2 adapters | OTel GenAI, provider usage, AI registry, MCP/A2A, FOCUS bridge | Golden trace/cost reconciliation, privacy and auth reviews |
| v1.3 analytics | Agent DAG/loop simulation, token/GPU workload, interval forecast | Controlled benchmark vs usage and billing holdouts |
| v1.4 operational diagnostics | AI readiness, AgentOps assurance, red-team and incident events | Cross-reviewer agreement and bounded false-negative testing |
| v2.0 evaluated framework | Multi-organization models and prospectively observed outcomes | External validation and reproducible study artifacts |


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
