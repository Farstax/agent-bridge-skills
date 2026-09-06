# Marketing pack

Strategy, acquisition, conversion, distribution, and measurement capabilities
for a resident business agent. Version `0.1.0`, pending Agent Bridge Skill
Pack support (`Farstax/agent-bridge#703`).

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
Acquisition ── SEO / GEO · content ideas · paid media audit
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
| `meta-ads-audit` | NotFair-derived | Read-only Meta (Facebook/Instagram) Ads account health audit. |
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
that commit). See `NOTICE.md` and each Skill's `skill.yaml` for exact
per-Skill provenance.

## Deliberate omissions (v0.1.0)

NotFair ships 45 Skills across SEO, GEO, paid media, and analytics, including
account-mutating and campaign-launch Skills (`google-ads` operate/copy/assets,
`meta-ads-creative`, `paid-ads-optimize`, `paid-ads-launch`, `paid-ads-setup`,
platform Skills for TikTok/X/LinkedIn/Amazon/ChatGPT Ads). This pack imports
only the **read-only audit and analysis** layer for v0.1.0 — nothing here can
change a live ad account, budget, or published page. Write-capable NotFair
Skills are deliberately left out until this pack has explicit
`spend-affecting-write` approval metadata and a real operator approval flow to
attach to them, rather than importing mutation capability with a metadata
schema that has not been exercised yet.

Each of these Skills was individually reviewed against the current NotFair
tree rather than assumed from a fixed list; the selection may change as the
upstream project or this pack evolves.

## External services

No Skill in this pack authorizes an external account on its own. Several
Skills can optionally use NotFair's hosted MCP, or Google's own APIs, for live
data — see `dependencies.externalServices` / `dependencies.mcp` in each
Skill's `skill.yaml`. The operator must connect and authorize those services
separately; installing this pack does not do it for them.
