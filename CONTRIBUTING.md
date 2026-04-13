# Contributing

Thank you for contributing to `trust-graph-artifacts`.

This repository converts selected Trust Graph concepts into governed artifacts. Contributions should improve structural clarity, executable precision, and validation quality.

---

## What to contribute

Useful contributions include:

- artifact proposals grounded in published essays
- schema refinements
- valid and invalid examples
- test cases
- mappings to related control systems or standards
- lifecycle and governance clarifications

---

## Before you open a pull request

Please ensure that the contribution:

1. identifies the source essay or conceptual basis
2. explains the governance problem being formalized
3. states what changes in authority, delegation, enforcement, revocation, or redress
4. includes or updates `artifact.yaml` where relevant
5. preserves naming and folder conventions

---

## Artifact proposals

New artifacts should begin with:

- an evaluation record in `evaluation/evaluations/`
- a proposed artifact folder derived from `artifacts/_template/`
- a clear rationale for why the concept requires formalization

Not every essay should become an artifact.

---

## Review criteria

Maintainers will review contributions for:

- conceptual precision
- structural coherence
- enforceability
- lifecycle clarity
- usefulness of examples and tests

---

## Discussion labels

Recommended issue labels:

- `artifact-proposal`
- `semantic-dispute`
- `enforcement-gap`
- `needs-examples`
- `needs-tests`
- `supersession`

---

## Style

Write clearly and precisely. Prefer falsifiable claims, explicit constraints, and implementation consequences over abstractions.
