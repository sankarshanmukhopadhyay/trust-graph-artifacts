# Authoring model

This repository uses a simple authoring rule:

> Write for both the validator and the next developer.

A package is incomplete if it is valid JSON but incomprehensible to a reader.
A package is also incomplete if it reads well but cannot be validated.

## Authoring sequence

1. State the trust problem clearly in the package README
2. Choose the correct package type
3. Express the package in `graph.json`
4. Bound package behavior in `constraints.json`
5. Define proof surfaces in `evidence.json`
6. Add valid and invalid examples
7. Add or update a test vector
8. Run validation

## Writing guidance

Package READMEs should explain three things explicitly:

- what problem pressure came from the essay
- what TSMM structure was chosen to model it
- what a developer or architect should learn from the package

That separation helps new contributors avoid mixing concept language with structural language.

## What not to do

- do not recreate a second ontology beside TSMM
- do not treat the essay as the schema
- do not hide key decisions only in prose
- do not use evidence files as narrative summaries
- do not add package-specific structure when shared structure already exists
