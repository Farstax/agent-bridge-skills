#!/usr/bin/env python3
import hashlib, json, subprocess
from pathlib import Path
import jsonschema
root = Path(__file__).resolve().parents[1]
original = (root / "catalogue.json").read_bytes()
catalogue = json.loads(original)
schema = json.loads((root / "schemas/skill-collection.schema.json").read_text())
jsonschema.Draft202012Validator(schema).validate(catalogue)

# OSS src/skillCollections.ts::provenance enforces these origin-specific
# constraints in addition to its canonical vendored JSON Schema.
upstream_fields = ('upstreamRepository', 'upstreamRevision', 'upstreamLicense',
                   'noticePath', 'noticeSha256')

def oss_provenance_valid(provenance):
    if provenance['origin'] == 'author-created':
        return (not provenance['modifiedFromUpstream']
                and all(key not in provenance for key in upstream_fields))
    return all(key in provenance for key in upstream_fields)

for skill in catalogue['skills']:
    assert oss_provenance_valid(skill['provenance']), f"incompatible OSS provenance: {skill['id']}"

# Prevent the exact author-created/NOTICE drift that broke unrelated installs.
author_provenance = next(s['provenance'] for s in catalogue['skills']
                         if s['provenance']['origin'] == 'author-created')
for key, value in [('noticePath', 'NOTICE.md'), ('noticeSha256', '0' * 64),
                   ('upstreamRepository', 'https://github.com/example/repo')]:
    assert not oss_provenance_valid({**author_provenance, key: value})
assert not oss_provenance_valid({**author_provenance, 'modifiedFromUpstream': True})
adapted_provenance = next(s['provenance'] for s in catalogue['skills']
                          if s['provenance']['origin'] == 'adapted-upstream')
for key in upstream_fields:
    assert not oss_provenance_valid({k: v for k, v in adapted_provenance.items() if k != key})

ids = {skill['id'] for skill in catalogue['skills']}
assert len(ids) == len(catalogue['skills'])
for skill in catalogue['skills']:
    directory = root / skill['content']['path']
    assert directory.is_dir(), f"missing Skill directory: {directory}"
    assert (directory / 'SKILL.md').is_file(), f"missing SKILL.md: {directory}"
    evals = directory / 'evals'
    assert evals.is_dir() and any(evals.glob('*.md')), f"missing eval: {skill['id']}"
    provenance = skill['provenance']
    if provenance.get('noticePath'):
        notice = root / provenance['noticePath']
        assert notice.is_file(), f"missing notice: {skill['id']}"
        assert hashlib.sha256(notice.read_bytes()).hexdigest() == provenance['noticeSha256']
for collection in catalogue['collections']:
    assert collection['skills'], f"empty Collection: {collection['id']}"
    for skill_id in collection['skills']: assert skill_id in ids, f"unknown Skill {skill_id} in Collection {collection['id']}"
revisions = {skill['content']['revision'] for skill in catalogue['skills']}
assert len(revisions) == 1, "catalogue must pin one exact source revision"
subprocess.run(['node', 'scripts/build-catalogue.mjs', '--revision', next(iter(revisions))], cwd=root, check=True)
assert (root / 'catalogue.json').read_bytes() == original, "catalogue is not reproducible from source at its pinned revision"
print(f"validated {len(catalogue['skills'])} Skills and {len(catalogue['collections'])} Collections")
