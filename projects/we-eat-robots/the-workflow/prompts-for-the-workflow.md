# Prompts for The Workflow

> Social Post Creator from Highlights - Tim Metz

These prompts power the "Highlight-to-Post Pipeline" workflow that turns reading highlights into authentic LinkedIn posts.

---

## Prompt 1: Content Scanner

**Purpose:** Find tagged highlights ready to be developed into posts

**How it works:**
This Python script scans a Logseq knowledge base for blocks tagged with `[[socialpost]]` and extracts their full context, including multi-paragraph highlights.

```python
# Simplified version of the scanning logic

def find_socialpost_entries(notes_directory):
    """
    Scan notes for entries tagged [[socialpost]]
    Returns list of entries with full context
    """
    entries = []

    for file in notes_directory.glob('**/*.md'):
        content = file.read_text()

        # Find lines with [[socialpost]] tag
        for line_num, line in enumerate(content.split('\n')):
            if '[[socialpost]]' in line:
                # Extract the full block context (the highlight + surrounding text)
                context = extract_block_context(content, line_num)

                entries.append({
                    'file': file.name,
                    'context': context,
                    'tags': extract_tags(line),
                    'created': file.stat().st_birthtime
                })

    # Sort by creation time, newest first
    return sorted(entries, key=lambda x: x['created'], reverse=True)
```

**Non-Claude-Code version:**
If you're using ChatGPT or Claude web interface:
1. Keep a running list of highlights in any notes app
2. Tag them with something like "READY FOR POST"
3. When ready to write, copy 2-3 tagged highlights into your chat

---

## Prompt 2: Voice-Guided Drafting

**Purpose:** Create a LinkedIn post draft that sounds authentically like you, not generic AI

**The secret sauce:** Define what you NEVER say, not just what you do say

### The Drafting Instructions

```markdown
# Create LinkedIn Post Draft

You have access to:
1. The highlight/insight I want to develop (provided below)
2. My voice fingerprint (what I DO and DON'T say)
3. Sample posts that performed well

## Your Task

Draft a LinkedIn post from this highlight that sounds authentically like me.

## Critical Voice Rules

### What I NEVER Say (Delete These Automatically)
- "Let's dive into..." / "Let's explore..."
- "The real problem is..." / "The key is..."
- "Here's the thing:" / "Here's what I mean:"
- "At the end of the day" / "The bottom line is"
- "In today's world" / "In the age of AI"
- "There's a name for this now" (meta-commentary)
- "Turns out [statement]" (AI transition phrase)
- "Furthermore," "Moreover," "Additionally" (too formal)
- Rhetorical questions mid-post ("Isn't it interesting that...")
- "colleague" (I say "coworker")
- "content" in professional contexts (I say "materials")

### What I Actually Do
- Open with recognition scenario ("You think you're..." or "You open a...")
- Use em-dashes liberally for breathing room
- Use radical sentence length variation (long + short for emphasis)
- Trust white space - don't over-explain connections
- Add parenthetical asides for self-awareness: "(Deadly sin, I know.)"
- Use simple conjunctions: "So," "And," "But" (conversational)
- End with genuine question (not rhetorical)
- Include source attribution: "researchers from [Org Name]" + "(Full article in comments.)"

### Structure
- Hook (concrete, specific - not abstract)
- Context (brief backstory)
- Insight or observation
- Application or implication
- Question to engage (single, direct)

### Rhythm
- Short paragraphs (1-3 sentences)
- Line breaks between each thought
- Staccato sentences for emotional buildup:
  "The content is vague.
   Key details are missing.
   You're not sure what to do with this."

## The Highlight to Develop

[INSERT YOUR TAGGED HIGHLIGHT HERE]

## Output

Draft a post (150-250 words) that:
1. Develops this insight in my authentic voice
2. Avoids all "never say" phrases
3. Includes my characteristic rhythm (em-dashes, white space)
4. Ends with a genuine question
```

---

## Prompt 3: Voice Fingerprint (The "Never Say" List)

**Purpose:** The negative fingerprint that catches AI-isms before they reach your audience

This is the most powerful part of the system. Instead of just telling AI what TO do (which it often interprets loosely), we specify what NEVER to include.

### Tim's "Never Say" List (Excerpt)

```markdown
# Phrases I Never Use

## AI-Generated Patterns (Delete on Sight)
1. "Let's dive into..." / "Let's explore..."
2. "Here's the thing:" / "Here's what I mean:"
3. "At the end of the day" / "The bottom line is"
4. "It's not about X, it's about Y" (false dichotomy)
5. "Isn't it...?" / "Don't you...?" (rhetorical questions)
6. "In today's world" / "In the age of AI"
7. "There's a name for this now"
8. "Turns out [statement]"
9. "My question for today:" (question framing)

## Transitions I Avoid
- "Furthermore," "Moreover," "Additionally"
- "Therefore," "Thus," "Consequently"
- "To put it another way," "In other words"
- "Not only X, but also Y"

## LinkedIn-Speak I Skip
- "Thrilled to announce..."
- "Excited to share..."
- "Game-changer" / "Revolutionary"
- "Best practices" as main topic
- Generic enthusiasm without substance

## Sentence Structures I Delete
- "It is important to note that..."
- "I would argue that..."
- "One might consider..."
- Hedging clusters ("arguably," "perhaps one could say")
- Accusatory you/I framing ("You did X, I suffer Y")
```

### How to Build Your Own Fingerprint

1. **Collect 5-10 of your best posts** (highest engagement)
2. **Analyze what you DON'T do:**
   - What transitions do you never use?
   - What phrases feel "off" when AI suggests them?
   - What opening patterns do you avoid?
3. **Document it explicitly** - AI follows negative rules more reliably
4. **Update after each edit session** - track what you change in AI drafts

---

## Prompt 4: Self-Validation Checklist

**Purpose:** Verify the draft sounds authentic before saving

```markdown
# Voice Authenticity Checklist

Before accepting this draft, verify:

## Red Flags (If Present, Revise)
- [ ] Contains any "never say" phrases
- [ ] Uses formal transitions (Furthermore, Moreover)
- [ ] Has rhetorical questions mid-post
- [ ] Missing em-dashes (should have 2-3)
- [ ] Over-explains connections between paragraphs
- [ ] Uses "colleague" instead of "coworker"
- [ ] Contains meta-commentary ("There's a name for this")
- [ ] Stats crammed in paragraphs (should be bullets)
- [ ] Vague source attribution ("studies show")

## Must-Haves (If Missing, Add)
- [ ] Opens with concrete specificity
- [ ] Has parenthetical aside(s)
- [ ] Uses line breaks for rhythm
- [ ] Ends with genuine question
- [ ] Includes source link reference

## Final Test
Read it out loud. Does it sound like something I would actually say?
If not, identify what feels "off" and revise.
```

---

## The Simplified Version (For ChatGPT/Claude Users)

If you don't use Claude Code, here's the pattern:

### Step 1: Tag Your Highlights
Keep interesting quotes/insights in any notes app. Mark the best ones "READY."

### Step 2: Create Your Fingerprint
Analyze 5-10 of your posts. Document:
- What phrases feel wrong when AI suggests them
- Your natural transitions
- Your characteristic rhythm

### Step 3: Use This Template
```
I want to turn this highlight into a LinkedIn post:

[PASTE HIGHLIGHT]

Write in my voice. Here's what I NEVER say:
- [Your "never say" list]

Here's what I DO:
- [Your characteristic patterns]

Draft a 150-250 word post that sounds authentically like me.
```

### Step 4: Track Your Edits
Every time you change an AI draft, ask: "Why did I change this?"
Add that pattern to your fingerprint for next time.

---

## Key Insight

The "negative fingerprint" approach (documenting what you NEVER say) is more effective than positive examples. AI is better at avoiding specific patterns than matching vague concepts like "conversational tone."

When I analyzed my editing patterns, I found I was deleting the same AI-generated phrases over and over:
- Meta-commentary ("There's a name for this now")
- Accusatory framing ("You did X, I suffer Y")
- Editorial flourishes that over-explain
- Question framing ("My question for today:")

Documenting these as explicit rules improved draft accuracy from ~50% to ~75% unchanged after editing.
