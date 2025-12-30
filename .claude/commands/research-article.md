---
description: Research supporting material from knowledge base for article draft
tags: [writing, research, articles]
---

You are helping research an article draft by finding relevant highlights, quotes, data, and insights from the user's personal knowledge base.

## Parameters

**Required:**
- **DRAFT_PATH**: {{arg1}} - Path to the article draft to research

**Optional:**
- **LOGSEQ_PATH**: {{arg2}} - Path to Logseq library (defaults to `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`)
- **KEYWORDS**: {{arg3}} - Comma-separated keywords to focus research on (optional)

## Your Task

Invoke the **article-researcher** agent to conduct comprehensive research with these objectives:

### 1. Claims Needing Validation
Identify unsupported claims in the draft and find credible sources to back them up.

### 2. Similar Arguments from Credible Sources
Find other respected authors or experts making the same points. These become linkable citations.

### 3. New Insights & Alternative Angles
Discover perspectives or ways of thinking about the topic that might enrich the article.

### 4. Contrary Views
Find well-reasoned counterarguments worth acknowledging or addressing.

### 5. Practical Examples & Case Studies
Locate real-world examples that illustrate the article's points.

### 6. Supporting Data & Research
Find relevant statistics, research findings, and empirical data.

## Research Process

The agent should:

1. **Read the draft** at DRAFT_PATH to understand:
   - Main thesis and arguments
   - Unsupported claims
   - Core themes and concepts
   - Intended audience and tone

2. **Search the knowledge base** at LOGSEQ_PATH using multiple strategies:
   - Direct keyword search from draft
   - Conceptual/thematic search (related but not identical terms)
   - Author and source name search
   - Tag-based search if applicable
   - If KEYWORDS provided, prioritize those themes

3. **Analyze findings** for each of the 6 research objectives:
   - Read full highlights/notes
   - Evaluate relevance and credibility
   - Extract specific quotes and data
   - Note source citations with locations
   - Determine where in draft each strengthens the argument

4. **Create research findings document** with:
   - Clear sections for each research objective
   - Specific quotes with full citations
   - Suggested placement in the draft
   - Explanation of why each addition strengthens the article
   - Prioritization of strongest additions
   - Full bibliography of sources consulted

## Output

Save the research findings as:
- **Filename**: `research-findings-logseq.md` (or `research-findings-[source].md` if using different knowledge base)
- **Location**: Same directory as the draft
- **Format**: Comprehensive markdown document following the structure defined in the article-researcher agent

The output should be:
- **Comprehensive** - Cover all 6 research objectives thoroughly
- **Actionable** - Provide specific integration recommendations
- **Prioritized** - Highlight the strongest additions clearly
- **Well-cited** - Include full source references with locations
- **Organized** - Structure findings logically for easy review

## Important Notes

- This is about **discovery and validation**, not just reinforcement
- Search broadly but curate carefully - quality over quantity
- Always explain WHY each addition strengthens the article
- Be honest about gaps - if you can't validate a claim, say so
- Maintain the author's voice - suggest enhancements, don't rewrite
- If contrary evidence exists, surface it

The goal is to help the author think more deeply about their topic and ensure their article is well-supported, credible, and considers multiple perspectives.
