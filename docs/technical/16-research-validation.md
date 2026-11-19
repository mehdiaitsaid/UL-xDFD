# 16. Academic validation, comparison baselines and threats to validity




## 16.1 Layered evaluation methodology


Separate language correctness from scientific usefulness. Evaluate: (1) syntactic/semantic conformance; (2) independent analyst repeatability; (3) evidence completeness and burden; (4) accuracy of cost/workload estimation relative to held-out telemetry and invoices; (5) usefulness and feasibility of optimization interventions; (6) readiness construct validity and prospective outcome prediction, if longitudinal labels become available. Success in one layer does not prove the next.


| Layer | Benchmark / design | Metrics and comparisons |
| --- | --- | --- |
| Syntax and semantics | Golden positive/negative model fixtures; fuzzed import cases | Detection precision/recall by error class, false positives, reproducibility |
| Modeling quality | Counterbalanced analysts on same case; DFD vs UL-xDFD | Coverage by requirement/phase, agreement, time spent, stakeholder corrections |
| Engineering cost | Several products / architectures / periods, price and invoice hold-out | MAE/WAPE/bias, interval coverage, allocation discrepancy |
| Workload forecasts | Independent test-loads and peak bursts; different platforms | Rate/p95 error, capacity violation frequency, calibration by scenario |
| Optimization | Baseline vs alternatives under identical constraints; controlled rollout | Total cost, SLO/risk violation, effort, Pareto diversity, realized savings |
| Adoption readiness | Survey-only and expert-only baselines vs evidence-based diagrams | Agreement, discriminant validity, decision utility, burden |
| Predictive impact | Temporal and organization-held-out prospective outcomes | External calibration, Brier/log loss, AUC where appropriate, subgroup error |


## 16.2 Research questions and preregistered hypotheses

- RQ1: Does UL-xDFD increase stakeholder/phase/technical requirement coverage versus plain DFD with matched modeling effort?
- RQ2: Does it improve inter-analyst agreement and detection of actionable risks relative to existing architectural and organizational assessments?
- RQ3: Does quantitative propagation yield less biased resource/cloud/project cost estimates than simple per-service extrapolation and expert baselines?
- RQ4: Do UL-xDFD-informed feasible interventions reduce actual CI/CD/cloud cost without harming security, reliability, delivery quality or staff burden?
- RQ5: Which socio-technical attributes have prospective incremental association or predictive power for DevOps/DevSecOps adoption outcomes after controlling for context?
- RQ6: When do additional modeling views cease to justify their time and maintenance burden?

## 16.3 Baselines and ablation studies


Required comparisons include classic DFD alone; the submitted xDFD quantitative model; the submitted E-DFD readiness model; a survey-only maturity assessment; spreadsheet/simple engineering estimates; and UL-xDFD full and selected-view ablations. A useful factorial design adds V2 workflow, V3 organization, V5 quantitative and V9 costs independently, then examines whether each contributes beyond its collection cost. The model must compete against strong and appropriately tuned baselines, including standard commercial FinOps cost tooling where accessible.


## 16.4 Dataset and artifact release policy


Release a benchmark with fictional verified fixtures, anonymized/consented organizational snapshots, timestamped model revisions, independently observed cost and outcomes, scenario data, coding manual and reproducible scripts. For privacy and contracts, share only permitted features/hashes and synthetic reconstructed graphs when necessary. Register site/organization IDs for grouped folds and do not disclose confidential cost records without permission. Plan sample sizes after pilots and account for nested observations (commits/services within organizations).


## 16.5 Threats to validity


| Threat | Mitigation or limitation |
| --- | --- |
| Construct validity | Separate “readiness”, “adoption activity”, “adoption success” and unrelated performance; instrument validation |
| Measurement bias | Independent evidence, preregistered sampling, telemetry definitions and review |
| Selection bias | Recruit failures/abandoned implementations, different organizations, private/public cloud sizes |
| Temporal leakage | Freeze baseline; prohibit future outcomes and post-change artifacts in prediction features |
| Overfitting/collinearity | Group splits, transparent models, regularization, nested CV and external tests |
| Confounding and causality | Adjustment for sector/team/size/tool adoption, difference-in-differences/controlled designs where feasible |
| External validity | Multiple industries, regulated environments, architectures, heterogeneous platforms |
| Intervention side effects | Track reliability/security/latency/employee burden alongside cost |
| Missing not at random | Unknown category and missingness analysis; sensitivity bounds |
| Model maintenance cost | Track hours to collect/validate/update; report marginal benefit per view |


## 16.6 Novelty claims and publication discipline


“Extended DFD” as a concept is not new. Prior security-enhanced DFDs and architecture description approaches already exist, as recognized in [I2]. A defensible contribution must be demonstrated, not asserted: a full-lifecycle annotation and formal validation language with cross-view traceability, quantitative cost inputs, socio-technical adoption evidence and prospective evaluation. Claim distinct contributions for metamodel, tooling, case studies and prediction; do not present a specification as proof of validated accuracy. A systematic literature review should be performed before a novelty claim in an academic paper.


## 16.7 Dedicated AI research evaluation and reproducibility protocol


Four complementary evaluation targets: (i) semantic correctness/coverage of AI graphs, (ii) AI workload/token/GPU/cost forecast accuracy, (iii) task-quality and agent-security diagnostic validity, and (iv) downstream decision quality of optimization and adoption advice. Performance on one target is not evidence of another.


| Research question | Design / baseline | Required evidence and metrics |
| --- | --- | --- |
| RQ-A1: Does AI graph extension improve completeness? | Same systems modeled by classical DFD, UL-xDFD v0.1 and AI profile in counterbalanced order | Recall/precision of components, agent side effects, security handoffs, modeler hours, agreement |
| RQ-A2: Can usage/AI cost be predicted? | Held-out periods/sites; provider invoice and OTel token/GPU measurements | WAPE/MAE/bias, predictive interval coverage, per-use-case reconciliation error |
| RQ-A3: Are agent risk diagnostics meaningful? | Controlled safe/unsafe agent fixtures with known behavior and independent red team | Precision/recall by rule class, severity agreement, false assurance rate |
| RQ-A4: Are AI recommendations beneficial? | Shadow-mode optimization then controlled rollout versus conservative baseline | Cost per accepted task, p95 task time, intervention quality, safety incident bounds |
| RQ-A5: Can AI adoption readiness be forecast? | Preregistered t0 scores and prospective external outcomes across organizations | Calibration, discrimination, subgroup stability, missingness, external validity |
| RQ-A6: Is the extension worth modeling effort? | Compare minimal/core/AI layers at fixed analyst time budgets | Coverage gain vs extra evidence minutes, maintainability and stakeholder decision utility |


Stratify by traditional ML vs GenAI vs agents, hosted API vs self-hosted, small vs large organizations, regulated vs unregulated tasks, and observed data sufficiency. All held-out test sets and measurement protocols must be frozen before tuning. Synthetic examples can test a validator but cannot establish cost-prediction accuracy or psychometric validity.


Threats: provider usage opacity; model version churn; hidden prompts; judge bias; harmful output under-observation; selection on successful agent runs; missing invoices; clustering by team/provider; leakage from post-adoption artifacts; and undocumented side effects. Report missingness, confidence bounds and adverse-case sensitivity tests.


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
