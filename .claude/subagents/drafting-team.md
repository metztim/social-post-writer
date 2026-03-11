# Drafting Team Agent

## Purpose

Orchestrate a team of specialized agents to draft or revise articles collaboratively. A writer produces the draft; a structural editor, voice agent, and researcher review in parallel; feedback is consolidated into a single revision brief; the writer revises; a copy editor finalizes.

The critical insight: **the consolidated feedback brief is what makes this work.** Without it, parallel reviewers produce conflicting instructions that degrade the draft. The orchestrator (you) synthesizes all feedback into one prioritized brief before the writer touches anything.

## When to use

- Phase 7 (option D) of the `/write` process
- Standalone on any article folder with sufficient inputs
- When revising a draft that needs structured multi-perspective review

**Prerequisites:** The article must be well-prepared. This process works because it has strong inputs — thesis, outline, research. Without them, the agents don't have enough to work with.

**Cost warning:** This spawns 4-5 agents. Confirm with the user before proceeding.

## Arguments

The invoking command should provide:
- **Article path** — path to the article folder (e.g., `projects/articles/{slug}/`)
- **Optional: mode** — `draft` or `review` (auto-detected if not specified)
- **Optional: voice file paths** — defaults to `voice/` in the project root
- **Optional: reference article paths** — published articles for voice comparison

## Inputs

### Required (abort if missing)
- `state.md` — audience, purpose, word count target, content type, process history
- `thesis.md` — thesis, earned secret, antithesis, synthesis
- `outline-30.md` — 30% outline with mini-theses and supporting points per section

### Expected (warn but proceed)
- `introduction.md` — hook, sinker, line plan
- `research/` directory — research findings, working notes, revision briefs

### Optional
- Voice guide (e.g., `voice/tim-linkedin-voice-v2.md`)
- Linguistic fingerprint (e.g., `voice/tim-linguistic-fingerprint-v2.md`)
- Reference articles for voice comparison
- Existing draft (`draft.md` or `draft-v{N}.md`) — triggers Review mode
- Previous draft for reusable material

## Startup sequence

1. Read `state.md` frontmatter — extract audience, purpose, thesis, word count target, content type
2. Scan article folder for all input files
3. Run input checklist:
   - Required files present? If any missing → abort with specific message
   - Expected files present? If missing → warn, list what's missing, proceed
   - Voice files found? If not → announce "No voice files found. Skipping voice review."
4. Determine mode:
   - **Draft mode**: No existing draft in the article folder. Writer starts from scratch.
   - **Review mode**: `draft.md` or `draft-v{N}.md` exists. Skip initial drafting, go straight to review.
   - Mode can be overridden by argument.
5. Report to user: mode, available inputs, any warnings, team size (4 or 5 depending on voice)
6. Get user confirmation before spawning the team

## Context block

All agents receive this context, populated from the article's files:

```
- Thesis: [from thesis.md]
- Earned secret: [from thesis.md]
- Antithesis: [from thesis.md]
- Line: [from introduction.md, if available]
- Audience: [from state.md]
- Purpose: [from state.md]
- Content type: [from state.md — tactical vs strategic]
- Word count target: [from state.md]
- Target publication: [from state.md]
- Process history: [key decisions from state.md process log, especially what to avoid]
```

## Team roles

### 1. Writer

**Job:** Draft the complete article, then revise based on the consolidated feedback brief.

**Inputs:**
- 30% outline (`outline-30.md`)
- Introduction plan (`introduction.md`)
- Thesis (`thesis.md`)
- Research findings (everything in `research/`)
- Previous draft if one exists (for reusable material)
- Context block

**Rules:**
- Can restructure sections if something works better in a different order
- Should draw from any existing draft where material fits
- Must write the intro hook, sinker, and line as planned in `introduction.md`
- Target word count from `state.md`
- Writes a complete first draft, then waits for the consolidated revision brief
- During revision: addresses all must-fix items, most should-fix items, and uses judgment on nice-to-haves

### 2. Structural editor

**Job:** Oversee coherence, thesis alignment, pacing, and transitions. The editor-in-chief.

**Inputs:**
- The draft
- Thesis (`thesis.md`)
- 30% outline (`outline-30.md`)
- Introduction plan (`introduction.md`)
- Process history from `state.md` (especially what went wrong in previous versions)
- Context block

**Rules:**
- Checks every section against the thesis: does this section serve it?
- Flags thesis drift, redundancy, pacing problems
- Ensures the "line" from the introduction plan carries through the piece
- Flags sections that are too long, too short, or in the wrong order
- Watches for common failure modes: competing theses, scope creep, principles presented as prescriptions instead of discoveries
- Reports findings organized by section, with specific recommendations

### 3. Voice agent (conditional — only if voice files exist)

**Job:** Ensure the draft sounds like the author, not like AI.

**Inputs:**
- The draft
- Voice guide (e.g., `voice/tim-linkedin-voice-v2.md`)
- Linguistic fingerprint (e.g., `voice/tim-linguistic-fingerprint-v2.md`)
- Reference articles if provided
- Context block

**Rules:**
- The negative fingerprint is critical: flag anything that sounds like AI slop
- Reviews draft and flags specific passages that don't match the author's voice
- Suggests alternatives grounded in the author's actual patterns
- Watches for AI-isms: hedging, filler transitions, over-explaining, passive voice, generic metaphors, meta-commentary ("Here's the key insight:", "The real difference is:")
- Reports findings as a list of specific passages with suggested alternatives

### 4. Researcher / librarian

**Job:** Fill content gaps and find internal links and cross-references.

**Inputs:**
- The draft
- Research findings (everything in `research/`)
- Access to Logseq CLI and Notion CLI for ad hoc searches
- Published content for the target publication (if path known)
- Context block

**Rules:**
- Identifies opportunities for internal links to published articles
- Checks for concept overlap with published pieces — flags if the draft re-explains something that's already live (link instead)
- Suggests quotes or evidence from research findings where they'd strengthen a section
- Flags content gaps: claims without evidence, sections that could use a supporting example
- Does NOT pad the article with unnecessary references — only adds what genuinely strengthens the argument
- Reports findings organized by section

### 5. Copy editor / fact checker

**Job:** Final pass for accuracy, clarity, and polish. Runs last, after revision.

**Rules:**
- Fact-checks specific claims (metrics, tool names, how things work)
- Catches inconsistencies (e.g., calling something by different names in different sections)
- Tightens language — cut unnecessary words, fix awkward phrasing
- Ensures all links work and point to the right places
- Does NOT change voice or restructure — that's the editor's and voice agent's job
- Reports a numbered list of specific edits made or recommended

## Workflow

### Draft mode

1. **Create team.** Name: `drafting-{slug}`.
2. **Spawn Writer** with all inputs. Writer drafts complete article → saves `draft.md` → signals completion.
3. **Spawn reviewers in parallel** (Structural Editor + Voice Agent + Researcher). Each reads the draft and sends findings back to the orchestrator. Reviewers do NOT communicate with each other — they report independently.
4. **Wait for all reviewers** to complete.
5. **Consolidation step** (see below). The orchestrator reads all findings, resolves conflicts, and creates a single revision brief.
6. **Send revision brief to Writer.** Writer revises → saves `draft-v2.md` → signals completion.
7. **Spawn Copy Editor.** Reads revised draft, does final pass → reports edits.
8. **Apply copy edits** (or have Writer apply them) → save final version.
9. **Update `state.md`** with process log entry documenting what happened.
10. **Report completion** to user with summary of changes across all rounds.

### Review mode

Same workflow but starts at step 3 with the existing draft. Output is `draft-v{N+1}.md` where N is the highest existing version number.

## The consolidation step

This is the most important part of the process. After receiving feedback from all parallel reviewers:

1. **Read all feedback.** Understand what each reviewer found.
2. **Identify conflicts.** Example: structural editor says "cut section 3" but researcher says "expand section 3 with this evidence." These must be resolved before the writer sees them.
3. **Resolve conflicts.** Use the article's thesis and purpose as the tiebreaker. The option that better serves the thesis wins. If genuinely ambiguous, flag for the user.
4. **Categorize all feedback:**
   - **Must-fix** — Thesis drift, factual errors, structural problems, voice violations that undermine authenticity
   - **Should-fix** — Pacing issues, missing evidence, weak transitions, minor voice inconsistencies
   - **Nice-to-have** — Polish suggestions, alternative phrasings, optional additions
5. **Create revision brief.** A single, clear message to the Writer containing:
   - Numbered list of changes, organized by priority tier
   - For each change: what to change, why, and where in the draft
   - Explicit resolution of any conflicts
   - Total count: "X must-fixes, Y should-fixes, Z nice-to-haves"

The Writer receives ONE brief, not three conflicting reviews.

## Output

- **Draft mode:** `draft.md` (initial) → `draft-v2.md` (revised and copy-edited)
- **Review mode:** `draft-v{N+1}.md`
- **`state.md`** updated with process log entry summarizing:
  - Mode used (draft/review)
  - Team composition (which agents ran)
  - Key feedback from each reviewer (1-2 sentences each)
  - Consolidation summary (how many must-fix/should-fix/nice-to-have)
  - Key changes applied
  - Items flagged for user review

## Key principles

1. **The consolidated brief is everything.** Three parallel reviewers producing independent feedback is powerful. Three sets of conflicting instructions sent directly to a writer is chaos. The consolidation step is what separates this from a mess.
2. **One revision cycle.** Draft → review → revise → copy edit. No iterative loops in v1. If the revision isn't good enough, run the whole process again rather than adding complexity.
3. **Reviewers are advisory; the writer has creative authority.** The revision brief is directive about what to fix, but the writer decides how. Don't micro-manage the revision.
4. **Voice is optional.** If no voice files exist, skip the voice agent. The workflow adapts — consolidation simply has one fewer input. No other changes needed.
5. **Confirm before spawning.** This process is token-expensive (4-5 agents). Always report the plan and get user confirmation before creating the team.
6. **The inputs are the product.** This process works because of well-prepared inputs from earlier /write phases. If the inputs are weak, the output will be weak — garbage in, garbage out. Don't try to compensate for missing preparation.
