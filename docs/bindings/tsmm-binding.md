---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
title: TSMM Binding
layout: default
parent: TSMM alignment
nav_order: 1
---

# TSMM Binding

The active binding declaration is available at:

```text
bindings/tsmm/tga-tsmm-binding.json
```

The binding constraints are available at:

```text
bindings/tsmm/constraints.json
```

## Binding purpose

The binding makes explicit that Trust Graph Artifacts is an interpretation corpus aligned to TSMM v0.20.0.

TGA owns package interpretation and essay provenance. TSMM owns the trust-system semantic grammar. TIS owns executable artifact contracts when artifacts need external validation, registry publication, or assurance-level semantics.

## Validation

Run:

```bash
python3 scripts/validate_tsmm_native.py
```

