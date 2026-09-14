#!/usr/bin/env python3
import hashlib, json, subprocess
from pathlib import Path
import jsonschema
root = Path(__file__).resolve().parents[1]
original = (root / "catalogue.json").read_bytes()
catalogue = json.loads(original)
schema = json.loads((root / "schemas/skill-collection.schema.json").read_text())
jsonschema.Draft202012Validator(schema).validate(catalogue)
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
