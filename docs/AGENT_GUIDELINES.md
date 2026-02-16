# Agent Usage Guidelines

**Purpose:** Document when and how to use agents in writing workflows based on best practices and learnings from practice.

**Last Updated:** 2026-02-16

---

## When to Use Agents

### ✅ Metrics Intelligence (Step 4.5)
**Type:** Custom Subagent (`engagement-pattern-analyst`)
**When:** Before drafting (optional)
**Why:** Provides data-driven insights from past performance
**Benefit:** Informs topic selection and approach with real engagement data

### ✅ Self-Review (Step 5.5)
**Type:** Task Tool (one-time validation)
**When:** After drafting, before saving to Notion
**Why:** Uncorrelated context catches AI patterns main thread might miss
**Benefit:** Prevents "two attempt pattern" and saves user review time

### ✅ Voice Refinement (Monthly)
**Type:** Task Tool (parallel analysis)
**When:** After accumulating 5-10 posts
**Why:** Systematic pattern extraction across multiple posts
**Benefit:** Data-driven voice guide updates
**See:** `workflows/voice-refinement.md`

### ✅ Article Research (`/write` Phase 4)
**Type:** Custom Subagent (`writing-researcher`)
**When:** During research phase of the `/write` process
**Why:** Deep search across Logseq + web, mapped to outline sections. Parallelizable, reusable.
**Benefit:** Comprehensive research with structured output organized by outline section
**See:** `.claude/subagents/writing-researcher.md`

### ✅ Article Editorial Review (`/write` Phase 8)
**Type:** Custom Subagent (`writing-editor`)
**When:** After drafting, during review phase of the `/write` process (optional)
**Why:** Uncorrelated context catches thesis drift, weak arguments, and cutting opportunities the main thread misses
**Benefit:** Fresh-eyes ABCD review (Awesome/Boring/Confusing/Didn't Believe) + specific cut recommendations
**See:** `.claude/subagents/writing-editor.md`

---

## When NOT to Use Agents

### ❌ Core Drafting (LinkedIn Step 5 / `/write` Phase 7)
**Reason:** Context continuity critical; the human writes, Claude supports conversationally
**Use:** Main thread
**Principle:** "Use agents for analysis, not final production"

### ❌ Thesis & Outline Development (`/write` Phases 1-3, 5-6)
**Reason:** Interactive sparring requires conversational flow and context continuity
**Use:** Main thread
**Principle:** "Agents can't spar — they analyze and report"

### ❌ Logseq Scanning (LinkedIn Steps 1-3)
**Reason:** Fast sequential operations, no parallelization benefit
**Use:** Main thread
**Principle:** "Don't use agents for trivial tasks"

### ❌ Notion Saving (LinkedIn Step 6)
**Reason:** Single API call, requires drafting context
**Use:** Main thread
**Principle:** "20k token overhead not justified"

---

## Lessons from Oct 24 Session

### What Went Wrong

**Agent 3 (Style Guide Updater):**
- Created new file instead of updating existing v1 guide
- Ignored existing voice guide structure and organization
- **Lesson:** Agents need explicit file paths and update instructions

**Agent 4 (Meta Post Writer):**
- Used AI patterns while writing about avoiding AI patterns
- Violated the style guide it was supposed to follow
- **Lesson:** Agents for analysis, humans for final production

### Guardrails Applied

1. **Explicit operations:** Always specify exact file paths and actions
2. **Human review gates:** All agent output reviewed before acceptance
3. **Analysis vs production:** Agents analyze/report; humans produce final content
4. **Context provision:** Give full context, don't assume agents remember

---

## Agent Design Principles (MECE + DRY)

### Single Source of Truth
- Voice patterns: ONLY in `voice/tim-linkedin-voice-v2.md`
- Workflow steps: ONLY in `workflows/post-creation.md`
- Agent configs: ONLY in `.claude/subagents/*.json`

### References, Not Copies
- Agent prompts reference voice guides by path
- Workflows reference agents by name
- No duplication of content across files

### Minimal System Prompts
- Single responsibility per agent
- Load content dynamically (don't embed)
- Explicit tool whitelisting (security)

---

## Quick Decision Tree

```
Is this analysis/validation? → Consider agent
  Research across multiple sources? → writing-researcher
  Editorial review with fresh eyes? → writing-editor
  Engagement metrics analysis? → engagement-pattern-analyst
Is this creative production? → Main thread
Is this interactive/conversational? → Main thread (thesis sparring, outline development)
Is this trivial operation? → Main thread
Will this run again? → Custom subagent
One-time complex work? → Task tool
```

---

## Related Resources

- Full agent guide: `~/Developer/Learning/claude-code/docs/agents/`
- Agent principles: MECE, DRY, single responsibility, least privilege
- Workflow file: `workflows/post-creation.md`
- Custom subagents: `.claude/subagents/`
