---
owner: maintainers
last_reviewed: 2026-04-27
applicable_version: v0.18.0
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
