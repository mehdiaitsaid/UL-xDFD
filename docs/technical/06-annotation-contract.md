# 6. Universal annotation contract


## 6.1 Record structure and status classification


All numerical, policy, readiness and decision-relevant assertions are annotations, not untyped notes. A record MUST include an ID, target, namespaced property, value or explicit missingness, datatype, unit if dimensional, scope, provenance kind/status, creation/review date and schema version. Estimated values SHOULD carry interval/distribution and method; telemetry SHOULD carry sample/window and query. “MUST” in this section denotes UL-xDFD rules, not an external standards clause.


| Field | Type / obligation | Rationale |
| --- | --- | --- |
| id / target_id | string; required | Persistent annotation and referenced element |
| key | namespace.property; required | Stable semantic dictionary and type |
| value / null | scalar/object/distribution; required (null for unknown) | Stores meaning without conflating absence and zero |
| datatype / unit | declared type; UCUM or declared unit for numeric | Enables dimensional validation |
| scope | scenario, phase, environment, time period, per-unit scope | Prevents invalid averaging/aggregation |
| status | observed/reported/estimated/derived/hypothetical/unknown/disputed/expired | Controls evidence eligibility |
| source_kind | telemetry/artifact/financial_record/survey/interview/estimate/simulation/derived | Input-origin categorization |
| evidence_refs | nonempty for observed; optional otherwise | Source tracking and audit |
| observed_at / valid_until | ISO datetime / window; one required | Temporal freshness and validity |
| method_ref / assumptions | link + formula/model/measurement protocol | Reproducible derivation |
| uncertainty | min/max, quantiles, sample N, calibrated CI or interval | Uncertainty with proper interpretation |
| review | role, status, date, comment | Stakeholder check and dispute trail |
| privacy_class | public/internal/restricted/secret-reference | Minimum necessary dissemination |
| rule_version | version string when derived | Exact deterministic transformation |


## 6.2 Value status and evidence strength


| Status | Meaning | Permitted use |
| --- | --- | --- |
| observed | Dated artifact, telemetry or ledger; reproducible source | Descriptive fact about observed window, with measurement limitations |
| reported | Survey or interview statement with sampled population | Stakeholder perception; not automatically objective capability |
| estimated | Engineering judgment or statistical estimate | Scenario and forecast; disclose model and uncertainty |
| derived | Computed from identified input records | Retain dependency DAG and deterministic rule version |
| hypothetical | Synthetic example/test fixture | Never present as evidence about a real organization |
| unknown | Collection attempted but unavailable | Coverage gap, not score 0 |
| disputed | Contradictory evidence or interpretations | Hold downstream high-stakes decisions until resolved |
| expired | Outside freshness threshold | Flag/retest; never silently accepted as current |


Evidence grades A (multiple independently corroborated objective records), B (single verified objective record or well-corroborated multi-role testimony), C (single report/estimate) and U (unknown) are provisional operational labels. They are not calibrated probabilities and must never be described as a validated scientific confidence scale.


## 6.3 Inheritance and precedence


An annotation applies only to its declared scope. Inheritance resolution order for matching properties is: element+scenario+environment+window → element+scenario → element+environment → element → containing boundary → explicitly declared organization defaults. The most specific compatible scope wins; equal-specificity conflicts are “disputed”, never arbitrarily chosen. Security classification uses a dedicated conservative propagation rule rather than this general precedence; overridden controls require approval. Each calculated output records the exact resolved source IDs.


## 6.4 Minimal normative example

The record below is an illustrative estimate from the source proposal. It is not a measured value from the sample application and is not a complete model file.

```yaml
id: AN-014
target_id: P2
key: compute.cpu_demand
value: 0.015
datatype: number
unit: core_second/request
scope:
  scenario_id: SC-normal
  phase_id: L09
  environment: production
  window: '2026-10'
status: estimated
source_kind: benchmark
evidence_refs: [EVID-12]
observed_at: '2026-10-31'
uncertainty:
  min: 0.011
  max: 0.020
  kind: engineering_range
```

## 6.5 Provenance, privacy and time rules

- Observed annotations MUST include a source ID and collection date; source references may be hashed, access-controlled URIs rather than copies of confidential data.
- All intervals have interval type (prediction interval, confidence interval, expert range, measurement percentile) and coverage interpretation; do not label an expert range a 95% CI.
- Costs MUST include currency ISO 4217 code, cost basis, rate-card/contract date and timezone/period; explicitly distinguish invoice actuals from modeled cost.
- Culture survey output is kept aggregated with agreed privacy thresholds and opt-out. Individual names, raw salary, identities, secrets and payload contents should not be stored in the graph.
- Derived calculations MUST record the dependency set and the software/model version; changes to a source invalidate or mark stale downstream derived values.
- An annotation applies at specified granularity: PER_REQUEST, PER_MESSAGE, PER_REPLICA, AGGREGATE, PER_MONTH, PER_PIPELINE_RUN, PER_PROJECT, etc.

## 6.6 AI annotation record requirements and quality semantics


The original universal annotation contract applies unchanged to all AI namespaces. Every numeric token, throughput, latency, cost or accuracy value MUST identify a unit, scenario, phase, observation window, model/prompt version where applicable, value status, source/evidence and population denominator. Values from a synthetic workload must be labeled hypothetical; source-kind telemetry without a real source does not transform assumptions into observations.


id: AI-ANN-018


target_id: MODELSVC1


key: aiinf.input_tokens_billed


value: {distribution: empirical, mean: 1650, p95: 4012}


datatype: object


unit: token/invocation


scope: {scenario_id: booking_assist, phase_id: L09, environment: production,


window: '2026-10', granularity: per_model_invocation}


status: observed


source_kind: telemetry


evidence_refs: [EVID-provider-usage-018]


observed_at: '2026-11-01'


uncertainty: {sampling: complete_billed_records, failed_calls_included: true}


review: {owner_role: ai_platform_owner, decision: approved, protocol: usage-v1}


Every generation/token metric distinguishes model-consumed from provider-billed counts if both are available. The quoted OpenTelemetry GenAI conventions themselves remain subject to versioning and some development-status schema changes. Where measurements are unavailable, encode unknown/estimated and preserve a risk-adjusted cost interval; never assign zero consumption by default.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
