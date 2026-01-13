# Screenshot Capture Instructions

> 6 screenshots needed for The Workflow podcast

---

## Before You Start

1. Have a folder with 5-10 sample articles (markdown or can scrape from blog)
2. Have an existing brand style guide (or be ready to generate one)
3. Have terminal ready with Claude Code
4. Have a test article to run style check on

---

## Screenshot 1: Source Articles

**What to capture:** A folder showing source articles or a blog page to scrape from

**Setup:**
1. Show a folder with several markdown files OR
2. Show a blog homepage with article titles visible

**Good to show:**
- Multiple article files (suggests volume)
- Recognizable file names or article titles
- Clean, organized structure

**Capture area:** Folder view or browser showing blog

---

## Screenshot 2: Terminal - Generate Style Guide

**What to capture:** Terminal showing Claude Code running the generation command

**Command to run:**
```bash
/generate-style-guide animalz /path/to/articles/
```

**Good to show:**
- The command being entered
- Output showing articles being analyzed
- Progress indicator or "Analyzing X articles..."

**Capture area:** Terminal window showing the generation process

---

## Screenshot 3: Generated Style Guide Excerpt

**What to capture:** A section of the generated style guide showing the 8-section structure

**Setup:**
1. Open the generated style guide markdown file
2. Scroll to show the table of contents OR
3. Show one section with DO/DON'T examples

**Good to show:**
- The 8 section structure (Voice & Tone, Grammar & Usage, etc.)
- Specific rules with ✅ DO and ❌ DON'T examples
- Evidence that it's comprehensive (50+ rules)

**Capture area:** Part of the style guide showing structure and detail

---

## Screenshot 4: Terminal - Run Style Check

**What to capture:** Terminal showing the style check command with 8 agents launching

**Command to run:**
```bash
/style-check animalz /path/to/test-article.md
```

**Good to show:**
- The command being entered
- Visual indication that 8 agents are running in parallel
- Agent names or progress indicators

**Capture area:** Terminal showing the parallel agent execution

---

## Screenshot 5: Violations Report

**What to capture:** The output report showing violations with line numbers and corrections

**Good to show:**
- Violation entries with line numbers
- Current text (exact quote)
- Suggested correction
- Rule being cited
- Summary at the end (e.g., "Total violations: 12")

**Capture area:** Several violations from the report (show 3-5 examples)

---

## Screenshot 6: Before/After Article Comparison

**What to capture:** Side-by-side or before/after showing corrections applied

**Setup:**
1. Show a section of the original article with issues
2. Show the same section after corrections

**Good to show:**
- Specific fixes (e.g., missing Oxford comma added)
- Clean, professional result
- Minimal changes needed (most content unchanged)

**Capture area:** Relevant portion showing the improvement

---

## Bonus Screenshots (Optional)

### The 8 Agents Running
**What:** Close-up of terminal showing all 8 agents running simultaneously
**Shows:** The "parallel is the unlock" concept visually

### Speed Comparison
**What:** Timer or log showing 5-10 minute completion
**Shows:** The 4-5x speedup claim is real

### Batch Review Output
**What:** Portfolio-level report from `/batch-review`
**Shows:** Scalability—works on 1 or 100 articles

---

## Tips for Good Screenshots

1. **Clean terminal:** Clear before capturing, or crop to relevant section
2. **Font size:** Make sure text is readable at article size
3. **Crop tight:** Don't include extra whitespace or unrelated UI
4. **Consistent style:** Same window size/zoom across screenshots
5. **Blur sensitive info:** Remove any private content if needed
6. **Real output:** Use actual generated content, not mock-ups

---

## Naming Convention

Save screenshots as:
- `01-source-articles.png`
- `02-terminal-generate.png`
- `03-style-guide-excerpt.png`
- `04-terminal-style-check.png`
- `05-violations-report.png`
- `06-before-after.png`

Upload to The Workflow's Google Drive folder.
