# Social Post Writer - Session Log

---

## 2025-10-21 - Initial Project Creation

**Session type:** Project setup & initial voice analysis

### What We Built

1. **Analyzed Tim's LinkedIn voice**
   - Studied 7 high-performing posts from MyContent
   - Extracted linguistic fingerprint (not generic patterns)
   - Identified what Tim NEVER says (AI-isms to avoid)
   - Documented actual recurring phrases and transitions

2. **Created voice guides**
   - `voice/tim-linkedin-voice-v1.md` - Comprehensive voice patterns
   - `voice/tim-linguistic-fingerprint-v1.md` - Deep linguistic analysis

3. **Set up infrastructure**
   - Added Claude Draft property to MyContent database (Notion)
   - Created project structure in `/Users/timmetz/Developer/Projects/Personal/social-post-writer/`
   - Saved 7 reference posts to `samples/tim/`

4. **Documented workflows**
   - Post creation workflow (`workflows/post-creation.md`)
   - Voice refinement workflow (`workflows/voice-refinement.md`)
   - Slash command (`/.claude/commands/draft-linkedin-post.md`)

### Key Insights

**Voice analysis approach:**
- Started with blog-style-guide generator as reference
- Tim correctly identified AI patterns in initial draft
- Pivoted to forensic linguistic analysis instead
- Focused on negative patterns (what Tim never says) as critical differentiator

**Learning loop design:**
- Store drafts in Notion Claude Draft field (easier for query/analysis)
- Compare to Tim's final edits monthly
- Correlate voice patterns with engagement metrics
- Compound learning: each post improves the next

### Testing workslop post

**Attempts:**
1. **v1:** Generic AI voice - Tim rejected ("tons of AI patterns")
2. **v2:** Applied linguistic fingerprint - Tim approved ("this is really good")

**Key difference:** Removing AI-isms ("isn't it... it's," "The real problem") and trusting white space for transitions

### Next Session

**Tasks:**
- Test `/draft-linkedin-post` workflow on real entry
- Refine voice guide based on first real usage
- Run first refinement cycle after 5-10 posts

---

## Session Stats

**Duration:** ~2 hours
**Token usage:** ~225k tokens
**Files created:** 10+
**Notion updates:** 2 (engagement metrics + Claude Draft property)
