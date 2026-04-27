# Package taxonomy

Choosing the right package type is an architectural decision.

## Profile

Use a **profile** when the package represents a reusable trust-system configuration with bounded roles, controls, and decisions.

## Pattern

Use a **pattern** when the package captures a recurring governance or control arrangement that can appear in multiple systems.

## Overlay

Use an **overlay** when the package applies cross-cutting policy or governance constraints across other packages.

## System

Use a **system** when the package models a worked end-to-end arrangement with named actors and operational effects.

## Evidence-model

Use an **evidence-model** when the package primarily defines what proof, receipt, verification output, or audit trace must be produced.

## Practical test

Ask this question:

> Is the package mainly about reusable structure, recurring behavior, cross-cutting constraint, composed operation, or proof output?

The answer usually points to the correct package type.


## Systems are intentionally sparse

The `systems/` category is reserved for composed trust-system models with concrete actors, policies, evidence surfaces, decisions, and effects. It is intentionally more selective than `patterns/` or `overlays/`.

The active system example is `systems/wallet-to-agent-identity`. A contributor template is available at `systems/_template/` to make the expected shape explicit without pretending that incomplete compositions are mature packages.
