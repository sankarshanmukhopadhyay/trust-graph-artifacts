# Artifact Methodology

This repository treats The Trust Graph essays as design pressure, not as executable truth. Each artifact translates an essay-derived governance claim into TSMM-aligned structure, schema validation, examples, tests, and evidence receipts.

## Source essays for this update

- [The Control Plane Has Already Shifted](https://thetrustgraph.substack.com/p/the-control-plane-has-already-shifted) — published 2026-04-13
- [The Commons After the Control Plane Shifts](https://thetrustgraph.substack.com/p/the-commons-after-the-control-plane) — published 2026-04-17
- [Who Holds the License](https://thetrustgraph.substack.com/p/who-holds-the-license) — published 2026-04-18

## Method

1. Identify the governance failure named by the essay.
2. Bind the failure to TSMM primitives: authority, delegation, scope, control, decision, lifecycle, evidence.
3. Produce an artifact YAML with source provenance.
4. Provide schema coverage and example instances.
5. Require receipts for each execution path.
6. Map risks to controls and tests.


## v0.3.0 artifact admission rule

A new artifact should be added when an essay introduces a control surface that can produce testable evidence. v0.3.0 applies that rule to authority envelopes, machine commitments, fraud externalities, inference substitution, legibility traps, high-risk infrastructure, and constitutional boundaries.

The admission test is whether the artifact can answer at least one of the following in machine-verifiable form: who had authority, what scope applied, what evidence was evaluated, what lifecycle state controlled execution, what effect was produced, and what route exists for challenge, reversal, reconciliation, or remediation.
