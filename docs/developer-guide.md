---
title: Developer guide
layout: default
parent: Method and authoring
nav_order: 5
---

# Developer guide

## Local setup

Requirements:

- Python 3.11+
- `jsonschema`

Install:

```bash
pip install jsonschema
```

## Validate changes

```bash
python3 scripts/validate_tsmm_native.py
```

## Recommended workflow for adding or revising a package

1. Update the package README first so intent is clear
2. Update `package.json` classification and metadata
3. Update `graph.json`
4. Update `constraints.json` and `evidence.json`
5. Refresh examples
6. Confirm the invalid example still fails for the right reason
7. Run validation

## Design review questions

Before merging, ask:

- Is the package type correct?
- Is the trust problem clearly bounded?
- Are decision points explicit?
- Are control surfaces visible?
- Does evidence describe what the system must emit, not just what we hope to log?
- Does the README explain the line between essay pressure and TSMM structure?


## TSMM v0.20 alignment checklist

Before merging a new or revised package, verify that:

1. The package has a clear Trust Graph source or governance pressure.
2. The graph models authority, evidence, policy, decision, and effect using TSMM-native concepts where applicable.
3. Any local Trust Graph vocabulary is mapped through `registries/outcome-vocabulary.yaml` or documented as narrative-only.
4. `assuranceLevel` is not treated as a TIS AL1-AL4 claim unless an explicit assurance artifact is referenced.
5. Runtime evidence is represented separately from essay provenance.
6. `python3 scripts/validate_tsmm_native.py` passes.
