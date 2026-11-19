# Appendix C. Unit, scope and measurement glossary




| Term | Definition and non-equivalence |
| --- | --- |
| Request / message / business unit | A request may generate many messages and may or may not produce one valid business outcome. |
| CPU core-second vs elapsed second | CPU demand is CPU time on an equivalent core; wall duration includes waiting/parallel processing. |
| vCPU vs core | Provider vCPU is a virtual allocation; actual performance is platform, CPU class and contention dependent. |
| B vs b; GB vs GiB | Byte B = 8 bits; GB decimal; GiB binary. Specify unit convention throughout. |
| Mbps vs MB/s | Bit rate is not byte rate; network link capacity uses transmitted bits and protocol overhead. |
| Observed p95 vs SLO p95 | Observed percentile requires sample/window; target requires scope and verification method. |
| Cost vs price vs usage | Price applies to meter usage; cost may include contracts, credits, allocation and taxes. |
| Billed vs amortized vs effective | Different financial recognition and commitment treatment; do not aggregate blindly. |
| Inferred vs measured | A model calculation is derived; a trace is an observation under a sampling protocol. |
| CI vs prediction interval | Confidence interval addresses parameter uncertainty; prediction interval addresses individual future outcomes. |
| Readiness vs adoption success | Capability profile at t0 differs from observed future attainment and calibrated probability. |
| Security risk score vs policy gate | A risk estimate cannot automatically override a mandatory security control. |
| Completeness vs correctness | Counting annotated items cannot prove representational truth or source accuracy. |


---

[Documentation home](../../README.md) · [Technical reference index](README.md)
