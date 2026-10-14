# `/requirements`: write the requirement document for an epic or topic

You write `requirements/<epic-slug>/requirement.md`. It is grounded in what the knowledge base
already says, and it asks the BA the few questions that matter. New knowledge you find on the way
(terms, rules, decisions) goes through the knowledge pipeline, not straight into pages.

## Before anything

Read:
- `PROJECT-PROFILE.md`;
- `knowledge/_meta/conventions.md` and `agents/_knowledge-pipeline.md`;
- `templates/requirement.md`.

## Input

An epic name or topic (`/requirements approving lists without a manager`), or an existing Jira epic
key (`/requirements PROJ-1200`). For a key, read the epic with `getJiraIssue` and use its summary and
description as the starting request.

The slug is lowercase and hyphenated, from the epic name. If `requirements/<slug>/requirement.md`
already exists, this is an update: read it, keep everything already confirmed, and show changes as a
diff. If its stories already have Jira keys, say so: after the update, `/review` and then `/backlog`
bring the changes into those stories. If the document was `approved` and the update changes its
requirements or stories, it goes back to `draft` with `approved_by` and `approved_on` cleared and
needs a new sign-off, unless every change comes from a decision by the person who signed it off.
Commit an update as `req: update <slug> <source id>`, and say in the report that `review.md` is out of
date until `/review` runs again.

## Steps

1. **Start from the current state.** Search the knowledge base for the area: capabilities,
   processes, entities, rules, decisions, open questions and glossary terms. Write a short "Current
   state" summary for the BA with a citation per statement, and list the open questions that touch
   this area. If the knowledge base has nothing on the area, say so, and suggest an `/intake` of
   existing material first.
2. **Clarify, with as few questions as possible.**
   - First decide what you can from the knowledge base, and state low-impact gaps as assumptions
     instead of asking.
   - Then ask in rounds of at most five questions, one at a time: multiple choice, with a
     recommended answer and why. Order them by impact: scope (what's in and out), then rules and
     permissions (who may do what, thresholds, calculations), then data (what is recorded, shown or
     missing), then the user's experience, then anything else. At the end of a round, summarise and
     decide whether another round is worth it.
   - Record each answer under "Clarifications", in a dated session. When the BA takes your
     recommendation, record "recommended, accepted by <role>". When they have no answer, it becomes
     an open question for whoever can decide it.
   - **Who decides.** Scope, the story split and the fix version are the BA's to settle for the
     document; they stay in the requirement and aren't staged as knowledge. Product behaviour
     (rules, permissions, what the product shows or allows) belongs to whoever `stakeholders.md`
     says can decide it. When the BA isn't that person, their answer is a **proposal**: it becomes a
     question to the owner with the BA's answer as the proposed one, and the requirement uses it
     marked "pending Q-x". The owner's sign-off of the requirement answers all of those at once
     (pipeline step 3, sign-off). Each proposal's question, new or existing, gets the BA's answer in
     its Proposed answer section, with the exact rule text and the page it belongs on (no BR- number yet), so the
     sign-off can add it as written. Tell the BA early: stories that rely on proposals wait for that sign-off.
   - Stop when what's left can be recorded as an assumption or an open question.
3. **Write the draft** to `requirements/<slug>/requirement.md` from `templates/requirement.md`, status
   `draft`, without committing it yet:
   - **Goal, scope (in and out), stakeholders:** from the knowledge base and the answers. User roles
     come from the entity pages for roles, or the profile's purpose.
   - **Functional requirements:** `FR-001`, each one testable statement with its source and status:
     `agreed`, or `pending Q-x` for a proposal waiting for its owner.
   - **Non-functional requirements:** `NFR-001`, in EARS form with a measure, each tied to a story's
     acceptance criterion.
   - **User stories:** `ST-01`, each with at least two Given/When/Then acceptance criteria, including
     a failure or permission path where one exists, and the rules it relies on (`None` if none).
     A question that blocks only one criterion is written against it: `Q-x (blocks AC-2)`.
   - **Assumptions** as `A-` rows (staged in step 5), **open questions**, and **success measures**
     ("None agreed yet" is fine; a question for the owner if they matter).
   - **Conflicts with the knowledge base:** every statement that contradicts a confirmed or approved
     rule, term or decision, with the question raised for it.
4. **Use the project's words.** Use glossary terms and the profile's preferred terms. Avoid the
   profile's vague words unless they have a measure.
5. **Check the draft.** Run the rule-based checks from `agents/review.md` on the draft file: the
   `critic` sub-agent when your tool has one (give it the draft's path and say "pre-check"; it then
   applies `agents/review.md`'s rule-based checks instead of `_critic.md`), otherwise a separate
   pass, re-reading the draft from the top. If you disagree with a finding, keep the text and show
   the finding with your reason. Provisional IDs
   (`Q-new-1`, `BR-new-1`) are reported as "pending staging", not as missing.
   - Fix what is mechanical yourself: missing or duplicate IDs, a story not in the "As a … I want …
     so that …" form, a vague word the knowledge base gives a measure for, a citation to the wrong
     ID, a requirement joining two statements (split it).
   - Don't invent content to pass a check. A missing failure path or a missing measure becomes an
     open question or a note to the BA.
   - This is a pre-check, not the review: it writes no `review.md` and gives no verdict.
6. **Stage new knowledge.** Terms defined, rules agreed by their owner, assumptions, risks and
   questions raised while writing (including the proposals from step 2) go into one staging file
   (`<date>-requirements-<slug>.md`), through pipeline steps 3 and 4. The document cites them by
   their provisional IDs for now.
7. **Show both together:** the document with the pre-check's remaining findings, and the staging
   file (pipeline step 5). The BA says yes or no to the document and decides each staged item.
   - If the document is a no, delete the draft file; staged items can still be applied on their own,
     with their links to the draft removed.
8. **Apply and commit once.** Apply the accepted items (pipeline step 6, steps 1 to 8), replace the
   provisional IDs in the document with the real ones, bring the document in line with any staged
   item the BA edited, and commit everything in one commit:
   `req: draft <slug>` (this replaces the pipeline's own commit). Ask before pushing. Rows in
   `trace/map.csv` are added later by `/backlog`.

## Report

- The document path, with counts of FR, NFR and stories.
- What the pre-check fixed, and what it left open.
- Open questions that block stories or single criteria, and who to ask. Proposals pending their
  owner, and the one message that would settle them: a sign-off of the requirement.
- Conflicts with the knowledge base.
- Next: `/review requirements/<slug>/requirement.md`.

## Never

- State a rule, value or permission without a source. If the BA can't give one, it stays an open
  question.
- Contradict a confirmed or approved knowledge item silently.
- Create anything in Jira; that is `/backlog`, after `/review`.
