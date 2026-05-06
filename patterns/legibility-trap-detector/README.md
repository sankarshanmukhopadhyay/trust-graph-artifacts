# Legibility Trap Detector Pattern

## Purpose

Pattern for detecting when institutions respond to inference failure by demanding more machine-readable behavior instead of replacing inference with verification infrastructure.

## Source essay

- Essay: *Before the Graph*
- URL: https://thetrustgraph.substack.com/p/before-the-graph
- Published: 2026-04-13

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.proxy-expansion-detection` — Detect growth in behavioral proxies used to compensate for weak verification.
- `control.user-burden-shift` — Flag systems that push verification cost or legibility burden onto subjects.
- `control.context-suppression-check` — Flag loss of human context, ambiguity, and contestability in machine-readable processes.
- `control.verification-alternative-required` — Require an available verification alternative before expanding inference demands.

## Required evidence fields

- `proxy_expansion_signal`
- `user_burden_assessment`
- `context_suppression_signal`
- `verification_alternative`
- `contestability_route`

## Threat model

- `threat.proxy-intensification` — Institution demands more proxy signals after inference failure.
- `threat.context-collapse` — Machine legibility strips the context needed for fair governance.
- `threat.false-risk-amplification` — Weak proxies increase friction or exclusion for legitimate subjects.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
