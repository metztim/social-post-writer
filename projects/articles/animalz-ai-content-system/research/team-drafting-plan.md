# Team drafting plan: Animalz AI Content System article

## Overview

Agent team to draft the article collaboratively. Writer produces the draft, other agents review, challenge, and improve through discussion — not just sequential passes.

## Team roles

### 1. Writer
**Job:** Draft each section, handle transitions and flow across the full piece.
**Inputs:**
- 30% outline (outline-30.md)
- Introduction plan (introduction.md)
- Thesis (thesis.md)
- Original draft for reusable material (draft.md)
- Research findings (research/research-findings.md)
- Working notes (research/working-notes.md)
- Revision brief (research/revision-brief.md) — knows what failed in v1
**Rules:**
- Can restructure sections if something works better in a different order
- Should draw from original draft where material fits the new structure
- Must write the intro hook, sinker, and line as planned
- Target: ~2000 words total
- Writes a complete first draft, then opens it for team review

### 2. Voice agent
**Job:** Ensure the draft sounds like Tim, not like AI.
**Inputs:**
- `voice/tim-linkedin-voice-v2.md` — LinkedIn voice guide
- `voice/tim-linguistic-fingerprint-v2.md` — Forensic linguistic analysis (positive + negative fingerprint)
- Tim's 5 reference articles (Dropbox paths below)
- The negative fingerprint is critical: flag anything that sounds like AI slop
**Reference articles (stylistic):**
- `/Users/timmetz/Library/CloudStorage/Dropbox/1 Animalz/2 Areas/AI Ops Animalz/1 Published articles/20250522 Confessions of an AI Addict - Animalz.md`
- `/Users/timmetz/Library/CloudStorage/Dropbox/1 Animalz/2 Areas/AI Ops Animalz/1 Published articles/20241205 Blockbuster Blogs How Breakthrough Ideas Are Born - Animalz.md`
- `/Users/timmetz/Library/CloudStorage/Dropbox/1 Animalz/2 Areas/AI Ops Animalz/1 Published articles/20240725 Stay Strong Never Let AI Fill Your Blank Page - Animalz.md`
**Reference articles (practical/similar type):**
- `/Users/timmetz/Library/CloudStorage/Dropbox/1 Animalz/2 Areas/AI Ops Animalz/1 Published articles/20251002 claude-code-for-content-marketers-a-no-code-guide-animalz.md`
- `/Users/timmetz/Library/CloudStorage/Dropbox/1 Animalz/2 Areas/AI Ops Animalz/1 Published articles/20251120 the-ai-onion-why-95-of-ai-projects-die-and-what-to-do-about-it-animalz.md`
**Rules:**
- Reviews draft and flags specific passages that don't sound like Tim
- Suggests alternatives grounded in Tim's actual patterns
- Watches for AI-isms: hedging, filler transitions, over-explaining, passive voice, generic metaphors
- The article is by Tim, first person — should feel like him telling the story

### 3. Structural editor
**Job:** Oversee coherence, thesis alignment, pacing, and transitions. The editor-in-chief.
**Inputs:**
- Thesis (thesis.md)
- 30% outline (outline-30.md)
- Introduction plan (introduction.md)
- Revision brief (research/revision-brief.md) — knows what went wrong in v1 and what reviewers flagged
**Rules:**
- Checks every section against thesis: does this serve "you need a system, not just workflows"?
- Flags thesis drift, redundancy, pacing problems
- Ensures the "line" (wishful workflow thinking → systems thinking) carries through
- Flags if a section is too long, too short, or in the wrong order
- Can instruct the writer to revise
- Watches for the v1 failure modes: three competing theses, "feels like writing" creep, principles as teaching not discovery

### 4. Researcher / Animalz librarian (combined)
**Job:** Fill content gaps flagged by the team, find internal links and cross-references to published Animalz content.
**Inputs:**
- Research findings (research/research-findings.md) — already-curated material from Logseq, Notion, project files
- Animalz blog content: `/Users/timmetz/Developer/Projects/Animalz/websites/website-statamic/content/collections/blog/`
- Published context engineering article: https://www.animalz.co/blog/context-engineering
- Published AI onion article: https://www.animalz.co/blog/ai-onion
- Access to Logseq CLI and Notion CLI for ad hoc searches
**Rules:**
- When another agent flags "this needs a supporting example" or "can we link to something here?" — this agent finds it
- Identifies opportunities for internal links to published Animalz articles
- Checks for concept overlap with published pieces — flags if we're re-explaining something that's already live
- Can suggest quotes from research-findings.md parking lot where they'd strengthen a section
- Does NOT pad the article with unnecessary references — only adds what genuinely strengthens the argument

### 5. Copy editor / fact checker
**Job:** Final pass for accuracy, clarity, and polish.
**Rules:**
- Fact-checks specific claims (metrics, tool names, how things work)
- Catches inconsistencies (e.g., calling something by different names in different sections)
- Tightens language — cut unnecessary words, fix awkward phrasing
- Ensures all links work and point to the right places
- Runs AFTER the team is satisfied with structure and content
- Does NOT change voice or restructure — that's the editor's and voice agent's job

## Workflow

1. **Writer** drafts the complete article (all sections + intro + conclusion)
2. **Structural editor** reviews for thesis alignment, pacing, structure
3. **Voice agent** reviews for Tim's voice and AI-isms
4. **Researcher/librarian** fills gaps and adds internal links
5. Steps 2-4 happen in parallel where possible, agents discuss and challenge each other
6. **Writer** revises based on team feedback
7. Repeat 2-6 until team consensus
8. **Copy editor** does final pass
9. Output: `draft-v2.md` (to distinguish from original `draft.md`)

## Key context for all agents

- **Thesis:** "To craft authentic and differentiated content with AI, you need more than just workflows — you need a system."
- **Line:** Journey from "wishful workflow thinking" to "systems thinking"
- **Audience:** Content/marketing leaders evaluating AI for content at scale. Not implementers — leaders.
- **Publication:** Animalz Intelligence (not traditional Animalz blog)
- **Tone:** Tim's voice. First person. Case study of building the LinkedIn thought leadership system.
- **Scope:** Focused on the LinkedIn TL system only. Anonymize customer names.
- **CTA direction:** Subtle — reader should finish thinking "I want this, who builds this?" Points toward AI services page.
- **What to avoid:** "Feels like writing" angle, "code-illiterate" framing, principles as prescriptions (frame as discoveries), over-explaining concepts covered in published pieces (link instead)
- **Nathan story:** Needs his permission — include but flag with a note

## File locations

All article files: `projects/articles/animalz-ai-content-system/`
```
state.md              — Process state + full history
thesis.md             — Thesis, earned secret, antithesis, synthesis, headline
outline-10.md         — H1 + H2 headers
outline-30.md         — 30% outline with mini-theses and supporting points
introduction.md       — Hook, sinker, line plan
draft.md              — Original draft (v1, for reference/reusable material)
research/
  working-notes.md    — Raw thinking from thesis sessions
  revision-brief.md   — Full revision brief + reviewer feedback
  research-findings.md — Curated research from Logseq, Notion, project files
```

Voice files: `voice/` (in writing-assistant root)
```
tim-linkedin-voice-v2.md
tim-linguistic-fingerprint-v2.md
```
