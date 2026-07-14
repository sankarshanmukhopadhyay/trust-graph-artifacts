# GitHub Commit Message

## Commit Title

```text
Align Trust Graph Artifacts with TSMM v0.21 and TIS v0.10 runtime assurance
```

## Commit Body

```text
Align trust-graph-artifacts as a v0.4.0 runtime assurance release.

This release updates the repository from TSMM v0.20 / TIS v0.8 alignment to
TSMM v0.21 / TIS v0.10, adds a formal TGA-to-TIS runtime assurance binding,
and introduces an end-to-end composition path from Trust Graph essay-derived
governance pressure to TSMM authority/runtime semantics and TIS executable
artifact contracts.

Major changes:
- add bindings/tis/ with TGA-to-TIS v0.10.0 projection metadata and constraints;
- update bindings/tsmm/ to TSMM v0.21.0 runtime governance semantics;
- add six TSMM-native package families for personhood participation, agent
  accountability, machine-decision redress, registry gatekeeper risk,
  proof-first market decisions, and executable trust governance;
- add runtime assurance composition examples under
  examples/composition/runtime-assurance-v0.4/;
- add TGA / TSMM / TIS runtime assurance and portfolio alignment crosswalks;
- update README, quickstart, architecture, documentation index, source catalog,
  provenance map, and essay-to-artifact crosswalks;
- add scripts/validate_tis_alignment.py and requirements.txt;
- harden validators so lean local environments provide useful fallback checks
  while full JSON Schema and YAML validation remain available through pinned
  dependencies.

Governance impact:
- makes authority origin, delegation, scope, policy, evidence, status,
  revocation, effect admission, registry publication, and redress explicit;
- preserves the boundary that essays are provenance and interpretation, not
  runtime evidence;
- preserves the boundary that registry publication is discoverability, not
  authorization;
- positions trust-graph-artifacts as the portfolio research-to-executable-
  artifact translation layer.

Validation:
- python3 scripts/validate_tsmm_native.py
- python3 scripts/validate_tis_alignment.py
- python3 scripts/validate_receipts.py
- python3 scripts/validate_authority_envelopes.py
```
