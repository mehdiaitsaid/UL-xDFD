# 8. Structural and cross-view validation rules




Validation consists of syntactic/schema checks, semantic cross-view invariants, evidence/data-quality checks, and scenario/decision gates. The first category can be enforced deterministically, while expert review remains necessary for semantic correctness. Each result has rule ID, severity (ERROR/WARNING/INFO), target IDs, evidence, explanation and suggested remediation. Exceptions are explicit records with approver and expiration.


| Rule | Domain | Validation assertion |
| --- | --- | --- |
| D01 | DATA | DATA edge source and target must be allowed DFD pairs, including P↔S and X↔P, not unexplained S→S. |
| D02 | DATA | Processes at every published level have inputs and outputs; source/sink exceptions are justified. |
| D03 | DATA | Parent/child decomposition balances boundary-crossing flow semantics and contracts. |
| D04 | DATA | Request and response distinguish sizes, direction, data classification and volume if materially different. |
| D05 | DATA | Payload and units are explicit; classification propagates conservatively across transformations. |
| G01 | GRAPH | Each node/edge ID is unique; endpoints/parent/evidence refs exist or are marked unresolved. |
| G02 | GRAPH | Typed edges cannot be inferred from an unlabeled arrow or diagram coloring. |
| G03 | GRAPH | Cycles and cross-organization loops are identified; no infinite recursive decomposition. |
| L01 | LIFECYCLE | All in-scope required phases, roles and decisions have coverage declarations. |
| L02 | LIFECYCLE | Critical requirements trace to process, implementation, tests and deployment/operation. |
| W01 | WORK | Every workflow precedes/retries relation has trigger semantics and finite assumptions. |
| W02 | WORK | Gateway outcomes have documented predicates and missing-case/default policy. |
| W03 | WORK | Human gates specify accountable role, calendar, wait distribution or unknown status. |
| W04 | WORK | Parallel join semantics are explicit; no naive summation of p95 latencies. |
| P01 | PEOPLE | Critical decisions have accountable owner; team handoffs specify acceptance and fallback. |
| P02 | PEOPLE | Culture assessments contain instrument, safe aggregation, response coverage and evidence. |
| Q01 | QUALITY | Every critical SLO/constraint has metric, comparator, unit, window, scope and test. |
| Q02 | QUALITY | No objective evidence is inferred from a reported organizational opinion. |
| C01 | CAPACITY | Compute demand uses measured/estimated CPU time, not automatically wall time/clock frequency. |
| C02 | CAPACITY | Flows changing count, volume or cardinality have explicit transformation operators. |
| C03 | CAPACITY | All loops/retries have finite bounds or a stable modeled traffic process. |
| C04 | CAPACITY | Shared cost/resource quantity is not duplicated across services and view projections. |
| C05 | CAPACITY | Memory, storage and network use distinguishable units and multiplicity scope. |
| S01 | SECURITY | Every trust crossing/sensitive store has data class, threat/control review and owner. |
| S02 | SECURITY | No secrets or unredacted personal data are persisted in annotations. |
| S03 | SECURITY | Access/policy exception has approving role, expiry and review evidence. |
| F01 | FINOPS | Charges have billing interval, currency, unit rate, pricing basis and source. |
| F02 | FINOPS | Allocations across owners sum to 1 (or retain an explicit unallocated remainder). |
| F03 | FINOPS | Usage/credit/commitment/amortization/tax treatment prevents double counting. |
| F04 | FINOPS | Actual and forecast columns are not silently mixed in the same total. |
| E01 | EVIDENCE | Observed records reference date/source; reported/estimated claims are not relabeled observed. |
| E02 | EVIDENCE | Disputed, expired, unknown and unsupported critical values block inappropriate claims. |
| E03 | EVIDENCE | All derived outputs link to inputs, model versions and assumption ledger. |
| R01 | RESEARCH | Predictive baseline features are frozen before outcome collection and use no future leakage. |
| R02 | RESEARCH | Diagnostic readiness construct is not equated to unvalidated adoption success probability. |
| O01 | OPTIM | Optimization satisfies nonnegotiable security/policy/SLO bounds and logs trade-offs. |
| O02 | OPTIM | Alternatives compare like-for-like value units, prices, periods and scenarios. |
| AI-STR01 | STR | Every AI model endpoint and agent run has a stable identity, provider/owner, version and scenario/boundary. |
| AI-STR02 | STR | AI inference and tool calls are separate edges; a DFD DATA transfer never implies action authorization. |
| AI-STR03 | STR | AI model outputs, embeddings, prompts and tool results are represented as distinguishable information assets. |
| AI-STR04 | STR | Multi-agent delegation retains identity/trace correlation, authority scope and exit policy. |
| AI-STR05 | STR | Model routing/fallback is explicit and provider/price-specific; model versions are immutable within a frozen snapshot. |
| AI-STR06 | STR | Every AI call/agent iteration maps to exactly one metering and provenance path or explicit unmetered status. |
| AI-DATA01 | DATA | RAG corpus content has origin, license/purpose, data class, retention and update/re-index evidence. |
| AI-DATA02 | DATA | Prompt/context/response recording is minimized; no sensitive raw prompts in publicly shared model snapshots. |
| AI-DATA03 | DATA | Embedding/index lineage ties chunks, encoder version, dimension and index build to a source corpus. |
| AI-DATA04 | DATA | Train/validation/test/evaluation partitions have contamination/leakage checks and rights-to-use documentation. |
| AI-DATA05 | DATA | Vector memory and persistent agent memory declare TTL, revocation, ownership and poisoning detection. |
| AI-DATA06 | DATA | Cross-tenant or cross-region AI data paths receive explicit trust and residency review. |
| AI-CTRL01 | CTRL | Every autonomous action has executable allow/deny policy distinct from model-generated guidance. |
| AI-CTRL02 | CTRL | Side-effectful or high-impact tools identify human confirmation, rollback or compensating action. |
| AI-CTRL03 | CTRL | Agent loops have step/tool/token/time/spend caps and stop/timeout/cancel behavior. |
| AI-CTRL04 | CTRL | Delegated credentials are least-privileged, scoped to run or operation, expiring and revocable. |
| AI-CTRL05 | CTRL | Agent failure, uncertainty or conflict has escalation/handoff and recovery procedure. |
| AI-CTRL06 | CTRL | MCP/A2A transport, authentication and protocol-version compatibility are declared where used. |
| AI-USAGE01 | USAGE | Billed input/output/cached/reasoning/multimodal usage units are not conflated or double-counted. |
| AI-USAGE02 | USAGE | A provider-reported billed token amount and tokenizer-derived estimated tokens have separate provenance. |
| AI-USAGE03 | USAGE | Agent expected call counts account for branch and retry distributions, including truncation and correlation. |
| AI-USAGE04 | USAGE | Hosted token API costs are distinguished from self-hosted accelerator and idle-reservation charges. |
| AI-USAGE05 | USAGE | GPU compute-hours and memory-hours have explicit device/runtime basis and measurement boundary. |
| AI-USAGE06 | USAGE | Tool, retrieval, indexing, observability and development costs are included or listed as excluded. |
| AI-EVAL01 | EVAL | Every declared AI quality goal includes a benchmark/eval set, sampling plan, metric, human/judge rubric and uncertainty. |
| AI-EVAL02 | EVAL | Offline benchmark scores and online business success are labeled different outcome constructs. |
| AI-EVAL03 | EVAL | LLM-as-judge outputs disclose judge/version and are not treated as infallible ground truth. |
| AI-EVAL04 | EVAL | All critical deployment gates include red-team/adversarial and regression evidence where relevant. |
| AI-EVAL05 | EVAL | Fairness, safety, misuse and material harmful impact are evaluated by context rather than graph properties. |
| AI-EVAL06 | EVAL | Post-deployment evaluation uses drift, quality and change-triggered review criteria. |
| AI-FIN01 | FIN | AI rate-card version, effective date, currency and tier are attached to all priced model/tool meters. |
| AI-FIN02 | FIN | Provider usage ledger is reconciled to invoices/FOCUS fields at a declared period and allocation grain. |
| AI-FIN03 | FIN | Cost per successful task uses independently defined successful-task denominator and excludes failed outputs from numerator only if policy specifies. |
| AI-FIN04 | FIN | Costs for AI trials, training/fine-tuning, data preparation, shared infrastructure and labor have allocation rules. |
| AI-FIN05 | FIN | Comparative model routing prices control for quality, workload mix, latency, risk and regional availability. |
| AI-FIN06 | FIN | AI cost forecasts present error bounds and drift triggers, not only a single point estimate. |
| AI-SAFE01 | SAFE | Security review covers prompt injection, tool misuse, output handling and agent supply chain for applicable boundaries. |
| AI-SAFE02 | SAFE | Provider API/data-retention terms and access rights are reviewed per AI system and geography. |
| AI-SAFE03 | SAFE | Tool-result or retrieved-document instructions are treated as untrusted data, not automatically elevated to policy. |
| AI-SAFE04 | SAFE | AI safety impacts and material risk approvals are linked to named accountable roles, not assumed from model score. |
| AI-SAFE05 | SAFE | A testable circuit-breaker / kill switch exists for privileged/long-running agents and its evidence is recorded. |
| AI-SAFE06 | SAFE | Potential external effects of agent actions are logged and reviewable with privacy controls. |


## 8.1 Validation severity and publishability


ERROR prevents an applicable conformance badge or quantitative output. WARNING marks a quality limitation and may permit provisional output with disclosure. INFO captures improvement opportunities. If quantitative assumptions remain unknown on a critical path, the model can still publish a structural view but should return “insufficient evidence” for affected forecasts. A readiness profile may still identify evidence-gathering tasks; it must not replace absent measurements with invented scores.


## 8.2 Coverage indicators


Coverage is measured over a declared population: critical requirements traced / in-scope critical requirements; critical flows with payload and scenario / all in-scope critical flows; charge amount allocated / attributable charge amount; stakeholder groups with recorded review / required stakeholder groups; scenarios with validated resource inputs / planned scenarios. Report numerator, denominator, date and exclusions, not merely a percentage. Completeness is always scope-relative.


## 8.3 AI-specific cross-view validation catalog (42 rules)


The base document lists 37 general semantic validation rules, which remain applicable to AI components. Version 1.0 adds 42 AI-specific rules in the existing validation table, for 79 total baseline + AI rules. These rules are requirements of the proposed research language, not a proof of model trustworthiness or any external-standard compliance.


| Rule group | Count | Sample critical failure and consequence |
| --- | --- | --- |
| AI-STR | 6 | Dangling model version, no call identity or missing relationship type → invalid trace |
| AI-DATA | 6 | Unlicensed RAG corpus, missing split or memory privacy ambiguity → held assessment |
| AI-CTRL | 6 | High-impact tool lacks independent authorization/stop criteria → critical gate |
| AI-USAGE | 6 | Billed token classes merged or tool/retrieval costs omitted → invalid cost output |
| AI-EVAL | 6 | No independent benchmark/denominator; judge assumed to be ground truth → unsupported quality claim |
| AI-FIN | 6 | Rate card not effective for scenario window or success count mismatch → unreconciled FinOps |
| AI-SAFE | 6 | Injection/tool permission/circuit-breaker review missing → security hold |


Severity policy: BLOCK invalid structure, unsafe autonomous action publication, untraceable billed charges, data-access breaches or prospective predictive claims with leakage; HOLD a decision where critical risk/quality evidence is unknown; WARN on estimated resource/quality assumptions with explicit uncertainty; INFO on optional telemetry and enrichment. Coverage reports MUST show unknown and disputed counts and cannot hide failures inside a weighted average.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
