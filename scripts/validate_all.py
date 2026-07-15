#!/usr/bin/env python3
import subprocess,json,datetime,pathlib,sys
checks=[('packages',['python','scripts/validate_tsmm_native.py']),('authority-envelopes',['python','scripts/validate_authority_envelopes.py']),('delegation-lineage',['python','scripts/validate_delegation_lineage.py']),('receipts',['python','scripts/validate_receipts.py']),('tis-alignment',['python','scripts/validate_tis_alignment.py']),('docs',['python','scripts/validate_docs_site.py']),('governance',['python','scripts/validate_repository_governance.py']),('relationships',['python','scripts/validate_portfolio_relationships.py'])]
out=[]
for i,c in checks:
 p=subprocess.run(c,text=True,capture_output=True);out.append({'id':i,'status':'pass' if p.returncode==0 else 'fail','detail':(p.stdout+p.stderr).strip()[-1000:]});print(f'{i}: {out[-1]["status"]}');
 if p.returncode:break
pathlib.Path('artifacts/validation').mkdir(parents=True,exist_ok=True);ev={'repository':'trust-graph-artifacts','repositoryVersion':pathlib.Path('VERSION').read_text().strip(),'commit':'working-tree','validationProfile':'repository-full','executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':out,'summary':{'passed':sum(x['status']=='pass' for x in out),'failed':sum(x['status']=='fail' for x in out),'skipped':0},'limitations':['Repository validation is not external certification.']};pathlib.Path('artifacts/validation/latest.json').write_text(json.dumps(ev,indent=2)+'\n');sys.exit(1 if ev['summary']['failed'] else 0)
