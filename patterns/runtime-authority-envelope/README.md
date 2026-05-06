# Runtime Authority Envelope

## Purpose

Runtime governance primitive that binds agent action to accountable authority, mandate, scope, policy, revocation state, evidence, and redress before operational effects are finalized.

## Source essay

- Essay: *The Authority Gap*
- URL: https://thetrustgraph.substack.com/p/the-authority-gap
- Published: 2026-05-06

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.authority-envelope-completeness` — Require technical actor, accountable controller, principal, mandate, scope, policy version, evidence reference, revocation state, and redress route.
- `control.execution-time-revocation-check` — Check authority and mandate status at the moment the operational effect is requested.
- `control.scope-bound-effect` — Deny or route actions whose requested effect exceeds the temporal, jurisdictional, transactional, or risk scope in the envelope.
- `control.redress-route-required` — Require a challenge, reversal, or remediation route for consequential actions.

## Required evidence fields

- `technical_actor`
- `accountable_controller`
- `principal`
- `mandate_reference`
- `scope_boundary`
- `policy_version`
- `revocation_state`
- `decision_receipt`
- `redress_route`

## Threat model

- `threat.identity-authority-substitution` — A named or authenticated agent is treated as authorized without mandate validation.
- `threat.stale-runtime-authority` — The action executes after mandate expiry, suspension, or revocation.
- `threat.unbounded-operational-effect` — The requested operation exceeds the envelope but is still executed.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
