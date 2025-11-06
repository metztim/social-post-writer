# Draft LinkedIn Post

**Purpose:** Create LinkedIn post draft from Logseq [[socialpost]] entries using Tim's authentic voice

**Workflow:** See [`workflows/post-creation/draft-linkedin-post-v2.md`](../../workflows/post-creation/draft-linkedin-post-v2.md)

---

## Quick Overview

1. **Scan** Logseq for [[socialpost]] tags (using Python script)
2. **Select** 3 most recent entries
3. **Present** options to user with full context
4. **Draft** post using Tim's authentic voice
5. **Save** to Notion MyContent database
6. **Mark** entry as used (remove [[socialpost]] tag)

---

## Key Features

**Self-Contained:**
- Dedicated scan script in `workflows/post-creation/scripts/`
- Step-by-step documentation in `workflows/post-creation/steps/`
- No external dependencies

**Robust File Handling:**
- Python-first (handles special characters)
- Proper URL encoding and curly quotes
- File birth time for age sorting

**Duplication Prevention:**
- Step 6 removes [[socialpost]] tag after use
- Adds note with Notion link
- Entry won't appear in future scans

**Voice Authenticity:**
- Uses Tim's actual linguistic patterns
- Self-validation against voice guides
- Quality bar: sounds like Tim (not generic AI)

---

## Files Referenced

**Main workflow:** `workflows/post-creation/draft-linkedin-post-v2.md`
**Voice guides:** `voice/tim-linkedin-voice-v2.md`, `voice/tim-linguistic-fingerprint-v2.md`
**Sample posts:** `samples/tim/*.md`
**Logseq:** `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`
**Notion DB:** `131edc77-7df2-80be-a79e-edc6e0955fc2`

---

## Previous Version

**v1:** Archived to `workflows/archive/draft-linkedin-post-v1.md`
