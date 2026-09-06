#!/usr/bin/env python3
"""Deterministic validation for catalogue.json, the artifact Agent Bridge fetches
from https://raw.githubusercontent.com/Farstax/agent-bridge-skills/main/catalogue.json.

Checks:
  - catalogue.json validates against the vendored canonical schema
    (schemas/skill-pack.schema.json, copied from Farstax/agent-bridge)
  - every Skill's content.repository/revision/path resolve to a real local directory
    and content.sha256 matches what Agent Bridge's own hashing algorithm computes for it
    (delegated to scripts/hash-skill-directory.mjs — the actual TS algorithm ported to a
    small standalone script — rather than a second, potentially divergent implementation)
  - every upstream-derived Skill's provenance.noticePath exists and its noticeSha256 matches
  - every SKILL.md has minimal required frontmatter
  - pack ids / Skill ids are unique
  - no secret values are present
  - pack-level dependencies/effects are a superset of what member Skills declare (a repo
    curation convention on top of what Agent Bridge itself enforces, so a reader of the pack
    summary doesn't miss a dependency a Skill actually has)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def load_json(path: Path):
    with path.open() as f:
        return json.load(f)


def load_schema_validator(path: Path) -> Draft202012Validator:
    schema = load_json(path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


SCHEMA = load_schema_validator(ROOT / "schemas" / "skill-pack.schema.json")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

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


def file_sha256(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hash_dir_via_node(dir_path: Path) -> str:
    result = subprocess.run(
        ["node", str(ROOT / "scripts" / "hash-skill-directory.mjs"), str(dir_path)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        fail(f"hash-skill-directory.mjs failed for {dir_path}: {result.stderr.strip()}")
        return ""
    return result.stdout.strip()


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
    try:
        frontmatter = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        fail(f"{skill_id}: SKILL.md frontmatter is not valid YAML ({exc})")
        return
    if not isinstance(frontmatter, dict):
        fail(f"{skill_id}: SKILL.md frontmatter must be a mapping")
        return
    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not name or name != skill_id:
        fail(f"{skill_id}: SKILL.md frontmatter name must equal the Skill id (got {name!r})")
    if not description or not str(description).strip():
        fail(f"{skill_id}: SKILL.md frontmatter missing non-empty 'description'")
    if len(text[end + 4:].strip()) < 50:
        fail(f"{skill_id}: SKILL.md body looks too thin to be a real Skill")


def check_skill(pack_id: str, skill: dict) -> None:
    skill_id = skill["id"]
    content = skill["content"]

    if not COMMIT_RE.match(content["revision"]):
        fail(f"{pack_id}/{skill_id}: content.revision must be an exact 40-char commit SHA, got {content['revision']!r}")

    if content["repository"] == "https://github.com/Farstax/agent-bridge-skills":
        skill_dir = ROOT / content["path"]
        if not skill_dir.is_dir():
            fail(f"{pack_id}/{skill_id}: content.path does not exist locally: {content['path']}")
        else:
            check_skill_md(skill_dir, skill_id)
            actual_sha256 = hash_dir_via_node(skill_dir)
            if actual_sha256 and actual_sha256 != content["sha256"]:
                fail(
                    f"{pack_id}/{skill_id}: content.sha256 does not match the current working tree "
                    f"(declared {content['sha256']}, computed {actual_sha256}) — "
                    f"regenerate with scripts/build-catalogue.mjs"
                )

    provenance = skill["provenance"]
    if provenance["origin"] in ("adapted-upstream", "vendored-upstream"):
        upstream_revision = provenance.get("upstreamRevision", "")
        if not COMMIT_RE.match(upstream_revision):
            fail(f"{pack_id}/{skill_id}: provenance.upstreamRevision must be an exact 40-char commit SHA, got {upstream_revision!r}")
        notice_path = provenance.get("noticePath")
        notice_sha256 = provenance.get("noticeSha256")
        if not notice_path or not notice_sha256:
            fail(f"{pack_id}/{skill_id}: {provenance['origin']} Skill must set provenance.noticePath and noticeSha256")
        else:
            resolved = (ROOT / notice_path).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{pack_id}/{skill_id}: provenance.noticePath resolves outside the repository: {notice_path}")
            else:
                if not resolved.is_file():
                    fail(f"{pack_id}/{skill_id}: provenance.noticePath does not exist: {notice_path}")
                elif file_sha256(resolved) != notice_sha256:
                    fail(f"{pack_id}/{skill_id}: provenance.noticeSha256 does not match {notice_path} on disk")

    for test_path in skill.get("tests", []):
        if not (ROOT / test_path).exists():
            fail(f"{pack_id}/{skill_id}: referenced test path does not exist: {test_path}")


def check_pack_aggregates(pack: dict) -> None:
    """Repo curation convention (not enforced by Agent Bridge itself): the pack's
    summary dependencies/effects should not omit anything a member Skill declares,
    so a reader of pack-level metadata alone isn't misled about what it touches."""
    derived_effects: set[str] = set()
    derived_service_names: set[str] = set()
    derived_mcp_names: set[str] = set()
    derived_secret_names: set[str] = set()

    for skill in pack.get("skills", []):
        derived_effects.update(skill["capabilities"]["effects"])
        deps = skill["dependencies"]
        derived_service_names.update(s["name"] for s in deps.get("externalServices", []))
        derived_mcp_names.update(s["name"] for s in deps.get("hostedMcps", []))
        derived_secret_names.update(s["name"] for s in deps.get("requiredSecrets", []))

    pack_effects = set(pack["capabilities"]["effects"])
    missing_effects = derived_effects - pack_effects
    if missing_effects:
        fail(f"{pack['id']}: pack.capabilities.effects is missing effect(s) used by its Skills: {sorted(missing_effects)}")

    pack_deps = pack["dependencies"]
    pack_service_names = {s["name"] for s in pack_deps.get("externalServices", [])}
    pack_mcp_names = {s["name"] for s in pack_deps.get("hostedMcps", [])}
    pack_secret_names = {s["name"] for s in pack_deps.get("requiredSecrets", [])}

    for label, derived, declared in (
        ("externalServices", derived_service_names, pack_service_names),
        ("hostedMcps", derived_mcp_names, pack_mcp_names),
        ("requiredSecrets", derived_secret_names, pack_secret_names),
    ):
        missing = derived - declared
        if missing:
            fail(f"{pack['id']}: pack.dependencies.{label} is missing entr(y/ies) used by its Skills: {sorted(missing)}")


def main() -> int:
    catalogue_path = ROOT / "catalogue.json"
    if not catalogue_path.exists():
        fail("catalogue.json is missing at the repository root")
        print("\n".join(f"  - {e}" for e in errors))
        return 1

    catalogue = load_json(catalogue_path)

    for err in sorted(SCHEMA.iter_errors(catalogue), key=lambda e: e.path):
        fail(f"catalogue.json schema error at {list(err.path)}: {err.message}")

    pack_ids = [p["id"] for p in catalogue.get("packs", [])]
    if len(pack_ids) != len(set(pack_ids)):
        fail(f"duplicate pack ids in catalogue.json: {pack_ids}")

    for pack in catalogue.get("packs", []):
        skill_ids = [s["id"] for s in pack.get("skills", [])]
        if len(skill_ids) != len(set(skill_ids)):
            fail(f"{pack['id']}: duplicate Skill ids: {skill_ids}")
        for skill in pack.get("skills", []):
            check_skill(pack["id"], skill)
        check_pack_aggregates(pack)
        for test_path in pack.get("tests", []):
            if not (ROOT / test_path).exists():
                fail(f"{pack['id']}: referenced pack test path does not exist: {test_path}")

    check_no_secret_values()

    for required in ("AGENTS.md", "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "catalogue.json", "schemas/skill-pack.schema.json"):
        if not (ROOT / required).exists():
            fail(f"missing required top-level file: {required}")

    if errors:
        print(f"FAILED — {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("OK — catalogue.json validates cleanly against the canonical schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
