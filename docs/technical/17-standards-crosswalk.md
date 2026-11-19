# 17. Standards, protocols and interoperability mapping




The following mapping distinguishes external sources from UL-xDFD-origin conventions. Alignment means concept reuse or documented import/export and never certifies conformance. Versions shown were checked against official organizations where available as of 15 November 2026. For licensed standards, consult the authoritative text before implementing or asserting formal compliance.


| External reference | Purpose | UL-xDFD use | Conformance boundary |
| --- | --- | --- | --- |
| [S1] ISO/IEC/IEEE 12207:2026 | Software life cycle processes | L00–L11 lifecycle coverage, stakeholder/process semantics | Reference terminology; UL-xDFD is not a 12207 assessment |
| [S2] ISO/IEC/IEEE 42010:2022 | Architecture description viewpoints | One model, distinct concerns and synchronized views | Complementary AD language, not conformance by naming |
| [S3] OMG BPMN 2.0.2 | Process ordering, gateways, events | V2 links to workflow/process artifacts | Do not use DFD arrows as BPMN sequence flow |
| [S4] OMG DMN 1.6 | Decision modeling | Gateway/predicate and decision references | External DMN engine owns execution semantics |
| [S5] ISO/IEC 25010:2023 | Nine-characteristic product quality model | Quality requirements and verification | A mapping, not licensed text reproduction |
| [S6] W3C PROV-O | Provenance entities, activities and agents | EVID lineage, derivation and source attribution | Explicit compatible mapping required for interoperability |
| [S7] OpenTelemetry | Distributed traces, metrics, logs and semantic conventions | Measured flow/process durations and runtime resource evidence | Sampling, context propagation and semantic stability matter |
| [S8] OpenLineage | Jobs/runs/datasets and facet extensibility | Data lineage and pipeline metadata | Optional adapter and custom facet namespace |
| [S9] ISO/IEC 27001:2022 | ISMS risk and control governance | SEC/ORG/RISK policy links | Not a certification substitute |
| [S10] NIST SP 800-218 (SSDF v1.1) | Secure software development practices | DevSecOps practices and secure lifecycle control evidence | Not a complete threat model or audit |
| [S11] FOCUS 1.4 (Jun 2026) | Open cost-and-usage normalization | Usage/billing ingestion and invoice reconciliation | Not a project labor/resource-sizing standard |
| [S12] FinOps Framework 2026 | Inform/Optimize/Operate and practice capabilities | FinOps scopes and business-value analytics | Operating framework, not an estimation equation |
| [S13] ISO/IEC 20000-1:2018 | Service management requirements | Service, incident, transition and improvement | Complementary management process |
| [S14] OMG SysML 2.0 | Requirements, model interchange, architecture | Requirements and technical model links | Not replaced by UL-xDFD |
| [S15] OpenAPI 3.2.1 | HTTP API interface description | API contract references from data flow | Other protocols need own contracts |
| [S16] DORA 2026 metric guidance | Five delivery performance metrics | Observed outcome indicators with explicit definitions | No automatic universal performance threshold |
| [S17] Green Software Foundation SCI | Software Carbon Intensity methodology | Optional measured energy/carbon-normalized functional unit | Requires boundary/functional-unit methodology |
| [S18] ISO/IEC 27005:2022 | Information security risk management guidance | Scenario risk method and treatment ownership | No risk likelihood inferred from graph alone |
| [S19] ISO/IEC 42001:2023 | AI management systems | Model governance, accountability, training and monitoring of AI use | Alignment only; no AI management system certification |
| [S20] ISO/IEC 23894:2023 | AI risk management guidance | AI risk method and controlled scenarios | Guidance; risk quantification remains local and evidence dependent |
| [S21] ISO/IEC 42005:2025 | AI system impact assessment | Impact and stakeholder assessment links | Not a claim that an assessment has been performed |
| [S22] NIST AI RMF 1.0 (2023) | Govern/Map/Measure/Manage AI risk | Model risk evidence and continuous review | Voluntary framework, not compliance certification |
| [S23] NIST AI 600-1 (2024) | Generative AI profile | GenAI operational/harm risk and evaluation vocabulary | Complementary profile; no automatic conformance |
| [S24] OWASP GenAI LLM Top 10 (2026) | Generative AI application threats | Injection, disclosure, excessive agency, unbounded consumption reviews | Reference checklists do not constitute a full security audit |
| [S25] OWASP Top 10 for Agentic Applications | Agentic threats and controls | Delegation, tool misuse, identity, memory poisoning and cascading failure | Threat taxonomy not a security certification |
| [S26] Model Context Protocol 2026-07-28 | Tools, resources and prompt interoperability | Protocol-role objects, tool metadata, auth and task scope | Reference exact negotiated protocol version |
| [S27] A2A Protocol 1.0 | Agent-to-agent discovery and task interoperability | Agent-card/task/message mappings with trust and auth boundaries | Optional protocol; exact supported binding must be stated |
| [S28] OpenTelemetry GenAI semantic conventions | Inference/embedding/tool traces and token usage | Measurements, models, call spans, provider-reported token units | Conventions include evolving/development fields; pin library/schema |
| [S29] FinOps Foundation FinOps for AI (2026) | AI scope, value and workload economics | AI costs across model API, GPU, SaaS and data; cost/success | Industry guidance; no universal AI price schedule |
| [S30] FOCUS 1.4 AI service classification | AI and ML billing categorization | AI charge normalization and multi-vendor reconciliation | FOCUS normalizes vendor billing, not individual agent traces |
| [S31] ISO/IEC 22989:2022 | AI terminology and concepts | Typed AI system/actor/model term mapping | Terminology only; not formal conformity claim |
| [S32] ISO/IEC 23053:2022 | Generic ML system framework | Model lifecycle and ML system components mapping | Information resource, not detailed model architecture standard |


## 17.1 Import/export contracts

- BPMN: store external process URI, activity ID, version, correlation and mapping rule; never claim an automatically proven sequence from a DFD.
- DMN: store decision ID, input/output schema and version, owner and error/default branches; do not embed and mutate vendor rules.
- OpenAPI/AsyncAPI: store contract identifiers, endpoints, types, validation, authentication and backward compatibility evidence.
- OpenTelemetry: persist resource/span identity mapping, sampling rate, interval, query, privacy filtering and environment; transport-independent references only.
- OpenLineage: map job/run/dataset facets with schema/version and collision-safe custom prefixes.
- FOCUS: import compatible cost and usage columns with version, currency, billing period, reconciliation basis; identify non-FOCUS project expenses separately.
- PROV-O: map evidence/activity/agent relationships and store content hashes or access-controlled URLs for sensitive source artifacts.
- ISO/IEC references: link the standard reference and a reviewed organizational control/requirement mapping, never copy copyrighted normative clauses wholesale.

## 17.2 AI standards and protocol reference crosswalk


The existing mapping table now includes [S19]–[S32]. The references have been checked against publicly available official materials as of 15 November 2026. They are external sources of terminology, process guidance, formats and risk taxonomies—not automatic certifications or evidence that UL-xDFD is internationally standardized. Versions matter: for example MCP 2026-07-28, A2A 1.0, FOCUS 1.4, ISO/IEC/IEEE 12207:2026 and OWASP LLM Top 10 2026 are explicitly identified.


| Standard / protocol | Direct implementation artifact | Special limitation |
| --- | --- | --- |
| ISO/IEC 42001 / 23894 / 42005 | AIMS controls, risk method, impact assessment reference | Do not reduce organizational compliance to a graph score |
| NIST AI RMF + GenAI profile | GOVERN/MAP/MEASURE/MANAGE mapped to policies/evidence | Risk is application-specific, not determined by model graph topology |
| OWASP LLM + Agentic Top 10 2026 | Threat labels, red-team coverage and action controls | No checklist alone proves security or output truth |
| MCP 2026-07-28 | Tool/resource/prompt protocol role, version, auth and metadata | Protocol role/semantic model differs from DFD data-flow |
| A2A 1.0 | Peer-agent discovery, task/delegation and security context | Do not assume all multiagent systems support A2A |
| OpenTelemetry GenAI | Model, tool and token counters with trace identities | Attributes in development: pin exact implemented conventions |
| FinOps for AI + FOCUS 1.4 | AI scope, cost allocation and billing bridge | Invoice normalization ≠ per-agent token cost trace |
| ISO 12207 and ISO 42010 | AI phases and all 12 coordinated views | Compliance requires checking licensed authoritative texts |


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
