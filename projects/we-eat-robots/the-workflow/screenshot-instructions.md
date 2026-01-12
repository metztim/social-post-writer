# Screenshot Capture Instructions

> 6 screenshots needed for The Workflow podcast

---

## Before You Start

1. Make sure you have at least one `[[socialpost]]` tagged entry in Logseq
2. Have Notion open in browser
3. Have terminal ready with Claude Code

---

## Screenshot 1: Logseq with Tag

**What to capture:** A Logseq page showing a highlight with the `[[socialpost]]` tag

**Setup:**
1. Open Logseq
2. Navigate to a page with a tagged highlight
3. Make sure the `[[socialpost]]` tag is clearly visible
4. Show some surrounding context (the highlight text, maybe other tags)

**Good to show:**
- The tag syntax: `[[socialpost]]`
- The highlight text that would become a post
- Any related tags like source or topic

**Capture area:** The block with the tag + 1-2 surrounding blocks

---

## Screenshot 2: Terminal - Scanning

**What to capture:** Terminal showing Claude Code scanning for entries

**Command to run:**
```bash
cd /Users/timmetz/Library/CloudStorage/Dropbox/Logseq
python3 /Users/timmetz/Developer/Projects/Personal/writing-assistant/workflows/post-creation/scripts/scan_socialpost.py
```

**Good to show:**
- The "Scanning Logseq for [[socialpost]] entries..." message
- The count of entries found
- The output file path

**Capture area:** Terminal window showing the scan running/completed

---

## Screenshot 3: Terminal - Options Presented

**What to capture:** Claude Code showing the 3 most recent entries

**How to get here:**
Run the `/draft-linkedin-post` command and capture when it displays the options

**Good to show:**
- Entry numbers (1, 2, 3)
- The highlight text for each
- Source file names
- The "Select entry" prompt

**Capture area:** Terminal showing all 3 options clearly

---

## Screenshot 4: Terminal - Drafting

**What to capture:** Claude Code generating the draft with voice guide

**How to get here:**
Select an entry and capture while Claude is:
- Loading voice guides
- Analyzing the entry
- Generating the draft

**Good to show:**
- Reference to voice guide files being loaded
- The drafting process happening
- Perhaps a preview of the draft output

**Capture area:** Terminal showing the drafting activity

---

## Screenshot 5: Notion - Saved Draft

**What to capture:** The Notion page with the Claude Draft property filled

**Setup:**
1. Open Notion to MyContent database
2. Find the newly created entry
3. Expand to show the "Claude Draft" property

**Good to show:**
- Page title
- "Claude Draft" property with the draft text
- "Type: LinkedIn post" property
- "Status: In progress" property

**Capture area:** Notion page with key properties visible

---

## Screenshot 6: Logseq - Tag Removed

**What to capture:** The original entry with tag removed and Notion link added

**Setup:**
1. Go back to Logseq
2. Navigate to the source file that was processed
3. Show the entry with:
   - `[[socialpost]]` tag REMOVED
   - Note with Notion link ADDED

**Good to show:**
- The same highlight from Screenshot 1
- The tag is now gone
- A note showing the Notion link

**Capture area:** The modified block showing the cleanup

---

## Bonus Screenshots (Optional)

### Voice Guide Excerpt
**What:** The voice fingerprint file showing the "never say" list
**File:** `voice/tim-linguistic-fingerprint-v2.md`
**Section:** Part 4 - "Tim Would Never Say" list

### Before/After Comparison
**What:** A Claude draft side-by-side with the final published post
**Shows:** The 75% accuracy and what gets edited

### Engagement Metrics
**What:** LinkedIn analytics showing engagement on a Claude-drafted post
**Shows:** That the workflow actually works

---

## Tips for Good Screenshots

1. **Clean terminal:** Clear before capturing, or crop to relevant section
2. **Font size:** Make sure text is readable at article size
3. **Crop tight:** Don't include extra whitespace or unrelated UI
4. **Consistent style:** Same window size/zoom across screenshots
5. **Blur sensitive info:** Remove any private Logseq content if needed

---

## Naming Convention

Save screenshots as:
- `01-logseq-tag.png`
- `02-terminal-scan.png`
- `03-terminal-options.png`
- `04-terminal-drafting.png`
- `05-notion-saved.png`
- `06-logseq-cleanup.png`

Upload to The Workflow's Google Drive folder.
