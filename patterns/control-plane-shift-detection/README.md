# Control Plane Shift Detection Pattern

**Kind:** pattern  
**Path:** `patterns/control-plane-shift-detection`  
**Source essay:** The Control Plane Has Already Shifted  
**Published:** 2026-04-13

## Why this package exists

Governance authority shifts into execution infrastructure without being explicitly recorded.

## What the essay contributes

The source essay supplies the design pressure around control-plane, legitimacy. This package turns that pressure into a TSMM-native shape that can be inspected, tested, and extended.

## What TSMM contributes

TSMM gives this package a structural vocabulary for authority, policy, evidence, trust decisions, and downstream effects.

## What to inspect first

1. `graph.json` — the package system shape
2. `constraints.json` — control and failure boundaries
3. `evidence.json` — evidence expectations
4. `examples/` — passing and failing graph surfaces
