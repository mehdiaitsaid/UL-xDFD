# 15. Worked end-to-end case study: hotel and event reservation



The following is a deliberately synthetic, non-empirical example. It demonstrates how one value stream can connect an initial customer goal to a DFD, architecture, CI/CD, physical resource usage, cloud cost and an adoption diagnosis. It is not a measured business or a benchmark dataset. Source categories and scenarios are illustrative and should be replaced by organization-approved artifacts and observations.


## 15.1 Boundary, business intent and logical flow


System boundary: online reservation product, production environment. Value unit: a successfully completed booking with a persisted booking ID. Actors: customer X1 and external payment provider X2. P1 receives booking requests; P2 validates and persists the reservation in S1; P2 optionally requests payment from X2; P3 sends a confirmation. Customer requests and notifications are separate flows. The stateful business workflow is not assumed to follow from the order of arrows alone.


X1 Customer       --F1 booking request--> P1 Booking API


P1 Booking API    --F2 validated request-> P2 Reservation Service


P2 Reservation    --F3 persist booking---> S1 Booking DB


P2 Reservation    --F4 payment request---> X2 Payment Provider


P2 Reservation    --F5 notification-----> P3 Notification Service


P3 Notification   --F6 confirmation----> X1 Customer


EV1 Validate  --WORK--> G1 Payment decision --WORK--> EV2 Persist


ROLE Product Owner --OWN accountable_for--> REQ-availability


PIPE1 CI/CD  --DEL deploys--> DEP1 Booking deployment


DEP1 --HOST hosted_on--> RES1 Cloud compute


BILL1 --COST allocates_to--> CC1 Reservations Product


## 15.2 Scenario assumptions and decision questions


| Input | SC-normal | SC-peak | Interpretation |
| --- | --- | --- | --- |
| Incoming traffic | 250 requests/s | 500 requests/s | Synthetic sustained short-window stress load, not monthly average |
| Payload request | 12,288 B mean | 12,288 B mean | Request body only; one direction |
| Process CPU demand | 0.015 core-s/request | 0.015 core-s/request | Assumed measured-class quantity but hypothetical in this example |
| Utilization target | 0.65 | 0.65 | Engineering planning target, not a universal SLO |
| Replica class | 2 vCPU each | 2 vCPU each | Perfectly equivalent replicas assumed for arithmetic |
| Wire factor / link target | 1.15 / 0.70 | 1.15 / 0.70 | Declared overhead and target link utilization |
| DB operations | 1.8/request | 1.8/request | Mean includes business writes and query checks |
| Annual baseline costs | Not modeled here | Not modeled here | Monthly illustrative scenario costs shown separately |


## 15.3 Derived capacity, routing and unit economics


Process CPU demand: normal = 250 × 0.015 = 3.75 core-equivalents; at 65% target provision ≈ 5.77 vCPU, rounded to 6 vCPU (3 × 2-vCPU replicas). Peak = 7.5 core-equivalents, provision ≈ 11.54 vCPU, rounded to 12 vCPU (6 × 2-vCPU replicas). This is a compute-only estimate: failures, synchronization, overhead and uneven traffic may require more.


One-direction request-wire link planning: normal ≈ 40.37 Mbit/s; peak ≈ 80.75 Mbit/s, including the illustrative wire factor and link utilization policy. Responses and payment/notification traffic require separate flow records and must not be invisibly absorbed into F1. Storage operations: normal 250 × 1.8 = 450 operations/s; peak = 900 operations/s before caching, failed attempts or replica write amplification.


| Cost category | Assumption | Synthetic monthly USD |
| --- | --- | --- |
| Compute | 6 vCPU × $0.04 × 720 h | 172.80 |
| Managed database | $0.12/h × 720 h | 86.40 |
| Storage | 120 GiB × $0.10/GiB-month | 12.00 |
| Egress | 500 GiB × $0.08/GiB | 40.00 |
| CI/CD | 1,500 runner-minutes × $0.01/minute | 15.00 |
| Observability | 25 GiB × $0.50/GiB | 12.50 |
| Shared platform | Explicitly allocated illustrative monthly share | 30.00 |
| Total | Selected illustrative cash-like charges only | 368.70 |


At 50,000 successfully completed bookings/month (a separately defined hypothetical value count), attributable runtime-plus-pipeline spend is $368.70/50,000 × 1,000 ≈ $7.37 per 1,000 completed bookings. This does not include project labor, taxes, all networking, backup, full vendor support, financing, nonproduction spend or reserve commitments. It is not a production forecast or real provider price quote. The 250 request/s capacity test is a short window and must not be multiplied by 720 hours as if sustained throughout the billing month.


## 15.4 Cross-view trace and a proposed optimization


| Trace hop | Example object | Verifiable research question |
| --- | --- | --- |
| Value → requirement | VAL1 completed booking → REQ1 p95 latency | Can the business unit and SLO be defined consistently? |
| Requirement → DFD | REQ1 → P1, P2, F1, F2 | Is the customer journey mapped to the relevant transformations? |
| DFD → code/pipeline | P2 → APP1/REPO1 → PIPE1 | Is a release testable and reproducible? |
| Pipeline → deployment | PIPE1 deploys DEP1, hosted on RES1 | What resources and approvals are required? |
| Runtime → charge | RES1 incurred BILL1, allocated to CC1 | Can resource costs be attributed without duplicates? |
| Change → observed outcome | CHG1 changes cache; OUT1 later validates | Were response time, spend and incident exposure actually improved? |


Optimization hypothesis: change cache placement to reduce repeat database reads. The model must first split DB reads from writes, define which reads are cacheable, collect hit-rate evidence, quantify cache CPU/memory/egress and invalidation errors, and preserve payment/security correctness. It cannot claim a 50% database saving solely because traffic decreases on one DFD edge.


## 15.5 Adoption-readiness example with unknown evidence


| Proposed finding | Evidence state | Responsible next action |
| --- | --- | --- |
| Releases require a manual gate with unmeasured wait time | unknown | Gather workflow logs and approval timestamps |
| Production backup and rollback controls are documented | reported | Run restore and rollback exercises; attach artifacts |
| CI/CD has a functioning pipeline for P2 | hypothetical | Verify via repository job logs and provenance |
| Team trust/psychological safety | unknown | Use voluntary anonymous instrument; suppress small subgroups |
| Most production charges are allocated to a product owner | estimated | Reconcile FOCUS/invoice quantities and allocation weights |


Diagnostic conclusion for this fictional case: assessment incomplete for a verified readiness claim; the correct action is to obtain missing evidence, not to generate a fake numerical readiness probability. A later prospective intervention can assess whether reducing approval wait and standardizing secure deployment changes independent delivery outcomes.


## 15.6 Example validation failures

- F1 rate missing its SC-normal reference would trigger a scenario-scope warning/error.
- A direct S1→X2 DATA edge would fail an allowed-endpoint rule unless modeled through an explicit process.
- An observed CPU-demand record without a dated benchmark source would fail provenance validation.
- BILL1 allocated 0.7 to two products and another 0.5 to a third would be rejected because the shared weights exceed 1.
- Calling an estimated readiness ordinal a “92% probability of successful DevOps adoption” would violate the predictive-boundary policy.

## 15.7 AI-assisted booking and agent tool flow — synthetic end-to-end extension


Use case: a customer asks the hotel reservation assistant whether a selected hotel is refundable and asks it to reserve a room. The workflow calls a model and optionally retrieves booking policy from a controlled RAG index. Read-only availability checks can be automatic; a booking or payment change requires a separate identity and policy gate. This extends, rather than replaces, the earlier hotel case study. All prices, percentages and token counts below are intentionally fictional and must not be used as vendor quotations.


| Element | Illustrative ID and property | Evidence / modeling purpose |
| --- | --- | --- |
| Business unit | AISYS1: validated AI-assisted booking or safe escalation | Outcome denominator and acceptance criteria |
| Agent | AGENT1: booking assistant, max 5 steps, $0.02/run token budget | Explicit policy and finite loop |
| Model and endpoint | MODEL1: fictional LLM-v7; MODELSVC1: hosted service | Traceable model selection and token cost |
| Knowledge | CORPUS1: refund policy; VINDEX1: refreshed daily | Approved retrieval source and stale-document risk |
| Tool 1 | TOOL1: search availability, read-only | Independent scope and API/query cost |
| Tool 2 | TOOL2: create booking, stateful and approval required | Authority and compensating transaction |
| Human gate | HITL1: confirm paid booking | Approval wait and labor cost |
| Evaluation | EVAL1: intent accuracy, supported citations and successful booking | Model behavior vs actual outcome |
| AI meter | AICHARGE1: separate input, output, retrieval and tool cost | Invoice reconciliation, no double billing |
| Outcome | AIOUT1: booked / escalated / rejected / failed | Count all attempts; report success definition |


Hypothetical monthly baseline: 50,000 incoming customer sessions; 70% use AI (35,000 AI-supported sessions); 1.4 billable model invocations per AI-supported session (49,000 calls); mean 1,500 billed input tokens/call and 350 output tokens/call. Synthetic rates of USD 0.50 per 1M input tokens and USD 2.00 per 1M output tokens are for arithmetic demonstration ONLY and intentionally do not represent any actual provider contract.


| Metric | Expression | Synthetic result |
| --- | --- | --- |
| AI-supported sessions | 50,000 × 0.70 | 35,000 sessions/month |
| Model invocations | 35,000 × 1.4 | 49,000 calls/month |
| Input billed tokens | 49,000 × 1,500 | 73,500,000 tokens/month |
| Output billed tokens | 49,000 × 350 | 17,150,000 tokens/month |
| Input charges | 73.5M / 1M × $0.50 | $36.75 |
| Output charges | 17.15M / 1M × $2.00 | $34.30 |
| Retrieval cost | 35,000 query equivalents × $0.0003 | $10.50 |
| Embedding-refresh cost | 5M tokens × $0.10 per 1M | $0.50 |
| Other AI platform cost | Synthetic index + observability period charge | $25.00 |
| Illustrative monthly AI incremental cost | Sum direct items; no duplicated provider GPU | $107.05 |
| Validated AI-supported successful outcomes | Independent hypothetical adjudication | 30,000 accepted successes |
| Illustrative AI incremental cost / accepted success | $107.05 / 30,000 | $0.00357 per success |


Scenario sensitivity: if average calls per AI-supported session increase from 1.4 to 2.4 with all other quantities held fixed, direct inference spend multiplies by 2.4/1.4 ≈ 1.71, while retrieval/fixed costs need not. Token cost must still be recalculated if longer loops inflate prompt context. For an actual prediction, use observed distributions and quality-conditioned branching rather than this deterministic average.


Quality/cost interpretation: the synthetic cost-per-success denominator uses 30,000 verified successful AI-supported sessions; it is not a causal gain over a non-AI baseline. If the same bookings would happen without AI, the incremental business value may be zero or negative even when token spend is low. Security, human approval labor, development, taxes and broader platform costs were excluded from the narrow numerical example and must be included or clearly disclosed in a fully loaded model.


## 15.8 Failure cases to test in the synthetic agent graph

- A retrieved refund-policy document contains an instruction to transfer customer data to an external URL. Treat it as untrusted DATA; policy denies tool invocation and a security evidence record is created.
- Model repeatedly retries availability checks until its max steps/time/token budget is reached; a verified circuit breaker stops the run and reports failed/escalated status.
- A tool response is delivered but the booking API fails after payment preauthorization; compensation and exactly-once/idempotency semantics are tested before marking success.
- A provider response has no token-usage metadata; the estimate is flagged, and invoice reconciliation remains pending rather than fabricating an observed token count.
- A prompt or model version changes; rerun EVAL1 and security gates, record artifact lineage and keep pre-change and post-change outcome windows separate.

---

[Documentation home](../../README.md) · [Technical reference index](README.md)
