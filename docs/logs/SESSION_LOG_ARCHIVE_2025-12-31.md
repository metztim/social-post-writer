# Writing Assistant - Session Log

---

## Session Log: 2026-02-27

**Project**: writing-assistant / copy / animalz-ai-services
**Type**: [copywriting]

### Objectives
- Run /copywrite process for Animalz AI Services landing page (animalz.co/ai-services)
- Develop strategy, research competitive landscape, generate variants, select finalists
- Create exec summary for stakeholder review
- Update positioning doc in Notion with process insights

### Summary
Completed Phases 1-5 of 7-phase copywriting process for the AI services landing page. Established core truth ("content people who had to become AI builders"), SOCO, SOCA through structured Sullivan/Dry/Wiebe frameworks. Competitive audit revealed the entire AirOps partner ecosystem is an SEO/AEO monoculture — content-first lane wide open. Generated 54 variants across 11 directions, three-laws tested, and selected three standalone finalist concepts. Created exec summary in Notion for stakeholder review. Updated positioning doc with full messaging strategy, competitive findings, banned words, and VOC. Process paused pending stakeholder feedback before Phase 6 (Full Copy).

### Files Changed
- `projects/copy/animalz-ai-services/state.md` — Created: process state (YAML + log) through Phase 5
- `projects/copy/animalz-ai-services/brief.md` — Created: deliverable, audience, attitude shift, constraints
- `projects/copy/animalz-ai-services/strategy.md` — Created: core truth, SOCO, SOCA, positioning statement
- `projects/copy/animalz-ai-services/research/competitive-copy-audit.md` — Created: 6 AirOps partners + AirOps copy audit, category clichés, banned words
- `projects/copy/animalz-ai-services/research/voice-of-customer.md` — Created: Ty's sales call VOC + web research (G2, forums, surveys)
- `projects/copy/animalz-ai-services/variants.md` — Created: 54 variants across 11 directions, labeled H/AI
- `projects/copy/animalz-ai-services/exec-summary-draft.md` — Created: strategy + 3 concepts for stakeholder review
- `projects/copy/animalz-ai-services/visual-prompts.md` — Created: Nano Banana Pro prompts for 3 billboard visuals
- `projects/copy/animalz-ai-services/SESSION-NOTES.md` — Created: detailed nuances, decisions, creative threads for session continuity
- `docs/SESSION_LOG.md` — Updated: this entry

### Referenced Materials
- `/Users/timmetz/Developer/Projects/Animalz/ai-services-business/marketing/services-page-copy.md` — Earlier draft of services page copy (pre-process), some variants pulled from here
- `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/docs/Animalz 2025 Brand Guidelines.pdf` — Brand colors, typography (ITC Souvenir Std, Founders Grotesk), critters, logo
- `/Users/timmetz/Developer/Projects/Animalz/websites/website-statamic` — Current website codebase, analyzed for voice/style reference
- `~/.claude/research/nano-banana-pro.md` — Nano Banana Pro prompting guide for image generation
- `~/.claude/research/copywriting-harry-dry-principles.md` — Copywriting principles reference
- Notion: AI Services Positioning doc (`312df6dc-2cc5-8154-acf7-f2b91d74c1fd`, work workspace)
- Notion: Context Engineering draft (`313df6dc-2cc5-8072-9827-f64b653b6a75`, work workspace) — referenced for team discipline insight
- Notion: Animalz Values (`2c7df6dc-2cc5-8063-aad2-f67c08e21ae6`, work workspace)
- Notion: Exec summary created at `314df6dc-2cc5-81a1-8d78-ec44757fef3d` (Marketing Projects, work workspace)

### Technical Notes
- The /copywrite process worked well for this type of service page — the structured phases prevented jumping to copy too early
- Competitive audit was highly valuable — the "monoculture" finding shapes the entire creative direction
- VOC from Ty's sales calls was more valuable than web research for actual prospect language
- Grain MCP exists but lacks search-across-calls capability — not useful for VOC extraction
- Animalz website voice analysis done via subagent exploring the Statamic codebase — characterized as "authority + accessibility + warmth"

### Future Plans & Unimplemented Phases

#### Phase 6: Full Copy
**Status**: Not started — blocked on stakeholder feedback on creative direction
**Planned steps**:
1. Receive stakeholder feedback on which concept(s) to develop
2. Resolve open questions (pricing visibility, team faces, AirOps prominence, client names, tone)
3. Write full landing page section by section: hero → problem/skills gap → what makes us different → AirOps section → how we work → service tiers → proof/results → published thinking → CTA
4. Apply Money Words throughout (You Rule, "get" not "pay", no "and" splitting messages)
5. Write in the medium — describe visual context even though working in text
6. Human writes first, Claude develops — same principle as exploration

#### Phase 7: Review
**Status**: Not started
**Planned steps**:
1. Kaplan's Law audit — every word must earn its place
2. Burrito test on body copy paragraphs
3. Interference check against banned words from Phase 3
4. Three laws recheck on final copy
5. SOCO alignment — does copy communicate ONE thing?
6. Simulate reality — copy in context (among competing pages, in search results)
7. Cut target: 10-33% reduction on body copy
8. Optional: spawn fresh-context reviewer subagent

### Next Actions
- [ ] Share exec summary Notion page with stakeholders (Ty, others)
- [ ] Generate billboard visuals using Nano Banana Pro prompts (visual-prompts.md)
- [ ] Collect stakeholder feedback on creative direction (A/B/C)
- [ ] Resolve open questions: pricing, team faces, AirOps prominence, client names, tone
- [ ] Resume /copywrite into Phase 6 after feedback
- [ ] Still pending: positioning doc in Notion could benefit from further refinement after stakeholder alignment

### Metrics
- Files created: 9
- Notion pages created: 1
- Notion pages updated: 1
- Variants generated: 54 (across 11 directions)
- Competitors audited: 7 (6 partners + AirOps)

### Learnings & Improvement Opportunities

**Workflow improvements:**
- The /copywrite process Phase 4 (Exploration) worked well with mixed sync: Tim writing variants in conversation, Claude coaching and pushing. The back-and-forth was natural.
- Exec summary creation for stakeholder review is a natural checkpoint between Phase 5 and 6 — could be formalized in the /copywrite command as an optional gate.

**New capabilities needed:**
- Grain API/MCP integration for searching sales call transcripts — would be valuable for VOC extraction if Animalz upgrades to Business Plan
- Billboard/ad visual generation workflow — writing Nano Banana Pro prompts manually works but could be a reusable skill

### Continuation Prompt
> Project: writing-assistant / copy / animalz-ai-services
> Session log: docs/SESSION_LOG.md
> Section: "## Session Log: 2026-02-27" (copywriting entry)
>
> Context: Running /copywrite for the Animalz AI Services landing page (animalz.co/ai-services). Completed Phases 1-5 of 7. Three finalist creative concepts selected, exec summary in Notion for stakeholder review. Paused pending feedback before Phase 6 (Full Copy).
>
> Key points:
> - Read `projects/copy/animalz-ai-services/SESSION-NOTES.md` first — contains critical nuances and creative threads
> - Read `projects/copy/animalz-ai-services/state.md` for process status
> - Exec summary in Notion: `314df6dc-2cc5-81a1-8d78-ec44757fef3d` (Marketing Projects, work workspace)
> - Positioning doc updated: `312df6dc-2cc5-8154-acf7-f2b91d74c1fd` (work workspace)
> - Visual prompts ready at `projects/copy/animalz-ai-services/visual-prompts.md`
>
> Referenced paths:
> - `projects/copy/animalz-ai-services/` — full project folder
> - `projects/copy/animalz-ai-services/SESSION-NOTES.md` — detailed nuances for continuity
> - `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/docs/Animalz 2025 Brand Guidelines.pdf`
> - `~/.claude/research/nano-banana-pro.md`
>
> Read the session log section above, familiarize yourself with the context, and let me know when ready to continue.

---

## Session Log: 2026-02-12

**Project**: writing-assistant
**Type**: [docs]

### Objectives
- Draft a LinkedIn post about building ClaudeQuote.com from a voice memo recorded while driving
- Produce three versions using different style references to compare approaches
- Create a Lex-optimized brief for Tim's Lex style fingerprint

### Summary
Created three LinkedIn post drafts about ClaudeQuote.com using different style approaches: (A) pattern-matching from published Notion posts, (B) codified linguistic fingerprint rules, and (C) a Lex-optimized brief. Tim preferred Draft A's conversational tone. Iteratively edited through ~8 rounds of feedback, pulling in "errand boy" from Lex and "I am not technical. At all." from Draft B. Final draft saved. Tim noted he no longer wants engagement questions at the end of LinkedIn posts ("so 2023").

### Files Changed
- `projects/linkedin-posts/claudequote-voice-memo/draft.md` - Created: Final LinkedIn post draft about building ClaudeQuote.com

### Referenced Materials
- `voice/tim-linguistic-fingerprint-v2.md` - Forensic linguistic analysis used for Draft B
- `voice/tim-linkedin-voice-v2.md` - Actionable voice guide used for Draft B
- `samples/tim/01-claude-code-style-guide.md` - Published post example used for Draft A pattern-matching
- `/Users/timmetz/Developer/Projects/Personal/claude-quote/` - The ClaudeQuote.com project (source of post content)
- `/Users/timmetz/Developer/Projects/Personal/claude-quote/docs/SESSION_LOG.md` - Build process details
- `/Users/timmetz/Developer/Projects/Animalz/claude-plugins/plugins/blog-style-guide-creator/brands/the-workflow/style-guide.md` - The Workflow house style (explored but not used for LinkedIn)
- Notion MyContent database - Published LinkedIn posts queried for style patterns
- https://www.animalz.co/blog/claude-code - Animalz Claude Code getting started guide (referenced in post)

### Plan File
- **Path**: `~/.claude/plans/async-roaming-crown.md`
- **Status**: Completed
- **Phases Completed**: All (exploration, design, drafting, editing)

### Technical Notes
- **Three-draft comparison approach worked well**: Running subagents with different style inputs (examples vs rules) produced meaningfully different outputs. Draft A (examples) was more conversational; Draft B (rules) was tighter/more rhythmic. Worth repeating.
- **Lex research**: Lex calls its feature "Style Guide" not "style fingerprint." Best input for Lex is outline + context (not a finished draft). It combines stored writing samples with structural content to generate.
- **Notion content gaps**: Some published LinkedIn posts in Notion had content stored in blocks that weren't fully readable via API. Only 2 of 5 posts had full content visible.
- **Tim's Superpath Slack message** was the key factual source — lists exactly what Tim did (5 items after the voice memo).

### Learnings & Improvement Opportunities

**CLAUDE.md updates:**
- Tim no longer wants engagement questions at post endings ("so 2023") — update voice guide v3 when next revising
- Tim prefers Draft A style (conversational/flowing) over Draft B style (tight/punchy) — the fingerprint rules may over-optimize for tightness
- Em-dashes: Tim asked to remove ALL em-dashes from this post. This contradicts the fingerprint which marks them as "signature punctuation." May be post-specific or an evolving preference — worth checking on next post.

**Workflow improvements:**
- The draft-linkedin-post skill could be enhanced to automatically read the voice fingerprint files and produce a first draft, saving the manual subagent setup
- Could add a "style comparison" mode that automatically produces drafts from different style references

### Next Actions
- [ ] Tim to review and edit the final draft before publishing
- [ ] Consider writing a full We Eat Robots article about the same topic (mentioned in voice memo)
- [ ] Update voice/fingerprint files with new preferences discovered (no engagement questions, em-dash usage)

### Metrics
- Files created: 1
- Drafts produced: 3 (+ 1 Lex brief + 1 combined edit)
- Editing rounds: ~8

### Continuation Prompt
> Project: writing-assistant
> Session log: docs/SESSION_LOG.md
> Section: "## Session Log: 2026-02-12" ([docs] entry)
>
> Context: Drafted a LinkedIn post about building ClaudeQuote.com from a voice memo. Final draft saved. Tim mentioned potentially continuing with a full We Eat Robots article on the same topic.
>
> Key points:
> - Final LinkedIn draft at projects/linkedin-posts/claudequote-voice-memo/draft.md
> - Tim prefers conversational Draft A style over tight/punchy Draft B
> - Tim no longer wants engagement questions at post endings
> - Tim asked to remove all em-dashes from this post (contradicts fingerprint)
> - Full article for We Eat Robots is a potential follow-up
>
> Referenced paths:
> - `projects/linkedin-posts/claudequote-voice-memo/draft.md`
> - `voice/tim-linguistic-fingerprint-v2.md`
> - `voice/tim-linkedin-voice-v2.md`
> - `/Users/timmetz/Developer/Projects/Personal/claude-quote/`
>
> Read the session log section above, familiarize yourself with the context, and let me know when ready to continue.

---

## Session Log: 2025-11-13

**Project**: social-post-writer
**Duration**: ~45 minutes
**Type**: [docs] [content-creation]

### Objectives
- Draft LinkedIn post about the /unslop command (custom Claude Code slash command)
- Research Claude Code ecosystem (skills, plugins, slash commands) to determine best sharing approach
- Finalize post for LinkedIn's 3,000 character limit

### Summary
User had a draft post about their /unslop command—a Claude Code slash command that fights AI-generated bloat in documentation by applying MECE, DRY, and simplicity principles. I researched the Claude Code ecosystem (skills vs plugins vs slash commands), provided strategic advice on sharing the command, helped expand the draft into a full article version, then condensed it back to a LinkedIn-optimized version. The final post explains the LLM repetition problem, shows the complete 18-line self-contained command, and includes safety warnings and clear installation instructions.

### Files Changed
- `drafts/unslop-command/unslop-command-article.md` - Created full article version with detailed explanations, before/after examples section, and installation instructions

---

## Session Log: 2025-12-31

**Project**: writing-assistant
**Duration**: ~30 minutes
**Type**: [content-creation]

### Objectives
- Find a specific quote from Dario Amodei in user's Logseq database about writing essays by hand
- Set up permanent Logseq access for this project
- Craft LinkedIn post featuring the quote for New Year's posting

### Summary
Configured permanent Logseq database access by creating project CLAUDE.md with the path. Located the Dario Amodei quote from "A Cheeky Pint With Anthropic CEO Dario Amodei" (interview with Stripe's John Collison). Iteratively refined a LinkedIn post through multiple rounds of editing—tightening the hook, ensuring journalistic accuracy with quote attribution, eliminating repetition, and applying Harry Dry's writing principles (visual, falsifiable, unique). Final post ready for Dec 31st posting.

### Files Changed
- `CLAUDE.md` - Created project-level config documenting Logseq database path at `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`

### Technical Notes
- Logseq stores data as markdown files in `pages/` and `journals/` directories
- Quote source: "A Cheeky Pint With Anthropic CEO Dario Amodei" - YouTube interview, timestamp ~01:02:04
- Journalistic standards: ellipsis brackets `[…]` for omissions, verbal fillers can be removed, but cutting context that changes tone should be disclosed
- Harry Dry's writing rules applied: Can I visualize it? Can I falsify it? Can nobody else say this?

### Final LinkedIn Post

```
We're three years into the ChatGPT era, and Dario Amodei, the CEO of Anthropic, still writes his own essays:

> "I use Claude to generate lots of ideas. I kind of use it as research. But so far, I've done the writing myself. […] I'd be comfortable with it for business emails, but writing an essay or something that I want to really get right, it's not quite there yet. But maybe it will be in a year or so."

Let's see if he's still writing them himself on December 31st 2026.

Until then, here's to another year where it takes humans to do great writing. 🥂
