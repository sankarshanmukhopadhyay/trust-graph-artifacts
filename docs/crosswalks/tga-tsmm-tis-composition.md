---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: TGA → TSMM → TIS Composition
layout: default
parent: TSMM alignment
nav_order: 4
---

# TGA → TSMM → TIS Composition

This document explains how a Trust Graph-derived package can be expressed through TSMM and then projected toward executable artifact contracts.

## Flow

```text
1. TGA source package identifies a governance failure pattern.
2. TSMM graph semantics describe the actors, authority, policies, evidence, decisions, and effects.
3. TGA decision receipt records the runtime decision using TSMM-profiled fields.
4. TIS-compatible receipt shape can be produced where external validation or publication is required.
5. TGA provenance extension preserves the Trust Graph essay origin and interpretive rationale.
```

## Example location

See:

```text
examples/composition/tsmm-tis-aligned-tga-decision/
```

## Governance interpretation

This flow prevents three common failures:

1. Treating essays as evidence.
2. Treating a local package schema as a competing meta-model.
3. Treating registry publication or discovery as runtime authorization.

