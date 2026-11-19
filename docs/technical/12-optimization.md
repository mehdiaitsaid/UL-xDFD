# 12. Optimization and decision-support methods




## 12.1 Optimization problem family


UL-xDFD identifies alternatives and input constraints; solvers remain plug-ins. Typical decision variables include service placement and sizing, horizontal replica limits, CI parallelism, test/scan scheduling, storage tiers, cache placement, data retention, deployment region, commitment procurement and change approval routing. Objective vectors may include total lifecycle cost, p95 end-user latency, reliability, development lead time, cloud/energy use, blast radius and staff burden. The Pareto frontier is often more meaningful than a single weighted optimum.


Generic formulation: choose x ∈ feasible configurations to minimize (C_lifecycle(x), T_delivery(x), L_tail(x), E_carbon(x)) subject to SLO(x), RTO/RPO(x), required_security_controls(x), staffing_capacity(x), regulatory constraints(x), budget(x) and resource limits(x). All uncertain constraints must state whether robust worst-case, chance-constrained or scenario-based interpretation is used; unknown inputs cannot be assumed feasible.


## 12.2 Candidate use cases and evidence required


| Optimization target | Required model information | Do not overlook |
| --- | --- | --- |
| Cloud rightsizing | Per-service demand distributions, utilization, quotas, measured performance and prices | Peak bursts, failure headroom, reservation commitments |
| Placement / microservice partition | Cross-flow rates/sizes, data sensitivity, coupling, deployment autonomy | Distributed transaction overhead, domain boundaries, ops labor |
| CI/CD sequencing | Job graph, work and wait times, failure/retry rates, runner and license costs | Security mandatory gates and flakiness |
| Risk-directed DevSecOps scan | Change paths, dependency graph, scanner cost, control/risk policy | False negatives, mandatory sensitive components |
| Deployment strategy | Release cadence, rollout/rollback, test and outage history | Migration risk, data compatibility and downtime |
| Storage/network | Retention, compliance, IOPS/throughput, region/transfer charges | Disaster recovery and restore obligations |
| Team/approval flow | Handoff delays, accountability, workload, feedback | Culture cannot be “optimized” by graph operations alone |


## 12.3 Counterfactual and intervention evidence


When proposing a cost reduction, preserve a baseline snapshot and change only named variables. Report predicted delta with uncertainty plus independent experimental/operational measurement after deployment. If the intervention changes traffic mix, security posture or quality conditions, these changes must be compared and disclosed rather than attributing every cost decrease to the algorithm. Field pilots should seek randomized or matched controls where feasible and report implementation costs and delayed effects.


## 12.4 AI and agent optimization as a constrained multiobjective problem


Let x encode model tier/routing, prompt strategy, RAG top-k/index, agent tool policy, max steps, inference placement, GPU batching, caching and CI evaluation schedule. Compare admissible alternatives on expected total spend, accepted-task utility, p95 latency, failure/harm risk, privacy, energy, human workload and compliance. One possible form is min_x E[C_total(x)] + α E[T_task(x)] + β E[Risk(x)] subject to hard policy constraints, task-success lower bound, privacy/data-locality rules, and capacity/rate-limit constraints. The coefficients are decision weights requiring expert elicitation and sensitivity analysis; they are not globally valid constants.


| Optimization target | Decision variables | Nonnegotiable comparison/validation |
| --- | --- | --- |
| Model routing | Cheap vs premium model by task difficulty; fallback gates | Matched prompts, success rubric, privacy and error bars |
| Context/prompt efficiency | Compress context, cache stable prefix, remove redundant retrieved chunks | No hidden quality/safety regression |
| RAG optimization | Chunk size, index policy, top-k, reranking and refresh | Retrieval recall, freshness, license and cost |
| Agent control/loop budget | Max steps, permitted tools, validation and escalation | Success and risk impact measured; no silent policy bypass |
| GPU and deployment | Quantization, batching, endpoints, scale-to-zero, spot/reservation | Latency, reliability, model accuracy and energy |
| Training/fine-tune | Checkpointing, LoRA/PEFT, distillation, early stop | Measured quality, data rights and total experimentation cost |
| AI in CI/CD | Selective model tests and red-team runs based on risk/changes | Mandatory security gates and no post-hoc quality leakage |


Recommendation outputs must provide the baseline and alternative, projected benefit range, quality/risk trade-off, required evidence, reversibility, policy approval and experimental verification plan. Pareto-front solutions are preferred to a single magic “optimal” architecture when business constraints are contested or estimated.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
