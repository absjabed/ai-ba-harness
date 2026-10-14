# `/review`: a read-only quality report

You check a requirement document, a Jira issue, or the knowledge base itself, and report what's
wrong, graded by severity. You change nothing except the report file (and, for `/review kb`, the
generated index and registers). Fixes happen only when the BA asks.

## Before anything

Read `PROJECT-PROFILE.md` and `knowledge/_meta/conventions.md`.

## Input

| Argument | Target |
|---|---|
| A path to a `requirement.md` | That document |
| A Jira key | That issue (read with `getJiraIssue`; its children with `searchJiraIssuesUsingJql "parent = <key>"`) |
| `kb` | The knowledge base |

## Documents and Jira issues

Run the rule-based checks first, then the judgement checks. Every finding cites where it is (section,
story or acceptance criterion, or Jira field) and says how to fix it.

### Rule-based checks

| Check | Severity if failed |
|---|---|
| Every story has the "As a … I want … so that …" form | major |
| Every story has at least two Given/When/Then acceptance criteria | major |
| A failure or permission path is covered where the story has one | major |
| Each FR and NFR is one statement (no "and"/"or" joining two requirements) and testable | major |
| NFRs are in EARS form with a measure | minor |
| No vague words from profile section 7 without a measure | minor |
| IDs present and unique (FR, NFR, ST, AC) | minor |
| Documents: `fix_version` set (a release, or `unscheduled`). Jira issues: fix version and parent epic set | major |
| Every `BR-`, `Q-`, `DEC-` and `CAP-` cited exists in the knowledge base | critical |

### Judgement checks

| Check | Severity if failed |
|---|---|
| Contradicts a confirmed or approved rule, term or decision | critical |
| Uses a term differently from the glossary | major |
| Story fails INVEST: not independent, not valuable on its own, too big to estimate, not testable | major |
| Missing paths: errors, permissions, empty states, limits, concurrency | major |
| Likely duplicate of an existing Jira issue. Search the summary terms with `searchJiraIssuesUsingJql` in the profile's projects | major |
| Open question still blocking a story | critical for that story |
| Acceptance criteria describe UI steps instead of behaviour | minor |

### Verdict

- **Ready:** no critical or major findings. Every story meets the definition of ready
  (`templates/jira/story.md`).
- **Not ready:** anything else. List the stories that are ready on their own, because `/backlog` can
  create those.

### Output

For a document, write `requirements/<slug>/review.md`, replacing any previous review. It starts with
the properties in conventions section 7 (`type: review`, `id: REVIEW-<slug>`, `title`, `verdict`,
`reviewed_on`, `sources`), then:
- the date;
- the verdict;
- counts by severity;
- the findings table (ID, severity, where, finding, fix);
- the list of ready stories.

For a Jira issue, show the report in the chat only.

If the verdict is ready and the document is still `draft`, ask the BA whether to set it to `confirmed`
(the status `/backlog` needs).

After the report, offer to fix the document. If the BA agrees, apply the fixes they choose as a diff,
then run the review again.

## `/review kb`

Check the knowledge base and report:

1. Broken links: every relative link resolves to an existing file and heading.
2. Pages missing from `index.md`, and index entries for pages that don't exist.
3. Pages breaking the file-name or property rules (missing `type`, `id`, `title` or `status`; unknown
   status; a superseded page without `superseded_by`).
4. Drafts older than `draft_age_days`.
5. Open questions past their `due` date.
6. Staging files older than a day.
7. Contradictions between pages: the same rule stated differently, or two pages giving different
   values for the same thing.
8. `BR-` IDs cited in `requirements/` or in `trace/map.csv` that no page defines.
9. Glossary terms used in pages with a different meaning.

Then rebuild `index.md`, `business-rules.md`, `decisions.md` and `open-questions.md` from the pages'
properties (conventions, section 12). Show the counts and the rebuilt files' diff. Commit only the
rebuilt files (`kb: review kb rebuild index`), and ask before pushing.

## Never

- Change the target document or the Jira issue without the BA asking.
- Edit knowledge pages during `/review kb`; only the generated files are rebuilt. Problems in pages
  are reported, and fixed through `/intake` or by the BA.
