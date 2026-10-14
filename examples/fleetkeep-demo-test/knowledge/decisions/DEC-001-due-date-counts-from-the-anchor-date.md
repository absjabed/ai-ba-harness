---
type: decision
id: DEC-001
title: Next due date counts from the anchor date
status: approved
decided_by: Product owner
decided_on: 2026-10-14
approved_by: Product owner
approved_on: 2026-10-14
owner: Product owner
sources: [SRC-001]
tags: [inspections]
created: 2026-10-14
updated: 2026-10-14
---

# Next due date counts from the anchor date

The next safety inspection due date is calculated from the vehicle's anchor date and interval, not
from the date the last inspection was done; a late inspection doesn't move the schedule, and an
early inspection doesn't move it either.

## Context

Decided by the Product owner at the inspections workshop of 2026-10-14
([SRC-001](../sources/SRC-001-2026-10-14-inspections-workshop.md)). The pilot customer's transport
manager said they usually move the due date forward when an inspection is done early, and wasn't
convinced by the anchored schedule.

## Options considered

| Option | For | Against |
|---|---|---|
| Move the due date when an inspection is done early (the pilot's current practice) | Matches how the pilot works today | Rejected by the Product owner: the schedule stays anchored |

## Decision

The next due date counts from the anchor date. A late inspection doesn't move the schedule, and an
early inspection doesn't move it either ("early is fine, schedule stays anchored").

## Consequences

- BR-002 on [CAP-002 Calculating the next safety inspection due date](../domains/inspections/CAP-002-calculating-the-next-inspection-due-date.md).
- Risk R-001 in [raid.md](../raid.md#risks): pilot users may resist the anchored schedule.

## Sources

- SRC-001: Inspections workshop, 2026-10-14, where the Product owner decided it
