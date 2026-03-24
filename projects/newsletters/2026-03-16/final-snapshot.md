---
source_of_truth: https://www.notion.so/timmetz/WER-Context-Engineering-325edc777df2808cb638e1b7c1561297
note: Final version written to Notion 2026-03-16. Tim will do a final edit pass before publishing.
---

## Context Engineering: how you make AI pull a rabbit out of a hat

When I first heard the term "context engineering" (sometime last year), I thought it was BS. I even wrote a [LinkedIn post](https://www.linkedin.com/posts/metztim_if-you-still-think-prompt-engineering-is-activity-7354461670066311168-8LGq) arguing people should forget about both prompt engineering AND context engineering.

I've changed my mind.

Since September 2025, I've been spending 95% of my time at Animalz on AI systems building and vibe coding — plus whatever spare hours I can find for personal projects. And what I've come to realize is that context is what matters most. Not how you phrase your prompt, but what information you provide the AI with and when in your process you provide it.

When you do this well, it can feel like AI pulls a rabbit out of a hat. Case in point: this article. Back in November, I jotted down "write article on context engineering" as a task. Forgot about it. Three months later, a background AI agent picked it up, went off on its own — pulling from my Notion workspaces, a decade of reading highlights, my local writing projects — and came back with a draft that became ~65% of the final article. The other 35% was me and Nathan Wahl editing, rewriting, and adding the parts only humans would think of. (See my [LinkedIn post](https://www.linkedin.com/posts/metztim_i-published-an-article-about-context-engineering-share-7438061504635207680-q6NV) about that.)

*The article about context engineering was itself a product of context engineering.*

The other essential insight: context engineering is often not something you can do alone. You need topical expertise, AI capabilities knowledge, systems thinking, and judgment about style and quality. It's rare to find all those things in one person.

My latest article on the Animalz blog explores this in more depth, including The 7 Elements of Great Context and what makes it hard.

**[Your Prompts Are Fine: Context Engineering Is Your Next AI Problem](https://www.animalz.co/blog/context-engineering)**

## Reads & Listens

Here's what stood out in my reading and listening this week.

### [Claude Opus 4.6 now has a 1M context window](https://claude.com/blog/1m-context-ga)

Anthropic made 1M context the default in Claude Code and available via the API. That's a 5x jump from the previous 200K limit.

In theory, more context is always better — but there's a thing called context rot: even though a model can handle a million tokens, the quality of its responses degrades as the context grows. The model loses focus, misses details, gets confused. This still happens with Opus 4.6. But the drop-off is much gentler than previous and competing models — meaningful degradation doesn't really kick in until past 500K tokens. So you can at least go double as long as before without noticing a quality hit.

### Europe can't do its own AI even when it wants to

[This Sacra research piece](https://sacra.com/research/100b-sovereign-ai-boom) on the $100B+ sovereign AI boom shows just how screwed Europe is when it comes to tech independence. It's a layer problem. Governments want to build their own AI models — but then they realize those models need to run somewhere. And there's no real European cloud provider. So their "sovereign AI" ends up running on AWS, Azure, or Google Cloud. US hyperscalers are actually some of sovereign AI's biggest beneficiaries — AWS launched its "European Sovereign Cloud" in January, Microsoft ships air-gapped Azure for governments. Countries are essentially "buying local" from the same American providers they're trying to reduce dependence on.

Germany's Aleph Alpha tried to build a European foundation model, couldn't keep up on quality, and retreated to consulting. Even France's Mistral — the European success story at $400M ARR — still runs on Nvidia GPUs.

What's funny is that in the same week I read this, I listened to the [Dwarkesh podcast with Elon Musk](https://www.youtube.com/watch?v=BYXbuik3dgA), and Musk makes a similar point about the US itself. Even the companies you'd think are the most self-sufficient — the hardware giants — have the same kind of dependency one layer down. "Nvidia's output is FTPing files to Taiwan. It's digital... a bitstream going to Taiwan." Apple sends files to China. Nobody actually makes their own stuff all the way down.

### [This Column Will Change Your Life: Helsinki Bus Station Theory](https://www.theguardian.com/lifeandstyle/2013/feb/23/change-life-helsinki-bus-station-theory)

Someone sent me this a long time ago (if it was you, thanks!!). I finally got around to reading it.

The Helsinki bus station theory, from photographer Arno Minkkinen, goes like this: all buses leaving Helsinki share the same route for the first few stops. Each stop is a year of creative work. After three stops, you show your work to someone and they say: "This looks like what [established person] already did." The temptation is to hop off, grab a cab back to the station, and pick a different bus. A different creative direction. Many people do this over and over.

The theory's point: if you stay on the bus, the routes eventually diverge. Your work becomes distinctly yours. But every time you switch buses, you reset to zero.

This month is my five-year anniversary at Animalz, which seems like an eternity. I've been wondering whether I'm stuck on a bus that's still at the same stops as everyone else — or whether the route is starting to diverge. Five years ago, the "AI + content" bus looked like what dozens of agencies were doing. Now, the intersection of AI systems building, content operations, and hands-on implementation experience feels like it's heading somewhere uniquely mine.

I've never enjoyed my role at the agency as much as now. Maybe that's what divergence feels like.

> "The Helsinki theory suggests that if you pursue originality too vigorously, you'll never reach it. Sometimes it takes more guts to keep trudging down a pre-trodden path, to the originality beyond. 'Stay on the fucking bus.'"
