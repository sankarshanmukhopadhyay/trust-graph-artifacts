# Public Agent Contestability Profile

**Kind:** profile  
**Path:** `profiles/public-agent-contestability-profile`  
**Source essay:** The Authority Gap  
**Published:** 2026-05-05

## Why this package exists

Public-service agents can turn routing, triage, eligibility, enforcement, or administrative recommendations into consequences that affected people must live with. A named agent is not enough. The system must expose who controls the agent, which public authority or delegated mandate made the action legitimate, what scope applied, what current authority state was checked, what receipt was produced, and how the affected person can challenge the result.

## What the essay contributes

The source essay distinguishes technical identity from legitimate authority. This profile applies that distinction to public-agent actions where contestability, human review, and redress cannot be treated as optional UX features.

## What TSMM contributes

TSMM gives the profile a machine-readable governance surface: accountable controller, policy, verifier, evidence bundle, trust decision, operational effect, and redress effect.

## Core controls

- `control.public-agent-function-classification`
- `control.human-review-escalation-required`
- `control.contestable-preliminary-determination`
- `control.redress-route-machine-readable`
- `control.administrative-authority-traceability`

## What to inspect first

1. `graph.json` — public-agent authority and contestability model
2. `constraints.json` — fail-closed and escalation controls
3. `evidence.json` — contestable decision receipt evidence
4. `examples/` — passing and failing graph surfaces
