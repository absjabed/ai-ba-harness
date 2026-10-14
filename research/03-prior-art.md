# Prior art: AI agents in BA and requirements roles

Research note, October 2026. Several of these projects have changed a lot recently (BMAD and Spec
Kit no longer match most blog posts about them). Claims I could not confirm against official
sources are marked [unverified].

## BMAD Method

Stable v6.12, installed with `npx bmad-method install`; a v7 alpha ships as Agent Skills. Earlier
versions used role personas: an Analyst wrote a project brief, a PM wrote the PRD with epics, a PO
"sharded" the PRD and architecture into small chunks, and a Scrum Master wrote self-contained story
files (rationale, constraints, tests, links back to the source docs) for the dev agent. The current
docs drop the personas and organise by the size of the work instead: trivial, one session,
epic-sized, project-sized. Skills cover brainstorming, product brief, PRD (create, update and
validate modes), UX, spec, architecture and ordered tickets. `bmad-check-implementation-readiness`
checks PRD, UX, architecture and epics for gaps before build.

Worth borrowing: ceremony that scales with the size of the work; separate create, update and
validate modes; a readiness check before hand-off; story files that carry their own context and
link back to the source.

Avoid: a large persona cast whose surface keeps changing between versions. The maintainers dropped
it themselves.

## GitHub Spec Kit and AWS Kiro

Spec Kit's commands are `constitution`, `specify`, `clarify`, `plan`, `tasks`, `analyze`,
`checklist` and `implement`.

- The spec template has prioritised user stories (P1 to P3), each with an independent test and
  Given/When/Then scenarios, plus edge cases, `FR-001` requirements, `SC-001` measurable success
  criteria, key entities and assumptions. It covers what and why, never how.
- `specify` prefers informed defaults recorded as assumptions, allows at most three
  `[NEEDS CLARIFICATION]` markers (ranked scope, then security, then UX, then tech), and re-checks
  the result against a 16-item quality checklist up to three times.
- `clarify` rates ten ambiguity categories as clear, partial or missing, then asks at most five
  questions, one at a time, multiple choice with a recommended answer. Each answer goes into a
  dated Clarifications section, and contradicting text in the spec is replaced.
- `checklist` writes "unit tests for English": numbered items (`CHK001`) that test the requirements,
  never the implementation; at least 80% must cite a spec section or say `[Gap]`; only a person
  ticks them.
- `analyze` is read-only. It reports duplication, ambiguity, underspecification, conflicts with the
  constitution, coverage gaps and inconsistency, graded critical to low, capped at 50 findings,
  with a requirement-to-task coverage table. Fixes are applied only after approval.

Kiro produces `requirements.md` (user stories with EARS acceptance criteria such as "WHEN … THE
SYSTEM SHALL …"), `design.md` and `tasks.md`. It supports requirements-first or design-first, has a
separate bugfix spec (current, expected and unchanged behaviour), and an "Analyze Requirements" step
that flags inconsistencies, ambiguities, conflicts and gaps before design. Its "Quick Spec" skips
the approval gates, which implies the normal flow has them [details unverified].

Worth borrowing: almost all of it. Capped clarification loops, answers recorded in the document,
quality checks kept separate from testing, read-only analysis, a bugfix variant.

Adapt: both tools are shaped around one developer's feature branch. A BA works across a whole
project and many stakeholders.

## Atlassian Rovo, Confluence and Jira

- Built-in Rovo agents include Product Requirements Guide (creates and reviews PRDs), Work Item
  Planner (breaks an epic or page into tasks), Work Item Organizer and Blocker Checker. Custom
  agents are built in Rovo Studio.
- Confluence's "Create Jira work items" drafts items from a page in a side panel; you edit or remove
  each one, then create them, and they are linked back into the page.
- Jira's "Suggest child work items" and "Break down with Rovo" let you accept, edit or decline each
  suggestion before anything is created.
- Duplicate detection is weak: "find and link similar work items as you create" is in beta, and the
  Triage Agent flags duplicates only after creation. A real pre-save check needs a Marketplace app.
- Jira Product Discovery's AI mostly summarises notes and drafts idea descriptions [a dedicated
  insight-summary feature unverified].

Worth borrowing: accept, edit or decline per item before anything is written; linking created items
back to the source page; respecting the user's own permissions.

Avoid: assuming the tracker will catch duplicates. Atlassian's docs and partners warn that bulk AI
creation is error-prone.

## Other commercial tools

| Tool | What it automates |
|---|---|
| Productboard Spark | Themes and synthesis over customer feedback (Zendesk, Gong and others), with citations; about 300 to 500 notes per board |
| Aha! AI | User stories from a feature plus its linked ideas and goals; acceptance criteria as a separate request |
| ClickUp Brain | PRDs and stories with acceptance criteria in Docs; tasks extracted from docs |
| ChatPRD | PRD drafts from an outline, review of existing docs, export to Confluence and Notion (vendor claims only) |
| StoriesOnBoard AI | A story map (goals, steps, stories, acceptance criteria) from a one-time product context; beta |
| Jama Connect Advisor | Scores requirements against INCOSE and EARS rules, singly or in bulk, over time |
| IBM RQA (DOORS Next) | Watson NLP trained on INCOSE guidance, about 11 quality scores [coverage beyond DOORS Next unverified] |
| Visure | Quality analysis while writing, test-case generation (mostly marketing material) |
| Microsoft | No official Copilot story drafting in Azure Boards found [unverified]; the third-party Copilot4DevOps fills the gap |

Worth borrowing: a one-time product-context setup, feedback synthesis with citations, rule-based
quality scoring. Avoid: vendor ROI figures as evidence.

## Open-source Claude Code and agent collections

- **VoltAgent awesome-claude-code-subagents** (about 160 agents) includes `business-analyst`,
  `product-manager`, `scrum-master`, `backlog-grooming` and `assumption-mapping`. The
  business-analyst agent is a long generic list of BA practices with checklist targets nobody can
  measure. It sets a tone but has no workflow, gates or templates.
- **CCPM** (automazeio/ccpm, about 8.4k stars): PRD, then epic, then tasks, then GitHub issues with
  sub-issues, then a worktree and code. Local task files are renamed to issue numbers through a
  mapping file. Status and standup are plain bash scripts, not model calls. Sync is user-initiated,
  with no deduplication.
- **wshobson/agents** (94 plugins, 202 agents): its "conductor" plugin keeps `product.md`,
  `tech-stack.md` and `workflow.md`, plus one track per feature with `spec.md` and `plan.md` and
  status markers [partly unverified; the catalog was down].

Worth borrowing: CCPM's ID mapping file and scripted status reports; conductor's persistent
product-context files. Avoid: one-file "BA persona" agents with no process behind them.

## Ten patterns to adopt

1. Capped clarification: one question at a time, multiple choice with a recommended answer, about
   five per session, answers written back to a dated log in the document (Spec Kit).
2. Informed defaults, recorded as assumptions; reserve "needs clarification" markers for
   high-impact unknowns, at most three (Spec Kit).
3. EARS for requirement statements (ubiquitous, WHEN, WHILE, WHERE, IF/THEN, one SHALL each) and
   Given/When/Then for scenarios (Kiro, Jama).
4. Stable IDs (FR-, NFR-, SC-, CHK-) in documents, a mapping file to tracker keys, and a coverage
   matrix from requirements to stories (Spec Kit, CCPM).
5. A read-only requirement-quality report, graded by severity, with edits applied only after
   approval (Spec Kit analyze, Kiro, INCOSE tools).
6. Checklists that test the requirements, never the implementation, ticked only by a person (Spec
   Kit checklist).
7. Sharding: PRD into epics into self-contained stories that link back to their source sections
   (BMAD).
8. A readiness check before hand-off with a pass, concerns or fail verdict (BMAD).
9. An approval step before any tracker write: per-item preview to accept, edit or decline, then
   link the created items back into the source document (Rovo, Confluence, CCPM).
10. Search for duplicates before creating, and propose a link or update instead; plus one
    persistent product-context file every command loads (conductor, Spec Kit; Jira has no generally
    available pre-save check).

Also: scale the process to the size of the work, so a small change doesn't trigger the full PRD
flow (BMAD).

## Sources

- https://github.com/bmad-code-org/BMAD-METHOD
- https://docs.bmad-method.org/plan/choose-a-planning-path/
- https://tessl.io/registry/skills/github/bmad-code-org/BMAD-METHOD/bmad-check-implementation-readiness
- https://codemyspec.com/blog/bmad-method-explained
- https://github.com/github/spec-kit
- https://raw.githubusercontent.com/github/spec-kit/main/templates/spec-template.md
- https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/specify.md
- https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/clarify.md
- https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/checklist.md
- https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md
- https://kiro.dev/docs/specs/ and https://kiro.dev/docs/specs/feature-specs/
- https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax
- https://support.atlassian.com/rovo/docs/atlassian-agents/
- https://www.atlassian.com/software/rovo/use-cases/work-item-planner
- https://jimiwikman.se/atlassian/atlassian-resources/atlassian-app-updates/break-down-work-items-with-rovo-in-list-view-r1265/
- https://support.atlassian.com/organization-administration/docs/understand-atlassian-intelligence-features-in-products
- https://support.atlassian.com/jira-product-discovery/docs/explore-atlassian-intelligence-in-jira-product-discovery/
- https://community.atlassian.com/forums/Jira-questions/Finding-similar-use-case-possible-in-JIRA-using-AI-or-any-tool/qaq-p/3190755
- https://support.productboard.com/hc/en-us/articles/48274747340947-Customer-feedback-management-in-Spark
- https://www.aha.io/ai-library/skill-user-stories
- https://help.clickup.com/hc/en-us/articles/40676496321303-Use-AI-for-documentation
- https://www.banani.co/blog/chatprd-ai-review
- https://docs.storiesonboard.com/en/articles/8193982-storiesonboard-ai-guide
- https://www.jamasoftware.com/datasheet/jama-connect-advisor
- https://requisis.com/en/saas-doors-dng/rqa-saas.html
- https://visuresolutions.com/features/requirements-quality-analysis-software
- https://www.g2.com/products/copilot4devops-plus/reviews
- https://www.spguides.com/create-agent-in-m365-copilot-to-generate-word-document/
- https://github.com/VoltAgent/awesome-claude-code-subagents
- https://github.com/wshobson/agents and https://www.vibeindex.ai/plugins/wshobson/agents/conductor
- https://github.com/automazeio/ccpm
