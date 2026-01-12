# Workflow Diagram Specification

> For creating the visual diagram for The Workflow podcast

## The 6-Step Flow

Create a horizontal or vertical flow diagram showing these 6 steps:

```
┌─────────────────┐
│ 1. TAG          │
│ Highlight in    │
│ Logseq          │
│ [[socialpost]]  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. SCAN         │
│ Claude Code     │
│ finds entries   │
│ (Python script) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. SELECT       │
│ Present 3 most  │
│ recent options  │
│ (Human choice)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ 4. DRAFT                            │
│ Claude Code applies voice guide     │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ Voice Fingerprint               │ │
│ │ • What I NEVER say              │ │
│ │ • My actual patterns            │ │
│ │ • Em-dash rhythm                │ │
│ │ • Sentence structure            │ │
│ └─────────────────────────────────┘ │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────┐
│ 5. SAVE         │
│ Notion API      │
│ MyContent DB    │
│ "Claude Draft"  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 6. CLEANUP      │
│ Remove tag      │
│ Add Notion link │
│ Prevent reuse   │
└─────────────────┘
```

---

## Detailed Step Descriptions

### Step 1: TAG
**Visual element:** Logseq page with highlighted text
**Label:** "Tag in Logseq"
**Subtext:** `[[socialpost]]`
**Icon suggestion:** Bookmark or tag icon
**What happens:** While reading, tag interesting highlights that could become posts

### Step 2: SCAN
**Visual element:** Terminal window with code running
**Label:** "Claude Code Scans"
**Subtext:** Python script
**Icon suggestion:** Magnifying glass
**What happens:** `/draft-linkedin-post` command triggers scan of entire knowledge base

### Step 3: SELECT
**Visual element:** List with checkboxes or options
**Label:** "Choose Entry"
**Subtext:** Human selection
**Icon suggestion:** Hand pointing or checkbox
**What happens:** 3 most recent entries displayed, user picks one to develop

### Step 4: DRAFT
**Visual element:** Document being written with a style guide reference
**Label:** "AI Drafts with Voice"
**Subtext:** 900+ line fingerprint
**Icon suggestion:** Pen + document
**What happens:** Claude Code loads voice guides and creates authentic draft

**Important detail to show:** The voice fingerprint box with:
- "What I NEVER say"
- "My actual patterns"
- "Em-dash rhythm"

### Step 5: SAVE
**Visual element:** Notion logo or database icon
**Label:** "Save to Notion"
**Subtext:** MyContent database
**Icon suggestion:** Cloud or database
**What happens:** Draft saved with metadata, ready for editing

### Step 6: CLEANUP
**Visual element:** Tag being removed
**Label:** "Mark as Used"
**Subtext:** Prevents reuse
**Icon suggestion:** Check mark or archive
**What happens:** Original tag removed, link added to Notion post

---

## Human vs. Automated Indicators

Mark clearly which steps are automated vs. require human judgment:

| Step | Type | Notes |
|------|------|-------|
| 1. Tag | Manual | Human taste - what's worth developing |
| 2. Scan | Automated | Python script finds all entries |
| 3. Select | Manual | Human choice - which entry today |
| 4. Draft | Automated | Claude Code + voice guide |
| 5. Save | Automated | Notion API |
| 6. Cleanup | Automated | File modification |

**Total:** 2 manual decisions, 4 automated steps

---

## Tools to Show

In a separate "Tool Stack" section or sidebar:

- **Logseq** - Knowledge base / reading highlights
- **Claude Code** - AI orchestration and drafting
- **Python** - File scanning (handles special characters)
- **Voice Guide** - Markdown files with linguistic patterns
- **Notion** - Draft storage and workflow management

---

## Alternative Simplified View

For the tier-1 (non-Claude-Code) audience:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   COLLECT   │ →  │   CREATE    │ →  │    DRAFT    │ →  │   REFINE    │
│  Highlights │    │ Fingerprint │    │  with Voice │    │  & Publish  │
│  in Notes   │    │  (once)     │    │    Guide    │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      ↑                   ↑                  ↑                  ↓
      │                   │                  │                  │
   Any notes           Analyze your       ChatGPT/Claude    Track what
   app works           own posts          with prompt       you change
```

---

## Color Coding Suggestions

- **Blue:** Manual/human steps (Tag, Select)
- **Green:** Automated steps (Scan, Draft, Save, Cleanup)
- **Orange/Gold:** The voice fingerprint (the "secret sauce")

---

## Key Visual Emphasis

The diagram should emphasize:

1. **The voice fingerprint box** - This is what makes the workflow unique
2. **Human judgment points** - Showing where taste/selection matters
3. **The feedback loop** - Edits improve the fingerprint over time

Consider adding a dotted feedback arrow from Step 5 back to the voice fingerprint, labeled "Edits improve fingerprint"

---

## Recommended Tools for Creating

- **Miro** (their preferred tool)
- **FigJam**
- **Excalidraw** (hand-drawn feel)
- **Canva**
