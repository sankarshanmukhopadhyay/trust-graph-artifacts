# Delegated Consent Protection Policy

## Overview

Formalizes consent as a runtime protection policy that binds permission, delegation, withdrawal, and appeal in AI-mediated settings.

---

## Source

- Essay: *After Consent: Rebuilding Choice, Delegation, and Protection for an AI-Mediated World*
- Published: 2025-12-23
- Canonical link: https://thetrustgraph.substack.com/p/after-consent

---

## Problem

- Static consent records fail under delegated action.
- Protective withdrawal is rarely encoded as a system constraint.
- Harm thresholds and emergency exceptions are often implicit.

---

## Model

- Permitted action classes and purpose binding.
- Delegation limits and chain-depth constraints.
- Protection triggers for pause, deny, or re-consent.
- Structured revocation and appeal paths.

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

This artifact now includes a TSMM projection at `bindings/tsmm/projections/after-consent.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
