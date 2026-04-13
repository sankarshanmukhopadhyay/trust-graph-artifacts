# Verification Policy Profile

## Overview

Turns verification policy into an explicit profile covering admissibility, issuer legitimacy, status checks, fallback handling, and disputes.

---

## Source

- Essay: *Why Digital Credential Verification Needs a New Policy Playbook*
- Published: 2025-12-19
- Canonical link: https://thetrustgraph.substack.com/p/why-digital-credential-verification

---

## Problem

- Verification rules are often implicit.
- Credential authenticity is confused with issuer legitimacy.
- Revocation checks are inconsistently applied.

---

## Model

- Claim coverage and issuer requirements.
- Freshness and revocation rules.
- Fallback handling.
- Appeal and evidence retention duties.

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
