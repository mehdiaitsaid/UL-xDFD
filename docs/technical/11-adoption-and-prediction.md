# 11. Adoption-readiness diagnostic and prediction



## 11.1 Readiness assessment is not project success prediction


Readiness is an evidence-backed capability and constraint profile for a named value stream, adoption target and baseline date. A software organization can have an elegant DFD and poor operational collaboration—or a complex architecture and excellent DevSecOps routines. Therefore graph size, process count, microservice count, edge density and cloud cost are not valid readiness proxies without tested context and predictive evidence. The model returns domain-specific findings, missing evidence, critical policy gates, feasible interventions and the uncertainty of each finding.


## 11.2 Candidate diagnostic dimensions


| Dimension | Concrete evidence | Illustrative critical gate |
| --- | --- | --- |
| Leadership and strategy | Sponsor, adoption objective, funds, decision rights, support policy | No accountable adoption sponsor for critical scope |
| Culture and teams | Anonymous team survey coverage, handoffs, learning practices, cross-role agreement | Sensitive cultural inferences from insufficient respondent groups prohibited |
| Architecture and dependency | Versioned service maps, release-coupling evidence, contracts and ownership | Critical unowned third-party dependency |
| Build, tests and delivery | Pipeline logs, artifact provenance, automated tests, change governance | Release cannot be rolled back and no mitigation owner |
| Security and privacy | Threat model, hard-gate scan policy, secrets controls, risk acceptance | Known critical secrets exposure without approved mitigation |
| Operations / reliability | SLIs, on-call, runbooks, backup and tested restore | No recovery plan for critical data |
| FinOps and cost visibility | Owner mapping, allocation coverage, billing evidence, budgets | No traceable cost owner on material critical service |
| Skills and vendor constraints | Role capacity, competency evidence, acquisition/legal restrictions | Required expertise unavailable for planned rollout |


A pilot scoring rubric may use descriptive ordinal levels (“not evidenced”, “emerging”, “repeatable”, “controlled”), but must publish its operational definitions and inter-rater agreement. Missing data is an explicit unknown state, not automatically “not ready.” An optional weighted diagnostic score is experimental until construct and cross-context validation is complete; it is never presented as a calibrated likelihood of successful adoption.


## 11.3 Decision-gate algorithm


INPUT: baseline_snapshot, adoption_target, scope, domain_rules, evidence_registry


1. validate structural + evidence quality, collect unknown/disputed flags


2. identify required gate evidence and blocked policy constraints


3. for each domain: extract verified facts and typed reports separately


4. apply transparent contextual diagnostics with explicit counterexamples


5. produce reasoned findings and evidence paths; do not infer culture from topology


6. recommend costed feasibility-ranked actions with owners and due dates


7. run missing-evidence and subjective-weight sensitivity analyses


8. output diagnostic_profile; predicted_success_probability: null


OUTPUT: auditable gaps, evidence coverage, policy gates and intervention candidates


## 11.4 Prospective predictive research pathway


To support eventual probabilities, freeze t0 snapshots before the intervention, pre-register success outcomes and horizons, measure outcomes at t0+h from independent sources, separate organizations when splitting train/validation/test, and check confounders (size, sector, maturity, investment, regulation, platform and change selection). Begin with transparent baseline regressions or ordinal models before complex graph learning; compare to surveys and context-only baselines and perform feature ablations. Evaluate external calibration, discrimination, group-level error, confidence intervals, missingness sensitivity and temporal transportability. This is a research program, not an implemented or validated classifier in UL-xDFD v0.1.


## 11.5 DORA and human-centered metrics


Use DORA’s five software delivery measures as independent operational indicators where suitable: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate [S16]. Preserve historical metric versions and measurement definitions; do not assume every team or industry has the same optimal deployment cadence. Human-centered constructs should rely on a defensible instrument and aggregation protocol; do not treat telemetry as a replacement for direct human evidence.


## 11.6 Readiness to adopt AI, MLOps, LLMOps and AgentOps


AI adoption readiness is a distinct but interoperable assessment: reliable data and documentation, model selection and evaluation capacity, AI governance and legal/privacy readiness, compute/provider procurement, training/release capability, incident response, user oversight and staff skills. A team may have mature DevOps CI/CD while lacking AI evaluation or authority controls; the reverse can also occur. Do not collapse readiness into an unvalidated universal score.


| Readiness dimension | Evidence and indicators | Critical gate / residual limitation |
| --- | --- | --- |
| Business fit | Task/value definition; AI vs deterministic baseline; user acceptance | No ethical justification or measured business value |
| Data and knowledge | Data licensing, privacy, source quality, RAG freshness | Sensitive data processing without approved basis |
| AI/ML engineering | Model/experiment registry, benchmarks, prompt/version control | No reproducible model/prompt acceptance process |
| AI secure delivery | Model supply chain, eval/release gates, rollback, secrets | Uncontrolled model or tool promotion |
| AgentOps authority | Tool allowlist, approvals, delegation control, circuit breaker | Unrestricted high-impact tool authority |
| FinOps and platform | Token/GPU cost ownership, metering, quotas, business unit | No accountable cost owner or spend cap |
| Organization and people | Training, human oversight, affected-stakeholder consultation | Insufficient evidence; surveys must preserve privacy |
| Monitoring and risk | Quality drift, red team, incident/appeal, provider change | No ability to detect/regress high-severity harm |


The framework should emit domain-level evidence strength, readiness barriers, scope-dependent critical gates and the next evidence-collection steps. If enough future outcomes are captured, AI-specific predictor training can be attempted with site/time splits, frozen t0 snapshots and independent prospective holdout; without this, the deliverable is a diagnosis, not an adoption-success probability.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
