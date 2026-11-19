# 4. Formal metamodel and semantic foundations



## 4.1 Definition as a typed, annotated, scenario-indexed graph


Define the proposed model M = (N, E, τN, τE, A, Φ, Ω, V, Π, H). N is the set of persistent typed entities; E is the set of directed typed relations; τN and τE are node/edge type functions; A is the annotation registry; Φ is the set of lifecycle phases; Ω is the set of workloads/scenarios and boundaries; V is the set of view projection definitions; Π is the provenance and evidence store; and H is the versioned snapshot/change history. Each annotation a ∈ A binds exactly one target ID, but may be inherited by explicitly defined scope rules.


A projection View_k(M, filter) returns a visualization and, optionally, a subset of relations and annotation summaries. A projection must not mutate the underlying model. Every visual ID must resolve to a canonical object or a clearly labeled external reference. Contradictions, hidden phases and unknown values remain visible in audit exports even if omitted from a diagram.


## 4.2 Identity, hierarchy, boundaries and scenario semantics

- IDs are immutable within a model lineage. When an element changes its meaning, create a new ID and a supersedes edge; never recycle the prior ID.
- A system boundary B encloses zero or more subprocess boundaries, environments and trust zones. External actors are external relative to a declared boundary, not globally.
- A decomposed parent process has balanced externally visible inputs and outputs unless exceptions are documented with a transformation or scope change.
- Scenario Ω contains actor/cohort, entry event, workload distribution, time window, time zone, environment, rollout state, failure mode, tenant population, pricing/contract assumptions and confidence.
- A requirement, cost or workload annotation can vary by phase, scenario, environment or time window; an unspecific value must not silently override a scoped value.
- Actuals, assumptions, predictions, interventions and future outcome labels are stored separately to avoid information leakage.

## 4.3 Multi-resolution modeling


Level 0 describes system context. Level 1 describes core business transformations and persistent data. Lower levels refine service/API or team processes. Cross-level edges require parent links and a documented composition rule. Quantitative calculations operate at a chosen decomposition level and declare reconciliation between parent and child totals. For example, one high-level “reserve room” process may refine into authentication, availability validation, payment authorization, booking persistence and notification; serial stages are additionally represented by workflow objects rather than inferred from data arrows.


## 4.4 Role of digital threads


A digital thread is a chain of references across views: idea → requirement → DFD flow/process → API/repository → pipeline/test → deployment/resource → telemetry/billing → outcome. Coverage requires all *in-scope* critical requirements and cost-bearing units to have at least one resolved trace path. Traceability does not imply that the implementation is correct; it means there is a reviewable claim about the connection.


## 4.5 Formal AI/agentic extension to the metamodel


Let the original UL-xDFD typed multigraph be M = (V,E,A,H,Sc,Pr,Ev,Snap), where V/E are typed nodes/edges, A annotations, H decomposition, Sc scenarios, Pr lifecycle phases, Ev evidence and Snap immutable snapshots. The AI profile introduces disjoint, explicitly typed subsets V_AI ⊂ V and E_AI ⊂ E, not a new untyped graph. A model call is an invocation event, a generated response is data, and a tool action is an authorized effect; they MUST have separate identities or an explicit correlation mapping.


Core runtime identity tuple: (application_id, use_case_id, scenario_id, environment, trace_id, agent_run_id, model_invocation_id, model_version, prompt_version, policy_version, provider, billing_period). Nullable fields must be documented when a subsystem cannot supply them. Propagation of user identity or raw conversation content into traces is not required and often prohibited by data minimization.


| Kind | Primary state | Independent boundary/measure |
| --- | --- | --- |
| AISYS | Business purpose, defined task, impact and quality acceptance | Use case and beneficiary, not model vendor |
| MODEL | Algorithm, weights/version, tokenizer, context modality | Model artifact/license and release state |
| MODELSVC | API endpoint, provider region, latency/capacity limits | Provider call, billing meter, contract |
| AGENT / AGRUN | Goal/tool policy vs correlated runtime attempt | Autonomy/step budget and stop outcome |
| TOOL / MCP / A2A | Interface capability, identity, scopes, side effects | External action and trust/authorization |
| PROMPT / CONTEXT | Template/version vs context/memory data | Content provenance, TTL and private data |
| CORPUS / CHUNK / VINDEX | Approved RAG content, indexing and search | Storage, embedding jobs, freshness and provenance |
| DATASET / EXPER / EVAL | Train/eval lineage, experiments and human labels | Split, leakage, GPU hours, acceptance |
| SAFE / HITL | Policy enforcement and human authorization | Risk control evidence, action records |
| GPU / AICHARGE / AIOUT | Accelerator capacity, charge and reviewed task success | Time/unit price, business denominator |


Determinism contract: the graph encodes possible, conditioned and observed actions, not a guaranteed execution sequence for nondeterministic LLM outputs. A path is allowed only if its predicates, policy constraints, exception handling and stop criteria are defined. Unobserved behavior is not assumed impossible.


Model-interface roles are orthogonal to mechanism: MCP relates hosts/clients/servers/tools/resources/prompts; A2A relates peer-agent capability discovery/tasks and messaging; OpenTelemetry is an observability convention; FOCUS governs normalized billing data. A transport call should not be modeled as a claim of conformance unless exact protocol versions and tests are recorded.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
