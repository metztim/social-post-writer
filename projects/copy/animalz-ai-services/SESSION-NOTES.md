# Session Notes: Animalz AI Services Copywriting Process

**Date:** 2026-02-27
**Process:** /copywrite (structured copywriting, 7 phases)
**Status:** Paused at Phase 5 (Selection), pending stakeholder feedback before Phase 6 (Full Copy)

## Files in this project

| File | Purpose |
|---|---|
| state.md | Process state (YAML frontmatter + log) |
| brief.md | Phase 1 output: deliverable, audience, attitude shift, constraints |
| strategy.md | Phase 2 output: core truth, SOCO, SOCA, positioning statement |
| research/competitive-copy-audit.md | Phase 3: 6 AirOps partners + AirOps copy, category clichés, banned words |
| research/voice-of-customer.md | Phase 3: Ty's sales calls + web research VOC |
| variants.md | Phase 4: 54 variants across 11 directions, labeled H/AI |
| exec-summary-draft.md | Stakeholder doc (also pushed to Notion) |
| visual-prompts.md | Nano Banana Pro prompts for 3 visuals (round 2 — text-free photos) |
| SESSION-NOTES.md | This file |

## External references

| Resource | Location |
|---|---|
| **Creative direction doc (Notion)** | `312df6dc-2cc5-81b8-9a12-edee568dfb00` (work workspace) — RENAMED from old services page copy, now holds exec summary with callout styling + images |
| Positioning doc (Notion) | `312df6dc-2cc5-8154-acf7-f2b91d74c1fd` (work workspace) — updated with messaging strategy, audience insights, competitive audit, banned words, VOC |
| Old exec summary (Notion) | `314df6dc-2cc5-81a1-8d78-ec44757fef3d` (Marketing Projects) — superseded by creative direction doc above |
| Earlier services page copy | `/Users/timmetz/Developer/Projects/Animalz/ai-services-business/marketing/services-page-copy.md` |
| Context engineering draft (Notion) | `313df6dc-2cc5-8072-9827-f64b653b6a75` (work workspace) |
| Animalz brand guidelines | `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/docs/Animalz 2025 Brand Guidelines.pdf` |
| Animalz website codebase | `/Users/timmetz/Developer/Projects/Animalz/websites/website-statamic` |
| Nano Banana Pro prompting guide | `~/.claude/research/nano-banana-pro.md` |

## Key decisions and nuances (preserve for next session)

### Core truth — the nuance matters
"Content people who **had to** become AI builders." The "had to" is critical — it communicates conviction, not hobby. They couldn't accept mediocre AI output and had no one else to turn to. Tim and Johnson are both marketers/writers who became AI-native builders — the rare combination exists within each person, not just at the agency level.

### The tension that's actually a strength
The brief says "your content people won't have the skills to build this" but the core truth says "we're content people who did build this." This tension is deliberate and is a strength, not a contradiction. Most content people won't make this leap — it took a specific combination of obsession, builder mentality, and years of pain. The page doesn't need to resolve this tension. The reader will feel it as credibility.

### SOCO is a feeling, not a tagline
"Animalz has already solved the AI content problem you're stuck on." This isn't hero copy — it's the feeling someone should have after reading the page. The one thing stuck in their head when they walk away.

**Tim's feedback (session 2):** The SOCO phrasing "feels off." The underlying takeaway ("they know what they're doing and can solve it for me") is right, but the words need work. The 3-second version ("They've already figured this out — I should just talk to them") is closer to what Tim means. **Revisit in Phase 6.**

### SOCA includes speed
"This is experimental — we're still figuring it out and it'll take a while." This covers both the competence doubt AND the slow-payoff fear. Prospects are allergic to "it takes months to see results" (burned by SEO hedging). Counter with proof of speed that already exists: same-day first drafts, 30-60 minute trending content, iteration within hours.

### Three finalist concepts — standalone, not combined
1. **The Secret** — "Some of our clients won't even tell their board how their content gets made." Strongest single headline. Brand-building. Extends into secrecy/guard/Coke recipe platform. Tim sees real potential in this as a full hero direction, not just a line.
2. **Publish Button** — worn-out button visual + "after six weeks with Animalz." Most distinctive visual. Campaign platform potential. Tim's strongest conviction — "can totally see the concept and lots of possibilities." Can extend into series of content-related physical objects pushed to their limits.
3. **Knowing Which Half** — "Half your content can be written by AI. The trouble is knowing which half." Most strategic. Riffs on classic Wanamaker ad quote. Trust-building with senior decision-makers. **Key insight (session 2):** The headline's power is what it implies — *we* know which half. The reader is stuck; Animalz already has the answer.

Tim's note: these are strong independently and could POTENTIALLY work together, but not necessarily. Combining might weaken each. Present as standalone directions.

### The creativity gap — NEW insight (session 2)
Competitors don't just lack content quality expertise — they lack **creativity**. Everything in the AirOps partner ecosystem looks and sounds the same: tacky, minimalistic, sci-fi aesthetics, same tired words. Animalz can stand out by bringing creativity, strategy, narrative, humor, and a point of view. Being human, risky, bold. The creative direction itself is a competitive advantage, regardless of which concept is chosen. **Tim wants this elevated to the positioning doc as part of the strategy.**

**DONE:** Added to positioning doc (`312df6dc-2cc5-8154-acf7-f2b91d74c1fd`):
- Competitive copy audit findings — new bullet on aesthetic/creative monoculture
- Competitive positioning → "What we are" — new bullet on creative vision/brand thinking

### Important creative threads to preserve
- "You will have some explaining to do when your AI-generated content is this good" — strong variant, related to The Secret concept but distinct. Surprise at end of sentence (Whipple). **Note: "You will" not "You'll" — the uncontracted form has more punch.**
- "This is NOT AI generated" / "This IS AI generated" contrast — clean two-line structure.
- "Others give you demos. We give you deliverables." — strong section header candidate.
- "Do you love debugging complex, unpredictable, moody AI models? We do." — section header for skills gap.
- "Nobody ever got fired for buying AirOps. But that day is not today." — bold AirOps section header. Risks alienating AirOps.
- "From 'will this ever work' to 'how do we keep up?'" — attitude shift in one line, section header.
- Coke recipe / guard the secret direction — Tim thinks this has hero potential, not just proof. "Some clients won't tell their board" + "workflows are the new IP" + "our workflows come with an NDA (not really, but you'll want one)."

### Visual prompts — round 2 approach (session 2)
Round 1 billboard-style images (text baked in) didn't work. Pivoted to:
- **Realistic photographs only** — no text on images
- **Text added as Notion captions** alongside the image
- Each prompt opens with ad concept context so the model understands the story
- Explicit no-text guardrail in every prompt
- Push for theatrical/exaggerated compositions, not subtle details
- **Reference image:** Only page 2 (Colors) of brand guidelines PDF — screenshot it since PDFs can't be attached to Gemini
- **New conversations** for each concept (don't iterate on failed compositions)
- Prompts in `visual-prompts.md`

Key learnings:
- Boardroom (Concept A): first attempt was too realistic/subtle — briefcase invisible. Revised to theatrical: person standing center frame, both hands behind back, exaggerated hiding gesture
- Publish button (Concept B): physical arcade button didn't work → CMS-style rectangular button on screen with cracked/worn screen or worn keyboard key
- Knowing Which Half (Concept C): both screens should look nearly identical (that IS the joke), person in theatrical frustration

### Competitive landscape (key facts)
- All AirOps partners are SEO/AEO monoculture
- TACO and Depends are copy-paste twins (shared template or same parent org)
- GrowthX is most differentiated ($18K/mo visible pricing, "who we're NOT for")
- Nobody in the ecosystem talks about content quality — the lane is wide open
- **Nobody in the ecosystem shows creative thinking either** — tacky, minimalistic, sci-fi aesthetics
- Full banned words list in competitive-copy-audit.md

### Animalz voice reference
- Heading font: ITC Souvenir Std Light (elegant serif)
- Body font: Founders Grotesk Regular (clean sans)
- Primary accent: Purple-500 (#9463EE)
- Critters: playful single-color line drawings
- Vibe: warm, editorial, playful but professional — NOT cold/techy B2B
- Tone: confident without arrogance, concrete metaphors, mix of short punchy and longer explanatory sentences, contractions freely, direct address, storytelling + transparency about trade-offs
- CTAs: soft and conversational ("Let's talk"), not commanding
- Tim's note: current pages are "quite weak" in copy but "general vibe is good" — distinguish from techy/minimal B2B growth engine aesthetic

### Notion page styling (session 2)
The creative direction doc (`312df6dc-2cc5-81b8-9a12-edee568dfb00`) was styled with callout blocks:
- 📋 Brief → gray callout
- 🎯 SOCO → green callout
- 🚫 SOCA → red callout
- 💰 Service tiers → gray callout
- 📊 Proof points → blue callout
- 💬 Open questions → yellow callout
Tim added images to all three concepts and a link to the positioning doc in the Brief callout.

### Notion API tip
To find inline comments (discussion threads) on a Notion page:
- `get-comments <page_id>` only returns page-level comments (sidebar)
- `get-comments <block_id>` returns inline discussions on that specific block
- Must iterate through all block IDs to find all comments

### Next steps
1. ~~Update positioning doc with creativity gap insight~~ **DONE**
2. Stakeholder review of creative direction doc in Notion (3 concepts + strategy + images)
3. Continue iterating visual prompts in Gemini (round 2 prompts ready in visual-prompts.md)
4. Based on feedback, proceed to Phase 6 (Full Copy) with chosen direction
5. Still pending: no decision yet on pricing visibility, team faces, AirOps section prominence, client names, tone calibration
6. SOCO phrasing needs revisiting in Phase 6
