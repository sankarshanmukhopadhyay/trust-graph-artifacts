# Test Harness

This directory records validation logic and harness notes for the repository.

## Active validator

- `scripts/validate_tsmm_bindings.py` validates the TSMM binding layer for the 12-artifact expansion set.

Current checks:

- manifest-level TSMM binding references
- projection completeness
- shared registry reference integrity
- trust decision to effect linkage
- lifecycle minimum-state coverage
