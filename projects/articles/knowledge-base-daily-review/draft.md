---
source_of_truth: /Users/timmetz/Developer/Projects/Personal/writing-assistant/projects/articles/knowledge-base-daily-review/draft.md
workflow_repo: "[TBD — repo URL once public]"
workflow_path: workflows/daily-review/
last_workflow_update: 2026-03-23
article_version: 1
---

# My AI Daily Review: 15 Minutes That Run My Entire Day

I wake up, open Claude Code, and type `/daily-review`.

Over the next 10-15 minutes, an AI agent tracks my sleep, serves me an inspirational quote, shows my calendar with meeting prep already done, triages my Apple Reminders, surfaces blocked tasks, proposes which of my to-dos it can handle autonomously, processes my digital inboxes — and asks me two questions along the way.

When it's done, I close the laptop and start my actual work. Everything's been sorted.

I've been running some version of this daily review for about a year now. People keep asking me how it works. So I figured I'd just show you — and explain why I built it this way.

---

## What it does

The daily review is a single Claude Code command that orchestrates 15+ individual steps across Notion (two workspaces), Apple Calendar, Apple Reminders, Logseq, Slack, and my local file system. It runs every weekday morning. On weekends, it automatically switches to a slim version — just health tracking, reminders, and whatever optional elements I feel like doing.

**The input:** Two numbers (hours slept, coffees yesterday) and a few yes/no decisions.

**The output:** A fully triaged morning. Sleep tracked with 14-day charts, meetings prepped, reminders converted to tasks, blocked items surfaced, AI-executable tasks launched in the background, and inboxes cleared.

[FLOWCHART — see flowchart spec below]

---

## How it works

The review runs in five phases. While I'm answering the first question, background agents are already fetching data from Notion, Slack, and my file system — so later phases have everything ready.

### Phase 1: Health + background launch

The review asks me one question: how many hours did I sleep, and how many coffees did I have yesterday.

While I answer, four background agents spin up:
- One preloads reflection data (inspirational quotes from my Logseq highlights, historical journal entries)
- One runs a fresh Slack triage scan
- One pre-classifies items from my file inboxes
- One gathers context for today's meetings by searching Notion and Logseq

Then it logs my sleep to Notion, syncs a local cache, and generates a 14-day bar chart — in the terminal. Same for coffee. The health snapshot looks like this:

```
Sleep History (last 14 days)

10h |
 9h |
 8h |       #
 7h | # - - # - # # # # - - - # -  <- target
 6h | #     # # # # # # # #   # #
    +----------------------------
     W T F S S M T W T F S S M T

3-night avg: 7.2h | 7-night avg: 6.8h
-> Steady trend; maintain current sleep routine.
```

I like having the visual. Takes about two seconds to spot a pattern.

> **Want more detail on health tracking?** Paste this into your AI tool:
>
> "I'm reading about the daily review workflow from [REPO_URL]. Explain how the health tracking step works — how does it calculate rolling averages, detect missed nights, and generate the sleep chart? Reference the source file at workflows/daily-review/steps/health.md."

### Phase 2: Reflection

Three parts here. First, a random inspirational quote from my Logseq highlights — curated from years of reading, so it's always something that resonates. Second, an "On This Day" section showing what I was doing 1-4 years ago (pulled from Logseq journal entries). Third, I pick from five reflection prompts and write a brief response.

**The whole thing saves to a local markdown file. No Notion, no sync overhead.** This is just for me.

The reflection step is the one that most surprised me. I added it because I thought "well, I have all these highlights, might as well surface them." But it's become the part I look forward to most. Seeing a quote from a book I read three years ago, next to what I wrote in my journal that same week — it connects things in ways I wouldn't have found on my own.

### Phase 3: Calendar + inbox

Three things happen here, all fetched live or from the pre-gathered data:

**Meetings.** If I had any unprocessed meetings (logged via Notion), it extracts action items assigned to me, presents them numbered, and I say which ones become tasks. One command: "1-3, 5" — done.

**Calendar look-ahead.** Shows today's events with inline context. The background agent already searched Notion and Logseq for related notes, previous meetings with the same people, active tasks on the same topic. So instead of just seeing "Client review: Acme Corp at 10am," I see the last meeting's key points and two active tasks related to them.

**Reminders triage.** Surfaces non-recurring Apple Reminders — overdue first, then today, then upcoming (3-day window). For each: convert to Notion task, mark done, or skip. Batch input: "1c, 2c, 4d, 5s".

> **Want more detail on meeting processing or calendar prep?** Paste this into your AI tool:
>
> "I'm reading about the daily review from [REPO_URL]. Walk me through how the meeting processing and calendar look-ahead steps work — how does it extract action items, and what does the background meeting prep agent search for? Reference workflows/daily-review/steps/meetings.md and calendar-lookahead.md."

### Phase 4: Work management

This is where the review earns its keep.

**Blocked items.** Queries both Notion workspaces for tasks in "Blocked / Waiting" status. But it doesn't dump everything — it applies surfacing rules. A task only shows up if it's overdue, flagged for today, or stale (untouched for 7+ days with no future reminder). Tasks with a future check-in date stay quiet until that date. I resolve, acknowledge, or create follow-ups.

**Task agent.** This is the step people ask about most. It scans my active tasks, classifies each one by AI-executability (can an agent do this autonomously?), checks feasibility (does the task have enough context?), and proposes candidates with a one-line pitch:

```
PROPOSED:
  1. [W]  Review intake form comparison  High    Auto-execute
     -> Compare current vs. latest intake form, flag discrepancies.
  2. [P]  Learn Harry Dry copywriting    Medium  Auto-execute
     -> Research video content, create reference sheet with key techniques.
```

I approve the ones I want ("y" for all, or "1, 2" for specific ones), and background agents start executing — while I continue the review. By the time I'm done, the results are appended to the Notion task pages and the tasks are renamed with a `[Review]` prefix so I know to check them.

**The system is conservative by design.** Tasks classified as "not executable" (calls, purchases, meetings) never get proposed. Tasks it already tried get permanently excluded. Low-confidence tasks (vague title, no description) get skipped with the reason shown. I can also snooze or permanently exclude individual tasks.

**Admin + goals nudges.** Date-aware reminders for recurring personal admin (finances, reimbursements) and a weekly goals check-in. Both skip silently when nothing's relevant — zero noise.

> **Want more detail on the task agent?** Paste this into your AI tool:
>
> "I'm reading about the daily review from [REPO_URL]. Explain the task agent step in detail — how does it classify tasks into tiers, assess feasibility, generate pitches, and execute approved tasks in the background? What safeguards prevent it from doing things it shouldn't? Reference workflows/daily-review/steps/task-agent.md."

### Phase 5: Inbox + optional elements

**Consolidated inbox.** A background agent already scanned four locations — two Notion scratchpads (personal + work), Desktop, Downloads, and a Dropbox transfer folder. It classified each item (task, delete, file, needs review) and I see the pre-sorted list. Usually I just type "ok" to accept all suggestions, then override a couple.

**Optional elements.** I get a checklist: Logseq highlight review? Content inbox triage? I pick what I have time for. Most days I skip both. Mondays I usually do the Logseq review.

Then the review shows a quick task agent status — "3 tasks completed, now [Review] tasks in Notion" — and ends.

---

## What you need to run it

The daily review depends on a specific stack:

- **Claude Code** with the Claude Opus model (the orchestrator and all agents run here)
- **Notion** (two workspaces — personal and work — with specific database schemas for tasks, journal, meetings)
- **Apple Calendar + Reminders** (accessed via a custom `ical` CLI tool built in Swift)
- **Logseq** (knowledge base for reflection quotes, journal entries, highlight reviews)
- **Slack** (for the triage agent that scans unreads)
- **Custom CLI tools:** `notion` (Notion API wrapper), `logseq` (Logseq search), `ical` (calendar/reminders), `gmail` (read-only email access)

**This isn't a plug-and-play install.** The workflow is deeply integrated with my specific Notion schemas, database IDs, and tool setup. But the architecture is entirely portable — the pattern of "orchestrator + step files + background agents" works with any set of tools.

The full workflow lives here: [REPO_URL]

You can read every step file, see exactly what each phase does, and adapt it for your own setup. Or just browse to understand the approach.

---

## How it evolved

- **Started as a sleep tracker.** The first version just logged sleep to Notion and showed a chart. That's it. Everything else was manual. (Early 2025)
- **Added reflection, then immediately loved it.** Surfacing random Logseq highlights during the morning routine was meant to be a nice-to-have. It became the step I look forward to most. The "On This Day" journal lookback came later and hit even harder. (Mid 2025)
- **Meeting processing replaced a manual Notion habit.** I was already logging meetings to Notion and extracting action items by hand. Automating the extraction — and making the "which ones become tasks?" decision a one-liner — saved 10+ minutes on busy meeting days. (Late 2025)
- **The task agent was the biggest leap.** Going from "show me my tasks" to "propose which ones AI can handle, then actually do them in the background" fundamentally changed how I think about task management. The conservative classification + feasibility checks took several iterations to get right. (Early 2026)
- **Background agents solved the speed problem.** The review used to take 25+ minutes because every data fetch was sequential. Launching four background agents during the first question — and having data ready by the time each phase needs it — cut the whole thing to under 15 minutes. (Early 2026)
- **Weekend mode came from burnout.** Running the full review on Saturdays felt like work. The slim weekend version — health, reminders, optional elements only — preserves the habit without the weight. (Feb 2026)
- **Consolidated inbox replaced three separate steps.** Desktop, Downloads, scratchpads, and Dropbox transfer used to be separate optional elements. Merging them into one pre-classified inbox with batch approval made the whole thing faster and less annoying. (Mar 2026)

---

## What I'd change next

**Smarter task agent memory.** Right now it tracks what it's tried before, but it doesn't learn from execution quality. If a research task consistently produces shallow results for a certain type of task, it should stop proposing those.

**Cross-day context.** The review doesn't know what happened yesterday beyond what's in Notion. If yesterday's task agent found something interesting, or if a Slack triage item from yesterday connects to today's calendar — that kind of cross-day threading is missing.

**Email integration.** Gmail access is read-only and not yet wired into the daily review. Surfacing emails that need replies, or connecting email threads to calendar events, would close a gap.

---

Have you built your own morning review system — AI-assisted or otherwise? What made you keep doing it?

---

## Flowchart spec

*To be generated with Whimsical MCP in a follow-up session.*

The flowchart should show:

**Top-level flow (left to right or top to bottom):**

1. **Start** (pill) -> "Weekend?" (diamond)
2. Weekend branch -> slim review (3 steps: Health, Reminders, Optional elements) -> End
3. Weekday branch -> 5 phases:

**Phase 1 node group:**
- "Ask sleep + coffee" (pill — human input)
- Fork to 4 background agents (rectangles): Reflection preload, Slack triage, Inbox preload, Meeting prep
- "Process health data" (rectangle) -> "Health snapshot" (ellipse — output)

**Phase 2 node group:**
- "Show daily reading + On This Day" (rectangle)
- "Reflection prompt" (pill — human input)
- Reads from: Logseq journals (cylinder), Reflection index (cylinder)

**Phase 3 node group:**
- "Process meetings" (rectangle) -> "Action item triage" (pill)
- "Calendar look-ahead" (rectangle) — reads from Meeting prep (cylinder)
- "Reminders triage" (pill) — reads from Apple Reminders (cylinder)

**Phase 4 node group:**
- "Blocked items" (rectangle) -> "Resolve/follow-up" (pill)
- "Task agent classify" (rectangle) -> "Approve tasks" (pill) -> "Background execution" (rectangle)
- "Admin nudge" (rectangle, conditional)
- "Goals nudge" (rectangle, conditional/weekly)
- Reads from / writes to: Notion personal + work (cylinders)

**Phase 5 node group:**
- "Consolidated inbox" (rectangle) -> "Batch approve" (pill)
- "Optional elements?" (diamond) -> Logseq .5 review, Content inbox
- "Task agent status" (ellipse — output)
- "Daily review complete" (ellipse — end)

**Target:** 12-15 nodes, not counting data stores. Data stores shown as connected cylinders on the side, not inline.
