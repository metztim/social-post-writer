# Writing Assistant Project

## Commands

### `/write` — Structured writing process
8-phase process for thought leadership articles: Foundation → Thesis → Structure → Research → 30% Outline → Introduction → Drafting → Review. Claude acts as strict editor enforcing discipline, not as AI shortcut. See `.claude/commands/write.md`.

### `/write-rescue` — Mid-process entry
Diagnoses an existing draft, maps it against the 8 phases, identifies gaps, and creates a state file so `/write` can take over.

### `/write-status` — Quick status check
Reports where an article is in the process and what's next.

### `/draft-linkedin-post` — LinkedIn post workflow
Separate workflow for LinkedIn posts. See `workflows/post-creation/`.

### `/research-article` — Article research
Standalone research agent for article drafts. See `.claude/subagents/article-researcher.md`.

## Article folder convention

Each article lives in `projects/articles/{slug}/`:
```
projects/articles/{slug}/
  state.md              # Process state (YAML frontmatter + process log)
  thesis.md             # Thesis, earned secret, antithesis
  outline-10.md         # Headers only (10% outline)
  outline-30.md         # Supporting points (30% outline)
  research/             # Research findings
  introduction.md       # Hook, sinker, line
  draft.md              # Full draft
  review-notes.md       # Editor review findings
```

## External data sources

### Logseq Knowledge Base
- **Path**: `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`
- **Format**: Markdown files organized by Logseq graph structure
- **Usage**: Reference for research, notes, and knowledge retrieval

To read Logseq pages, look in:
- `pages/` — Main pages
- `journals/` — Daily journal entries (format: `YYYY_MM_DD.md`)

## People

- **Tim Metz** — Director of Marketing & Innovation at Animalz. Author, primary user.
