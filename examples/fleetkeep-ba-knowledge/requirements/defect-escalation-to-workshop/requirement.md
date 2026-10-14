---
type: requirement
id: REQ-defect-escalation-to-workshop
title: Defect escalation to workshop
status: confirmed
area: defects
owner: Lead BA
jira_epic: FK-1301
fix_version: 2026.11
approved_by:
approved_on:
delivered_on:
sources:
  - SRC-003
  - SRC-004
  - DEC-002
  - FK-1192
created: 2026-10-09
updated: 2026-10-13
---

# Defect escalation to workshop

## Goal

When a defect escalates because nobody has acted on it, the workshop at the vehicle's depot sees it
at once and the transport manager can turn it into a job card in one step. Transport managers and
technicians lose less time, and category-A vehicles spend less time off the road.

## Current state

From the knowledge base on 2026-10-09:

- A driver reports a defect in the walkaround check with a category A, B or C; a category-A defect
  sets the vehicle to VOR at once ([CAP-001](../../knowledge/domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md), BR-002, BR-003).
- Only a transport manager can triage, reject or raise a job card for a defect, and a defect can't
  skip a state ([CAP-002](../../knowledge/domains/defects/CAP-002-triaging-a-defect.md), BR-014,
  BR-005, BR-006).
- A category-A defect with no triage outcome 4 hours after the report, or a category-B defect after
  36 hours, is escalated to the transport manager by email; FleetKeep checks once an hour and resends
  failed emails at the next check ([CAP-004](../../knowledge/domains/defects/CAP-004-escalating-unactioned-defects.md),
  BR-015, BR-016, BR-017, [DEC-001](../../knowledge/decisions/DEC-001-escalation-clock-starts-at-report.md)).
- The workshop doesn't see escalations today ([R-001](../../knowledge/raid.md#risks)). The Product
  owner agreed to flag escalated defects at the top of the depot's workshop queue
  ([DEC-002](../../knowledge/decisions/DEC-002-escalated-defects-top-of-workshop-queue.md), confirmed,
  recorded second-hand).
- Every change to a defect is in its audit trail ([PROC-001](../../knowledge/processes/defects/defect-to-return-to-service/PROC-001-defect-to-return-to-service.md), BR-012).
- Open questions touching this area: whether the escalation clock runs outside working hours
  ([Q-002](../../knowledge/questions/Q-002-escalation-clock-outside-working-hours.md)) and what state
  a deferred defect takes ([Q-004](../../knowledge/questions/Q-004-state-of-a-deferred-defect.md)).

## Scope

**In:**
- Flagging escalated defects on the workshop queue of the vehicle's depot, at the top.
- Emailing the depot's technicians when a category-A defect escalates.
- Triaging an escalated defect and raising its job card in one action.
- Recording each escalation in the defect's history.

**Out:**
- Changing the escalation thresholds (BR-015, BR-016) or the clock (Q-002).
- Text messages or phone notifications.
- Escalating category-C defects.
- Any change to return to service ([CAP-006](../../knowledge/domains/vehicles/CAP-006-authorising-return-to-service.md)).
- Adding escalations to the audit pack export (see [I-001](../../knowledge/raid.md#issues)).

## Stakeholders

| Role | Interest | Decides |
|---|---|---|
| Product owner | A workshop that acts on escalations | Scope, rules, release |
| Pilot transport manager | Fewer category-A vehicles waiting off the road | Nothing in the product |
| Pilot workshop supervisor | Seeing what matters first in the queue | Nothing in the product |
| Engineering lead | A change that fits the hourly escalation check | Technical approach |
| Compliance adviser | Escalations an auditor can trace | Interpretation of regulator guidance |

## Functional requirements

| ID | Requirement | Source | Rules |
|---|---|---|---|
| FR-001 | When a defect escalates, FleetKeep flags it on the workshop queue of the vehicle's depot. | DEC-002 | BR-015, BR-016 |
| FR-002 | Flagged defects are listed above every other item in the workshop queue, oldest escalation first. | DEC-002 | None |
| FR-003 | A defect's flag is removed when its job card is raised or it is rejected. | SRC-004 | BR-005, BR-006 |
| FR-004 | When a category-A defect escalates, FleetKeep emails the technicians assigned to the vehicle's depot, as well as the transport manager. | FK-1192, SRC-004 | BR-015 |
| FR-005 | A transport manager can triage an escalated defect and raise its job card in one action, which records both state changes. | Q-001 answer, SRC-004 | BR-014, BR-005 |
| FR-006 | Each escalation is recorded in the defect's history with the time, the threshold passed and the roles notified. | SRC-004 | BR-012 |

## Non-functional requirements

In EARS form: `<optional precondition> the <system> shall <response>`, using WHEN (event), WHILE
(state), WHERE (feature), IF … THEN (unwanted behaviour), or no keyword (always).

| ID | Requirement | Measure | Source |
|---|---|---|---|
| NFR-001 | WHEN a defect passes its escalation threshold, FleetKeep shall flag it on the depot's workshop queue within 60 minutes. | Test with defects passing each threshold at different minutes past the hour; every flag appears within 60 minutes | CAP-004 (hourly check) |
| NFR-002 | IF an escalation email can't be sent, THEN FleetKeep shall send it at each following hourly check until it is sent, and never twice to the same person. | Forced send failure in test; email arrives after the next check, once per recipient | CAP-004 |
| NFR-003 | WHILE a technician views the workshop queue, FleetKeep shall show only flagged defects for vehicles at the technician's own depots. | Permission test with technicians at two depots | ENT-003, SRC-001 |
| NFR-004 | WHERE a defect is flagged, the workshop queue shall mark it with the word "Escalated" as well as a colour. | Accessibility review of the queue | SRC-004 |

## User stories

| Story | Summary | FR | Jira key |
|---|---|---|---|
| ST-01 | See escalated defects at the top of the workshop queue | FR-001, FR-002, FR-003 | FK-1302 |
| ST-02 | Email depot technicians when a category-A defect escalates | FR-004 | FK-1303 |
| ST-03 | Raise a job card from an escalated defect | FR-005 | FK-1304 |
| ST-04 | See the escalations in a defect's history | FR-006 | FK-1305 |

### ST-01 See escalated defects at the top of the workshop queue

As a workshop technician, I want escalated defects at my depot flagged at the top of the workshop
queue, so that I can prepare for the most overdue repairs first.

**AC-1 Escalated defect is flagged**
- Given a category-B defect at my depot, reported 36 hours ago and still in Triaged
- When FleetKeep runs its hourly escalation check
- Then the defect appears at the top of my depot's workshop queue, marked "Escalated"

**AC-2 Oldest escalation first**
- Given two flagged defects at my depot, one escalated at 08:00 and one at 09:00
- When I open the workshop queue
- Then the 08:00 defect is listed first, and both are above every unflagged item

**AC-3 Other depots stay hidden**
- Given a flagged defect at a depot I am not assigned to
- When I open the workshop queue
- Then I don't see that defect

**AC-4 Flag cleared by a triage outcome**
- Given a flagged defect at my depot
- When the transport manager raises its job card, or rejects it with a reason
- Then the flag is removed from the queue

**Business rules:** BR-015, BR-016, BR-005, BR-006
**Out of scope:** changing the thresholds; category-C defects
**Open questions:** Q-002 (non-blocking: it changes when a threshold is reached, not how the flag behaves)

### ST-02 Email depot technicians when a category-A defect escalates

As a workshop technician, I want an email when a category-A defect at my depot escalates, so that an
immobilised vehicle isn't left waiting while the transport manager is away from the depot.

**AC-1 Category A emails the depot's technicians**
- Given a category-A defect at depot North, reported 4 hours ago and still in Reported
- When FleetKeep runs its hourly escalation check
- Then the transport manager and each technician assigned to depot North receive one escalation email naming the vehicle and the defect

**AC-2 Category B doesn't email technicians**
- Given a category-B defect that has just passed its 36-hour threshold
- When FleetKeep runs its hourly escalation check
- Then the transport manager receives the escalation email, the technicians don't, and the defect is flagged on the queue

**AC-3 A failed email is sent once at the next check**
- Given an escalation email that couldn't be sent to one technician
- When the next hourly check runs
- Then that technician receives it, and nobody who already had it receives it again

**Business rules:** BR-015, BR-016
**Out of scope:** text messages; emails for category-C defects
**Open questions:** Q-002 (non-blocking, as for ST-01)

### ST-03 Raise a job card from an escalated defect

As a transport manager, I want to triage an escalated defect and raise its job card in one action,
so that the workshop can start without me stepping through triage separately.

**AC-1 Triage and raise in one action**
- Given an escalated category-A defect still in Reported
- When I select "Raise job card" on the flagged defect
- Then the defect moves to Triaged and then to Job card raised, both changes are in its history with my role and the time, and the job card appears in the depot's workshop queue

**AC-2 Technicians can't do it**
- Given a workshop technician viewing the same flagged defect
- When they try to raise its job card
- Then the action isn't offered to them, and a direct attempt is refused

**AC-3 Already triaged**
- Given an escalated defect already in Triaged
- When I raise its job card
- Then only the change to Job card raised is recorded

**Business rules:** BR-014, BR-005, BR-012
**Out of scope:** rejecting from the flag (rejection works as today, from Triaged with a reason)
**Open questions:** None

### ST-04 See the escalations in a defect's history

As a compliance officer, I want each escalation shown in the defect's history, so that I can show an
auditor when an unactioned defect was chased and who was told.

**AC-1 Escalation recorded**
- Given a defect that escalated at 14:00
- When I open the defect's history
- Then I see an escalation entry with the time, the threshold passed (4 or 36 hours) and the roles notified

**AC-2 History can't be changed**
- Given I am a compliance officer viewing that history
- When I look at the escalation entry
- Then I can't change or delete it

**Business rules:** BR-012, BR-013
**Out of scope:** adding escalations to the audit pack export
**Open questions:** None

## Assumptions

- A-002: technicians usually look at the workshop queue at the start of each shift, so the queue flag
  reaches them for category-B defects without an email. Assumed from the Pilot workshop supervisor's
  description (SRC-001); to confirm against the pilot depots' shift patterns (D-001).
- A-003: escalation emails to technicians use the same email channel as today's escalations, the only
  notification channel FleetKeep has. To confirm with the Engineering lead.

## Open questions

| Question | Blocks | Asked of | Due |
|---|---|---|---|
| [Q-002](../../knowledge/questions/Q-002-escalation-clock-outside-working-hours.md) Does the escalation clock run outside depot working hours? | None (marked non-blocking by the Lead BA) | Product owner | 2026-10-21 |
| [Q-004](../../knowledge/questions/Q-004-state-of-a-deferred-defect.md) What state does a deferred defect take when its job card closes? | None (marked non-blocking: flags apply only before a job card is raised) | Product owner | 2026-10-23 |

## Conflicts with the knowledge base

None. FR-005 was checked against BR-005: the one action records both state changes, so no state is
skipped.

## Success measures

- SC-001: in the pilot operator's account, the median time from a category-A escalation to its job
  card being raised is under 2 hours over the first 4 weeks after release, against the 4 weeks
  before, measured from the defects' history.
- SC-002: over the same 4 weeks, no escalated defect at a pilot depot waits more than 8 hours for a
  triage outcome.

## Clarifications

### Session 2026-10-09

- Q: Should category-B escalations email technicians too? → A: No. Category-B escalations are flagged on the queue only; technicians are emailed for category A (Lead BA, from FK-1192 comment 6).
- Q: Who can raise a job card from a flagged defect? → A: Only the transport manager (Lead BA, from the answer to Q-001).
- Q: Does a technician opening a flagged defect remove the flag? → A: No; only a triage outcome removes it, because the flag means "no triage outcome yet" (Lead BA, from BR-015 and BR-016).
- Q: Does the deferred-defect gap block this epic? → A: No; flags apply only before a job card is raised, so Q-004 is non-blocking (Lead BA).
