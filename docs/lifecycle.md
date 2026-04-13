# Lifecycle

Artifacts in this repository move through a controlled lifecycle.

```text
Idea → Essay → Evaluated → Draft → Experimental → Stable → Deprecated
```

## States

### Draft

Initial formalization exists but is incomplete.

### Experimental

The model is structurally coherent and may include examples or early tests.

### Stable

The artifact has sufficient clarity, examples, and validation support for sustained reuse.

### Deprecated

The artifact remains visible for lineage but should no longer be used for new work.

## Lifecycle rules

- Every artifact must declare status in `artifact.yaml`.
- Deprecated artifacts should identify a successor where possible.
- Lifecycle transitions must be justified in pull requests or decision notes.
