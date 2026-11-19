# 2. Reconciliation of the two submitted specifications



## 2.1 Source strengths, inherited concepts, and extensions


| Source | Strong inherited contribution | What UL-xDFD adds |
| --- | --- | --- |
| [I1] xDFD v0.9 | Quantitative flow/CPU/memory/storage/network calculations; scoped values; traffic operators; security, quality, FinOps and conformance | Product value, requirements, people, phase-aware engineering effort, lifecycle traceability, multi-view governance, outcomes and predictor validation |
| [I2] E-DFD v0.1 | Six synchronized views; team/culture evidence; workflow time; control vs data semantics; longitudinal readiness design | Richer numerical operations; storage and network models; FOCUS reconciliation; project/CI pipeline cost; full software lifecycle and explicit decision optimization |
| UL-xDFD v0.1 | Single typed graph, 12 views, 24 annotation families, scenario and phase references | Testable schema, standard mapping, validation rules, research architecture, deployment artifacts |


## 2.2 Migration and compatibility rules

- Legacy DFD P/S/E/F IDs retain their source document identity and are namespaced at import (e.g., legacy.xdfd:P2) to avoid clashes.
- Both submitted proposals call a generic resource “R”; UL-xDFD distinguishes physical/cloud resource RES, organization role ROLE and cost center CC to prevent ambiguous edges.
- Use the common status taxonomy: observed, reported, estimated, derived, hypothetical, unknown, disputed, expired. Preserve original status in legacy.raw_status.
- Existing xDFD workload, network, storage, security and FinOps properties map to data.*, compute.*, storage.*, net.*, sec.*, fin.*; retain original field names as aliases.
- Existing E-DFD readiness constructs, temporal events and evidence records map to org.*, culture.*, work.*, del.*, evid.*, outcome.*.
- Do not coerce DFD data-transfer arcs into workflow edges; use a typed mapping or unresolved record when the semantic transformation is not reliable.

## 2.3 Problem/challenge coverage and remaining risk


| Challenge in ordinary DFD | UL-xDFD mechanism | Residual research/engineering risk |
| --- | --- | --- |
| Ordering, retries, time and parallelism | WORK relation family, BPMN links, timed scenarios and trace evidence | Not every event is instrumented; tail latency not additive |
| Analyst omission or inconsistent diagram | Coverage requirements, decomposition balancing, interviews, independent reviews | Unseen systems and hidden manual work remain possible |
| Workload/resource/cost not explicit | Scoped demand, processing, deployment and billing annotations | Cloud performance and prices change; forecasts are uncertain |
| People/culture absent | Role and accountable-owner links, anonymous surveys, decisions | Culture cannot be proven from graph density |
| Complexity confused with readiness | Construct-specific diagnostics, contextual controls, critical gates | Feature weights and construct validity require study |
| No reliable prediction outcomes | Frozen baselines, independent prospective outcomes | Prediction claims need representative longitudinal evidence |


## 2.4 Integration policy for AI in the reconciled model

- Use existing P/S/F/X objects for logical data movement; add AI objects only where the model/tool/runtime distinction adds operational meaning. A MODEL is not identical to a model-serving MODELSVC, and an AGENT definition is not the same as a runtime AGRUN.
- Represent model requests and outputs as named data-flow records AND separately represent metered model invocation. This prevents double charging a tool result, a network request, and a model inference as if they were three independent model calls.
- Agent goals, policies and plan/loop behavior are workflow semantics; actions with side effects require a TOOLCALL and POLICY/HITL relation. Text in a prompt or retrieved document cannot grant execution authority.
- Training and production inference are separate lifecycle operations; their resource and cost boundaries must be declared. Also distinguish model cost, application cost and full business process cost.
- AI risk claims and maturity/readiness outcomes remain diagnostic unless reproducible evidence and prospective validation justify predictive statements.

---

[Documentation home](../../README.md) · [Technical reference index](README.md)
