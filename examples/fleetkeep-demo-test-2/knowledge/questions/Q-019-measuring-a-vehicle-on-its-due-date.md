---
type: question
id: Q-019
title: Whether a vehicle is measured against its due date on that day
status: confirmed
state: open
asked_on: 2026-10-20
asked_of: Product owner
consulted: []
due: 2026-11-03
answered_on:
answer_source:
approved_by:
approved_on:
blocks: []
owner: Lead BA
sources: [SRC-006, SRC-007, SRC-008]
tags: [inspections]
created: 2026-10-20
updated: 2026-10-22
---

# Whether a vehicle is measured against its due date on that day

On the day a vehicle's inspection is due and not yet done, should the vehicle be measured against that due date rather than the following one?

## Where it comes up

- [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), rule BR-011.
- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-019 (which replaced BR-004, DEC-003).
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-008, ST-02 and ST-03.
- Split from [Q-001](Q-001-next-due-date-after-a-missed-inspection.md), which the Product owner's sign-off answered as written.

## What is unclear

The Lead BA's proposal for Q-001 asked the Product owner "whether the due date itself should count" ([SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md)). The Product owner signed off the requirement "as written" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)), where FR-008 says "after today", but didn't answer that question separately. As written, a vehicle not yet inspected shows green (or amber, for an interval of 3 weeks or less, BR-019) on the day its inspection is due, and red from the next day.

## Possible answers

1. No, as signed off: a vehicle's next due date is the first of its due dates after today that no inspection has met (BR-011).
2. Yes: a vehicle's next due date is the first of its due dates on or after today that no inspection has met, so a vehicle not yet inspected shows amber on the day its inspection is due.

## Why it matters

What the dashboard shows on the day an inspection is due, and the tests for that day, depend on it.

## Answer
