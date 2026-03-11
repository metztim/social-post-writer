# Review Notes — Context Engineering Article

**Reviewer:** Tim Metz (editorial pass, 2026-02-26)
**Source:** my-os/data/task-agent/2026-02-23/context-engineering-article-tim-revised.md

## General editorial directives

1. **Treat all additions/changes as editor notes**, not verbatim directives. Tim has given direction and thoughts; the writer should polish and improve.
2. **Use "customers" throughout**, never "clients."
3. **Add more second-person singular** to reduce distance to reader.
4. **H2 headers feel generic** and not in typical Animalz style. Need to check/build Animalz style guide for header guidance.
5. **Consider the "team not individual" angle** as a potential central thesis or more prominent thread throughout.
6. **Cross-reference** the AI Services positioning doc: https://www.notion.so/animalzco/AI-Services-Positioning-312df6dc2cc58154acf7f2b91d74c1fd
7. **Search Logseq** for additional relevant data, insights, or quotes.
8. **Consider blog vs. playbook** (Animalz blog, knowledge-base in animalz-intelligence-os, or both).

## Section-by-section inline comments

### Introduction
- No specific comments. Tim revised the opening from third-person to second-person ("Your marketing team...") and tightened the hook.

### The rise of context engineering
- {placeholder}: Insert Karpathy's title/role/description
- {placeholder}: Insert descriptive words for LangChain
- **Comment:** "The following two grafs feel a little out of the blue. I wonder if these should open the section, and then we weave in its origins and how it took off."
- **Comment on "what the model sees when it answers":** "That makes it sound as if the model looks at the context when it has finished its answer. But it's more about all the info you give it to help it figure out the right answer or action, right?"
- **Comment on adjusted definition:** "If prompt engineering was about crafting the perfect question, context engineering is about building the perfect information environment for the AI to operate in within each step of a process." — Tim asks: "Let me know what you think of this adjusted definition."

### Why most AI content operations produce commodity output
- **Comment on "typical workflow" paragraph:** "Too simplistic. This is probably what happened in 2024, and might still happen at some companies, but we should assume forward-thinking AI teams are a bit more sophisticated. They'll probably do SEO research and include that data, plus examples, expert interview transcripts, but then throw it into a ChatGPT or Claude project. That produces 'decent' content, but it's mostly the same as everyone else."
- **Comment on "well-engineered context" list:** "Here we also need some more sophistication... Consider everything we're doing in animalz-intelligence-os. We're pulling in data from external APIs and MCPs; feeding previous posts and engagement metrics back; programmatically evaluating and testing outputs; doing dedicated brand calibration sessions; constructing rich bios of authors, etc. Search the entire project for the best examples."
- **Comment on closing line:** "'The gap between these two approaches is the difference between decent and delightful content' — maybe there's a better way? Like average and amazing; or AI slop and {insert something}"
- Tim flagged an apparent editing artifact: "not incremental." appears as orphaned text on line 97.

### Context engineering as a system design problem
- {placeholder} after each sub-problem: "insert example from our work/system"
- **Freshness problem comment:** "These situations feel accurate but boring. Something like 'Twitter/shit happens.' 'Your competitor lowers prices/disses you in an ad.' More real but fun examples."
- **Orchestration problem comment:** "As a regular reader, I'd think: these sound easy. Why is this hard? It gets more difficult when you think about 'how to pull your most recent published posts from LinkedIn? How do I get the latest AEO visibility data right before my production run?'"
- **Compression problem comment:** "I would soften this slightly. Latest models (e.g., Opus 4.6) seem to handle large context well. But still better to have relevant context than overload with unnecessary context."
- **Evaluation problem comment on "is working":** "I'm wondering if 'helpful' or 'beneficial' is clearer? Had to read twice."
- **Evaluation problem comment on testing:** "Most readers wouldn't understand this. In simpler language: 'In traditional software, something either works or it doesn't, making testing (relatively) easy. Writing is more subjective, so knowing whether your context made things better or worse is much harder.'"
- {placeholder}: "Insert something about evals here and how we've started using those, and link to Lenny's podcast about evals."

### What this looks like in practice
- **Comment on section title:** "Feels like a throwaway H2. What we're trying to do here is describe our solution: a central context library, which some call a 'context graph.' Pull in research on this term from web and Logseq."
- Tim renamed "Intelligence Library" → "Animalz Intelligence OS"
- **Comment on "first and third party data":** "Maybe clunky, but I want something that captures the idea of adding almost real-time data, whether our own engagement metrics or weather data from a third party API. Maybe there's a better term?"
- **Comment:** "We should also add somewhere that this system/library is more of a concept than tied to a specific tool. Can be as basic as a spreadsheet to Notion bases to Supabase or data warehouses."
- **Comment on bullet list:** "We should add raw materials like interview transcripts, first and third party data, AEO visibility data, etc. Scan our whole system for examples of what we store."
- **Comment on Stuut/fintech example:** "Not sure if this is convincing. Better example: before we ingested previously published posts into a LinkedIn workflow, output sounded authentic individually but felt repetitive across posts. Adding actual published posts and engagement data made performance jump."
- **Comment on organizational challenge:** "Important point to make somewhere: You don't only build your context graph for the AI models. As workflows work, less time goes to raw production but more info floods in — customers submit more materials, workflows produce more briefs/drafts, AI surfaces more research. Managing all that becomes an organizational/logistics challenge, which is why you need a categorized system."

### The context engineering skill gap
- **Comment on framing as "skill gap":** "Strange phrasing — makes it sound like you need all skills in one person. Actually, this might be a really interesting and contrarian angle: many people think a 'context engineer' is one role. Actually it's a combination that almost always requires a team. Tim's example: he covers all four for Animalz, but for customers, he lacks domain expertise while the services team knows the customer but can't build AI systems."
- **Comment on Chrome extension:** "We've even started involving customers in context engineering. Created a submission form and Chrome extension clipper that allows team and customers to capture content into Raw Materials."
- **Comment on AI Onion:** "I think we can work in and reference the AI Onion article (https://www.animalz.co/blog/ai-onion) — this is exactly what the onion is about. Maybe include practical tips and reference the onion for depth."

### What to do about it
- **Major comment:** "Tips are directionally right but feel hand-wavy and sometimes generic. Most leave me wondering: ok, but HOW do I do this?"
- **Tim's brainstormed alternatives (from comment):**
  1. Start with basics: up-to-date style guide, gold star examples, audience info, author bio (rich bio makes writing better)
  2. Don't overcomplicate infrastructure. You might outgrow Notion in 18 months, but AI makes migration easy now. Less lock-in. More of a two-way door decision.
  3. Accommodate team preferences. Services team didn't feel comfortable editing brand kits in AirOps, so moved to Notion. Make it easy to add/update context — Google Docs readers, browser extension, YouTube transcription from links via web form.
  4. Give workflow context about recent content. Individual workflows don't know what you wrote last week. Solutions: 1) loading similar topics from a sitemap in AirOps, 2) loading recent social posts + engagement via Ordinal API.
  5. Do blind tests. Let stakeholders/readers judge without knowing who/what created content. Easy to set up with Claude Code. 10-20 rounds between human vs. AI, different models, or different context/prompts gives signal.
  6. Look at what's really going into prompts. In AirOps, prompts look reasonable with variables, but actual resolved prompts can be huge with lots of overlap.

### The bottom line
- **Comment on model convergence claim:** "I agree a little but also not. True for content creation, but not all industries/AI uses. Not 100% convinced models are converging — Anthropic → coding/enterprise, Google → consumer/product, OpenAI → both. Too hard to call definitively."
- **Comment on "context systems":** "Important distinction needed throughout: context is a component of the overall AI content system, not a system in or by itself."
- {placeholder}: "insert word that signals super star content but ideally alliterates with slop"
- **Comment on conclusion length:** "Getting there, but can probably make the same point more powerfully with 35% fewer words."

## Comparison: original vs. revised (task #7 — to be completed)

_To be filled in during Phase 2 content work: highlight regressions, improvements, and further opportunities._
