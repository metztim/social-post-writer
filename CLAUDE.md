# Writing Assistant Project

> Unified craft workspace for all content writing. Articles, LinkedIn posts, copy projects, and voice system live here. Pipeline tracking lives in Notion (MyContent for personal, Content Calendar for Animalz).

## Content strategy

See `CONTENT_STRATEGY.md` for topic pillars, publication routing rules, quality bar, and exclusions. Referenced by `/write` Phase 1 (Foundation) and the global `/content` command.

### Notion integration

- **MyContent** (`131edc77-7df2-80be-a79e-edc6e0955fc2`, personal) — personal pipeline tracker
- **Content Calendar** (`249df6dc-2cc5-81bc-8944-f44570c7cdce`, work) — Animalz pipeline tracker
- When starting a `/write` session, ensure the piece has a corresponding Notion entry
- Rich context goes in Notion **page body** (`notion append-blocks`), not properties

## Commands

### `/write` — Structured writing process
8-phase process for thought leadership articles: Foundation → Thesis → Structure → Research → 30% Outline → Introduction → Drafting → Review. Claude acts as strict editor enforcing discipline, not as AI shortcut. See `.claude/commands/write.md`.

### `/write-rescue` — Mid-process entry
Diagnoses an existing draft, maps it against the 8 phases, identifies gaps, and creates a state file so `/write` can take over.

### `/write-status` — Quick status check
Reports where an article is in the process and what's next.

### `/draft-linkedin-post` — LinkedIn post workflow
Separate workflow for LinkedIn posts. See `workflows/post-creation/`.

### `/copywrite` — Structured copywriting process
7-phase process for short-form conversion copy (landing pages, ads, emails, taglines): Brief → Strategy → Research → Exploration → Selection → Full Copy → Review. Grounded in Harry Dry's three laws, Sullivan's advertising principles, and Wiebe's Money Words. Claude coaches and tests quality — human generates the ideas and writes the variants. See `.claude/commands/copywrite.md`.

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

## Copy project folder convention

Each copy project lives in `projects/copy/{slug}/`:
```
projects/copy/{slug}/
  state.md              # Process state (YAML frontmatter + process log)
  brief.md              # Deliverable, audience, attitude shift, constraints
  strategy.md           # Core truth, positioning, SOCO/SOCA
  research/             # Competitive copy, VOC, references
  variants.md           # All variants with three-laws scoring
  copy.md               # Final copy
  review-notes.md       # Review findings
```

## External data sources

### Logseq Knowledge Base
- **Path**: `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq`
- **Format**: Markdown files organized by Logseq graph structure
- **Usage**: Reference for research, notes, and knowledge retrieval

To read Logseq pages, look in:
- `pages/` — Main pages
- `journals/` — Daily journal entries (format: `YYYY_MM_DD.md`)

### Animalz Knowledge Base (Notion)

Writing advice, style guides, and content strategy docs from the Animalz team. Query with the Notion CLI:

```bash
# Browse by category
notion query "Knowledge Base" --filter '{"property": "Category", "select": {"equals": "CATEGORY"}}' -w work

# Read a specific article
notion get-blocks <page_id> -w work
```

| Writing need | Category filter |
|---|---|
| Style, voice, craft | Writing Fundamentals |
| Editing standards, copyediting | Editing & Quality |
| SEO, optimization, AEO | SEO & Optimization |
| Topic ideation, research process | Research & Ideation |
| Long-form article structure | Long-form content |
| Email and newsletter copy | Email & Newsletters |
| LinkedIn content | LI Content |
| AI writing tools and red flags | AI Resources |

Additional useful filters:
- `Document type`: "Guides & Best-Practices", "How-To", "Policies / Standards"
- `Audience`: "Staff", "Freelancer"
- `Status`: "Active" for current docs

## People

- **Tim Metz** — Director of Marketing & Innovation at Animalz. Author, primary user.
