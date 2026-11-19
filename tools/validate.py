#!/usr/bin/env python3
"""UL-xDFD v1.0 AI research starter structural validator; not a full semantic conformance checker."""
import yaml,json,sys
from jsonschema import Draft202012Validator
m=yaml.safe_load(open(sys.argv[1],encoding='utf8'))
s=json.load(open(sys.argv[2],encoding='utf8'))
errs=[str(e) for e in Draft202012Validator(s).iter_errors(m)]
nodes={n['id']:n for n in m.get('nodes',[])}
edgeids={e['id'] for e in m.get('edges',[])}
scids={x['id'] for x in m.get('scenarios',[])}
phaseids={x['id'] for x in m.get('phases',[])}
evidids={x['id'] for x in m.get('evidence',[])}
for e in m.get('edges',[]):
 if e.get('source') not in nodes or e.get('target') not in nodes:errs.append('Dangling '+e['id'])
for a in m.get('annotations',[]):
 if a.get('target_id') not in set(nodes)|edgeids:errs.append('Bad annotation target '+a['id'])
 if a.get('scope',{}).get('scenario_id') not in scids:errs.append('Bad scenario '+a['id'])
 if a.get('scope',{}).get('phase_id') and a['scope']['phase_id'] not in phaseids:errs.append('Bad phase '+a['id'])
 if a['status']=='observed' and not a['evidence_refs']:errs.append('Observed without evidence '+a['id'])
 for e in a['evidence_refs']:
  if e not in evidids:errs.append('Missing evidence '+a['id'])
 if a['datatype'] in ('number','integer') and not a.get('unit'):errs.append('Missing numeric unit '+a['id'])
for c in m.get('constraints',[]):
 if c.get('scenario_id') not in scids:errs.append('Bad constraint scenario')
 for x in c.get('target_ids',[]):
  if x not in set(nodes)|edgeids:errs.append('Bad constraint target '+x)
if errs:
 print('FAIL',len(errs),'issues');print('\n'.join(errs));sys.exit(1)
print('PASS: structural schema, graph IDs, annotation refs, observed-evidence checks, basic units')
print('NOT CHECKED: AI policy truth, prompt security, agent termination, costs, cloud pricing, readiness validity')
