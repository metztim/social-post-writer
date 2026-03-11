# AI Made Building our Content System Feel Like Writing

- What We Didn't Expect to Learn Building an AI Content System
- The AI Content System That Designed Itself
- The AI System We Discovered by Building It
- Opportunities, Systems, Context: What Actually Matters for AI Content
- When Infrastructure/Engineering/Building Becomes Creative Work
- How We Built an AI Content System (And What We Learned)
- Beyond Workflows: Building an AI Content System
- We Built AI Infrastructure Without Engineers—Here's What Emerged
- Opportunities Over Optimizations: A Better Way to Implement AI
- We Didn't Design Our AI System—We Followed It
- AI Made Building Feel Like Writing
- AI Made Building our Content System Feel Like Writing
- The AI Content System That Revealed Itself
- We Didn't Design This AI Content System—We Discovered It
- When Building Starts to Feel Like Writing
- We Built This AI System by Talking to Claude

* * *

We set out to "transform our LinkedIn content service with AI" with the same goals as every other AI implementation project: achieve efficiencies, maintain quality, keep humans in the loop, _blah blah blah_.

The content system we built went way beyond those uninspiring goals. But we didn't plan it that way, we discovered it. We followed the work the way a writer follows a draft: each thing we built showed us what to make next, and gave us something worth writing down along the way.

## 1\. Opportunities over Optimizations

We thought AI x our [LinkedIn thought leadership program](https://www.animalz.co/services/linkedin-content) = AirOps workflows.

[AirOps](https://www.airops.com/) let's you string together a sequence of prompts and data in a visual workflow builder.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/188e90a1-86ee-4055-b082-298c24e701d7-RackMultipart20260129-167-su3s6w.png)

We created two such workflows. One turns raw materials (e.g., transcripts, blog articles) into briefs for LinkedIn posts. The second creates posts from those briefs. Our team then shapes those drafts: tightening hooks, cutting filler, making sure the voice actually sounds like the customer.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/8ce7ef9d-58ba-413d-bbfe-9f0a0f03839c-RackMultipart20260129-167-51hmt4.png)

That was the plan.
Then we had to onboard our first customer for this new process.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/2108110c-7277-4196-9c08-9155bca948e4-RackMultipart20260129-147-aeum1b.png)

Like many agencies, we use an intake form for new customers. All parties involved accept these as a necessary evil to get the partnership off to a good start. But intake forms become unnecessarily more evil when you ask a customer for information they already provided during the sales process (often the first minor annoyance in the new relationship).

Our new workflows for the LinkedIn thought leadership program needed completely different information from our traditional intake form. And since said customer needed the intake form the next day, I decided to vibe code a new one.

As I did so, I realized AI could go through all the materials generated during the sales process — call transcripts, proposals, etc. — plus do a _Deep Research_, and use all that data to pre-fill as much of the intake form as possible.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/d872dc0b-509e-4e71-8855-45927cf66f64-RackMultipart20260129-202-yf2osv.png)

Claude Code (CC) one-shotted the form including a smart UX. We didn't ask for it, but CC was thoughtful enough to automatically highlight pre-filled fields, emphasizing _our_ thoughtfulness to the new customer.

Customers loved it.

Even though this form is longer than our original, completion rates are higher _and_ faster. The traditional form often got filled in a hurry or not at all. The new one sees a response time of less than 24 hours for 80% of customers that have used it.

While we couldn't articulate _opportunities over optimization_ at the time, we'd glimpsed it: using AI just to achieve **optimization** is too limiting. The new form indeed reduced work for our team (fewer incomplete materials to chase), but also created an **opportunity** to improve quality (more information provided) _and_ the customer experience.

## _4\. Customers over Confidence (Bonus Principle #1)_

_Previously, we kept AI efforts internal until they were done. We wanted to get workflows stable before using them for customers._

_This approach didn't work. We'd never feel confident enough to use them, and real customer work always took priority over what felt like isolated R&D projects._

_By committing to using these workflows for actual customer deliverables, we created urgency, and built in a fast feedback loop (made possible by vibe coding) between our AI team, service team, and customer._

_Essentially, we landed on a cycle many product development teams follow:_ **_design_** _the best way to solve a problem,_ **_build_** _the solution, then_ **_test_** _it with users, and go through the cycle as fast as possible._

## 2\. Systems over Workflows

The success of the intake form and the chase of customer needs gifted us more opportunities dressed up as challenges.

Customers submitted more raw materials than our team could keep track off, so we created a submission form. Many founders didn't have an existing style guide, so we vibe coded a style calibrator to capture their taste. And our team was overwhelmed with reviewing post variations coming out of the workflows, so we created an interactive dashboard to make that task easier: flagging which drafts needed heavy editing versus a light polish, and tracking which angles had already been used.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/77e93dba-aaff-4da4-b1c3-28c0871cdbaa-RackMultipart20260129-202-cyg58d.png)

All these elements started adding up to something that looked more like a system than a bunch of workflows. In fact, it would be more accurate to say that these different elements forced us to start treating the whole as a system instead of a process.

Before reaching this point we had already articulated the [AI implementation onion](https://www.animalz.co/blog/ai-onion), meaning that an AI workflow touches many processes and resources outside of the workflow itself. But the onion idea still assumed a tool like AirOps would be at the center.

Instead, what became apparent now is that the data that goes in and out of the workflows needs a home and is the actual central anchor of the system. The raw materials, the brand kits, the previously published content; it all needs to be stored, managed, and updated as it flows through these different tools and processes.

In this particular case, we decided to use Notion as the connecting tissue for the system. But depending on your goals and scale, it can be anything from a spreadsheet to a Supabase database to a full enterprise data warehouse like Snowflake.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/522984f1-982d-4833-a443-119eef5468da-RackMultipart20260129-167-9845ee.png)

We chose Notion because you can programmatically access its databases (e.g., with Claude Code and other tools), while the UX is relatively straightforward. Our Services team could now trigger workflows from Notion by changing the status on an item, without having to access and learn AirOps.

We created three Notion databases for our LinkedIn program:

1. **Raw Materials**: Stores data like interview transcripts, style examples, and company information.
2. **Briefs**: Holds the briefs that the brief generation workflow creates from raw materials. One raw material can lead to multiple briefs.
3. **LinkedIn Content**: Saves the posts that the second AirOps workflow generates from the briefs. One brief always leads to one post.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/8174e7ed-3e85-4db2-b4a5-54016674bc29-RackMultipart20260129-153-ceonp8.png)

The Notion databases again highlighted the opportunities over optimization principle. While we implemented them out of a necessity to manage and optimize the storage of data, they'd spawn many future innovation opportunities, both big (as we'll soon see) and small.

For example, we could now use Notion Automations to trigger Slack notifications for team members when the status of a database item changed (e.g., "completed," "warning").

## _5\. Claude Code over Coding Competence (Bonus Principle #2)_

_By now, you might be asking: "__Wait, how does this all work?__" The answer is Claude Code, and the insight that you can vibe code infrastructure, not just apps._

_We, a code-illiterate team, have built everything described in this article. And many of the ideas we developed in collaboration with Claude Code._

_Here's one example of how Claude Code helped solve a problem:_

_When we tried to send data from our Notion database to an AirOps workflow, we got stuck because Notion prepares data in a structure AirOps doesn't accept, with no way to change it._

_Claude Code suggested we create a kind of router on an Animalz-owned server to take data from Notion, restructure it, and send it to AirOps. So instead of Notion → AirOps, we now send data: Notion → Animalz server → AirOps._

_This solution again confirmed the opportunities principle: the router became perfect for other improvements later, like routing form submissions, handling YouTube links that needed transcription, and more._

## 3\. Context over Prompts

Good prompts matter. The right AI model for each task matters. But what really made the difference for our LinkedIn program has been context, and lots of it.

In mid-2025, "context engineering" became the term for this: the art of getting the right information to your AI at exactly the right moment. Our brand kits contain pages of positioning, style, and product info. Unlike models from a year or two ago, the latest ones flourish on all this data when it arrives at the right point in a workflow.

The Notion databases made internal context awareness relatively straightforward. Because we had already connected all the elements, published posts, previous research, and brand materials could flow into workflows at the right moment, preventing the AI from retreading yesterday's topic or reusing a similar format.

But the other super power our system and Claude Coding unlocked was external context.

Vast amounts of data are available through third-party API and MCP services. A lot of this information has always been there, but connecting it to your system or product required expensive engineering skills.

Claude Code can now handle this for you from start to finish. Not just the building of the pipeline between your infrastructure and an API, but even the discovery of which services might have the data that you're looking for.

![](https://lex-img-p.s3.us-west-2.amazonaws.com/img/c5f26a19-d20d-402a-a1fb-344802524c10-RackMultipart20260129-153-kfdp75.png)

#### Post engagement data from Ordinal

Our biggest wish was to get LinkedIn engagement data feeding back into the system. We were already working with Ordinal (formerly Assembly) to handle LinkedIn scheduling for our customers, and it turned out they have an API.

Now, once every 24 hours, our router pulls published posts and their engagement metrics from Ordinal. Not just posts we created, but everything our customers publish: text, images, carousels, and all the metadata. This information feeds back into the system to keep improving brand kits, prompts, and post variety based on what's working.

#### Trending topics from QueryM

QueryM monitors social media for trending topics within specific parameters. We create a profile for each customer and their industry. When something relevant breaks, QueryM sends a signal to our router, which deposits a piece of raw material into the Notion database and triggers the entire workflow system.

30 to 60 minutes later, several fully drafted posts roll out. Our team gets a notification, picks the strongest angle, and edits the draft. Our customers get relevant content within hours of something happening in their industry.

## Creativity over Engineering

The distinction between designing and discovering collapses when building becomes as quick as describing an idea.

We didn't start with "opportunities over optimizations" or "systems over workflows" or "context over prompts." Those principles emerged through the building. The intake form led to the submission form, which led to the router, which led to external APIs — each thing we built revealed the next opportunity.

The router wasn't on any roadmap; it emerged from a conversation between us, the problem, and Claude Code. This is why the process felt more like writing than engineering: you discover what you're making while you make it. Outlines are provisional. The draft teaches you what it wants to be.

That's what happened here, except with infrastructure instead of words.

With Claude Code, there's no spec-to-developer handoff, no months-long feedback loop. You can follow an idea the same afternoon you have it. Building becomes iterative, intuitive; closer to drafting than to scoping.

For content marketers who also think of themselves as writers, that might sound familiar — and hopeful. Building used to require a different kind of brain. Now, with AI handling the engineering, it feels like the creative work we already know how to do.