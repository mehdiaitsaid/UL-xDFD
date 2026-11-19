# Research and implementation roadmap

UL-xDFD v1.0 is a research specification with a small reference implementation. The milestones below are proposed work, not completed releases.

| Stage | Intended result | Suggested acceptance evidence |
| --- | --- | --- |
| R0 — Specification consolidation | Stable identifiers, views, annotation vocabulary and versioning policy | Independent terminology review; resolved semantic conflicts |
| R1 — Semantic validation | Implement selected cross-view rules beyond JSON Schema | Positive/negative fixtures and reproducible failures |
| R2 — Modeling workflow | Editor or import pipeline; review and snapshot management | Two independent analysts model the same bounded case |
| R3 — Quantitative engine | Scenario propagation, resource and cost calculations, uncertainty | Checked units, calibration data and invoice comparisons |
| R4 — Integration adapters | Trace, lineage, workflow, CI, cloud usage and AI metering imports | Recorded version contracts and repeatable round trips |
| R5 — Decision support | Cost- and risk-constrained alternatives, explainable trade-offs | Controlled comparisons with established baselines |
| R6 — Field research | Diverse product/team pilots with measured outputs | Coverage, review effort, consistency and user utility |
| R7 — Predictive studies | Frozen baseline factors with later independent outcomes | Grouped/time-aware splits, calibration and external validation |

## Research questions worth testing

Does the extended model reveal material cost or adoption blockers that a conventional DFD, survey, architecture document, or billing dashboard would miss? Do analysts agree more often, or does annotation burden outweigh the benefit? Can model-based cost forecasts improve beyond simple traffic × unit-cost baselines? Do agentic elements improve cost attribution and safety review? These are testable hypotheses, not established findings.

## Roadmap guardrails

A readiness diagnostic should describe evidence-backed gaps even before any predictor exists. No adoption probability should be marketed before independent prospective validation. A model optimizer must preserve mandatory security and service constraints. Study costs should include data collection and maintenance, not just implementation speed.

See [conformance and implementation plans](technical/18-conformance-and-roadmap.md) and [academic validation](technical/16-research-validation.md).

[Back to README](../README.md)
