# Standards, protocols, and references

UL-xDFD builds on several established bodies of work. The mapping here tells implementers **what each source contributes** and **what it does not prove**. A reference in the model is not evidence that an organization complies with the source's standard.

This map was reviewed against official public sources on **16 November 2026**. Protocol versions and working conventions can change. Always record the exact version used in an implementation.

| Source | Why it matters to UL-xDFD | Important boundary |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) | Coverage of software lifecycle processes from conception to retirement | Our twelve lifecycle phases are a proposal, **not** reproduced normative ISO stages. |
| [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) | Architecture concerns and multiple coordinated viewpoints | Alignment does not certify conformance with an architecture description standard. |
| [OMG BPMN](https://www.omg.org/spec/BPMN/) and [DMN](https://www.omg.org/spec/DMN/) | Workflows, gates, and decision logic | DFD arrows must never be interpreted automatically as workflow sequence. |
| [ISO/IEC 25010](https://www.iso.org/standard/78176.html) | Product quality characteristics | Verification requires explicit tests and metrics. |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | Evidence entities, activities, agents and provenance links | Interoperability requires an implemented mapping. |
| [OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | Runtime traces, token usage and agent/inference spans | Some generative-AI conventions are still under development; pin versions. |
| [OpenLineage](https://openlineage.io/docs/spec/) | Run/job/dataset lineage, extensible facets | Does not replace all application data flow or financial attribution. |
| [FinOps Framework](https://www.finops.org/framework/) | Business-value and technology-cost management practices | Operating framework, not a universal prediction equation. |
| [FOCUS 1.4](https://focus.finops.org/what-is-focus/) | Common cost/usage and billing reconciliation definitions | Does not identify every agent run or model-specific pricing meter. |
| [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure software-development evidence | A profile mapping is not a security certification. |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | AI risks, evaluation, governance and GenAI-specific risks | Framework adoption and risk status must be assessed with contextual evidence. |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | Organizational AI management system requirements | No ISO certification is implied. |
| [Model Context Protocol](https://modelcontextprotocol.io/specification/) | Client/server/tool/resource/prompt interface roles | Pin protocol revision and actual auth configuration. |
| [Agent2Agent (A2A)](https://a2a-protocol.org/v1.0.0/) | Communication between agent applications | Optional, not a synonym for all multi-agent interactions. |
| [OWASP GenAI Security](https://genai.owasp.org/) | LLM/agentic threat categories and security review | Threat lists do not prove the system is safe. |
| [DORA](https://dora.dev/) | Delivery performance metrics and human-centered research context | Metrics need controlled definitions and cannot be inferred from diagram density. |

The original v1.0 [standards crosswalk](technical/17-standards-crosswalk.md) contains additional mappings, including SysML, carbon accounting, service management, ISO risk guidance, and agent/data lifecycle concepts. It also retains its original source-version claims for auditability; when its cited version differs from a subsequently published protocol, prefer the authoritative current specification and record the actual revision used.

## Research provenance

The unified model builds on two earlier team specifications:

1. **xDFD v0.9** — quantitative data flow, workloads, resources, storage, network and technology cost (8 November 2026).
2. **E-DFD v0.1** — evidence-based DevOps readiness, workflow timing, stakeholders and longitudinal research design (15 November 2026).

The second-stage **UL-xDFD v1.0** merged the common model and added the AI and agentic profile. The source Word document is retained in [`source/`](../source/UL-xDFD-v1.0-source-specification.docx) for provenance. The [origin/compatibility section](technical/02-origins-and-compatibility.md) explains which concepts were inherited and where mappings are not automatic.

## External reference use

Some ISO and other normative standards are licensed texts. This repository **links to** their official descriptions rather than reproducing their full normative contents. In any publication, cite the authoritative source for borrowed terminology and cite UL-xDFD separately for the proposed metamodel, field names, and validation catalog.

[Back to README](../README.md)
