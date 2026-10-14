---
type: review
id: REVIEW-inspection-scheduling-and-dashboard
title: Review of Inspection scheduling and dashboard
owner: Lead BA
verdict: not-ready
reviewed_on: 2026-10-20
sources: [REQ-inspection-scheduling-and-dashboard]
---

# Review of Inspection scheduling and dashboard

Reviewed on 2026-10-20, after the Product owner's sign-off of the same day (SRC-007) turned every
pending FR to `agreed`. The document is `approved` (Product owner, 2026-10-20).

**Verdict: not ready.** Three major findings, on ST-03, ST-04 and ST-05. ST-01 and ST-02 are ready.

## Counts

| Severity | Findings |
|---|---|
| Critical | 0 |
| Major | 3 |
| Minor | 3 |

## Findings

| ID | Severity | Where | Finding | Fix |
|---|---|---|---|---|
| F-01 | major | FR-017; ST-04 | The order among overdue vehicles is not specified: FR-017 says only "overdue vehicles first", and ST-04 AC-3 checks only that overdue vehicles come before the others. The sign-off left this open as [Q-018](../../knowledge/questions/Q-018-order-of-overdue-vehicles-on-the-dashboard.md) (open, blocks CAP-003), but the document doesn't list Q-018 anywhere, so nothing marks ST-04 as waiting on it. FR-017 also doesn't say how vehicles with the same next due date, or several "Not scheduled" vehicles, are ordered | `/requirements` update: list Q-018 against ST-04 (blocking a new criterion for two overdue vehicles, or non-blocking if the BA accepts ST-04 without it) and in the Open questions table. Ask the Product owner about ties through `/intake` (add it to Q-018 or a new question) |
| F-02 | major | ST-03, ST-04 | No empty state: nothing says what the dashboard shows when there are no vehicles to list (the user can "find nothing") | `/requirements` update: add a criterion to ST-03, for example "Given no vehicles, When a transport manager opens the dashboard, Then it shows that there are no vehicles", once the Product owner confirms the wording through `/intake` (a question, as it is product behaviour) |
| F-03 | major | ST-03; ST-05 AC-1 | Which vehicles a user sees is not stated: ST-05 AC-1 says a compliance officer sees "every vehicle's inspection status", and ST-03 doesn't say whose vehicles are listed. The product serves several operators (profile section 4, `tenancy-and-access`: "Operators, users, roles"), and the knowledge base has nothing on whether a user sees only their own operator's vehicles. That is a missing permission path | `/intake` a question to the Product owner (which vehicles a transport manager and a compliance officer see on the dashboard); then `/requirements` update ST-03 and ST-05 AC-1 ("every vehicle of their operator", or as answered) with a criterion that another operator's vehicles are not shown |
| F-04 | minor | Current state; ST-02 to ST-05 "Open questions"; Open questions table | The document still lists Q-001, Q-002 and Q-012 to Q-016 as open, with due dates, "proposed answer" notes and "(blocks AC-x)" markers, although the sign-off answered them all on 2026-10-20. They block nothing now, but `/backlog` would copy these lines into the stories' "Open questions" in Jira | `/requirements` update: replace them with the answers (or "None"), and keep Q-003, Q-011, Q-017 and the new Q-018 and Q-019 |
| F-05 | minor | FR table "Rules" column; ST-02 to ST-05 "Business rules" | The rules the sign-off created aren't cited: FR-006 to FR-010 and FR-015 to FR-019 say "None", and the stories' Business rules lines name only BR-001 to BR-004. The approved rules are BR-008 (FR-006), BR-009 (FR-009), BR-010 (FR-007, FR-019), BR-011 (FR-008), BR-012 (FR-010), BR-013 (FR-013), BR-014 (FR-014), BR-015 (FR-015), BR-016 (FR-016), BR-017 (FR-017) and BR-018 (FR-018) | `/requirements` update: fill the Rules column and each story's Business rules line with these IDs |
| F-06 | minor | FR-008; ST-02, ST-03 | [Q-019](../../knowledge/questions/Q-019-measuring-a-vehicle-on-its-due-date.md) (whether a vehicle is measured against its due date on that day; open, non-blocking) touches FR-008 but isn't listed in the document | `/requirements` update: list Q-019 as non-blocking against ST-02 and ST-03, and in the Open questions table |

Rule-based checks with no findings: story form, at least two criteria per story, a failure or
permission path for refusals and invalid input (ST-01 AC-3, AC-4; ST-05 AC-2, AC-3), one testable
statement per FR, vague words (none found outside the Clarifications), IDs present and unique,
`fix_version` (2026.12), every cited `BR-`, `Q-`, `CAP-` and `ENT-` exists, every FR `agreed`, no
assumptions relied on. Every criterion's dates were checked against BR-003, BR-004 and BR-008 to
BR-017 and agree with them. There are no NFRs, so the EARS check had nothing to check; the document
says no source gives a measure.

## Checks that couldn't run

- **Likely duplicates in Jira:** not run, because the Atlassian tools aren't available in this
  session. It doesn't change the verdict; `/backlog` runs its own duplicate search.

## Ready stories

What `/backlog` can create now:

- **ST-01** Set a vehicle's inspection interval and anchor date (Q-017 and Q-011 are non-blocking)
- **ST-02** Work out each vehicle's next inspection due date (its questions Q-014, Q-001 and Q-002
  are answered; Q-003 is non-blocking)

## Blocked stories

None. Every question the document lists against a story or criterion is either answered by the
sign-off (Q-001, Q-002, Q-012 to Q-016) or marked non-blocking by the BA (Q-003, Q-011, Q-017).

## Not ready, for findings (not blocked)

- **ST-03** Show each vehicle's inspection status on the dashboard: F-02, F-03
- **ST-04** List vehicles on the dashboard by urgency: F-01, F-02
- **ST-05** Let compliance officers see the dashboard read-only: F-03

The BA declined the offer to fix the document ("no, just the report").
