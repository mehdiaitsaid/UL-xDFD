# Core concepts

## What UL-xDFD is

UL-xDFD is an **annotation-driven, multi-view description of a software value stream**. The canonical representation is a typed, directed graph indexed by scenarios, phases, evidence, and snapshots. A diagram is a readable projection of that model; it is not the only source of truth.

The original DFD semantics remain intact:

| Object | Meaning |
| --- | --- |
| `X` | An external actor or system relative to a declared boundary. |
| `P` | A process that performs a meaningful transformation. |
| `S` | A logical store of information. |
| `F` | A directed transfer of information; this does **not** imply temporal precedence. |

Other nodes represent requirements, roles, business value, deployment resources, pipelines, evidence and AI systems. Relations must be typed: `DATA` is different from `WORK`, `OWNERSHIP`, `POLICY`, `AICOST`, and `TOOLCALL`. See the [source-defined node and edge catalog](technical/05-elements-edges-notation.md).

## Views are not phases

`V0` through `V11` tell us *which question is being asked*. `L00` through `L11` tell us *where in the product lifecycle the claim belongs*. A model can track finance in feasibility, rollout, operations, and retirement without creating four independent versions of the same concept.

## Scenario-aware measurements

A fact is only useful with its circumstances. `CPU time = 20 ms` needs a request type, observed or estimated status, instance or aggregate scope, collection window, hardware and evidence source. The same principle applies to model input tokens, GPU reservation time, human approval waiting, and cost per completed transaction.

## Evidence and missingness

The documentation uses `observed`, `reported`, `estimated`, `derived`, `hypothetical`, `unknown`, `disputed`, and `expired`. An expert estimate can be valuable for design, but it is not telemetry. A missing record should result in a visible gap or an insufficient-evidence finding, not a silent assumption of zero usage or zero readiness.

## The digital thread

A typical trace is:

```text
business goal → requirement → data/process → API or agent → test/pipeline
            → deployment → trace or financial record → reviewed outcome
```

This does not prove that the requirement was implemented correctly. It gives reviewers a checkable set of claimed connections and lets tools report broken links.

For the formal definition, annotation inheritance rules, and reference syntax, see [the metamodel](technical/04-formal-metamodel.md), [annotation contract](technical/06-annotation-contract.md), and [serialization appendix](technical/appendix-a-serialization.md).

[Back to README](../README.md)
