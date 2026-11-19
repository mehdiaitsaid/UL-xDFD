# Contributing to UL-xDFD

We welcome careful research and implementation contributions. Please distinguish **proposed semantics**, **implemented behavior**, **measured evidence**, and **hypotheses**.

## Before proposing a change

Read [the problem definition](README.md#the-problem), [the modeling guide](docs/modeling-guide.md), and [the formal metamodel](docs/technical/04-formal-metamodel.md). Explain which view, lifecycle phase, actor and scenario your proposal addresses. Reusing an existing node or annotation family is preferable to inventing a conflicting meaning.

A good issue includes a concrete use case, the current behavior or missing concept, proposed fields/units, evidence or standard references, and any backward-compatibility implications. Security or privacy concerns should avoid exposing secrets, customer data, or agent transcripts in public issues.

## Pull request checklist

- State whether the change is **documentation**, **schema/validator**, **example**, **interoperability mapping**, or **research evidence**.
- Keep existing identifiers stable; when semantics change, document a migration.
- Provide explicit units, scopes and value statuses for new numbers.
- Add positive and negative fixtures if validation semantics change.
- Update the relevant view, annotation dictionary, standards crosswalk, and changelog.
- Run `python -m pip install -r requirements.txt` and `python -m unittest discover -s tests -v`.
- Do not use a synthetic example as a claim of industrial performance or prediction accuracy.

## Decision process

The research team should designate maintainers, review policies and an external contributor agreement before opening a public contribution workflow. Until that is published, this is a suggested process rather than a formal project governance charter.
