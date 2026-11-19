# What validation means

UL-xDFD calls something *valid* only relative to the checks that were actually applied. A file that parses is not necessarily a coherent model; a coherent model is not necessarily a correct estimate; and a correct billing calculation does not prove that an agent is safe.

## Checks implemented in the starter kit

The included [`tools/validate.py`](../tools/validate.py) performs selected structural tests. It checks the supplied JSON Schema, dangling graph references, annotation and scenario targets, observed annotations without evidence, missing referenced evidence, basic numeric units, and constraint targets. It will not access real cloud accounts or execute AI agents.

Run:

```bash
python -m pip install -r requirements.txt
python tools/validate.py examples/hotel-ai.yaml schemas/ul-xdfd-ai-v1.schema.json
```

## Proposed semantic catalog

The full language proposes **37 general rules and 42 AI-specific rules**, covering cross-view traceability, decisions and workflows, resource consistency, cost allocation, measurement provenance, governance, authorization, agent budgets, data rights, evaluation evidence, and safety. These rules are in [the technical validation section](technical/08-validation-rules.md). Most are **not** implemented by the example script.

### Severity

- **Error:** a critical requirement for a particular output is violated. That output should not be represented as conformant.
- **Warning:** an output may be provisional if its limitation is visible.
- **Information:** an improvement opportunity or noncritical quality issue.

For example, missing model-token price assumptions do not prevent rendering a logical DFD, but they should prevent claiming a precise inference-cost forecast.

## A meaningful testing progression

Start with schema and references. Next, add semantic relations and decomposition balancing. Then implement cost/unit reconciliation and explainable diagnostic rule outputs. Real telemetry, invoice verification, stakeholder review, and controlled comparisons are separate evaluation layers.

[Back to README](../README.md)
