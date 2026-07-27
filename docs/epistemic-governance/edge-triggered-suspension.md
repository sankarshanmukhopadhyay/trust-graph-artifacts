---
title: Edge-triggered suspension
layout: default
parent: Epistemic governance
nav_order: 4
---
# Edge-triggered suspension

A qualifying objection can pause effect admission before consequences make a knowledge failure visible. Adopters configure eligible objectors, threshold, objection window, suspension period, review authority, emergency override, and retrospective review.

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Announced
  Announced --> Suspended: qualifying objection
  Announced --> Implemented: gate satisfied
  Suspended --> Reviewed
  Reviewed --> Modified
  Reviewed --> Withdrawn
  Reviewed --> Implemented
  Suspended --> Override: bounded emergency
  Override --> RetrospectiveReview
```

Thresholds are profile parameters, not universal constants.
