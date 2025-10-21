# Draft LinkedIn Post

**Purpose:** Create LinkedIn post draft from Logseq [[socialpost]] entries using Tim's authentic voice

---

## Workflow

### Step 1: Scan Logseq for [[socialpost]] Entries

Search for `[[socialpost]]` tags in Tim's Logseq database and save to `/tmp/logseq_socialpost_entries.json`

### Step 2: Select 3 Most Recent Entries

Sort by file birth time and select the 3 most recent `[[socialpost]]` entries.

### Step 3: Extract Page Context

For each selected entry, extract additional highlights from the same source page to provide richer material for the post.

### Step 4: Present Options to User

Display all 3 entries with:
- The specific [[socialpost]] block
- Related highlights from same page
- Source file and age

### Step 5: Draft Post Using Authentic Voice

After user selects entry:

1. **Load voice guides:**
   - Read `voice/tim-linkedin-voice-v1.md`
   - Read `voice/tim-linguistic-fingerprint-v1.md`

2. **Analyze reference samples:**
   - Review posts in `samples/tim/` for current patterns
   - Identify similar post types for structural guidance

3. **Draft the post:**
   - Apply Tim's actual linguistic patterns (not AI generic ones)
   - Use his characteristic transitions and phrases
   - Match his sentence rhythm and white space usage
   - **Avoid AI-isms** listed in linguistic fingerprint

4. **Save draft to Notion:**
   - Create new page in MyContent database if needed
   - OR update existing page
   - Populate **Claude Draft** property with draft text
   - Set Status to "In progress"

### Step 6: Report Back

Provide user with:
- Link to Notion page
- Draft preview
- Note on which voice patterns were applied

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

---

## Files Referenced

- Voice guide: `voice/tim-linkedin-voice-v1.md`
- Linguistic fingerprint: `voice/tim-linguistic-fingerprint-v1.md`
- Sample posts: `samples/tim/*.md`
- Logseq location: `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`
- MyContent database ID: `131edc77-7df2-80be-a79e-edc6e0955fc2`
