# Step 6: Mark Entry as Used

## Purpose
Update the source Logseq entry to prevent reuse in future workflow runs.

## Why This Matters

**Prevention beats detection:**
- Removing [[socialpost]] tag = entry won't appear in future scans
- Adding note = preserves history of where it was used
- Single source of truth in Logseq

**Alternative approach (worse):**
- Query Notion database each time = slow, complex
- Check for duplicates during selection = easy to miss
- This approach is simpler and more reliable

## Implementation

### Step 6.1: Remove [[socialpost]] Tag

Find the line in the Logseq file and remove the [[socialpost]] tag:

**Before:**
```markdown
- **Tags**: #[[socialpost]] #[[topic]] #[[.3]]
```

**After:**
```markdown
- **Tags**: #[[topic]] #[[.3]]
```

### Step 6.2: Add Note with Link

Add a child note with link to the Notion post:

**After:**
```markdown
- **Tags**: #[[topic]] #[[.3]]
  - **Note**: Used in [Post Title](https://notion.so/page-id)
```

## File Handling

**Use Python (NOT bash):**
```python
from pathlib import Path
import glob

# Get file path from entry data
file_path = entry['absolute_path']

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the specific line
old_line = entry['line']  # Original line with [[socialpost]]
new_line = old_line.replace('#[[socialpost]]', '').replace('  #', ' #')
note_line = f"\t\t- **Note**: Used in [Post Title](https://notion.so/page-id)"

# Replace and add note
content = content.replace(
    old_line,
    new_line + '\n' + note_line
)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
```

## Important Notes

**Indentation matters:**
- Match Logseq's indentation (tabs, not spaces)
- Note should be child of Tags line

**Multiple tags:**
- Clean up double spaces after removing [[socialpost]]
- Preserve other tags exactly as they were

**Link format:**
- Use Notion page URL from Step 5
- Use descriptive title (not just "Post")

## Success Criteria

- [[socialpost]] tag removed from entry
- Note added with link to Notion post
- File saved successfully
- Entry won't appear in future scans
- History preserved for reference
