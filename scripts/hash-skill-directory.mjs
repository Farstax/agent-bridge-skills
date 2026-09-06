// Ported 1:1 from Farstax/agent-bridge src/skillPacks.ts hashSkillPackDirectorySha256
// (commit c72f5878bf77d52c209bbc47b748b592836744c8). Do not change this algorithm without
// re-checking it against the current upstream implementation — a mismatch here means
// Agent Bridge computes a different content.sha256 than this repo published, and every
// install of the affected Skill fails closed on a checksum mismatch.
import { createHash } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import { join, relative } from "node:path";

export function hashSkillPackDirectorySha256(dir) {
  const hash = createHash("sha256");
  for (const file of files(dir)) {
    hash.update(relative(dir, file).split("\\").join("/"));
    hash.update("\0");
    hash.update(readFileSync(file));
    hash.update("\0");
  }
  return hash.digest("hex");
}

function files(dir) {
  const result = [];
  for (const entry of readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) result.push(...files(full));
    else if (entry.isFile()) result.push(full);
    else throw new Error(`Unsupported Skill Pack filesystem entry: ${full}`);
  }
  return result;
}

// CLI: `node scripts/hash-skill-directory.mjs <dir>` prints the digest to stdout.
// Used by tests/validate.py so hash verification always goes through this one
// implementation rather than a second, potentially-divergent port.
if (import.meta.url === `file://${process.argv[1]}`) {
  const dir = process.argv[2];
  if (!dir) {
    console.error("Usage: node scripts/hash-skill-directory.mjs <dir>");
    process.exit(1);
  }
  console.log(hashSkillPackDirectorySha256(dir));
}
