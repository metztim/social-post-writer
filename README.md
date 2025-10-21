# Social Post Writer

**AI-powered LinkedIn post creation that learns your authentic voice**

---

## Overview

This project helps Tim draft LinkedIn posts from Logseq [[socialpost]] entries using his authentic voice, with a continuous learning loop that improves quality over time.

**Key features:**
- Scans Logseq for [[socialpost]] candidates
- Drafts posts using linguistic fingerprint analysis (not generic AI patterns)
- Learns from Tim's edits through monthly refinement cycles
- Correlates voice patterns with engagement metrics
- Compounds quality over time

---

## Quick Start

```bash
cd /Users/timmetz/Developer/Projects/Personal/social-post-writer
/draft-linkedin-post
```

**What happens:**
1. Scans Logseq for 3 most recent [[socialpost]] entries
2. Shows options with page context
3. You select one
4. Claude drafts using your voice guide
5. Saves to Notion MyContent → Claude Draft field
6. You edit and publish

---

## The Compounding Loop

```
Logseq [[socialpost]]
    ↓
Claude drafts (using voice guide)
    ↓
Saves to Notion → Claude Draft
    ↓
Tim edits → Final version
    ↓
Post published → Engagement metrics
    ↓
Monthly refinement:
  - Analyze Tim's edits
  - Correlate with engagement
  - Update voice guide
    ↓
Next draft is better ↻
```

**Result:** Each post improves the system for future posts

---

## Project Structure

```
.claude/commands/
  └── draft-linkedin-post.md    # Main workflow command

voice/
  ├── tim-linkedin-voice-v1.md         # Current voice guide
  ├── tim-linguistic-fingerprint-v1.md # Deep linguistic analysis
  └── archive/                         # Previous versions

samples/tim/
  ├── 01-claude-code-style-guide.md    # Reference posts
  ├── 02-no-writing-no-thinking.md
  └── ... (7 total sample posts)

workflows/
  ├── post-creation.md         # Main drafting workflow
  └── voice-refinement.md      # Monthly learning loop

docs/
  └── SESSION_LOG.md          # Session notes

TASKS.md                      # Project tasks
README.md                     # This file
```

---

## How Voice Capture Works

### Phase 1: Initial Analysis (Complete)

Analyzed 7 high-performing LinkedIn posts to extract:

1. **Negative fingerprint** - What Tim NEVER says
   - "The real problem is..."
   - "isn't it... it's..." constructions
   - "Let's dive into..."
   - Generic LinkedIn-speak

2. **Positive fingerprint** - What Tim DOES say
   - "Turns out" for revelations
   - "For me," / "For October," for grounding
   - "My question for today:" for endings
   - "Here's what happened:" for narrative

3. **Micro-patterns**
   - White space as primary transition (50% of transitions)
   - Simple conjunctions ("So," "And," "But")
   - Radical sentence length variation
   - Trust reader to follow jumps

### Phase 2: Continuous Refinement (Ongoing)

**Monthly process:**
1. Compare Claude drafts to Tim's final versions
2. Extract recurring edit patterns
3. Correlate voice patterns with engagement metrics
4. Update voice guide with findings
5. Version increment

**Metrics tracked:**
- % of draft unchanged (voice accuracy)
- Engagement rate of Claude-drafted posts
- Time saved vs writing from scratch

---

## Integration with Existing Systems

### Logseq

**Source:** `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`
**Tag:** `[[socialpost]]`
**Usage:** Same scanning approach as logseq-dot5-review workflow

### Notion MyContent Database

**Database ID:** `131edc77-7df2-80be-a79e-edc6e0955fc2`

**New property added:**
- **Claude Draft** (rich text) - Stores initial AI-generated draft

**Existing properties used:**
- Reactions, Comments, Reposts, Impressions (engagement metrics)
- Engagement Rate (formula)
- Metrics Updated (date)
- Publishing date (date)
- Status (status)

**Workflow integration:**
- Claude saves draft → Claude Draft field
- Tim edits → Final version section in page body
- Metrics populate → Learning loop uses for refinement

---

## Voice Guide Philosophy

**Descriptive, not prescriptive**

This isn't about how Tim "should" write—it's about capturing how he ACTUALLY writes.

The guide documents:
- What he consistently does
- What he consistently avoids
- His subconscious linguistic patterns
- What correlates with high engagement

**Why this matters:**

Most AI writing sounds generic because it follows templates. This system learns Tim's actual voice through:
1. Forensic linguistic analysis
2. Negative pattern identification (what to avoid)
3. Iterative refinement from real edits
4. Engagement-driven optimization

---

## Usage Notes

### When to Use

**Good for:**
- Converting Logseq highlights into LinkedIn posts
- Maintaining consistent posting schedule
- First drafts that need Tim's voice
- Learning what voice patterns drive engagement

**Not for:**
- Posts requiring deep original thinking
- Sensitive/controversial topics
- Situations where authenticity requires Tim to write from scratch

### Best Practices

1. **Review Claude Draft thoughtfully** - It won't be perfect
2. **Edit freely** - Your edits train the system
3. **Run monthly refinement** - Learning loop requires consistency
4. **Version voice guides** - Keep history for rollback
5. **Check engagement patterns** - Data tells the truth

---

## Current Status

**✅ Complete:**
- Initial voice guide created (v1)
- Linguistic fingerprint documented (v1)
- 7 sample posts archived
- MyContent database configured
- Post creation workflow documented
- Voice refinement workflow documented

**⏳ Next Steps:**
- Test workflow on first real post
- Run first refinement cycle (after 5-10 posts)
- Iterate based on findings

---

## Performance Targets

**Voice accuracy:** 80%+ of draft unchanged after first refinement cycle
**Engagement:** Claude-drafted posts perform within 10% of manually written posts
**Efficiency:** 50% time savings on post creation

---

## Related Projects

- **my-os** (`/Users/timmetz/Developer/Projects/system/my-os`) - Personal automation system
- **logseq-dot5-review** - Similar Logseq scanning workflow for [[.5]] entries

---

## Questions?

- **How it works:** See `workflows/post-creation.md`
- **Learning loop:** See `workflows/voice-refinement.md`
- **Voice guide:** See `voice/tim-linkedin-voice-v1.md`
- **Linguistic analysis:** See `voice/tim-linguistic-fingerprint-v1.md`
