---
layout: default
title: Single-Agent Record Review
parent: Worked Examples
grand_parent: Agentic Systems Architecture and Governance
nav_order: 1
permalink: /guides/agentic-systems-architecture-and-governance/examples/single-agent-bounded-job/
---

# Single-Agent Bounded Record Review

## Job

Review one named internal policy document and produce a non-binding classification and summary. The system may read only the named document and write only a draft review record.

## Authority and effects

| Effect | Authority | Capability |
|---|---|---|
| read policy document | review mandate, named resource | read-only, one-document grant |
| write draft classification | review mandate | draft-record write grant |
| publish final classification | prohibited | no capability issued |

## Sequence

```mermaid
sequenceDiagram
  participant U as Authorized requester
  participant W as Review workflow
  participant P as Policy decision point
  participant B as Capability broker
  participant D as Document store
  participant E as Evidence store
  U->>W: Create bounded review job
  W->>P: Verify role, mandate and document scope
  P-->>W: Permit read
  W->>B: Request one-document read grant
  B-->>W: Scoped grant
  W->>D: Read named document
  W->>P: Submit candidate classification
  P-->>W: Permit draft write only
  W->>E: Store receipts and draft result
```

## Negative demonstrations

- request for a second document is denied;
- attempt to publish is denied;
- expired mandate prevents draft write;
- altered candidate-action digest invalidates approval.
