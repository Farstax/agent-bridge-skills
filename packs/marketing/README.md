# Marketing pack

Strategy, acquisition, conversion, distribution, and measurement capabilities
for a resident business agent. Version `0.2.0`, installable through Agent
Bridge's Skill Pack mechanism (`Farstax/agent-bridge#703`) — see the top-level
`README.md` for install commands.

## Flow

```
Research
  ↓
Positioning
  ↓
Offer
  ↓
Brand / creative direction
  ↓
Acquisition ── SEO / GEO · content ideas · paid media audit + operation
  ↓
Conversion ── landing-page copy · lead magnets · email sequences
  ↓
Distribution ── content atomisation · newsletters
  ↓
Measurement ── GA4 · Search Console · ad performance
  ↓
Campaign review → next hypothesis
```

## Skills

| Skill | Origin | Job |
|---|---|---|
| `market-research` | Farstax-authored | Turn public signal (reviews, forums, competitor pages) into named pain points and demand evidence. |
| `positioning` | Farstax-authored | Find a defensible market position and the angle that makes it obvious. |
| `offer-design` | Farstax-authored | Design a specific, priced offer with real risk reversal. |
| `brand-voice` | Farstax-authored | Define and enforce one consistent, human brand voice. |
| `creative-strategy` | Farstax-authored | Define visual/creative direction before any asset is produced. |
| `lead-magnets` | Farstax-authored | Design a narrow, high-value free asset that leads to the core offer. |
| `conversion-copy` | Farstax-authored | Write landing-page and direct-response copy grounded in the offer and positioning. |
| `email-sequences` | Farstax-authored | Build welcome, nurture, launch, and cart-recovery email sequences. |
| `newsletters` | Farstax-authored | Run a recurring newsletter as a relationship and distribution asset. |
| `content-atomisation` | Farstax-authored | Turn one long-form asset into platform-native distribution pieces. |
| `campaign-review` | Farstax-authored | Turn real performance data into one next experiment. |
| `seo-analysis` | NotFair-derived | Full technical + content SEO audit against live Search Console and page-performance data. |
| `keyword-research` | NotFair-derived | Seed-driven keyword and topic-cluster discovery. |
| `geo-optimizer` | NotFair-derived | Audit and improve content for citation in AI answer engines. |
| `content-planner` | NotFair-derived | Turn Search Console demand data into a dated content calendar. |
| `search-console` | NotFair-derived | Query live Google Search Console performance and indexing data. |
| `google-analytics` | NotFair-derived | Query live GA4 traffic, acquisition, and conversion data. |
| `google-ads-audit` | NotFair-derived | Read-only Google Ads account health audit. |
| `google-ads-manage` | NotFair-derived | Operate an already-authorized Google Ads account, including supported bid, budget, targeting and campaign mutations. |
| `meta-ads-audit` | NotFair-derived | Read-only Meta (Facebook/Instagram) Ads account health audit. |
| `meta-ads-manage` | NotFair-derived | Operate an already-authorized Meta Ads account, including supported budget, delivery and campaign mutations. |
| `paid-ads-review` | NotFair-derived | Read-only cross-channel paid-media performance review. |

## Provenance

Farstax-authored Skills are modernised from Farstax's private
`nickconstantinou/antigravity-marketing` Antigravity workspace. Modernisation
removed:

- fixed send times, hardcoded model/provider choices, and named third-party
  tools (Exa, Firecrawl, Playwright, specific image generators) — Skills now
  state the evidence or capability required instead;
- manufactured urgency and fake scarcity language ("beta pricing ends in 48
  hours", "this goes away soon");
- "twist the knife" and other manipulative persuasion instructions;
- unsupported "vibe" statistics and unverifiable claims.

What was kept: specific offers, a consistent human voice, channel-native
distribution, measurable goals, and an evidence-led feedback loop from real
campaign performance to the next hypothesis (`campaign-review`, modernised
from the old "Echo Loop" retrospective idea).

NotFair-derived Skills are adapted from
[`nowork-studio/notfair-plugin`](https://github.com/nowork-studio/notfair-plugin)
at commit `daf87d3d4c985fa34ff7843aa570bc8c0d656ec2` (MIT licence, verified at
that commit). See `NOTICE.md` and each Skill's entry in the repository root `catalogue.json` for exact
per-Skill provenance.

## Write-capable scope (v0.2.0)

Version 0.2 adds the two smallest operational extensions to the existing ad
audits: `google-ads-manage` and `meta-ads-manage`. They can perform supported
live mutations, including spend-affecting changes, **only through authority
already granted by the workspace owner and connected account/tool**.

Installing the pack does not authorize an ad account, widen OAuth scope,
change an account role, create a budget, or add a Farstax-specific spend
approval system. Account permissions, configured budgets/limits, and native
tool/service controls remain authoritative. If a requested write is denied or
unavailable, these Skills stop and return the exact proposed change rather
than trying to obtain or bypass broader authority.

The pack still deliberately omits NotFair's broader mutation surface — for
example paid-ad launch/setup/creative Skills and additional ad platforms —
until there is a concrete use case that justifies adding them. The goal is a
curated operational set, not a mirror of every upstream Skill.

## External services

No Skill in this pack authorizes an external account on its own. Several
Skills can optionally use NotFair's hosted MCP, or Google's own APIs, for live
data and supported writes — see `dependencies.externalServices` /
`dependencies.hostedMcps` in each Skill's `dependencies` in `catalogue.json`.
The operator must connect and authorize those services separately; installing
this pack does not do it for them.
