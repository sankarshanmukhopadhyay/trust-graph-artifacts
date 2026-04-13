# First-Person Assertion Envelope

## Overview

This artifact formalizes a shift away from issuer-centric admissibility toward accountable first-person assertions evaluated against explicit acceptance policy.

The core claim is that some high-value decisions require subjects to present evidence-bearing assertions directly, with the receiving party making admissibility decisions against declared policy rather than treating third-party issuance as the only legitimate source of trust.

---

## Source

- Essay: *First-Person Credentials*
- Published: 2026-03-02
- Canonical link: https://thetrustgraph.substack.com/p/first-person-credentials

---

## Problem

Credential systems often collapse admissibility into issuance. That works poorly when:

- no relevant issuer exists
- the subject must speak for itself in near real time
- evidence is heterogeneous or distributed
- dispute and challenge need to remain open after submission

Without a governed structure, first-person claims become either informal statements with weak trust value or opaque application data with no explicit challenge semantics.

---

## Model

This artifact defines an assertion envelope with:

- a **subject** making the assertion
- a **claim** being advanced
- supporting **evidence references**
- an **attestation method** describing how the subject stands behind the claim
- **counterparty requirements** describing what the receiving party expects
- a **dispute endpoint** for challenge and correction
- lifecycle controls such as expiry and supersession

The model is designed to separate assertion, evaluation, and challenge rather than collapsing them into a single trust gesture.

---

## Governance Impact

### Authority

Authority to assert remains with the subject. Authority to accept remains with the receiving party and its policy.

### Delegation

Evaluation can be delegated, but the basis for acceptance must remain inspectable.

### Enforcement

Assertions can be accepted or rejected against machine-readable fields and policy requirements.

### Revocation

Assertions may expire, be superseded, or have evidence references withdrawn.

### Redress

A challenge path is mandatory. Redress is not treated as an external afterthought.

---

## Status

Draft

---

## Next Steps

- refine field cardinality and evidence typing
- add JSON Schema or equivalent validation form
- add test cases for conflicting evidence and supersession


## TSMM Binding

This artifact now includes a TSMM projection at `bindings/tsmm/projections/first-person-credentials.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
