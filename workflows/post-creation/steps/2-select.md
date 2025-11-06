# Step 2: Select 3 Most Recent Entries

## Purpose
Sort all found entries by file birth time and select the 3 most recent for presentation.

## Implementation

```python
import json
from pathlib import Path

# Load entries
with open('/tmp/logseq_socialpost_entries.json', 'r') as f:
    entries = json.load(f)

# Sort by birth_time (most recent first)
sorted_entries = sorted(entries, key=lambda x: x['birth_time'], reverse=True)

# Take top 3
top_3 = sorted_entries[:3]

# Save to new file
with open('/tmp/logseq_socialpost_top3.json', 'w') as f:
    json.dump(top_3, f, indent=2, ensure_ascii=False)

print(f"Selected 3 most recent entries from {len(entries)} total")
```

## Output

**File:** `/tmp/logseq_socialpost_top3.json`

Contains the 3 most recently created entries based on file birth time.

## Edge Cases

**Less than 3 entries:**
- If only 1-2 entries found, proceed with what's available
- Inform user of the count

**No entries found:**
- Report to user
- Suggest checking if [[socialpost]] tags exist in Logseq

## Success Criteria

- 3 (or fewer if unavailable) most recent entries selected
- Sorted by actual creation date (birth time, not modification time)
- Saved to temp file for next step
