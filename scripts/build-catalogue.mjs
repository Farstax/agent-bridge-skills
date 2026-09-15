#!/usr/bin/env node
import { createHash } from "node:crypto";
import { existsSync, readFileSync, readdirSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
const args = process.argv.slice(2);
const index = args.indexOf("--revision");
const revision = index >= 0 ? args[index + 1] : null;
if (!revision || !/^[0-9a-f]{40}$/i.test(revision)) { console.error("usage: node scripts/build-catalogue.mjs --revision <40-char-commit-sha>"); process.exit(1); }
const source = JSON.parse(readFileSync("catalogue.source.json", "utf8"));
const files = (dir) => {
  const out = [];
  for (const entry of readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...files(full)); else if (entry.isFile()) out.push(full);
  }
  return out;
};
const hashDirectory = (dir) => {
  const hash = createHash("sha256");
  for (const file of files(dir)) { hash.update(path.relative(dir, file).split(path.sep).join("/")); hash.update("\0"); hash.update(readFileSync(file)); hash.update("\0"); }
  return hash.digest("hex");
};
const fileHash = (file) => createHash("sha256").update(readFileSync(file)).digest("hex");
const skills = source.skills.map((skill) => {
  if (!existsSync(skill.content.path) || !statSync(skill.content.path).isDirectory()) throw new Error(`missing Skill directory: ${skill.content.path}`);
  const provenance = { ...skill.provenance };
  if (provenance.noticePath) { if (!existsSync(provenance.noticePath)) throw new Error(`missing notice: ${provenance.noticePath}`); provenance.noticeSha256 = fileHash(provenance.noticePath); }
  return { id: skill.id, description: skill.description, content: { ...skill.content, revision, sha256: hashDirectory(skill.content.path) }, provenance };
});
writeFileSync("catalogue.json", JSON.stringify({ schemaVersion: 2, catalogueId: source.catalogueId, skills, collections: source.collections }, null, 2) + "\n");
