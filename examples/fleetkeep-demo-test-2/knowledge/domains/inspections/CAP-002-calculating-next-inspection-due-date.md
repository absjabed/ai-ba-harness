---
type: capability
id: CAP-002
title: Calculating the next inspection due date
status: confirmed
area: inspections
owner: Product owner
sources: [SRC-001, SRC-006, SRC-007]
rules: [BR-003, BR-008, BR-010, BR-011]
aliases: []
tags: [inspections]
created: 2026-10-15
updated: 2026-10-20
---

# Calculating the next inspection due date

The product works out when each vehicle's next safety inspection is due, counting from the vehicle's anchor date ([SRC-001](../../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md)).

## Who and when

| Role | What they do here | When |
|---|---|---|

## What the user sees

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Anchor date | Yes | Set on [Setting a vehicle's inspection interval and anchor date](CAP-001-setting-inspection-interval-and-anchor-date.md) |
| Safety inspection interval | Yes | Whole weeks, one per vehicle (BR-001) |

## Rules applied

In the order they are evaluated.

1. **BR-003** The next due date is the vehicle's anchor date plus a whole number of its inspection intervals; doing an inspection early or late doesn't move the schedule. (SRC-001)
2. **BR-008** A vehicle's first due date is its anchor date plus one inspection interval; the anchor date itself is not a due date. (SRC-007, Q-014)
3. **BR-010** An inspection meets every unmet due date on or before the day it is done; when there is none, it meets the first due date after that day. (SRC-007, Q-001)
4. **BR-011** A vehicle's next due date is the first of its due dates after today that no inspection has met. (SRC-007, Q-001)

## Outcomes

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|

## Interactions

- Uses the interval and anchor date from [Setting a vehicle's inspection interval and anchor date](CAP-001-setting-inspection-interval-and-anchor-date.md).

## Open items

> [!CAUTION]
> **Unresolved:** how the inspection rules apply to a vehicle while it is VOR. See [Q-003](../../questions/Q-003-inspection-rules-for-vor-vehicles.md).

## Sources

- SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
- SRC-006: the Lead BA's answers while writing the inspection scheduling and dashboard requirement, 2026-10-18
- SRC-007: the Product owner's sign-off of the inspection scheduling and dashboard requirement, 2026-10-20
