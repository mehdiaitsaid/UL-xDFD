# 5. Element types, edge families and notation



## 5.1 Core elements and additional entities


| Tag | Semantic type | Definition / example |
| --- | --- | --- |
| X | External entity | Customer, partner system, regulator or supplier relative to a boundary |
| P | Logical process | Transformation of data and business work |
| S | Data store | Logical database, cache, file, registry or durable queue |
| F | Data flow | Directed movement of information with payload semantics |
| B | Boundary | System, tenant, geographic, organizational or trust boundary |
| IDEA | Idea/initiative | Desired capability or change proposal |
| VAL | Value unit | Booking, customer, feature, transaction or business outcome |
| REQ | Requirement | Functional, technical, quality, security and financial requirement |
| USE | Use case/journey | Customer or internal actor scenario |
| EV | Workflow event/task | Trigger, activity, wait or completion state |
| G | Gateway/approval | Branching condition, review or control gate |
| TEAM | Team | Stable organizational unit or outsourced responsibility |
| ROLE | Role | Persona or function; no personal identifier required |
| SKILL | Capability | Required competence/training or assessed gap |
| APP | Application/module | Deployable or internal technical component |
| API | Interface/contract | Versioned HTTP, event or data interface |
| REPO | Source repository | Code/configuration or infrastructure source |
| PIPE | Pipeline/job | CI, build, test, scan, deploy pipeline or task |
| ART | Artifact | Build product, SBOM, package, release manifest |
| ENV | Environment | Dev, test, staging, prod, DR |
| DEP | Deployment unit | Container, function, VM, bare-metal service |
| RES | Resource | Compute, storage, networking or SaaS costed unit |
| CC | Cost center | Business owner, product, team, allocation target |
| BILL | Charge/ledger record | Usage, invoice, commitment, credit, labor cost record |
| RISK | Risk/control/obligation | Security, privacy, availability or financial policy |
| EVID | Evidence | Measurement, interview, telemetry, artifact or financial source |
| OUT | Outcome | Later observed impact, intervention or experiment endpoint |
| CHG | Change/decision | Alternative, approval, intervention, snapshot lineage |
| AISYS | AI system/use case | Governed AI capability with use case, intended purpose, constraints and impact scope |
| MODEL | AI model/version | Classical model, foundation model, embedding model or fine-tuned weights; immutable version |
| MODELSVC | Model-serving endpoint | Hosted API or self-hosted model server; provider, metering, residency and runtime |
| AGENT | AI agent definition | Goal-directed orchestration, policies, tools, autonomy level and exit criteria |
| AGRUN | Agent task/run | Correlated runtime attempt with max steps, state, outcome and billable usage |
| ORCH | Agent orchestrator | Multi-step planner/router coordinating model and tools, not necessarily autonomous |
| TOOL | Agent tool/capability | Executable operation with input/output schema, authorization and possible side effects |
| MCP | MCP host/client/server | Named protocol-role participant for tools, resources and prompts; version pinned |
| A2A | A2A peer/agent card | Inter-agent capability discovery/interaction and task-hand-off interface |
| PROMPT | Prompt/template/guardrail | System/developer/user prompt templates and checked versions; content held externally |
| CONTEXT | Context/memory segment | Ephemeral or persistent conversation/task memory; provenance, sensitivity, TTL |
| CORPUS | Knowledge corpus | Approved source documents for retrieval/ingestion with license and retention terms |
| CHUNK | Retrievable chunk | Chunking strategy, chunk lineage and vector/index version |
| VINDEX | Vector/hybrid index | Embedding index and search service with build, update, capacity and retrieval cost |
| DATASET | ML dataset/split | Training, validation, test, benchmark or eval datasets with provenance and leakage rules |
| EXPER | Training/evaluation run | Reproducible experiment ID, compute, parameters, checkpoint and reproducibility |
| EVAL | AI evaluation suite | Tasks, rubric, sampling, acceptance gates, human review and independent outcome labels |
| SAFE | AI policy/guardrail | Independent allow/deny constraints; enforceable authorization and task boundaries |
| HITL | Human intervention gate | Explicit review/override/appeal and authorization of high-impact agent actions |
| GPU | Accelerator resource | GPU/TPU class, memory, energy, occupancy and accounting boundary |
| AICHARGE | AI metering/charge | Inference, reserved capacity, training, embeddings, RAG, tool, platform or license charge |
| AIOUT | AI task outcome | Task success, reviewed correctness, harm or business value tied to a declared denominator |


## 5.2 Directed relationship families


| Family | Typical predicates | Semantics and enforcement |
| --- | --- | --- |
| DATA | transfers | X/P/S ↔ P; only sanctioned pairs; payload and direction are explicit |
| DECOMP | refines / contains | Child maps to unique parent; level balancing is checked |
| REQMAP | satisfies / constrains | Requirement → scope/element; tests prove stated coverage |
| WORK | precedes / triggers / waits / retries | Temporal/workflow relationship; no implicit data transfer |
| DEC | approves / rejects / gates | Named decision, predicate and owner |
| OWN | responsible_for / accountable_for | Role/team → activity/unit; RACI contextualized |
| CONTR | consumes / produces_contract | Application/flow → API/data contract |
| CODE | implements / built_from | Source/deployment ↔ logical process / repo |
| DEL | builds / tests / deploys / rolls_back | Pipeline/job/release relations |
| HOST | hosted_on / connected_to | Deployment/technical dependency mapping |
| RESUSE | consumes_resource | Workload/deployment → quantity/metric resource |
| COST | incurs / allocates / bills | Charges → cost center/product; semantics and time basis |
| SEC | crosses_trust / mitigates / violates | Threat, control, zone, evidence relations |
| EVID | supports / disputes / measured_by | Evidence provenance; not causal proof |
| PHASE | occurs_in / transitions_to | Life-cycle membership and change tracking |
| OUTCOME | evaluates / intervenes_on | Baseline change → later observed endpoint |
| ALT | compares / supersedes | Versioned alternatives; not a data flow |
| INVOKES | agent_invokes / model_call | Agent/orchestrator invokes model endpoint; one call is an explicit metered event |
| TOOLCALL | agent_calls_tool / tool_returns | Authorized action invocation distinct from data returned or state changed |
| RETRIEVES | retrieves / ranked_chunks | Retrieval request and result linkage; document ranking/top-k and provenance |
| EMBEDS | embeds / indexes | Corpus/chunk transform to vectors/index; count embedding jobs and storage separately |
| MODELDEP | serves / routed_to / fallback_to | Model routing, version pinning, conditional fallback and capacity plan |
| DELEGATE | delegates / agent_message | Inter-agent task/control relationship distinct from A2A payload data transfers |
| TRAINS | trained_on / fine_tuned_from | ML development provenance; no assumption that data ownership transfers |
| EVALUATES | evaluates_model / judged_by | Evaluation suite, judge type, adjudication and holdout evidence |
| POLICY | permits / denies / needs_approval | Independent policy constraints for agent tools and protected actions |
| AICOST | billed_for / allocated_ai_cost | Usage-to-charge and model/provider attribution; avoid double count of cost layers |
| AIRESULT | attempts / completes / escalates | Run-to-business outcome, including unsuccessful and abandoned tasks |


## 5.3 Diagram legend and visual encoding


Figure 2. DFD data edges remain distinct from workflow/control edges. Sample only—not a complete flow or workflow model.


Render a rounded rectangle for P, rectangle for X, store glyph for S and solid directed arrow for DATA/F. Non-data relationships are different line styles and labeled text; color alone is never a type discriminator. Optional compact badges: DF(data), WL(workload), TM(timing), ORG(owner), DL(delivery), OP(operations), SEC(security), FO(cost), EV(evidence). Values in badges are summaries; the annotation records and legend remain authoritative. The accessible text form is mandatory for each published diagram.


## 5.4 AI-specific node and edge notation


An AI subgraph uses tagged overlays without altering the traditional X/P/S/F glyphs. Example short badges: MODEL:m7, AGENT:booking-assistant, INV:token-meter, TOOL:reservation.search, RAG:index-2026Q4, HITL:approve-refund. Dashed control arrows and solid DATA arrows must retain distinct legends; color is never the sole discriminator.


X1 Customer -F1: request-> P1 BookingAPI -F2: context-> P2 AssistantGateway


P2 -F3: user+policy context-> P3 AI planner


P3 -INVOKES-> MODELSVC1 (MODEL1@v7) -F4: generated plan-> P3


P3 -TOOLCALL: read-only-> TOOL1 SearchBooking -F5: booking data-> P3


P3 -POLICY-> SAFE1 (allow.read) ; P3 -POLICY-> HITL1 (approve.write)


P3 -RETRIEVES-> VINDEX1 -F6: ranked chunks-> P3


P3 -AIRESULT-> AIOUT1 ; AICHARGE1 -AICOST-> CC1


In the textual example, the modeling arrows are semantic relations and source/destination direction; the notation is illustrative, not executable source code. Every corresponding machine record must resolve to a typed node or edge with a stable ID, and each model call, retrieval and action records its own meter.


## 5.5 Agentic control and multi-agent semantics


| Relation | Required annotations | Prohibited inference |
| --- | --- | --- |
| INVOKES | model, input/output token classes, fallback, request/response ID | A prompt is not a model call without invocation evidence |
| TOOLCALL | action, scoped principal, idempotence, side effects, approval | Returned text does not imply executed action |
| DELEGATE | agent identity, permission attenuation, task deadline and correlation | Delegation does not transfer unlimited privileges |
| RETRIEVES | query type, top-k, corpus/index version, retrieval quality | Retrieval is not fact validation by itself |
| TRAINS | dataset ID/split, license, model version, run resource and quality | Training data is not automatically allowed for inference export |
| MODELDEP | deployment, provider, route probability, reliability and failover | Model routing does not preserve quality/cost automatically |
| AIRESULT | attempted/completed/escalated; assessor and denominator | Output delivered is not synonymous with task success |


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
