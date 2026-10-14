---
type: review
id: REVIEW-inspection-due-dates-and-dashboard-banding
title: Review of Inspection due dates and dashboard banding
verdict: not-ready
reviewed_on: 2026-10-15
sources: [REQ-inspection-due-dates-and-dashboard-banding]
---

# Review of Inspection due dates and dashboard banding

**Date:** 2026-10-15

**Document:** [requirement.md](requirement.md), status `draft`, fix version `2026.12`.

**Verdict:** not ready.

| Severity | Count |
|---|---|
| Critical | 5 |
| Major | 8 |
| Minor | 6 |

Not checked: the likely-duplicate search in Jira, because the Atlassian connection wasn't available.
Run `/review` again once it is, before `/backlog`.

Every cited `BR-`, `Q-`, `DEC-` and `CAP-` exists in the knowledge base, every FR marked
`pending Q-x` names an open question, and every story relying on one lists it under its open
questions. The worked dates in ST-02, ST-03 and ST-04 are arithmetically right.

## Findings

| ID | Severity | Where | Finding | Fix |
|---|---|---|---|---|
| F-01 | critical (ST-05) | ST-05; FR-011 | Q-004 (open, due 2026-10-29) blocks the whole story; FR-011 is pending Q-004. | Get the Product owner's answer to Q-004, or their sign-off of the requirement, which answers it with the proposed "Not scheduled". Keep ST-05 out of `/backlog` until then. |
| F-02 | critical (ST-01) | ST-01 AC-2, AC-3; FR-002, FR-003 | Q-007 blocks AC-2 and Q-008 blocks AC-3. Those are the story's failure and permission paths: without them only AC-1 is left, under the two criteria the definition of ready asks for. | Get Q-007 and Q-008 answered (or the requirement signed off). |
| F-03 | critical (ST-02) | ST-02 AC-2, AC-3; FR-005, FR-006 | Q-006 blocks AC-2 and AC-3; AC-1 alone is under two criteria. | Get Q-006 answered (or the requirement signed off). |
| F-04 | critical (ST-03) | ST-03 AC-1, AC-2; FR-007, FR-003 | Q-005 blocks AC-1 and Q-008 blocks AC-2, so no criterion is left. | Get Q-005 and Q-008 answered (or the requirement signed off). |
| F-05 | critical (ST-04) | ST-04 AC-5; FR-009, FR-010 | Q-008 blocks AC-5, the story's only permission path. Without it ST-04 keeps four criteria (AC-1 to AC-4 hold under every answer Q-008 lists) but no permission path. | Get Q-008 answered (or the requirement signed off); see also F-10. |
| F-06 | major | FR-004; Assumptions, second bullet | The first due date being the anchor date plus one interval is product behaviour, read from DEC-001 by the Lead BA. It is an assumption with no `A-` ID, not in `raid.md`, with no owner or date, yet FR-004 isn't marked pending and ST-02 AC-1, ST-03 AC-1 and every example date depend on it. | Stage it as an `A-` row through `/intake`, or add it to a question for the Product owner (Q-006 fits) and mark FR-004 `pending Q-x`; list it under ST-02's and ST-03's open questions. |
| F-07 | major | FR-002; ST-01 | FR-002 joins several requirements (unit in weeks, whole numbers, at least 1, no maximum), and "no maximum until the regulator's guidance (ACT-001) sets one" depends on a future event, so it can't be tested as written. Only the minimum has a criterion; a value that isn't a whole number (2.5 weeks) has none. | Split into: the unit is whole weeks; the interval is at least 1 week; any whole number of weeks from 1 upward is accepted. Record the future maximum as a dependency on ACT-001. Add a criterion for a non-whole value, blocked by Q-007. |
| F-08 | major | FR-010; ST-04 AC-5 | "Compliance officers can only view the dashboard" reads two ways: read-only on the dashboard, or nothing but the dashboard. No FR says what anyone can change from the dashboard, so "can't change anything from it" has nothing to test against. | Reword: "Compliance officers can see the dashboard but can't change anything from it", and state what, if anything, a transport manager can change from it. Still pending Q-008. |
| F-09 | major | Goal; ST-02 (summary and AC-1 to AC-3) | The goal and ST-02 say the transport manager can see each vehicle's next due date, but no FR says where the date is shown (FR-008 shows only the band). ST-02's criteria start "When its next due date is worked out", which no user does or observes, so the story isn't testable as written. | Add an FR for where the next due date is shown (product behaviour: a pending proposal with a question to the Product owner), and rewrite the criteria as "When the transport manager opens <where it is shown>, Then the next due date shown is …". |
| F-10 | major | ST-04; FR-009 | Missing permission path: FR-009 says who can see the dashboard, but nothing says who can't (technicians, drivers). Q-008's page notes those roles aren't covered. | Add the other roles to Q-008, an FR "No other role can see the dashboard" pending Q-008, and a criterion "a driver can't open the dashboard" blocked by Q-008. |
| F-11 | major | ST-02; FR-005 | Missing path: an inspection that satisfies no due date (a second inspection in the same period, one done on or before the previous due date, one before the anchor date). FR-005 only says what happens when one does. Q-006's page also asks about an inspection done on the previous due date itself; the document doesn't carry that. | Add these cases to Q-006 and a criterion for them, blocked by Q-006. |
| F-12 | major | ST-03; FR-007 | Missing paths that Q-005's page lists itself: an interval change after inspections were recorded (which recalculated due dates they satisfy), and a change that puts the recalculated next due date in the past (red at once?). AC-1 covers only a vehicle with no inspection. | Add criteria for both, blocked by Q-005, and make sure Q-005 asks both. |
| F-13 | major | ST-04; ST-05 | Missing empty and partial states: a dashboard with no vehicles, and a vehicle with an anchor date but no interval (CAP-002 needs both; ST-05 covers only a missing anchor date, and its AC-2 doesn't say whether the vehicle has an interval). | Add criteria for both, or put them out of scope with a reason. What the dashboard shows is the Product owner's: add it to Q-004. |
| F-14 | minor | Properties, `area` | `area: inspections`, but the scope includes CAP-001 and FR-001 to FR-003, which are in the vehicles area. The template asks for a list when a document spans several areas. | `area: [inspections, vehicles]`. |
| F-15 | minor | Functional requirements table | The table has no Status column (the current template has one: `agreed` or `pending Q-x`). The pending markers sit in the Source column, and FR-001, FR-004 and FR-008 carry no status. | Add the Status column, move each `pending Q-x` into it, and mark the rest `agreed` (FR-004 pending, see F-06). |
| F-16 | minor | NFR-001; ST-04 | NFR-001 isn't tied to any story's acceptance criterion, and its measure doesn't say whether "under 3 seconds" applies to every load or a percentile, or under what conditions. | Add a criterion to ST-04 for a 2,000-vehicle fleet loading in under 3 seconds. Agree the percentile and conditions with the Engineering lead, and with the Product owner if it changes what DEC-003 means. |
| F-17 | minor | ST-02 AC-3 | "Overdue since 2026-12-14": under BR-005 the vehicle is amber on its due date and red (overdue) from the day after, so it is overdue since 2026-12-15. The outcome isn't affected. | "Given that vehicle, with next due date 2026-12-14 and no inspection recorded since". |
| F-18 | minor | FR-008; ST-04 AC-1 to AC-4 | "Today" has no time zone, so around midnight a vehicle's band depends on whose date counts (the customer's or the system's). | State the time zone (for example the customer organisation's), or raise a question to the Product owner. |
| F-19 | minor | ST-03 AC-2 | Repeats ST-01 AC-3 (a compliance officer can't change the interval); "the next due date stays as it was" follows from it. | Keep the permission criterion in ST-01 and give ST-03 a failure path of its own, for example an invalid new interval refused with the due date unchanged. |

## Ready stories

None.

Stories that would be ready without a blocked criterion: none. ST-04 comes closest: without AC-5
it has four criteria and its rules exist, but no permission path (F-05, F-10).

Most of what blocks the stories is the five open questions to the Product owner (Q-004 to Q-008,
due 2026-10-29). The Product owner's sign-off of this requirement would answer all of them with
the proposed answers. The major findings need fixing in the document as well.
