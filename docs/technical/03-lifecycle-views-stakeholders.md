# 3. Coverage contract: lifecycle, viewpoints and stakeholders


## 3.1 The lifecycle axis


Every record MAY reference one or more phases; phase assignment is not inferred solely from the graph. The recommended baseline aligns conceptually with the software life-cycle coverage in ISO/IEC/IEEE 12207:2026 [S1]. It includes governance and acquisition as well as engineering and operations. Cycles and parallel phases are permitted; neither stage-gated waterfall nor DevOps continuous delivery is imposed.


| Phase | Scope and artifacts | Typical stakeholders | Minimum traceables |
| --- | --- | --- | --- |
| L00 Idea / opportunity | Business problem, proposed value unit, sponsor, strategic assumptions; AI suitability, harm and business-value hypothesis | Product sponsor, customer, finance; Product, AI lead, impacted users and AI governance | Hypothesis, desired outcome, volume range, decision date; AI acceptance/evidence refs and cost provenance |
| L01 Discovery / feasibility | Stakeholder needs, process context, alternatives, constraints; Model-versus-rules baseline; agent autonomy feasibility; data availability | Product, domain experts, security, procurement; AI architect, data owners, security and end users | Stakeholder register, initial DFD, competing options; AI acceptance/evidence refs and cost provenance |
| L02 Requirements / planning | Functional/nonfunctional requirements and acceptance criteria; AI acceptance thresholds, model/task boundaries, human-review and spend caps | Product, BA, QA, architects, compliance; ML engineer, AI product lead, legal and evaluation owner | Requirement IDs, SLO/risk/cost caps, effort forecast; AI acceptance/evidence refs and cost provenance |
| L03 Architecture / design | Logical DFD, solution design, data contracts, threat analysis; AI components, RAG topology, agent tool graph, data residency and trust zones | Architects, platform, security, data governance; AI engineer, security, platform and data governance | Component mappings, boundary review, capacity scenarios; AI acceptance/evidence refs and cost provenance |
| L04 Acquisition / sourcing | Provider and vendor selection, licensing and contracts; Model/vendor terms, API token tiers, data-use terms, GPU commitments | Procurement, vendor manager, legal, finance; FinOps, procurement, vendor risk and legal | Rate cards, contract terms, exit costs, commitments; AI acceptance/evidence refs and cost provenance |
| L05 Build / implementation | Repositories, commits, dependencies, code review, artifacts; Prompts, tools, data pipelines, training/fine-tune runs and model versions | Developers, maintainers, DevEx; ML/LLM engineer, AI application developer, data engineer | Engineering effort, testable changes, provenance; AI acceptance/evidence refs and cost provenance |
| L06 Verification / validation | Testing, security scans, performance and acceptance; Offline/online evals, red-team, prompt injection, safety and task success | QA, security, reliability engineers; AI evaluator, QA, red-team, domain specialist | Test coverage, measured resource costs, defects; AI acceptance/evidence refs and cost provenance |
| L07 Integration / release | CI/CD builds, signing, gates, deployment approvals; Model/prompt registry, evaluation gates, canary rollouts, agent policy | Release manager, DevOps, security; MLOps/LLMOps, release and security owner | Pipeline topology, minutes, manual waits, policies; AI acceptance/evidence refs and cost provenance |
| L08 Deployment / transition | Infrastructure provisioning, rollout, migration, rollback; GPU/model endpoints, embeddings, index refresh and authorized tools | Platform, SRE, operators; AI platform, SecOps and rollout owner | Environments, strategies, migration costs, rollback; AI acceptance/evidence refs and cost provenance |
| L09 Operate / support | Observed load, incidents, billing, SLOs, vulnerabilities; Token/billed usage, tool traces, drift, quality, hallucination and incidents | SRE, service desk, FinOps, security operations; AI SRE, risk owner, FinOps and model provider | Telemetry, invoices, availability, attribution, spend; AI acceptance/evidence refs and cost provenance |
| L10 Improve / evolve | Optimization, modernization, adoption interventions; Model routing, prompt reduction, caching and autonomy changes | Product, engineering, finance, governance; Product, AI research, operators and finance | Before/after experiment, cost/quality/risk impact; AI acceptance/evidence refs and cost provenance |
| L11 Retirement / disposal | Shutdown, data retention/deletion, contract exit; Model/data/index deletion, agent capability revoke, vendor exit | Data owners, legal, operations, finance; Data protection, legal, security, model owner | Decommission cost, evidence of deletion, liabilities; AI acceptance/evidence refs and cost provenance |


## 3.2 The synchronized view axis


| View | View name | Model content | Question |
| --- | --- | --- | --- |
| V0 | Logical data | External entities; data processes; stores; flow contracts; trust zones; AI overlay: Prompt/context/tool-result data, embeddings, retrieved chunks, feature inputs, model outputs and trust boundaries | Data lineage and transformations |
| V1 | Demand, value and requirements | Ideas, business capabilities, requirements, KPIs, product hypotheses; AI overlay: AI use-case value, success denominators, autonomy constraints, model/service quality goals and cost caps | Why the system exists and its required outcomes |
| V2 | Workflow, events and time | Precedence, gateways, approvals, retries, queues, calendars; AI overlay: Agent loop/plan, model calls, tool invocation, human checkpoints, timeouts, routing and deterministic control edges | How work actually proceeds |
| V3 | People, organizations and governance | Roles, team topology, responsibility, approvals, culture evidence; AI overlay: AI/agent owners, tool permissions, red-team, model risk committee, human appeal and workforce readiness | Who owns decisions, risks and handoffs |
| V4 | Software and technical architecture | Modules, APIs, dependencies, runtimes, data contracts and vendors; AI overlay: Model endpoint or hosted weights, prompt/version, agent runtime, vector search, model registry and MCP/A2A interface | How logical processes map to implementation |
| V5 | Workloads, infrastructure and capacity | Compute, memory, storage, network, locality, scaling profiles; AI overlay: GPU/accelerator memory-hours, tokens, requests, KV/cache utilization, embeddings, retrieval and training resources | Resource requirements and constraints |
| V6 | Delivery, testing and DevSecOps | Repository, CI/CD pipeline, tools, scans, artifacts, release gates; AI overlay: MLOps/LLMOps/AgentOps, data/model CI, eval suites, prompt tests, model cards, supply chain and deployment gates | Cost and risk of development and delivery |
| V7 | Operations, resilience and service management | SLO/SLI, observability, backup, incident, response, reliability; AI overlay: Inference latency/TTFT/throughput, tool traces, task success, regressions, agent stop/recovery and quality drift | Operational behavior and recoverability |
| V8 | Security, privacy and compliance | Threats, trust boundaries, controls, data handling, obligations; AI overlay: Prompt injection, model/data poisoning, excessive agency, tool privileges, content safety, privacy and impact | What may happen and what must be protected |
| V9 | FinOps, procurement and sustainability | Billing, contract, allocation, forecast, business unit, energy/SCI; AI overlay: Tokens and model rates, RAG/index/tool costs, GPU hours, experimentation, amortization and cost/successful outcome | Technology and lifecycle economics |
| V10 | Evidence, uncertainty and outcomes | Measurements, citations, confidence basis, registry, follow-up; AI overlay: Model and prompt lineage, evaluation provenance, inference usage source, A/B trial, monitoring and uncertainty | What is known vs estimated and when |
| V11 | Lifecycle, decisions and change | Phase links, baseline, alternatives, interventions, version changes; AI overlay: AI procurement-to-retirement, model/prompt changes, agent capability expansion, deprecation and outcome follow-up | What was decided, changed, and learned |


Figure 1. Twelve coordinated projections of one canonical UL-xDFD graph; all views share IDs and the same evidence registry.


## 3.3 Stakeholder coverage rule


A stakeholder register MUST include the stakeholder role, decision authority, concerns, lifecycle involvement, represented organization, responsible boundary and review status. “The developer” or “the business” is not a sufficient universal actor. Minimum pilot participation: product/business, developer, QA, platform/DevOps, SRE/operations, security/privacy, data governance, FinOps/finance, and a manager/decision owner; add procurement, legal, customer representatives and external providers where relevant. Missing groups are explicitly logged.


| Stakeholder view | Information they validate | Typical decision rights |
| --- | --- | --- |
| Sponsor/product/customer | Business units, demand assumptions, value objectives, acceptance | Funding, scope and priority |
| Business analyst / UX | Data/process completeness, journeys, business exceptions | Acceptance and representation of workflows |
| Software architect/developer | Flows, contracts, code mapping, implementation estimates | Technical solution design |
| QA and test engineer | Tests, quality constraints, performance assumptions | Verification evidence and readiness gates |
| Platform/DevOps | CI/CD, deployment, environments, infrastructure cost | Delivery changes and automation |
| SRE/operations | SLOs, incidents, observability, failover | Runtime reliability and recovery |
| Security/privacy/compliance | Classification, threats, controls, regulatory constraints | Risk acceptance and security go/no-go |
| FinOps/finance/procurement | Billing basis, allocation, commitment and staffing costs | Budget, financial reconciliation, sourcing |
| Data owner/steward | Storage, quality, retention, lineage, cross-border rules | Data stewardship and deletion |
| Vendor/outsourcer | Contract boundary, SLA, billing, dependency behavior | Contracted obligations and escalation |
| AI engineering / ML platform / data science | Model/version selection, eval/quality gates, datasets, GPU capacity, model and agent telemetry | Model and evaluation governance; technical deployment |
| AI safety/model risk, data protection and human oversight | AI impact, agent privileges, red-teaming, audit, fallback and appeal policies | AI approval, tool-action authority, risk acceptance and stop conditions |


## 3.4 AI across all twelve views and twelve lifecycle phases


AI is a cross-cutting profile rather than a thirteenth mandatory view. The same AISYS or AGENT identifier may appear in an architecture, workflow, security, operations and economics projection. A filtered visual view must never be interpreted as the full graph.


| View | AI-specific concern / minimal evidence | Typical stakeholder |
| --- | --- | --- |
| V0 | Prompt context, retrieved facts, model output and tool data classification | Data architect / privacy owner |
| V1 | Business value per successful AI task; failure/appeal and AI necessity | Product/beneficiary |
| V2 | Agent plan and bounded loop; model/tool sequence, retries, human decision | Workflow / agent engineer |
| V3 | Model owner, model-risk and action accountability; skill readiness | Manager / AI governance |
| V4 | Serving endpoint/version, agent runner, MCP/A2A, corpus/index/prompt | AI architect / platform |
| V5 | Tokens, GPU RAM-hours, inference concurrency, retrieval and batch workloads | ML platform / performance |
| V6 | Dataset/prompts/model CI, eval gates, agent-tool integration tests | MLOps / QA / DevSecOps |
| V7 | Agent traces, TTFT, quality drift, failed tool calls, stop/recover | AI SRE / support |
| V8 | Excessive authority, injection, poisoning, policy validation and impact | Security / legal / ethics |
| V9 | Fully allocated AI cost by use case/quality; contracts and carbon | AI FinOps / procurement |
| V10 | Token metering provenance, evaluation holdouts, error bars and outcomes | Research lead / auditor |
| V11 | Model changes, retraining, prompt/version drift, sunset and delisting | Release / model owner |


Phase-specific evidence is embedded in the amended L00–L11 table: feasibility includes “should this be AI?” comparisons; design includes tool authority; procurement includes provider data-use terms; build includes prompts and training; verification includes eval holdouts; operations includes drift/token telemetry; and retirement includes index/model-data erasure and revoked agent access. Phase membership remains many-to-many, so continuous training and redeployment are expected.


An AI workload is in scope only when the boundary names users, provider(s), deployment locality, data sensitivity, supported action authority, model and tool version(s), quality target, desired business value, representative scenarios and measurement windows.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
