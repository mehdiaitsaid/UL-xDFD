# 14. Reference tooling and algorithmic architecture




## 14.1 Tool components and interfaces


A suggested implementation uses a source-connector layer, a versioned graph/annotation registry, a schema and rule engine, an evidence/measurement store, independent analyzers, and a controlled editor/reporting interface. A relational store with typed tables is sufficient for a pilot; a property graph or RDF store is optional. Persist canonical JSON/YAML and controlled dictionaries in source control so results are reproducible without proprietary tool dependencies.


| Module | Input and output contract | Suggested technology / boundary |
| --- | --- | --- |
| Model editor/importer | DFD/process records, stable IDs, human review, annotation forms | Web editor, CLI; vendor-neutral UML/BPMN imports as references |
| Canonical storage | Versioned YAML/JSON, snapshots, policy versions, provenance | Git + database/object store; immutable freeze tags |
| Schema & semantic validator | Typed fields, units, graph invariants, coverage/issue report | JSON Schema 2020-12 + Python/TypeScript graph rules |
| Connector adapters | Contracts, repo/CI events, telemetry, billing and survey aggregates | OpenAPI, OpenTelemetry, OpenLineage, FOCUS, Git interfaces |
| Quantitative engine | Scenario demand graph, resource models, interval estimates | Python; separate modules for queueing/simulation |
| FinOps analyzer | Usage, rate, ledger basis, allocation and cost by value unit | FOCUS normalization and business allocations |
| Adoption analyzer | Reviewed, evidence-qualified organizational indicators | Rule catalog first; ML only when independent outcome dataset exists |
| Optimization engine | Decision variables, constraints, alternatives and outcomes | MILP, constraint solver, simulation, Bayesian optimization |
| Reports and audit | Views, diagnostics, forecast, provenance, model diff | DOCX/HTML/JSON with accessible legends and redaction |


## 14.2 End-to-end algorithms

The algorithm lines in this section are **pseudocode from the proposal**, not commands executed by the current structural validator. The runnable script is [`tools/validate.py`](../../tools/validate.py).


ALGORITHM ULXDFD_BUILD_AND_VALIDATE


import DFD; register stable IDs and boundaries


import phase/requirements/owner links and optional BPMN/contract refs


attach scoped annotations with evidence sources and value status


validate: JSON Schema, units, typed graph, DFD balancing, cross-view semantics


validate: owner/policy gates, shared-cost attribution, source freshness and privacy


create issue backlog, adjudicate, freeze reviewed snapshot


return {snapshot, views, issues, coverage, provenance_digest}


ALGORITHM ULXDFD_COST_AND_CAPACITY


for each named scenario/window: propagate flows using bounded operators


compute service/resource demand under measured/estimated performance profiles


apply topology, SLO, resiliency, quota and calendar constraints


join bill/rate/contract data, avoid charge double count, allocate shared spending


propagate assumptions and uncertainty; compare later invoices/load tests


return {resources, costs, unit_economics, uncertainty, tests_needed}


ALGORITHM ULXDFD_OPTIMIZE


validate baseline and nonnegotiable security, policy, risk and SLO constraints


generate named feasible alternative configurations (retain baseline)


evaluate same scenario mix and value-unit boundary under cost/performance models


rank Pareto-efficient candidates with uncertainty and intervention effort


require human review, limited rollout and post-change observed verification


return {alternatives, constraints, tradeoffs, selected_option_or_null}


ALGORITHM ULXDFD_RESEARCH_PREDICT (OPTIONAL)


freeze time t0 evidence-based features and organization group IDs


independently measure pre-registered later outcomes


split by organization/time; prevent leakage and selection bias


compare transparent baseline with graph-aware methods using nested validation


externally evaluate discrimination, calibration, uncertainty and fairness


return prediction only after sufficient prospectively validated evidence


## 14.3 Interoperability and format governance


An implementation SHOULD offer JSON Schema Draft 2020-12 for core shape checking and publish a separate semantic-rules catalog. Data flows can reference OpenAPI 3.2.1 [S15] or AsyncAPI-compatible messages as external contracts, without claiming that the schema itself validates those contracts. BPMN 2.0.2 [S3] and DMN 1.6 [S4] can be linked by stable IDs for workflow/decisions; PROV-O [S6] expresses provenance; OpenTelemetry [S7] supports runtime evidence; OpenLineage [S8] informs data-pipeline lineage; FOCUS [S11] supports comparable technology costs. Adapter test suites are necessary before claiming an interoperable mapping.


## 14.4 Package deliverables and reproducibility


The optional accompanying ulxdfd_v0_1.schema.json is a structural core validator, not a full semantic validator; the accompanying UL_xDFD_Hotel_Example_v0_1.yaml is a synthetic model used to test parsing and reference integrity. The schema intentionally allows versioned domain-specific annotations. Future tooling should publish schema plus controlled dictionary, semantic-rule code, fixtures with expected failures, and an exporter producing identical analysis from the same input snapshot and engine version.


## 14.5 Reference tooling for AI-native UL-xDFD


| Tool/module | Input sources | Published machine output / safety boundary |
| --- | --- | --- |
| AI inventory adapter | Model registry, model/API contracts, inference deployments | MODEL/MODELSVC/GPU objects and versioned provenance |
| Agent graph adapter | Agent framework manifests, tool definitions, MCP/A2A endpoint metadata | AGENT/TOOL/DELEGATE/POLICY typed edges, unverified issues |
| AI telemetry adapter | OTel GenAI spans, provider usage logs, GPU metrics | Correlated call/run/token/cost records with privacy redaction |
| RAG lineage adapter | Corpus manifests, chunk records, index build and queries | CORPUS/CHUNK/VINDEX/RETRIEVES, refresh and access metadata |
| Evaluation/guardrail adapter | Offline eval suite, human labels, runtime safety events | EVAL/SAFE/HITL records and documented quality uncertainty |
| AI cost reconciler | Provider invoices, rate cards, FOCUS, resource labels and ledger | Attributed AI charges, missing/remainder allocation and unit cost |
| Policy and scenario engine | Graph snapshots, caps, workload mix and risk constraints | Scenario forecasts, infeasibility and prioritized validation issues |
| Artifact release checker | Model, prompt, tools, eval and policy versions | Reproducible AI-specific conformance reports |


PIPELINE: discovery -> import/provenance -> normalize -> validate CORE/AI ->


freeze scenario snapshot -> workload/cost propagation -> readiness diagnosis ->


constrained alternative search -> expert approval -> experimental rollout ->


observed outcome and periodic recalibration


Every connector MUST publish its fields/versions and known information loss. In particular, not every provider reveals reasoning-token usage, training energy, model internals or per-request invoice IDs; the tool must mark unsupported attributes unknown rather than infer hidden values as objective measurements.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
