---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: TSMM v0.20 Alignment
layout: default
nav_order: 6
---

# TSMM v0.20 Alignment

Trust Graph Artifacts v0.2.0 aligns the active package corpus with TSMM v0.20.0. The release does not replace the existing corpus. It makes the repository boundary explicit so that TGA remains an interpretation and evidence corpus rather than a competing meta-model.

## Layer boundary

| Layer | Repository | Ownership |
|---|---|---|
| Semantic trust-system grammar | TSMM | Entities, authority, delegation, policy, evidence, lifecycle state, verification, trust decisions, operational effects, and runtime governance semantics. |
| Executable artifact contracts | Trust Infrastructure Schemas | Authority boundaries, evidence bundles, decision receipts, registry entries, assurance levels, and validation-ready publication artifacts. |
| Interpretation corpus | Trust Graph Artifacts | Essay-derived governance packages, failure patterns, provenance overlays, and TSMM-native examples. |

## Normative posture

A TGA package is not a new trust model. It is a TSMM-native interpretation package with Trust Graph provenance.

TGA MAY introduce package-specific vocabulary when that vocabulary is required to preserve the force of the source argument. TGA MUST map such vocabulary to TSMM concepts when the term appears in machine-readable artifact surfaces.

TGA MUST distinguish essay provenance from runtime evidence. Essays explain why a governance pattern matters. Runtime evidence proves what a system evaluated, accepted, denied, restricted, or escalated at execution time.

## What changed in v0.2.0

- Added `bindings/tsmm/tga-tsmm-binding.json` as the machine-readable alignment declaration.
- Added `bindings/tsmm/constraints.json` as the binding constraint set.
- Added TSMM decision receipt profile documentation.
- Added outcome and assurance vocabulary mappings.
- Added a TSMM/TIS/TGA composition example for executable governance decisions.
- Updated stale documentation version markers.
- Updated decision receipt schema namespace hygiene.

## Implementation rule

When a new package is added, it should answer four questions:

1. Which Trust Graph source or governance pressure motivated it?
2. Which TSMM concepts does it model?
3. Which evidence or decision artifacts would prove the modeled governance claim at runtime?
4. Does any machine-readable vocabulary require a crosswalk to TSMM or TIS?

