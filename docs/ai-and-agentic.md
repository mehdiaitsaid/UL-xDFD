# Modeling AI and agentic systems

AI-enabled systems have two kinds of movement: information moves between components, and the system may decide to *act*. That difference is important. A retrieved document is data; a function call that changes a reservation is a controlled operation. UL-xDFD represents them separately.

## AI objects

The v1.0 specification adds model identities (`MODEL`), serving endpoints (`MODELSVC`), agents (`AGENT`) and runs (`AGRUN`), orchestrators (`ORCH`), tools (`TOOL`), protocol roles (`MCP`/`A2A`), prompts (`PROMPT`), memory (`CONTEXT`), corpora and chunks (`CORPUS`/`CHUNK`), indexes (`VINDEX`), datasets and evaluations, controls (`SAFE`/`HITL`), accelerators (`GPU`), AI billing (`AICHARGE`) and outcomes (`AIOUT`). The exact definitions are in [Section 5](technical/05-elements-edges-notation.md).

A use-case design should identify the *purpose* of the AI capability, not merely the provider name. The provider can change; the required outcome and trust boundaries remain.

## Agent execution

An agent definition should state available tools, permissions, autonomy level and stop conditions. Each run can record model invocations, tool outcomes, token/time/spend consumption, failures and the result of any human approval. The possible route is not the same thing as an observed trace, and an LLM-generated plan is not an authorization grant.

For a privileged tool action, specify an allow/deny control outside the model, a responsible owner, an audit record, and a rollback or compensating action when necessary. Record the escalation path when the agent is uncertain or fails.

## Retrieval-augmented generation

RAG adds its own evidence chain: corpus origin and usage rights, chunking, embedding model/version, indexing frequency, retrieval strategy, results, and freshness checks. Treat retrieved instructions as untrusted material and do not silently promote them to policy. Storage, re-indexing, embeddings, and retrieval fees belong in the cost model even when the model API is cheap.

## Resource and quality accounting

A robust profile distinguishes billed from estimated tokens and separately accounts for input, output, cached, reasoning, image/audio and any provider-specific units. Self-hosted inference needs GPU/accelerator runtime and idle capacity accounting. Evaluate quality with a defined benchmark, human-review policy, baseline, and uncertainty; a single automated judge is not an unquestioned ground truth.

## Interoperability

[MCP](https://modelcontextprotocol.io/specification/) and [A2A](https://a2a-protocol.org/) have distinct roles. MCP connects applications/agents with tools and contextual resources; A2A supports interoperability among agent systems. A diagram claiming either protocol should record the actual negotiated version and required authentication behavior. [OpenTelemetry GenAI semantics](https://opentelemetry.io/docs/specs/semconv/gen-ai/) can help attach measured inference/agent traces but some conventions are evolving.

The detailed [AI annotation dictionary](technical/07-annotation-dictionary.md), [42 AI validation rules](technical/08-validation-rules.md), and [agent reference example](technical/appendix-e-agent-example.md) complete this guide.

[Back to README](../README.md)
