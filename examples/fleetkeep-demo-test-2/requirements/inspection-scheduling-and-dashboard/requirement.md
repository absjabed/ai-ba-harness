---
type: requirement
id: REQ-inspection-scheduling-and-dashboard
title: Inspection scheduling and dashboard
status: draft
area: inspections
owner: Lead BA
jira_epic:
fix_version: 2026.12
approved_by:
approved_on:
delivered_on:
sources: [SRC-001, SRC-002, SRC-005, SRC-006, SRC-007, SRC-008, DEC-003, SRC-009]
created: 2026-10-18
updated: 2026-10-22
---

# Inspection scheduling and dashboard

## Goal

Transport managers can give each vehicle its own safety inspection schedule and see, on one
dashboard, which vehicles are overdue or close to their next inspection, so the operator keeps its
fleet road-legal. Compliance officers can check the same dashboard without changing anything.

## Current state

What the knowledge base says today:

- Each vehicle has its own safety inspection interval in whole weeks; there is no fleet-wide
  interval (BR-001, [CAP-001](../../knowledge/domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md)).
  The regulator guidance requires the operator to decide and write down an interval for each vehicle
  ([SRC-002](../../knowledge/sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)).
- Only a transport manager sets or changes a vehicle's inspection interval or anchor date (BR-002,
  CAP-001; [ENT-001](../../knowledge/entities/ENT-001-transport-manager.md)).
- Each due date is the anchor date plus a whole number of intervals, and doing an inspection early or
  late doesn't move the schedule (BR-003,
  [CAP-002](../../knowledge/domains/inspections/CAP-002-calculating-next-inspection-due-date.md);
  T-001 in the [glossary](../../knowledge/glossary.md#anchor-date)). The first due date is the anchor
  date plus one interval (BR-008). An inspection meets every unmet due date on or before its day, or
  else the first due date after it (BR-010), and the next due date is the first due date after today
  that no inspection has met (BR-011).
- A vehicle is overdue from the day after a due date that no inspection has met, with no grace
  period (BR-009), and stays overdue until an inspection meets that due date (BR-012).
- The dashboard bands each vehicle green when its next due date is more than 21 days away, amber when
  it is 21 days away or less, and red when the inspection is overdue (BR-019,
  [CAP-003](../../knowledge/domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md)).
  The Product owner changed the amber band from 14 to 21 days on 2026-10-22
  ([DEC-003](../../knowledge/decisions/DEC-003-amber-starts-21-days-before-due-date.md)), replacing
  BR-004. An overdue vehicle shows red whatever its next due date (BR-013); the days are calendar days
  (BR-014); a vehicle with no anchor date shows grey, "Not scheduled" (BR-015).
- The dashboard shows each scheduled vehicle's next due date beside its status (BR-016), lists
  overdue vehicles first, then the other scheduled vehicles by next due date, then the vehicles that
  are not scheduled (BR-017), and only transport managers and compliance officers can see it
  (BR-018; [ENT-002](../../knowledge/entities/ENT-002-compliance-officer.md)).
- The regulator guidance calls an inspection done after its due date "late", has no grace period, and
  requires late inspections to be visible to an auditor (T-003, SRC-002).
- Inspections are recorded through
  [CAP-004](../../knowledge/domains/inspections/CAP-004-recording-a-safety-inspection.md), with a brake
  performance test (BR-005).

Open questions that touch this area:

- [Q-018](../../knowledge/questions/Q-018-order-of-overdue-vehicles-on-the-dashboard.md): the order
  among overdue vehicles on the dashboard (Product owner).
- [Q-019](../../knowledge/questions/Q-019-measuring-a-vehicle-on-its-due-date.md): whether a vehicle is
  measured against its due date on the day it is due (Product owner).
- [Q-017](../../knowledge/questions/Q-017-refused-intervals-and-anchor-dates.md): which intervals and
  anchor dates the product refuses (Product owner).
- [Q-003](../../knowledge/questions/Q-003-inspection-rules-for-vor-vehicles.md): how the inspection
  rules apply to VOR vehicles (Product owner).
- [Q-005](../../knowledge/questions/Q-005-how-an-auditor-sees-late-inspections.md): how an auditor
  sees late inspections (Product owner).
- [Q-011](../../knowledge/questions/Q-011-what-happens-when-a-vehicle-is-re-registered.md): what
  happens to a vehicle's record and schedule when it is re-registered (Product owner; R-003 in the
  [RAID log](../../knowledge/raid.md)).

## Scope

**In:**
- Setting and changing each vehicle's inspection interval and anchor date.
- Working out each vehicle's due dates and next due date from its anchor date.
- Showing each vehicle's inspection status on the dashboard (green, amber, red, or not scheduled),
  the order the dashboard lists vehicles in, which vehicles each user sees, what an empty dashboard
  shows, and who can see it.

**Out:**
- VOR vehicles: how the inspection rules apply to them is Q-003, still open.
- Brake performance tests (Q-009, Q-010).
- Recording a safety inspection (CAP-004); this requirement uses the inspections recorded there.
- Notifications about due or overdue inspections.
- Re-registering a vehicle (Q-011, R-003).

## Stakeholders

| Role | Interest | Decides |
|---|---|---|
| Product owner | A product operators trust | Product behaviour and business rules, including every proposal pending in this document; release content |
| Compliance adviser | That the product reflects the regulator guidance | How the regulator guidance is read for the product |
| Lead BA | This document | Scope, story split and fix version of this document; its wording |
| Engineering lead | Technical design | Technical approach |
| Transport manager (product role, ENT-001) | Keeping each vehicle's inspections on time | Nothing in the product's rules; sets each vehicle's interval and anchor date |
| Compliance officer (product role, ENT-002; not the Compliance adviser) | Checking the fleet's inspection status | Nothing in the product's rules |

## Functional requirements

| ID | Requirement | Source | Rules | Status |
|---|---|---|---|---|
| FR-001 | Each vehicle has its own safety inspection interval, a whole number of weeks; there is no fleet-wide interval. | [CAP-001](../../knowledge/domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md) | BR-001 | agreed |
| FR-002 | Only a transport manager can set or change a vehicle's inspection interval or anchor date. | CAP-001, ENT-001 | BR-002 | agreed |
| FR-003 | The product refuses an inspection interval that is not a whole number of weeks. | CAP-001 | BR-001 | agreed |
| FR-004 | Each of a vehicle's due dates is its anchor date plus a whole number of its inspection intervals. | [CAP-002](../../knowledge/domains/inspections/CAP-002-calculating-next-inspection-due-date.md) | BR-003 | agreed |
| FR-005 | Recording an inspection early or late doesn't change the vehicle's due dates. | CAP-002 | BR-003 | agreed |
| FR-006 | A vehicle's first due date is its anchor date plus one inspection interval; the anchor date itself is not a due date. | SRC-006 (recommended, accepted by Lead BA), SRC-007 | BR-008 | agreed |
| FR-007 | An inspection meets every unmet due date on or before the day it is done. | SRC-006 (recommended, accepted by Lead BA), SRC-007 | BR-010 | agreed |
| FR-008 | A vehicle's next due date is the first due date after today that no inspection has met. | SRC-006 (Lead BA's proposed answer), SRC-007 | BR-011 | agreed |
| FR-009 | A vehicle is overdue from the day after a due date that no inspection has met; there is no grace period. | SRC-006 (Lead BA's proposed answer), SRC-002, SRC-007 | BR-009 | agreed |
| FR-010 | A vehicle stays overdue until an inspection is recorded that meets the missed due date. | SRC-006 (Lead BA's proposed answer), SRC-007 | BR-012 | agreed |
| FR-011 | A vehicle with no anchor date has no due dates and no next due date. | CAP-002 (the anchor date is a required input) | BR-003 | agreed |
| FR-012 | The dashboard shows each vehicle's inspection status: green when its next due date is more than 21 days away, amber when it is 21 days away or less, red when the vehicle is overdue. | [CAP-003](../../knowledge/domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), DEC-003 | BR-019 | agreed |
| FR-013 | An overdue vehicle shows red whatever its next due date. | SRC-006 (follows from the Lead BA's proposed answer to Q-001), SRC-007 | BR-013 | agreed |
| FR-014 | The days to a vehicle's next due date are counted as calendar days. | SRC-006 (recommended, accepted by Lead BA), SRC-007 | BR-014 | agreed |
| FR-015 | A vehicle with no anchor date shows grey on the dashboard, labelled "Not scheduled". | SRC-006 (Lead BA's proposed answer), SRC-007 | BR-015 | agreed |
| FR-016 | The dashboard shows each scheduled vehicle's next due date beside its inspection status. | SRC-006 (recommended, accepted by Lead BA), SRC-007 | BR-016 | agreed |
| FR-017 | The dashboard lists overdue vehicles first, then the other scheduled vehicles by next due date (earliest first), then the vehicles that are not scheduled. | SRC-006 (Lead BA's proposed answer; placing "Not scheduled" last recommended, accepted by Lead BA), SRC-007 | BR-017 | agreed |
| FR-018 | Only transport managers and compliance officers can see the inspection dashboard. | SRC-006 (Lead BA's proposed answer), SRC-007 | BR-018 | agreed |
| FR-019 | An inspection done when no due date on or before its day is unmet meets the first due date after that day. | SRC-006 (recommended, accepted by Lead BA), SRC-007 | BR-010 | agreed |
| FR-020 | A user sees on the inspection dashboard only the vehicles of their own operator. | SRC-009 (recommended, accepted by Lead BA) | None | pending Q-020 |
| FR-021 | When there are no vehicles to list, the dashboard shows the message "No vehicles to show". | SRC-009 (recommended, accepted by Lead BA) | None | pending Q-021 |
| FR-022 | The dashboard lists overdue vehicles among themselves by their oldest missed due date, earliest first. | SRC-009 (recommended, accepted by Lead BA) | None | pending Q-018 |
| FR-023 | Vehicles the dashboard's order doesn't otherwise separate are listed by registration number, A to Z. | SRC-009 (recommended, accepted by Lead BA) | None | pending Q-022 |

## Non-functional requirements

None agreed yet. No source gives a measure for how quickly the dashboard loads or how up to date its
statuses must be.

## User stories

| Story | Summary | FR | Jira key |
|---|---|---|---|
| ST-01 | Set a vehicle's inspection interval and anchor date | FR-001, FR-002, FR-003 | |
| ST-02 | Work out each vehicle's next inspection due date | FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, FR-011, FR-019 | |
| ST-03 | Show each vehicle's inspection status on the dashboard | FR-009, FR-012, FR-013, FR-014, FR-015, FR-020, FR-021 | |
| ST-04 | List vehicles on the dashboard by urgency | FR-016, FR-017, FR-022, FR-023 | |
| ST-05 | Let compliance officers see the dashboard read-only | FR-002, FR-018, FR-020 | |

ST-02 needs ST-01 (a vehicle has an interval and anchor date); ST-03 and ST-04 need ST-02 (the next
due date and whether a vehicle is overdue).

### ST-01 Set a vehicle's inspection interval and anchor date

As a transport manager, I want to set and change each vehicle's inspection interval and anchor date,
so that every vehicle has its own inspection schedule.

**AC-1 Set a schedule**
- Given a vehicle with no inspection interval or anchor date, and the user is a transport manager
- When they set an interval of 6 weeks and an anchor date of 2026-09-07
- Then the vehicle has an inspection interval of 6 weeks and an anchor date of 2026-09-07

**AC-2 Change one vehicle's interval**
- Given two vehicles, each with an interval of 6 weeks, and the user is a transport manager
- When they change the first vehicle's interval to 8 weeks
- Then the first vehicle's interval is 8 weeks and the second vehicle's is still 6 weeks

**AC-3 Another role is refused**
- Given a vehicle with an interval of 6 weeks and an anchor date of 2026-09-07, and the user is a driver
- When they try to change the interval or the anchor date
- Then the change is refused, and the interval and anchor date are unchanged

**AC-4 Interval not in whole weeks**
- Given the user is a transport manager
- When they enter an interval of 6.5 weeks
- Then the interval is refused and the vehicle's interval is unchanged

**Business rules:** BR-001, BR-002

**Out of scope:** what happens to the schedule when a vehicle is re-registered (Q-011).

**Open questions:** Q-017 (non-blocking; its answer adds criteria for refused values), Q-011
(non-blocking; re-registration is out of scope)

### ST-02 Work out each vehicle's next inspection due date

As a transport manager, I want the product to work out each vehicle's next inspection due date from
its anchor date, so that I know when each vehicle must next be inspected.

**AC-1 First and later due dates**
- Given a vehicle with an anchor date of 2026-09-07 and an interval of 6 weeks
- When the product works out its due dates
- Then the first is 2026-10-19 and the next ones are 2026-11-30 and 2027-01-11

**AC-2 An early inspection doesn't move the schedule**
- Given a vehicle with due dates 2026-10-19, 2026-11-30 and 2027-01-11
- When an inspection is recorded on 2026-10-14
- Then the vehicle's due dates are still 2026-10-19, 2026-11-30 and 2027-01-11

**AC-3 An early inspection meets the coming due date**
- Given a vehicle with an anchor date of 2026-09-07 and an interval of 6 weeks (due dates 2026-10-19,
  2026-11-30 and 2027-01-11), none yet met, and today is 2026-10-14
- When an inspection is recorded on 2026-10-14
- Then the vehicle's next due date is 2026-11-30

**AC-4 A missed due date stays overdue**
- Given a vehicle with due dates 2026-10-19 and 2026-11-30, and no inspection has met 2026-10-19
- When today is 2026-10-20
- Then the vehicle is overdue, and its next due date is 2026-11-30

**AC-5 A late inspection ends the overdue**
- Given a vehicle with due dates 2026-10-19 and 2026-11-30, no inspection has met 2026-10-19, and
  today is 2026-11-02
- When an inspection is recorded on 2026-11-02
- Then the vehicle is no longer overdue, and its next due date is 2026-11-30

**AC-6 No anchor date**
- Given a vehicle with an interval of 6 weeks and no anchor date
- When the product works out its due dates
- Then the vehicle has no due dates and no next due date

**Business rules:** BR-001, BR-003, BR-008, BR-009, BR-010, BR-011, BR-012

**Out of scope:** VOR vehicles (Q-003); recording the inspection itself (CAP-004).

**Open questions:** Q-019 (non-blocking; the criteria follow BR-011 as signed off), Q-003
(non-blocking; VOR is out of scope)

### ST-03 Show each vehicle's inspection status on the dashboard

As a transport manager, I want to see each vehicle's inspection status on the dashboard, so that I can
see which vehicles are overdue or within 21 days of their next due date.

**AC-1 Green**
- Given today is 2026-10-18 and a vehicle that is not overdue, with its next due date on 2026-11-30
- When a transport manager opens the dashboard
- Then the vehicle shows green

**AC-2 Amber within 21 days**
- Given today is 2026-10-18, a vehicle that is not overdue with its next due date on 2026-11-08, and
  another that is not overdue with its next due date on 2026-11-09
- When a transport manager opens the dashboard
- Then the first vehicle shows amber and the second shows green

**AC-3 Red when overdue**
- Given today is 2026-10-18 and a vehicle whose due date 2026-10-17 no inspection has met, with its
  next due date on 2026-11-28
- When a transport manager opens the dashboard
- Then the vehicle shows red

**AC-4 Not scheduled**
- Given a vehicle with no anchor date
- When a transport manager opens the dashboard
- Then the vehicle shows grey, labelled "Not scheduled"

**AC-5 Another operator's vehicles are not shown**
- Given two operators, each with one vehicle, and the user is a transport manager of the first
- When they open the dashboard
- Then only the first operator's vehicle is listed

**AC-6 No vehicles to show**
- Given the user is a transport manager whose operator has no vehicles
- When they open the dashboard
- Then it shows the message "No vehicles to show"

**Business rules:** BR-009, BR-012, BR-013, BR-014, BR-015, BR-019

**Out of scope:** how a VOR vehicle shows (Q-003); notifications.

**Open questions:** Q-020 (blocks AC-5, AC-6), Q-021 (blocks AC-6), Q-019 (non-blocking; the
criteria follow BR-011 as signed off), Q-003 (non-blocking; VOR is out of scope)

### ST-04 List vehicles on the dashboard by urgency

As a transport manager, I want the dashboard to list overdue vehicles first and the rest by next due
date, so that the vehicles to inspect first are at the top.

**AC-1 Next due date shown**
- Given a vehicle with its next due date on 2026-11-30
- When a transport manager opens the dashboard
- Then the vehicle's row shows 2026-11-30 beside its status

**AC-2 Order**
- Given today is 2026-10-18 and four vehicles: A overdue with its next due date on 2026-11-28, B not
  overdue with its next due date on 2026-11-30, C not overdue with its next due date on 2026-10-25,
  and D with no anchor date
- When a transport manager opens the dashboard
- Then the vehicles are listed in the order A, C, B, D

**AC-3 Overdue before an earlier next due date**
- Given today is 2026-10-18, two overdue vehicles E and F with their next due dates on 2026-11-28 and
  2026-11-05, and a vehicle G that isn't overdue, with its next due date on 2026-10-20
- When a transport manager opens the dashboard
- Then E and F are both listed before G

**AC-4 Oldest missed due date first among overdue vehicles**
- Given today is 2026-10-18 and two overdue vehicles: H whose oldest missed due date is 2026-10-12,
  and J whose oldest missed due date is 2026-10-05
- When a transport manager opens the dashboard
- Then J is listed before H

**AC-5 Vehicles sharing a place are listed by registration number**
- Given two vehicles that are not overdue, both with their next due date on 2026-11-30, registered
  KX21 ABC and BD70 XYZ
- When a transport manager opens the dashboard
- Then BD70 XYZ is listed before KX21 ABC

**Business rules:** BR-016, BR-017

**Out of scope:** filtering or searching the dashboard.

**Open questions:** Q-018 (blocks AC-4), Q-022 (blocks AC-5)

### ST-05 Let compliance officers see the dashboard read-only

As a compliance officer, I want to see the inspection dashboard without being able to change any
vehicle's schedule, so that I can check the fleet's inspection status.

**AC-1 Compliance officer sees the dashboard**
- Given the user is a compliance officer
- When they open the inspection dashboard
- Then they see the dashboard, with each listed vehicle's inspection status

**AC-2 Compliance officer can't change a schedule**
- Given a vehicle with an interval of 6 weeks and an anchor date of 2026-09-07, and the user is a
  compliance officer
- When they try to change its interval or anchor date
- Then the change is refused, and the interval and anchor date are unchanged

**AC-3 Other roles are refused**
- Given the user is a driver
- When they try to open the inspection dashboard
- Then they are refused

**AC-4 Another operator's vehicles are not shown**
- Given two operators, each with one vehicle, and the user is a compliance officer of the first
- When they open the inspection dashboard
- Then only the first operator's vehicle is listed

**Business rules:** BR-002, BR-018

**Out of scope:** what other screens a compliance officer can see.

**Open questions:** Q-020 (blocks AC-4)

## Assumptions

None. Every gap found while writing is about product behaviour, so it is a question to the Product
owner instead.

## Open questions

| Question | Blocks | Asked of | Due |
|---|---|---|---|
| [Q-020](../../knowledge/questions/Q-020-which-vehicles-a-user-sees-on-the-dashboard.md) Which vehicles a user sees on the inspection dashboard (proposed answer: FR-020) | ST-03 AC-5, AC-6; ST-05 AC-4 | Product owner | 2026-11-05 (proposed) |
| [Q-021](../../knowledge/questions/Q-021-dashboard-with-no-vehicles-to-list.md) What the dashboard shows when there are no vehicles to list (proposed answer: FR-021) | ST-03 AC-6 | Product owner | 2026-11-05 (proposed) |
| [Q-018](../../knowledge/questions/Q-018-order-of-overdue-vehicles-on-the-dashboard.md) In what order the dashboard lists overdue vehicles (proposed answer: FR-022) | ST-04 AC-4 | Product owner | 2026-11-03 |
| [Q-022](../../knowledge/questions/Q-022-order-of-vehicles-sharing-a-place.md) How the dashboard orders vehicles its order doesn't separate (proposed answer: FR-023) | ST-04 AC-5 | Product owner | 2026-11-05 (proposed) |
| [Q-019](../../knowledge/questions/Q-019-measuring-a-vehicle-on-its-due-date.md) Whether a vehicle is measured against its due date on that day | Nothing yet (non-blocking; the criteria follow BR-011 as signed off) | Product owner | 2026-11-03 |
| [Q-017](../../knowledge/questions/Q-017-refused-intervals-and-anchor-dates.md) Which inspection intervals and anchor dates the product refuses, and whether both must be set together (no proposed answer) | Nothing yet (non-blocking; recommended, accepted by Lead BA) | Product owner | 2026-11-01 |
| [Q-003](../../knowledge/questions/Q-003-inspection-rules-for-vor-vehicles.md) How inspection rules apply to VOR vehicles | Nothing here (non-blocking; out of scope) | Product owner | 2026-10-29 |
| [Q-011](../../knowledge/questions/Q-011-what-happens-when-a-vehicle-is-re-registered.md) What happens to a vehicle's record and schedule when it is re-registered | Nothing here (non-blocking; out of scope) | Product owner | 2026-10-31 |

One sign-off of this version by the Product owner answers Q-020, Q-021, Q-018 and Q-022 with
their proposed answers.

## Conflicts with the knowledge base

None. FR-012 follows the Product owner's change of 2026-10-22 (DEC-003), which superseded BR-004
(14 days) with BR-019 (21 days); the version of this document signed off on 2026-10-20 still said 14
days.

## Success measures

- None agreed yet.

## Clarifications

### Session 2026-10-18

Round 1:

- Q: What is in scope? → A: In: per-vehicle intervals, the next due date from the anchor date, and
  the dashboard banding. Out: VOR (Q-003 open), brake tests, notifications, re-registration (Lead BA).
  Recording a safety inspection (CAP-004) stays out as well (recommended, accepted by Lead BA). With
  VOR and re-registration out, Q-003 and Q-011 don't block this document (recommended, accepted by
  Lead BA).
- Q: (Q-001) When a due date passes without an inspection, which due date is next? → A: "The next due
  date is the first one after today that hasn't been met by an inspection; a missed one stays overdue
  until an inspection is recorded." (Lead BA; a proposal for the Product owner, pending Q-001)
- Q: (Q-002) Is there a grace period before an inspection is overdue? → A: "No grace period; follow
  the regulator." (Lead BA; a proposal for the Product owner, pending Q-002)
- Q: Who can see the dashboard? → A: Transport managers and compliance officers; compliance officers
  read-only (Lead BA; a proposal for the Product owner, pending Q-012). That compliance officers
  can't change intervals or anchor dates already follows from BR-002.
- Q: How does the dashboard show a vehicle with no anchor date? → A: "Show it grey, 'Not scheduled'"
  (Lead BA; a proposal for the Product owner, pending Q-013).

Not asked, decided from the knowledge base: who sets intervals and anchor dates (only a transport
manager, BR-002).

Round 2:

- Q: (Q-001) Which due date does an inspection meet? → A: Every unmet due date on or before the day
  it is done; when there is none, the first due date after that day (recommended, accepted by Lead
  BA; a proposal for the Product owner, pending Q-001).
- Q: Is the anchor date itself a due date? → A: No; the first due date is the anchor date plus one
  interval (recommended, accepted by Lead BA; a proposal for the Product owner, pending Q-014).
- Q: How are the 14 days before a due date counted? → A: Calendar days (recommended, accepted by Lead
  BA; a proposal for the Product owner, pending Q-015).
- Q: What does the dashboard show for each vehicle, and in what order? → A: "Overdue first, then by
  next due date" (Lead BA). Showing the next due date beside the status, and listing "Not scheduled"
  vehicles last, recommended, accepted by Lead BA. A proposal for the Product owner, pending Q-016.
- Q: Which fix version? → A: 2026.12 (Lead BA).

Round 3:

- Q: How should the work be split into stories? → A: Five stories, ST-01 to ST-05 (recommended,
  accepted by Lead BA).

Raised by the pre-check, with no answer from the BA:

- Which inspection intervals (for example 0 weeks) and anchor dates the product refuses, and whether
  both must be set together: an open question for the Product owner (Q-017), non-blocking
  (recommended, accepted by Lead BA).

The Product owner signed off this document on 2026-10-20, with every proposal pending in it
([SRC-007](../../knowledge/sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)).

### Session 2026-10-22

An update after the Product owner changed the amber band from 14 to 21 days (DEC-003, SRC-008).

Round 1:

- Q: What does this update cover? → A: The 21-day amber band, plus bringing the document in line
  with the knowledge base and the 2026-10-20 review (F-01, F-04, F-05, F-06: the answered questions
  leave the open-question lists, the rules the sign-off created are cited, Q-018 and Q-019 are
  listed), and raising F-02 and F-03 as proposals for the Product owner (recommended, accepted by
  Lead BA).
- Q: Which vehicles does a user see on the dashboard? → A: Only the vehicles of their own operator
  (recommended, accepted by Lead BA; a proposal for the Product owner, pending Q-020).
- Q: What does the dashboard show when there are no vehicles to list? → A: The message "No vehicles
  to show" (recommended, accepted by Lead BA; a proposal for the Product owner, pending Q-021).
- Q: (Q-018) In what order are overdue vehicles listed among themselves? → A: The oldest missed due
  date first, with a criterion in ST-04 that Q-018 blocks (recommended, accepted by Lead BA; a
  proposal for the Product owner, pending Q-018).
- Q: How are vehicles the order doesn't separate listed (the same next due date, the same oldest
  missed due date, or not scheduled)? → A: By registration number, A to Z (recommended, accepted by
  Lead BA; a proposal for the Product owner, pending Q-022).

Round 2:

- Q: The document was approved on 2026-10-20 and now changes: FR-012 and ST-03 follow DEC-003, and
  four proposals are pending. Does it keep its approval? → A: No: it goes back to `draft` and its
  approval is cleared, so `/review` runs again and the Product owner signs off this version, which
  also answers the four proposals (recommended, accepted by Lead BA). The 2026-10-20 sign-off stays in
  `sources` (SRC-007) as the record of the earlier version's approval.

Not asked, decided from the knowledge base: Q-019 is non-blocking, because the criteria follow
BR-011 as signed off and its answer would only add or change criteria (the 2026-10-20 review, F-06).
