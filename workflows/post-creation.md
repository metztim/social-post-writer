# Post Creation Workflow

**Purpose:** Draft LinkedIn posts from Logseq [[socialpost]] entries using Tim's authentic voice

**Status:** Production Ready
**Last Updated:** 2025-11-05

---

## Quick Start

```bash
cd /Users/timmetz/Developer/Projects/Personal/social-post-writer
/draft-linkedin-post
```

---

## Workflow Steps

### Step 1: Scan Logseq Database

Search `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq` for all `[[socialpost]]` tags.

**Output:** `/tmp/logseq_socialpost_entries.json`

### Step 2: Select Recent Entries

Sort entries by file birth time (not modification time) and select 3 most recent.

**Output:** `/tmp/logseq_socialpost_selected.json`

### Step 3: Enhance with Page Context

For each entry, extract additional highlights from the same source page/journal.

**Why:** Related highlights provide depth, supporting quotes, stats, or examples that can enrich the post.

**Output:** `/tmp/logseq_socialpost_enhanced.json`

### Step 4: Present Options

Display 3 entries showing:
- The [[socialpost]] block with full context
- Additional highlights from same page
- Source file name and age

User selects which entry to develop.

### Step 4.5: Analyze Recent Performance (Optional)

**Purpose:** Gather intelligence on what's working before drafting.

**Agent:** Launch `engagement-pattern-analyst` subagent to:
- Query Notion MyContent for last 5-10 published posts
- Identify top-performing topics and patterns
- Flag underperforming patterns to avoid
- Return 1-2 paragraph summary

**Output:** Brief intelligence report informing drafting strategy

**Note:** This step can be skipped if drafting immediately, but provides data-driven insights over time.

### Step 5: Draft Using Voice Guide

**Load voice references:**
- `voice/tim-linkedin-voice-v2.md` - Overall voice patterns
- `voice/tim-linguistic-fingerprint-v2.md` - Detailed linguistic analysis
- Review similar posts in `samples/tim/` for structural guidance

**Drafting process:**
1. Identify post type (quote-based, tutorial, personal reflection, etc.)
2. Apply Tim's actual transition words (not AI generic ones)
3. Match his sentence rhythm and white space patterns
4. Use his characteristic phrases
5. Avoid all phrases on "Tim would never say" list

**Critical:** If draft doesn't sound authentically like Tim, acknowledge it and revise

### Step 5.5: Self-Review Draft

**Purpose:** Catch AI patterns before user review using uncorrelated context.

**Method:** Launch Task tool agent to:
- Load draft + Voice Authenticity Checklist (below)
- Check for negative patterns (meta-commentary, AI-isms, over-explanation)
- Check for positive patterns (white space, specific language, deletable material)
- Return: PASS (authentic) or FAIL (needs revision) with specific issues

**If FAIL:** Revise draft in Step 5 before proceeding

**If PASS:** Continue to Step 6

**Rationale:** Separate validation context prevents overfitting and catches issues early.

### Step 6: Save to Notion MyContent

**Option A: New Post**
- Create new page in MyContent database
- Set Title
- Populate **Claude Draft** property
- Set Status to "In progress"

**Option B: Existing Post**
- User provides Notion page ID
- Update existing page
- Populate **Claude Draft** property

### Step 7: User Editing

User reviews Claude Draft in Notion and:
- Edits into Final version (in page body)
- **Expects 20-30% deletions** (strategic cuts are Tim's editorial strength)
- Publishes
- Engagement metrics populate over time for future analysis

---

## Voice Authenticity Checklist

Before saving draft, verify:

**Negative checks (Tim NEVER does these):**
- [ ] No "Let's dive into..." or "Let's explore..."
- [ ] No "The real problem is..." or "The key is..."
- [ ] No "At the end of the day" / "The bottom line is..."
- [ ] No "Furthermore," / "Moreover," / "Additionally,"
- [ ] No "Here's the thing:" (use "Here's what happened:" instead)
- [ ] No "isn't it... it's..." constructions

**Positive checks (Tim DOES these):**
- [ ] Opens with concrete, specific, personal
- [ ] Uses white space as primary transition
- [ ] Short paragraphs (mostly 1-2 sentences)
- [ ] Radical sentence length variation
- [ ] "Turns out" for revelations
- [ ] "For me," / "For October," for personal grounding
- [ ] "My question for today:" for endings
- [ ] Self-aware parentheticals
- [ ] Names real people, tools, companies

---

## Output Locations

**Temp files:**
- `/tmp/logseq_socialpost_entries.json` - All entries found
- `/tmp/logseq_socialpost_selected.json` - 3 selected entries
- `/tmp/logseq_socialpost_enhanced.json` - Entries with page context

**Final draft:**
- Notion MyContent database → Claude Draft property

---

## Performance

**Time:** 15-20 minutes total
- Scanning: 1-2 min
- Selection & context: 1-2 min
- Metrics analysis (optional): 2-3 min
- Drafting: 5-10 min
- Self-review: 2-3 min
- Notion upload: 1 min

**Token usage:** 20-35k tokens (varies by entry complexity and agent usage)

**Success metrics:**
- Voice authenticity: 70-80% of draft unchanged in editing
- Engagement: Tracking over time via Notion metrics

---

## Related Files

- Slash command: `.claude/commands/draft-linkedin-post.md`
- Voice guide: `voice/tim-linkedin-voice-v2.md`
- Linguistic fingerprint: `voice/tim-linguistic-fingerprint-v2.md`
- Refinement process: `workflows/voice-refinement.md`
- Agent guidelines: `docs/AGENT_GUIDELINES.md`
- Engagement analyst: `.claude/subagents/engagement-pattern-analyst.json`
