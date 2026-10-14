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
diff.

## Steps

1. **Start from the current state.** Search the knowledge base for the area: capabilities,
   processes, entities, rules, decisions, open questions and glossary terms. Write a short "Current
   state" summary for the BA with a citation per statement, and list the open questions that touch
   this area. If the knowledge base has nothing on the area, say so, and suggest an `/intake` of
   existing material first.
2. **Clarify, with as few questions as possible.**
   - First decide what you can from the knowledge base, and state low-impact gaps as assumptions
     instead of asking.
   - Then ask one question at a time:
     - multiple choice, with a recommended answer and why;
     - at most five questions per round;
     - ordered by impact: scope, then rules and permissions, then data, then user experience, then
       everything else.
   - Record each answer under "Clarifications", in a dated session.
   - Stop when what's left can be recorded as an assumption or an open question.
3. **Write the document** from `templates/requirement.md`, status `draft`:
   - **Goal, scope (in and out), stakeholders:** from the knowledge base and the answers.
   - **Functional requirements:** `FR-001`, each one testable statement with its source.
   - **Non-functional requirements:** `NFR-001`, in EARS form with a measure.
   - **User stories:** `ST-01`, each with at least two Given/When/Then acceptance criteria, including
     a failure or permission path where one exists, and the rules it relies on.
   - **Assumptions, open questions and success measures.**
   - **Conflicts with the knowledge base:** every statement that contradicts a confirmed or approved
     rule, term or decision, with the question raised for it.
4. **Use the project's words.** Use glossary terms and the profile's preferred terms. Avoid the
   profile's vague words unless they have a measure.
5. **Stage new knowledge.** Terms defined, rules agreed, decisions made and questions raised while
   writing go into one staging file (`<date>-requirements-<slug>.md`), following pipeline steps 3 to 5.
   The document can cite them as `Q-new-n` until they're accepted; update the citations to real IDs
   after applying.
6. Show the document, write it after a yes, and commit it with any applied knowledge changes:
   `req: draft <slug>`. Ask before pushing.

## Report

- The document path, with counts of FR, NFR and stories.
- Open questions that block stories, and who to ask.
- Conflicts with the knowledge base.
- Next: `/review requirements/<slug>/requirement.md`.

## Never

- State a rule, value or permission without a source. If the BA can't give one, it stays an open
  question.
- Contradict a confirmed or approved knowledge item silently.
- Create anything in Jira; that is `/backlog`, after `/review`.
