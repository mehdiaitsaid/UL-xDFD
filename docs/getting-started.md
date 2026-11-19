# Getting started with UL-xDFD

UL-xDFD begins with a question, not a diagramming tool. Choose a small value stream—one use case and one environment—and identify the decision you need to support. For example: *How much could an AI-assisted hotel-booking flow cost per month, and what must be true before an agent is allowed to finalize a paid reservation?*

## 1. Set the boundary

Name the product, process, team, and environment you are studying. Define the model's time window, beneficiaries, and what is deliberately excluded. Do not mix production actuals with design-time assumptions. A current-state and a proposed future-state model are separate snapshots.

In a booking example, the customer, booking API, payment processor, AI model endpoint, and payment approval may be relevant. A third-party payment service is external **relative to the selected system boundary**.

## 2. Draw the logical DFD

Start with external entities (`X`), transformations (`P`), stores (`S`), and directed data flows (`F`). Label requests and responses separately when their volumes or sensitivities differ. Do not draw an AI tool permission as a data-flow arrow. The [element catalog](technical/05-elements-edges-notation.md) distinguishes relation types.

## 3. Add the surrounding context

Link the DFD to a value unit, requirement, deployment component, responsible role, workflow decision, and the resource or charge that it drives. Only annotate the properties necessary for the initial decision. Unknown values are legitimate data: write `unknown` rather than creating a convenient number.

## 4. Add AI components if they exist

A hosted model endpoint and an LLM model version are separate objects. An agent has a definition, an authorized tool inventory, and executions. Retrieval has its own corpora and indexes. A tool that can cause an external side effect must have an independent authorization path. Read [AI and agentic modeling](ai-and-agentic.md).

## 5. Attach a scenario and evidence

A numeric claim needs a value, unit, scope, source kind, evidence status, and relevant timestamp. It must be clear whether a figure is per request, per run, per replica, or aggregated for a month. For example, `1500 token/invocation` in the YAML example is **hypothetical**. It is not a measurement of a real model.

## 6. Validate the starter example

From the repository root, using Python 3:

```bash
python -m pip install -r requirements.txt
python tools/validate.py examples/hotel-ai.yaml schemas/ul-xdfd-ai-v1.schema.json
```

The command reports a structural pass or the issues it found. It does not run the 79 proposed semantic rules or any external assessment framework.

## 7. Decide what to test next

Use the graph to identify missing inputs and review ownership. Then design a small measurement study: request rates, token and tool-call counts, model quality, CPU/GPU utilization, billing quantities, or developer workflow timing. Keep observed outcomes separate from earlier forecasts. The [modeling guide](modeling-guide.md), [quality rules](validation.md), and [research protocol](technical/16-research-validation.md) show how to progress.

[Back to README](../README.md)
