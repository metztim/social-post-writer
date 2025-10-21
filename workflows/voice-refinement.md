# Voice Refinement Workflow

**Purpose:** Continuously improve draft quality by learning from Tim's edits and engagement metrics

**Frequency:** Monthly, or after every 5-10 posts with Claude drafts
**Status:** Ready to implement
**Last Updated:** 2025-10-21

---

## Overview

This workflow creates a feedback loop:
1. Claude drafts post → saves to Claude Draft field
2. Tim edits → publishes Final version
3. Engagement metrics populate
4. Monthly analysis: compare drafts to finals, correlate with engagement
5. Update voice guide with learnings

**Result:** Each post makes the next one better

---

## Step 1: Collect Recent Posts for Analysis

Query MyContent database for posts with:
- Claude Draft populated (has my draft)
- Final version published (has Tim's edits)
- Engagement metrics filled in (has performance data)
- Publishing date within last 30 days

**Query:**
```
database_id: 131edc77-7df2-80be-a79e-edc6e0955fc2
filter: {
  "and": [
    {"property": "Claude Draft", "rich_text": {"is_not_empty": true}},
    {"property": "Status", "status": {"equals": "Done"}},
    {"property": "Metrics Updated", "date": {"is_not_empty": true}}
  ]
}
sorts: [{"property": "Publishing date", "direction": "descending"}]
page_size: 10
```

**Expected:** 5-10 posts per monthly review

---

## Step 2: Draft vs Final Comparison

For each post, perform detailed comparison:

### A. Extract Both Versions

**From Notion:**
- Claude Draft (from property)
- Final version (from page body, under "# Final version" heading)

**Save to temp:**
- `/tmp/voice-refinement/draft-[post-title].md`
- `/tmp/voice-refinement/final-[post-title].md`

### B. Word-Level Diff Analysis

Compare line by line:
- What phrases did Tim change?
- What sentences did Tim remove entirely?
- What did Tim add that Claude didn't include?
- What structural changes did Tim make?

**Tools:** Use git diff or similar text comparison

### C. Pattern Extraction

Identify recurring edits across multiple posts:

**Categories to track:**
1. **Claude-isms Tim always removes**
   - Example: If Claude says "The real problem" and Tim changes it 3+ times

2. **Tim's preferred alternatives**
   - Example: Claude says "Additionally," Tim changes to "And" or uses white space

3. **Structural changes**
   - Does Tim consistently shorten/lengthen paragraphs?
   - Does Tim add/remove line breaks in specific patterns?

4. **Voice refinements**
   - Phrases Tim adjusts to sound more authentic
   - Transitions Tim prefers

---

## Step 3: Engagement Correlation Analysis

**Questions to answer:**

1. **Which posts performed best?**
   - Sort by engagement rate
   - Sort by impressions
   - Identify top 3 performers

2. **What did those posts have in common?**
   - Voice patterns Claude got right
   - Elements Tim kept vs changed
   - Structure and format

3. **Which Claude patterns correlated with success?**
   - Did posts where Claude used X pattern perform better?
   - Did posts where Tim made fewer edits perform better/worse?

4. **Which Claude patterns correlated with poor performance?**
   - Did certain AI-isms hurt engagement?
   - Did over-explained transitions reduce engagement?

**Save findings:** `/tmp/voice-refinement/engagement-analysis.md`

---

## Step 4: Update Voice Guide

Based on comparison and engagement analysis:

### A. Update "Tim Would Never Say" List

Add newly discovered patterns:
```markdown
## Tim Would Never Say

[Existing patterns...]

### Newly Discovered (2025-11 refinement):
- "The challenge is..." (Tim prefers direct statements)
- "This begs the question..." (Tim asks questions directly)
```

### B. Refine Positive Fingerprint

Add confirmed successful patterns:
```markdown
## Tim's Actual Recurring Phrases

[Existing patterns...]

### Confirmed in Recent Posts:
- "Turns out" - used in 4/5 recent posts for revelations
- Opening with "You [verb]..." - 3/5 posts, high engagement
```

### C. Document Engagement Learnings

```markdown
## What Works (Based on Metrics)

### High Engagement Patterns:
- Quote-based opens: 7.69% avg engagement
- "My question for today:" endings: 5.2% avg engagement
- White space transitions (no connectors): 4.1% avg engagement

### Low Engagement Patterns:
- Over-explained transitions: 1.8% avg engagement
- Generic questions: 1.5% avg engagement
```

### D. Version Increment

- Save current voice guide to `voice/archive/tim-linkedin-voice-v1.md`
- Update main guide: `voice/tim-linkedin-voice-v2.md`
- Document changes in changelog section

---

## Step 5: Test Updated Guide

Draft next post using updated voice guide and compare quality:
- Does it sound more authentically like Tim?
- Fewer phrases that need editing?
- Better engagement on published version?

---

## Refinement Log Format

Keep record of each refinement cycle in `voice/refinement-log.md`:

```markdown
## November 2025 Refinement

**Posts analyzed:** 7
**Date range:** Oct 1 - Oct 31, 2025
**Avg engagement:** 3.2%

### Key Learnings:

**Claude consistently over-used:**
- "The real problem" (removed in 5/7 posts)
- "isn't... it's..." (removed in 4/7 posts)

**Tim consistently preferred:**
- Simple "And" over "Additionally" (6/7 posts)
- White space over explicit transitions (7/7 posts)

**Engagement insights:**
- Posts with quotes averaged 5.1% engagement (vs 2.8% without)
- "My question for today:" endings: 4.2% avg engagement
- Posts where Claude used fewer AI-isms: 3.8% vs 2.1% engagement

**Voice guide updates:**
- Added 3 new "never say" patterns
- Refined opening hook guidelines
- Updated transition preferences

**Next refinement:** December 2025 (after next 5-10 posts)
```

---

## Success Metrics

Track improvement over time:

**Voice accuracy:**
- % of draft kept unchanged by Tim (target: increase over time)
- # of voice-related edits needed (target: decrease over time)

**Engagement performance:**
- Avg engagement rate of Claude-drafted posts
- Compare to posts written without Claude

**Efficiency:**
- Time Tim spends editing Claude drafts vs writing from scratch
- Quality of first draft (fewer revisions needed)

---

## Prerequisites

**Data required:**
- Claude Draft populated in MyContent
- Final version published
- Engagement metrics filled in
- Minimum 5 posts for meaningful analysis

**Tools:**
- Notion API access to MyContent
- Text diff tools for comparison
- Python for statistical analysis (optional)

---

## Iteration Frequency

**Monthly refinement:** Standard cadence

**Ad-hoc refinement:** When:
- Multiple posts in a row need heavy editing
- User notices recurring Claude patterns that don't match voice
- Engagement metrics show unusual patterns

---

## Related Files

- Post creation: `workflows/post-creation.md`
- Voice guide: `voice/tim-linkedin-voice-v1.md`
- Linguistic fingerprint: `voice/tim-linguistic-fingerprint-v1.md`
- Main command: `.claude/commands/draft-linkedin-post.md`
