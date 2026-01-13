# The Workflow Interview Prep Answers

> Tim Metz - Style Guide Reverser

---

## INTRO

### Who you are, what you do, where you spend 'get-shit-done' energy

I'm Director of Marketing & Innovation at Animalz, where I help B2B companies build content systems that actually work. Outside of that, I write the "We Eat Robots" newsletter about AI workflows for knowledge workers—basically documenting everything I learn about making AI useful for real work, not just demos.

Most of my energy right now goes into two things: helping Animalz clients build content strategies that survive the AI shift, and building my own AI-assisted workflows that I can actually use day-to-day. The style guide workflow we're talking about today came from that second bucket.

### Overhyped AI claim that made you roll your eyes

There's this format I see all the time: "X just killed Y" — when X just released some new, usually not-so-amazing feature. Like "Beautiful.ai just killed Powerpoint."

It's lazy hyperbole that makes everything sound revolutionary when most releases are incremental. A new feature doesn't kill anything. The installed base, the switching costs, the workflows people have built—none of that disappears because someone shipped a nice demo.

The worst part is it trains people to expect revolution when what actually works is evolution. My most useful AI workflows aren't revolutionary—they're boring. They just save me 20 minutes on something I do every day.

---

## THE WORKFLOW

### Introduce the workflow like it's a superhero

**Name:** The Style Guide Reverser

**Unique powers:**
- Extracts your actual editorial voice from published content (15-20 articles → 50+ specific rules)
- Reviews articles 4-5x faster than manual editing using 8 parallel agents
- Works with any brand—just feed it different source articles
- Creates enforcement that scales (the guide isn't just a document that sits unused)

**Why it's famous:**
This workflow turned weeks of style guide creation into hours. More importantly, it made style enforcement actually practical. Before this, style guides were documents that got created once and then ignored because checking against them was too tedious.

### What problem were you solving?

Two connected problems with style guides:

1. **They either don't exist or immediately get out of date.** Writing a comprehensive style guide manually takes weeks. Most brands skip it entirely, or create one that nobody maintains.

2. **They're hard to enforce consistently.** Even when you have a guide, checking a single article against 50+ rules takes 40+ minutes. At that pace, you skip it when deadlines are tight. Quality drifts.

### Measurable outcome you were aiming for

- **Generation:** Create usable style guide in 1-2 hours (vs weeks manually)
- **Review:** Check articles in 5-10 minutes (vs 40+ minutes)
- **Speedup:** 4-5x faster editorial review
- **Quality:** Consistent voice across all content

### What wasn't working before?

- Our Animalz style guide was outdated (embarrassing to admit)
- I'd sometimes skip copy-editing because deadlines were tight
- Different writers had different interpretations of "our voice"
- Reviewing a single article for style took forever
- Style guides existed but weren't enforced because enforcement didn't scale

### Step-by-step walkthrough

**Step 1: Install Claude Code**
One command in Terminal: `curl -fsSL https://claude.ai/install.sh | bash`
Then type `claude` to start and authenticate with your Claude account (one-time setup).

**Step 2: Collect Source Articles**
Gather 15-20 representative published articles. Claude Code can scrape directly from a blog URL, or you can use local markdown files. This is your "corpus" of what good looks like.

**Step 3: Run Style Guide Generator**
Single command: `/generate-style-guide [brand-name] [source]`
Claude analyzes patterns across 8 editorial dimensions and extracts 50+ specific rules with DO/DON'T examples.

**Step 4: Review Generated Guide**
Human reviews the AI-extracted patterns. This is where you catch any misidentified patterns or add context the AI couldn't infer. Takes 30-60 minutes.

**Step 5: Run Style Check on New Article**
Command: `/style-check [brand-name] [article-path]`
This is where the magic happens—8 specialized agents run in parallel, each reviewing against one section of the style guide.

**Step 6: Review Violations Report**
Get a detailed report with:
- Line numbers (exact location)
- Issue description
- Current text (exact quote)
- Suggested correction
- Rule being violated

Takes 5-10 minutes to review vs 40+ minutes for manual checking.

**Step 7: Apply Corrections**
Fix issues manually or use `--auto-apply` flag for automatic fixes. Your choice based on comfort level.

### Tools at each step

| Step | Tool | Why this one |
|------|------|--------------|
| Collect | Claude Code / manual | Scraping saves copy-paste work |
| Generate | Claude Code + generator agent | Large context window handles all articles |
| Review Guide | Human | Judgment call on extracted rules |
| Style Check | 8 parallel agents | Simultaneous = fast |
| Report | Claude Code | Compiles all agent findings |
| Apply | Manual or auto | User choice |

### The 8 Parallel Agents (The Secret Sauce)

| # | Agent | Focus | Example Catch |
|---|-------|-------|---------------|
| 1 | Voice & Tone | Passive voice, pronoun consistency | "The article was written" → "We wrote" |
| 2 | Grammar & Usage | Oxford commas, Title Case | Missing comma in list |
| 3 | Punctuation | Em dashes, list punctuation | Wrong em dash spacing |
| 4 | Formatting | Headings, hyperlinks | H3 should be H2 |
| 5 | Technical Standards | Dates, numbers | "5%" → "5 percent" |
| 6 | Content Patterns | CTAs, openings | Missing call-to-action |
| 7 | Industry Terms | Acronyms, terminology | Undefined "CMS" |
| 8 | Quick Reference | Cross-check | Final sanity check |

**Why parallel matters:** 8 agents simultaneously = 5-10 min. Sequential = 40+ min.

### Manual vs automated

**Manual (requires human judgment):**
- Reviewing the generated style guide
- Final editorial decisions on corrections
- Deciding which violations matter vs which to ignore

**Automated:**
- Article collection (scraping)
- Pattern extraction
- Style checking (8 agents)
- Report generation
- Auto-apply (optional)

### Results

- **Animalz style guide:** 757 lines, 50+ rules, comprehensive
- **Review time:** 5-10 minutes per article (down from 40+)
- **First real use:** Caught issues I would have missed manually
- **Scalable:** Same effort whether reviewing 1 article or 100

### Surprises (good and chaotic)

**Good surprise:**
The parallel agent approach was shockingly fast. I expected some speedup, but 4-5x was better than I'd hoped. And because each agent is specialized, they catch more issues than a single "check everything" prompt.

**Another good surprise:**
AI extracted patterns I wasn't consciously aware of. Looking at our actual articles revealed conventions we followed but had never documented.

**Chaotic discovery:**
First version over-extracted patterns. Too many rules made the guide unwieldy. Had to tune for patterns with 95%+ consistency (rules) vs 70-95% (preferences) vs one-offs (ignore).

**Limitation:**
Still needs human review—AI catches mechanical issues, not strategic ones. "Is this the right CTA for this audience?" requires judgment the AI doesn't have.

### What you wouldn't automate again

**Style guide review is non-automatable:**
The AI extracts patterns, but a human needs to verify: "Yes, this is actually a rule we want, not just a coincidence in our sample."

**Final editorial judgment is non-automatable:**
The report tells you what violates the rules. But sometimes you break rules intentionally. That decision stays human.

**Strategic content decisions are non-automatable:**
"Should we write about this topic?" "Is this the right angle?" The workflow handles execution quality, not content strategy.

---

## THE GOLDFLOW (Philosophical)

### What this workflow taught you about automation

**"AI is better at extracting patterns than we are at articulating them."**

I spent years trying to describe our brand voice. Struggling to write down rules that captured what made Animalz content sound like Animalz. The AI just looked at the articles and found the patterns.

This reversed my mental model. Instead of "write rules, then enforce," it's "create examples, extract rules, then enforce." Much more practical.

### When does automation make sense?

Automation works when you can answer "yes" to all three:

1. **Do you have examples of "good"?** The published articles serve as ground truth. No examples = no patterns to extract.

2. **Is the task decomposable?** Editorial review breaks into 8 distinct dimensions. Each can be evaluated independently.

3. **Does speed matter?** If you're reviewing one article per month, manual is fine. If you're reviewing dozens, the 4-5x speedup matters.

### Principle this confirmed

**"Parallel is the unlock."**

A single AI reviewing for everything is slow and misses issues. 8 specialized agents—each an expert in one domain—catch more issues faster.

This mirrors how professional editorial teams work. You don't have one editor checking everything. You have specialists. The workflow just lets you deploy 8 specialists simultaneously.

---

## Additional Notes for Interview

### The backstory with Animalz

We're a content marketing agency that preaches content quality. Our own style guide being outdated was... embarrassing. This workflow fixed that in hours instead of the weeks it would have taken manually.

Now we're exploring using it for client style guides too—reverse-engineer their existing content into enforceable standards.

### For their audience (content marketers)

The principles transfer even without Claude Code:

1. **Collect examples:** Gather 15-20 of your best articles
2. **Use the generation prompt:** Feed them to ChatGPT with the extraction prompt
3. **Review section by section:** Check articles against one style guide section at a time
4. **Track what you change:** Every correction improves the guide

The workflow is slower without Claude Code (40+ min vs 5-10 min), but it works.

### The "X killed Y" connection

When people say "AI killed editing," they're missing the point.

AI handles the mechanical parts—catching inconsistent commas, wrong date formats, missing Oxford commas. Humans handle the strategic parts—is this on-brand, is this the right angle, does this serve the reader.

The tool matters less than understanding which parts to automate. That's what the "X killed Y" takes always miss.

---

## Profile/Bio Info

**Tim Metz**
- Director of Marketing & Innovation at Animalz
- Author of "We Eat Robots" newsletter
- LinkedIn: https://www.linkedin.com/in/metztim
- Focus: AI workflows for knowledge work
