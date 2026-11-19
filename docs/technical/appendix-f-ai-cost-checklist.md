# Appendix F. Quantitative equations, meters and cost-boundary checklist




| ID | Relationship / equation | Unit or non-equivalence |
| --- | --- | --- |
| EQ-AI-01 | Calls/month = AI sessions/month × E[calls/AI session] | Model invocation, not session; use branching and retries |
| EQ-AI-02 | Token cost = Σ(class m) billed_tokens_m × unit_price_m | Class-dependent currency/1M tokens, not one blended average |
| EQ-AI-03 | Provider API cost = Σ endpoint calls + modality-specific API items | Do not add self-hosted GPU charge for included hosted calls |
| EQ-AI-04 | GPU allocation = Σ replicas × booked GPU hours × rate | Allocated capacity vs useful utilization and standby cost |
| EQ-AI-05 | Cost per accepted AI task = fully allocated AI-related cost / independently accepted successes | Undefined when accepted successes = 0; not automatically ROI |
| EQ-AI-06 | Total project cost = lifecycle labor and procurement + delivery + operational platform + AI total + retirement | Accounting scope, taxes, CapEx/OpEx and credits specified |
| EQ-AI-07 | RAG cost = embedding + index/storage + retrieval/reranking + network + operations | Avoid counting index storage both under RAG and general cloud twice |
| EQ-AI-08 | Agent expected cost = Σ paths P(path) × cost(path); plus failures/safety overhead | Branch correlations, truncation, max steps, retry and escalation |
| EQ-AI-09 | AI task p95 = empirical/simulated percentile of full task path duration | Cannot sum independent p95 component latencies |
| EQ-AI-10 | AI energy/task = total attributed system energy / validated tasks | Boundary, PUE, energy source and sharing rules required |
| EQ-AI-11 | Savings = cost_baseline − cost_alternative with quality/risk guards | Same period, currency, demand, task definition and outcome threshold |
| EQ-AI-12 | Intervention effect = observed treated outcome − credible counterfactual | A before/after comparison alone cannot prove causation |


Mandatory forecast boundary checklist: model and prompts pinned; traffic/calendar mix; token classes; inference type; retries/fallback; RAG storage and query pattern; training/fine-tuning schedule; agent tool budgets; human approval; provider quotas; direct and shared costs; provider price effective date; billing currency; invoice/FOCUS bridge; value denominator; uncertainty interval; missing data and evidence owner.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
