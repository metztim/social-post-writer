---
source_of_truth: local draft
note: First draft for WER 2026-03-23. Needs Tim's review before writing to Notion.
---

## This article couldn't exist without AI. And AI couldn't have written it.

Last week I published my second long-form piece on the Animalz blog in two weeks. [Your Prompts Are Fine](https://www.animalz.co/blog/context-engineering) was about 65% AI-generated. This one — not even close.

[Don't Stop at Workflows: Build a Compounding Content System](https://www.animalz.co/blog/content-system) went through four versions, two human editors, and months of iteration before it was ready. The ideas had to be lived first. You can't AI-generate "I spent several months cursing at my computer before the workflows worked" — that was just my actual life.

But here's the thing. The article also couldn't have existed without AI. Not the writing — the *making*. Claude Code published it to our Statamic CMS. The Whimsical MCP server generated the flowcharts. Nano Banana Pro (Gemini's image model) created the visuals. I vibe-coded a customer onboarding form that became one of the article's key examples. **The article about building AI content systems was itself built by AI content systems — just not the parts you'd expect.**

That's what I think most people get wrong about AI and content. The conversation is always about whether AI can *write*. But writing was the smallest part of shipping this piece. The leverage was in everything around it.

**[Don't Stop at Workflows: Build a Compounding Content System](https://www.animalz.co/blog/content-system)**

## Reads & Listens

### When AI "factchecks" a war photo — and gets it wrong

[This Guardian piece](https://www.theguardian.com/global-development/2026/mar/17/atrocity-ai-slop-verify-facts-iran-minab-graves) covers how Gemini and Grok confidently misidentified a real photo from the Iran war — each hallucinating a completely different (wrong) origin story. The cemetery of Minab, a photo of graves for over 100 schoolgirls killed by a missile, was real. Both AIs said it wasn't. Both provided fake sources.

The problem is real and serious. But the article itself commits a version of the same sin it criticizes: no model attribution. "Gemini" and "Grok" — which versions? The free consumer tier? The latest Pro model? These are vastly different systems. I'm fairly confident that a frontier model like Claude Opus 4.6 would say "I cannot verify the provenance of this image" rather than confidently fabricate a Turkish earthquake origin story. The calibration gap between model tiers is enormous.

**Two things can be true: AI providers should be much more aggressive about warning users on sensitive topics — especially on basic, free-tier models. And reporters covering AI should provide version numbers.** Saying "Gemini hallucinated" without specifying which Gemini is like saying "a car crashed" without specifying whether it was a 20-year-old beater or a car with full self-driving. The distinction matters for understanding the actual risk.

### I've been tracking AI bubble commentary for five months. Here's how the narrative shifted.

Since October, I've been highlighting articles and podcasts about the AI bubble question. Not on purpose at first — it just kept coming up in my reading. When I looked back at the trail this week, the pattern surprised me.

[IMAGE: bubble-timeline.png]

In October, most smart analysts were hedging or outright calling it a bubble. M.G. Siegler called it ["a bet that could bust."](https://spyglass.org/ai-bubble/) Ben Thompson wrote that [bubbles build infrastructure](https://stratechery.com/2025/the-benefits-of-bubbles/) — acknowledging the bubble while finding the silver lining. Howard Marks published a [careful Oaktree memo](https://www.oaktreecapital.com/insights/memo/is-it-a-bubble) drawing dotcom parallels. Cal Newport argued in the New Yorker that [AI agents failed to live up to their hype](https://www.newyorker.com/culture/2025-in-review/why-ai-didnt-transform-our-lives-in-2025).

Then in early 2026, the product started catching up to the investment. Dario Amodei [wrote about models solving unsolved math](https://www.darioamodei.com/essay/the-adolescence-of-technology). Matt Shumer declared the ["hitting a wall" debate over](https://shumer.dev/something-big-is-happening). And this month, Ben Thompson published [Agents Over Bubbles](https://stratechery.com/2026/agents-over-bubbles/) — explicitly flipping from his November position: "I no longer believe we're in a bubble."

Not everyone agrees. Paul Kedrosky went on Derek Thompson's podcast to say ["Yes, AI is a bubble. There is no question."](https://www.derekthompson.org/p/yes-ai-is-a-bubble-there-is-no-question) **The consensus didn't shift in one direction — it dissolved.** The skeptics got louder. The middle moved toward "maybe not." And the thing that changed wasn't the investment numbers — it was the product. Agents that actually work turned a valuation debate into a capability debate.

### 86,000 NYT readers can't tell the difference

The New York Times [ran a blind taste test](https://x.com/kevinroose/status/2031397522590282212): human writing vs. AI writing, five questions, pick your favorite. 86,000 people took it. 54% preferred the AI version. Preference was even higher for factual reporting (62%) than opinion pieces (48%).

Around the same time, the FT's Elaine Moore [made the point](https://www.ft.com/content/b2ebb99a-cfea-465f-93ff-0ea8ed6bfac5) that detection now depends more on context than content. If you know someone's style is sparse and they produce 800 words of florid text — sure, maybe AI. But in a blind test? Good luck. She also noted that AI companies pulled back on em dashes once people started flagging them. **The tells keep disappearing. The detection game is basically over — for both humans trying to spot AI, and AI trying to spot reality** *(see the Iran piece above)*.

---

One more thing: I'm working on an extended Claude Code guide for the Animalz blog. If you have specific questions about Claude Code, things you'd like covered, or topics you're curious about — hit reply. I'm actively collecting input for the guide.

Thanks for reading!

Tim
