# Feedback for Sara: EP13 — The Claude Code Workflow

Tim's consolidated feedback on the article, organized by priority. This supplements the inline comments Tim already left in the Google Doc.

## Must-fix (3 items)

### 1. LinkedIn URL
The Tim Metz hyperlink in the second paragraph of the opener links to `/in/timmetz/` — correct URL is `/in/metztim`.

### 2. Step 6 appears twice
Two headings both say "Step 6: Apply the corrections." The first covers the violations report output, the second covers the three apply options (manual, `--auto-apply`, `--dry-run`). Either merge into one Step 6, or rename: "Step 6: Review the violations report" and "Step 7: Apply the corrections."

### 3. Summaries vs full text contradiction
Step 3 says Claude Code "fetches and stores the full text of each article locally, not a compressed summary." But the "What doesn't shine" section says Tim noticed it used article summaries rather than full text.

Both are true — the nuance is: Claude Code *should* use full text, but the error was in the prompt Tim initially gave the agents. He didn't specify full articles, so Claude set the tool mode to "summary." Once corrected in the instructions, it does pull full articles. Suggested fix: in Step 3, rather than saying "not a compressed summary," foreshadow that it's important to tell Claude to pull the full articles. The warning in "What doesn't shine" then shows what happens if you don't.

## Sara's open questions

### Alternative use cases (Sara's comment on "Competitor hubs · Category pages · Sales enablement assets")
The current alternatives don't fit a style guide workflow. What we're really doing is *reverse engineering a set of standards from existing samples* — then enforcing those standards on new content. More accurate alternatives:

- **Messaging/positioning guide** — feed existing landing pages and sales decks, extract the implicit positioning rules, enforce consistency across new materials
- **Tone of voice guide** — feed customer-facing emails or support docs, extract communication patterns
- **Client brand audit** — extract a client's style from their published content, check new drafts against it (relevant for agencies)
- **Content strategy consistency check** — feed existing top-performing content, extract what makes it work, check new briefs against those patterns
- **Freelancer onboarding** — give freelancers an enforceable style guide extracted from your actual published work, not a static doc

### "No need to write these from scratch" (Sara's comment asking for more detail)

**Tim's comment for the doc:**

> The templates in the zip are ready to use — download, swap in your brand name and any rules specific to your style, and run. The command files tell Claude Code what to do when you type a slash command, and the agent files define what each of the eight parallel agents checks for. Readers don't need to write any of this from scratch.

### Zip download link (Sara's comment on what to include)

**Tim's comment for the doc:**

> The full zip is the right call. Readers need both the command files and the agent files together — linking to individual folders would just be confusing. One download, everything they need.

## Links assessment

Sara asked specifically about which external links make sense and which are overkill.

**All current links should stay** — the link density is reasonable for a tutorial-style article:
- Claude Code product page — essential
- Animalz website — essential context
- Animalz blog Claude Code guide — directly relevant, Tim wrote it
- Google Drive zip (prompts download) — essential for the tutorial
- Google Drive style guide example — useful reference
- Carl Vellotti "Claude Code for Everyone" — good supplementary resource for readers wanting more
- Hannah Stulberg "Claude Code for Everything" — good supplementary, different angle
- Sara's and Diandra's LinkedIn profiles — standard

**Fix:** Tim's LinkedIn URL (see must-fix #1)

**Add:**
- **We Eat Robots newsletter** (`weeatrobots.substack.com`) — Tim's newsletter is mentioned in the intro ("Author of We Eat Robots") but never linked. Add a link where he's first described.
- **LinkedIn style guide post** — The original post about this workflow (`https://www.linkedin.com/posts/metztim_ever-since-chatgpt-came-out...`) would add context in the opener or Goldflow section. Shows the real thing.

**Consider:**
- Tim's "What only you can tell AI" article on We Eat Robots — thematically relevant to the "you can't automate the thinking" closing, but possibly too much of a detour. Tim's call.

**Nothing to cut.** All existing links earn their place.

## Content additions Tim suggests

### Max plan upgrade anecdote (on "You'll Max it out fast")
Tim upgraded from Pro to Max x20 within 24 hours of starting Claude Code. "I guess it was just love at first sight!" — a personal touch that makes the token usage warning more relatable.

### Claude as guardrail against bad habits (on the Workflow Warning section)
Tim has started experimenting with using Claude to guard against his own worst impulses:
- A writing assistant command that guides through the Animalz editorial process (thesis first, 30% outline before drafting) but explicitly tells Claude not to do any writing — forces Tim to write
- Feature freeze mode in his CLAUDE.md file for an app he's building, so Claude pushes back hard on new feature ideas

This connects directly to the behavioral warning: if the risk is "falling asleep at the wheel," one solution is telling Claude to wake you up.

## Editing quality note

In the "What triggered The Workflow" section, the verbs are in past tense ("Client work always took front row," "Tim was running internal marketing largely solo"). Present/active tense would be stronger and more engaging: "Client work always takes front row, and Tim runs internal marketing largely solo." Both are grammatically correct, but present tense reads as ongoing reality rather than a narrated backstory.

## What works well

Worth calling out specifically — the article does a lot right:
- The anti-hype opener is exactly the right positioning
- The parallel agent explanation is genuinely the clearest anyone has written on why this architecture matters
- The behavioral warning is the kind of honesty most AI articles skip
- The closing ("you can automate the style check, you can't automate the thinking") is perfect
- Sara's voice throughout has real personality — it sounds like their publication while representing Tim's views accurately
