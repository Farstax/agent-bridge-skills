---
name: brand-voice
description: Define one consistent, human brand voice and use it as a filter for every other text-generation Skill in this pack. Use once per brand/project, or whenever asked to define tone, voice, or style guide, or to check a draft against the existing voice.
---

# Brand Voice

## Job

Define a specific, human voice for a brand and give every other writing Skill
in this pack a concrete standard to write and check against.

## Trigger

Run once per brand or project to define the voice profile. Re-run the check
step against any draft from `conversion-copy`, `email-sequences`,
`newsletters`, or `content-atomisation`.

## Required inputs

- Any existing brand material (past copy, About page, founder's own words) —
  prefer deriving voice from real examples over inventing one.
- If no existing material exists, ask the operator to describe how they'd
  explain the product to a friend.

## Method

1. Derive a small number of concrete, checkable voice attributes from real
   examples: sentence-length pattern, vocabulary register, what the brand
   never says. Avoid archetypes that aren't grounded in the operator's actual
   material.
2. Build a short banned/avoid list specific to this brand's actual bad habits
   (jargon it currently overuses), not a generic industry list.
3. State the check protocol as questions a reviewer could answer without
   guessing: does this sound like something a specific named person would
   say; does the first paragraph earn its place; is there a concrete claim
   instead of a vague one.

## Evidence requirements

Voice attributes must be traceable to supplied examples or the operator's own
description. Do not assign a voice archetype the operator hasn't validated.

## Outputs

A voice profile: 3-5 concrete attributes, an avoid-list, and a short
checklist other Skills or a human reviewer can apply to a draft.

## Failure / insufficient evidence

If no brand material and no operator description are available, ask for one
rather than defaulting to an invented persona.

## Dependencies and effects

No external service required. Local reasoning over supplied material.

See `skill.yaml` for machine-readable metadata.
