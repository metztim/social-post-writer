---
source_of_truth: /Users/timmetz/Developer/Projects/Personal/writing-assistant/projects/articles/claude-code-hub/research/campaign-research-report.md
note: Research report for Claude Code content campaign. Pre-drafting phase.
---

# Claude Code Content Campaign: Research & Structure Proposal

**Date:** 2026-03-23
**Prepared for:** Tim Metz, Nathan Wahl
**Status:** Research complete, awaiting discussion

---

## Part 1: Internal content audit

### 1.1 Published article (Oct 2025)

**File:** `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/projects/internal/author-fingerprint-research/corpus/tim/20251002 claude-code-for-content-marketers-a-no-code-guide-animalz.md`
**URL:** https://www.animalz.co/blog/claude-code
**Word count:** 2,645

**What it covers:**
- Why use Claude Code (unconstrained I/O, folder structure as context, agents, get-it-done mindset)
- Installation (one command)
- Five use cases: queryable database, transcript analysis, content audit, interactive presentations, style guide reverse-engineering
- Essential slash commands and custom commands
- Plugin marketplace (animalzinc/claude-plugins) with 4 plugins

**What's outdated or missing:**
- Written for Opus 3.5/Sonnet 3.5 era. No mention of Opus 4.5/4.6 capabilities (agent teams, 1M context, voice mode, adaptive thinking, context compaction)
- Plugins section references a now-outdated plugin architecture. Skills, hooks, and the merged commands/skills system (v2.1.3+) didn't exist yet
- No mention of MCP integrations, which are now central to power use
- No mention of CLAUDE.md as the key customization mechanism
- Use cases are good but basic. Missing: AEO workflows, Notion integration, writing processes, research agents, CLI tool building
- No mention of /write, /copywrite, /newsletter, or any structured process commands
- Installation has been simplified further; pricing/plans have changed
- No AEO angle at all

### 1.2 Claude Code vs. AirOps vs. agents (draft, Jan 2026)

**Folder:** `/Users/timmetz/Developer/Projects/Animalz/content/claude-code-airops-agents/`
**Draft:** `drafts/20260109 1025 claude-code-vs-airops-vs-agents.md`
**Research transcript:** `20260111-ai-agent-research.txt`

**Key content:**
- Clear spectrum framework: structured (AirOps/workflows) → middle (Claude Code) → unstructured (agents)
- Comparison table: Claude Code vs. Workflow vs. Agent across 12 dimensions
- Claude Code's flexibility-as-liability argument (skipping steps)
- Agents: "automate the navigation of a solution space that must already exist"
- Deep dive into what agents actually are (loop + LLM + tools + termination)

**Campaign relevance:** This is strong conceptual material for a spoke article on "Claude Code vs. workflows vs. agents" or a section in the hub explaining where Claude Code fits in the AI tool landscape. The comparison table is ready for reuse.

### 1.3 Claude plugins repo

**Path:** `/Users/timmetz/Developer/Projects/Animalz/claude-plugins/`
**Repo:** github.com/animalzinc/claude-plugins

**Five published plugins:**
1. Blog Style Guide Creator — multi-agent style guide generation
2. Interactive Presentation Generator — data to HTML presentations
3. Interactive Transcript Analyzer — parallel agent research synthesis
4. Content Library Auditor — CMS export analysis
5. Copywriting Coach — 7-phase /copywrite process

**Campaign relevance:** These are the featured shareable resources for the hub. Each plugin could have a mini-profile in the commands/plugins collection section. The style guide creator and copywriting coach are the most compelling for marketers.

### 1.4 Writing assistant commands

**Path:** `/Users/timmetz/Developer/Projects/Personal/writing-assistant/.claude/commands/`

**Available commands:**
| Command | Description |
|---|---|
| `/write` | 8-phase structured article writing (508 lines, deeply built out) |
| `/copywrite` | 7-phase copywriting process (also published as plugin) |
| `/newsletter` | 4-phase weekly newsletter workflow |
| `/draft-linkedin-post` | LinkedIn post creation |
| `/write-rescue` | Mid-process entry for existing drafts |
| `/write-status` | Quick progress check |
| `/research-article` | Standalone research agent |

**Campaign relevance:** `/write` is the crown jewel for the hub — a sophisticated, opinionated writing process trained on Animalz editorial philosophy. The Tim/Nathan meeting specifically called out sharing the /write command as a featured resource. The command demonstrates what's possible when you embed domain expertise into Claude Code.

### 1.5 Animalz Intelligence OS — Knowledge base

**Path:** `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/knowledge-base/src/content/`

**Key content relevant to campaign:**
- `playbook/build-commands-from-knowledge.md` — How to build AI commands from personal knowledge (detailed case study of building /copywrite from book highlights and Logseq notes)
- `playbook/ai-workflow-onion.md` — Three-layer framework for AI workflow maturity (workflow → experience → organization)
- `playbook/calibrate-brand-voice.md` — Brand voice calibration process
- `playbook/keep-commands-lean.md` — Command design principles
- `commands/write.md` — /write command documentation
- `research/evaluating-ai-content-quality.md` — AI content quality evaluation
- Various changelogs documenting capabilities built over time

**Campaign relevance:** The knowledge base is a goldmine of practical playbook material. "Build commands from knowledge" is a strong standalone spoke article or hub section. The "AI Workflow Onion" framework provides a maturity model readers can self-assess against.

### 1.6 Hub Guide page (Notion, work workspace)

**Notion ID:** `313df6dc-2cc5-804a-b2a0-ca77fa4e893b`
**Status:** Drafting
**Related tasks:** 3

**Page content includes:**
- Section idea: "Commands vs Skills vs Plugins vs Hooks" — decision framework from building 26 slash commands
- Key insight: Commands/Skills merged in v2.1.3; difference is configuration intent, not separate systems
- Reference files for extensibility guide and migration analysis

### 1.7 Consolidated Notion tasks (work workspace)

All these have been consolidated into the Claude Code content strategy task (`321df6dc`):
- `2a0df6dc` — Create Claude Code tips compendium from Logseq (Done)
- `2a0df6dc` — Create Claude Code commands/plugins/agents cheat sheet (Done)
- `2a0df6dc` — Create guide: When and how to use Claude Code agents (Done)
- `315df6dc` — Research Claude Code vs Coworker (Done)
- `317df6dc` — Turn Ahrefs E-E-A-T audit checklist into Claude Code skill (Done)
- `319df6dc` — Do Claude Code open office hours (Done)
- `318df6dc` — Review and update Claude Code Basics wiki page (Done)

**Active tasks:**
- `312df6dc` — Plan demo Claude Code capabilities (Dropped — replaced by content approach)
- `328df6dc` — Your Claude Partner Network application — Next Steps (Not started, High priority)
- `30ddf6dc` — Review Josh's AEO process with Claude Code (Not started, High priority)
- `329df6dc` — Sync with Tom on Claude Code usage patterns (Not started, High priority)
- `329df6dc` — Use monthly call for Claude Code training/demos (Not started)
- `31adf6dc` — Release video: Notion-Claude Code integration (Not started, Critical)
- `30ddf6dc` — Inform team: query Notion KB from Claude Code (In progress)

### 1.8 MyContent (personal Notion)

**Claude Code LinkedIn series (Claude 101):**
13 sub-items under the "Claude Code 101 series" parent (`27eedc77`), all published Sept-Oct 2025:
- #1: Setup (26 reactions, 962 impressions, 3.1% engagement)
- #2: Presentations
- #3: Transcript analysis
- #4: Commands
- #5: WordPress analysis
- Style guide post (77 reactions, 7,063 impressions, 1.6% engagement — **best performer**)

**Other Claude-related content:**
- "Why use Claude Code?" LinkedIn post (Sept 2025)
- "Coding with Claude" series
- "Vibe coding with Cursor, Claude 4 Opus, and Codex" (published)
- Several idea-stage posts (Claude Code on existing projects, planning, Scrunch API, Slack bot)

### 1.9 Logseq notes

**High-relevance pages:**
- "Building More Efficient AI Agents" (Anthropic) — tagged `claude code ideas`, covers MCP code execution, context-efficient tool results
- "Effective Context Engineering for AI Agents" (Anthropic) — context engineering fundamentals, used in original article
- "How to Use Claude Code Like the People Who Built It" (Every) — tips from builders
- "Hooks" (Anthropic docs) — Claude Code hooks documentation
- "Claude Code Q&A" (Katie Parrott/Every) — practical tips: plan mode, TDD, sub-agents, MCP, CLAUDE.md, containers, Pomodoro with AI
- "Give Yourself a Promotion" (Every) — beautiful non-technical user perspective on Claude Code experience
- "Writing Effective Tools for Agents" (Anthropic) — tool design for agents
- "Subagents" (Anthropic docs) — subagent documentation
- "Vibe Check: Claude Skills Need a 'Share' Button" (Every) — skills sharing ecosystem
- "The Workflows Turning One Engineer Into Ten" (Every/Katie Parrott) — Claude Code Camp subagents demos

### 1.10 Content strategy alignment

**File:** `/Users/timmetz/Developer/Projects/Personal/writing-assistant/CONTENT_STRATEGY.md`

Claude Code content maps to **all three pillars:**
1. **AI + content operations:** How Animalz uses Claude Code in production
2. **Building with AI:** What Tim's building (writing workflows, agent systems)
3. **Working differently with AI:** How Claude Code changes knowledge work patterns

**Publication routing:** Hub guide → Animalz Blog (serves SEO + thought leadership). Spokes can split between Animalz Blog (SEO-focused) and WER/LinkedIn (personal insights, building-in-public angle).

---

## Part 2: External landscape research

### 2.1 Existing Claude Code guides for marketers

The landscape has gotten crowded since the Oct 2025 article. Key competitors:

| Source | Angle | Depth |
|---|---|---|
| [claudecodeformarketers.com](https://claudecodeformarketers.com/) | Dedicated site: CLAUDE.md for brand voice | Medium |
| [cc4.marketing](https://cc4.marketing/) | Interactive course taught inside Claude Code | Deep |
| [Firecrawl blog](https://www.firecrawl.dev/blog/claude-code-for-marketing) | General "Claude Code for Marketing" overview | Light |
| [Growth Method](https://growthmethod.com/claude-code-guide-marketers/) | Guide to Claude Code for marketers | Medium |
| [MKT1 Newsletter](https://newsletter.mkt1.co/p/real-marketers-claude-code-builds) | "What 4 Marketers Are Building" — real examples | Medium |
| [Stack and Scale](https://www.stackandscale.ai/p/the-marketers-blueprint-for-claude) | 5-min install + 5 workflows | Light |
| [Product Talk](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/) | "What It Is and Why Non-Technical People Should Use It" | Medium |
| [Every](https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required) | Everyday tasks, no programming required | Medium |
| [Every](https://every.to/source-code/claude-code-the-most-common-questions-beginners-ask) | Common beginner questions FAQ | Medium |
| [claude101.every.to](https://claude101.every.to/) | "Claude Code for Beginners" course | Deep |
| [MindStudio blog](https://www.mindstudio.ai/blog/claude-code-content-marketing-skill-system) | Skill-based content machine | Medium |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Open-source marketing skills for Claude Code | Deep (code) |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | Massive beginner-to-power-user guide | Very deep |

**Key observation:** Most guides are generic "what is Claude Code + basic use cases." None combine (a) marketer-specific depth with (b) ready-to-install plugins/commands with (c) production-tested workflows from an agency that actually uses them daily. That's the positioning gap.

### 2.2 Opus 4.6 capabilities (released Feb 5, 2026)

Per [Anthropic's announcement](https://www.anthropic.com/news/claude-opus-4-6) and [technical docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6):

| Feature | Marketing impact |
|---|---|
| **1M token context window** | Analyze entire content libraries in a single session |
| **128k output tokens** | Generate comprehensive reports, audits, full drafts |
| **Agent teams** | Split complex tasks across coordinated agents (e.g., research + outline + draft) |
| **Adaptive thinking** | Better reasoning on complex strategy questions |
| **Context compaction** | Longer sessions without losing thread |
| **Self-correction** | 76% on MRCR v2 — catches its own mistakes during review |

### 2.3 Recent Claude Code updates (March 2026)

Per [Claude Code changelog](https://code.claude.com/docs/en/changelog):

| Feature | Marketing relevance |
|---|---|
| **Voice mode (push-to-talk)** | Dictate prompts instead of typing — huge for non-technical users |
| **/loop command** | Recurring monitoring (e.g., track competitor content changes) |
| **/effort command** | Simplified effort control (low/medium/high) |
| **MCP elicitation** | Interactive forms from MCP servers during execution |
| **Channels (research preview)** | Message Claude Code via Telegram/Discord |
| **Plugin improvements** | Better install flows, richer controls |

### 2.4 Competitive positioning

**Claude Code vs. alternatives for non-developers:**
- **Cursor/Windsurf:** IDE-focused, explicitly positioned for developers. Multiple comparison articles confirm these are not for non-technical users
- **Lovable/Bolt:** No-code app builders. Different category entirely
- **ChatGPT/Claude chat:** Limited by context windows, response limits, no local file access
- **GitHub Copilot Workspace:** Developer-centric

**Animalz's differentiation:**
Claude Code is the only tool in this space that bridges the gap between "AI chat" and "developer tool" for knowledge workers. Animalz is uniquely positioned because:
1. They actually use it in production (not theoretical)
2. They have distributable plugins and commands (not just advice)
3. They've built sophisticated writing/editing processes on it (not just basic use cases)
4. Tim has the Claude Code 101 LinkedIn series with proven engagement
5. Claude Partner Network application in progress — potential official relationship

### 2.5 AEO opportunity

Several articles already cover Claude Code for AEO:
- [Discovered Labs](https://discoveredlabs.com/blog/how-to-leverage-claude-code-for-aeo-geo-optimization) — Claude Code for AEO/GEO optimization
- [Search Engine Land](https://searchengineland.com/claude-code-seo-work-470668) — Claude Code as SEO command center

**Key queries to target (based on search landscape):**
- "Claude Code for marketers" — multiple competing pages, but Animalz already ranks
- "Claude Code for content marketing" — growing search intent
- "Claude Code commands for marketing" — underserved
- "Claude Code plugins content" — underserved
- "how to use Claude Code without coding" — high intent, growing
- "Claude Code vs ChatGPT for content" — comparison intent
- "Claude Code CLAUDE.md guide" — specific feature queries
- "Claude Code for SEO / AEO" — emerging intent
- "Claude Code skills for writing" — very underserved
- "Claude Code for non-developers" — broad, high volume

**Recommendation:** Use Ahrefs MCP (per Tim/Nathan meeting notes) to validate these queries and find additional opportunities before finalizing the hub structure.

### 2.6 Community questions (synthesized from search results)

**Most common non-developer questions:**
1. "Do I need coding experience?" (setup anxiety)
2. "What's the difference between Claude Code and regular Claude?" (positioning)
3. "What can I actually do with it?" (use cases)
4. "How do I set up CLAUDE.md?" (customization)
5. "What are commands/skills/plugins/hooks?" (extensibility confusion)
6. "Is the Pro plan enough or do I need Max?" (pricing)
7. "How do I use it with my existing tools?" (integrations/MCP)
8. "What's an agent/subagent?" (conceptual)
9. "How do I share what I build with my team?" (collaboration)
10. "Can it actually write content for me?" (expectations management)

---

## Part 3: Structure proposal

### 3.1 Hub page outline

**URL:** animalz.co/claude-code (overwrite existing article)
**Format:** Living guide (continuously updated, not static blog post)
**Estimated length:** 4,000-5,000 words

| H2 Section | What it covers | Notes |
|---|---|---|
| **Why Claude Code for content marketers** | Updated value proposition: unconstrained I/O, folder-as-context, agents, get-it-done mode. What changed with Opus 4.6 (1M context, agent teams, voice mode). Where Claude Code fits vs. chat AI, workflows, developer tools. | Replaces current "Why Trouble Yourself" section. Add the spectrum framework from the AirOps draft. |
| **Getting started** | Updated installation, first prompt, project folder setup. Pricing guidance (Pro vs. Max). Voice mode as accessibility feature. | Keep current structure but update for 2026 reality. Add voice mode — this is huge for non-technical adoption. |
| **Your first CLAUDE.md** | How to create a CLAUDE.md that teaches Claude your brand voice, project context, and preferences. This is the #1 customization mechanism and wasn't in the original article. | New section. Critical gap in original. Link to brand voice spoke. |
| **Use cases for content teams** | Updated use cases with brief descriptions + links to spoke articles for depth. Categories: Analysis & Research, Content Production, SEO & AEO, Team Operations. | Updated from original 5 use cases. Each gets 2-3 paragraphs max on hub, with "deep dive" links to spokes. |
| **Commands, skills & plugins** | Decision framework (commands vs. skills vs. plugins vs. hooks). Featured Animalz plugins with install instructions. Curated 3rd-party resources. | Per Tim/Nathan meeting: this is a major section. Include the framework from the Hub Guide Notion page. |
| **Building your own workflows** | How to go from basic prompts to structured commands. The "AI Workflow Onion" maturity model. | Links to "build commands from knowledge" spoke. Includes the Onion Framework. |
| **FAQ** | Answers to the 10 most common questions (from 2.6 above). | Quick-hit format. AEO-optimized with question-and-answer structure. |
| **Office hours & community** | Regular office hours offering. How to get help. Links to resources. | Per Tim/Nathan meeting. Turns the guide into a relationship, not just content. |

### 3.2 Spoke articles

| # | Title | Covers | Existing material | Effort | Priority |
|---|---|---|---|---|---|
| **S1** | How We Built a Structured Writing Process in Claude Code | Deep dive into /write command: 8-phase process, quality gates, the philosophy of "human fills the blank page." How to embed editorial expertise into AI workflows. | `/write` command (508 lines), knowledge base "build commands from knowledge" playbook, /copywrite as second example | Medium (material exists, needs narrative) | **High** — This is the hero content. Demonstrates depth no competitor has. |
| **S2** | Claude Code Commands, Skills & Plugins: The Content Marketer's Cheat Sheet | Comprehensive reference: what each extensibility mechanism does, when to use which, featured plugins with install instructions, curated 3rd-party picks. | Hub Guide Notion page extensibility framework, claude-plugins repo, merged commands/skills analysis | Medium | **High** — Most directly actionable for readers. |
| **S3** | CLAUDE.md for Content Teams: Teach AI Your Brand Voice | How to write an effective CLAUDE.md: brand voice encoding, project context, editorial standards, team conventions. Real examples from Animalz. | Style guide creator plugin, brand voice calibration playbook, CLAUDE.md files across repos | Light-medium | **High** — Addresses the #1 beginner question after "how do I install it." |
| **S4** | Claude Code vs. Workflows vs. Agents: Where Each Shines | Updated version of the Jan 2026 draft. Spectrum framework, comparison table, practical decision guide for content teams. | AirOps draft + research transcript (nearly complete), Onion Framework | Light (draft exists, needs updating for Opus 4.6 era) | **Medium** — Good thought leadership, less directly actionable. |
| **S5** | Using Claude Code Agents for Content Research | When and how to use subagents and agent teams for research, competitive analysis, transcript analysis, and content audits. | Transcript analyzer plugin, research-article subagent, agent teams documentation | Medium | **Medium** — Builds on existing plugins, good for intermediate users. |
| **S6** | Claude Code for AEO: Answer Engine Optimization Workflows | How to use Claude Code (with Ahrefs MCP) for AEO audits, content optimization, query research. | AEO audit project, Josh's AEO process (pending review), AEO module in toolkit | Heavy (needs building + writing) | **Medium** — High strategic value for Animalz, but more work needed. |
| **S7** | What Changed with Opus 4.6 (and Why Marketers Should Care) | Practical impact of 1M context, agent teams, voice mode, context compaction on marketing workflows. Not a feature list — what you can do now that you couldn't before. | Logseq notes on Opus 4.6, "Something Big Is Happening" highlights | Medium | **Low** — Time-sensitive content that may be less relevant as more updates ship. Better as a WER/LinkedIn piece. |

### 3.3 Content map: existing materials → hub/spoke sections

```
EXISTING MATERIAL                          → HUB/SPOKE DESTINATION
─────────────────────────────────────────────────────────────────
Published article (Oct 2025)               → Hub: rewritten core, updated use cases
Claude Code vs AirOps draft (Jan 2026)     → S4: Claude Code vs. Workflows vs. Agents
Claude plugins repo (5 plugins)            → Hub: Commands section + S2: Cheat Sheet
/write command (508 lines)                 → S1: Structured Writing Process (hero)
/copywrite command                         → S1: second example + S2: featured plugin
/newsletter command                        → S2: featured command
Knowledge base playbooks                   → Hub: Building Workflows + S1 + S3
Hub Guide Notion page (extensibility)      → Hub: Commands section + S2
LinkedIn 101 series (13 posts)             → Hub: embedded examples, social proof
Logseq highlights (20+ pages)              → Research inputs across all spokes
AEO audit project                          → S6: AEO spoke
Style guide creator plugin                 → S3: Brand Voice spoke
Tom's usage patterns (pending sync)        → Hub: internal adoption proof points
Josh's AEO process (pending review)        → S6: AEO spoke
```

### 3.4 Gaps: what needs to be created from scratch

1. **CLAUDE.md tutorial content** (S3) — Need to create a marketer-friendly walkthrough with real examples. Existing CLAUDE.md files are for AI consumption, not human tutorial material.

2. **Updated comparison with 2026 competitor landscape** (S4) — The Jan 2026 draft predates Opus 4.6. Needs updating for agent teams, 1M context, and the fact that many prior limitations no longer apply.

3. **AEO workflow documentation** (S6) — The AEO audit project exists but hasn't been documented for external consumption. Need Josh's process review first.

4. **Curated 3rd-party plugin/skill list** (S2) — Need to evaluate external resources (coreyhaines31/marketingskills, awesome-claude-code lists, Anthropic's official skills repo) and curate a recommended list.

5. **Whimsical flowcharts** (Hub + all spokes) — Per Tim/Nathan meeting, each command/skill process gets a visual flowchart. None exist yet.

6. **Office hours structure** (Hub) — Need to define format, cadence, signup mechanism.

7. **AEO query validation** — Need Ahrefs MCP data to validate target queries before finalizing structure.

### 3.5 Recommended publishing sequence

**Phase 1: Foundation (weeks 1-2)**
1. **Hub page** — Rewrite animalz.co/claude-code as the living guide hub. This immediately replaces outdated content and establishes the /claude-code URL as the destination.
2. **S3: CLAUDE.md for Content Teams** — Publish alongside hub. Most immediately useful for anyone who reads the hub and wants to get started.

**Phase 2: Hero content (weeks 3-4)**
3. **S1: Structured Writing Process** — The piece that demonstrates Animalz's depth. This is the content no competitor can replicate because it's based on a real, sophisticated, production-tested writing system.
4. **S2: Commands/Skills/Plugins Cheat Sheet** — Reference material that drives return visits and plugin installs.

**Phase 3: Depth (weeks 5-8)**
5. **S4: Claude Code vs. Workflows vs. Agents** — Thought leadership piece. Can also be adapted for WER newsletter.
6. **S5: Agents for Content Research** — Intermediate-level content for users who've graduated past basics.
7. **S6: AEO Workflows** — Depends on Josh's process review being complete.

**Ongoing:**
- Update hub page as new features launch, new plugins are added, or new spoke articles publish
- S7 (Opus 4.6 changes) can be a LinkedIn/WER piece any time rather than a formal spoke

---

## Part 4: Strategic recommendations

### 4.1 Positioning

**Tagline concept:** "Practical, plug-and-play Claude Code for content teams"

**Key differentiators to emphasize:**
1. **Production-tested, not theoretical.** Everything featured is used daily at Animalz.
2. **Install and go.** Plugins and commands readers can use immediately.
3. **Process, not prompts.** The /write command isn't a prompt — it's an 8-phase editorial system. That depth is unique.
4. **Agency perspective.** We've solved the problems content teams actually face (voice consistency, quality gates, team scaling).

### 4.2 Distribution plan

| Channel | Content | Timing |
|---|---|---|
| Animalz blog (/claude-code) | Hub + all spokes | Ongoing |
| LinkedIn (Tim) | Announce each spoke, share excerpts, reboot Claude 101 series | Weekly during campaign |
| WER Newsletter | Deep-dive excerpts, behind-the-scenes of building /write | 1-2 featured issues |
| Claude Partner Network | Share hub as credibility piece in application | When hub is live |
| Monthly team call | Demo featured workflows live | Ongoing |
| Office hours | Drive to hub page for resources | Regular cadence |

### 4.3 AEO optimization approach

Per Tim/Nathan meeting, use Ahrefs MCP to:
1. Pull actual search volume for target queries identified in 2.5
2. Identify question-format queries for the FAQ section
3. Find long-tail opportunities for spoke articles
4. Structure FAQ section with exact question phrasing from search data

Recommend running Ahrefs analysis as a separate task before finalizing the hub outline.

### 4.4 Risks and considerations

1. **Velocity of change.** Claude Code ships features weekly. The hub structure must accommodate frequent updates without full rewrites. Recommendation: date each section, use "last updated" timestamps.

2. **Plugin architecture changes.** Commands/skills merged in v2.1.3. More changes likely. Keep the extensibility section focused on concepts (what can you customize) rather than implementation details (exactly how the YAML works).

3. **Competitor content growing fast.** Multiple dedicated sites (claudecodeformarketers.com, cc4.marketing, claudecodeplugins.io) have appeared. Speed matters — the hub should go live within 2 weeks, not 2 months.

4. **Balancing Animalz vs. personal brand.** Some content (like /write) lives in Tim's personal writing-assistant repo. Clear attribution and cross-linking needed. The hub is Animalz content; WER can cover the personal building-in-public angle.

5. **Claude Partner Network timing.** Application pending (`328df6dc`). If approved, this changes distribution possibilities significantly. Consider aligning hub launch with partnership announcement if timing works.

---

## Appendix: Source index

### Internal files referenced
- Published article: `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/projects/internal/author-fingerprint-research/corpus/tim/20251002 claude-code-for-content-marketers-a-no-code-guide-animalz.md`
- AirOps draft: `/Users/timmetz/Developer/Projects/Animalz/content/claude-code-airops-agents/drafts/20260109 1025 claude-code-vs-airops-vs-agents.md`
- AirOps research: `/Users/timmetz/Developer/Projects/Animalz/content/claude-code-airops-agents/20260111-ai-agent-research.txt`
- Plugins repo: `/Users/timmetz/Developer/Projects/Animalz/claude-plugins/README.md`
- /write command: `/Users/timmetz/Developer/Projects/Personal/writing-assistant/.claude/commands/write.md`
- /copywrite command: `/Users/timmetz/Developer/Projects/Personal/writing-assistant/.claude/commands/copywrite.md`
- Content strategy: `/Users/timmetz/Developer/Projects/Personal/writing-assistant/CONTENT_STRATEGY.md`
- Knowledge base playbook (commands from knowledge): `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/knowledge-base/src/content/playbook/build-commands-from-knowledge.md`
- Knowledge base playbook (onion framework): `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/knowledge-base/src/content/playbook/ai-workflow-onion.md`
- Intelligence OS CLAUDE.md: `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os/CLAUDE.md`

### Notion pages referenced
- Claude Code Hub Guide: `313df6dc-2cc5-804a-b2a0-ca77fa4e893b` (work)
- Claude Code 101 series: `27eedc77-7df2-8051-af34-f4cf38e38cde` (personal)
- Claude Partner Network application: `328df6dc-2cc5-80db-81de-c9b9a55a35f6` (work)
- Sync with Tom on usage patterns: `329df6dc-2cc5-816d-809b-d5571544db72` (work)
- Review Josh's AEO process: `30ddf6dc-2cc5-8160-bdba-f0df0fdf7696` (work)
- Inform team re: Notion KB from Claude Code: `30ddf6dc-2cc5-812b-a1a9-c080c3525647` (work)

### External sources
- [Anthropic: Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)
- [What's new in Claude 4.6](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)
- [TechCrunch: Opus 4.6 with agent teams](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/)
- [InfoQ: Opus 4.6 context compaction](https://www.infoq.com/news/2026/03/opus-4-6-context-compaction/)
- [Claude Code March 2026 updates](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)
- [Every: How to Use Claude Code for Everyday Tasks](https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required)
- [Every: Common Beginner Questions](https://every.to/source-code/claude-code-the-most-common-questions-beginners-ask)
- [Claude Code for Marketers (course)](https://claudecodeformarketers.com/)
- [cc4.marketing (interactive course)](https://cc4.marketing/)
- [MKT1: What 4 Marketers Are Building](https://newsletter.mkt1.co/p/real-marketers-claude-code-builds)
- [Product Talk: Claude Code for non-technical people](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)
- [coreyhaines31/marketingskills (GitHub)](https://github.com/coreyhaines31/marketingskills)
- [awesome-claude-code (GitHub)](https://github.com/hesreallyhim/awesome-claude-code)
- [FlorianBruniaux/claude-code-ultimate-guide (GitHub)](https://github.com/FlorianBruniaux/claude-code-ultimate-guide)
- [Anthropic official skills repo](https://github.com/anthropics/skills)
- [Claude Code plugins hub](https://claudecodeplugins.io/)
- [Discovered Labs: Claude Code for AEO](https://discoveredlabs.com/blog/how-to-leverage-claude-code-for-aeo-geo-optimization)
- [Search Engine Land: Claude Code as SEO command center](https://searchengineland.com/claude-code-seo-work-470668)
- [DEV Community: Cursor vs Windsurf vs Claude Code comparison](https://dev.to/pockit_tools/cursor-vs-windsurf-vs-claude-code-in-2026-the-honest-comparison-after-using-all-three-3gof)
