# What project-level BAs do, and where AI helps

Research note, October 2026. Sources at the end; claims I could not verify are marked.

## The work, by BABOK knowledge area

IIBA's Business Analysis Standard keeps the six BABOK v3 knowledge areas and their 30 tasks. They run
in parallel on a real project. The table maps each area to the recurring work on a software
delivery project and rates how much AI can take on.

| Knowledge area | Recurring tasks | Artifacts | AI fit | Why |
|---|---|---|---|---|
| Planning & monitoring | Pick a predictive or adaptive approach, map stakeholders, set decision rights, decide where requirements live, report status | BA plan, stakeholder register, RACI, power/interest map, change-control process, RAID log, status reports | Medium | Good at templates and status roll-ups from Jira. It cannot know who really holds power or must approve |
| Elicitation & collaboration | Plan interviews and workshops, write question sets, take notes, play results back | Elicitation plan, interview guides, agendas, meeting notes, confirmed results, decision log, action items | High for prep and summaries; low for running sessions | Rapport, reading the room and negotiation stay human |
| Requirements life cycle | Trace, maintain and reuse requirements, prioritise (MoSCoW, WSJF), assess changes, get approval | Traceability matrix, change requests with impact analysis, prioritised backlog, sign-off records, baselines | High for trace links, impact candidates and duplicate detection; medium for prioritisation; none for approval | The WSJF arithmetic is easy; the value judgements and the approval are accountability |
| Strategy analysis | Current state, future state, risks, change strategy | Problem statement, as-is process maps, gap analysis, business case, risk register, transition plan, vision | Medium | Structures and drafts well from supplied evidence, and invents current-state facts if it isn't given any |
| Requirements analysis & design definition | Specify and model, verify quality, validate against need, compare design options | BRD/FRD, epics, user stories with Gherkin acceptance criteria, to-be process maps, use cases, data dictionary, glossary, business rules, NFRs, options analysis | High for drafting, rule and glossary extraction and quality checks; low to medium for validation and choosing a solution | Drafting is pattern work; validation needs the business |
| Solution evaluation | UAT planning and support, defect triage against requirements, post-go-live KPI review | UAT plan, scenarios, UAT sign-off, business release notes, training material, benefits report | Medium to high for scenarios and release notes; none for sign-off | Sign-off is an accountability act |

The Agile Extension (v2, 2017) adds three planning horizons that map cleanly onto harness modes:
strategy (portfolio and product decisions), initiative (epics, roadmap, options) and delivery (story
splitting, refinement, acceptance criteria, answering the team's questions). A newer edition may
exist; not checked.

## How BAs use AI today

- IIBA's Global State of Business Analysis surveys show BAs who see a positive AI impact on their
  career at 63% (2024), 74% (2025) and 69% (2026); negative sentiment was 5% in 2026 (n = 2,120,
  122 countries). The task-level breakdown is members-only, so I could not verify which tasks they
  use AI for.
- A Thoughtworks pilot had a BA and a QA use AI to break three epics into stories, acceptance
  criteria and test scenarios: about 20% less analysis time (including writing the context) and
  about 10% fewer bugs and rework reasons, self-estimated on a small sample. Their main lesson:
  output quality depends on reusable project context (domain, architecture). Changing existing
  requirements was harder than specifying new ones.
- Research on story quality: ChatGPT's ratings broadly agree with human raters but vary between
  runs (Ronanki et al., 2023, who suggest taking the best of three). On 182 industrial stories
  (Silva et al., XP 2026), GPT-5-mini had the best recall, while the rule-based AQUSA tool had far
  fewer false positives and GPT-5 hallucinated often. The authors recommend rule-based checks first,
  then an LLM review.
- A 2025 review of 74 LLM-for-requirements studies found the field mostly exploratory, with little
  industrial validation.
- Atlassian Rovo turns a Confluence page into proposed Jira items on a canvas that you edit before
  clicking "Create all". Propose, review, then create is the vendor pattern too.
- Atlassian's State of Teams 2025 reports about a quarter of time spent searching for information,
  and half of workers saying teams duplicated work without knowing (figures via press coverage).
- I found no credible BA-specific survey of AI usage share; the figures that exist come from vendor
  blogs.

What AI does well for a BA: meeting summaries with decisions and actions; story and acceptance
criteria drafts from notes; interview question sets; glossary and business-rule extraction;
spotting ambiguity, missing edge cases and contradictions; suggesting trace links and change
impact; release notes and UAT scenarios from tickets.

Where it goes wrong (DataArt gives concrete examples):

- It invents systems, integrations and rule values (a CRM sync that doesn't exist, a wrong lockout
  threshold), and writes acceptance criteria that break unwritten company policy.
- It contradicts itself across iterations and misses edge cases.
- It produces ideas with no link to a goal or KPI.
- It can write biased or privacy-invasive requirements.
- It floods the backlog with too many or duplicate tickets.
- Confidential data leaks when people paste minutes or code into unapproved tools (Samsung, 2023).
- It cannot handle stakeholder politics, priority trade-offs or sign-off.

## Quality checks to run on AI output

- **INVEST** for each story: independent, negotiable, valuable, estimable, small, testable.
- **ISO/IEC/IEEE 29148:2018** for each requirement: necessary, appropriate, unambiguous, complete,
  singular, feasible, verifiable, correct, conforming. The 2011 edition used a different list, so
  pin the edition.
- **Gherkin** acceptance criteria: one behaviour per scenario, observable outcomes, no UI
  implementation steps, scenario outlines for data variants.
- **Definition of Ready** as a light team checklist, not an approval gate (Scrum.org warns against
  gating on it; it isn't in the Scrum Guide).
- **Rule-based structural checks** (AQUSA-style: well formed, atomic, minimal, uniform, unique)
  before any LLM review.

## Controls the evidence points to

1. Propose, review, then write: a full preview and an explicit yes before anything goes to Jira or
   Confluence, with a cap on how many items one batch can create.
2. Provenance: every requirement, rule and acceptance criterion cites its source (note file and
   line, transcript timestamp, or ticket key). Anything without one is an assumption or an open
   question, never a fact.
3. Check for duplicates and conflicts against the backlog and glossary before proposing anything.
4. Two quality gates: the deterministic checklist first, then an LLM review, run more than once for
   stability.
5. Ground the agent in reusable project context (glossary, domain model, policies, architecture).
6. People own the political acts: prioritisation calls, approvals, UAT sign-off and stakeholder
   messages. The AI drafts; a named person decides, and the decision log records who.
7. Data handling: approved tools and tenants only, redact personal and confidential data from
   notes, and review requirements that affect people for bias.
8. Play elicitation summaries back to the participants (BABOK's "confirm elicitation results")
   before they become requirements.

## Sources

- IIBA tasks and knowledge areas: https://www.iiba.org/knowledgehub/business-analysis-standard/4-tasks-and-knowledge-areas/introducing-business-analysis-tasks/
- IIBA Global State of BA 2026: https://www.iiba.org/career-resources/the-global-state-of-business-analysis/the-global-state-of-business-analysis-reports-and-surveys/the-global-state-of-business-analysis-2026/
- IIBA 2025 findings: https://www.iiba.org/business-analysis-blogs/top-5-findings-from-the-2025-global-state-of-business-analysis-report/
- Agile Extension horizons: https://www.iiba.org/business-analysis-blogs/what-is-agile-business-analysis-and-how-can-it-help-your-organization/
- Agile Extension v2 release: https://www.iiba.org/globalassets/about-iiba/press-releases/2017-08-iiba-and-agile-alliance-release-babok-guide-v2.pdf
- Thoughtworks pilot: https://www.thoughtworks.com/insights/blog/generative-ai/using-ai-requirements-analysis-case-study
- DataArt failure modes: https://team.dataart.com/articles/future-business-analyst-ai-validator-role
- Ronanki et al. 2023: https://arxiv.org/pdf/2306.12132
- Silva et al., XP 2026: https://conf.researchr.org/details/xp-2026/xp-2026-papers/9/Evaluating-the-Quality-of-User-Stories-An-Extended-Comparative-Study-of-Multiple-LLM
- LLM-for-RE review: https://arxiv.org/abs/2509.11446v1
- LLM agent for story quality: https://arxiv.org/pdf/2403.09442
- 29148:2018 characteristics: https://arxiv.org/pdf/2408.10886 (2011 list: https://www.formalmind.com/?p=999)
- Rovo create work items: https://support.atlassian.com/jira-software-cloud/docs/create-work-items-with-rovo/
- State of Teams 2025: https://www.atlassian.com/blog/state-of-teams-2025
- Microsoft Work Trend Index 2025: https://news.microsoft.com/en-cee/?p=3503
- Samsung restriction: https://www.theregister.com/2023/05/02/samsung_generative_ai_ban/
- Definition of Ready: https://www.scrum.org/node/14779
- INVEST (not fetched): https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/
- Gherkin reference (not fetched): https://cucumber.io/docs/gherkin/reference/
