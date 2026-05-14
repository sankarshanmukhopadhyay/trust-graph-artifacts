---
title: Execution Model
layout: default
parent: Executable governance
nav_order: 2
---

# Execution Model

The execution model converts governance claims into a replayable path: input received, authority resolved, delegation checked, revocation state checked, policy evaluated, decision made, enforcement executed, and receipts emitted. A policy that cannot produce a receipt is not evidence-bearing in this repository.


## v0.3.0 execution-time controls

Execution-time governance now includes runtime authority envelopes and machine commitment checks. A consequential action should pass through the following sequence before finalization:

1. identify the technical actor;
2. resolve the accountable controller and represented principal;
3. load the mandate and policy version;
4. evaluate scope, risk, and boundary conditions;
5. check revocation and lifecycle state;
6. produce a decision receipt or commitment receipt;
7. execute, deny, suspend, or route for review;
8. preserve contestability, reversal, or reconciliation evidence.

This sequence is intentionally stronger than authentication. It treats execution as an institutional act that requires authority, evidence, and accountable effect control.


## Authority envelope execution gate

The v0.3.1 execution gate requires consequential agent actions to resolve actor, controller, principal, mandate, scope, policy version, evidence, authority registry state, revocation freshness, decision receipt, and redress route before producing an operational effect. Missing current authority state fails closed for high-consequence actions. Missing redress or human review escalates public-agent actions rather than allowing silent finality.
