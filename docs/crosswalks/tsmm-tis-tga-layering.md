---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: TSMM / TIS / TGA Layering
layout: default
parent: TSMM alignment
nav_order: 3
---

# TSMM / TIS / TGA Layering

TGA v0.2.0 is aligned to the TSMM v0.20 and Trust Infrastructure Schemas v0.8 split.

```text
TSMM = semantic trust-system model
TIS  = executable artifact contract layer
TGA  = Trust Graph interpretation and package corpus
```

## Why this matters

Without this boundary, TGA could accidentally become a parallel schema authority. That would weaken interoperability. The goal is different: TGA should make Trust Graph-derived governance patterns usable as TSMM-native packages and, where required, project them into TIS-compatible artifacts.

## Layer responsibilities

| Responsibility | TSMM | TIS | TGA |
|---|---:|---:|---:|
| Define abstract trust-system concepts | Yes | No | No |
| Define executable artifact shapes | No | Yes | Limited profiles/examples |
| Preserve essay provenance | No | No | Yes |
| Provide governance failure pattern corpus | No | No | Yes |
| Emit runtime decision examples | Yes | Yes | Yes, as profiled examples |
| Own AL1-AL4 assurance semantics | No | Yes | No |

## Composition rule

A TGA-derived runtime decision SHOULD be expressible as:

```text
TGA source package
  → TSMM trust decision semantics
  → TIS executable receipt where publication or external validation is needed
  → TGA provenance extension for essay-derived interpretation context
```

