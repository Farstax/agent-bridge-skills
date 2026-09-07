#!/usr/bin/env node
// Generates catalogue.json (the schemas/skill-pack.schema.json v1 contract Agent Bridge
// fetches from https://raw.githubusercontent.com/Farstax/agent-bridge-skills/main/catalogue.json)
// from the metadata below. This script is the source of truth for pack/Skill metadata;
// catalogue.json is a generated, checked-in build artifact.
//
// Usage:
//   node scripts/build-catalogue.mjs --revision <40-char commit SHA> [--out catalogue.json]
//
// --revision must be the exact commit SHA (already pushed/reachable on the remote) whose
// tree contains the Skill directories referenced below unchanged. Content is hashed from
// the local working tree, so the working tree must match that commit's content exactly
// for the referenced Skill paths and notice files.
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
import { hashSkillPackDirectorySha256 } from "./hash-skill-directory.mjs";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const REPOSITORY = "https://github.com/Farstax/agent-bridge-skills";
const NOTFAIR_COMMIT = "daf87d3d4c985fa34ff7843aa570bc8c0d656ec2";
const NOTFAIR_REPOSITORY = "https://github.com/nowork-studio/notfair-plugin";
const HOSTS = ["codex", "claude", "agy"];

function fileSha256(path) {
  return createHash("sha256").update(readFileSync(path)).digest("hex");
}

function farstaxSkill({ id, description, effects, approval, tests }) {
  return {
    id,
    description,
    supportedHosts: HOSTS,
    dependencies: emptyDependencies(),
    capabilities: { effects, approval },
    tests,
    provenance: {
      origin: "farstax-authored",
      modifiedFromUpstream: false,
      lastReviewed: "2026-09-06",
    },
  };
}

function notfairSkill({ id, description, effects, approval, tests, upstreamPath, dependencies }) {
  return {
    id,
    description,
    supportedHosts: HOSTS,
    dependencies: dependencies ?? emptyDependencies(),
    capabilities: { effects, approval },
    tests,
    provenance: {
      origin: "adapted-upstream",
      upstreamRepository: NOTFAIR_REPOSITORY,
      upstreamRevision: NOTFAIR_COMMIT,
      upstreamLicense: "MIT",
      noticePath: "packs/marketing/NOTICE.md",
      lastReviewed: "2026-09-06",
      modifiedFromUpstream: true,
    },
    _upstreamPath: upstreamPath,
  };
}

function emptyDependencies() {
  return { requiredLocal: [], optionalLocal: [], externalServices: [], hostedMcps: [], requiredSecrets: [] };
}

// Derives the pack-level dependencies summary from its resolved Skills so the
// pack manifest can't silently omit a dependency a Skill actually declares —
// this is the exact drift class review already flagged once in this repo.
function aggregateDependencies(resolvedSkills) {
  const byName = (list) => {
    const seen = new Map();
    for (const item of list) if (!seen.has(item.name)) seen.set(item.name, item);
    return [...seen.values()];
  };
  return {
    requiredLocal: byName(resolvedSkills.flatMap((s) => s.dependencies.requiredLocal)),
    optionalLocal: byName(resolvedSkills.flatMap((s) => s.dependencies.optionalLocal)),
    externalServices: byName(resolvedSkills.flatMap((s) => s.dependencies.externalServices)),
    hostedMcps: byName(resolvedSkills.flatMap((s) => s.dependencies.hostedMcps)),
    requiredSecrets: byName(resolvedSkills.flatMap((s) => s.dependencies.requiredSecrets)),
  };
}

function hostedMcp(name, purpose, url) {
  return { hostedMcps: [{ name: "NotFair", purpose, url, authorization: "OAuth" }], requiredLocal: [], optionalLocal: [], externalServices: [], requiredSecrets: [] };
}

const NO_MUTATION_APPROVAL = "None — Skill performs no external mutation or spend; normal tool/account authorization remains authoritative for any live-data connection it uses.";
const DRAFT_APPROVAL = (what) => `Operator reviews and confirms ${what} before it is published or sent anywhere.`;

const skills = [
  // Farstax-authored: strategy, offer, brand, conversion, distribution, review
  farstaxSkill({
    id: "market-research", description: "Turn public signal into named pain points, demand evidence, and a competitive gap.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL,
    tests: ["packs/marketing/skills/market-research/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "positioning", description: "Define a defensible market position and the angle that makes it obvious.",
    effects: ["local-read"], approval: NO_MUTATION_APPROVAL,
    tests: ["packs/marketing/skills/positioning/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "offer-design", description: "Design a specific, priced offer with real risk reversal.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("the price, guarantee, and bonus terms"),
    tests: ["packs/marketing/skills/offer-design/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "brand-voice", description: "Define one consistent, human brand voice as a filter for other writing Skills.",
    effects: ["local-read"], approval: NO_MUTATION_APPROVAL,
    tests: ["packs/marketing/skills/brand-voice/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "creative-strategy", description: "Define visual and creative direction grounded in brand voice and audience.",
    effects: ["local-read"], approval: NO_MUTATION_APPROVAL,
    tests: ["packs/marketing/skills/creative-strategy/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "lead-magnets", description: "Design a narrow, high-value free asset that leads to the core offer.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("the drafted asset and landing copy"),
    tests: ["packs/marketing/skills/lead-magnets/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "conversion-copy", description: "Write evidence-led landing-page and direct-response copy grounded in the offer and brand voice.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("all factual claims, pricing, and guarantees"),
    tests: ["packs/marketing/skills/conversion-copy/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "email-sequences", description: "Design welcome, nurture, launch, and recovery email sequences without manufactured pressure.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("sequence content and any claim, deadline, or bonus"),
    tests: ["packs/marketing/skills/email-sequences/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "newsletters", description: "Plan and draft a recurring newsletter with one clear goal per issue.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("the issue and any cited number or result"),
    tests: ["packs/marketing/skills/newsletters/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "content-atomisation", description: "Turn one long-form asset into platform-native distribution pieces.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("each piece"),
    tests: ["packs/marketing/skills/content-atomisation/evals/eval-1.md"],
  }),
  farstaxSkill({
    id: "campaign-review", description: "Diagnose campaign performance and check drafted assets against brand voice and offer.",
    effects: ["local-read"], approval: NO_MUTATION_APPROVAL,
    tests: ["packs/marketing/skills/campaign-review/evals/eval-1.md"],
  }),

  // NotFair-derived: read-only SEO/GEO/analytics/paid-media audit layer
  notfairSkill({
    id: "seo-analysis", description: "Full technical and content SEO audit using live Search Console and page-performance data.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "seo/seo-analysis",
    tests: ["packs/marketing/skills/seo-analysis/evals/eval-1.md"],
    dependencies: hostedMcp("google-search-console + google-pagespeed-insights", "Optional hosted connector for Search Console/PageSpeed access instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "keyword-research", description: "Seed-driven keyword discovery, clustering, and prioritization.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "seo/keyword-research",
    tests: ["packs/marketing/skills/keyword-research/evals/eval-1.md"],
    dependencies: hostedMcp("keyword-data-provider", "Optional hosted connector for keyword volume/difficulty data instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "geo-optimizer", description: "Audit and restructure content for citability by AI answer engines.",
    effects: ["draft-write"], approval: DRAFT_APPROVAL("rewritten content"), upstreamPath: "seo/geo-optimizer",
    tests: ["packs/marketing/skills/geo-optimizer/evals/eval-1.md"],
  }),
  notfairSkill({
    id: "content-planner", description: "Build a dated content calendar from real Search Console demand data.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "seo/content-planner",
    tests: ["packs/marketing/skills/content-planner/evals/eval-1.md"],
    dependencies: hostedMcp("google-search-console", "Optional hosted connector for Search Console access instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "search-console", description: "Query live Search Console performance, indexing, and sitemap status.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "analytics/search-console",
    tests: ["packs/marketing/skills/search-console/evals/eval-1.md"],
    dependencies: hostedMcp("google-search-console", "Optional hosted connector for Search Console access instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "google-analytics", description: "Query live GA4 traffic, acquisition, engagement, and conversion data.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "analytics/google-analytics",
    tests: ["packs/marketing/skills/google-analytics/evals/eval-1.md"],
    dependencies: hostedMcp("google-analytics", "Optional hosted connector for GA4 access instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "google-ads-audit", description: "Read-only Google Ads account health audit and business-context capture.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "google-ads/audit",
    tests: ["packs/marketing/skills/google-ads-audit/evals/eval-1.md"],
    dependencies: hostedMcp("google-ads", "Optional hosted connector for Google Ads access instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "meta-ads-audit", description: "Read-only Meta (Facebook + Instagram) Ads account health audit and business-context capture.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "meta-ads/audit",
    tests: ["packs/marketing/skills/meta-ads-audit/evals/eval-1.md"],
    dependencies: hostedMcp("meta-ads", "Optional hosted connector for Meta Ads access instead of a direct API credential.", NOTFAIR_REPOSITORY),
  }),
  notfairSkill({
    id: "paid-ads-review", description: "Read-only, evidence-based cross-channel paid-media performance review.",
    effects: ["external-read"], approval: NO_MUTATION_APPROVAL, upstreamPath: "paid-ads/paid-ads-review",
    tests: ["packs/marketing/skills/paid-ads-review/evals/eval-1.md"],
    dependencies: hostedMcp("google-ads + meta-ads", "Optional hosted connector for cross-channel ad-platform data instead of direct API credentials.", NOTFAIR_REPOSITORY),
  }),
];

function buildPack(revision) {
  const noticePath = join(repoRoot, "packs", "marketing", "NOTICE.md");
  const noticeSha256 = fileSha256(noticePath);

  const resolvedSkills = skills.map(({ _upstreamPath, ...skill }) => {
    const dir = join(repoRoot, "packs", "marketing", "skills", skill.id);
    const provenance = skill.provenance.origin === "farstax-authored"
      ? skill.provenance
      : { ...skill.provenance, noticeSha256 };
    return {
      id: skill.id,
      description: skill.description,
      content: {
        repository: REPOSITORY,
        revision,
        path: `packs/marketing/skills/${skill.id}`,
        sha256: hashSkillPackDirectorySha256(dir),
      },
      provenance,
      supportedHosts: skill.supportedHosts,
      dependencies: skill.dependencies,
      capabilities: skill.capabilities,
      tests: skill.tests,
    };
  });

  const allEffects = [...new Set(resolvedSkills.flatMap((s) => s.capabilities.effects))];
  const packDependencies = aggregateDependencies(resolvedSkills);

  return {
    id: "marketing",
    displayName: "Marketing",
    description: "Strategy, acquisition, conversion, distribution and marketing measurement capabilities for a resident business agent.",
    version: "0.1.0",
    maintainer: "Farstax",
    license: "MIT",
    categories: ["marketing", "growth"],
    capabilityTags: ["business:marketing", "business:growth"],
    attribution: [NOTFAIR_REPOSITORY, "https://github.com/nickconstantinou/antigravity-marketing"],
    compatibility: { apiVersion: 1, minAgentBridgeVersion: "2026.9.7-2", supportedHosts: HOSTS },
    dependencies: packDependencies,
    capabilities: {
      effects: allEffects,
      approval: "Individual Skill approval requirements apply (see each Skill's capabilities.approval). Installing this pack grants no external account access, OAuth authorization, secret value, or spend/mutation authority on its own.",
    },
    tests: ["tests/validate.py"],
    skills: resolvedSkills,
  };
}

function main() {
  const args = process.argv.slice(2);
  const revisionIndex = args.indexOf("--revision");
  if (revisionIndex === -1 || !args[revisionIndex + 1]) {
    console.error("Usage: node scripts/build-catalogue.mjs --revision <40-char commit SHA> [--out catalogue.json]");
    process.exit(1);
  }
  const revision = args[revisionIndex + 1];
  if (!/^[0-9a-f]{40}$/.test(revision)) {
    console.error(`--revision must be an exact 40-character lowercase commit SHA, got: ${revision}`);
    process.exit(1);
  }
  const outIndex = args.indexOf("--out");
  const out = outIndex === -1 ? join(repoRoot, "catalogue.json") : args[outIndex + 1];

  const catalogue = {
    schemaVersion: 1,
    catalogueId: "farstax-agent-bridge-skills",
    catalogueVersion: "1.0.0",
    packs: [buildPack(revision)],
  };
  writeFileSync(out, `${JSON.stringify(catalogue, null, 2)}\n`);
  console.log(`Wrote ${out} pinned to revision ${revision}`);
}

main();
