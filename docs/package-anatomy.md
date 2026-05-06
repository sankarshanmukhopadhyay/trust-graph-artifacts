---
title: Package anatomy
layout: default
nav_order: 4
---

# Package anatomy

Every package in this repository follows the same core shape.
This consistency is part of the developer experience.

## Required files

### `package.json`
Metadata, classification, source essay provenance, and pointers to the other package surfaces.

### `graph.json`
The primary TSMM-native structure. This is where the system shape lives.

### `constraints.json`
Operational constraints, controls, threats, and lifecycle rules that bound package behavior.

### `evidence.json`
The evidence outputs, verification expectations, and decision-receipt surfaces required by the package.

### `examples/valid-graph.json`
A minimal graph instance that should pass repository validation.

### `examples/invalid-graph.json`
A deliberately broken graph instance that should fail repository validation.

### `tests/test-vector.json`
A compact declaration of what the validator is expected to observe.

### `README.md`
A narrative bridge for humans. It explains why the package exists, how it uses TSMM, and what a developer should inspect first.

## Reading strategy

When reviewing a package, read from outside in:

1. README
2. package metadata
3. graph
4. constraints
5. evidence
6. examples and tests

That lets you understand the package before you inspect implementation details.
