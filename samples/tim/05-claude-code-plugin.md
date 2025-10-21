# Claude Code plugin

**Published:** 2025-10-15
**Reactions:** 33 | **Comments:** 8 | **Reposts:** 0 | **Impressions:** 2,513
**Engagement Rate:** 1.63%

---

Remember the AI style guide creator I built with Claude Code? It's now a published plugin. In an

**Animalz**

plugin marketplace. That didn't exist 30 minutes ago.

And I didn't build any of it.

Here's what happened:

**Anthropic**

announced Claude Code plugins a few days ago. I thought: "Maybe my style guide creator could be one of those."

So I opened Claude Code and said: "Can you analyze how existing plugins work, convert my blog style guide creator into a plugin, and also create a marketplace to distribute it?"

It did all of it. In one session, with one click:

• Analyzed existing plugin structures from GitHub
• Converted all my agents and commands to plugin format
• Added proper documentation, examples, and copy
• Created marketplace infrastructure
• Published everything to GitHub
• Created a v1.0.0 release

For context: Last week I reverse-engineered our Animalz style guide by having Claude Code analyze 15 blog posts. Then I had 8 specialized agents review my articles against it.

Now that workflow is a plugin anyone can install.

Launch Claude Code, then use these commands:

/plugin marketplace add animalzinc/claude-plugins

/plugin install blog-style-guide-creator

That's it. It's open source and free on GitHub:

**https://lnkd.in/gY_7tzPH**

More plugins coming soon I guess! 😃

P.S. Not sure how to get started with Claude Code? We just published a getting started guide on the Animalz blog (link in comments).
