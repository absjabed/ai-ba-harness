---
type: capability
id: CAP-002
title: Calculating the next safety inspection due date
status: confirmed
area: inspections
owner: Product owner
sources: [SRC-001, DEC-001, SRC-002]
rules: [BR-002]
aliases: [start date]
tags: [inspections]
created: 2026-10-14
updated: 2026-10-15
---

# Calculating the next safety inspection due date

Works out when a vehicle's next safety inspection is due, from the vehicle's anchor date and its
safety inspection interval ([DEC-001](../../decisions/DEC-001-due-date-counts-from-the-anchor-date.md)).

## Who and when

Not described in the sources yet.

## What the user sees

Not described in the sources yet.

## Inputs

| Input | Required? | Rules |
|---|---|---|
| [Anchor date](../../glossary.md#anchor-date) | yes | The date the schedule counts from (BR-002) |
| Safety inspection interval | yes | Set per vehicle, on [CAP-001](../vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md) |

## Rules applied

In the order they are evaluated.

1. **BR-002** The next safety inspection due date is calculated from the vehicle's anchor date and
   interval, not from the date the last inspection was actually done, so neither a late nor an
   early inspection moves the schedule. ([SRC-001](../../sources/SRC-001-2026-10-14-inspections-workshop.md), DEC-001)

## Outcomes

Not described in the sources yet.

## Failure and blocked paths

Not described in the sources yet.

## Interactions

- [CAP-001 Setting a vehicle's safety inspection interval](../vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md)
  provides the interval.
- [CAP-003 Seeing inspection due status on the dashboard](CAP-003-seeing-inspection-due-status-on-the-dashboard.md)
  bands vehicles by this due date.

## Open items

> [!CAUTION]
> **Unresolved:** what happens to the due date while a vehicle is VOR
> ([Q-001](../../questions/Q-001-due-date-while-a-vehicle-is-vor.md)).

> [!CAUTION]
> **Unresolved:** what happens to the next due date when a vehicle's interval changes
> ([Q-005](../../questions/Q-005-due-date-after-an-interval-change.md)).

> [!CAUTION]
> **Unresolved:** which due date a recorded safety inspection satisfies
> ([Q-006](../../questions/Q-006-which-due-date-an-inspection-satisfies.md)).

> [!NOTE]
> **Assumption:** until Q-001 is answered, a VOR vehicle's next due date is worked out like any other
> vehicle's ([A-001](../../raid.md#assumptions)).

## Sources

- SRC-001: Inspections workshop, 2026-10-14 (Lead BA's notes)
- DEC-001: Next due date counts from the anchor date
- SRC-002: Requirements clarification session, 2026-10-15 (Lead BA)
