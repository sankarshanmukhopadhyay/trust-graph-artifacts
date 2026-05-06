---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: Assurance Posture Crosswalk
layout: default
parent: TSMM alignment
nav_order: 7
---

# Assurance Posture Crosswalk

TGA uses TSMM posture labels in active decision receipts. These labels describe the maturity and operating posture of the modeled system. They are not equivalent to TIS AL1-AL4 assurance levels.

| TGA / TSMM posture | Meaning | Typical executable assurance floor |
|---|---|---|
| `minimal` | Basic model integrity and provenance are available. | AL1 candidate |
| `operational` | Runtime evidence, authority checks, and review path are represented. | AL2 candidate |
| `assured` | Stronger audit or independent assessment evidence is expected. | AL3 candidate |
| `agentic` | Agent-mediated execution context. Not an assurance level. | Risk-based AL selection |

## Rule

Where executable assurance rigor is required, TGA packages SHOULD also reference TIS AL1-AL4 or another explicit assurance profile.

The canonical machine-readable mapping lives in `registries/assurance-vocabulary.yaml`.

