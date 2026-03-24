# /newsletter

Weekly newsletter workflow for We Eat Robots. Tim provides rough input in a Notion page — ranging from polished drafts to raw notes to pasted AI output — then runs `/newsletter` to research, rewrite, polish, and write the final version back to Notion.

## Arguments

$ARGUMENTS — Either:
- A Notion page URL or ID: `/newsletter 325edc777df2808cb638e1b7c1561297`
- No argument: resume the most recent in-progress newsletter issue

## Core philosophy

**Preserve Tim's angles, not his exact words.** Tim's opinions and perspectives are sacred — his phrasing is not. When Tim has written genuine commentary, refine it. When he's dumped raw notes or AI output, rewrite it from scratch in his voice. The goal is a newsletter that sounds like Tim wrote every word thoughtfully, regardless of what the input looked like.

The newsletter is Tim telling smart friends what he read this week and why it matters. It's personal curation with genuine engagement — not content aggregation.

## Core rules

1. **Never skip phases.** Complete each phase before the next. No jumping ahead.
2. **Preserve Tim's angles, rewrite freely.** His opinions and connections are the value. The words can change. Full rewrites are expected for raw notes or AI output.
3. **Enforce quality gates.** Each phase has specific gates. Actively test them — don't just ask about them.
4. **Checkpoint every phase.** Explicit user confirmation before advancing.
5. **Read state first.** Always read `state.md` before doing anything.
6. **DO NOT use AskUserQuestion.** Use plain text prompts for natural conversation.
7. **Use Notion CLI, not MCP.** All Notion operations go through the `notion` CLI tool.
8. **Search locally first.** For Tim's published content, search local project files + MyContent Notion DB (personal workspace). Never web-search for Tim's own posts.

Display current phase prominently: `**[Phase X/4: Name]**`

## Newsletter structure

Each issue has up to two sections:

**Featured article (optional):** Tim's latest published article with personal context + link. Could be an Animalz blog post, WER article, or timmetz.nl piece. Some weeks there's no new article — that's fine, skip this section entirely.

**Reads & Listens (required):** 2-4 curated items Tim read or listened to that week. Each item gets 1-2 short paragraphs of Tim's commentary + link to source. The commentary is the value — not the summary. Tim's take on why it matters, what surprised him, what connection he made.

## Startup

### Resuming an existing issue
If no argument provided, or argument matches an existing folder at `projects/newsletters/{date}/` with a `state.md`:
1. Read `state.md` frontmatter and process log
2. Read the Notion page content (use `notion_page_id` from state.md)
3. Announce: "Resuming newsletter for **{publish_date}**. You're in **Phase {X}: {name}**. Last time: {summary from process log}. Ready to continue?"

### Finding the most recent issue
If no argument provided:
1. Scan `projects/newsletters/*/state.md` for the most recently updated file where not all phases are complete
2. Present it and ask for confirmation
3. If none found, ask user to provide a Notion page URL or ID for a new issue

### Starting a new issue
If the argument is a Notion page URL or ID:
1. Extract the page ID (strip URL formatting if needed)
2. Read the Notion page to get the title and confirm it's a newsletter issue
3. Create `projects/newsletters/{YYYY-MM-DD}/` (use the Monday publish date)
4. Create `state.md` with initial YAML frontmatter
5. Begin Phase 1

## State file format

```yaml
---
title: "WER Newsletter - YYYY-MM-DD"
slug: "YYYY-MM-DD"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
current_phase: 1
notion_page_id: "<page-id>"
publish_date: "YYYY-MM-DD"
phases:
  1_intake: { status: pending }
  2_research: { status: pending }
  3_rewrite: { status: pending }
  4_qa: { status: pending }
sections:
  featured_article: { present: false, title: "", url: "" }
  reads_and_listens: []
    # Each entry: { title: "", source_url: "", readiness: "polished|draft|raw|link-only", status: "pending" }
notion_comments: []
  # Each: { comment_text: "", source_block_id: "", addressed: false }
gates_passed: []
---

# Process Log
```

Update `state.md` after each phase completion: set phase status to `complete` with date, advance `current_phase`, update `last_updated`, and append a process log entry summarizing what was decided.

---

## Phase 1: Intake

**[Phase 1/4: Intake]**

**Goal:** Read the Notion page completely, catalog all content and inline comments, assess each section's readiness, and collect source URLs.

### 1a. Scan Logseq for flagged items
Search for items Tim has tagged for the newsletter while reading during the week:
```bash
logseq search-all "wer newsletter" --limit 20
```

For each result tagged `#[[wer newsletter]]` (that isn't already tagged `[[used]]`):
- Note the page title, highlight text, and Tim's note
- Check if it's already in the Notion draft
- If not: flag it as a potential addition Tim may have forgotten to include

Also scan MyContent for newsletter-tagged items:
```bash
notion query "MyContent" --filter '{"and":[{"property":"Type","multi_select":{"contains":"WER newsletter"}},{"property":"Status","status":{"does_not_equal":"Done"}},{"property":"Status","status":{"does_not_equal":"Discarded"}}]}' -w personal
```

For each result: note the title, check if it's already in the Notion draft.

Present all unfiled items together: "I found {N} items flagged for the newsletter ({M} from Logseq, {K} from MyContent) that aren't in your draft yet: {list}. Want to add any?"

### 1b. Read page content
Read the full Notion page:
```bash
notion get-blocks <page_id> -w personal --raw
```

Parse the page structure. Identify:
- "Final version" section (output destination — note the heading block ID)
- "Drafts" section (source content)
- "Research" section (any notes Tim has added)
- Each content section: featured article, individual Reads & Listens entries
- **Extract links from H3 headings** (check `rich_text[].text.link` in raw JSON — heading titles often contain the source URL)

### 1c. Read inline comments
```bash
notion get-comments <page_id> -w personal --raw
```

Map each comment to its source block using `_source_block_id`. Extract Tim's instructions and context. **Comments are often the most important research triggers** — things to look up, sources to verify, footnotes to add, points to clarify.

### 1d. Assess readiness of each section
For each section, categorize the input:

| Readiness | Description | What Claude does |
|---|---|---|
| **Polished** | Tim's actual writing, clear angle | Light polish + voice pass |
| **Draft** | Tim's rough notes, angle present but prose needs work | Rewrite in Tim's voice, preserving angle |
| **Raw** | Pasted AI output, research dump, or someone else's words | Full rewrite from scratch in Tim's voice — extract the useful data points, write Tim's take |
| **Link only** | Just a URL or title, no commentary | Flag — Tim needs to provide his angle before Claude can write anything |

### 1e. Collect source URLs upfront
Ask Tim for any missing source URLs now — don't defer to QA. Check:
- Links in H3 headings (already extracted in 1b)
- Links mentioned in the body text
- Logseq source pages (may have Readwise tracking URLs, not clean ones)
- Flag any items with no source URL: "I need the URL for: {list}"

### 1f. Present inventory
Show Tim what you found:
- **Featured article:** Present or absent? If present: title, where published, how much context Tim has drafted, readiness level
- **Reads & Listens:** List each item with: title, source URL (or missing), readiness level, any inline comments/instructions
- **Gaps:** Flag link-only items, missing URLs, sections that need Tim's angle
- **Comments to address:** List all inline comments with the text they're attached to

### 1g. Confirm scope
"Here's what I found. Anything missing or wrong before I start researching?"

**Quality gate:** All sections identified with readiness levels. All comments cataloged. All available source URLs collected.

**Checkpoint:** Tim confirms the inventory is complete. Tim provides missing URLs and angles for link-only items.

**Files to create/update:** Create folder and `state.md` with section inventory, readiness levels, and comments populated.

---

## Phase 2: Research

**[Phase 2/4: Research]**

**Goal:** Enrich each section with relevant context Tim may have forgotten or not thought to include.

**Important:** Tim often has context (specific URLs, Logseq pages, podcast timestamps) that you can't find through searching. When research comes up short, ask Tim directly rather than guessing or web-searching for his own content.

For each Reads & Listens item AND the featured article (if present):

### 2a. Comment-driven research (do this first)
Address each inline comment from Phase 1 — these are often the most specific and valuable research tasks:
- If Tim says "I might have a LinkedIn post about this" — search `projects/linkedin-posts/` and `notion search "topic" -w personal`
- If Tim says "search and link if so" — do the search and find the link
- If Tim provides context ("Footnote: ...") — note it for inclusion
- If Tim says to verify something — verify it (read the source, check the quote, confirm the claim)

### 2b. Logseq search
Search Tim's knowledge base for related notes:
```bash
logseq search "topic keywords"
```
Use `logseq search-all` if the priority search doesn't find enough. Use `logseq get-page "Title"` for full content of promising results.

Look for: prior thinking on this topic, book highlights, related frameworks, ref/ tagged examples.

### 2c. Existing content check
Search for connections to Tim's published work — **always search locally first:**
- Local project files: `projects/linkedin-posts/`, `projects/articles/`, `projects/we-eat-robots/`
- MyContent database: `notion search "topic" -w personal`
- Previous newsletter issues in `projects/newsletters/`
- Animalz blog posts: Notion KB (`notion query "Knowledge Base" -w work`) or `notion search "topic" -w work`

Look for: articles Tim wrote on the same topic, frameworks he's published, LinkedIn posts worth linking back to.

### 2d. Source verification
For items where Tim references specific claims, quotes, or data points:
- Read the original source if Tim provides or pastes it (don't re-fetch what Tim has already provided)
- Verify quotes are accurate
- Check if Tim's characterization of the source is fair
- Flag any inaccuracies or nuances Tim might want to address

### 2e. Pillar alignment
Map each item to content pillars from `CONTENT_STRATEGY.md`:
1. AI + content operations
2. Building with AI
3. Working differently with AI

Not a gate (some items may not map cleanly), but helps Tim see the through-line in his curation choices.

### 2f. Present findings
For each item, report:
- Related Logseq notes (with attribution: "From your notes on...")
- Connections to published work (with links)
- Comment resolutions (what you found for each inline comment)
- Source verification results (any inaccuracies or nuances found)
- Pillar alignment
- Suggested enrichments: specific additions Tim might want to make

**Quality gate:** Every item has been searched. All inline comments requiring research have been addressed. Findings are mapped to specific sections.

**Checkpoint:** Tim reviews findings, decides which enrichments to use. Tim provides any context Claude couldn't find.

**Files to create/update:** Save research findings to `research/enrichment-notes.md`. Update `state.md`.

---

## Phase 3: Rewrite & Polish

**[Phase 3/4: Rewrite & Polish]**

**Goal:** Produce the final newsletter text — rewriting, restructuring, and polishing as needed based on each section's readiness level.

### 3a. Read voice guides
Read these before writing:
- `voice/tim-linkedin-voice-v2.md` — primary reference (newsletter voice ≈ LinkedIn voice)
- `voice/tim-linguistic-fingerprint-v2.md` — negative constraints (what NOT to sound like)

### 3b. Rewrite each section according to readiness

**Polished sections (Tim's actual writing):**
- Light voice pass against the 15 critical patterns
- Tighten: cut meta-commentary, generic enthusiasm, summary that restates the source
- Preserve Tim's specific phrasing, asides, and personality

**Draft sections (Tim's rough notes):**
- Rewrite in Tim's voice, preserving his angle and key points
- Add structure: clear opening, Tim's take, connection or insight
- Apply voice patterns: em dashes, short paragraphs, mixed sentence lengths

**Raw sections (AI output, research dumps):**
- Full rewrite from scratch in Tim's voice
- Extract useful data points from the raw material
- Write Tim's actual take — what does this mean for his readers?
- Keep it short: 1-2 paragraphs per item

**Link-only sections:** Should have been resolved in Phase 1. If any remain, flag them.

### 3c. Newsletter-specific voice calibration
The newsletter is slightly more casual than LinkedIn posts:
- More first-person asides and reactions
- More "telling a friend what I read" energy
- Less structured argument, more genuine curiosity
- OK to be brief — a strong two-sentence take is better than a padded paragraph

Things to cut:
- Meta-commentary ("This is interesting because...", "The practical impact is real")
- Generic enthusiasm ("Really great piece...")
- Summary that restates what the source already says
- Prescriptive advice (this isn't an article, it's curation with opinion)
- AI-isms: "The honest caveat", "It's worth noting", hedging language

### 3d. Review newsletter flow
- **"Remove the link" test:** For each item — if you remove the link, does Tim's commentary stand on its own as a mini-opinion piece? If not, it's too much summary.
- **Featured article:** Is the context personal and specific? Not "I wrote about X" but why, what surprised him, the story behind it.
- **Flow:** Do items feel curated or random? Is there variety in source types? Is overall length 5-10 minutes?
- **Order:** Consider thematic flow. Usually: featured article → practical tool updates → broader perspective pieces → personal/reflective closer.

### 3e. Present the full draft
Show Tim the complete newsletter text. For each section, briefly note what changed and why. Don't silently rewrite — make the transformation visible.

**Quality gate:** Passes the voice checklist. No AI-isms. Each commentary sounds like Tim. The "remove the link" test passes for each item.

**Checkpoint:** Tim approves the draft (may request changes — iterate until approved).

**Files to create/update:** Update `state.md`.

---

## Phase 4: QA & Publish

**[Phase 4/4: QA & Publish]**

**Goal:** Final checks, then write the polished version to Notion.

### 4a. Link verification
- All source URLs are present and correctly formatted
- Featured article link is correct
- Any internal links (to Tim's articles, LinkedIn posts) are valid

### 4b. Comment resolution check
Go through the list of Notion comments from Phase 1. Confirm each has been addressed in the final version. Flag any unresolved comments.

### 4c. Proofread
- Spelling, grammar, punctuation
- Consistent formatting across sections
- No orphaned references or incomplete sentences
- Source attributions are present and specific

### 4d. Write to Notion
Read the page structure to find the "Final version" section:
```bash
notion get-blocks <page_id> -w personal --raw
```

Find the block ID of the "Final version" heading, then **append ALL content in a single call** (multiple calls with `--after` on the same block will reverse the order):
```bash
notion append-blocks <page_id> '<all blocks JSON>' --after <final_version_heading_id> -w personal
```

Format using proper Notion block types:
- `heading_2` for section headers (Featured Article title, Reads & Listens)
- `heading_3` for individual item titles (with source URL as link on the heading text where available)
- `paragraph` for commentary text
- `quote` for block quotes
- `bulleted_list_item` for lists if needed
- Include links as rich text with href

### 4e. Mark Logseq sources as used
For each Reads & Listens item that originated from a Logseq page tagged `#[[wer newsletter]]`, update the tag in Logseq:
- Add `[[used]]` tag to the highlight
- Add a note referencing which newsletter it was featured in, with the Substack link once published

This prevents the same item from surfacing in future `[[wer newsletter]]` scans.

### 4f. Save local snapshot
Write the final content to `final-snapshot.md` as a local reference copy with `source_of_truth` frontmatter pointing to the Notion page.

### 4g. Report completion
- Summary of what was published
- Any comments that were not fully addressed
- Pillar alignment summary (which pillars this issue touched)
- Word count

**Quality gate:** All links verified. All comments addressed. Content written to Notion successfully.

**Checkpoint:** Tim confirms the Notion page looks correct.

**Files to create/update:** Create `final-snapshot.md`. Update `state.md` — mark all phases complete.

---

## Notes

- Use `/save-session` if interrupted mid-process
- Phases are sequential but revisiting earlier phases is fine
- For multi-session newsletters, always read state.md and the Notion page before continuing
- Track which quality gates have passed in state.md `gates_passed` list
- Voice reference: newsletter is LinkedIn-adjacent but slightly more casual — Tim talking to friends about what he read
- **Notion append ordering:** When using `--after` on the same block multiple times, subsequent appends insert BEFORE previous ones. Always append all content in a single call to maintain correct order.
