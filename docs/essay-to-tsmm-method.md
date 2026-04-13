# Essay-to-TSMM Method

## Purpose

This method defines how a narrative essay becomes a TSMM-native package.

## Step 1: Determine package kind

Decide whether the essay yields primarily a:

- profile
- pattern
- overlay
- system
- evidence-model

Use the minimum type that captures the concept cleanly.

## Step 2: Extract trust-system primitives

Extract, at minimum:

- actors and roles
- authority sources
- policy surfaces
- trust relationships
- evidence or assessment expectations
- trust decisions
- downstream effects
- lifecycle states and revocation semantics

## Step 3: Construct TSMM graph

Create `graph.json` using the TSMM graph schema. The graph should include only the nodes and edges necessary to make the concept legible and testable.

## Step 4: Externalize constraints

Create `constraints.json` containing:

- control set
- policy rules
- threats
- lifecycle states and transitions

## Step 5: Externalize evidence

Create `evidence.json` containing:

- evidence outputs
- verification expectations
- decision receipt requirements

## Step 6: Add examples and tests

Every package must include:

- one valid graph example
- one invalid graph example
- a package-local test vector with expected outcomes
