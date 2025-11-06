# Step 1: Scan Logseq for [[socialpost]] Entries

## Purpose
Search for all blocks tagged with [[socialpost]] in your Logseq database and save them to a JSON file.

## Implementation

**Use the dedicated Python script:**
```bash
cd /Users/timmetz/Library/CloudStorage/Dropbox/Logseq
python3 /path/to/workflows/post-creation/scripts/scan_socialpost.py
```

**The script will:**
- Scan both `pages/` and `journals/` directories
- Extract full block context (including multi-paragraph highlights)
- Capture file birth time for age-based sorting
- Save results to `/tmp/logseq_socialpost_entries.json`

## Critical Rules

**ALWAYS use Python (NOT bash commands):**
- Logseq files contain special characters (URL encoding, curly quotes)
- Python's glob handles these gracefully
- Bash find/grep/ls will fail on special characters

**Use file birth time (NOT modification time):**
- Logseq sync operations modify file mtimes
- Birth time provides accurate age-based selection

## Output

**File:** `/tmp/logseq_socialpost_entries.json`

**Format:**
```json
[
  {
    "file": "pages/Article Title (highlights).md",
    "line_num": 14,
    "line": "- **Tags**: #[[socialpost]] #[[topic]] #[[.3]]",
    "context": "Full block with multi-line content...",
    "tags": ["socialpost", "topic", ".3"],
    "filename": "Article Title (highlights).md",
    "parent_line": "First line of content...",
    "birth_time": 1762239448.865329,
    "absolute_path": "/full/path/to/file.md"
  }
]
```

## Error Handling

**If file not found:**
- Use glob pattern matching (handles special characters)

**If encoding error:**
- Skip file and log error
- Continue with other files

**If no entries found:**
- Check if [[socialpost]] tag exists in Logseq
- Verify Logseq path is correct

**Common issues:**
- Curly quotes in filenames (use glob, not string paths)
- URL-encoded characters (%3A for :, %20 for spaces)
- UTF-8 encoding (must specify explicitly)

## Success Criteria

- JSON file created at `/tmp/logseq_socialpost_entries.json`
- All [[socialpost]] entries captured
- No false positives (entries already marked as used should have tag removed)
- Report shows count of entries found
