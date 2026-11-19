# Appendix A. YAML serialization and reference guidance

The earlier unified proposal included a small **non-AI v0.1 illustration**. This repository uses the later **v1.0 AI/agentic structural schema**, so examples should not silently mix the two versions. The canonical, runnable v1.0 fixture is [`examples/hotel-ai.yaml`](../../examples/hotel-ai.yaml).

## File contract

The v1.0 root includes `spec_version`, `metadata`, `phases`, `scenarios`, `nodes`, `edges`, `annotations`, and `evidence`. A `constraints` section and the selected `ai_profiles` may also be included. The JSON Schema is under [`schemas/ul-xdfd-ai-v1.schema.json`](../../schemas/ul-xdfd-ai-v1.schema.json).

## A valid reference header

```yaml
spec_version: '1.0'
metadata:
  id: hotel-ai-booking
  name: Hotel AI assistant example (synthetic)
  revision: 1
  status: hypothetical
  date: '2026-11-15'
phases:
  - id: L03
    label: Architecture
  - id: L09
    label: Operation
scenarios:
  - id: SC-ai-booking
    label: AI-assisted hotel booking
    environment: simulation
    phase_id: L09
    window: synthetic-month
```

This is only an **excerpt**: it intentionally omits the remaining required collections. Use the linked fixture to validate a complete model.

## Interoperability and migration

Identifiers are stable within their lineage. When importing earlier xDFD or E-DFD models, retain original IDs in a namespaced alias and map property names explicitly. Do not transform a `DATA` edge into workflow precedence, a model suggestion into an authorization, or an unmeasured value into an observation. Numeric records require units, a scenario, and provenance. Conformance requires more than passing the structural schema.

---

[Documentation home](../../README.md) · [Technical reference index](README.md)
