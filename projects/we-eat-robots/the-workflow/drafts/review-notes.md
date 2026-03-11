# Review notes: The Claude Code Workflow that enforces your brand style guide

Reviewed: 2026-02-26
Reviewer: Tim Metz (via /represent-tim)
Feedback loop: 2026-02-26 (Tim's verdicts annotated below as **[VERDICT]**)

## Summary

Sara's done great work here — the article is engaging, well-structured, and captures the workflow accurately in most places. The writing has real personality and the anti-hype framing in the opener is exactly the right positioning. There are a handful of factual issues that need fixing before publication, a structural duplicate that slipped through, and some representation nuances I'd want to adjust. None of this requires a rewrite — it's specific, targeted fixes.

## Must-fix

### Duplicate step heading **[VERDICT: Flag for Sara]**

Step 6 ("Apply the corrections") appears twice. The first Step 6 covers the violations report output, the second covers the three apply options (manual, `--auto-apply`, `--dry-run`). These should be either:
- Merged into a single Step 6, or
- The first one renamed to "Step 6: Review the violations report" and the second to "Step 7: Apply the corrections"

The numbering matters because readers will follow this as a tutorial.

### LinkedIn URL **[VERDICT: Flag for Sara]**

The opener links to `https://www.linkedin.com/in/timmetz/` — my actual LinkedIn URL is `https://www.linkedin.com/in/metztim`. Please verify and correct. (This appears in the Tim Metz hyperlink in the second paragraph of the opener.)

### Internal contradiction about article summaries vs. full text **[VERDICT: Flag for Sara, with nuance]**

Tim's correction: The error was in the prompt, not Claude's default behavior. He didn't specify full articles, so Claude set tool mode to "summary." Once corrected in the instructions, it does pull full articles. Frame as: important to give clear instructions, not as a Claude limitation.

Step 3 says Claude Code "fetches and stores the full text of each article locally, not a compressed summary." But the "What doesn't shine" section says "During our session, Tim noticed that the style guide generator had used article summaries rather than the full text."

Both can't be true. The reality is: Claude Code is *supposed* to use full text, but it sometimes uses summaries if you don't watch it carefully. I'd suggest:
- Step 3: Remove "not a compressed summary" — just say it "fetches and stores each article locally"
- Keep the warning in "What doesn't shine" as-is — it's an important caveat

### "4x faster" vs "4-5x faster" **[VERDICT: Accurate but won't flag — too nitpicky for their publication]**

The sneak peek section says "4x faster than human review." I consistently describe this as 4-5x faster (5-10 min vs 40+ min). Small difference but I'd rather be precise about it. Change to "4-5x faster."

### "False negatives" in Step 4 **[VERDICT: Accurate but won't flag — up to them how to present it]**

The snuance matters in Tim's own writing but he doesn't feel it's his role to push on this in someone else's publication.

Step 4 says the AI "will occasionally give you false negatives." The actual issue is over-extraction — the AI identifies *too many* patterns as rules, not too few. The first version was unwieldy because it treated coincidences as rules. The correct framing would be something like: "will occasionally identify patterns that aren't actually consistent rules, or miss rules that should be there."

## Should-fix

### "Automating everything in sight" **[VERDICT: Right but won't flag — their stylistic choice, not a misrepresentation. Would flag if own channel.]**

The opener says Tim has "the specific kind of brain that, once it discovered Claude Code, immediately started automating everything in sight." This leans into exactly the hype the article's framing is supposed to push back against. I automate *strategically* — the whole point of the article is that this specific workflow solves a specific problem. Suggestion: "the specific kind of brain that, once it discovered Claude Code, started building workflows for everything he wished he had time to do manually" — or similar. The distinction matters.

### "You could have one running too" after the 20-30 minute claim **[VERDICT: Same — their style, their call. Not quoting Tim.]**

The opener says "He built the whole thing in about 20 to 30 minutes, which means by the time you finish this issue, you could have one running too." The 20-30 minutes is accurate for *me*, someone who's been building in Claude Code daily. A first-time user will need more time for setup, understanding the files, and reviewing the output. I'd soften to: "which means the build itself is faster than most meetings" or acknowledge that first-time setup takes longer.

### Alternative use cases in sneak peek don't fit **[VERDICT: Sara asked for alternatives in the doc. Tim brainstorming better ones.]**

The sneak peek lists "Alternative use cases: Competitor hubs · Category pages · Sales enablement assets." These are not alternative use cases for a style guide workflow. A style guide enforcer checks editorial consistency — it doesn't help build competitor hubs or sales assets. If alternative use cases are needed, more accurate ones would be: "Client brand audits · Freelancer onboarding · Content migration QA"

### Voice memo claim needs verification **[VERDICT: "I definitely said something along these lines" — confirmed roughly accurate]**

The Goldflow section says "Tim literally built this workflow from a single voice memo." I want to make sure this is accurate to what I said during the interview. I did use voice memos as input for Claude Code, but I'm not certain the *style guide workflow specifically* started from a voice memo. If I said this during our call, keep it. If Sara inferred it, we should either verify or soften to something like "Tim describes the typical Claude Code workflow as starting with a plain-language description of the problem."

### "90% of the rest autonomously" needs verification **[VERDICT: See voice memo above — same confirmation]**

Same section: "Claude Code created 90% of the rest autonomously." I don't recall giving a specific percentage. If this came from the interview, keep it. If it's editorial, I'd remove the specific number — it invites scrutiny about what counts as autonomous.

### "Tim is convinced AI will soon replicate anyone's writing style perfectly" **[VERDICT: Actually agrees! Won't put a timeline on it, but thinks 6-36 months. Still not a reason to stop writing.]**

Tim's correction: "I think that's true. I won't put a timeline on it, but I do think whether in 6 months or 36, we're going to hit a point where AI models can analyze and articulate and replicate your writing style better than you can yourself. So I'm not against this quote. I do think that's still not a reason to stop writing."

Original review said this was stronger than Tim's position — it wasn't. He holds this view. The review over-softened.

This is stronger than my actual position. I've said AI is getting better at extracting and applying patterns, and context windows are growing. But "convinced" + "perfectly" overstates it. I'd prefer: "Tim thinks AI is getting close to replicating individual writing styles" — less absolute, more honest.

## Consider

### Escaped characters

Throughout the article, `\!\!\!` and `\!` appear — these look like Google Docs conversion artifacts. Should be cleaned to `!!!` and `!` in the published version. (Sara may already be handling this in the Doc.)

### Bold density

Almost every paragraph has at least one bold phrase. When everything is emphasized, nothing is. Consider reducing bold to the truly key moments — the claims that matter most. Currently the bold is doing a lot of work and could be more selective.

### "Trash your English literature degree"

The phrase "You don't need to write code or trash your English literature degree" in the How to Build intro is fun and on-brand for The Workflow. Keep it.

### Caption on image1

"Tim can talk about Claude Code for hours. We're still here." — This made me laugh. Keep it.

### "It's AI, friend, not magic" in Step 4

Good line. On-brand. Keep.

### The Workflow warning section

The behavioral warning ("a human who is actually paying attention, not one who is relieved the hard part is over") is exactly the kind of caveat I'd add myself. Well done.

## Links review

### Links that should stay
- Claude Code product page (`claude.com/product/claude-code`) — essential
- Animalz website (`animalz.co`) — essential context
- Animalz blog Claude Code guide (`animalz.co/blog/claude-code`) — directly relevant, I wrote this
- Google Drive zip (prompts download) — essential for the tutorial
- Google Drive style guide example — useful reference
- Sara's and Diandra's LinkedIn profiles — standard

### Links to verify
- **Tim's LinkedIn URL** — currently wrong (see Must-fix above)
- **Carl Vellotti's "Claude Code for Everyone"** (`ccforeveryone.com`) — I didn't suggest this. Is this resource still current and accurate? Worth a quick check before publication.
- **Hannah Stulberg's "Claude Code for Everything"** (Substack) — Same. I didn't suggest this. Verify it's still good and up to date.

### Missing links I'd suggest adding
- **We Eat Robots newsletter** (`weeatrobots.substack.com`) — My newsletter is mentioned in the article intro but never linked. Add a link where I'm first described as "Author of We Eat Robots."
- **LinkedIn style guide post** — The original LinkedIn post about this workflow (`https://www.linkedin.com/posts/metztim_ever-since-chatgpt-came-out...`) would be a good link in the article, especially in the opener or the Goldflow section. It shows the original public description.

### Links that could be cut
- None feel excessive. The article has a reasonable link density.

## What works well

- **The opener is excellent.** The anti-hype framing ("AI hype is a new kind of yellow fever") sets the tone perfectly and positions this as different from the typical Claude Code breathlessness. The fake quotes are spot-on parody.
- **The problem framing** in "What triggered The Workflow" is accurate and relatable. "Brand style guide maintenance is the kind of task that always gets added to the list but never makes it to the top" — that's exactly right.
- **The parallel agent explanation** is the best I've seen anyone write about why this architecture matters. "One context window doing eight jobs at once will always deprioritize at least a few of them. Eight agents, each doing one focused job, do not." Clear, accurate, compelling.
- **The behavioral warning** is the kind of honesty most AI articles skip. "A workflow that builds itself in half an hour also lowers your standards in half an hour" is a great line.
- **The closing** ("you can automate the style check, you can't automate the thinking that makes the writing worth checking") captures exactly the tension I'm always trying to articulate.
- **Sara's voice** throughout is engaging and distinctive. The newsletter has real personality — the parenthetical asides, the "friend" address, the playful jabs. It's their publication and it sounds like them while still representing my views accurately.
