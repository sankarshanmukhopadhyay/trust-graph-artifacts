---
owner: maintainers
last_reviewed: 2026-06-30
applicable_version: v0.4.0
title: TSMM / TIS / TGA Layering
layout: default
parent: TSMM alignment
nav_order: 3
---

# TSMM / TIS / TGA Layering

TGA v0.4.0 is aligned to the TSMM v0.21 and Trust Infrastructure Schemas v0.10 split.

```text
TSMM = semantic trust-system model and runtime governance grammar
TIS  = executable artifact contract layer for assurance evidence
TGA  = Trust Graph interpretation and package corpus
```

## Why this matters

Without this boundary, TGA could accidentally become a parallel schema authority. That would weaken interoperability. The goal is different: TGA should make Trust Graph-derived governance patterns usable as TSMM-native packages and, where required, project them into TIS-compatible runtime assurance artifacts.

## Layer responsibilities

| Responsibility | TSMM | TIS | TGA |
|---|---:|---:|---:|
| Define abstract trust-system concepts | Yes | No | No |
| Define executable artifact shapes | No | Yes | Limited profiles/examples |
| Preserve essay provenance | No | No | Yes |
| Provide governance failure pattern corpus | No | No | Yes |
| Emit runtime decision examples | Yes | Yes | Yes, as profiled examples |
| Own AL1-AL4 assurance semantics | No | Yes | No |
| Define runtime governance envelope semantics | Yes | No | No |
| Validate evidence bundle and decision receipt contracts | No | Yes | No |
| Preserve essay-derived provenance extension | No | No | Yes |

## Composition rule

A TGA-derived runtime decision SHOULD be expressible as:

```text
TGA source package
  → TSMM trust decision semantics
  → TIS executable receipt where publication or external validation is needed
  → TGA provenance extension for essay-derived interpretation context
```

For the v0.4.0 runtime assurance path, prefer the more complete chain in `docs/crosswalks/tga-tsmm-tis-runtime-assurance.md`.
