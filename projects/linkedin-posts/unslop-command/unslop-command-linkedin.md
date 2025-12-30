# LinkedIn Version (2,847 characters)

We drown in workslop because it's so easy to create seemingly useful materials with Claude Code. Enter the /unslop command.

Frustrated with the pile of slop I wade through daily (thanks to Claude Code, not my coworkers 😃), I made a command I can point at any bloated text file.

**The problem:**

LLMs repeat themselves. Constantly.

You write "don't use title case" at the start of a prompt. Other instructions follow. Your output still has title case.

So you add at the end: "Remember, don't use title case!" It works.

But when you're generating documentation at scale with Claude Code, this becomes a vicious cycle: Important instructions get repeated → previous instructions get forgotten → more reminders get added → files bloat → clarity drops → more repetition needed.

**The solution:**

An 18-line command based on three principles:

• MECE: Non-overlapping sections that cover the whole topic
• DRY: One source of truth, referenced everywhere
• Simplicity: As simple as possible, but not simpler

Here's the entire command:

```
Analyze the specified file for bloat and propose a streamlined version.

Apply these Writing Standards:
- MECE (Mutually Exclusive, Collectively Exhaustive): Non-overlapping sections that cover the whole topic
- DRY (Don't Repeat Yourself): One source of truth, referenced everywhere
- Essential: Only include what's necessary

For each section, challenge:
- Cut? Is this essential or inferable?
- Relocate? Does it belong elsewhere?
- Redundant? Is this repeated? Cross-reference instead.

Propose:
1. Sections to cut (with justification)
2. Sections to relocate (with destination)
3. Streamlined version
4. Before/after line count

Be aggressive but not simplistic: "as simple as possible, but not simpler."
```

**What it does:**

Point it at any file and it shows you which sections to cut (with reasons), what to relocate, and a streamlined version with before/after line counts.

Results: 30-50% reduction in most files. The amazing part? Instructions often work better. Less really is more.

**Try it:**

Back up your files first. Then save the command above to `~/.claude/commands/unslop.md` and run `/unslop [file-pattern]` on any documentation.

I used it on my entire Claude Code library. It found thousands of unnecessary lines. Including, embarrassingly, in the file that defined these principles.

The meta-lesson: The best tool for fighting AI slop is AI itself—pointed at the right target with clear constraints.

Try it on your documentation. You might be surprised what it finds.
