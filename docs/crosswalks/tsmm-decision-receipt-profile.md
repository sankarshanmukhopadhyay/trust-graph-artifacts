---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
---

# TSMM Decision Receipt Profile

TGA decision receipts are TSMM-profiled receipts with Trust Graph provenance extensions.

## Profile boundary

The following fields belong to the TSMM-aligned receipt core:

- `decisionId`
- `timestamp`
- `subjectRef`
- `requestingActorRef`
- `authorityBasis`
- `policyRefs`
- `evidenceRefs`
- `boundaryRef`
- `decision`
- `effect`
- `revocationStateChecked`
- `assuranceLevel`
- `reviewPath`

The following fields are TGA extensions:

- `receiptId`
- `receiptType`
- `sourceEssays`
- `signature`
- `decision.decisionType`
- `effect.controlPlaneStep`
- `effect.transformationApplied`
- `authorityBasis.delegationRefs`
- `authorityBasis.licenseRef`

## Assurance rule

`assuranceLevel` uses TSMM posture language:

- `minimal`
- `operational`
- `assured`
- `agentic`

These values do not claim TIS AL1-AL4 assurance rigor. If a receipt is used in an executable assurance process, it should reference a separate assurance profile or TIS artifact.

## Provenance rule

`sourceEssays` is a design provenance field. It should not be used to prove runtime facts. Runtime evidence belongs in `evidenceRefs`.

