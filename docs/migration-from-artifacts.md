# Migration from the earlier artifact model

This repository used to represent essay-derived work as local artifacts with TSMM bindings layered on afterward.

That model has been retired in favor of direct TSMM-native authoring.

## What changed

- `artifacts/` has been replaced by package-type directories
- `artifact.yaml` has been replaced by `package.json`
- TSMM is no longer treated as a binding target
- graphs, constraints, and evidence are now the primary source structures

## Why the change matters

The earlier model was semantically compatible with TSMM, but it still carried a separate local ontology. The new model removes that duplication and makes the line between essay narrative and TSMM structure easier to understand.
