---
type: requirement
id: REQ-<epic-slug>
title: <Epic or topic name>
status: draft
area: <area from the profile; a list when it spans several>
owner: <role, usually the Lead BA>
jira_epic:
fix_version: <release, or unscheduled>
approved_by:
approved_on:
delivered_on:
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Epic or topic name>

## Goal

<The business outcome in one or two sentences, and who benefits.>

## Current state

<What the knowledge base says about this area today, with citations: capabilities, rules, processes,
open questions. Written by /requirements from the knowledge base, so everyone starts from the same
facts.>

## Scope

**In:**
- <item>

**Out:**
- <item>

## Stakeholders

| Role | Interest | Decides |
|---|---|---|

## Functional requirements

| ID | Requirement | Source | Rules | Status |
|---|---|---|---|---|
| FR-001 | <One testable statement> | <SRC- / DEC- / Q- answer> | <BR-000, or None> | <agreed / pending Q-000> |

Cite knowledge pages with links relative to this file, for example
`([CAP-004](../../knowledge/domains/<area>/CAP-004-<slug>.md), BR-016)`.

## Non-functional requirements

In EARS form: `<optional precondition> the <system> shall <response>`, using WHEN (event), WHILE
(state), WHERE (feature), IF … THEN (unwanted behaviour), or no keyword (always).

| ID | Requirement | Measure | Source |
|---|---|---|---|
| NFR-001 | WHEN <event>, the <system> shall <response> within <measure>. | <how it is checked> | <source> |

## User stories

| Story | Summary | FR | Jira key |
|---|---|---|---|
| ST-01 | <verb and object> | FR-001 | <filled by /backlog> |

### ST-01 <Summary>

As a <role>, I want <capability>, so that <benefit>.

**AC-1 <short name>**
- Given <starting state>
- When <action>
- Then <observable outcome>

**AC-2 <short name>**
- Given <starting state>
- When <action>
- Then <observable outcome>

**Business rules:** <BR-000, or None>

**Out of scope:** <item>

**Open questions:** <None, or Q-000 (blocks the story), Q-000 (blocks AC-2), or Q-000 (non-blocking)>

## Assumptions

- <A-000: assumption, why it's assumed, how to confirm. Staged as a row in `knowledge/raid.md`>

## Open questions

| Question | Blocks | Asked of | Due |
|---|---|---|---|

## Conflicts with the knowledge base

<Every place where this requirement contradicts a confirmed or approved rule, term or decision, with
the question raised for it. "None" if none.>

## Success measures

- <SC-001: measurable outcome, or "None agreed yet">

## Clarifications

<Questions asked while writing this document, with the answer and date, newest last.>

### Session YYYY-MM-DD

- Q: <question> → A: <answer> (<who>)
