---
type: requirement
id: REQ-inspection-due-dates-and-dashboard-banding
title: Inspection due dates and dashboard banding
status: draft
area: inspections
owner: Lead BA
jira_epic:
fix_version: 2026.12
approved_by:
approved_on:
delivered_on:
sources: [SRC-001, SRC-002, DEC-001, DEC-002, DEC-003]
created: 2026-10-15
updated: 2026-10-15
---

# Inspection due dates and dashboard banding

## Goal

Transport managers can see, for every vehicle, when its next safety inspection is due and whether it
is green (more than 14 days away), amber (14 days or less) or red (overdue), so the fleet stays
road-legal. Compliance officers can see the same status.

## Current state

- Each vehicle has its own safety inspection interval, set on that vehicle; there is no fleet-wide
  interval ([BR-001](../../knowledge/domains/vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md),
  CAP-001, confirmed). The pilot customer uses 6 weeks for HGVs and 8 weeks for vans, as practice,
  not a product default (SRC-001). The interval's unit and range aren't set
  ([Q-007](../../knowledge/questions/Q-007-interval-unit-and-range.md), open).
- The next due date is calculated from the vehicle's anchor date and interval, not from when the
  last inspection was done; neither a late nor an early inspection moves the schedule
  ([BR-002](../../knowledge/domains/inspections/CAP-002-calculating-the-next-inspection-due-date.md),
  CAP-002, confirmed; [DEC-001](../../knowledge/decisions/DEC-001-due-date-counts-from-the-anchor-date.md),
  approved by the Product owner).
- The dashboard shows each vehicle green when the next due date is more than 14 days away, amber at
  14 days or less, red when overdue
  ([BR-003](../../knowledge/domains/inspections/CAP-003-seeing-inspection-due-status-on-the-dashboard.md),
  CAP-003, confirmed; [DEC-002](../../knowledge/decisions/DEC-002-inspection-due-banding.md),
  approved). The days are calendar days and a vehicle due today is amber (BR-005, confirmed).
- The dashboard loads in under 3 seconds for fleets of up to 2,000 vehicles
  ([DEC-003](../../knowledge/decisions/DEC-003-dashboard-load-time-for-large-fleets.md), approved;
  answers [Q-003](../../knowledge/questions/Q-003-dashboard-load-time-for-large-fleets.md)).
- Every safety inspection includes a brake performance test
  ([BR-004](../../knowledge/domains/inspections/CAP-004-recording-a-safety-inspection.md), CAP-004,
  confirmed).
- Open questions touching this area, all asked of the Product owner:
  [Q-001](../../knowledge/questions/Q-001-due-date-while-a-vehicle-is-vor.md) (due date while VOR),
  [Q-002](../../knowledge/questions/Q-002-block-closing-an-inspection-without-a-brake-test.md)
  (closing an inspection without a brake test),
  [Q-004](../../knowledge/questions/Q-004-no-anchor-date-on-the-dashboard.md) (vehicle with no
  anchor date), [Q-005](../../knowledge/questions/Q-005-due-date-after-an-interval-change.md)
  (interval change), [Q-006](../../knowledge/questions/Q-006-which-due-date-an-inspection-satisfies.md)
  (which due date an inspection satisfies), Q-007 (interval unit and range) and
  [Q-008](../../knowledge/questions/Q-008-who-sets-intervals-and-sees-the-dashboard.md) (who sets
  intervals and sees the dashboard).

## Scope

**In:**
- Setting a vehicle's safety inspection interval (CAP-001).
- Calculating the next safety inspection due date from the anchor date (CAP-002).
- Showing each vehicle's inspection due status on the dashboard (CAP-003).

**Out:**
- Blocking the closing of an inspection without a brake test result (Q-002, open).
- What happens to the due date while a vehicle is VOR (Q-001, open); A-001 applies meanwhile.
- Notifications about due or overdue inspections.
- Recording a safety inspection itself (CAP-004); this requirement only uses recorded inspections.
- Setting or changing a vehicle's anchor date.
- Which organisation's vehicles a user can see (tenancy-and-access).

## Stakeholders

| Role | Interest | Decides |
|---|---|---|
| Product owner | What the product does and what each release delivers | Scope, business rules, permissions, release content; answers Q-004 to Q-008 |
| Lead BA | A requirement the team can trust | Requirement wording |
| Compliance adviser | In line with the regulator's guidance | How regulator guidance is interpreted; consulted on Q-007 |
| Engineering lead | How it is built | Technical approach and estimates; how anchor dates are stored today (ACT-002) |
| Transport manager (user) | Keeping each vehicle's inspections on time | Nothing in the product |
| Compliance officer (user) | Seeing that inspections are on time | Nothing in the product |
| Pilot transport manager | The pilot fleet's schedule | Nothing in the product; may resist the anchored schedule (risk R-001) |

## Functional requirements

| ID | Requirement | Source | Rules |
|---|---|---|---|
| FR-001 | Each vehicle has its own safety inspection interval; setting one vehicle's interval doesn't change any other vehicle's. | SRC-001 | BR-001 |
| FR-002 | A safety inspection interval is a whole number of weeks, at least 1, with no maximum until the regulator's guidance (ACT-001) sets one. | SRC-002 (recommended answer adopted), pending Q-007 | |
| FR-003 | Only a transport manager can set or change a vehicle's safety inspection interval. | SRC-002 (Lead BA's view), pending Q-008 | |
| FR-004 | A vehicle's due dates are its anchor date plus whole multiples (1, 2, 3 ...) of its interval. | DEC-001; the first due date being one interval after the anchor date is an assumption (see Assumptions) | BR-002 |
| FR-005 | A recorded safety inspection satisfies the earliest due date not yet satisfied, if it was done after the due date before that one (or after the anchor date, for the first). | SRC-002 (recommended answer adopted), pending Q-006 | BR-002 |
| FR-006 | A vehicle's next due date is its earliest due date not yet satisfied. | SRC-002 (recommended answer adopted), pending Q-006 | BR-002 |
| FR-007 | When a vehicle's interval changes, its next due date is recalculated from the same anchor date with the new interval. | SRC-002 (Lead BA's view), pending Q-005 | BR-002 |
| FR-008 | The dashboard shows each vehicle with a next due date as green when it is more than 14 calendar days away, amber at 14 days or less (including the due date itself), and red from the day after it. | DEC-002, SRC-002 | BR-003, BR-005 |
| FR-009 | Transport managers and compliance officers can see the dashboard. | SRC-002 (Lead BA's view), pending Q-008 | |
| FR-010 | Compliance officers can only view the dashboard. | SRC-002 (Lead BA's view), pending Q-008 | |
| FR-011 | On the dashboard, a vehicle with no anchor date is shown grey, labelled "Not scheduled". | SRC-002 (Lead BA's view), pending Q-004 | |

## Non-functional requirements

In EARS form: `<optional precondition> the <system> shall <response>`, using WHEN (event), WHILE
(state), WHERE (feature), IF … THEN (unwanted behaviour), or no keyword (always).

| ID | Requirement | Measure | Source |
|---|---|---|---|
| NFR-001 | WHEN a transport manager or compliance officer opens the dashboard for a fleet of up to 2,000 vehicles, FleetKeep shall show every vehicle's inspection due status in under 3 seconds. | Timed from opening the dashboard until every vehicle's band is shown, with a test fleet of 2,000 vehicles | DEC-003 |

## User stories

| Story | Summary | FR | Jira key |
|---|---|---|---|
| ST-01 | Set a vehicle's safety inspection interval | FR-001, FR-002, FR-003 | |
| ST-02 | See a vehicle's next due date counted from its anchor date | FR-004, FR-005, FR-006 | |
| ST-03 | Recalculate the next due date when the interval changes | FR-007, FR-003 | |
| ST-04 | See each vehicle's inspection due status on the dashboard | FR-008, FR-009, FR-010 | |
| ST-05 | Show vehicles with no anchor date as "Not scheduled" | FR-011 | |

### ST-01 Set a vehicle's safety inspection interval

As a transport manager, I want to set each vehicle's safety inspection interval, so that each
vehicle's inspections are scheduled to its own interval.

**AC-1 Interval set on one vehicle only**
- Given two vehicles, each with an interval of 6 weeks
- When the transport manager sets the first vehicle's interval to 8 weeks
- Then the first vehicle's interval is 8 weeks and the second vehicle's is still 6 weeks

**AC-2 Interval under 1 week is refused**
- Given a vehicle with an interval of 6 weeks
- When the transport manager enters an interval of 0 weeks
- Then the interval isn't saved and the vehicle's interval is still 6 weeks

**AC-3 Compliance officer can't set an interval**
- Given a compliance officer is signed in
- When they look at a vehicle's safety inspection interval
- Then they can't set or change it

**Business rules:** BR-001
**Out of scope:** setting the anchor date
**Open questions:** Q-007 (blocks AC-2), Q-008 (blocks AC-3)

### ST-02 See a vehicle's next due date counted from its anchor date

As a transport manager, I want each vehicle's next safety inspection due date worked out from its
anchor date and interval, so that the schedule stays anchored whether inspections are early or late.

**AC-1 First due date**
- Given a vehicle with anchor date 2026-11-02, an interval of 6 weeks and no inspection recorded
- When its next due date is worked out
- Then it is 2026-12-14

**AC-2 Early inspection doesn't move the schedule**
- Given that vehicle, with next due date 2026-12-14
- When a safety inspection done on 2026-12-07 is recorded
- Then its next due date is 2027-01-25, not 2027-01-18

**AC-3 Late inspection doesn't move the schedule**
- Given that vehicle, overdue since 2026-12-14
- When a safety inspection done on 2026-12-20 is recorded
- Then its next due date is 2027-01-25, not 2027-01-31

**Business rules:** BR-002
**Out of scope:** VOR vehicles (Q-001; A-001 applies); whether an inspection without a brake test
counts (Q-002)
**Open questions:** Q-006 (blocks AC-2 and AC-3)

### ST-03 Recalculate the next due date when the interval changes

As a transport manager, I want a vehicle's next due date recalculated when I change its interval, so
that the schedule matches the new interval without losing its anchor date.

**AC-1 Recalculated from the same anchor date**
- Given a vehicle with anchor date 2026-11-02, an interval of 6 weeks, next due date 2026-12-14 and
  no inspection recorded
- When the transport manager changes the interval to 8 weeks
- Then the next due date is 2026-12-28 and the anchor date is still 2026-11-02

**AC-2 Compliance officer can't change the interval**
- Given a compliance officer is signed in
- When they look at a vehicle's interval
- Then they can't change it, and the next due date stays as it was

**Business rules:** BR-002
**Out of scope:** changing the anchor date
**Open questions:** Q-005 (blocks AC-1), Q-008 (blocks AC-2)

### ST-04 See each vehicle's inspection due status on the dashboard

As a transport manager, I want to see each vehicle's inspection due status on the dashboard, so that
I can see at a glance which inspections are due within 14 days or overdue.

**AC-1 Green more than 14 days away**
- Given today is 2026-10-15 and a vehicle's next due date is 2026-10-30
- When the transport manager opens the dashboard
- Then the vehicle is green

**AC-2 Amber at 14 days**
- Given today is 2026-10-15 and a vehicle's next due date is 2026-10-29
- When the transport manager opens the dashboard
- Then the vehicle is amber

**AC-3 Amber on the due date**
- Given today is 2026-10-15 and a vehicle's next due date is 2026-10-15
- When the transport manager opens the dashboard
- Then the vehicle is amber

**AC-4 Red the day after**
- Given today is 2026-10-15 and a vehicle's next due date is 2026-10-14
- When the transport manager opens the dashboard
- Then the vehicle is red

**AC-5 Compliance officer sees the dashboard read-only**
- Given a compliance officer is signed in
- When they open the dashboard
- Then they see each vehicle's inspection due status and can't change anything from it

**Business rules:** BR-003, BR-005
**Out of scope:** notifications; VOR vehicles (A-001 applies)
**Open questions:** Q-008 (blocks AC-5)

### ST-05 Show vehicles with no anchor date as "Not scheduled"

As a transport manager, I want vehicles with no anchor date shown as "Not scheduled", so that I can
see which vehicles have no inspection schedule yet.

**AC-1 No anchor date shows "Not scheduled"**
- Given a vehicle with an interval but no anchor date
- When the transport manager opens the dashboard
- Then the vehicle is grey, labelled "Not scheduled"

**AC-2 Not counted as green, amber or red**
- Given a vehicle with no anchor date
- When the transport manager opens the dashboard
- Then the vehicle isn't shown green, amber or red

**Business rules:** None yet (the behaviour is Q-004; BR-003 doesn't cover vehicles without a due
date)
**Out of scope:** setting the anchor date
**Open questions:** Q-004 (blocks the story)

## Assumptions

- A-001: Until Q-001 is answered, a VOR vehicle's next due date and band are worked out like any
  other vehicle's. Assumed because VOR behaviour is out of scope and Q-001 is open; confirmed when
  the Product owner answers Q-001.
- (No ID yet) The first due date is the anchor date plus one interval, not the anchor date itself.
  Assumed as the reading of "counts from" (DEC-001); FR-004, ST-02 AC-1 and ST-03 AC-1 depend on
  it. Not in `raid.md` yet; to confirm with the Product owner alongside Q-006.

## Open questions

| Question | Blocks | Asked of | Due |
|---|---|---|---|
| Q-004 What does the dashboard show for a vehicle with no anchor date? | ST-05 | Product owner | 2026-10-29 |
| Q-005 What happens to the next due date when a vehicle's interval changes? | ST-03 AC-1 | Product owner | 2026-10-29 |
| Q-006 Which due date does a recorded safety inspection satisfy? | ST-02 AC-2, AC-3 | Product owner | 2026-10-29 |
| Q-007 What unit and range can a safety inspection interval have? | ST-01 AC-2 | Product owner | 2026-10-29 |
| Q-008 Who can set a vehicle's interval, and who can see the dashboard? | ST-01 AC-3, ST-03 AC-2, ST-04 AC-5 | Product owner | 2026-10-29 |
| Q-001 What happens to the due date while a vehicle is VOR? | none (out of scope; A-001) | Product owner | 2026-10-28 |
| Q-002 Should closing an inspection be blocked without a brake test result? | none (out of scope) | Product owner | 2026-10-28 |

## Conflicts with the knowledge base

None stated. FR-011 would add a fourth state to the three bands of DEC-002 (approved) and BR-003
(confirmed); instead of stating it as a rule, it is raised as Q-004 and ST-05 waits for the answer.

## Success measures

- SC-001: none agreed yet. Proposed, for the Product owner to confirm: before release, every pilot
  vehicle's band matches a manual calculation from its anchor date and interval.

## Clarifications

### Session 2026-10-15

- Q: Scope? → A: In: per-vehicle intervals, due-date calculation from the anchor date, dashboard
  banding. Out: brake test enforcement (Q-002), VOR behaviour (Q-001), notifications. (Lead BA)
- Q: Who sets intervals and who sees the dashboard? → A: Transport managers set intervals and see
  the dashboard; compliance officers see the dashboard read-only. (Lead BA; raised as Q-008 for the
  Product owner)
- Q: How are days counted, and which band is a vehicle due today? → A: Calendar days; due today is
  amber. (Lead BA; BR-005)
- Q: Which due date does a recorded inspection satisfy? → A: No specific answer; the recommended
  option was adopted (the earliest due date not yet satisfied, if done after the one before). (Lead
  BA; raised as Q-006)
- Q: What happens to the next due date when the interval changes? → A: Recalculated from the same
  anchor date. (Lead BA; raised as Q-005)
- Q: What does a vehicle with no anchor date show? → A: Grey "Not scheduled". (Lead BA; raised as
  Q-004)
- Q: Interval unit and range? → A: No specific answer; the recommended option was adopted (whole
  weeks, at least 1, no maximum until the regulator's guidance). (Lead BA; raised as Q-007)
- Q: How quickly must the dashboard load, and for how many vehicles (Q-003)? → A: Under 3 seconds
  for fleets of up to 2,000 vehicles, agreed by the Product owner by email today. (Lead BA relaying
  the Product owner; DEC-003)
- Q: Fix version? → A: 2026.12. (Lead BA)
