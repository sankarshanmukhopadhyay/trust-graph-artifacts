---
title: Methodology
layout: default
parent: Method and authoring
nav_order: 1
---

# Methodology

This repository exists at the boundary between a conceptual corpus and a modeling discipline.

- **The Trust Graph** contributes the conceptual pressure
- **TSMM** contributes the structural grammar
- **This repository** contributes the package design and validation discipline

## 1. Essay qualification

A source essay must contain enough operational structure to be converted into a TSMM-native package.
Signal helps prioritize, but signal alone never qualifies an essay.

A qualifying essay should yield at least one of the following clearly enough to model:

- named actors, institutional positions, or operational subjects
- bounded authority or authority failure modes
- control surfaces or policy constraints
- decision points or admissibility thresholds
- evidence, verification, or challenge semantics
- lifecycle, revocation, supersession, or invalidation implications

## 2. Package classification

Once qualified, the concept is assigned to the most appropriate TSMM-native package type:

- profile
- pattern
- overlay
- system
- evidence-model

Choosing the wrong package type usually makes the package harder to understand than the graph itself.

## 3. Native authoring

The concept is then authored directly as a TSMM-native package.
The repository does not preserve an intermediate artifact vocabulary.

A package must define:

- source provenance
- package metadata
- graph structure
- constraints and controls
- evidence outputs
- valid and invalid examples
- at least one test vector

## 4. Validation

The package must pass repository validation and remain understandable to a technically literate reader.

That means this repository optimizes for two forms of legibility at once:

- machine legibility through schemas and validation
- developer legibility through READMEs, file structure, and predictable package anatomy
