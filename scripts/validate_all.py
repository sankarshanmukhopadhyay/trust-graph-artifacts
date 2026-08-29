#!/usr/bin/env python3
import subprocess, json, datetime, pathlib, sys, os

PYTHON = sys.executable
checks = [
    ('packages',[PYTHON,'scripts/validate_tsmm_native.py']),
    ('tsmm-alignment',[PYTHON,'scripts/validate_tsmm_alignment.py']),
    ('arpa-alignment',[PYTHON,'scripts/validate_arpa_alignment.py']),
    ('authority-envelopes',[PYTHON,'scripts/validate_authority_envelopes.py']),
    ('delegation-lineage',[PYTHON,'scripts/validate_delegation_lineage.py']),
    ('receipts',[PYTHON,'scripts/validate_receipts.py']),
    ('tis-alignment',[PYTHON,'scripts/validate_tis_alignment.py']),
    ('tsms-golden-path',[PYTHON,'scripts/validate_tsms_golden_path.py']),
    ('assurance-cases',[PYTHON,'scripts/validate_assurance_cases.py']),
    ('publication-provenance',[PYTHON,'scripts/validate_publication_surfaces.py']),
    ('docs',[PYTHON,'scripts/validate_docs_site.py']),
    ('governance',[PYTHON,'scripts/validate_repository_governance.py']),
    ('relationships',[PYTHON,'scripts/validate_portfolio_relationships.py'])
]
out=[]
for check_id, command in checks:
    proc=subprocess.run(command,text=True,capture_output=True)
    out.append({'id':check_id,'status':'pass' if proc.returncode==0 else 'fail','detail':(proc.stdout+proc.stderr).strip()[-2000:]})
    print(f'{check_id}: {out[-1]["status"]}')
    if proc.returncode:
        break
pathlib.Path('artifacts/validation').mkdir(parents=True,exist_ok=True)
ev={
    'repository':'trust-graph-artifacts',
    'repositoryVersion':pathlib.Path('VERSION').read_text().strip(),
    'commit':os.environ.get('GITHUB_SHA','working-tree'),
    'validationProfile':'repository-full',
    'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'checks':out,
    'summary':{
        'passed':sum(x['status']=='pass' for x in out),
        'failed':sum(x['status']=='fail' for x in out),
        'skipped':len(checks)-len(out)
    },
    'limitations':['Repository validation is not external certification.']
}
pathlib.Path('artifacts/validation').mkdir(parents=True,exist_ok=True)
pathlib.Path('artifacts/validation/latest.json').write_text(json.dumps(ev,indent=2)+'\n')
sys.exit(1 if ev['summary']['failed'] else 0)
