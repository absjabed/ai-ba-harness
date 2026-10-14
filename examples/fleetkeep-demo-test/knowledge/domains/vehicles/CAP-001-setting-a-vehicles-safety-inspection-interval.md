---
type: capability
id: CAP-001
title: Setting a vehicle's safety inspection interval
status: confirmed
area: vehicles
owner: Product owner
sources: [SRC-001, SRC-002]
rules: [BR-001]
aliases: []
tags: [vehicles, inspections]
created: 2026-10-14
updated: 2026-10-15
---

# Setting a vehicle's safety inspection interval

Each vehicle has its own safety inspection interval, set on that vehicle, which its inspection
schedule is based on ([SRC-001](../../sources/SRC-001-2026-10-14-inspections-workshop.md)).

## Who and when

Not described in the sources yet.

## What the user sees

Not described in the sources yet.

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Safety inspection interval | yes | Set per vehicle (BR-001). For example, the pilot customer uses 6 weeks for HGVs and 8 weeks for vans (SRC-001); this is their practice, not a product default. |

## Rules applied

In the order they are evaluated.

1. **BR-001** Every vehicle has its own safety inspection interval, set on that vehicle; there is no
   fleet-wide interval. (SRC-001)

> [!IMPORTANT]
> The regulator expects each vehicle's inspection interval to be written down for that vehicle, not
> for the fleet, as interpreted by the Compliance adviser (SRC-001). The guidance itself is due from
> [ACT-001](../../raid.md#actions).

## Outcomes

Not described in the sources yet.

## Failure and blocked paths

Not described in the sources yet.

## Interactions

- [CAP-002 Calculating the next safety inspection due date](../inspections/CAP-002-calculating-the-next-inspection-due-date.md)
  uses this interval, with the vehicle's anchor date, to work out the next due date
  ([DEC-001](../../decisions/DEC-001-due-date-counts-from-the-anchor-date.md)).

## Open items

> [!CAUTION]
> **Unresolved:** the interval's unit and range
> ([Q-007](../../questions/Q-007-interval-unit-and-range.md)).

> [!CAUTION]
> **Unresolved:** who can set or change a vehicle's interval
> ([Q-008](../../questions/Q-008-who-sets-intervals-and-sees-the-dashboard.md)).

## Sources

- SRC-001: Inspections workshop, 2026-10-14 (Lead BA's notes)
- SRC-002: Requirements clarification session, 2026-10-15 (Lead BA)
