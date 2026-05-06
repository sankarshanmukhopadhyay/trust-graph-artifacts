---
title: TSMM and The Trust Graph
layout: default
nav_order: 5
---

# TSMM and The Trust Graph

This repository only makes sense if the distinction between TSMM and The Trust Graph stays sharp.

## TSMM is the meta model

TSMM is the modeling grammar.
It tells us how to represent trust systems in a way that is structurally legible.

TSMM contributes:

- typed nodes and edges
- explicit trust decisions and effects
- lifecycle-aware representations
- reusable structural consistency across packages

TSMM is about **form**.

## The Trust Graph is the conceptual driver

The Trust Graph is where the pressure comes from.
The essays isolate the recurring operational failures that governance language usually hides.

The Trust Graph contributes:

- problem selection
- failure framing
- architectural stance
- normative pressure around authority, evidence, and accountability

The Trust Graph is about **why this trust problem matters**.

## This repository is the conversion layer

This repository turns essay pressure into TSMM-native packages.

That means:

- the essay does not dictate the final schema
- TSMM does not choose the problem for us
- the package authoring process is responsible for the conversion

## A useful rule of thumb

If a statement explains **why governance breaks**, it probably belongs to the essay layer.
If a statement explains **how the system is modeled**, it probably belongs to the TSMM layer.
If a statement explains **how to use or validate the package**, it probably belongs to this repository’s package layer.

## Why this matters for developers

Without this distinction, governance repositories often become confusing mixes of:

- prose
- policy slogans
- half-structured examples
- incomplete schemas

This repository tries to avoid that. It gives developers a clean path from concept to model to validation.


## v0.2.0 alignment note

Trust Graph Artifacts now declares an explicit TSMM v0.20.0 binding. TSMM is the semantic authority for trust-system concepts. TGA is the interpretation and provenance corpus. TIS is the executable artifact contract layer when validated artifacts need to cross repository or organizational boundaries.

This means a TGA package should be reviewed as a TSMM-native model with Trust Graph provenance, not as an independent trust-system meta-model.
