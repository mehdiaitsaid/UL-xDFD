# FinOps, AI consumption, and cost modeling

## Start by choosing the accounting question

A cloud bill, a project budget and cost per successful business outcome are different metrics. UL-xDFD separates engineering effort, infrastructure/managed services, delivery/security pipelines, governance activities, AI components, and verified business value. Where a charge is shared, its allocation or unallocated remainder must be visible.

## A practical cost chain

```text
scenario volume
   × actions per scenario
   × usage per action
   × price per usage unit
   + reserved/shared charges
   + project, tools, operations and assurance costs
   - applicable credits
   = scenario cost under declared accounting assumptions
```

This is a planning structure, **not** a universal cost equation that eliminates provider-specific billing rules. Each quantity must have a period, currency, contract/region where relevant, and a source. Avoid adding a monthly provisioned-capacity charge twice when it already covers inference consumption.

## AI provider charges

For a provider class priced in currency per million tokens:

`class_cost = provider_billed_tokens / 1,000,000 × effective_rate`

Compute each class separately. Do not equate a local tokenizer estimate with the quantity a provider bills. Image, audio, provisioned throughput and tool charges can use different units. Maintain request- or batch-level correlation where invoices make it available and disclose allocation gaps where they do not.

## Agent and RAG expenses

An AI-assisted workflow may include model calls, retries, embeddings, index maintenance, retrieval, tool APIs, evaluation, logging, human authorization and rollback. An agent capable of repeating calls must specify step, time, token and spend budgets. Forecasts should test both normal and runaway/failure scenarios.

## Outcomes, not just calls

`cost_per_accepted_task = attributable_cost / independently_verified_accepted_tasks`

If the denominator is zero, the ratio is **undefined**, not zero. To argue that an agent generates value, compare it with a non-AI or prior-process baseline and consider completion quality, latency, labor and risk—rather than celebrating a lower price per token.

## Billing evidence

[FOCUS](https://focus.finops.org/what-is-focus/) helps normalize technology costs and reconcile billing information; the [FinOps Framework](https://www.finops.org/framework/) supplies a broader practice and value vocabulary. Neither provides the entire project labor model or guarantees that a vendor invoice can identify an individual agent run. UL-xDFD records that attribution bridge as an explicit assumption or measurement.

The complete proposal covers [workload propagation](technical/09-workload-and-capacity.md), [project/cloud/pipeline/AI costs](technical/10-cost-and-finops.md), and [AI metering boundary checks](technical/appendix-f-ai-cost-checklist.md).

[Back to README](../README.md)
