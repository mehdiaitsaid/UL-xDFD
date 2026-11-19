# 9. Quantitative analysis and scenario propagation




## 9.1 Workload and transformation semantics


An inbound business event may create zero, one or multiple downstream data actions. The output-rate model captures filtering, fan-out, retries, caching, batching, aggregation and conditional branches as independent, scenario-scoped operators. An example dependency matrix B may describe expected internal calls per upstream event. For a linear stationary model with exogenous arrival vector b and spectral radius(B) < 1, expected demand is λ = (I − B)^−1 b. This is not a universal theorem for arbitrary timed, stateful or nonlinear applications; when stability or independence assumptions fail, replace with trace-driven simulation, queueing analysis or bounded conservative scenarios.


| Operator | Illustrative relation | Necessary caution |
| --- | --- | --- |
| Pass / filter | λout = λin × p_pass | Document what is dropped and where |
| Fan-out | λout = λin × E[calls/event] | Routes may be conditional/correlated |
| Cache read | λDB_cacheable = λcacheable × (1−hit_rate) | Non-cacheable calls not reduced |
| Retry | λtotal ≈ λbase × E[attempts] | Capped attempts and failure correlation needed |
| Batch | λmessages ≈ λrecords / E[batch_size] | Remainders, flush windows and latency matter |
| Compression | bytes_out ≈ bytes_in × ratio | CPU/network trade-off, measured ratio |
| Replication | write traffic × replica count (where applicable) | Sync/async and billing treatment vary |
| Aggregation | rate/bytes depend on window and group key | No universal cardinality conservation |


## 9.2 Resource-sizing equations, interpretation and limitations


Compute demand. D_CPU (core-equivalents) = Σ_i λ_i [requests/s] × dCPU_i [core-seconds/request]. Provisioned vCPU ≈ D_CPU / u_target, adjusted for per-vCPU measured performance, autoscaling minima, bin packing, failure headroom, throttling, platform sharing and burst constraints. CPU clock speed/IPC alone do not provide reliable cross-application CPU demand.


Concurrency. For stable flow under Little’s Law, L = λW. W is mean system time for the same customer population and process boundary; it is not a direct estimate of concurrent resident memory without a validated allocation model.


Memory. M_replica ≈ M_base + (L_per_replica × ΔM_active) + M_cache + M_runtime + M_buffer; add specified operational margin and account for garbage collection, shared objects, queues and peak tail concurrency.


Network. B_payload = 8 × Σ_f λ_f × E[payload_bytes_f] bit/s; B_provisioned = B_payload × k_wire / u_network for the link/path assumed. Price egress by provider-specific metering and direction, not by the same throughput formula alone.


Storage. S_physical ≈ ingest_rate × retained_window × physical-to-logical_ratio × replica_factor × index_factor + snapshots + logs + backups. Read/write IOPS, tier migrations and storage growth are separate constraints.


Queue stability. A stationary single queue needs mean arrival intensity below effective service capacity, but finite-buffer loss, burstiness, service-time tails, synchronization and autoscaler delay require more than an average ratio.


Latency. End-to-end latency is computed from correlated stage samples, critical-path timing or a validated queue/simulation model. Adding individual p95 values is generally not the end-to-end p95; parallel join semantics materially change the result.


Reliability. A = 1 − unavailable_time/measurement_window. Products for series components or 1−(1−A)^n for redundancy are idealized and rely on independence and nearly perfect failover; common-cause and provider failures must be examined.


Demand growth. Use empirical seasonality, cohort conversion, seasonal spikes, controlled product launches or bounded scenarios. A constant compound-growth extrapolation is only a simplified assumption, not an authoritative forecast.


Uncertainty. Propagate input distributions by Monte Carlo or scenario envelopes where feasible; report percentile/coverage correctly and identify strongly correlated input drivers. A safety buffer is an explicit choice, not an inferred truth.


## 9.3 Multi-scenario requirements


At minimum define SC-baseline, SC-peak, SC-failure and SC-growth. A research implementation SHOULD also include cold-start, CI/CD burst, data reprocessing/migration, security incident and disaster recovery where relevant. Scenario comparisons use exactly the same business-value denominators and declare changed factors. A design in private cloud additionally needs server utilization, energy metering, amortization, depreciation and shared-node allocation assumptions.


## 9.4 Model checking for quantitative inconsistencies

- Check conserved data identities separately from byte conservation: compression, aggregation and duplication invalidate naive byte equality.
- Detect loops without bounded retry logic, negative rates, frequencies with missing time units, and impossible replicas/scaling quotas.
- Distinguish requests/s from completed business units/month; a customer journey may generate dozens of requests but one order.
- Audit cost model quantities against deployment plan and tags; no resource or reserved capacity should be counted twice.
- Mark forecasts provisional when estimates lack representative workload tests or when provider rate cards are outdated.
- Retain the explicit transformation of raw metrics and the horizon over which extrapolation is performed.

## 9.5 AI workload, agent-loop and RAG propagation


AI invocation is a demand-transforming workload operator. Inference demand depends on routed use cases, branch probabilities, retries, fallback decisions, context growth, dynamic tool use and model-specific tokenization. Traditional requests/s to CPU or bytes/s alone are insufficient for GenAI capacity and price estimation.


| Quantity | Proposed equation / semantics | Validity condition |
| --- | --- | --- |
| Expected model calls | E[Nmodel \| session] = Σbranch P(branch \| scenario) × E[calls \| branch] | Condition on user mix; count retries and agent loops once |
| Model call rate | λmodel = λsessions × E[Nmodel \| session] | Use only when long-run expected demand is stationary over selected window |
| Billed input tokens | B_in = Σcalls (input_total − input_cached − discounted_other) by rate class | Never subtract cache unless provider confirms billed distinctions |
| Agent token amplification | A_tok = (Σ input+output tokens across invoked models)/(baseline single-call token count) | Define baseline and include unsuccessful tasks |
| RAG retrieval load | λretrieval = λsessions × P(RAG used) × E[queries \| RAG session] | Measure correlated queries and re-ranking separately |
| Embedding volume | T_embed = Σ new/changed chunks × tokens_per_chunk; vectors = chunks × versions | Avoid assuming one chunk corresponds to one source document |
| GPU occupancy | GPU_hours_allocated = Σ device count × reserved wall-hours | Allocated ≠ utilized; disclose useful work and idle allocation |
| Queue stability | ρ = λ × E[device service time] / available service capacity | No direct mapping from vCPU to LLM TPS without benchmark |
| Task completion | successes = sessions × P(accepted successful outcome \| scenario) | Quality denominator independent of number of model outputs |


For mixed model tiers m, the expected number of billable invocations is Σ_s N_sessions,s Σ_m P(m | s)E[calls_m | s]; call probabilities and token distributions can be correlated. Monte Carlo or discrete-event simulation can propagate branches, token length, rate limits, timeouts and human approval waits using audited assumptions. Percentiles must be simulated or measured; p95 of each step cannot be added to claim a path p95.


Training/fine-tune scenarios must declare epochs, effective dataset tokens, gradient accumulation, accelerator count, measured throughput, checkpoint frequency, storage/network I/O, evaluation repeat count and failures. Hardware sizing from nominal FLOPs is a rough lower bound and not a reliable practical predictor without device/kernel/precision/interconnect benchmarking.


## 9.6 AI token taxonomy, capacity and shared resource pools

- Track input, output, cached-input, provider reasoning/internal output (if metered/disclosed), embeddings, reranking, and modality-specific units separately. Aggregate only after conversion to the same billable rate class and billing period.
- Model TTFT, inter-token latency, end-to-end task latency, retrieval wait, tool wait and human approval wait as distinct metrics. Streaming reduces perceived response time but may not reduce billable tokens.
- Include context/prompt inflation from tool schemas, system policies, long agent memory and retrieval chunks; token load is conditional on context management, not just user text size.
- Hosted API capacity depends on provider quotas and rate limits; self-hosted models require accelerator memory, KV cache, batching, concurrency, utilization, model load/warmup, failure headroom and admission controls.
- Represent agent fan-out, fallback and retry as guarded branching operators; bound recursion and prevent infinite expectation where retries are unconstrained.
- Private cloud GPUs require measured device power/utilization and allocator overhead, and shared clusters need explicit idle, reserved and amortized-cost treatment.

---

[Documentation home](../../README.md) · [Technical reference index](README.md)
