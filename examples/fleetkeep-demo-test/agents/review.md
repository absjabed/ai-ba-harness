# `/review`: a read-only quality report

You check a requirement document, a Jira issue, or the knowledge base itself, and report what's
wrong, graded by severity. You change nothing except the report file (and, for `/review kb`, the
generated index and registers). Fixes happen only when the BA asks.

## Before anything

Read `PROJECT-PROFILE.md`, `knowledge/_meta/conventions.md`, `knowledge/glossary.md`,
`knowledge/stakeholders.md`, `knowledge/raid.md`, and the pages and questions the target cites. For a
document, also `templates/requirement.md` and the definition of ready in `templates/jira/story.md`.
`git pull --ff-only` first.

## Input

| Argument | Target |
|---|---|
| A path to a `requirement.md` | That document |
| A Jira key | That issue (read with `getJiraIssue`; its children with `searchJiraIssuesUsingJql "parent = <key>"`) |
| `kb` | The knowledge base |

## Documents and Jira issues

Run the rule-based checks first, then the judgement checks. Every finding has an ID (`F-01`, `F-02`,
...), cites where it is (section, story or acceptance criterion, or Jira field) and says how to fix
it. The vague-word and statement checks apply to requirements, stories and criteria, not to the
Clarifications log.

### What "blocked" means

- A **criterion is blocked** while a question listed against it (`Q-x (blocks AC-2)`) is open.
- A **story is blocked** when a question blocks the whole story, or when what is left without its
  blocked criteria no longer meets the definition of ready (for example the only permission path
  is the blocked one).
- An FR marked `pending Q-x` blocks the criteria that test it; the story lists that question
  against them. A question marked `(non-blocking)` by the BA blocks nothing.

Blocked items aren't graded as findings: they're listed under "Blocked", with the question and who
can answer it. A requirement whose only problems are blocked stories can still be ready for the rest.

### Rule-based checks

| Check | Severity if failed |
|---|---|
| Every story has the "As a … I want … so that …" form | major |
| Every story has at least two Given/When/Then acceptance criteria | major |
| A failure or permission path is covered wherever a user can be refused, enter something invalid, or find nothing | major |
| Each FR and NFR is one testable statement. A list of values ("green, amber or red") or of roles is fine; two separate behaviours joined by "and" are not | major |
| NFRs are in EARS form with a measure, and each is tested by at least one story's criterion | minor |
| No vague words from profile section 7 without a measure | minor |
| IDs present and unique (FR, NFR, ST, AC) | minor |
| Documents: `fix_version` set (a release, or `unscheduled`). Jira issues: fix version and parent epic set. For a document, the epic is created by `/backlog` | major |
| Every `BR-`, `Q-`, `DEC-`, `CAP-` and `A-` cited exists in the knowledge base. Provisional IDs (`Q-new-1`) during `/requirements`' pre-check are reported as "pending staging" instead | critical |
| Every FR's status is `agreed` or `pending Q-x` in the FR table's Status column, and each pending question is open | major (minor for a document written before the Status column, with the marker elsewhere) |
| Every assumption a requirement or criterion relies on has an `A-` row in `raid.md`. An assumption about product behaviour should be a question instead, with the FR pending | major |

### Judgement checks

| Check | Severity if failed |
|---|---|
| A requirement or outcome contradicts a confirmed or approved rule, term or decision | critical (minor when it's only wording in a Given) |
| Uses a term differently from the glossary | major |
| Story fails INVEST: not valuable on its own, too big to estimate, not testable. Order dependencies between stories of one epic are fine when stated | major |
| Missing paths: errors, permissions, empty states, limits, concurrency | major |
| Likely duplicate of an existing Jira issue. Search the summary terms with `searchJiraIssuesUsingJql` in the profile's projects. Without Atlassian, say the check wasn't run; it doesn't change the verdict, and `/backlog` runs its own | major |
| Acceptance criteria describe UI steps instead of behaviour | minor |

### Verdict

- **Ready:** no critical or major findings. Every story that isn't blocked meets the definition of
  ready.
- **Not ready:** anything else.

Either way, list the ready stories (what `/backlog` can create now) and the blocked ones with their
questions.

### Output

For a document, write `requirements/<slug>/review.md`, replacing any previous review. It starts with
these properties: `type: review`, `id: REVIEW-<slug>`, `title: Review of <requirement title>`,
`owner` (the reviewer's role), `verdict`, `reviewed_on`, `sources` (the requirement's `REQ-` ID).
Then:
- the date and the verdict;
- counts by severity;
- the findings table (ID, severity, where, finding, fix);
- the checks that couldn't run, and why;
- the ready stories, and the blocked stories with their questions.

Commit it: `req: review <slug> <verdict>`, staging only that file. Ask before pushing.

For a Jira issue, show the report in the chat only.

If the verdict is ready, or the BA accepts the remaining findings (record that in `review.md`), and
the document is still `draft`, ask the BA whether to set it to `confirmed` (the status `/backlog`
needs). After a sign-off changes the document (pending FRs become agreed), run `/review` again
before `/backlog`.

After the report, offer to fix the document. Fixes that only change the document's wording are
applied as a diff after a yes, then the review runs again. Fixes that need new or changed
knowledge (a question, an assumption, a rule) go through `/requirements` (an update) or `/intake`.

## `/review kb`

1. **The mechanical checks.** Run `python tools/kb.py check` when Python is available. It covers
   properties, file names, IDs, rules, links and anchors, IDs cited but not defined, overdue
   questions and actions, old drafts and staging files, and generated files out of date. Without
   Python, check those by hand.
2. **The judgement checks,** which no script can do:
   - contradictions between pages: the same rule stated differently, or two pages giving different
     values for the same thing;
   - a cited ID that exists but doesn't say what the citing page claims (a callout that cites
     `ACT-001` for a different action, a rule cited for the wrong behaviour);
   - glossary terms used in pages with a different meaning;
   - a confirmed page whose key sections all say "not known yet": worth an open question;
   - rules whose wording leaves out how something is counted or measured (calendar or working days,
     a time zone, what "overdue" means), with no question tracking it;
   - business areas from profile section 4 with no capability or process page yet: gaps to fill
     through `/kb-seed` or elicitation.
3. **Questions to chase.** Open questions grouped by the role in `asked_of`, overdue first. For each
   role, one short message they can answer: each question in a sentence, what it blocks, and the due
   date. Show the drafts in the chat for the BA to send; never send anything.
4. **Rebuild** `index.md`, `business-rules.md`, `decisions.md` and `open-questions.md`:
   `python tools/kb.py rebuild`, or by hand to conventions section 12. Show the counts and the
   diff. Commit only the rebuilt files (`kb: review kb rebuild index`), and ask before pushing.

## Never

- Change the target document or the Jira issue without the BA asking.
- Edit knowledge pages during `/review kb`; only the generated files are rebuilt. Problems in pages
  are reported, and fixed through `/intake` or by the BA.
