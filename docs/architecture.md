# Architecture

This repository has a deliberately simple architecture.

## Layer 1: Concept source

`essays/` and `provenance/` preserve where the package idea came from.
These files answer questions like:

- Which essay introduced the core pressure or failure mode?
- When was it published?
- What package or packages were derived from it?

## Layer 2: TSMM-native package corpus

`profiles/`, `patterns/`, `overlays/`, `systems/`, and `evidence/` are the operational center of the repository.

Each package is self-contained and machine-readable. A package exists to express one reusable trust-system construct in native TSMM terms.

## Layer 3: Shared vocabularies and rules

`registries/` and `schemas/` provide the common language and validation boundaries that keep the corpus coherent.

- registries define reusable terms and categories
- schemas define what a valid package and graph must look like

## Layer 4: Validation and maintenance

`scripts/` and `validation/` turn the repository from a static document set into something a developer can check, extend, and trust incrementally.

## Design principle

The repository intentionally separates:

- **problem framing**
- **system grammar**
- **reusable package implementation**

That separation is what keeps The Trust Graph from collapsing into theory and TSMM from being treated as abstract decoration.
