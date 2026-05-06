---
title: Runtime authority envelopes
layout: default
parent: Authority, commitments, and high-risk governance
nav_order: 1
---

# Runtime authority envelopes

## Purpose

The runtime authority envelope is the v0.3.0 control surface for agentic execution. It treats identity as necessary but insufficient. A system may know which technical actor is present and still be unable to answer whether that actor is permitted to make an institutional action true.

The envelope is therefore the admissibility wrapper for consequential action. It binds actor, controller, principal, mandate, scope, policy version, evidence, revocation state, decision receipt, and redress route before the action is finalized.

## Package surface

- `patterns/runtime-authority-envelope`
- `patterns/agent-mandate-envelope`
- `patterns/authority-legitimacy-validation`
- `evidence/execution-time-delegation`
- `evidence/legitimate-control-decision-receipt`

## Governance invariant

A consequential agent action MUST NOT be treated as authorized only because the agent is named, authenticated, registered, or persistent. Authorization is a runtime relation among accountable controller, represented principal, delegated mandate, policy scope, revocation state, and permitted effect.

## Minimum fields

- technical actor
- accountable controller
- represented principal
- mandate reference
- scope boundary
- policy version
- evaluated facts
- revocation state
- decision receipt reference
- redress or reversal route

## Assurance posture

Authority envelopes are designed to produce evidence, not confidence. A verifier should be able to reconstruct which authority was used, which constraints were checked, which policy version was applied, why the effect was allowed or denied, and how an affected party can contest the result.
