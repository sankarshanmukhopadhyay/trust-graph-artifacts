# Legitimacy Gap Evaluator Pattern

**Kind:** pattern  
**Path:** `patterns/legitimacy-gap-evaluator`  
**Source essay:** The Control Plane Has Already Shifted  
**Published:** 2026-04-13

## Why this package exists

Systems exercise real authority without the controls needed to make that authority legitimate.

## What the essay contributes

The source essay supplies the design pressure around legitimacy, control-plane. This package turns that pressure into a TSMM-native shape that can be inspected, tested, and extended.

## What TSMM contributes

TSMM gives this package a structural vocabulary for authority, policy, evidence, trust decisions, and downstream effects.

## What to inspect first

1. `graph.json` — the package system shape
2. `constraints.json` — control and failure boundaries
3. `evidence.json` — evidence expectations
4. `examples/` — passing and failing graph surfaces
