# Writing Assistant

Tools and workflows for content creation — articles, LinkedIn posts, and podcast prep.

---

## Workflows

### `/write` — Structured article writing (primary)

8-phase process for thought leadership articles: Foundation, Thesis, Structure, Research, 30% Outline, Introduction, Drafting, Review. Claude acts as strict editor enforcing discipline at each phase.

```bash
/write
```

Related commands:
- `/write-rescue` — Pick up a broken or in-progress draft mid-process
- `/write-status` — Quick check on where an article stands

Articles live in `projects/articles/{slug}/` with a standard file structure (state.md, thesis.md, outlines, research/, draft.md, review-notes.md).

### `/draft-linkedin-post` — LinkedIn post drafting

Scans Logseq for `[[socialpost]]` entries, drafts using Tim's voice guides, saves to Notion MyContent.

```bash
/draft-linkedin-post
```

Detailed workflow: `workflows/post-creation/draft-linkedin-post-v2.md`

---

## Project structure

```
.claude/
  commands/              # Slash commands (/write, /write-rescue, /write-status, /draft-linkedin-post)
  subagents/             # Writing-researcher, writing-editor agents

projects/
  articles/              # Article drafts (per /write process)
  linkedin-posts/        # LinkedIn post drafts
  we-eat-robots/         # Podcast prep materials

voice/
  tim-linkedin-voice-v2.md          # Voice guide
  tim-linguistic-fingerprint-v2.md  # Linguistic analysis
  archive/                          # Previous versions

samples/tim/             # Reference LinkedIn posts (7 published + drafts)

workflows/
  post-creation/         # LinkedIn post workflow (v2) with scripts and steps
  voice-refinement.md    # Monthly voice learning loop
  archive/               # Previous workflow versions

analysis/                # Post analysis and editing pattern research
docs/                    # Session log, agent guidelines, tasks, interviews
```

---

## Voice system

Voice guides capture how Tim actually writes — not how he "should" write. Built from forensic analysis of published posts, refined through edit pattern analysis.

- **Voice guide:** `voice/tim-linkedin-voice-v2.md`
- **Linguistic fingerprint:** `voice/tim-linguistic-fingerprint-v2.md`
- **Refinement process:** `workflows/voice-refinement.md`

---

## External integrations

- **Logseq:** `/Users/timmetz/Library/CloudStorage/Dropbox/Logseq` — source material, `[[socialpost]]` entries
- **Notion MyContent:** Database `131edc77-7df2-80be-a79e-edc6e0955fc2` — draft storage, engagement metrics
