# Workflow Diagram Specification

> For creating the visual diagram for The Workflow podcast

## The 6-Step Flow

Create a horizontal or vertical flow diagram showing these 6 steps:

```
┌─────────────────────┐
│ 1. COLLECT          │
│ 15-20 published     │
│ articles            │
│ (scrape or local)   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ 2. GENERATE         │
│ /generate-style-    │
│ guide [brand]       │
│ (Claude Code)       │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ 3. REVIEW GUIDE     │
│ Human reviews       │
│ AI-extracted        │
│ patterns            │
└────────┬────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│ 4. STYLE CHECK                                      │
│ /style-check [brand] [article]                      │
│                                                     │
│ ┌─────────────────────────────────────────────────┐ │
│ │ 8 PARALLEL AGENTS                               │ │
│ │                                                 │ │
│ │ [1]Voice  [2]Grammar  [3]Punct  [4]Format      │ │
│ │ [5]Tech   [6]Content  [7]Terms  [8]Quick       │ │
│ │                                                 │ │
│ │ All run simultaneously = 4-5x speedup          │ │
│ └─────────────────────────────────────────────────┘ │
└────────┬────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────┐
│ 5. VIOLATIONS       │
│ REPORT              │
│ Line numbers +      │
│ exact corrections   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ 6. APPLY            │
│ Fix manually OR     │
│ use --auto-apply    │
│ flag                │
└─────────────────────┘
```

---

## Detailed Step Descriptions

### Step 1: COLLECT
**Visual element:** Blog with articles or folder with markdown files
**Label:** "Collect Articles"
**Subtext:** 15-20 representative articles
**Icon suggestion:** Folder or stack of documents
**What happens:** Gather published content that represents your brand voice

### Step 2: GENERATE
**Visual element:** Terminal window running command
**Label:** "Generate Style Guide"
**Subtext:** `/generate-style-guide [brand]`
**Icon suggestion:** Magic wand or generator icon
**What happens:** AI analyzes patterns across 8 editorial dimensions

### Step 3: REVIEW GUIDE
**Visual element:** Document with checkmarks
**Label:** "Review Generated Guide"
**Subtext:** Human verification
**Icon suggestion:** Eye or magnifying glass
**What happens:** Human reviews extracted rules, catches any misidentified patterns

### Step 4: STYLE CHECK
**Visual element:** 8 agents running in parallel (this is the "secret sauce")
**Label:** "Run Style Check"
**Subtext:** 8 parallel agents
**Icon suggestion:** Multiple runners or parallel arrows
**What happens:** Each agent reviews article against one section of style guide simultaneously

**Important detail to show:** The 8 agent boxes:
- Voice & Tone
- Grammar & Usage
- Punctuation
- Formatting
- Technical Standards
- Content Patterns
- Industry Terms
- Quick Reference

### Step 5: VIOLATIONS REPORT
**Visual element:** Report with line numbers
**Label:** "Get Violations Report"
**Subtext:** Line numbers + corrections
**Icon suggestion:** Clipboard or report
**What happens:** Detailed report with exact quotes, corrections, and rule citations

### Step 6: APPLY
**Visual element:** Document with corrections being applied
**Label:** "Apply Corrections"
**Subtext:** Manual or auto-apply
**Icon suggestion:** Checkmark or apply button
**What happens:** Fix issues manually or use `--auto-apply` for automatic fixes

---

## Human vs. Automated Indicators

Mark clearly which steps are automated vs. require human judgment:

| Step | Type | Notes |
|------|------|-------|
| 1. Collect | Semi-auto | Claude Code can scrape; or manual local files |
| 2. Generate | Automated | AI analyzes patterns |
| 3. Review Guide | Manual | Human verifies extracted rules |
| 4. Style Check | Automated | 8 parallel agents |
| 5. Violations Report | Automated | Generated output |
| 6. Apply | Choice | Manual OR automated |

**Total:** 1 manual decision (review guide), rest is automated

---

## The 8 Agents (Sidebar or Callout)

Show these 8 agents as a key visual element:

| # | Agent | Focus | Example Catch |
|---|-------|-------|---------------|
| 1 | Voice & Tone | Passive voice, pronoun consistency | "The article was written" → "We wrote" |
| 2 | Grammar & Usage | Oxford commas, Title Case | Missing comma in list |
| 3 | Punctuation | Em dashes, list punctuation | Wrong em dash spacing |
| 4 | Formatting | Headings, hyperlinks | H3 should be H2 |
| 5 | Technical Standards | Dates, numbers, percentages | "5%" → "5 percent" |
| 6 | Content Patterns | CTAs, openings | Missing call-to-action |
| 7 | Industry Terms | Acronyms, terminology | Undefined "CMS" |
| 8 | Quick Reference | Cross-check | Final sanity check |

---

## Alternative Simplified View

For the tier-1 (non-Claude-Code) audience:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   COLLECT   │ →  │   GENERATE  │ →  │ STYLE CHECK │ →  │    APPLY    │
│   15-20     │    │   Style     │    │  (8 agents  │    │ Corrections │
│   Articles  │    │   Guide     │    │  parallel)  │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      ↑                   ↑                  ↑                  ↓
      │                   │                  │                  │
 From your blog      50+ specific       4-5x faster         On-brand
 or local files      rules extracted   than manual         content
```

---

## Speed Comparison Visual

Consider adding a speed comparison:

```
MANUAL REVIEW
├── Voice & Tone ────────────────────────────────────> 5 min
├── Grammar & Usage ─────────────────────────────────> 5 min
├── Punctuation ─────────────────────────────────────> 5 min
├── Formatting ──────────────────────────────────────> 5 min
├── Technical Standards ─────────────────────────────> 5 min
├── Content Patterns ────────────────────────────────> 5 min
├── Industry Terms ──────────────────────────────────> 5 min
├── Quick Reference ─────────────────────────────────> 5 min
└── TOTAL: ~40+ minutes

8 PARALLEL AGENTS
├── All 8 agents run simultaneously ─────────────────> 5-10 min
└── TOTAL: 5-10 minutes (4-5x faster)
```

---

## Color Coding Suggestions

- **Blue:** Manual/human steps (Review Guide, manual Apply)
- **Green:** Automated steps (Collect, Generate, Style Check)
- **Orange/Gold:** The 8 parallel agents (the "secret sauce")

---

## Key Visual Emphasis

The diagram should emphasize:

1. **The 8 parallel agents box** - This is what makes the workflow fast
2. **Human review point** - Shows where judgment matters
3. **The speed comparison** - 4-5x faster than manual

---

## Recommended Tools for Creating

- **Miro** (their preferred tool)
- **FigJam**
- **Excalidraw** (hand-drawn feel)
- **Canva**
