---
title: Public agent contestability
layout: default
parent: Authority, commitments, and high-risk governance
nav_order: 2
last_reviewed: 2026-05-14
---

# Public agent contestability

## Purpose

Public-sector and public-service agents require a stricter authority posture than ordinary workflow automation because their actions can affect eligibility, routing, benefit access, enforcement posture, administrative burden, or procedural rights. The public-agent contestability profile applies the runtime authority envelope to those contexts.

## Package surface

- `profiles/public-agent-contestability-profile`
- `artifacts/public-agent-contestability-profile`
- `schemas/receipts/authority_envelope_receipt.schema.json`
- `validation/authority-envelope-test-cases.yaml`

## Control requirements

- Classify whether the agent action is advisory, routing, eligibility-affecting, denial-producing, approval-producing, enforcement-adjacent, or commitment-generating.
- Bind the action to a public accountable controller and mandate.
- Require current authority-state verification before consequential effect.
- Produce a contestable authority-envelope receipt.
- Preserve a human review path for high-consequence or unverifiable action.
- Publish a machine-readable redress route with remedy class and responsible office.

## Enforcement and revocation

A public-agent action SHOULD fail closed or escalate when the authority registry is unreachable, revocation state is stale, the mandate is outside scope, or the redress route is missing. Public systems must not convert automation convenience into non-contestable administrative finality.

## Evidence produced

The expected evidence artifact is an authority-envelope receipt that records technical actor, accountable controller, principal, mandate, scope, policy version, evidence references, revocation state, decision receipt reference, execution context, assurance posture, and redress route.
