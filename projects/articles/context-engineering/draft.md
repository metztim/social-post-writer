# Your Prompts Are Fine: Context Engineering Is Your Next AI Problem

<!-- H1 ALTERNATIVES for Tim:
1. Context Engineering Is the Discipline That Separates AI Demos From AI Results
2. Same AI, Different Context, Completely Different Results
3. Why Your AI Content Sounds Like Everyone Else's
4. The Missing Discipline in AI Content
5. Context Engineering Is a Team Discipline, Not a Solo Skill
6. What Content Teams need to know about context engineering
7. Context Engineering: The Missing Layer in Your AI Content Stack
8. Your AI Prompts Are Fine. Your Context Is the Problem.
9. Your Prompts Are Fine: Context Engineering is your next AI Problem (leading candidate)
-->

If you've built an AI content workflow that technically works but produces output you'd never actually publish, the problem isn't your prompts. It's your context — everything the model doesn't know about your brand, your audience, and your editorial worldview.

What you need is better context engineering, the discipline of building the right information environment for every step of your AI workflow. Here we'll talk about why it's harder than most teams expect and how to start closing the distance.

## Context is the new prompt

If prompt engineering is about crafting the right question, context engineering is about building the right information environment: the data, examples, constraints, brand knowledge, and strategic intent that shape every step of your workflow. It's also how those elements get orchestrated, compressed, and refreshed over time.

The term is recent. Shopify CEO Tobi Lutke coined it in June 2025, describing it as "the art of providing all the context for the task to be plausibly solvable by the LLM." Andrej Karpathy followed days later. By late 2025, Anthropic had published a comprehensive engineering guide on it, and LangChain's State of Agent Engineering report found that 32% of organizations cite output quality as their top AI barrier with most failures traced to context, not model capability.

## The 7 elements of great context

The better AI content teams are already doing the basics for their context engineering: SEO research, expert interviews, reference examples, a style note in the workflow. The output is grammatically correct, topically relevant, factually sound.

It's also indistinguishable from every competitor in the industry.

It's garbage context in, garbage content out. Decent context produces decent content. *Great* content requires well-engineered context. Most teams already provide the basics — product knowledge, company facts, a style note. These seven elements are the differentiating layer on top:

- **Brand intelligence:** A curated voice guide built from systematic analysis of your best-performing content — vocabulary, rhetorical patterns, what makes the voice distinctive.
- **Author intelligence:** How this person actually thinks and communicates — rhetorical habits, the analogies they reach for, the opinions they hold, the experiences they draw from.
- **Strategic context:** The brand's editorial worldview. Where it aligns with industry consensus, where it deliberately diverges, and why.
- **Audience model:** Not demographics but decision context — what this audience already knows, what objections they carry, what they're trying to decide, and how they actually talk about it.
- **Competitive intelligence:** What everyone else is already saying, so the model can take positions that are actually differentiated.
- **Quality examples:** Exemplary pieces that demonstrate the target standard, not abstract rules about good writing.
- **Dynamic data:** Recent engagement metrics, trending topics, your own recently published content so the AI isn't retreading last week's angles.

So why doesn't everyone do this? Because context engineering is genuinely hard. Harder than most teams expect.

## Context engineering is harder than it looks

Everyone hears "context engineering" and puts all the weight on "context." But "engineering" is half the work. This is essentially a system design challenge with four interlocking problems.

**Curation.** Out of everything that could be relevant, what does the model actually need for this specific step? You can't just dump an entire knowledge base into a context window. Chroma's research on "context rot" shows that model accuracy degrades as irrelevant tokens accumulate, even well within technical limits — a finding Anthropic has built into their context engineering framework. An 8-component brand kit might total 15,000 tokens, but a LinkedIn drafting step doesn't need the competitive intelligence section, and a brief-generation step doesn't need the format examples. Each step gets only what's relevant.

**Freshness.** Context goes stale faster than you'd expect. A competitor launches a campaign. A CEO says something on a podcast. Pricing changes overnight. You need mechanisms to keep context current without someone manually updating a document every time something shifts. We pull engagement data from a social analytics API every 24 hours so our workflows know what's resonating. A separate tool monitors trending topics in each customer's industry — when it detects a signal, our system can draft a timely post within 30 to 60 minutes.

**Orchestration.** Different workflow steps need different context, from different sources, in different formats. How do you get the latest search visibility data right before a production run? How do you make sure the brief-generation step has brand strategy but the drafting step has the voice guide? The challenge is designing data flows that deliver the right context at the right moment without human intervention.

**Evaluation.** How do you know your context is actually helping? A change to the voice guide might improve tone but degrade accuracy. The most reliable signal we've found is blind testing: 10 to 20 rounds where stakeholders judge output without knowing whether it came from a different model, a different context configuration, or a different prompt. It's surprisingly easy to set up and consistently reveals what's actually working versus what you assume is working. (Hamel Husain and Shreya Shankar's work on AI evals shaped how we think about this.)

## Context engineering is a team discipline

Here's what two years of building AI content systems taught me: this isn't one person's job, and you won't solve it with a single hire.

Doing it well requires four capabilities that rarely live in the same person.

1. **Domain expertise** — you can't engineer context for a topic you don't deeply understand.
2. **Editorial judgment** — selecting exemplary content, defining voice, and calibrating quality are editorial skills, not technical ones.
3. **Systems thinking** — the orchestration, freshness, and curation challenges require structured thinking about data flows.
4. **AI literacy** — understanding how models process context, where attention degrades, and how formatting affects output requires hands-on experience with LLMs.

We ran into this directly with a customer's LinkedIn program. Their published posts were already in the workflow as voice reference, but the output kept retreading the same angles and structures. We broke the pattern by adding engagement metrics so the AI could see what had already performed and avoid repeating it. That fix required editorial judgment to identify the problem, AI literacy to understand why it was happening, and systems thinking to solve it. No single person on either side of that engagement had all three.

When we work with customers, the pattern is consistent: they bring domain expertise and editorial judgment; we bring systems thinking and AI literacy. Neither side can do it alone. And as workflows mature, a fifth challenge emerges — the context library itself becomes an organizational system, managing the growing body of intelligence that everything else depends on. Without someone owning that, it accumulates as noise instead of compounding as an asset.

This is what we described in our AI Onion framework: an AI workflow touches everything around it — input collection, quality controls, feedback loops, organizational processes. Context engineering done right is cross-functional by nature, not by preference.

## Six things we'd do from day one

Here's what we've learned from two years of building and iterating:

**Start with the basics — and take them seriously.** An up-to-date style guide, a curated set of gold standard examples, a clear audience profile, and a rich author bio. These four elements will improve any AI content workflow. The author bio especially — a detailed, specific bio that captures how someone thinks, what analogies they reach for, and what opinions they hold produces noticeably more human output than a generic credential summary.

**Don't overcomplicate your infrastructure.** You'll probably outgrow your first tool in 18 months, and that's fine. AI makes migration easier than ever. A Notion database is a perfectly good starting point. Don't let infrastructure anxiety keep you from starting.

**Make it easy for everyone to contribute context.** Our services team didn't feel comfortable editing brand kits in AirOps, so we moved that to Notion. We built a Chrome extension, a Google Docs reader, and a YouTube transcription form — multiple input methods so people use whatever's comfortable. The best context system is one people actually feed.

**Give your workflows awareness of recent content.** Individual AI workflows have no memory of what you published last week. Without that awareness, you get repetition. We solve this by loading similar topics from a customer's sitemap and pulling recent social posts with engagement metrics via API — the workflow can avoid retreading angles and build on what's performing.

**Run blind tests.** Let stakeholders judge content without knowing whether it came from a human, an AI, or a different context configuration. Ten to twenty rounds gives you real signal, not assumptions. It's easy to set up and consistently reveals what's actually working versus what you think is working.

**Inspect what your prompts actually contain.** In a workflow tool, prompts look clean and manageable with variables. But when those variables resolve, the actual prompt sent to the model can be enormous — with significant overlap between sections. Look at your resolved prompts regularly. You'll almost always find opportunities to compress, deduplicate, and improve.

## Context compounds. Model access doesn't.

The next phase of AI content won't be defined by which companies have the best models. The distance between models narrows with every release. The defining advantage will be the systems companies build around those models — and context is the most critical layer.

Every improvement to your brand intelligence, every refined example, every better-structured knowledge base makes every subsequent output better. A competitor can switch to the same model you're using overnight. They can't replicate two years of curated context.

And this is just the content side. The same pattern is already playing out across every function that touches AI: research, analysis, operations, customer support. As agents take on more of the work, the value shifts from doing the work to organizing the information that makes it possible. How you structure your knowledge, how you keep it current, how you make it accessible to the systems that need it, that becomes the work.

The teams building this muscle for content right now are practicing a discipline they'll need for everything else.
