# Revision brief: Animalz Intelligence article

**Purpose of this document**: A working brief for Tim to revise the draft. Not a plan for Claude to execute.

---

## The diagnosis

The draft is trying to serve three purposes:
1. **Infrastructure case study**: Show how we built the system
2. **Creative thesis**: Establish that Claude Code makes building feel like writing
3. **Positioning play**: Subtly show AirOps implementations need serious partners

These purposes conflict in tone, structure, and audience expectations.

## Feedback synthesis

All three reviewers hit the same core issues:
- **Ronnie**: Audience confusion, title/content mismatch, underdeveloped principles, no clear business case
- **Peter**: Section order wrong (1,4,2,5,3), "building feels like writing" claim not demonstrated beyond intro, wants Stuut pilot mentioned
- **Nathan**: "clever over clear," doesn't understand/agree with the writing parallel, asks "what are we trying to do for people here?", headers don't communicate takeaways

**Core question from all three**: What is this piece trying to do for readers?

## Evaluation results

| Angle | Rating | Effort to fix | Key insight |
|-------|--------|---------------|-------------|
| **Framework** (3 principles) | 55% | Moderate rewrite | Closest fit, but principles diluted by bonus sections and implementation detail |
| **Case Study** (how we built it) | 52% | Moderate rewrite | Strong narrative bones; needs specifics, metrics, timeline, replicability |
| **Marketing** (need a partner) | 40% | Moderate rewrite | "Code-illiterate" and "vibe coding" actively undermine partnership positioning |
| **Product Story** (birth of AI) | 38% | Heavy restructuring | No characters, no stakes, no naming moment - requires complete reframe |
| **Creative Thesis** (feels like writing) | **25%** | Heavy restructuring | **The promise the title makes is what the draft delivers LEAST** |

### Critical finding

The current title ("AI Made Building our Content System Feel Like Writing") sets up an expectation that the content **barely addresses**. This explains all three reviewers' feedback:
- Nathan: "i'm not sure i agree with/understand the parallel between how you built this and 'the way a writer follows a draft'"
- Peter: "outside of the intro paragraph, I don't leave the post understanding how building feels like writing"
- Ronnie: "Title asserts but content doesn't demonstrate"

The draft is trying to be a creative essay but reads as an engineering case study.

---

## Final direction (confirmed with Tim)

### What this piece IS
A **narrative case study with principles** for **content/marketing leaders** that subtly signals: "This is complex. You need experts to build this for you."

### What this piece IS NOT
- A how-to guide for implementation (too complex, wrong audience)
- A DIY checklist (principles help leaders *evaluate and manage*, not implement)
- The "feels like writing" angle (separate piece, different audience, opposite message)

### Target audience
Content/marketing leaders or executives who:
- Have tried AI (ChatGPT training, shared prompts) and it's not really working
- Are maybe considering tools like AirOps
- Need to understand: "Yes, use these tools, but it's way more comprehensive than just building workflows"
- Don't need how-to details, but want to understand the shape of what's possible

### Publication
Animalz Intelligence (not traditional Animalz blog)

---

## Recommended structure

**1. Open with "before"** — Ground reader in the relatable problem

Your raw material:
> "Different team members had different prompts. Mostly Claude, some ChatGPT. Not really a shared library. Everyone had their own versions."

What to convey: This is the state many readers are in. It works, sort of. But it's not a system.

---

**2. The catalyst** — We decided to build something different

Keep brief. You started with AirOps workflows. But quickly discovered you were building something bigger.

---

**3. Three discoveries** — Each as a story beat, framed as discovery not prescription

Reframe the principles as "what we discovered" not "what you should do":

| Principle | Current framing (teaching) | Reframe as (discovery) |
|-----------|---------------------------|------------------------|
| Opportunities over optimizations | "Use AI to find opportunities" | "We weren't just making things faster—we were creating capabilities we didn't know we needed." |
| Systems over workflows | "Build systems, not workflows" | "The data needed a home. That changed everything." |
| Context over prompts | "Context engineering matters" | "Good prompts aren't enough. Context is the multiplier." |

**Important nuance on the framework:** The principles should still be *useful* to leaders — but useful for *evaluating and managing* AI projects, not for *implementing them*. Leaders can use the framework to:
- Recognize if their current approach (ChatGPT prompts, basic workflows) is missing something
- Ask better questions of their team or potential partners
- Know what good looks like vs. a half-measure
- Have language for what they need

This keeps the framework genuinely valuable while reinforcing "we figured this out through experience" rather than "here's your DIY checklist."

---

**4. Weave in the "bonus" insights** (don't name them as principles)

- **Customers over Confidence**: Part of the pacing. "We shipped before we felt ready. That urgency mattered."
- **Claude Code**: Brief explanation of what connects it all. Not "we can vibe code!" but "This is what makes the connections possible." Less accessibility, more capability.

---

**5. The "after"** — What this looks like now

- Concrete results (the 80% completion rate, the 30-60 minute trending content)
- The compounding nature: "Each piece creates new opportunities"
- Forward vision (briefly): feedback loops, expanding channels

---

**6. Close** — The implicit message lands

Not "here's how you can do this" but "this is what becomes possible."

Reader should feel: "I want this. Who builds this?"

### Revision checklist

As you revise, check these off:

- [ ] **Opening**: Replace "blah blah blah" dismissive opener with vivid "before" state reader recognizes
- [ ] **Section order**: Fix from 1, 4, 2, 5, 3 → chronological narrative flow (1, 2, 3)
- [ ] **Bonus principles**: Remove as named sections; weave insights into the narrative
- [ ] **"Code-illiterate" framing**: Remove or minimize (undermines "you need experts" positioning)
- [ ] **"Feels like writing"**: Remove entirely from title and body (save for future separate piece)
- [ ] **Claude Code section**: Reframe from "you can vibe code!" to "this is what makes the connections possible"
- [ ] **Principles framing**: Shift from "here's what you should learn" to "here's what we discovered"
- [ ] **Before/after contrast**: Make clearer what changed (add metrics where possible)
- [ ] **Ending**: Write an actual conclusion that lands the implicit "you need experts" message

### Title directions to consider

Remove "feels like writing" — options:
- "How We Built an AI Content System (And What We Learned)"
- "From Prompts to Platform: Building Animalz Intelligence"
- "Beyond Workflows: What It Actually Takes to Build an AI Content System"
- "We Thought We Were Building Workflows. We Were Wrong."
- "What We Discovered Building an AI Content System"

---

## Separate future piece (parking lot)

**"When Building Starts to Feel Like Writing"**
- Thought leadership for content marketers / content engineers
- Message: "You can do this too—vibe coding is accessible"
- Written from scratch, not derived from this piece
- Different publication channel (maybe Animalz blog)

---

## Additional feedback (post-brief)

### Nathan's follow-up (after reading Tim's Slack analysis)
> "the main premise is still vague: you need to build a whole system (of what? or that does what?)"

This challenges the thesis to be more specific. "You need a system" is too broad — the thesis needs to answer what kind of system and what it actually does that workflows alone can't.

### Ronnie's full feedback
- Audience confusion: piece can't decide who it's for
- Title asserts but content doesn't demonstrate
- No clear before/after business case
- Principles read as retrospective labels, not transferable guidance
- Creates more questions than answers for a savvy content marketer

### Tim's Slack analysis
- "Feels like writing" destabilized the piece — discovered during conclusion writing, reworked into intro
- Real goal: "getting good results with AI for content (at scale) requires much more than ChatGPT prompts or even AirOps"
- Audience: content/marketing leaders deciding how to use AI, not content marketers getting started
- Solution: narrative case study with principles framed as discoveries, more before/after, more results