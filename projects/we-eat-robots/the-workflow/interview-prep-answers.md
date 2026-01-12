# The Workflow Interview Prep Answers

> Tim Metz - Social Post Creator from Highlights

---

## INTRO

### Who you are, what you do, where you spend 'get-shit-done' energy

I'm a content marketing strategist at Animalz, where I help B2B companies build content systems that actually work. Outside of that, I write the "We Eat Robots" newsletter about AI workflows for knowledge workers—basically documenting everything I learn about making AI useful for real work, not just demos.

Most of my energy right now goes into two things: helping Animalz clients build content strategies that survive the AI shift, and building my own AI-assisted workflows that I can actually use day-to-day. The social post creator we're talking about today came from that second bucket.

### Overhyped AI claim that made you roll your eyes

There's this format I see all the time: "X just killed Y" — when X just released some new, usually not-so-amazing feature. Like "Beautiful.ai just killed Powerpoint."

It's lazy hyperbole that makes everything sound revolutionary when most releases are incremental. A new feature doesn't kill anything. The installed base, the switching costs, the workflows people have built—none of that disappears because someone shipped a nice demo.

The worst part is it trains people to expect revolution when what actually works is evolution. My most useful AI workflows aren't revolutionary—they're boring. They just save me 20 minutes on something I do every day.

---

## THE WORKFLOW

### Introduce the workflow like it's a superhero

**Name:** The Highlight-to-Post Pipeline

**Unique powers:**
- Turns scattered reading notes into LinkedIn posts that actually sound like me
- Uses a "negative fingerprint" (what I NEVER say) to catch AI-isms before they escape
- Saves about 50% of my drafting time while maintaining engagement rates
- Gets better over time through a continuous learning loop

**Why it's famous:**
This workflow enabled the most viral LinkedIn post I ever wrote. More importantly, it let me finally bridge the gap between consuming content (reading, highlighting) and creating content (posting). Before this, highlights just sat in my notes app. Now they actually turn into things.

### What problem were you solving?

Three connected problems:

1. **The highlight graveyard:** I was reading constantly, highlighting great stuff, and then... nothing. Those highlights sat unused in Logseq for months.

2. **AI posts sounded wrong:** Every time I tried using ChatGPT to draft posts, they came out generic. "Let's dive into..." "Here's the thing..." It wasn't my voice.

3. **Time pressure killed consistency:** Manual post writing takes me 45+ minutes. At that pace, I couldn't post consistently enough to build momentum.

### Measurable outcome you were aiming for

- **Time:** Cut post creation from ~45 minutes to ~20 minutes (50% reduction)
- **Quality:** Keep engagement rates within 10% of my manually-written posts
- **Accuracy:** Get to 70-80% of the draft unchanged during editing (meaning Claude is nailing my voice most of the time)

### What wasn't working before?

- Highlights scattered across apps, completely disconnected from my publishing workflow
- AI drafts that required 80%+ rewriting—at which point, why use AI?
- Context-switching cost: finding highlights → remembering why they mattered → drafting → editing
- No feedback loop to improve AI outputs over time

### Step-by-step walkthrough

**Step 1: Tag (Manual)**
While reading in Logseq, I tag interesting highlights with `[[socialpost]]`. Takes 2 seconds. This is the human taste decision—what's actually worth developing?

**Step 2: Scan (Automated)**
I run `/draft-linkedin-post` in Claude Code. A Python script scans my entire Logseq knowledge base for anything tagged `[[socialpost]]`.

**Step 3: Select (Manual)**
Claude presents the 3 most recent tagged entries with full context—the highlight, surrounding notes, and source. I pick which one I want to develop today.

**Step 4: Draft (Automated)**
This is where the magic happens. Claude Code loads my voice fingerprint—a 900+ line document that captures:
- What I NEVER say (the "negative fingerprint")
- My actual linguistic patterns
- My characteristic rhythm (em-dashes, white space, etc.)

It drafts a post applying all these rules.

**Step 5: Save (Automated)**
The draft saves to my Notion "MyContent" database with the raw Claude draft in a dedicated property.

**Step 6: Cleanup (Automated)**
The `[[socialpost]]` tag gets removed from the original Logseq entry and a link to the Notion post gets added. This prevents the same highlight from showing up in future scans.

### Tools at each step

| Step | Tool | Why this one |
|------|------|--------------|
| Tag | Logseq | Already my knowledge base, markdown-native |
| Scan | Python script | Handles special characters in filenames reliably |
| Select | Claude Code terminal | Shows full context at a glance |
| Draft | Claude Code + voice guides | Massive context window for the fingerprint |
| Save | Notion API | Where I track all content anyway |
| Cleanup | File modification | Prevents duplicate processing |

### Manual vs automated

**Manual (requires human judgment):**
- Tagging highlights (taste)
- Selecting which entry to develop (relevance)
- Final editing pass (voice nuances)
- Deciding when NOT to post

**Automated:**
- Scanning for entries
- Gathering context
- Drafting with voice rules
- Saving to Notion
- Cleaning up source

### Results

- **First Claude-drafted post:** 3.43% engagement rate (above my average)
- **Time savings:** 50%+ confirmed
- **Draft accuracy:** ~75% unchanged after editing (up from ~50% before the fingerprint)
- **Consistency:** Can actually maintain a posting cadence now

### Surprises (good and chaotic)

**Good surprise:**
The "negative fingerprint" approach was WAY more effective than I expected. Telling Claude what I NEVER say worked better than showing it examples of what I do say. AI is better at avoiding specific patterns than matching vague concepts like "conversational tone."

**Chaotic discovery:**
Initial drafts were consistently too long. Claude was being thorough when I needed concise. Had to add explicit length constraints.

**Limitation:**
Can't capture the "spark" of genuine insight. The workflow handles execution, but human judgment still has to decide: "Is this highlight actually interesting enough to develop?" Sometimes I select something, Claude drafts it perfectly, and I realize... the underlying insight just isn't that compelling.

### What you wouldn't automate again

**Selection is non-automatable:**
I tried having Claude pick the "most interesting" highlight. It couldn't. It would choose things that looked complete or well-formatted, not things that had genuine insight potential.

**Final edit is non-automatable:**
Even with 75% accuracy, that last 25% matters. It's where the real voice lives—the small choices that make something sound like me vs. "pretty good AI copy."

**Timing/relevance is non-automatable:**
Just because a highlight exists doesn't mean now is the right time to post about it. Context matters. What's happening in my industry? What have I posted recently? That judgment stays human.

---

## THE GOLDFLOW (Philosophical)

### What this workflow taught you about automation

**"AI doesn't replace taste—it amplifies throughput for people who have it."**

The workflow only works because I still make the creative decisions: What to highlight. Which highlight to develop. What the final edit should be. Claude handles the tedious middle—the drafting mechanics—so I can focus on taste.

People ask "will AI replace writers?" The better question is: "Which parts of writing are actually creative, and which are just execution?" This workflow helped me see the boundary more clearly.

### When does automation make sense?

Automation works when you can answer "yes" to all three:

1. **Can you clearly define "good"?** I can because I have 900 lines of voice rules. Most people can't articulate their own style—so AI just gives them generic output.

2. **Is there a feedback loop?** Every time I edit a Claude draft, I ask "why did I change this?" and update the fingerprint. The system learns.

3. **Does it handle the tedious parts, not the creative parts?** I keep selection and final edit. Claude handles scanning and first-draft mechanics.

### Principle this confirmed

**"Negative constraints are more powerful than positive examples."**

I spent months trying to teach Claude my voice by showing it examples. Marginal improvement.

Then I documented what I NEVER say—specific phrases, transitions, structures that feel wrong. Massive improvement.

The insight: AI is better at rule-following than pattern-matching. "Never use 'let's dive into'" is actionable. "Sound conversational" is vague.

---

## Additional Notes for Interview

### The backstory with the viral post

The LinkedIn post about "workslop" (AI-generated work content that shifts cognitive burden to readers) performed really well. What's interesting: that was one of the first posts where I systematically compared the Claude draft to my final version.

That comparison generated most of the "negative fingerprint" insights—I could see exactly what I was deleting and why. The meta-learning from one post improved all future posts.

### For their audience (content marketers)

The principles transfer even without Claude Code:

1. **Build a fingerprint:** Analyze your own writing. Document what you never say.
2. **Use the negative:** When prompting ChatGPT/Claude, include "Never use these phrases: [list]"
3. **Track your edits:** Every time you change AI output, ask why. Add it to your rules.
4. **Feedback loop matters more than perfect v1:** My first version was ~50% accurate. Now it's ~75%. That improvement came from systematic learning.

### The "X killed Y" connection

When people say "ChatGPT killed writing," they're missing the same thing as "Beautiful.ai killed Powerpoint."

The tool matters less than the workflow around it. A bad workflow with ChatGPT produces garbage. A good workflow with the same tool produces useful output. The differentiator is human judgment, systematic improvement, and clear definition of quality.

That's what the "X killed Y" takes always miss.
