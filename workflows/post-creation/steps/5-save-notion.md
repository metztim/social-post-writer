# Step 5: Save Draft to Notion

## Purpose
Create or update a page in the MyContent database with the draft post.

## Notion Database

**Database ID:** `131edc77-7df2-80be-a79e-edc6e0955fc2`

## Implementation

### Create New Page

```python
# Use mcp__notion-personal__API-post-page
```

**Required properties:**
- **Title**: Descriptive title for the post
- **Type**: Set to "LinkedIn post"
- **Status**: Set to "In progress"
- **Claude Draft**: The full draft text

### OR Update Existing Page

If user specifies an existing page to update:

```python
# Use mcp__notion-personal__API-patch-page
```

**Update:**
- **Claude Draft** property with new text
- **Status** to "In progress" if not already

## Draft Format

**The Claude Draft property should contain:**
- Complete post text
- Proper formatting (line breaks, etc.)
- Ready to copy/paste to LinkedIn

**Do NOT include:**
- Meta-commentary about the draft
- Instructions or notes
- Source attribution (unless part of post)

## Report Back

Provide user with:
1. **Link to Notion page**
2. **Draft preview** (first 100 chars)
3. **Note on voice patterns applied**

Example:
```
✓ Saved to Notion: [Post Title](https://notion.so/...)

Draft preview:
"Your carefully crafted editorial style guide won't travel to ChatGPT or Gemini..."

Voice patterns applied:
- Direct, concrete opening
- Short paragraphs with white space
- No meta-commentary
```

## Success Criteria

- Draft saved to Notion MyContent database
- All required properties set
- User has link to review/edit
- Draft is ready for user refinement
