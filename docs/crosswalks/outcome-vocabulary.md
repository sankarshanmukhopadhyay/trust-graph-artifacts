---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: Outcome Vocabulary Crosswalk
layout: default
parent: TSMM alignment
nav_order: 6
---

# Outcome Vocabulary Crosswalk

Trust Graph language is intentionally expressive. Machine-readable governance artifacts need tighter terms. This crosswalk preserves both.

| TGA local term | TSMM canonical term | Guidance |
|---|---|---|
| `degrade` | `downgrade` | Prefer `downgrade` for decision outcomes. `degrade` may remain in legacy labels, narrative text, or mapped effect IDs. |
| `escalate` | `review` | Use `review` as the decision outcome. Use `escalate` for operational routing to a review path. |
| `quarantine` | `suspend` or `restricted` | Use `suspend` when authority or effect is stopped. Use `restricted` when the effect remains partially admissible. |
| `block` | `deny` or `blocked` | Use `deny` for the decision outcome and `blocked` for effect admission. |

The canonical machine-readable mapping lives in `registries/outcome-vocabulary.yaml`.

