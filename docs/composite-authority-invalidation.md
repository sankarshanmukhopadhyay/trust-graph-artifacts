# Composite Authority Invalidation Pressure Test

This project-local artifact exercises the collective-authority proposition without
claiming canonical semantic or portable-contract authority.

The fixture distinguishes the collective principal from its controllers and
tests:

- valid current 2-of-3 exercise;
- insufficient participation;
- duplicate-member counting;
- stale membership;
- stale threshold/exercise rule;
- missing composition evidence; and
- exact-action binding failure.

The crucial lifecycle rule is that a material membership or rule change prevents
old composition evidence from authorizing a **new** action. Historical
verification of an earlier action remains separately preserved when that action
was valid under the state applicable at the time.

TSMM remains the semantic authority. TIS remains the portable contract authority.
This artifact exists so those propositions can be falsified by executable
examples before any cross-stack schema promotion.
