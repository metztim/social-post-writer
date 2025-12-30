# Fighting AI Slop with the /unslop Command

We drown in workslop because it's so easy to create lots of seemingly useful materials, especially with a powerful tool like Claude Code. Enter the /unslop command.

Frustrated with the pile of slop I wade through daily (thanks to Claude Code, not my coworkers 😃), I've made an /unslop command that I can point at any text file.

## Why LLMs create bloat

One of AI's biggest sins when generating instructions and documentation: it repeats itself. Constantly.

Here's why: LLMs repeat instructions that are important. You might say at the start of a prompt: "don't use title case." Then a bunch of other instructions follow, and your output still has title case.

The common solution? Add at the end: "Remember, don't use title case!" This usually works.

But this becomes problematic when you're designing and generating workflows, instructions, and reference files at industrial scale—as happens with Claude Code projects.

Because important instructions get repeated, previous important instructions get forgotten, so more reminders for those get added in and across files, and on and on. A vicious cycle of bloat.

## Three principles to fight it

The /unslop command is based on three principles:

**MECE** (Mutually Exclusive, Collectively Exhaustive): Partition content into non‑overlapping buckets that, together, cover the whole topic. If something fits two buckets, the buckets are wrong. If something fits none, you're missing one.

**DRY** (Don't Repeat Yourself): Establish a single source of truth for each fact, rule, or step; reuse it by reference (link, include, variable) instead of copy‑pasting. When it changes, you update it once.

**Simplicity heuristic**: "Make things as simple as possible, but not simpler." Use it to decide when to merge, trim, or reference; if a cut would drop a necessary distinction, keep it.

## The command itself

Here's the entire thing—18 lines:

```markdown
Analyze the specified file for bloat and propose a streamlined version.

Apply these Writing Standards:
- MECE (Mutually Exclusive, Collectively Exhaustive): Non-overlapping sections that cover the whole topic
- DRY (Don't Repeat Yourself): One source of truth, referenced everywhere
- Essential: Only include what's necessary

For each section, challenge:
- **Cut?** Is this essential or inferable?
- **Relocate?** Does it belong elsewhere (docs/, component CLAUDE.md, README, etc.)?
- **Redundant?** Is this repeated? Cross-reference instead.

Propose:
1. Sections to cut (with justification)
2. Sections to relocate (with destination)
3. Streamlined version
4. Before/after line count

Be aggressive but not simplistic: "as simple as possible, but not simpler."
```

That's it. No configuration, no dependencies, no complexity.

## What it does

Point it at any file and it shows you:
- Which sections to cut (with justification)
- Which info to move or reference from other files
- A streamlined version
- Before/after line count

It cuts down most of my files by at least 30%, often more than 50%.

The amazing thing? The instructions often work better. Less really is more.

## Try it yourself

**As a slash command:**
1. Back up your files first
2. Copy the command above
3. Save it to `~/.claude/commands/unslop.md` (create the directory if needed)
4. Restart Claude Code
5. Run `/unslop [file-pattern]` on any documentation

**As a skill (recommended):**
Coming soon—I'll be publishing this as a proper Claude skill that can automatically detect bloated documentation.

## The meta-lesson

The best tool for fighting AI slop is AI itself—just pointed at the right target with clear constraints.

Try it on your documentation. You might be surprised what it finds.

I used this command on my entire Claude Code documentation library. It found thousands of unnecessary lines. Including, embarrassingly, in the file that defined these principles.
