# Portable Eligibility Credential Profile

## Overview

Turns eligibility into a portable credential profile that can be reused across counterparties without repeated proving rituals.

---

## Source

- Essay: *Portable Eligibility: Turning Credentials into Composable Market Access*
- Published: 2026-01-23
- Canonical link: https://thetrustgraph.substack.com/p/portable-eligibility

---

## Problem

- Eligibility is recomputed separately by every market participant.
- Portability is weak even when the underlying facts are stable.
- Individuals and firms bear repeated proof costs.

---

## Model

- Eligibility class and jurisdiction.
- Qualifying basis and validity window.
- Reliance conditions.
- Appeal endpoint.

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
