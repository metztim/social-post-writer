---
source_of_truth: local draft
note: V2 — Tim rewrote the featured section. Claude improving flow + tightening.
---

## This article can't live with AI — and can't live without it

Last week I published my second long-form piece on the Animalz blog in two weeks. The first — [about context engineering](https://www.animalz.co/blog/context-engineering) — was ~65% AI-generated. This one, not at all.

[Don't Stop at Workflows: Build a Compounding Content System](https://www.animalz.co/blog/content-system) went through four versions, two human editors, and months of iteration before it was ready. I had to think — and therefore write — my way through what I really wanted to say.

With context engineering, the purpose was clear from the start: define the concept and share what I'd learned from building with it. The content system piece was harder. I started by trying to break down the entire architecture. Too complex. Then a mix of principles and architecture — even more confusing. I eventually landed on a "here's how we built it" story, and that felt right. But it still needed a major rewrite before it really worked.

Through all of this, I used AI to polish each draft. And after each round of polishing, it said: this is great, let's ship it.

My human editors disagreed.

AI still has some way to go before it can really diagnose whether something works — not just at the sentence level, but strategically, structurally, conceptually.

And yet the article in its current form couldn't have existed *without* AI either.

Not the writing — the *making*. Claude Code handled the entire publishing workflow to the Animalz CMS *(this might sound trivial if you've never had to publish a blog post, but anyone who has knows it can easily take 15–45 minutes without automation)*. The Whimsical MCP generated the flowcharts. Nano Banana Pro (Gemini's image model) created all the visuals. And the assets discussed in the article — like the intelligent onboarding form and Chrome plugin — I vibe-coded.

**Even in the writing, AI helped a lot with polishing and research. This article would never have existed in its current form without AI. But it also shows that any serious thinking and strategy still needs humans.**

**[Don't Stop at Workflows: Build a Compounding Content System](https://www.animalz.co/blog/content-system)**

## Reads & Listens

### Why sloppy AI reporting makes misinformation harder to fix

More than 100 schoolgirls were killed by a missile in Minab, Iran. A photo of their freshly dug graves went around the world. When people turned to AI to verify the image, [both Gemini and Grok told them it was fake](https://www.theguardian.com/global-development/2026/mar/17/atrocity-ai-slop-verify-facts-iran-minab-graves) — each confidently hallucinating a different (wrong) origin story, complete with fabricated sources. The photo was real. The AI "factchecks" were not.

This is genuinely dangerous. When AI tools deny evidence of atrocities, people suffer — families who lost children see their grief questioned. The Guardian piece covers this well. But there's a problem with how the article — and most AI reporting — frames the issue: no model attribution. "Gemini" and "Grok" — which versions? The free consumer tier you get on Google Search? The latest Pro model? These are vastly different systems with vastly different accuracy.

That distinction matters *because* the stakes are this high. If we want to actually fix the problem of AI-powered misinformation, we need to know where the failures are. A frontier model would likely say "I cannot verify this image" rather than fabricate a Turkish earthquake origin story. **The real scandal isn't just that AI hallucinated — it's that the weakest, least calibrated models are the ones hundreds of millions of people use as default fact-checkers, and nobody is being precise about that.** Not the AI providers, who bury disclaimers in fine print. And not the reporters covering it, who write "Gemini" without a version number — like writing "a car crashed" without saying whether it had airbags.

### The AI bubble narrative is shifting — I tracked it

Since October, I've been highlighting articles about whether we're in an AI bubble. Back then, most voices were hedging or calling it outright: Siegler called it ["a bet that could bust,"](https://spyglass.org/ai-bubble/) Thompson said [bubbles build infrastructure,](https://stratechery.com/2025/the-benefits-of-bubbles/) Marks drew [dotcom parallels,](https://www.oaktreecapital.com/insights/memo/is-it-a-bubble) Newport said [agents failed to deliver.](https://www.newyorker.com/culture/2025-in-review/why-ai-didnt-transform-our-lives-in-2025)

Then the product started catching up. Shumer declared the ["hitting a wall" debate over.](https://shumer.dev/something-big-is-happening) And this month, Ben Thompson explicitly flipped: ["I no longer believe we're in a bubble."](https://stratechery.com/2026/agents-over-bubbles/) *(Not everyone agrees — Kedrosky [called it a bubble "without question."](https://www.derekthompson.org/p/yes-ai-is-a-bubble-there-is-no-question))*

**The consensus didn't shift — it dissolved.** I used Claude Code to map the trend from my reading highlights:

*[IMAGE: bubble-timeline.png]*

### 86,000 NYT readers can't tell the difference

The New York Times [ran a blind taste test](https://x.com/kevinroose/status/2031397522590282212): human writing vs. AI writing, five questions, pick your favorite. 86,000 people took it. 54% preferred the AI version. Preference was even higher for factual reporting (62%) than opinion pieces (48%).

Back in December, the FT's Elaine Moore [already argued](https://www.ft.com/content/b2ebb99a-cfea-465f-93ff-0ea8ed6bfac5) that detection depends more on context than content. If you know someone's style is sparse and they produce 800 words of florid text — sure, maybe AI. But in a blind test? Good luck. She also noted that AI companies pulled back on em dashes once people started flagging them. **The tells keep disappearing. The detection game is basically over — for both humans trying to spot AI, and AI trying to spot reality** *(see the Iran piece above)*.

---

One more thing: I'm working on an extended Claude Code guide for the Animalz blog. If you have specific questions about Claude Code, things you'd like covered, or topics you're curious about — hit reply. I'm actively collecting input for the guide.

Thanks for reading!

Tim
