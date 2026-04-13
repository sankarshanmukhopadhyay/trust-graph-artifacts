# Authoring Model

Each package directory contains:

- `package.json`
- `graph.json`
- `constraints.json`
- `evidence.json`
- `examples/`
- `tests/`
- `README.md`

## Design rules

- Author TSMM-native objects directly
- Keep the source essay in metadata, not in the object grammar
- Prefer explicit trust decisions and effects over implicit consequences
- Add lifecycle semantics whenever authority can narrow, expire, suspend, or revoke
- Add decision receipt expectations whenever a package affects operational outcomes
