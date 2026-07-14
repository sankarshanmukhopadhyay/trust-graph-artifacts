#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in [root/'patterns/delegation-lineage-envelope/package.json',root/'patterns/delegation-lineage-envelope/constraints.json',root/'patterns/delegation-lineage-envelope/evidence.json',root/'profiles/delegation-first-governance-profile/package.json']:
    try:
        json.loads(p.read_text())
    except Exception as e:
        errors.append(f'{p}: {e}')
cases=yaml.safe_load((root/'validation/delegation-lineage-test-cases.yaml').read_text())
required={'valid-linear-chain','invalid-scope-expansion','invalid-principal-substitution','invalid-broken-lineage','invalid-domain-translation-amplification','invalid-aggregation-amplification','invalid-refresh-renegotiation','invalid-partial-revocation'}
found={x['id'] for x in cases['cases']}
if required-found:
    errors.append('missing test cases: '+', '.join(sorted(required-found)))
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Delegation lineage validation passed.')
