- Staccato "The result?" section needed em-dash rhythm
- Closing question too generic → more provocative version
- Source link needed specificity ("Full How I Write episode")

**User disagreed with one recommendation:**
- I suggested cutting "He thinks more writers should follow a slower rhythm" as meta-commentary
- User correctly noted it provides necessary transition from Dan's personal practice to his advice for others
- Kept the line

**Notion API notes:**
- Successfully created database entry using `database_id` in parent (not `page_id`)
- Properties schema: `{"title": [{"text": {"content": "..."}}]}`
- Added content via `API-patch-block-children` with paragraph blocks
- Cannot update Type/Status via API (user set manually)

### Final Post Structure
1. Personal admission (weekly guilt)
2. Dan Wang intro with credential ("China analyst")
3. His approach: one annual letter
4. Transition: "He thinks more writers should follow a slower rhythm"
5. Quote from podcast
6. Platform pressure (Substack, Twitter)
7. Dan's result: quality over quantity
8. Tim's aspiration: monthly feels right
9. Reader perspective: would welcome slower pace from others
10. Question: "What pace feels right to you, either as a reader or a writer?"

### Key Decisions Made

**Angle selection:**
- Not about Dan's annual letters (too extreme for most)
- Focus on monthly/quarterly as achievable alternative to weekly treadmill
- Add personal struggle for authenticity
- Include reader perspective to broaden appeal

**Voice authenticity:**
- Added self-deprecating parenthetical: "(Content marketer who can't keep a content schedule. I know.)" — later removed by user in final edit
- Short punchy phrases: "One post. One year."
- Em-dash rhythm throughout
- Single question ending (no framing like "My question for today:")

**Dan Wang intro:**
- "China analyst Dan Wang" - clean, provides context for unfamiliar readers
- Considered other options: credential-based (publications), achievement-based (built reputation with one thing)

### Notion Entry Created
- **Page ID**: 2c0edc77-7df2-815e-a702-ffb7e5932ea4
- **Title**: "Dan Wang: Monthly/quarterly writing rhythm"
- **URL**: https://www.notion.so/Dan-Wang-Monthly-quarterly-writing-rhythm-2c0edc777df2815ea702ffb7e5932ea4
- **Status**: Ideas (user to update)
- **Type**: Not set (user to update to "LinkedIn post")

### Next Actions
- [ ] User to finalize and publish from Notion
- [ ] Add podcast link to comments when publishing
- [ ] Track engagement for future voice guide refinement

### Metrics
- Files created: 0 (source already existed)
- Notion pages created: 1
- Agent tasks launched: 2 (voice rewriter, editorial review)
- Draft iterations: 3 (initial → agent-refined → user-edited)
- Final word count: ~220 words

---

## Session Log: 2025-12-11

**Project**: writing-assistant
**Type**: [creative]

### Objectives
- Create visual for LinkedIn post "What Would The Buddha Do?"
- Find and use Gemini image generation tooling

### Summary
Explored creating a minimalistic visual for a LinkedIn post about using "What would the Buddha do?" as an AI prompt. Located the Gemini 3 Pro image generation skill in the plugins marketplace. Iteratively refined prompts to achieve a chat interface aesthetic showing the prompt and "Probably nothing." response.

### Files Changed
- None (creative/visual work session)

### Technical Notes
- **Gemini imagegen skill location**: `~/.claude/plugins/marketplaces/every-marketplace/plugins/compound-engineering/skills/gemini-imagegen/`
- **LinkedIn optimal dimensions**: 1200×627 (≈1.91:1), closest Gemini ratio is 16:9
- **Model used**: `gemini-3-pro-image-preview`
- **Multi-turn refinement**: Gemini supports iterative feedback to refine generated images

### Image Prompt Evolution
**Initial concept**: Minimalistic screenshot of prompting window with subtle Buddhist ornaments

**V1 result**: Quote card with mandalas in corners, lotus icon - too decorative, not UI-like

**V1 feedback given**:
```
Make this look like an actual screenshot of a chat interface, not a quote card. Add a visible text input field border around "What would the Buddha do?" to show it as a user message. Remove the mandala ornaments from the corners entirely. Replace "Perhaps, he would first..." with just "Probably nothing." and add a blinking text cursor after it to suggest the response is still being typed. Remove the lotus icon. The aesthetic should be clean functional UI like ChatGPT or Claude - realistic spacing, subtle shadows, proper message alignment. Keep the warm neutral background but make it feel like a real app screenshot.
```

**V2 result**: Chat bubbles with correct alignment, but artifacts (scrollbars, partial buttons, cropped UI chrome)

**V2 feedback prepared**:
```
Remove all the UI chrome around the edges - the scrollbars, the partial "Chat" button at top, the vertical elements on the left side. Just show the two chat bubbles cleanly centered on a plain background with nothing else. Keep the chat bubble styling and message alignment. The background should be clean white or very light gray, not tan/beige. Make it look like a polished, intentionally designed crop of a chat interface - just the essential exchange, no window decorations or browser elements.
```

### Next Actions
- [ ] Continue Gemini iteration with V2 feedback to clean up artifacts
- [ ] Finalize visual and attach to LinkedIn post
- [ ] Post "What Would The Buddha Do?" content

### Metrics
- Files modified: 0
- Gemini iterations: 2
- Prompt refinements: 2

---

## Session Log: 2025-12-16

**Project**: writing-assistant
**Type**: [docs] [review]

### Objectives
- Fact-check and refine LinkedIn post about "not-do lists" for 2026

### Summary
Reviewed a draft LinkedIn post about saying no to opportunities in the new year. Verified Warren Buffett's "5/25 Rule" attribution (noted it's third-hand and hedged appropriately with "supposedly"). Researched Lao Tzu quote origin — found it's from Tao Te Ching Chapter 48 but the user's version was a paraphrase, not a verbatim quote. Revised attribution to avoid false precision (removed quotation marks, used paraphrase style). Final polish on grammar and flow.

### Files Changed
- No files modified (review/consultation session)

### Technical Notes
- **Buffett 5/25 Rule**: Also called "Buffett's Two Lists" or "25/5 Focus Method". Story is third-hand (pilot → blogger → everyone). Buffett reportedly skeptical of attribution.
- **Lao Tzu quote**: Original (Ch. 48) contrasts 學 (learning) with 道 (Tao), not knowledge with wisdom. User's "knowledge/wisdom" framing was interpretation, not translation. Solution: paraphrase without quotation marks.
- **Journalistic standards**: Direct quotes in quotation marks must be actual verbatim quotes or established translations. Paraphrases should not use quotation marks.

### Next Actions
- [ ] Post finalized draft to LinkedIn
- [ ] Consider adding source link to Emily Kramer's MKT1 newsletter in post

### Metrics
- Files modified: 0
- Research queries: 2 (Buffett method name, Lao Tzu quote origin)

---

## Imported from we-eat-robots-writing: 2025-10-06

> *This session was imported when consolidating we-eat-robots-writing into writing-assistant (2025-12-30)*

**Project**: we-eat-robots-writing (now merged into writing-assistant)
**Duration**: ~2 hours
**Type**: [feature] [research] [tooling]

### Objectives
- Research supporting material from Logseq highlights library for "AI's Maddening Multitasking Trap" article draft
- Create reusable article research system for future articles

### Summary
Conducted comprehensive research through Logseq highlights library to find supporting data, quotes, and insights for the AI multitasking article. Found extensive material from books like BrainChains, A World Without Email, Four Thousand Weeks, Deep Work, The Distracted Mind, and others. Created a detailed research findings document with recommendations organized by theme. Then designed and implemented a reusable article research system consisting of a specialized agent and slash command for future article research workflows.

### Files Changed
- `projects/articles/ai-multitasking-trap/research-findings-logseq.md` - Created comprehensive research findings document
- `.claude/subagents/article-researcher.md` - Created specialized agent for comprehensive article research
- `.claude/commands/research-article.md` - Created slash command to invoke article-researcher agent

### Technical Notes

**Research Methodology**:
- Used parallel Grep searches across Logseq library with multiple keyword strategies
- Read 10+ highlight files including BrainChains, A World Without Email, Four Thousand Weeks, Deep Work
- Organized findings by type: research data, powerful quotes, supporting concepts, solutions

**Key Discoveries**:
- Strong research data: 25-100%+ task switching costs, 4x efficiency loss from multitasking
- Identified powerful concepts: attention residue (Sophie Leroy), overhead tax (Cal Newport)

**Design Decisions**:
- Chose single agent over multiple agents because research objectives are interconnected
- Structured agent for 6 research objectives: claims validation, similar arguments, new insights, contrary views, practical examples, supporting data

---

## Future Sessions

**Continue here for:**
- LinkedIn post drafting (test enhanced workflow)
- Article drafting with /research-article workflow
- Newsletter writing (we-eat-robots)
- Voice guide refinement (data-driven v3 update)
- Engagement analysis (systematic correlation)
- Workflow improvements (measure agent effectiveness)

**Session logs for this project:** Continue adding above this line

---

## Session Log: 2025-12-30

**Project**: writing-assistant
**Duration**: ~45 minutes
**Type**: [refactor] [docs] [config]

### Objectives
- Analyze current state of writing-assistant project after hiatus
- Check MCP servers and API integrations
- Compare with we-eat-robots-writing project and decide on merge strategy
- Consolidate into unified writing repository

### Summary
Conducted comprehensive analysis of both writing projects using parallel subagents. Discovered writing-assistant is a mature LinkedIn post drafting system with voice capture, while we-eat-robots-writing focuses on article research workflows. Designed and implemented a unified repository structure with `projects/` directory organized by content type (linkedin-posts, articles, we-eat-robots newsletter). Imported all assets from we-eat-robots-writing including the article-researcher agent and /research-article command.

### Files Changed
- `projects/linkedin-posts/` - Created directory, moved all drafts from `drafts/`
- `projects/articles/` - Created directory for long-form content
- `projects/articles/ai-multitasking-trap/` - Imported from we-eat-robots-writing
- `projects/articles/dan-wang-writing/` - Moved from drafts
- `projects/we-eat-robots/` - Created empty directory for newsletter editions
- `.claude/subagents/article-researcher.md` - Imported specialized research agent
- `.claude/commands/research-article.md` - Imported slash command for article research
- `docs/SESSION_LOG.md` - Merged we-eat-robots session log entry
- `drafts/` - Removed (contents moved to projects/)

### Technical Notes

**MCP Server Status**:
- Notion Personal: Connected and functional
- Chrome DevTools: Connected and functional

**Key Design Decisions**:
1. **Projects by type, not status**: `linkedin-posts/`, `articles/`, `we-eat-robots/` allows different workflows per content type
2. **Research co-location**: Each article keeps its `research-findings-*.md` alongside the draft (no shared research folder)
3. **Voice guides centralized**: Root-level `voice/` directory serves all project types
4. **Single .claude/**: All commands and agents in one place at repo root
5. **Notion for published work**: Local folders for drafts/research; Notion MyContent for tracking engagement

**Project Comparison Summary**:
| Aspect | writing-assistant | we-eat-robots-writing |
|--------|------------------|----------------------|
| Focus | LinkedIn posts, voice authenticity | Articles, research depth |
| Maturity | Production-ready (v2 voice guide) | Early stage |
| Main workflow | /draft-linkedin-post | /research-article |

### Future Plans & Unimplemented Phases

#### Phase: Archive/Delete we-eat-robots-writing
**Status**: Not started
**Planned Steps**:
1. Verify all content successfully imported (confirmed in this session)
2. Archive or delete `/Users/timmetz/Developer/Projects/Personal/we-eat-robots-writing`
3. Update any cross-references if needed

#### Phase: Test Imported Workflows
**Status**: Not started
**Planned Steps**:
1. Run `/research-article` command on an existing draft to verify it works
2. Confirm Logseq path permissions are correct in settings.local.json
