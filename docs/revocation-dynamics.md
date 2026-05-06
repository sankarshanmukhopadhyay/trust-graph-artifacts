---
title: Revocation Dynamics
layout: default
parent: Temporal governance
nav_order: 2
---

# Revocation Dynamics

Revocation is not a flag. It is a distributed governance process.

A revocation event becomes meaningful only when relying environments stop accepting the revoked authority. The interval between origin revocation and enforcement convergence is the revocation lag gradient.

## Required evidence

A revocation-aware system should capture:

- the revocation origin;
- the effective time;
- each node that observed the event;
- each node that enforced the event;
- lag in milliseconds;
- fail-open or fail-closed behavior;
- maximum observed lag;
- final consistency state.

## Assurance posture

High-assurance systems should prefer fail-closed or escalation behavior when revocation state is stale, partially propagated, or unverifiable.

The `revocation-lag-analyzer` package is the anchor artifact for this capability.
