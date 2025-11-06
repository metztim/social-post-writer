# Draft LinkedIn Post - v2

**Purpose:** Create LinkedIn post draft from Logseq [[socialpost]] entries using Tim's authentic voice

**Version:** 2.0
**Status:** Production Ready
**Last Updated:** 2025-11-06

---

## What's New in v2

**🔧 Self-Contained & Maintainable:**
- Dedicated `scripts/scan_socialpost.py` for robust scanning
- Step-by-step documentation in `steps/` directory
- Python-first approach (no bash for file operations)
- Proper file handling for special characters

**🎯 Prevention Over Detection:**
- Step 6 removes [[socialpost]] tag after use
- Entries naturally excluded from future scans
- Preserves history with Notion link in note

**📚 No External Dependencies:**
- All learnings internalized
- Self-contained workflow
- No references to other projects

---

## Quick Start

Run through the workflow steps in order. Each step has detailed instructions in its own file.

---

## Workflow Steps

### Step 1: Scan Logseq for [[socialpost]] Entries
→ See [`steps/1-scan.md`](steps/1-scan.md)

Find all blocks with [[socialpost]] tags.

**Implementation:** `scripts/scan_socialpost.py` - Python script with full extraction logic
**Output:** List of entries saved to `/tmp/logseq_socialpost_entries.json`

**Critical:** Uses Python (not bash) for robust handling of:
- URL-encoded filenames (%3A for :)
- Curly quotes in titles
- Special characters

---

### Step 2: Select 3 Most Recent Entries
→ See [`steps/2-select.md`](steps/2-select.md)

Sort by file birth time and select 3 most recent.

**Output:** Selected entries saved to `/tmp/logseq_socialpost_top3.json`

---

### Step 3: Present Options to User
→ See [`steps/3-present.md`](steps/3-present.md)

Display all 3 entries with:
- The specific [[socialpost]] block
- Related highlights from same page
- Source file and age
- All relevant tags

**Critical:** Show full content, never truncate

---

### Step 4: Draft Post Using Authentic Voice
→ See [`steps/4-draft.md`](steps/4-draft.md)

After user selects entry:

1. **Load voice guides:**
   - `voice/tim-linkedin-voice-v2.md`
   - `voice/tim-linguistic-fingerprint-v2.md`

2. **Analyze reference samples:**
   - Review posts in `samples/tim/` for current patterns
   - Identify similar post types for structural guidance

3. **Draft the post:**
   - Apply Tim's actual linguistic patterns (not AI generic)
   - Use his characteristic transitions and phrases
   - Match his sentence rhythm and white space usage
   - **Avoid AI-isms** listed in linguistic fingerprint

4. **Self-review draft:**
   - Validate against Voice Authenticity Checklist
   - Check for AI patterns
   - Revise if needed

**Quality Bar:** Must sound authentically like Tim, not generic LinkedIn copy

---

### Step 5: Save Draft to Notion
→ See [`steps/5-save-notion.md`](steps/5-save-notion.md)

Create new page in MyContent database:
- Populate **Claude Draft** property with draft text
- Set **Type** to "LinkedIn post"
- Set **Status** to "In progress"

**Database ID:** `131edc77-7df2-80be-a79e-edc6e0955fc2`

**Report back:**
- Link to Notion page
- Draft preview
- Voice patterns applied

---

### Step 6: Mark Entry as Used
→ See [`steps/6-mark-used.md`](steps/6-mark-used.md)

Update source Logseq entry:
1. Remove [[socialpost]] tag
2. Add note with link to Notion post

**Why:** Prevents reuse in future workflow runs automatically

**Example transformation:**
```markdown
Before:
- **Tags**: #[[socialpost]] #[[topic]] #[[.3]]

After:
- **Tags**: #[[topic]] #[[.3]]
  - **Note**: Used in [Post Title](https://notion.so/page-id)
```

---

## Critical Rules

**Voice Authenticity:**
- NEVER use phrases from "Tim would never say" list
- ALWAYS use Tim's actual transition words (not generic ones)
- Trust white space—don't over-explain connections
- Lead with concrete, specific, personal

**Quality Bar:**
- If draft doesn't sound authentically like Tim, flag it and try again
- Better to admit uncertainty than fake his voice

**File Handling:**
- Always use Python for Logseq file operations
- Never use bash find/grep/ls (fails on special characters)
- Handle URL encoding and curly quotes properly

---

## Files Referenced

**Voice guides:**
- `voice/tim-linkedin-voice-v2.md`
- `voice/tim-linguistic-fingerprint-v2.md`

**Sample posts:**
- `samples/tim/*.md`

**Logseq location:**
- `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`

**MyContent database:**
- Database ID: `131edc77-7df2-80be-a79e-edc6e0955fc2`

---

## Version History

### v2 - 2025-11-06
- **NEW:** Self-contained workflow structure with steps/ and scripts/
- **NEW:** Step 6 - Mark entries as used (remove [[socialpost]] tag)
- **NEW:** Python-first approach for all file operations
- **IMPROVED:** Robust handling of special characters in filenames
- **IMPROVED:** No external workflow dependencies
- **FIXED:** File encoding and special character issues

### v1 - 2024-11-01
- Initial workflow creation
- Basic [[socialpost]] scanning
- Voice-based drafting

---

## Related Files

**Current Version (v2):**
- Main orchestrator: `workflows/post-creation/draft-linkedin-post-v2.md` (this file)
- Scan script: `workflows/post-creation/scripts/scan_socialpost.py`
- Step files: `workflows/post-creation/steps/*.md`

**Previous Version:**
- `workflows/archive/draft-linkedin-post-v1.md`

**Slash Command:**
- `.claude/commands/draft-linkedin-post.md` (points to this workflow)
