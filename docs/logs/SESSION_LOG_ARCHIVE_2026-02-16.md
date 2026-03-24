3. Test article-researcher agent output format

### Next Actions
- [ ] Archive or delete we-eat-robots-writing repository (all content imported)
- [ ] Test `/research-article` command on a draft article
- [ ] Continue work on ai-multitasking-trap article (research complete, draft integration pending)
- [ ] Consider creating README in projects/ explaining the structure

### Metrics
- Files moved: 10
- Files imported: 4 (article-researcher.md, research-article.md, 2 article files)
- Directories created: 4 (projects/, linkedin-posts/, articles/, we-eat-robots/)
- Git commits: 2 (pre-cleanup + restructure)

---

## Session Log: 2026-01-13

**Project**: writing-assistant
**Type**: [docs]

### Objectives
- Prepare materials for "The Workflow" podcast appearance (Jan 15th)
- Update Style Guide Creator workflow documentation
- Review and update Animalz Claude Code article

### Summary
Pivoted from Social Post Creator to Style Guide Creator workflow for The Workflow podcast—more universally applicable since it doesn't require a Second Brain/Logseq setup. Created comprehensive interview prep materials, prompts document with 8-agent appendix, workflow diagram spec, and screenshot instructions. Also reviewed the Animalz Claude Code article for updates (installation method, slash commands). Final corrections made based on actual plugin review: article count (5+ not 15-20), flexible source inputs, and --dry-run flag.

### Files Changed
- `projects/we-eat-robots/the-workflow/prompts-for-the-workflow.md` - Complete rewrite with Style Guide prompts + 8 agent appendix
- `projects/we-eat-robots/the-workflow/interview-prep-answers.md` - Updated for 7-step workflow, corrected article count
- `projects/we-eat-robots/the-workflow/workflow-diagram-spec.md` - 6-step visual flow, corrected article count, added --dry-run
- `projects/we-eat-robots/the-workflow/screenshot-instructions.md` - 6 screenshots for Style Guide workflow
- `projects/we-eat-robots/the-workflow/links-and-resources.md` - Updated bio and links

### Technical Notes
- **Plugin commands verified**: `/generate-style-guide`, `/style-check`, `/batch-review`, `/update-style-guide`, `/validate-style-guide`
- **Article minimum**: 5 articles minimum, 10-15 recommended (not 15-20 as originally documented)
- **Source flexibility**: Local files, URLs, blog URL with guidance, or any combination
- **Flags**: `--auto-apply` and `--dry-run` (dry-run takes precedence)
- **Installation simplified**: Native installer now recommended over npm (`curl -fsSL https://claude.ai/install.sh | bash`)
- **The Workflow format**: Written Substack newsletter, not audio podcast—interview is for research, output is written article

### Future Plans & Unimplemented Phases

#### Phase: Screenshots
**Status**: Not started
**Planned Steps**:
1. Capture source articles (folder or blog view)
2. Terminal running `/generate-style-guide` command
3. Generated style guide excerpt showing 8 sections
4. Terminal running `/style-check` with 8 agents visible
5. Violations report with line numbers
6. Before/after article comparison

#### Phase: Final Assembly
**Status**: Not started
**Planned Steps**:
1. Find toddler photo (Tim's task)
2. Upload all materials to The Workflow's Google Drive
3. Create workflow diagram in Miro (their preferred tool)

### Animalz Article Updates Discussed
- Installation: Update to native installer (one command, no Node.js required)
- Slash commands: Update list (remove /export, add /resume, /cost, /config)
- First test prompt: "analyze my desktop and downloads folders" works after typing `claude`
- Plugins section: Verified accurate for animalz/claude-plugins

### Next Actions
- [ ] Find toddler photo
- [ ] Capture 6 screenshots per screenshot-instructions.md
- [ ] Upload materials to Google Drive by Tuesday EOD
- [ ] Create visual diagram in Miro
- [ ] Update Animalz article with new installation method
- [ ] Update Animalz article slash commands section

### Metrics
- Files modified: 5
- Git commits: 2 (41555b9, f7518ed)
- Lines added: ~989
- Lines removed: ~510

---

## Session Log: 2026-01-14

**Project**: writing-assistant/projects/we-eat-robots/the-workflow
**Type**: [docs]

### Objectives
- Review and sort 27 screenshots for The Workflow podcast interview prep
- Select 10 best screenshots covering the full workflow
- Organize backups and rename files with descriptive names

### Summary
Reviewed all 27 screenshots captured for The Workflow podcast, categorized them by workflow stage (generate → style check → violations report), selected the 10 best that tell the complete story, moved 17 backup files to a new backup folder, and renamed the primary 10 with numbered descriptive names.

### Files Changed
- `screenshots/01-command-autocomplete.png` - Renamed from CleanShot 23.52.46
- `screenshots/02-source-selection-menu.png` - Renamed from CleanShot 23.53.11
- `screenshots/03-fetching-articles.png` - Renamed from CleanShot 23.55.21
- `screenshots/04-style-guide-generated.png` - Renamed from CleanShot 00.42.19
- `screenshots/05-style-guide-preview.png` - Renamed from CleanShot 00.42.39
- `screenshots/06-eight-agents-launching.png` - Renamed from CleanShot 00.49.37
- `screenshots/07-agents-completed.png` - Renamed from CleanShot 00.51.33
- `screenshots/08-violations-summary.png` - Renamed from CleanShot 00.52.47
- `screenshots/09-report-with-chart.png` - Renamed from CleanShot 00.53.57
- `screenshots/10-priority-recommendations.png` - Renamed from CleanShot 00.54.47
- `screenshots/backup/` - Created, contains 17 backup screenshots

### Technical Notes
- Screenshots cover 4 of 6 workflow stages from screenshot-instructions.md
- Missing: Source articles folder view, Before/after comparison
- User opted to proceed without capturing missing types
- Key visual (06-eight-agents-launching) shows all 8 parallel agents - the "money shot"

### Future Plans & Unimplemented Phases
None - task completed as requested.

### Next Actions
- [ ] Upload 10 primary screenshots to The Workflow Google Drive
- [ ] Consider capturing source articles folder view if needed later
- [ ] Consider capturing before/after comparison if needed later

### Metrics
- Files renamed: 10
- Files moved to backup: 17
- Directories created: 1 (screenshots/backup/)

---

## Session Log: 2026-01-27

**Project**: writing-assistant
**Type**: [feature]

### Objectives
- Sync LinkedIn posts to Notion MyContent database
- Extract engagement metrics (impressions, reactions, comments, reposts)
- Add full post content to page bodies

### Summary
Synced 20 LinkedIn posts to Notion: updated 11 existing posts with current engagement metrics and created 9 new posts with all properties. Used Chrome DevTools MCP for browser automation to extract post data from LinkedIn. Discovered and worked around a bug in the MCP post-page tool by using the direct Notion API script at `~/.claude/scripts/notion-api.py`. Session paused before adding body content to the 9 newly created pages.

### Files Changed
- `~/.claude/plans/shimmering-tinkering-bird.md` - Plan file for LinkedIn-to-Notion sync (updated with remaining task)

### Technical Notes
- **Chrome DevTools MCP**: Effective for browser automation with logged-in sessions (LinkedIn)
- **MCP post-page bug**: The parent parameter was being stringified instead of passed as object; workaround is using `~/.claude/scripts/notion-api.py` directly
- **Database ID confusion**: Notion's MCP returns `data_source_id` (b0bdaa81-c088-4ef7-b92b-75690666958c) but page creation requires actual `database_id` (131edc77-7df2-80be-a79e-edc6e0955fc2) from page parent responses
- **Notion text limit**: 2000 characters per text block; long posts need to be split into multiple paragraphs

### Plan File
- **Path**: `~/.claude/plans/shimmering-tinkering-bird.md`
- **Status**: In Progress
- **Phases Completed**: Post extraction, metrics update, page creation
- **Remaining**: Add body content to 9 newly created pages

### Future Plans & Unimplemented Phases

#### Add Post Body Content
**Status**: Not started
**Planned Steps**:
1. Query Notion database for LinkedIn posts: `python3 ~/.claude/scripts/notion-api.py personal query-database 131edc77-7df2-80be-a79e-edc6e0955fc2 '{"property": "Type", "multi_select": {"contains": "LinkedIn post"}}'`
2. Check which pages have empty bodies using `get-blocks`
3. Use Chrome DevTools MCP to navigate to LinkedIn and extract full post text via JavaScript evaluation
4. For each page needing content, use `append-blocks` to add paragraphs (split at 2000 chars)
5. Verify content added via Notion UI

### Next Actions
- [ ] Add body content to 9 newly created LinkedIn posts in Notion
- [ ] Verify all 20 posts have complete data in Notion

### Metrics
- Notion pages updated: 11
- Notion pages created: 9
- Total posts synced: 20

---

## Session Log: 2026-01-30

**Project**: writing-assistant
**Type**: [content] [creative]

### Objectives
- Decide whether to add an image to LinkedIn post about ActiveCampaign interview
- Explore creative approaches to the post

### Summary
Started with a practical question about LinkedIn post images, evolved into creative reimagining of the post "as the Buddha would write it." This produced a standalone koan about AI and clarity that will be published on both LinkedIn and We Eat Robots Substack. Refined the piece through multiple iterations, ultimately choosing radical minimalism: no image, no subtitle, just "A Koan" as the title.

### Files Changed
- No files modified in repository (content created for external platforms)

### Technical Notes
- **The koan created**:
  ```
  The student asked: "How do I use AI without creating noise?"
  The teacher said: "First, know what you want to say. The tool cannot find clarity you do not possess."
  The student asked: "But what if the tool writes faster than I can think?"
  The teacher said: "Then you have only accelerated your confusion."
  ```
- Echoes the classic Buddhist parable about the businessman who doesn't have time to meditate
- For LinkedIn: Post as "A koan" with no framing, no image
- For Substack: Title "A Koan", no subtitle, no image, SEO description uses the opening question
- URL slug changed from `a-koan` to `ai-koan` for discoverability

### Key Decisions
1. **Image decision**: For LinkedIn, the article header screenshot (active campaign 2.png) would work, but for the koan-only version, no image is better
2. **No attribution**: Decided against crediting Claude or linking to the original ActiveCampaign article - would undercut the minimalism
3. **"Content age" vs "AI content age"**: Kept broader framing, then dropped it entirely to just "A koan"
4. **Substack SEO**: Keep `ai-koan` as slug for discoverability (infrastructure doesn't affect reader experience)

### Next Actions
- [ ] Publish koan on We Eat Robots Substack
- [ ] Post koan version on LinkedIn
- [ ] Consider follow-up post showing before/after unslop comparison (using unslop-sideview.png)

### Metrics
- Files modified: 0
- Creative output: 1 koan for dual-platform publishing

---

## Session Log: 2026-02-16

**Project**: writing-assistant
**Type**: [feature] [refactor]

### Objectives
- Design and build a structured writing process tool (`/write`) for thought leadership articles
- Research the Animalz writing methodology from published articles, Logseq knowledge base, and internal resources
- Reorganize the writing-assistant project around this new primary workflow
