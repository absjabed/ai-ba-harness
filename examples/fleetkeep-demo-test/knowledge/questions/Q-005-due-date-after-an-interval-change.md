---
type: question
id: Q-005
title: What happens to the next due date when a vehicle's interval changes?
status: confirmed
state: open
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on:
answer_source:
blocks: [CAP-002]
owner: Lead BA
sources: [SRC-002]
tags: [inspections, vehicles]
created: 2026-10-15
updated: 2026-10-15
---

# What happens to the next due date when a vehicle's interval changes?

When a vehicle's safety inspection interval changes, how is its next due date worked out?

## Where it comes up

- [CAP-002 Calculating the next safety inspection due date](../domains/inspections/CAP-002-calculating-the-next-inspection-due-date.md) (BR-002).
- [CAP-001 Setting a vehicle's safety inspection interval](../domains/vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md).
- Requirement REQ-inspection-due-dates-and-dashboard-banding.

## What is unclear

BR-002 and [DEC-001](../decisions/DEC-001-due-date-counts-from-the-anchor-date.md) say the due date
counts from the anchor date and the interval, but not what happens when the interval changes. The
Lead BA's view: "Changing a vehicle's interval recalculates its next due date from the same anchor
date" ([SRC-002](../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md)). Not covered
either: which of the recalculated due dates the inspections already done satisfy, and whether the
vehicle turns red at once when the recalculated next due date is already past. The due date was set
for 2026-10-29 by the Lead BA.

## Possible answers

1. Recalculated from the same anchor date with the new interval (the Lead BA's view; consistent
   with DEC-001).
2. Re-anchored at the date of the change.
3. The current due date stays; the new interval applies from the next one.

## Why it matters

Changing an interval, and the due date and band that follow, can't be built or tested until this is
decided.

## Answer

