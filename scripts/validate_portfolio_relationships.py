#!/usr/bin/env python3
from pathlib import Path
import json

p = Path('data/portfolio-relationships.json')
d = json.loads(p.read_text())
required = {'source_repository','target_repository','relationship_type','authority_direction','artifact_mapping','compatibility_range','maturity','validation','known_limitations','supersession'}
relationships = d.get('relationships', [])
for i, rel in enumerate(relationships):
    missing = required - set(rel)
    if missing:
        raise SystemExit(f'relationship {i} missing: {sorted(missing)}')
    if rel['source_repository'] == rel['target_repository']:
        raise SystemExit('self dependency is not permitted')

required_baselines = {
    ('trust-graph-artifacts', 'trust-systems-meta-model', 'normative-dependency'): 'TSMM v0.24.0 reviewed baseline',
    ('trust-infrastructure-schemas', 'trust-graph-artifacts', 'supports'): 'TIS v0.14.1 reviewed baseline',
}
for key, expected in required_baselines.items():
    matches = [rel for rel in relationships if (rel['source_repository'], rel['target_repository'], rel['relationship_type']) == key]
    if len(matches) != 1:
        raise SystemExit(f'expected exactly one portfolio relationship for {key}, found {len(matches)}')
    if matches[0]['compatibility_range'] != expected:
        raise SystemExit(f'portfolio relationship {key} must declare {expected}')

print(f"Portfolio relationships: PASS ({len(relationships)} declarations; reviewed TSMM/TIS baselines current)")
