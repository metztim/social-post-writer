---
source_of_truth: https://www.notion.so/animalzco/Your-Content-Deserves-More-Than-Wishful-Workflow-Thinking-24ddf6dc2cc580ed997ae8d812ef814d
note: This is a local snapshot. The Notion page above is the canonical version. Edit there, not here.
---

# Your Content Deserves More Than Wishful Workflow Thinking

Most content teams that adopt AI follow the same arc. They start with prompt chaos — everyone on the team running their own version of ChatGPT or Claude, no shared system, no consistency. Then someone builds a proper workflow, and for a moment it feels like the problem is solved. Inputs go in, outputs come out. Structured, repeatable, scalable.

That's where we were at Animalz when we launched our AI-powered [LinkedIn program](https://www.animalz.co/blog/linkedin-playbook-b2b-startups). Two AirOps workflows: one to turn raw materials into briefs, another to turn briefs into posts. Our team would shape the drafts — tighten hooks, cut filler, make sure the voice sounded like the customer.

That was the plan. And the plan was just the beginning of our troubles.

We've already named this phenomenon [the AI onion](https://www.animalz.co/blog/ai-onion): each layer of implementation reveals the next. This is what the onion looks like when you peel all the way through.

## Your workflows need to work

Getting the workflow right is genuinely hard, and if you can't get through this layer, you'll never even encounter the challenges ahead.

Raw materials go in, briefs come out. Briefs go in, posts come out. Sounds simple, but the first version of any workflow is usually an impressive-looking way to arrive at output that's generic or garbage. Only by tweaking, testing, failing, cursing at our computers, and doing more tweaking and testing did we eventually get something we were happy with.

We learned this the hard way. We assigned Nathan, one of our best editors — Editorial Director, all-round curator of good taste — to workflow building. He's focused on quality, and the tools don't require coding, so it seemed like a natural fit. Turned out, Nathan hated it — not because the work was bad, but because it was the wrong kind of work for him. The actual work was engineering: is this system improving? Can this prompt handle edge cases? Why did this batch produce garbage when the last one was fine? You need people who like experimentation, iterative problem-solving, systems thinking. Not necessarily coders, but not typical content people either. We sent Nathan back to editorial, where he belongs.

## Your data needs a smart home

Workflows that run autonomously produce overwhelming amounts of data — and we didn't see that coming. Raw materials, output, versions to compare, briefs. The workflow worked. The data management didn't.

So we built Notion databases — Raw Materials, Briefs, LinkedIn Content — all connected, all triggerable. And something shifted. Notion became more accessible than AirOps for the service team. Not everyone needed to learn the workflow tool; they could work where they were already comfortable, triggering workflows by changing a status on a Notion item. That insight — that the system should reduce the surface area of what any individual person needs to learn — changed how we thought about the whole architecture.

But Notion can't talk to AirOps directly — the data formats don't match. So we built a server-side router to sit between them, restructuring data on an Animalz-owned server. [Claude Code](https://www.animalz.co/blog/claude-code) suggested it — we wouldn't have thought of it on our own. That router then became useful for everything else: form submissions, YouTube transcription, connecting data sources we hadn't imagined yet. On top of it, a review dashboard that flags which drafts need heavy editing versus a light polish, and tracks which angles have already been used.

AirOps was no longer the center of the system. Data was. The workflows were just one component — important, but not central. This is [context engineering](https://www.animalz.co/blog/context-engineering) in practice.

## Your customers get the white-glove treatment

As we built the system, it created opportunities we hadn't planned for. The infrastructure made them possible.

The intake form is my favorite example. We needed to onboard our first customer for the new LinkedIn program, and our traditional intake form didn't capture the right information. The customer needed it the next day, so I vibe coded a new one. As I built it, I realized AI could go through all the materials generated during the sales process — call transcripts, proposals, research — and pre-fill as much of the form as possible. Claude Code one-shotted the form and added a UX touch we didn't ask for: it automatically highlighted the pre-filled fields, showing the customer we'd done our homework before they even started.

Customers loved it. Even though the new form is longer than the original, 80% complete it in less than 24 hours. The old form often got filled in a hurry or not at all. That wasn't planned.

The same pattern repeated. Many founders didn't have a style guide, so we built a style calibrator — a tool to capture their taste through examples and preferences rather than asking them to articulate a style they'd never defined. Customers submitted more raw materials than our team could track, so we created a submission form that made contributing easy. Each of these tools emerged from a problem the system surfaced, and together they made the service feel tailored — not "we run your stuff through a tool" but "we've done the homework before you even arrive."

## Your system gets smarter every cycle

When you improve a draft by hand, you fix that draft. When you improve the system, every future run gets better. That difference compounds in ways that are hard to appreciate until you've lived with it.

Our biggest wish was engagement data feeding back into the system. We were already working with Ordinal (formerly Assembly) for LinkedIn scheduling, and it turned out they have an API. Now, once every 24 hours, our router pulls published posts and their engagement metrics from Ordinal — not just posts we created, but everything our customers publish: text, images, carousels, all the metadata. This information feeds back into the system. Brand kits get refined. Prompts get adjusted. Post variety shifts based on what's actually working — not what we guess is working.

And then there's real-time content. LinkedIn rewards relevance and timeliness, and we wanted the system to take advantage of that. QueryM monitors social media for trending topics within specific parameters, and when something relevant breaks, it sends a signal to our router, which deposits a piece of raw material into the Notion database and triggers the entire workflow. Thirty to sixty minutes later, several fully drafted posts roll out. Our team picks the strongest angle, edits the draft, and customers get relevant content within hours of something happening in their industry. That capability didn't exist before the system did.

Every new data source, every refined brand kit, every feedback cycle compounds. A competitor can switch AI models overnight. They can't replicate the system.

## Your people need to stay sharp

Once the system works, the biggest risk is your team trusting it too much.

I've watched this happen with multiple people, and the pattern is always the same. They start skeptical — "AI can't do this," "I don't trust it," "the output isn't good enough." Then the first version ships, and the posts coming out look... good. Polished. Professional. And instantly — not gradually, instantly — they flip. First drafts get treated as finished pieces. V1 output goes directly to customers.

"Sometimes I wonder if we made an airplane that is too easy to fly," an Airbus engineer once said, "because in a difficult airplane the crews may stay more alert."

So we built speed bumps — small, deliberate friction points that keep people engaged instead of surrendering to the machine. A human reviews every brief before it moves forward. Drafts carry explicit instructions marking them as first drafts and flagging what needs human judgment. We'd gone to near-full autopilot and had to pull back.

## What you're actually building

If you're a content team that's adopted AI, you're probably somewhere on this path — stuck on workflow quality, drowning in data, or wondering why the outputs feel competent but the service doesn't feel differentiated. The reason is that a workflow is not a system.

A system is workflows plus data infrastructure plus customer-facing tools plus feedback loops plus human judgment at the right moments. Each layer reveals the next, and the teams that stop peeling too early will end up with the same generic output as everyone else running the same AI models. The moat isn't the model. It's the system you build around it — and the people sharp enough to keep it honest.

We built ours through months of trial, error, and a lot of layers we didn't see coming. If you're starting that journey or stuck partway through, [we'd love to talk about what we've learned](https://www.animalz.co/ai-services).
