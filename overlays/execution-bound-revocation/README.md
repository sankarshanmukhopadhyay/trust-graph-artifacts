# Execution-Bound Revocation Overlay

## Purpose

Binds revocation evaluation to the moment of action, not merely issuance, resolution, or archival preservation.

This package is part of the repository's **Temporal Governance and Revocation Dynamics** layer. It treats revocation and persistence as executable governance problems: authority must be checked at the moment of use, propagation state must be evidenced, and downstream effects must be auditable.

## Source essay

- **The Persistence Trap** — https://thetrustgraph.substack.com/p/the-persistence-trap
- Published: `2026-04-14`

## What this package tests

- Whether authority remains legitimate at execution time.
- Whether revocation state is fresh enough for the action being taken.
- Whether propagation evidence exists across relevant execution nodes.
- Whether downstream delegations or derived artifacts are contaminated by upstream revocation.
- Whether timing/routing/replay signals are recorded without overclaiming intent.

## Evidence produced

- `revocation-propagation-receipt`
- `execution-authority-state-receipt`
- `gradient-exploitation-signal-receipt` where risk indicators are present

## Enforcement posture

Execution MUST be blocked, quarantined, or escalated when current authority state cannot be proven within the configured freshness and propagation bounds.
