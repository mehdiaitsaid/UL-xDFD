# 7. Domain annotation dictionary




The namespace families below are a proposed controlled vocabulary. Each field requires a definition, applicability, type, unit where applicable, collection protocol and version. The tables show representative fields; the machine-readable schema and a future public dictionary registry can expand them. None of these labels are asserted to be fields mandated by ISO, FOCUS or another third-party specification.


## CORE — identity and context


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| core.id | UUID/string | all | Globally unique stable ID; original legacy ID retained |
| core.type | enum | all | Entity/edge type from registered taxonomy |
| core.boundary | ref | P/S/X/DEP | Named system and organization/trust boundary |
| core.version | SemVer | model | Schema and snapshot version |
| core.maturity_scope | enum | model | Core/engineering/FinOps/adoption/research selected profiles |
| core.owner_role | ROLE ref | all critical | Maintainer/author of claim, not necessarily risk owner |


## STRAT — business strategy and portfolio


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| strat.initiative | IDEA ref | IDEA | Initiative and strategic objective |
| strat.priority | ordinal | IDEA/REQ | Decision priority and method |
| strat.horizon_months | month | IDEA | Forecast/project evaluation horizon |
| strat.funding_cap | currency | IDEA/CC | Program cap and approved budget window |
| strat.alternatives | ref[] | CHG | Make/buy, cloud/on-prem, architecture alternatives |
| strat.assumptions | object | IDEA | Business growth, market, adoption assumptions |


## VALUE — demand and outcome units


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| value.unit_definition | object | VAL | A meaningful completed business unit and exclusion rules |
| value.arrivals | distribution/s | USE/F | Customer/workload arrivals plus seasonal calendar |
| value.conversion | ratio | USE | Conversion of attempts to completed business units |
| value.revenue_or_benefit | currency/unit | VAL | Optional value with source and time horizon |
| value.segment | enum | USE | Tenant/cohort/region/customer segment |
| value.hypothesis | string | IDEA/CHG | Falsifiable value hypothesis |


## REQ — requirements and acceptance


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| req.kind | enum | REQ | Functional, quality, security, finance, privacy, operability |
| req.priority | enum | REQ | Prioritized criticality (defined profile) |
| req.acceptance | ref/string | REQ | Testable condition and verification method |
| req.slo | numeric+period | REQ | SLI target, denominator and measurement window |
| req.trace_to | ref[] | REQ | Processes, code, tests, cost and operations |
| req.decision_owner | ROLE ref | REQ | Accountable approval authority |


## DATA — logical and transport semantics


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| data.schema_ref | URI/version | F/S | Data model or schema and version |
| data.classification | enum | F/S | Sensitivity, purpose and labeling policy |
| data.size_bytes | distribution B/message | F | Payload size, mean and higher percentiles |
| data.rate | distribution message/s | F | Rate under exact scenario and period |
| data.routing | object | P/F | Filter, split, duplicate, batch or aggregate semantics |
| data.quality | object | F/S | Completeness, accuracy, freshness, error bounds |
| data.correlation | ref/string | F/EV | Request/session/batch correlation keys (non-sensitive) |
| data.retention | days | S/F | Time to retain and deletion handling |


## PROC — transformation and computing


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| proc.cpu_core_seconds | core_second/request | P | Measured/estimated CPU demand, not elapsed time |
| proc.runtime_seconds | distribution s/request | P | Wall time including waits; not interchangeable with CPU |
| proc.memory_delta | MiB/request | P | Incremental retained working set while active |
| proc.cache_hit | ratio | P/S | Measured by request class; affects only cacheable calls |
| proc.fanout | calls/inbound_call | P | Expected branch multiplicity |
| proc.error_retry | object | P | Capped retry policy, retry probability and budget |
| proc.accelerator | GPU_s/job | P | GPU/TPU time, accelerator capacity and utilization |
| proc.algorithm_version | string | P | Workload-transform semantics and implementation revision |


## WORK — workflow and decisions


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| work.trigger | event/ref | EV | Entry condition and correlation rule |
| work.predecessors | ref[] | EV | Explicit ordering separate from DATA edges |
| work.branch_predicate | DMN/expr | G | Named decision with mutually clear outcomes |
| work.parallel_join | enum | EV/G | ALL/ANY/QUORUM/TIMEOUT semantics |
| work.retry_policy | object | EV/P | Max attempts, backoff, jitter, timeout, DLQ |
| work.approval_latency | distribution h | G | Observed/manual waiting time by scenario |
| work.failure_path | ref[] | EV | Compensation, rollback or escalation route |


## TIME — temporal and lead-time evidence


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| time.calendar | ref/timezone | EV/TEAM | Time zone, work calendar, off-hours |
| time.duration_p50_p95 | distribution seconds | P/EV | Recorded latency distribution and sample N |
| time.wait_p95 | seconds/hours | G/EV | Queue/manual wait in named workflow |
| time.deploy_lead | hours | PIPE | Change lead time definition and measurement |
| time.valid_window | time interval | all annotations | Assessment and retrospective observation window |
| time.batch_window | s | P/EV | Batch flush and end-to-end buffering |


## ORG — responsibilities and organization


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| org.responsible_team | TEAM ref | P/PIPE/DEP | Per activity operational responsibility |
| org.accountable_role | ROLE ref | critical P/REQ/G | Single explicit decision accountability within scope |
| org.consulted_roles | ref[] | REQ/CHG | Cross-disciplinary consultations |
| org.handoff | object | WORK/TEAM | Ownership transition and acceptance condition |
| org.decision_latency | duration | G | Observed time spent awaiting cross-team decision |
| org.skills_required | ref[] | TEAM/PIPE | Competencies required, gap assessment source |
| org.outsourcing | object | TEAM | Supplier, contract obligations and escalation |


## CULT — organizational readiness evidence


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| cult.instrument | URI/version | TEAM | Survey/research instrument, validity status |
| cult.participation | count+rate | TEAM | Number invited and replied; safe aggregation |
| cult.psych_safety | ordinal | TEAM | Perception only, not deduced from graph shape |
| cult.trust_collaboration | ordinal | TEAM | Perceived collaboration and response differences |
| cult.learning | ordinal | TEAM | Blameless learning practices with independent examples |
| cult.privacy_threshold | count | TEAM | Minimum subgroup N before disclosure |
| cult.interview_disagreement | object | TEAM | Cross-role contradictions and adjudication |


## ARCH — architecture, code and contracts


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| arch.style | enum | APP | Monolith, modular monolith, microservices, hybrid |
| arch.repo | URI | APP/REPO | Repository mapping, owner and access restrictions |
| arch.api_contract | URI/version | API/F | OpenAPI/AsyncAPI/data contract |
| arch.dep_version | string | APP | Software and provider dependency version |
| arch.release_coupling | ratio/ordinal | APP/DEP | Evidence-based change coordination need |
| arch.tech_debt | object | APP | Measured change burden with bounded interpretation |
| arch.portability | object | DEP | Exit and portability constraints, scope |


## BUILD — engineering work and delivery pipeline


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| build.job_duration | distribution minute/run | PIPE | Runner/wait stage execution distribution |
| build.job_frequency | runs/day | PIPE | Triggered, scheduled, manual counts |
| build.runner_resource | vCPU/GiB/unit | PIPE | CPU/memory, hosted/on-prem and price basis |
| build.scan_strategy | object | PIPE | Tool target/depth, risk-based gate and override |
| build.approval | G ref | PIPE | Manual gates, owner, timing and exception |
| build.cache | object | PIPE | Build cache hit rates, storage and invalidation |
| build.provenance | URI/version | ART | Attestation, SBOM, signature and traceability |
| build.failure_rework | count/rate | PIPE | Failures, retries, rework definition |


## TEST — verification and coverage


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| test.case_ref | URI | REQ/PIPE | Test case, method and expected result |
| test.run_cost | currency/run | PIPE | Compute, license, human and storage cost |
| test.coverage | ratio+denominator | REQ/APP | Specify code/behavior/risk coverage meaning |
| test.perf_profile | object | USE/P | Load scenario, tool, environment and results |
| test.sec_findings | count+severity | APP/PIPE | Verified vulnerability counts and validation dates |
| test.flakiness | ratio | PIPE | Flaky test definition and sampling window |
| test.release_blocker | bool+policy | G | Hard gate and authorized exception process |


## SEC — security, privacy and supply chain


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| sec.trust_zone | ref | B/P/DEP | Boundary and network/data trust zones |
| sec.threat | RISK ref | P/F/S/DEP | Threat scenario and risk assessment method |
| sec.control | ref | RISK | Control ID, verification and accountable owner |
| sec.authz | policy/ref | API/P | Identity and authorization enforcement model |
| sec.encryption | object | F/S | In-transit and at-rest controls; keys not copied |
| sec.data_residency | region/jurisdiction | S/RES | Processing/storage/backup locality |
| sec.supply_chain | ref[] | ART/PIPE | SBOM provenance, signing, third-party restrictions |
| sec.privacy_law | ref | DATA/RISK | Legal applicability assessed by qualified counsel |


## OPS — observability, reliability and service


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| ops.sli | object | APP/DEP | SLI query, denominator and sampling window |
| ops.slo | object | APP/REQ | Target, period and error budget |
| ops.oncall | TEAM ref | DEP | Escalation and support rota policy (no personal roster) |
| ops.incident | ref/stats | APP | Relevant incident data, classification and cause |
| ops.recovery | RTO/RPO | DEP/S | Restore requirements and tested evidence |
| ops.telemetry | object | APP/PIPE | Metrics, tracing, logging, retention and ingest cost |
| ops.rollback | minutes+evidence | DEP/PIPE | Measured recovery rollback/roll-forward |
| ops.dependencies | ref[] | APP | Third-party failure behavior and SLO |


## INFRA — compute and deployment


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| infra.platform | enum | RES/ENV | Public/private cloud, on-prem, hybrid, edge |
| infra.capacity | resource units | RES | vCPU, GiB, GPU, memory bandwidth and limits |
| infra.replica_policy | object | DEP | Min/max HPA, scaling thresholds and quotas |
| infra.utilization | distribution % | RES | Observed CPU, memory, I/O and period |
| infra.unit_perf | benchmarked index | RES | Compute class reference and measured variance |
| infra.topology | object | RES | Zones, region, node pool, shared tenancy |
| infra.failover_headroom | ratio | RES | N+1, failure-zone assumptions |
| infra.billing_unit | unit/time | RES | Meter and charge granularity |


## NET — network and distributed messaging


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| net.protocol | string | F/API | Protocol and negotiated properties |
| net.bytes_wire | distribution byte/message | F | Wire payload including selected overhead |
| net.latency | distribution ms | F | RTT, region, sampling and percentile |
| net.bandwidth | bit/s | RES/F | Peak sustained link demand |
| net.egress_class | enum | F/RES | Cross-AZ, cross-region, Internet, on-prem |
| net.retry_wire | ratio | F | Separate packet retransmit vs application retry |
| net.message_guarantee | enum | API/F | At-most/at-least/effectively-once and dedupe |


## STOR — persistence, backup and I/O


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| stor.growth | GiB/day | S | Net ingest vs retained live data |
| stor.retention | days | S | TTL, legal hold, tiering and removal |
| stor.iops | ops/s | S | Random/sequential reads/writes with sizes |
| stor.replication | integer+mode | S | Copies, zones and synchrony |
| stor.compression | ratio | S | Measured physical/logical ratio |
| stor.index_factor | ratio | S | Index and metadata expansion |
| stor.backup | object | S | Backup cadence, retention, data transfer and test |
| stor.consistency | enum | S | Consistency and transactional assumptions |


## FIN — FinOps and project economics


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| fin.cost_source | FOCUS/invoice/estimate | BILL | Billing origin and dataset version |
| fin.charge_class | enum | BILL | Consumption, license, credit, amortization, tax |
| fin.unit_price | currency/meter | RES/PIPE | Metering basis, region, contract and effective date |
| fin.allocation | object | BILL/CC | Owner/weight, shared split, unallocated ledger |
| fin.price_commitment | object | BILL/RES | Discount, commitment, coverage and term |
| fin.forecast | distribution currency/period | CHG | Scenario and model assumptions |
| fin.project_effort | person_hour/role | CHG/L-phase | Labor effort, rate basis, capitalized/expense treatment |
| fin.unit_economics | currency/VAL | VAL | Attributable spend per valid business outcome |
| fin.budget | currency/period | CC | Budget cap, owner and tolerance |
| fin.waste_flag | object | RES/PIPE | Measured idle/overprovisioned resource evidence |


## SUST — sustainability and environmental impact


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| sust.energy | kWh/period | RES | Measured/estimated power × time and boundary |
| sust.carbon_intensity | gCO2e/kWh | RES | Location/time and published source |
| sust.embodied | gCO2e/unit | RES | Hardware embodied emissions and allocation basis |
| sust.sci_unit | functional unit | VAL | Business unit and SCI method reference |
| sust.data_quality | enum | RES | Measured, provider-supplied, modeled or unavailable |
| sust.constraints | object | CHG | Energy/carbon targets and uncertainty |


## RISK — compliance, constraints and governance


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| risk.category | enum | RISK | Operational, cyber, delivery, financial, regulatory |
| risk.acceptance | ROLE ref | RISK | Owner who can accept residual risk |
| risk.likelihood_basis | method | RISK | Distinct from guess-based numeric probability |
| risk.mitigation | ref[] | RISK | Control, test, exception and cost |
| risk.exposure_window | time interval | RISK | Time risk applies and next review |
| risk.policy_ref | URI/version | RISK | Relevant policy and clause identifier |


## CHANGE — alternatives and intervention tracking


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| change.proposal | object | CHG | Baseline, target elements, objective and sponsor |
| change.option | ref[] | CHG | Comparable architecture/deployment/pipeline options |
| change.delta | object | CHG | Cost/latency/risk/effort difference with unit |
| change.rollout | object | CHG | Experiment cohort, rollout and rollback plan |
| change.effects | OUT ref[] | CHG | Observed post-change endpoints and attribution scope |
| change.decision | object | CHG | Approver, date, caveats, selected alternative |


## EVID — measurement and data integrity


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| evid.source | URI/hash | EVID | Confidential references, integrity hash and source type |
| evid.collected_at | ISO date/time | EVID | Collection time, expiration and custodian |
| evid.protocol | ref/version | EVID | Instrument and measurement protocol |
| evid.quality | object | EVID | Coverage, missingness, sampling, calibration |
| evid.review | object | EVID | Independent approval and contradictions |
| evid.dependencies | ref[] | derived annotation | Full lineage of calculations |


## OUT — assessment, outcomes and research


| Key | Type/unit | Applies to | Rule, definition and measurement constraint |
| --- | --- | --- | --- |
| out.adoption_baseline | object | OUT | Pre-intervention scope, evidence and baseline date |
| out.adoption_outcome | object | OUT | Actual later outcomes from registered protocol |
| out.dora_metric | object | OUT/PIPE | One of current five measures with own definition |
| out.cost_error | MAE/WAPE | OUT | Hold-out forecast error metric and denominator |
| out.recommendation | object | OUT | Rationale, feasibility and approved actions |
| out.causal_design | object | OUT | Control/experiment design or explicit none |
| out.generalizability | object | OUT | Organization/site coverage and exclusions |


## 7.1 Dictionary governance and extensibility


Namespaces must be managed by a registry with key, semantic version, type, unit constraints, applicability, allowed vocabularies, source standards mapping, default freshness and normative profile. Vendor-specific keys use vendor.*; custom research keys use org.<registered-project>.*. A field that changes semantics receives a new key or major dictionary version. No field may be redefined by a new domain team while retaining the same canonical key.


## 7.2 AI profile: fifteen additional annotation families


The original 24 namespace families remain available. The following fifteen AI families (114 reference fields) extend the shared annotation contract. A field is REQUIRED only when its type/profile/scope is relevant; a missing field cannot be silently approximated by zero. Type units listed here are proposed UL-xDFD vocabulary, not claimed normative terms from external standards.


### AIMODEL — model identity and capability


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aimodel.kind | enum | MODEL | classical_ml, llm, embedding, vision, multimodal, speech, reranker |
| aimodel.id_version | string | MODEL | Immutable provider/model/weights version and checkpoint ref |
| aimodel.context_limit | token | MODEL | Nominal context limit; distinguish input/output and multimodal pricing |
| aimodel.modalities | enum[] | MODEL | Supported text/image/audio/video/structured modalities |
| aimodel.license_and_rights | ref | MODEL | Use, redistribution, commercial and derivative-model terms |
| aimodel.model_card | URI/hash | MODEL | Known limitations, provenance, evaluations and risk documentation |
| aimodel.training_cutoff | date/null | MODEL | Where known; freshness constraint, not model correctness guarantee |
| aimodel.quantization | enum/object | MODEL | Weights precision, trade-off, context and performance measurements |


### AIINF — inference consumption and service performance


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aiinf.input_tokens_billed | token/invocation | MODELSVC | Provider-billed input token count, incl. cache classification |
| aiinf.output_tokens_billed | token/invocation | MODELSVC | Provider-billed output token count incl. reasoning if priced |
| aiinf.cached_tokens | token/invocation | MODELSVC | Separately priced cached/prefix units and eligibility |
| aiinf.modal_usage | object | MODELSVC | Image/audio/video requests, units, duration or token equivalents |
| aiinf.request_rate | calls/second | MODELSVC | Observed/modelled calls, burst quantiles and scenario |
| aiinf.ttft_p95 | ms | MODELSVC | First-token latency distribution incl. streaming semantics |
| aiinf.generation_tps | token/second | MODELSVC | Decode throughput per endpoint and distribution |
| aiinf.route_fallback | object | MODELSVC | Routing/policy, fallback probability, retry count and impact |


### AIAGENT — agent state, autonomy and run budgets


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aiagent.goal | ref/string | AGENT | Intended task and permitted scope; explicit non-goals |
| aiagent.autonomy | enum | AGENT | Assistive, advisory, supervised action, bounded autonomous action |
| aiagent.step_limit | count/run | AGENT | Max orchestration/model/tool steps per attempt |
| aiagent.budget_limit | currency/run | AGENT | Hard spend/token/time cap and enforcement point |
| aiagent.planning_policy | ref/version | AGENT | Planner/re-planner version and policy controls |
| aiagent.delegation | object | AGENT | Allowed peers, propagated scope, TTL and agent identity |
| aiagent.stop_conditions | object | AGENT | Completion, abstain, escalate, interrupt/cancel/circuit breaker |
| aiagent.run_outcome | enum | AGRUN | success/fail/partial/escalated/cancelled with human/automated adjudication |


### AITOOL — tools, protocol and side effects


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aitool.schema | URI/hash | TOOL | Input/output type, version, validation constraints |
| aitool.permission_scopes | set | TOOL | Read/write scope, delegated principal and expiry |
| aitool.side_effects | enum | TOOL | Read-only, reversible, irreversible, external communication |
| aitool.approval_gate | HITL/SAFE ref | TOOL | Human or independent policy approval before critical action |
| aitool.idempotence | enum | TOOL | Retry safety, idempotency key and compensating transaction |
| aitool.calls_per_run | distribution | TOOL | Counts conditional on branching, retries, timeouts and failures |
| aitool.latency_cost | object | TOOL | API execution latency, vendor rate or resource requirement |
| aitool.protocol | object | MCP/A2A/TOOL | MCP/A2A/HTTP, version, authentication, transport binding |


### AIPROMPT — prompts, context and memory


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aiprompt.template_version | hash/ref | PROMPT | Versioned system/developer prompt artifact with restricted access |
| aiprompt.token_overhead | token/invocation | PROMPT | Prompt boilerplate and tool-schema contribution |
| aiprompt.generation_parameters | object | PROMPT/MODELSVC | Temperature, seeds if applicable, max output, top-p |
| aiprompt.data_minimization | enum/ref | PROMPT/CONTEXT | PII sanitization, retention and sensitive span controls |
| aiprompt.context_window | token | CONTEXT | Reserved user/tool/retrieval memory budget |
| aiprompt.memory_ttl | hours/days | CONTEXT | Memory expiration, editing and revocation |
| aiprompt.input_trust | enum | CONTEXT | Trusted policy vs untrusted user/retrieved/tool-returned data |


### AIRAG — retrieval-augmented generation lifecycle


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| airag.source_ref | URI/ref | CORPUS | Data origin, permission and evidence of right to retrieve |
| airag.ingest_rate | documents/day | CORPUS | Bulk/continuous source changes and refresh patterns |
| airag.chunk_size | token/chunk | CHUNK | Chunk distribution and overlap, tokenizer version |
| airag.embedding_model | MODEL ref | VINDEX | Encoder version, dimension and re-embedding policy |
| airag.vector_count | vectors | VINDEX | Live/stale vectors with index overhead and replicas |
| airag.query_topk | integer | VINDEX | Top-k and filtering policy; observed candidate count |
| airag.retrieval_quality | metric/rubric | EVAL | Recall@k, grounding, relevance, evaluation source |
| airag.refresh_lag | time | CORPUS/VINDEX | Data freshness and revocation delay |
| airag.index_cost | currency/period | VINDEX | Index build, search, disk, network, API and refresh allocation |


### AIDATA — datasets, labels and data rights


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aidata.dataset_id | URI/hash | DATASET | Dataset version, licensing, consent and source lineage |
| aidata.split_manifest | object | DATASET | Train/validation/test/holdout, leakage exclusions |
| aidata.sample_count | count | DATASET | Population, selection, class/group coverage |
| aidata.label_quality | object | DATASET | Human review, disagreement, ambiguity and inter-rater agreement |
| aidata.pii_sensitive | enum/ref | DATASET | PII classification and confidentiality boundary |
| aidata.retention_rights | object | DATASET | Removal, re-use, geographic transfer and deletion constraints |
| aidata.drift_monitor | object | DATASET | Feature/semantic/source drift and re-evaluation triggers |


### AIMLOPS — model development and delivery


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aimlops.train_run_id | EXPER ref | MODEL/EXPER | Reproducible training/fine-tuning experiment and seed |
| aimlops.method | enum | EXPER | Training, PEFT, fine-tuning, distillation, embeddings update |
| aimlops.accelerator_hours | GPU-hour | EXPER | Elapsed allocated GPU hours with device and occupancy basis |
| aimlops.checkpoint_gib | GiB | EXPER | Checkpoint storage, frequency and retention |
| aimlops.pipeline_gate | EVAL/SAFE ref | PIPE | Release gate for data/model/prompt/agent changes |
| aimlops.rollback_ref | ref/version | MODEL/PIPE | Rollback version, canary traffic and recovery proof |
| aimlops.reproducibility | object | EXPER | Code/weights/data/environment hash, deterministic limits |


### AIEVAL — AI evaluation and quality evidence


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aieval.task_success | ratio+denominator | EVAL/AIOUT | Business task completion validated by rubric and sample frame |
| aieval.groundedness | ordinal/ratio | EVAL | Claim support on traceable corpus, reviewer and rubric |
| aieval.answer_quality | object | EVAL | Human/judge quality, agreement, limitations and confidence |
| aieval.safety_rate | ratio+scenario | EVAL | Relevant violations on named adversarial case suite |
| aieval.hallucination_rate | ratio+denominator | EVAL | Operational definition, assessor and uncertainty |
| aieval.latency_slo | percentile/time | EVAL | Task end-to-end SLO, separate from per-model inference |
| aieval.fairness | object | EVAL | Harm/disparity analysis appropriate to affected population |
| aieval.eval_dataset_version | DATASET ref | EVAL | Frozen holdout for model/prompt/agent acceptance |


### AIGOV — AI management and impact governance


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aigov.intended_use | ref | AISYS | Approved purpose, affected stakeholders and prohibited uses |
| aigov.risk_class | enum/method | AISYS | Risk/impact classification with method/version and reviewer |
| aigov.model_owner | ROLE ref | AISYS/MODEL | Accountable AI system and model decision authority |
| aigov.safety_policy | SAFE ref | AISYS/AGENT | Hard tool/prompt/provider rules and independent enforcement |
| aigov.human_oversight | HITL ref | AISYS/TOOL | Approval, override, appeal, and review population |
| aigov.provider_data_terms | URI/version | MODELSVC | Data use, retention, subprocessor, geographic boundaries |
| aigov.audit_event_policy | ref | AGRUN | Logged decisions/actions excluding unnecessary sensitive content |
| aigov.impact_review | URI/ref | AISYS | Impact assessment, date, affected individuals and limitations |


### AIOPS — AI service operations and incident response


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aiops.trace_coverage | ratio+N | MODELSVC/AGRUN | Percent of runs with model/tool/agent trace and metering IDs |
| aiops.error_rate | ratio+window | MODELSVC/TOOL | Provider/tool timeouts/errors/retries with denominator |
| aiops.quality_drift | method | MODEL/AISYS | Comparison of verified outcome quality over windows |
| aiops.rate_limit | calls/s | MODELSVC | Quotas, shared tenants and overload fallbacks |
| aiops.model_uptime | ratio+window | MODELSVC | Endpoint uptime with SLA contract definition |
| aiops.agent_incident | object | AGRUN | Misuse, runaway, exfiltration, unintended action and response |
| aiops.stop_test | EVID ref | AGENT | Recorded kill/timeout and credential revoke exercise |


### AICOST — AI metering, billing and full cost


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aicost.input_price | currency/1M_token | MODELSVC | Exact billed input-token tier and rate effective date |
| aicost.output_price | currency/1M_token | MODELSVC | Exact output/reasoning token price class |
| aicost.cached_price | currency/1M_token | MODELSVC | Cache hit/billed token discount and availability |
| aicost.gpu_rate | currency/GPU-hour | GPU | Device class, capacity reservation, idle allocation, period |
| aicost.tool_price | currency/call | TOOL | External API/execution fee or self-hosted resource equivalent |
| aicost.eval_cost | currency/run | EVAL | Judge calls, human reviewer time and batch evaluation compute |
| aicost.allocated_total | currency/period | AISYS/CC | Fully loaded use-case cost with excluded categories and FOCUS bridge |
| aicost.per_success | currency/success | AIOUT | Fully allocated cost ÷ accepted independently verified successful outcomes |


### AIACT — agent authorization and containment


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aiact.permission_subject | ROLE/service_id | TOOL/AGENT | Actual service principal not model-generated role label |
| aiact.delegated_scope | object | AGRUN | Restricted authorization of peer/child agent |
| aiact.confirmation_required | boolean | TOOL | Mandatory independent user/human approval for high-impact effects |
| aiact.reversible | enum | TOOL | Read-only, reversible transaction or irreversible action |
| aiact.action_log | URI/hash | AGRUN | Tamper-evident action arguments/outcomes with privacy minimization |
| aiact.abuse_limit | object | AGENT | Token/time/spend/tool/day quotas and enforced circuit breaker |
| aiact.secret_policy | URI/ref | AGENT/MCP | Credential storage, scope, revocation and no-prompt exposure |


### AIHUMAN — human review, appeal and workforce


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aihuman.review_type | enum | HITL | Approve, inspect, challenge, override, appeal, escalate |
| aihuman.wait_duration | distribution/time | HITL | Human-in-the-loop latency and queue impact |
| aihuman.reviewer_role | ROLE ref | HITL | Accountable role and qualifications where appropriate |
| aihuman.override_rate | ratio+N | HITL | Independent human disagreement / override by scenario |
| aihuman.review_cost | currency/hour | HITL | Loaded personnel costs, time basis and scope |
| aihuman.intervention_outcome | object | HITL | Approved/rejected/corrected and later observed consequences |
| aihuman.staff_readiness | instrument | TEAM | Capability/training/participation measured without personal ranking |


### AIENERGY — AI energy and sustainability


| Field | Type / unit | Applies to | Definition and measurement constraint |
| --- | --- | --- | --- |
| aienergy.gpu_energy | kWh/period | GPU | Measured accelerator energy, device share and meter method |
| aienergy.shared_pue | ratio | GPU/RES | Facility overhead allocation and geography |
| aienergy.inference_energy | Wh/success | AISYS | Measured energy per accepted task incl. system boundary |
| aienergy.embodied_share | kgCO2e/period | GPU | Embodied hardware allocation boundary and useful lifetime |
| aienergy.carbon_factor | gCO2e/kWh | GPU | Location and grid temporal period |
| aienergy.provider_proxy | object | MODELSVC | Provider disclosed data or declared unknown for opaque API |
| aienergy.sci_functional_unit | unit | AISYS | Reference business unit and calculation boundary |


## 7.3 Profile-driven required-field rules


For AI-INFERENCE, require MODELSVC provider, MODEL version, one throughput/usage basis, per-model/token metering classes, price/version, scenario and evidence status. For AI-AGENT, additionally require AGENT/AGRUN identity, allowed TOOLs, max steps/time/cost, permission mapping and reviewed run outcomes. For AI-RAG, require corpus/index lineage, retrieval metrics, refresh and storage/embedding cost. For AI-TRAINING, require dataset rights/splits, experiment resources, evaluation gates and model artifact lineage. For AI-ASSURANCE, require explicit risk/impact and red-team/override evidence. These requirements can be checked independently with graded completeness.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
