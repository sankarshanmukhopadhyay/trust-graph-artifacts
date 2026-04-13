# Privacy Term Enforcement Profile

## Overview

Encodes privacy terms as enforceable profiles that can survive delegation into processor and agent chains.

---

## Source

- Essay: *Machine-Readable Privacy Terms and the Infrastructure of Control*
- Published: 2026-01-30
- Canonical link: https://thetrustgraph.substack.com/p/machine-readable-privacy-terms

---

## Problem

- Privacy terms are usually descriptive rather than enforceable.
- Downstream processors can drift from the original use boundary.
- Deletion promises are not machine-checked.

---

## Model

- Allowed purposes and prohibited uses.
- Retention and deletion obligations.
- Transfer boundaries.
- Complaint and remedy channels.

---

## Governance Impact

### Authority

Authority is made explicit in the schema and manifest rather than inferred from surrounding context.

### Delegation

Delegated behavior is bounded by declared fields, conditions, and lifecycle controls.

### Enforcement

The artifact is designed to support deterministic checks rather than narrative interpretation alone.

### Revocation

The artifact includes status or lifecycle controls that can narrow, suspend, or withdraw its effect.

### Redress

A structured path exists for challenge, correction, or appeal where the concept requires it.

---

## Status

Draft

---

## Next Steps

- refine field cardinality and enum coverage
- add JSON Schema or equivalent validation form
- add richer edge-case examples

---

## TSMM Binding

This artifact now includes a TSMM projection at `bindings/tsmm/projections/machine-readable-privacy-terms.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
