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
