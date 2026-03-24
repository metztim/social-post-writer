---
source_of_truth: /Users/timmetz/Developer/Projects/Personal/writing-assistant/projects/articles/knowledge-base-daily-review/format-template.md
note: Reusable format template for WER workflow/command explanation articles
---

# WER Workflow Article Format Template

> Standardized format for We Eat Robots articles that explain AI workflows, commands, or processes. Balances accessibility with depth — readers grasp the system without drowning in prompt-level detail.

## Design principles

1. **Show the shape, not every pixel.** Describe what each part does and why it exists. Don't reproduce every prompt or instruction verbatim — that's what the repo link is for.
2. **Interactivity over length.** Where a reader might want more detail on a specific section, provide a "paste this prompt" block that references the public repo. Keeps the article scannable while giving power users a path to depth.
3. **MECE sections.** Each H2 covers one distinct concern. No overlap between sections.
4. **Concrete over abstract.** Every section includes at least one specific example, screenshot, or output sample.

---

## Required H2 sections

### 1. Hook + context (no H2 heading — this is the intro)
What problem does this workflow solve? Why did you build it? Open with a concrete moment or frustration that led to creating it. Keep this to 2-3 short paragraphs.

### 2. What it does
One-paragraph overview of the workflow's purpose and scope. What goes in, what comes out, how long does it take. Include the Whimsical flowchart here.

**Required element:** Whimsical flowchart showing the workflow's major phases and decision points.

### 3. How it works
Walk through the major phases/steps at a conceptual level. Group related steps into logical blocks rather than listing every individual step. For each block:
- What it does (1-2 sentences)
- Why it matters (1 sentence)
- One concrete example of its output

This is the "meat" section but should stay at the block/phase level, not the individual-prompt level.

**Required element:** "Go deeper" prompt blocks for readers who want more detail on specific phases. Format:

```
> **Want more detail on [phase name]?** Paste this into Claude, ChatGPT, or your AI tool of choice:
>
> "Read the [step-name].md file at [repo-url]/workflows/[path] and explain how [specific aspect] works, including what tools it uses and what the output looks like."
```

### 4. What you need to run it
Prerequisites, dependencies, and setup. What tools/accounts/APIs does the workflow require? Link to the public repo with installation instructions.

**Required element:** Link to installable command/plugin or public repo.

### 5. How it evolved
5-7 bullet points showing key milestones in the workflow's development. Not a changelog — a curated narrative of the most interesting inflection points. What was added, removed, or fundamentally rethought, and why.

Format:
- **[Milestone label]:** One sentence describing what changed and why. (Approximate date or version.)

### 6. What I'd change next
1-3 things you're considering changing or adding. Shows the workflow is alive and thinking is ongoing. Invites reader input.

### 7. CTA
One simple question inviting readers to share their own approach or ask questions. No framing — just the question.

---

## Flowchart spec

Each article includes a Whimsical flowchart. Guidelines for the flowchart:

- **Granularity:** Show major phases and key decision points. Do NOT show every individual step or prompt.
- **Shape conventions:** Per Whimsical standards in CLAUDE.md:
  - Rectangle = automated processes (AI steps)
  - Pill = human actions (user input, review)
  - Diamond = decisions (weekend mode, optional elements)
  - Cylinder = data stores (Notion, Logseq, cache files)
  - Ellipse = outputs (health snapshot, task confirmations)
- **Color:** Single color (Purple-500 #9463EE) unless differentiation serves clarity.
- **Layout:** Top-to-bottom flow. Parallel branches shown side by side. Aim for 10-15 nodes max.

---

## "Go deeper" prompt block format

Standardized format for in-article prompt blocks:

```markdown
> **Want more detail on [section topic]?** Paste this into your AI tool:
>
> "I'm reading about [workflow name] from [repo URL]. Explain how the [specific component] works — what does it do step by step, what tools does it call, and what does the output look like? Reference the source files at [specific path]."
```

Rules:
- One per major section of "How it works" (not every sub-step)
- Always reference the public repo URL so the AI tool can read the source
- Frame the question around what the reader likely wants to understand
- Keep the prompt under 3 sentences

---

## Evolution section guidelines

- Exactly 5-7 bullet points (strict)
- Chronological order
- Each bullet: bold label + one sentence + approximate timeframe
- Include at least one "we tried X and it didn't work" moment
- Include at least one "new capability unlocked Y" moment
- Rewrite this section with each article update to keep it curated (don't just append)

---

## Article metadata

Every workflow article should include in its YAML frontmatter:
- `workflow_repo`: URL to the public repo
- `workflow_path`: Path within the repo to the workflow files
- `last_workflow_update`: Date of last significant workflow change
- `article_version`: Increment when article is substantially updated

---

## Anti-patterns (from Tim's voice memo)

- **Don't reproduce every prompt.** That's what the repo is for.
- **Don't overlap between sections.** If "How it works" explains what a step does, "What it does" shouldn't repeat it — it should stay at the overview level.
- **Don't write a changelog.** The evolution section is curated storytelling, not a commit log.
- **Don't be too high-level.** Each section needs at least one concrete example, output sample, or specific detail.
- **Don't resemble "The Workflow" interview format.** Keep sections clean and distinct.
