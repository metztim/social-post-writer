# LinkedIn Post: The /copywrite Command
**Status:** Draft
**Date:** 2026-02-27

---

At **Animalz**, *Hey Whipple, Squeeze This* by **Luke Sullivan** is making the rounds. And I thought — what if these advertising principles could actually enforce themselves while I'm writing copy?

It became much more than one book.

I built a `/copywrite` slash command for **Claude Code** — a 7-phase copywriting process grounded in everything I've read about the craft. Brief, Strategy, Research, Exploration, Selection, Full Copy, Review. Each phase has quality gates you can't skip past.

**Harry Dry**'s three laws sit at the center: "Can I visualize it? Can I falsify it? Can nobody else say this?" Every variant you write gets scored against all three. **Sullivan**'s concepting lenses — invert, exaggerate, try metaphor, try before/after — push you into new directions when you hit a wall. **Joanna Wiebe**'s Money Words framework catches interference: "Every time you use the word 'and,' you lose a conversion." And there are about ten more — **Ogilvy**, **Sugarman**, **Beckwith**, **Kaplan's Law** — each contributing a specific quality gate or test. (Full reading list in the comments.)

But none of it matters without the core design decision — the human fills the blank page.

In strict mode, AI never gives the first suggestion. It asks questions and waits. In the Exploration phase, you write 15+ variants before AI helps extend. And the pushback is specific:

"You've got 8. Most follow the same pattern. What else is there?"

"None of these are falsifiable yet."

"You're being safe. What's the version that scares you a little?"

So the AI isn't doing the work. It's making sure you can't skip it.

You can do this with any book. Read something that changes how you think about a craft. Distill the principles into phases, quality gates, and pushback prompts. Turn it into a structured process your AI guides you through. Your AI is only as good as the frameworks you give it.

What book would you turn into a command?

(Plugin link in the comments.)

---

## First Comment

The reading list behind `/copywrite` — every book and framework that feeds into the command:

- *Hey Whipple, Squeeze This* — Luke Sullivan (concepting lenses, "say it straight then say it great")
- Marketing Examples — Harry Dry (three laws, volume mandate, "bleed the tap dry")
- Copyhackers — Joanna Wiebe (Money Words, interference, the You Rule)
- *Selling the Invisible* — Harry Beckwith ("if it's this hard to write the ad, the product is flawed")
- *Crossing the Chasm* — Geoffrey Moore (positioning statement template)
- *A Smile in the Mind* — Beryl McAlhone ("the audience travels 5-40% to unlock the puzzle")
- David Ogilvy ("write to each of them a letter")
- Joe Sugarman (two-line ad structure: curiosity then payoff)
- Pete Barry ("print is to advertising what figure drawing is to fine art")
- Lisa Cron (visualization test: "if I can't see it, it's not there yet")
- Kevin Kelly ("start from the cover and the headline")
- Kaplan's Law ("any word not working for you is working against you")

[Plugin link when ready]

---

## VISUAL: Tree View (for image generation)

```
/copywrite — Structured Copywriting Process
═══════════════════════════════════════════════════════════════════

PHASE 1: BRIEF                                    ┌─────────────────────────┐
├── 1a. Deliverable type                           │ SULLIVAN                │
│   (landing page / ad / email / tagline / social) │ "This is an ad about…"  │
├── 1b. Audience                                   │                         │
│   Who, where, emotional state                    │ HARRY DRY               │
├── 1c. Attitude shift                             │ "Current attitude is the │
│   Point A → Point B                              │  starting point"        │
├── 1d. "This is an ad about…" test                │                         │
├── 1e. Constraints                                └─────────────────────────┘
│
│   GATE: All answers confirmed. No vague audiences.
│
PHASE 2: STRATEGY                                  ┌─────────────────────────┐
├── 2a. Core truth                                 │ SULLIVAN                │
│   Sullivan's bar test + counterargument test     │ Bar test, brand =       │
├── 2b. SOCO                                       │ adjective               │
│   Single Overriding Communications Objective     │                         │
├── 2c. SOCA                                       │ BECKWITH                │
│   Single Overriding Communications Avoidance     │ "If it's this hard to   │
├── 2d. Positioning statement (optional)           │  write the ad…"         │
│   Geoffrey Moore template                        │                         │
│                                                  │ WIEBE                   │
│   GATE: Bar test passed. SOCO contains no "and." │ "Every 'and' loses a    │
│                                                  │  conversion"            │
│                                                  │                         │
│                                                  │ MOORE                   │
│                                                  │ Positioning template    │
│                                                  └─────────────────────────┘
│
PHASE 3: RESEARCH                                  ┌─────────────────────────┐
├── 3a. Competitive copy audit                     │ WIEBE                   │
│   3-5 competitors, exact words                   │ "Same words = inter-    │
├── 3b. Voice of customer                          │  ference"               │
│   Real language from reviews, calls, forums      │                         │
├── 3c. Reference copy                             │                         │
│   Great examples and why they work               └─────────────────────────┘
│
│   GATE: 3+ competitors collected. Category clichés listed. Customer language captured.
│
PHASE 4: EXPLORATION                               ┌─────────────────────────┐
├── 4a. Word association                           │ HARRY DRY               │
│   Product, pain, outcome, category, emotion      │ "Bleed the tap dry"     │
├── 4b. Variant generation                         │ "Write 100 lines"       │
│   15+ human-written before AI helps              │                         │
│   ┌─ PUSHBACK PROMPTS ──────────────────────┐    │ SULLIVAN                │
│   │ "Most follow the same pattern"          │    │ Concepting lenses:      │
│   │ "None of these are falsifiable yet"     │    │ Invert, Exaggerate,     │
│   │ "What's the version that scares you?"   │    │ Metaphor, Before/After, │
│   │ "What if you couldn't use any of        │    │ Omit, Reframe,          │
│   │  those words?"                          │    │ Passage of time         │
│   └─────────────────────────────────────────┘    │                         │
├── 4c. Zoom In check                              │ LISA CRON               │
│   "Can you drop this on your foot?"              │ "If I can't see it,     │
├── 4d. Claude extends (after 15+ human variants)  │  it's not there yet"    │
│                                                  └─────────────────────────┘
│   GATE: 20+ total variants. 15+ human. 3+ angles. All pass Zoom In.
│
PHASE 5: SELECTION                                 ┌─────────────────────────┐
├── 5a. Three laws test                            │ HARRY DRY               │
│   Visualize? Falsify? Nobody else?               │ Three laws table        │
│   ┌────────┬───────┬───────┬───────────┐         │                         │
│   │Variant │ Viz?  │False? │Nobody     │         │ WIEBE                   │
│   │        │       │       │ else?     │         │ Money Words:            │
│   ├────────┼───────┼───────┼───────────┤         │ You Rule, "get",        │
│   │  #1    │  Y/N  │  Y/N  │   Y/N     │         │ "and" check, "pay"      │
│   │  #2    │  Y/N  │  Y/N  │   Y/N     │         │ check, interference     │
│   └────────┴───────┴───────┴───────────┘         │                         │
├── 5b. Money Words check                          │ KEVIN KELLY             │
├── 5c. Human selects finalists                    │ "Start from the         │
│                                                  │  headline"              │
│   GATE: All variants scored. Human selects.      └─────────────────────────┘
│
PHASE 6: FULL COPY                                 ┌─────────────────────────┐
├── Adapts by copy_type:                           │ SUGARMAN                │
│   ├── Taglines → skip to Review                  │ Two-line structure:     │
│   ├── Ads → headline + body + visual + CTA       │ curiosity → payoff      │
│   ├── Landing pages → hero + value + proof + CTA │                         │
│   ├── Emails → subject + preview + body + CTA    │ SULLIVAN                │
│   └── Social → platform-native                   │ "Never show what you're │
│                                                  │  saying"                │
│   Writing rules:                                 │                         │
│   ├── Human writes first, Claude develops        │ OGILVY                  │
│   ├── Write in the medium                        │ "Write to each of them  │
│   ├── Facts guarantee substance                  │  a letter"              │
│   └── The You Rule throughout                    │                         │
│                                                  │ PETE BARRY              │
│   GATE: Complete deliverable in context.         │ "Print = figure drawing │
│                                                  │  of advertising"        │
│                                                  └─────────────────────────┘
│
PHASE 7: REVIEW                                    ┌─────────────────────────┐
├── 7a. Kaplan's Law audit                         │ KAPLAN'S LAW            │
│   Word by word — every word earns its place      │ "Any word not working   │
├── 7b. Burrito test                               │  for you is working     │
│   Pull one sentence. Does the paragraph hold?    │  against you"           │
├── 7c. Interference check                         │                         │
│   Category clichés from Phase 3                  │ HARRY DRY               │
├── 7d. Three laws recheck                         │ "A great sentence is    │
├── 7e. SOCO alignment                             │  a good sentence made   │
│   One thing. Only one thing.                     │  shorter"               │
├── 7f. Simulate reality                           │                         │
│   Feed, inbox, billboard at 60mph                │ ELMORE LEONARD          │
├── 7g. Cut target                                 │ via WIEBE               │
│   10-33% reduction                               │ "Skip the part the      │
├── 7h. Optional: reviewer subagent                │  reader skips"          │
│                                                  └─────────────────────────┘
│   GATE: All checks pass. 10-33% cut. Final copy approved.

═══════════════════════════════════════════════════════════════════
MODES: Strict (default) — AI asks, waits, never originates
       Helpful — AI participates as thinking partner
       Phase 3 + 7 are mode-independent (research + review)

CORE PHILOSOPHY: "Human fills the blank page."
═══════════════════════════════════════════════════════════════════
```
