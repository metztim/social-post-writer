# Step 3: Present Options to User

## Purpose
Display the 3 selected entries with full context so the user can choose which to draft into a post.

## Implementation

For each entry, show:
1. **Option number** (1, 2, 3)
2. **Source file** (readable name)
3. **Age** (days since creation)
4. **Tags** (all tags from the entry)
5. **The [[socialpost]] block** (the specific highlight marked for social)
6. **Additional context** (other highlights from same source page)

## Format Example

```markdown
### Option 1: Article Title

**Source:** Article Title (highlights)
**Age:** ~2 days old (created Nov 4, 2025)
**Tags:** #socialpost #topic #.3

**The [[socialpost]] Block:**
> Quote or content marked for social post
>
> **Note**: Any existing notes

**Additional Context from Same Article:**
- Related highlight 1
- Related highlight 2
- Related highlight 3
```

## Presentation Rules

**Show full content (never truncate):**
- Display complete highlights
- Include all context from source page
- Don't summarize or shorten

**Group by source:**
- If multiple entries from same file, note it
- Helps user see thematic options

**Be clear about selection:**
- Number each option clearly
- Make it easy to say "Option 2"

## Success Criteria

- All 3 options clearly presented
- Full context provided for each
- User can easily select which to draft
- No information lost or truncated
