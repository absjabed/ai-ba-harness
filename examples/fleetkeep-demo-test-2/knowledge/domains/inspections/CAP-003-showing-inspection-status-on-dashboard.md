---
type: capability
id: CAP-003
title: Showing a vehicle's inspection status on the dashboard
status: confirmed
area: inspections
owner: Product owner
sources: [SRC-001, SRC-006, SRC-007, SRC-008, DEC-003, SRC-009]
rules: [BR-019, BR-009, BR-012, BR-013, BR-014, BR-015, BR-016, BR-017, BR-018]
aliases: []
tags: [inspections]
created: 2026-10-15
updated: 2026-10-22
---

# Showing a vehicle's inspection status on the dashboard

The dashboard shows each vehicle's inspection status as green, amber or red, depending on how close its next due date is ([SRC-001](../../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md)).

## Who and when

| Role | What they do here | When |
|---|---|---|
| [Transport manager](../../entities/ENT-001-transport-manager.md) | Sees the vehicles' inspection status on the dashboard | Not stated in the source |
| [Compliance officer](../../entities/ENT-002-compliance-officer.md) | Sees the vehicles' inspection status on the dashboard, without changing any vehicle's schedule (BR-002) | Not stated in the source |

## What the user sees

Each vehicle with its inspection status: green, amber or red (BR-019).

A vehicle with no anchor date shows grey, labelled "Not scheduled" (BR-015).

Each scheduled vehicle's next due date beside its status (BR-016). Overdue vehicles come first, then the other scheduled vehicles by next due date, then the vehicles that are not scheduled (BR-017).

## Inputs

| Input | Required? | Rules |
|---|---|---|
| The vehicle's next due date | Yes | From [Calculating the next inspection due date](CAP-002-calculating-next-inspection-due-date.md) |

## Rules applied

In the order they are evaluated.

1. ~~**BR-004** A vehicle's inspection status is green when its next due date is more than 14 days away, amber when it is 14 days away or less, and red when the inspection is overdue. (SRC-001)~~ superseded by BR-019 ([DEC-003](../../decisions/DEC-003-amber-starts-21-days-before-due-date.md))
2. **BR-019** A vehicle's inspection status is green when its next due date is more than 21 days away, amber when it is 21 days away or less, and red when the inspection is overdue. ([SRC-008](../../sources/SRC-008-2026-10-22-amber-band-change.md), DEC-003)
3. **BR-009** A vehicle is overdue from the day after a due date that no inspection has met; there is no grace period. (SRC-007, Q-002)
4. **BR-012** A vehicle stays overdue until an inspection is recorded that meets the missed due date. (SRC-007, Q-001)
5. **BR-013** An overdue vehicle shows red whatever its next due date. (SRC-007, Q-001)
6. **BR-014** The days to a vehicle's next due date are counted as calendar days. (SRC-007, Q-015)
7. **BR-015** A vehicle with no anchor date shows grey on the dashboard, labelled "Not scheduled". (SRC-007, Q-013)
8. **BR-016** The dashboard shows each scheduled vehicle's next due date beside its inspection status. (SRC-007, Q-016)
9. **BR-017** The dashboard lists overdue vehicles first, then the other scheduled vehicles by next due date (earliest first), then the vehicles that are not scheduled. (SRC-007, Q-016)
10. **BR-018** Only transport managers and compliance officers can see the inspection dashboard. (SRC-007, Q-012)

## Outcomes

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|

## Interactions

- Uses the next due date from [Calculating the next inspection due date](CAP-002-calculating-next-inspection-due-date.md).

## Open items

> [!CAUTION]
> **Unresolved:** how a VOR vehicle's status is shown on the dashboard. See [Q-003](../../questions/Q-003-inspection-rules-for-vor-vehicles.md).

> [!CAUTION]
> **Unresolved:** the order the dashboard lists overdue vehicles in among themselves. See [Q-018](../../questions/Q-018-order-of-overdue-vehicles-on-the-dashboard.md).

> [!CAUTION]
> **Unresolved:** which vehicles a user sees on the dashboard: only their own operator's, or every operator's. See [Q-020](../../questions/Q-020-which-vehicles-a-user-sees-on-the-dashboard.md).

> [!CAUTION]
> **Unresolved:** what the dashboard shows when there are no vehicles to list. See [Q-021](../../questions/Q-021-dashboard-with-no-vehicles-to-list.md).

> [!CAUTION]
> **Unresolved:** how the dashboard orders vehicles its order doesn't separate, such as two with the same next due date. See [Q-022](../../questions/Q-022-order-of-vehicles-sharing-a-place.md).

## Sources

- SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
- SRC-006: the Lead BA's answers while writing the inspection scheduling and dashboard requirement, 2026-10-18
- SRC-007: the Product owner's sign-off of the inspection scheduling and dashboard requirement, 2026-10-20
- SRC-008: the Product owner's email changing the amber band to 21 days, 2026-10-22 (DEC-003)
- SRC-009: the Lead BA's proposals while updating the inspection scheduling and dashboard requirement, 2026-10-22
