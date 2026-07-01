---
owner: maintainers
last_reviewed: 2026-06-30
applicable_version: v0.4.0
title: TGA / TSMM / TIS Runtime Assurance
layout: default
parent: Crosswalks
nav_order: 6
---

# TGA / TSMM / TIS Runtime Assurance

This crosswalk defines the v0.4.0 alignment path from Trust Graph essay-derived governance pressure to TSMM runtime governance semantics and TIS v0.10.0 executable artifact contracts.

## Release Position

TGA does not become a schema authority in v0.4.0. It remains the Trust Graph interpretation corpus. Its job is to turn governance failure patterns into reusable TSMM-native packages and, where reliance crosses repository or organizational boundaries, project those packages into TIS-compatible evidence artifacts.

## Runtime Assurance Chain

```text
Trust Graph essay-derived package
  -> TSMM authority graph
  -> TSMM runtime governance envelope
  -> TIS authority boundary
  -> TIS evidence bundle
  -> TIS evaluation envelope
  -> TIS decision receipt
  -> TIS registry publication profile
  -> TGA provenance extension
```

## Responsibility Boundary

| Surface | Owner | Purpose |
|---|---|---|
| Essay-derived governance pressure | TGA | Preserve the problem frame and interpretive rationale. |
| Trust-system semantics | TSMM | Define authority, delegation, evidence, policy, trust decision, lifecycle, and effect semantics. |
| Runtime artifact contracts | TIS | Provide machine-validatable authority boundaries, evidence bundles, evaluation envelopes, decision receipts, and registry publication profiles. |
| Provenance extension | TGA | Record source essay and package interpretation without treating the essay as runtime evidence. |

## Artifact Mapping

| TGA Surface | TSMM Concept | TIS Artifact |
|---|---|---|
| `graph.json` | Trust-system graph / authority graph | `profiles/tsmm/tsmm-runtime-governance-projection.schema.json` |
| `constraints.json` authority controls | Authority graph, delegation, policy constraint | `governance/authority-boundary.schema.json` |
| `evidence.json` evidence expectations | Evidence artifact / evidence bundle | `evidence/evidence-bundle-manifest.schema.json` |
| Package assessment | Assessment | `oasf/oasf-evaluation-envelope.schema.json` |
| Package decision receipt | Trust decision / effect admission | `decision/decision-receipt.schema.json` |
| Registry or publication examples | Trust registry / publication state | `registry/registry-publication-profile.schema.json` |

## Non-Equivalence Rules

1. Essay provenance is not runtime evidence.
2. Registry publication is not authorization.
3. A schema-valid artifact is not sufficient proof of legitimate control.
4. A TGA assurance posture label is not a TIS AL1-AL4 assurance level.
5. A completed task is not necessarily an allowed effect.

## Validation Evidence

The v0.4.0 release adds `scripts/validate_tis_alignment.py` to check that active package evidence surfaces which claim TIS runtime assurance projection include the expected authority-boundary, evidence-bundle, evaluation-envelope, decision-receipt, and registry-publication artifact references.

See `examples/composition/runtime-assurance-v0.4/` for the canonical v0.4.0 composition example.
