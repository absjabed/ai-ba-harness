---
type: harness-feedback
title: A "Data" line under each story in the requirement template
status: applied-locally
kind: harness change
risk: behaviour
version_impact: minor
raised_by: Lead BA
raised_on: 2026-10-15
harness_version: 0.5.0
---

# A "Data" line under each story in the requirement template

<!-- status: proposed (written, not applied) · applied-locally (also changed in this repository) ·
     accepted (taken into the harness; give the version) · declined (with the reason) -->

## The problem

The Lead BA: "the requirement template should have a 'Data' line under each story, listing the
entities and fields it reads or changes; developers keep asking". A story in a requirement document
says what the user sees and which rules apply, but not which data it reads or changes, so developers
come back to the BA to ask which fields a story uses.

## Evidence

`requirements/inspection-due-dates-and-dashboard-banding/requirement.md`, ST-02 "See a vehicle's next
due date counted from its anchor date". The Lead BA reports that the developer asked which fields
the due date uses. The story's criteria mention the anchor date, the interval and recorded
inspections in passing, and FR-004 to FR-006 describe the calculation, but nothing in the story
says, in one place, which data it reads. The story ends with only:

```text
**Business rules:** BR-002
**Out of scope:** VOR vehicles (Q-001; A-001 applies); whether an inspection without a brake test
counts (Q-002)
**Open questions:** Q-006 (blocks AC-2 and AC-3)
```

With the proposed line, ST-02 would have said something like "**Data:** Vehicle: anchor date, safety
inspection interval (reads). Safety inspection: date done (reads)." The developer's question itself
was asked in person; it isn't recorded in the repository.

## Proposed change

Add a **Data** line to each story in the requirement template, after the business rules, and tell
`/requirements` how to fill it: the entities the story reads or changes and the fields involved, in
business words (conventions rule 7: no table or column names), taken from the entity and capability
pages. A field the knowledge base doesn't name becomes an open question, not a guess.

```diff
--- a/templates/requirement.md
+++ b/templates/requirement.md
@@ -80,6 +80,8 @@ As a <role>, I want <capability>, so that <benefit>.
 
 **Business rules:** <BR-000, or None>
 
+**Data:** <Entity: field, field (reads or changes), one entry per entity, in business words; None if none>
+
 **Out of scope:** <item>
 
 **Open questions:** <None, or Q-000 (blocks the story), Q-000 (blocks AC-2), or Q-000 (non-blocking)>
--- a/agents/requirements.md
+++ b/agents/requirements.md
@@ -59,6 +59,9 @@ bring the changes into those stories.
    - **User stories:** `ST-01`, each with at least two Given/When/Then acceptance criteria, including
      a failure or permission path where one exists, and the rules it relies on (`None` if none).
      A question that blocks only one criterion is written against it: `Q-x (blocks AC-2)`.
+     Its **Data** line lists the entities it reads or changes and the fields involved, in business
+     words from the entity and capability pages (no table or column names). A field the knowledge
+     base doesn't name is an open question, not a guess.
    - **Assumptions** as `A-` rows (staged in step 5), **open questions**, and **success measures**
      ("None agreed yet" is fine; a question for the owner if they matter).
    - **Conflicts with the knowledge base:** every statement that contradicts a confirmed or approved
```

## Files touched

- `templates/requirement.md`
- `agents/requirements.md`

## What else it affects

- `/review` reads `templates/requirement.md` but has no check for the Data line, so a story without
  one isn't flagged. Not proposed here; a minor check could be added later if the line proves useful.
- `/backlog` builds Jira stories from `templates/jira/story.md`, which has no Data section, so the line
  stays in the requirement document and doesn't reach Jira. Developers who read only the Jira story
  won't see it (the story's Source section links the document). Adding it to the Jira template is
  left out deliberately: it changes what `/backlog` writes to Jira and every existing story would show
  a difference on the next run.
- The conventions: rule 7 (business language) already covers how the line is worded. Entity pages
  (`knowledge/entities/`, `ENT-`) are the natural source; this project has none yet.
- Existing requirement documents don't change; they get the line the next time `/requirements`
  updates them.
- The handbook's description of the requirement template, if it lists the story lines (the handbook
  isn't in project repositories, so it wasn't checked).

## Outcome

Applied locally on 2026-10-15 by the Lead BA (profile section 8). Not yet accepted in the harness.
