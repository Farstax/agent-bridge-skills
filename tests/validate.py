#!/usr/bin/env python3
"""Deterministic validation for the agent-bridge-skills catalogue.

Checks, per AGENTS.md:
  - catalog.yaml and every pack.yaml / skill.yaml is schema-valid
  - every referenced Skill/path exists
  - every SKILL.md has minimal required frontmatter
  - every upstream-derived Skill has repository + exact commit + licence + notice,
    and the declared attribution.notice path actually resolves inside the repo
  - notices cover third-party imports
  - no secret values are present
  - pack ids / Skill ids are unique
  - catalogue references resolve
  - pack-level dependencies/secrets/effects are consistent with the union of
    what the pack's member Skills actually declare (pack metadata does not
    drift from Skill metadata)
"""
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


def load_json(path: Path):
    with path.open() as f:
        return json.load(f)


def load_schema_validator(path: Path) -> Draft202012Validator:
    schema = load_json(path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


CATALOG_SCHEMA = load_schema_validator(ROOT / "schemas" / "catalog.schema.json")
PACK_SCHEMA = load_schema_validator(ROOT / "schemas" / "pack.schema.json")
SKILL_SCHEMA = load_schema_validator(ROOT / "schemas" / "skill.schema.json")

COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")

# Heuristic secret-value patterns. skill.yaml/pack.yaml only ever declare
# secret *names*; these patterns catch an accidentally-committed value.
SECRET_VALUE_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9]{16,}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
]


def check_no_secret_values() -> None:
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(errors="ignore")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in SECRET_VALUE_PATTERNS:
            if pattern.search(text):
                fail(f"possible committed secret value in {path.relative_to(ROOT)}")


def check_skill_md(skill_dir: Path, skill_id: str) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"{skill_id}: missing SKILL.md at {skill_md.relative_to(ROOT)}")
        return
    text = skill_md.read_text()
    if not text.startswith("---\n"):
        fail(f"{skill_id}: SKILL.md must start with YAML frontmatter")
        return
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{skill_id}: SKILL.md frontmatter is not closed")
        return
    frontmatter_raw = text[4:end]
    try:
        frontmatter = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError as exc:
        fail(f"{skill_id}: SKILL.md frontmatter is not valid YAML ({exc})")
        return
    if not isinstance(frontmatter, dict):
        fail(f"{skill_id}: SKILL.md frontmatter must be a mapping")
        return
    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not name or not isinstance(name, str):
        fail(f"{skill_id}: SKILL.md frontmatter missing non-empty 'name'")
    elif name != skill_id:
        fail(f"{skill_id}: SKILL.md frontmatter name '{name}' does not match skill id")
    if not description or not isinstance(description, str) or not description.strip():
        fail(f"{skill_id}: SKILL.md frontmatter missing non-empty 'description'")
    body = text[end + 4:]
    if len(body.strip()) < 50:
        fail(f"{skill_id}: SKILL.md body looks too thin to be a real Skill")


def check_attribution_notice(skill_path: Path, skill_id: str, notice_rel: str) -> None:
    """Resolve attribution.notice relative to the Skill dir; it must exist and
    stay inside the repository (no ../.. escape past ROOT)."""
    candidate = (skill_path / notice_rel).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        fail(f"{skill_id}: attribution.notice '{notice_rel}' resolves outside the repository")
        return
    if not candidate.is_file():
        fail(f"{skill_id}: attribution.notice '{notice_rel}' does not resolve to an existing file")


def check_skill(pack_dir: Path, pack_id: str, skill_ref: dict, notice_text: str) -> dict | None:
    skill_id = skill_ref["id"]
    skill_path = pack_dir / skill_ref["path"]
    if not skill_path.is_dir():
        fail(f"{pack_id}/{skill_id}: referenced path does not exist: {skill_path.relative_to(ROOT)}")
        return None

    check_skill_md(skill_path, skill_id)

    skill_yaml_path = skill_path / "skill.yaml"
    if not skill_yaml_path.exists():
        fail(f"{pack_id}/{skill_id}: missing skill.yaml")
        return None

    data = load_yaml(skill_yaml_path)
    schema_errors = sorted(SKILL_SCHEMA.iter_errors(data), key=lambda e: e.path)
    for err in schema_errors:
        fail(f"{pack_id}/{skill_id}: skill.yaml schema error at {list(err.path)}: {err.message}")

    if data.get("id") != skill_id:
        fail(f"{pack_id}/{skill_id}: skill.yaml id '{data.get('id')}' does not match pack.yaml reference")

    origin = data.get("origin", {})
    origin_type = origin.get("type")
    if origin_type in ("adapted-upstream", "vendored-upstream"):
        upstream = origin.get("upstream", {})
        commit = upstream.get("commit", "")
        if not COMMIT_RE.match(commit):
            fail(f"{pack_id}/{skill_id}: upstream.commit must be an exact 40-char commit SHA, got {commit!r}")
        for field in ("repository", "path", "license"):
            if not upstream.get(field):
                fail(f"{pack_id}/{skill_id}: upstream.{field} is required for {origin_type} Skills")
        if not origin.get("importedAt") or not origin.get("lastUpstreamReview"):
            fail(f"{pack_id}/{skill_id}: importedAt and lastUpstreamReview are required for {origin_type} Skills")
        notice_rel = data.get("attribution", {}).get("notice")
        if not notice_rel:
            fail(f"{pack_id}/{skill_id}: {origin_type} Skill must set attribution.notice")
        else:
            check_attribution_notice(skill_path, f"{pack_id}/{skill_id}", notice_rel)
            if skill_id not in notice_text and upstream.get("path", "") not in notice_text:
                fail(f"{pack_id}/{skill_id}: not referenced in the pack's NOTICE.md")
    elif origin_type == "farstax-authored":
        if "upstream" in origin:
            fail(f"{pack_id}/{skill_id}: farstax-authored Skill must not declare an upstream block")
    else:
        fail(f"{pack_id}/{skill_id}: invalid origin.type {origin_type!r}")

    for eval_path in data.get("evals", []):
        if not (skill_path / eval_path).exists():
            fail(f"{pack_id}/{skill_id}: eval path does not exist: {eval_path}")

    return data


def check_pack_aggregates(pack_id: str, pack_data: dict, skill_datas: list[dict]) -> None:
    """Pack-level dependencies/secrets/effects must not drift from what the
    pack's Skills actually declare. Skill metadata is canonical; the pack
    manifest is a summary that must agree with it exactly, so an Agent Bridge
    install-preview reading only pack.yaml sees the true dependency surface."""
    derived_services: set[str] = set()
    derived_external_write = False
    derived_financial_spend = False
    derived_external_read = False
    derived_secret_names: set[str] = set()

    for skill in skill_datas:
        deps = skill.get("dependencies", {})
        for svc in deps.get("externalServices", []):
            derived_services.add(svc["id"])
        for mcp in deps.get("mcp", []):
            derived_services.add(mcp["id"])
        effects = skill.get("effects", {})
        derived_external_write = derived_external_write or bool(effects.get("externalWrite"))
        derived_financial_spend = derived_financial_spend or bool(effects.get("financialSpend"))
        if effects.get("level") != "local-read-only" or deps.get("externalServices") or deps.get("mcp"):
            derived_external_read = True
        for secret in skill.get("secrets", []):
            derived_secret_names.add(secret["name"])

    declared_services = set(pack_data.get("dependencies", {}).get("externalServices", []))
    if declared_services != derived_services:
        missing = derived_services - declared_services
        extra = declared_services - derived_services
        detail = []
        if missing:
            detail.append(f"missing from pack.yaml: {sorted(missing)}")
        if extra:
            detail.append(f"declared in pack.yaml but not used by any Skill: {sorted(extra)}")
        fail(f"{pack_id}: pack.yaml dependencies.externalServices disagrees with its Skills ({'; '.join(detail)})")

    declared_secret_names = {s["name"] for s in pack_data.get("secrets", [])}
    if declared_secret_names != derived_secret_names:
        fail(
            f"{pack_id}: pack.yaml secrets {sorted(declared_secret_names)} disagrees with "
            f"Skill-declared secrets {sorted(derived_secret_names)}"
        )

    effects = pack_data.get("effects", {})
    if bool(effects.get("externalWrite")) != derived_external_write:
        fail(f"{pack_id}: pack.yaml effects.externalWrite disagrees with its Skills (expected {derived_external_write})")
    if bool(effects.get("financialSpend")) != derived_financial_spend:
        fail(f"{pack_id}: pack.yaml effects.financialSpend disagrees with its Skills (expected {derived_financial_spend})")
    if bool(effects.get("externalRead")) != derived_external_read:
        fail(f"{pack_id}: pack.yaml effects.externalRead disagrees with its Skills (expected {derived_external_read})")


def check_pack(pack_ref: dict) -> None:
    pack_yaml_path = ROOT / pack_ref["path"]
    if not pack_yaml_path.exists():
        fail(f"catalog.yaml references missing pack manifest: {pack_ref['path']}")
        return
    pack_dir = pack_yaml_path.parent
    data = load_yaml(pack_yaml_path)

    schema_errors = sorted(PACK_SCHEMA.iter_errors(data), key=lambda e: e.path)
    for err in schema_errors:
        fail(f"{pack_ref['id']}: pack.yaml schema error at {list(err.path)}: {err.message}")

    if data.get("id") != pack_ref["id"]:
        fail(f"pack.yaml id '{data.get('id')}' does not match catalog.yaml entry '{pack_ref['id']}'")

    notice_path = pack_dir / "NOTICE.md"
    notice_text = notice_path.read_text() if notice_path.exists() else ""

    skill_ids: list[str] = []
    skill_datas: list[dict] = []
    for skill_ref in data.get("skills", []):
        skill_data = check_skill(pack_dir, data.get("id", pack_ref["id"]), skill_ref, notice_text)
        skill_ids.append(skill_ref["id"])
        if skill_data is not None:
            skill_datas.append(skill_data)

    if len(skill_ids) != len(set(skill_ids)):
        fail(f"{pack_ref['id']}: duplicate Skill ids within pack: {skill_ids}")

    if len(skill_datas) == len(skill_ids):
        check_pack_aggregates(pack_ref["id"], data, skill_datas)

    for test_path in data.get("tests", []):
        if not (ROOT / test_path).exists():
            fail(f"{pack_ref['id']}: referenced test path does not exist: {test_path}")

    for readme in ("README.md",):
        if not (pack_dir / readme).exists():
            fail(f"{pack_ref['id']}: missing {readme}")


def main() -> int:
    catalog_path = ROOT / "catalog.yaml"
    catalog = load_yaml(catalog_path)

    schema_errors = sorted(CATALOG_SCHEMA.iter_errors(catalog), key=lambda e: e.path)
    for err in schema_errors:
        fail(f"catalog.yaml schema error at {list(err.path)}: {err.message}")

    pack_ids = [p["id"] for p in catalog.get("packs", [])]
    if len(pack_ids) != len(set(pack_ids)):
        fail(f"duplicate pack ids in catalog.yaml: {pack_ids}")

    for pack_ref in catalog.get("packs", []):
        check_pack(pack_ref)

    check_no_secret_values()

    for required in ("AGENTS.md", "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "catalog.yaml"):
        if not (ROOT / required).exists():
            fail(f"missing required top-level file: {required}")

    if errors:
        print(f"FAILED — {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("OK — catalogue, packs, and Skills validate cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
