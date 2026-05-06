---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: Decision Provenance
layout: default
parent: Executable governance
nav_order: 5
---

# Decision Provenance

Decision provenance answers what decision was made, which input and output were involved, which authority made the decision valid, which constraints were checked, whether the actor was valid under current revocation state, and which review path remains available.

A decision without provenance is a log entry. A decision with a TSMM-aligned receipt is an assurance artifact.

## Provenance model

TGA decision provenance now uses the same runtime assurance core as TSMM decision receipts:

- `subjectRef` identifies the thing being decided.
- `requestingActorRef` identifies the actor or agent requesting the effect.
- `authorityBasis` records authority source, scope, and status.
- `policyRefs` records the policy surface applied to the decision.
- `evidenceRefs` records the evidence surface inspected by the decision.
- `boundaryRef` records the trust boundary crossed or implicated.
- `decision` records outcome and reason.
- `effect` records whether the operational effect was permitted, blocked, restricted, or queued for review.
- `revocationStateChecked` records the revocation source, status, and check time.
- `reviewPath` records where challenge, appeal, escalation, or redress can occur.

## Trust Graph extension

TGA adds `sourceEssays` to preserve the intellectual provenance of each receipt design. This is intentionally separate from runtime evidence. Essays explain why a control surface matters; receipts prove what happened at execution time.

This distinction keeps TGA aligned with TSMM while preserving the repository's role as an operational interpretation layer for The Trust Graph.


## TSMM v0.20 alignment rule

A TGA decision provenance record is valid when it can be interpreted as a TSMM runtime trust decision without losing authority, policy, evidence, revocation, assurance, effect, or review-path context. TGA-specific fields may add provenance and interpretive force, but they should not redefine TSMM semantics.

Where an external executable artifact contract is needed, the decision can be projected into a TIS-compatible receipt using the composition pattern in `docs/crosswalks/tga-tsmm-tis-composition.md`.
