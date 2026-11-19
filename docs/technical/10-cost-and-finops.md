# 10. Cloud, project and pipeline cost modeling




## 10.1 Required separation of financial concepts


Cost is modeled in four noninterchangeable layers: (A) engineering/project investment (human labor, training, tools and acquisition); (B) provisioning and runtime technology costs (cloud/on-prem compute, storage, network, managed services, SaaS); (C) delivery/security pipeline and observability costs; (D) economic outcome, such as attributable cost per completed reservation, net benefits or avoided incident loss. Different accounting treatments are never collapsed without an explicit reconciliation policy. These boundaries prevent an apparently low cloud bill from hiding implementation and team costs.


| Cost layer | Representative items | Financial qualifier |
| --- | --- | --- |
| Project / change lifecycle | Person-hours × loaded rates by role, onboarding, integration, training, consulting, security assessment | Estimate vs approved budget vs actual; CAPEX/OPEX treatment is local policy |
| Technology operations | vCPU/VM/node hours, storage tiers, DB, bandwidth, SaaS licenses, network, backup, observability | Cloud bill, invoice, FOCUS normalized columns or metered private-cloud costs |
| CI/CD and DevSecOps | Runners, test infrastructure, scan minutes/licenses, artifact storage, failed/re-run jobs, reviewer hours | Run-specific quantity, allocation to product/phase and marginal vs fully loaded cost |
| Governance and risk | Compliance audit, contract, remediation, support effort, change approval work | Avoid speculative “risk savings” as realized cash |
| Business value and outcomes | Cost per completed booking, release lead-time improvement, avoided outage exposure | Define denominator, valuation basis, attribution and uncertainty |
| AI model/agent services | Hosted inference/token API; training/fine-tune GPU time; vector retrieval; tool calls; AI observability/evaluation; labor | Distinguish input/output/cache/multimodal metering, hosted vs self-hosted, AI direct/indirect costs, and double-count prevention |


## 10.2 Cost equations and reconciliation


For a scenario s and a calendar/accounting period t, forecast cost C(s,t) = Σ_i quantity_i(s,t) × effective_rate_i(t,contract,location) + usage_fees + shared_allocations + licenses + engineering_labor + migration_cost + monitoring + risk_controls − applicable_credits. Apply exclusive cost categories, recognized-period treatment, commitment eligibility, cash-versus-amortized basis and taxes separately; do not subtract a credit twice or assume reserved capacity is free.


A business unit metric is C_attributable / N_valid_business_units. Both numerator and denominator must use compatible products, periods, customer segments and inclusion/exclusion criteria. Provide a cost-allocation coverage measure and an “unallocated” remainder. FOCUS v1.4 [S11] can normalize technology usage/cost records and support invoice reconciliation, but is not itself a full software-project cost model; human work and organizational interventions remain UL-xDFD extension objects.


For shared resource R with owner weights w_j ≥ 0: allocated_cost_j = w_j × shared_cost_R and Σ_j w_j ≤ 1. The residual (1−Σ_j w_j) is explicitly unallocated and never silently omitted. Transfer charges must not be reassigned independently at both sender and receiver unless the ledger explicitly defines distinct charges.


## 10.3 CI/CD cost and scan-optimization profile


A delivery pipeline is modeled as job/event nodes with ordered or parallel gates, human waiting, build and test artifacts, security scanners and runner infrastructure. For pipeline job j: Cj = runner_minutes_j × rate_j + tool_fees_j + artifact_storage_j + transfer_j + human_review_hours_j × loaded_rate_j + allocated_shared_cost_j. If runner charges are already included in a shared subscription bill, do not add a second standalone charge without a marginal-cost rationale.


For risk-driven pipeline optimization, decisions select scan target/depth/schedule x_j subject to a mandatory-security-controls set, expected risk budget, quality gates and maximal delivery latency. The optimization may minimize expected cost/latency, but risk is a constraint not an optional penalty. A baseline full scan, change-aware scan and zero-knowledge fail-safe policy should be compared; permission to skip tests/scanners must be supported by an explicit policy, not generated from an unvalidated risk score.


## 10.4 Private cloud and on-premises cost


Private-cloud costing must include measured or estimated energy (IT and, if available, facility overhead), hardware acquisition amortization/depreciation, maintenance, networking, licenses, floor/rack/cooling costs if within scope, capacity slack and shared staffing. Energy estimates should use actual measured power at a declared boundary and sampled duty cycle; constant per-core watt assumptions are only research simulation parameters, not real hardware consumption. Allocation of shared node energy to services is model-based and should be compared with metering where feasible.


## 10.5 Forecast errors and scenario governance


A forecast report contains central estimate and uncertainty interval, spend by month and component, charge source, excluded items, price/FX/tax assumptions, capacity utilization, per-business-unit economics, drivers, sensitivity and reconciliation. Evaluate forecasts prospectively using MAE, RMSE, WAPE (when denominator is meaningful), signed bias and interval coverage by horizon; MAPE is undefined at actual zero and unstable for small actuals. Forecast accuracy for cloud bills must be distinguished from prediction accuracy for a new application without measured baseline.


## 10.6 Complete AI cost-accounting model and forecasts


For a chosen currency and effective price tier, API inference cost is calculated by summing provider-billed quantities, not by interpreting narrative model responses. For model m and pricing class k: C_API = Σ_m Σ_k Q_billed(m,k) × P(m,k). If rate cards quote currency per million tokens, first divide billed tokens by 1,000,000. Non-token modalities (images, minutes, requests, provisioned throughput) use their own billing meters.


Total cost of AI-enabled value stream per period = API inference + self-hosted/reserved GPU capacity (without duplicating included provider token charges) + embeddings/index and retrieval + external tools + guardrails/evaluation + observability/storage/egress + software development/operations/human review + attributable common costs + contractual fees − applicable credits. Taxes, invoice reconciliation, financial recognition, sunk costs and incremental opportunity costs are reported separately where material.


| Cost family | Primary usage quantities | Required allocation/reconciliation check |
| --- | --- | --- |
| Inference API | Billed input/output/cache tokens, images/audio/video, tier or rate | Provider request IDs vs metering ledger, price effective date |
| Self-hosted inference | GPU-hours, RAM/storage, orchestration and idle reservation | No duplicated hosted token charge, measured deployment boundary |
| Training / tuning | GPU-hours, experiments, datasets, checkpoint, evaluation | CapEx/OpEx recognition and trial-failure cost allocation |
| RAG / embeddings | Tokens embedded, index build, vectors stored, queries/rerank | Corpus update windows, index replicas, allocation |
| Agent tools | API calls, workflow executions, human approval, side effects | Actions vs attempts; side-effect cleanups and compensations |
| Quality/safety/ops | Red team, eval judge or human hours, logs, telemetry, incident | Costs may be necessary even when token spend is low |
| Contract/commitments | Reserved capacity, minimum spend, license, credits, taxes | Net vs gross and commitment coverage in FOCUS bridge |
| Business unit | Validated completed task, booking, resolution or conversion | Do not divide by requests when success denominator is different |


AI FinOps must also distinguish direct model provider charges from secondary cloud resources and labor. Forecast interval width is driven by model route mix, context length, user growth, looping/failures, cache behavior, price changes and quality-gate acceptance. Every forecast is scenario-based (normal, peak, long-context, abusive-runaway, provider outage, model migration, quota reduction).


Unit economics: Cost_per_accepted_task = total fully allocated cost attributable to AI-supported attempts / independently verified accepted successes. A separate “incremental AI cost per incremental success versus non-AI baseline” is needed for ROI; denominator can be zero, which must be reported as undefined, not zero. Productivity estimates require measured workflow time and quality, not agent output counts.


FOCUS 1.4 can normalize provider billing and AI service categories but does not expose every prompt/agent run. The solution must bridge provider request/cost IDs to FOCUS-aligned invoices while recognizing missing allocation and avoiding invented token-level mappings in opaque bills. FinOps Foundation AI guidance prioritizes fully allocated cost and per-business-outcome value [S29–S30].


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
