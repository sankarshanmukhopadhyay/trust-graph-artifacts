# Trust Graph TSMM Patterns

Most systems claim governance.

Very few can prove it.

This repository exists for the systems that need to.

---

## The problem

Across identity, trust registries, and AI systems, governance is still mostly performative.

- Policies exist, but are not enforced  
- Delegation exists, but is not bounded  
- Revocation exists, but does not propagate  
- Decisions are made, but not evidenced  

At small scale, this is tolerable.

At system scale, it becomes dangerous.

> If a system cannot explain, constrain, and revoke authority at execution time, it is not governed. It is merely configured.

---

## What this repository does

This repository takes concepts from **The Trust Graph** and forces them into a harder form:

**TSMM-native structures that can be tested, validated, and challenged.**

There is no secondary abstraction layer.

There are no narrative-only artifacts.

Everything here is expressed using the **Trust Systems Meta Model (TSMM)** as the only grammar.

---

## What you will find here

This is not a collection of ideas.

It is a collection of **enforceable shapes of systems**.

- **Profiles** — what a bounded trust system must look like  
- **Patterns** — how authority, delegation, and control actually behave  
- **Overlays** — constraints that systems cannot ignore  
- **Systems** — composed, end-to-end representations  
- **Evidence models** — what must be produced when a system acts  

Every entry is:

- structured  
- constrained  
- testable  
- falsifiable  

---

## Why this matters

Most failures in digital systems are not failures of intelligence.

They are failures of control.

- Who was allowed to act?
- Under what authority?
- Was that authority still valid?
- What rules were applied?
- What evidence exists for the decision?

If those questions cannot be answered deterministically, the system is not trustworthy.

It is opaque.

And opacity does not scale.

---

## The position

This repository takes a clear stance:

> Governance that cannot be executed is not governance.

> Safety without revocation is theater.

> Transparency without control is storytelling.

> Logs are not evidence.

The goal is not to describe better systems.

The goal is to make systems **legible, enforceable, and accountable under pressure**.

---

## Relationship to TSMM

TSMM is not a reference here.

It is the foundation.

Every construct in this repository is a TSMM-native object:

- entities and roles  
- authority and delegation  
- controls and constraints  
- decisions and effects  
- evidence and auditability  
- lifecycle and revocation  

This makes every entry:

- comparable  
- composable  
- testable across contexts  

---

## How to use this repository

If you are building systems:

Start with:

- `profiles/`
- `patterns/`
- `overlays/`

Look for what constrains authority, not what enables functionality.

If you are evaluating systems:

Start with:

- `evidence/`
- `validation/`

Ask what the system produces when it acts.

If the answer is “logs”, you are not looking at governance.

---

## Method

Each entry follows a disciplined path:

1. Extract a concept from an essay  
2. Identify authority, control, and lifecycle  
3. Classify into a TSMM-native type  
4. Formalize as a graph  
5. Add constraints  
6. Define evidence  
7. Validate with examples and tests  

If it cannot pass this process, it does not belong here.

---

## What this is not

- Not a standards document  
- Not a policy library  
- Not a compliance checklist  
- Not a theoretical framework  

This is a **working surface for systems that must hold under real conditions**.

---

## Provenance

All concepts originate from:

https://thetrustgraph.substack.com

The essays ask the questions.

This repository forces the answers into executable form.

---

## Final note

Most systems today optimize for capability.

This repository optimizes for **accountability**.

That is a harder problem.

That is the point.
