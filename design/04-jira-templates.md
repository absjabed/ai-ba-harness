# Jira issue templates

`/backlog` builds every Jira issue from these templates, so issues look the same whoever writes them,
and developers, testers and the Dev and QA harnesses always find the same sections in the same
place. The templates live in the project repository at `templates/jira/<type>.md`. Section headings
are fixed; the content in angle brackets is filled in.

Descriptions are written in markdown and sent through the Atlassian server, which converts them to
Jira's own format. Whether `createJiraIssue` accepts markdown directly or needs a content-format
flag is to be checked at build time.

## Fields, for every type

| Field | Filled from | Notes |
|---|---|---|
| Project | `PROJECT-PROFILE.md` | |
| Issue type | The template | Epic, Story, Task, Spike, Bug, Sub-task |
| Summary | The template's summary rule | Under 100 characters |
| Description | The template body | Markdown sections below |
| Parent | The epic created first in the same batch, or an existing epic | Stories, tasks and spikes always have a parent epic |
| Fix version | The requirement document's fix version | Required; `/backlog` refuses without one, or asks for "unscheduled" explicitly |
| Components | Profile defaults plus the requirement's area | |
| Labels | `ba-harness` plus the area tag | `ba-harness` makes harness-created issues easy to find |
| Priority | Left empty unless the requirement states it | Priority is a stakeholder decision, not the BA agent's |
| Story points | Never set | The team estimates |
| Assignee | Never set | |
| Required custom fields | Recorded per issue type by `/setup` | `/backlog` refuses if one has no value |

Every description ends with a **Source** section linking back to the requirement document and the
knowledge pages, so anyone can trace an issue to where it came from.

## Epic

**Summary:** `<Outcome in business words>` (for example "Technicians can close job cards
from the workshop floor").

```markdown
## Goal
<One or two sentences: the business outcome and who benefits.>

## Scope
**In:** <bulleted list>
**Out:** <bulleted list>

## Success measures
- <SC-001: a measurable outcome, e.g. "median approval time under one working day">

## Stakeholders
| Role | Interest | Decides |
|---|---|---|

## Business rules affected
- <BR-104: one-line summary>

## Assumptions and risks
- <A-006 / R-003 with one line each>

## Source
- Requirement: <link to requirements/<epic-slug>/requirement.md>
- Knowledge: <links to CAP-/PROC- pages>
```

## Story

**Summary:** `<Verb> <object>` from the user's point of view (for example "Raise a job card
from the defect screen").

```markdown
## User story
As a <role>, I want <capability>, so that <benefit>.

## Context
<Why this story exists and what the user does before and after. Link the capability page.>

## Acceptance criteria
**AC-1 <short name>**
- Given <starting state>
- When <action>
- Then <observable outcome>

**AC-2 <short name>**
- Given …
- When …
- Then …

## Business rules
- <BR-104: one line> (link)

## Out of scope
- <What this story deliberately doesn't do>

## Open questions
- <Q-014 with one line, or "None">

## Source
- Requirement: <document link>, <FR-003>, <story ID>
- Knowledge: <CAP-012 link>
```

**Definition of ready**, checked by `/review` and shown in the `/backlog` preview:

- Has the user story form and at least two acceptance criteria, including a failure or permission
  path where one exists.
- Every business rule it relies on exists in the knowledge base.
- Open questions are "None", or the BA has marked each as non-blocking.
- Fits INVEST: independent, negotiable, valuable, estimable, small, testable.
- Has a fix version and a parent epic.

## Task

For work that delivers no user-facing behaviour by itself (data migration, configuration,
documentation, an access request).

**Summary:** `<Verb> <object>` (for example "Load depot codes for the pilot customer").

```markdown
## What and why
<What needs doing and what it enables.>

## Done when
- <Checkable outcome>

## Source
- <Requirement or knowledge link>
```

## Spike

For a question that needs investigation before a story can be written.

**Summary:** `Spike: <the question>` (for example "Spike: can the upstream system send cancellation
reasons?").

```markdown
## Question
<The question, linked to its open question Q-xxx.>

## Why it matters
<What is blocked until it is answered.>

## Timebox
<e.g. 2 days>

## Exit criteria
- <What the answer must contain, e.g. "yes or no, with the message field name if yes">

## Source
- Open question: <Q-xxx link>
```

When the spike is done, its answer goes back through `/intake` (or `/sync` picks it up from the
comments) and closes `Q-xxx`.

## Bug (from UAT or business review only)

The QA harness raises defects found in testing. The BA harness uses this template only for problems
found in UAT or business review.

**Summary:** `<Symptom> in <screen or flow>`.

```markdown
## What happened
<Observed behaviour.>

## What should happen
<Expected behaviour, citing the acceptance criterion or business rule: AC-2 of PROJ-1234, BR-104.>

## Steps to reproduce
1. …

## Environment
<UAT or environment name, date, role used; never real personal data>

## Business impact
<Who is affected and how badly.>

## Source
- <UAT session record SRC-xxx, story key>
```

## Sub-task

Only when the team asks for them. The BA harness doesn't split stories into sub-tasks by default;
that's the delivery team's job.

## Summary conventions

| Type | Pattern | Avoid |
|---|---|---|
| Epic | Business outcome | Technology names, "Phase 2" |
| Story | User action | "As a…" in the summary (it belongs in the body) |
| Task | Verb and object | Vague verbs: "handle", "manage", "support" |
| Spike | "Spike:" plus the question | Open-ended topics without a question |
| Bug | Symptom in place | Blame, guesses at the cause |
