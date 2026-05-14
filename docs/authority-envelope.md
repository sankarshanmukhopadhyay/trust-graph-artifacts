---
title: Runtime authority envelopes
layout: default
parent: Authority, commitments, and high-risk governance
nav_order: 1
last_reviewed: 2026-05-14
---

# Runtime authority envelopes

## Purpose

The runtime authority envelope is the control surface for consequential agentic execution. It treats identity as necessary but insufficient. A system may know which technical actor is present and still be unable to answer whether that actor is permitted to make an institutional action true.

The envelope is therefore the admissibility wrapper for consequential action. It binds actor, controller, principal, mandate, scope, policy version, evidence, revocation state, decision receipt, and redress route before the action is finalized.

## Source alignment

This package is derived from *The Authority Gap* and the associated authority-envelope framing in The Trust Graph. The repository uses the canonical source URL `https://thetrustgraph.substack.com/p/the-authority-gap` and treats `the-authority-envelope` as an authority-envelope source alias when referenced in issue discussions or release planning.

## Package surface

- `patterns/runtime-authority-envelope`
- `patterns/agent-mandate-envelope`
- `patterns/authority-legitimacy-validation`
- `evidence/execution-time-delegation`
- `evidence/legitimate-control-decision-receipt`
- `profiles/public-agent-contestability-profile`
- `schemas/receipts/authority_envelope_receipt.schema.json`
- `examples/receipts/authority_envelope_receipt.example.json`

## Governance invariant

A consequential agent action MUST NOT be treated as authorized only because the agent is named, authenticated, registered, or persistent. Authorization is a runtime relation among accountable controller, represented principal, delegated mandate, policy scope, revocation state, and permitted effect.

## Minimum envelope fields

- technical actor
- accountable controller
- represented principal
- mandate reference
- scope boundary
- policy version
- evidence references
- revocation state check
- decision receipt reference
- redress or reversal route
- execution context
- assurance posture

## Execution path

1. Resolve the technical actor.
2. Resolve the accountable controller.
3. Resolve the represented principal.
4. Load the delegated mandate.
5. Load the current policy version.
6. Evaluate temporal, purposive, jurisdictional, transactional, and risk scope.
7. Resolve current authority state from the authority registry.
8. Check revocation freshness and cache age.
9. Bind the decision receipt to policy, evidence, revocation state, and redress route.
10. Allow, deny, suspend, or escalate.

## Runtime enforcement posture

The v0.3.1 hardening layer makes the envelope testable. `scripts/validate_authority_envelopes.py` executes authority-envelope completeness cases, PAD cases, and revocation-lag cases. `scripts/validate_tsmm_native.py` runs those checks as part of the repository-wide validation gate.

Implemented validation targets include:

- `authority-envelope-runtime-completeness`
- `PAD-001`
- `PAD-002`
- `RLG-001`
- `RLG-002`
- `public-agent-contestability`

## Assurance posture

Authority envelopes are designed to produce evidence, not confidence. A verifier should be able to reconstruct which authority was used, which constraints were checked, which policy version was applied, why the effect was allowed, denied, suspended, or escalated, and how an affected party can contest the result.
