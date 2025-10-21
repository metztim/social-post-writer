# Social Post Writer - Tasks

---

## Active Tasks

### [ ] Test Workflow on First Real Post
**Status:** Ready to test
**Description:** Run `/draft-linkedin-post` workflow end-to-end on actual [[socialpost]] entry

**Next Steps:**
1. cd to social-post-writer project
2. Run /draft-linkedin-post
3. Select entry
4. Review draft quality
5. Edit and publish
6. Verify Claude Draft saved correctly to Notion

**Success criteria:**
- Draft sounds authentically like Tim
- Claude Draft property populated in MyContent
- Workflow completes without errors

---

### [ ] First Voice Refinement Cycle
**Status:** Not Started (waiting for 5-10 posts)
**Description:** Run first monthly refinement after accumulating sufficient data

**Prerequisites:**
- 5-10 posts with Claude Draft + Final version + Engagement metrics
- At least 2 weeks since posts published (for stable metrics)

**Process:**
- Follow `workflows/voice-refinement.md`
- Compare drafts to finals
- Extract edit patterns
- Correlate with engagement
- Update voice guide to v2

---

## Completed

### [✓] Initial Voice Guide Creation
**Completed:** 2025-10-21
**Output:**
- `voice/tim-linkedin-voice-v1.md`
- `voice/tim-linguistic-fingerprint-v1.md`

**Based on:** 7 LinkedIn posts (Sept-Oct 2025)

---

### [✓] Project Setup
**Completed:** 2025-10-21
**Output:**
- Project structure created
- Claude Draft property added to MyContent
- Workflows documented
- Slash command created

---

## Future Enhancements

### [ ] Voice Guide Versioning System
**Priority:** Medium
**Description:** Formalize version control for voice guides

**Ideas:**
- Git tracking of voice guide changes
- Changelog in voice guide file
- A/B testing different voice patterns

---

### [ ] Engagement Prediction
**Priority:** Low
**Description:** Predict engagement before publishing based on voice patterns

**Approach:**
- Train simple model on voice features → engagement
- Flag when draft has low-engagement patterns
- Suggest adjustments before Tim edits

---

### [ ] Multi-Platform Support
**Priority:** Low
**Description:** Adapt voice guide for other platforms (X.com, newsletter, etc.)

**Current:** LinkedIn-specific
**Future:** Platform-specific voice variations

---

## Notes

**Refinement frequency:** Monthly or after 5-10 posts
**Voice guide versioning:** Increment major version when substantial changes
**Archive policy:** Keep all previous versions for rollback
