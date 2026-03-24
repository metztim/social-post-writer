---
superseded_by: draft-v5.md
source_of_truth: https://www.notion.so/animalzco/Your-Content-Deserves-More-Than-Wishful-Workflow-Thinking-24ddf6dc2cc580ed997ae8d812ef814d
note: Superseded. See draft-v5.md or the Notion page above for the current version.
---

# Your Content Deserves More Than Wishful Workflow Thinking

We thought we knew what "AI for our [LinkedIn program](https://www.animalz.co/blog/linkedin-playbook-b2b-startups)" meant. Two AirOps workflows — one to turn raw materials into briefs, another to turn briefs into posts. Our team would shape the drafts: tighten hooks, cut filler, make sure the voice actually sounded like the customer.

That was the plan.

Before that plan, we had the same setup as most content teams: different people, different prompts, no shared system. Mostly Claude, some ChatGPT. Everyone had their own versions of everything.

AirOps workflows felt like the real answer — a step up from prompt chaos into something structured and scalable. And they were. But they were also just the beginning.

What we discovered wasn't a workflow. It was a system — databases, routers, intake forms, feedback loops, style calibrators, API integrations. The work of building it looked nothing like content work. We'd already named this phenomenon [the AI onion](https://www.animalz.co/blog/ai-onion): each layer of implementation reveals the next. This is what the onion actually looks like when you peel all the way through it.

## Your workflows need to work

Getting the workflow right is genuinely hard. And if you can't get through this layer, you'll never even encounter the challenges ahead.

Raw materials go in, briefs come out. Briefs go in, posts come out. Sounds simple. It isn't. The first version of any workflow is an impressive-looking way to arrive at output that's generic or garbage. Only by tweaking, testing, failing, cursing at our computers, and doing more tweaking and testing did we eventually get something we were happy with. The real work is product development, not content work.

[Needs Nathan's permission] We learned this the hard way. We assigned Nathan, one of our best editors, to workflow building. He's focused on quality, and the tools don't require coding — it seemed like a natural fit. But Nathan hated it. Not because the work was bad, but because it was the wrong kind of work for him. He was evaluating output the way an editor evaluates a draft: is this good? The actual work was engineering: is this system improving? You need people who like experimentation, iterative problem-solving, systems thinking. Not necessarily coders, but not typical content people either.

Most teams are still stuck in this layer. Some will stay here for months. But even when you nail it — even when the workflows consistently produce good output — you've only built the engine. Not the car.

## Your data needs a smart home

Workflows that run autonomously produce overwhelming amounts of data. We didn't see that coming.

We were drowning in raw materials, output, versions to compare, briefs. The workflow worked. The data management didn't.

So we built Notion databases — Raw Materials, Briefs, LinkedIn Content — all connected, all triggerable. Something shifted. Notion became more accessible than AirOps for the service team. Not everyone needed to learn the workflow tool. They could work where they were already comfortable, triggering workflows by changing a status on a Notion item.

But Notion can't talk to AirOps directly — the data formats don't match. So we built a server-side router to sit between them, restructuring data on an Animalz-owned server. [Claude Code](https://www.animalz.co/blog/claude-code) suggested it. We wouldn't have thought of it on our own. That router then became useful for everything else: form submissions, YouTube transcription, connecting data sources we hadn't imagined yet.

We also built a review dashboard that flags which drafts need heavy editing versus a light polish, and tracks which angles have already been used for each customer.

AirOps was no longer the center of the system. Data was. The workflows were just one component — important, but not central. This is [context engineering](https://www.animalz.co/blog/context-engineering) in practice: the right information, arriving at the right point in the workflow, is what makes the difference between generic output and something that actually sounds like the customer.

## Your customers get the white-glove treatment

As we built the system, it created opportunities we hadn't planned for. Not because we were visionary, but because the infrastructure made them possible.

The intake form is my favorite example. We needed to onboard our first customer for the new LinkedIn program, and our traditional intake form didn't capture the right information. The customer needed it the next day. So I vibe coded a new one.

As I built it, I realized AI could go through all the materials generated during the sales process — call transcripts, proposals, research — and pre-fill as much of the form as possible. Claude Code one-shotted the form and added a UX touch we didn't ask for: it automatically highlighted the pre-filled fields, showing the customer we'd done our homework before they even started.

Customers loved it. Even though the new form is longer than the original, 80% complete it in less than 24 hours. The old form often got filled in a hurry or not at all.

That wasn't planned.

The same pattern repeated. Many founders didn't have a style guide, so we built a style calibrator — a tool to capture their taste through examples and preferences rather than asking them to articulate a style they'd never defined. Customers submitted more raw materials than our team could track, so we created a submission form that made contributing easy.

Each of these tools emerged from a problem the system surfaced. And together, they made the service feel bespoke — not "we run your stuff through a tool" but "we've done the homework before you even arrive."

## Your system gets smarter every cycle

When you improve a draft by hand, you fix that draft. When you improve the system, every future run gets better.

Our biggest wish was engagement data feeding back into the system. We were already working with Ordinal (formerly Assembly) for LinkedIn scheduling, and it turned out they have an API. Now, once every 24 hours, our router pulls published posts and their engagement metrics from Ordinal — not just posts we created, but everything our customers publish: text, images, carousels, all the metadata.

This information feeds back into the system. Brand kits get refined. Prompts get adjusted. Post variety shifts based on what's actually working — not what we guess is working.

And then there's real-time content. QueryM monitors social media for trending topics within specific parameters. We create a profile for each customer and their industry. When something relevant breaks, QueryM sends a signal to our router, which deposits a piece of raw material into the Notion database and triggers the entire workflow.

30 to 60 minutes later, several fully drafted posts roll out. Our team gets a notification, picks the strongest angle, edits the draft. Customers get relevant content within hours of something happening in their industry. That capability didn't exist before we built the system.

Every new data source, every refined brand kit, every feedback cycle compounds. A competitor can switch AI models overnight. They can't replicate the system.

## Your people need to stay sharp

Once the system works, the biggest risk is your team trusting it too much.

I've watched this happen with multiple people, and it's always the same pattern. They start skeptical — "AI can't do this," "I don't trust it," "the output isn't good enough." Then the first version ships, and the posts coming out look... good. Polished. Professional. And instantly — not gradually, instantly — they flip. First drafts get treated as finished pieces. V1 output goes directly to customers.

"Automation tends to turn us from actors into observers," Nicholas Carr wrote in *The Glass Cage*. That's exactly what happens — except it doesn't creep in over months. It happens the moment the system produces something that looks polished. "Sometimes I wonder if we made an airplane that is too easy to fly," an Airbus engineer once said, "because in a difficult airplane the crews may stay more alert."

So we built speed bumps — small friction points that keep people engaged instead of surrendering to the machine. We'd gone to near-full autopilot and had to pull it back.

The system is powerful. But it needs sharp humans. That's not wishful workflow thinking — that's the part nobody warns you about.

What are you building speed bumps for?
