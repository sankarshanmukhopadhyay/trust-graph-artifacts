---
title: Machine commitments
layout: default
parent: Authority, commitments, and high-risk governance
nav_order: 2
---

# Machine commitments

## Purpose

Machine commitments are operational promises, obligations, reservations, approvals, offers, acceptances, or future-state assertions created by automated systems. They become governance-relevant when another party can reasonably rely on them.

v0.3.0 introduces a commitment governance cluster that treats commitments as evidence-bearing institutional objects rather than transient model outputs.

## Package surface

- `profiles/machine-commitment-governance-profile`
- `evidence/proof-carrying-commitment-receipt`
- `overlays/commitment-lifecycle-mediation`

## Lifecycle states

Commitments may move through drafted, authorized, issued, active, modified, conflicted, fulfilled, breached, reconciled, revoked, retired, or expired states. Lifecycle state is not documentation metadata. It controls whether the commitment may still induce reliance.

## Proof-carrying commitment model

A proof-carrying commitment records:

- commitment identifier
- technical actor
- accountable controller
- principal
- delegated mandate
- policy version
- commitment terms
- activation conditions
- constraint checks
- authority validation
- revocation state
- execution attestation
- counterparty reliance
- reconciliation route
- contestability route

## Assurance posture

A machine commitment is not governable unless it can be independently evaluated. The receipt must allow a verifier to answer who had authority to commit, what was actually committed, under which constraints, whether reliance was foreseeable, and what happens if the commitment drifts, conflicts, or fails.
