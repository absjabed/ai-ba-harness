---
type: capability
id: CAP-001
title: Setting a vehicle's inspection interval and anchor date
status: confirmed
area: inspections
owner: Product owner
sources: [SRC-001, SRC-002, SRC-005, SRC-006]
rules: [BR-001, BR-002]
aliases: []
tags: [inspections]
created: 2026-10-15
updated: 2026-10-18
---

# Setting a vehicle's inspection interval and anchor date

Each vehicle has its own safety inspection interval, in whole weeks, and an anchor date; together they set the vehicle's inspection schedule ([SRC-001](../../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md)).

## Who and when

| Role | What they do here | When |
|---|---|---|
| [Transport manager](../../entities/ENT-001-transport-manager.md) | Sets or changes a vehicle's inspection interval and anchor date | Not stated in the source |

## What the user sees

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Safety inspection interval | Yes ([SRC-002](../../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)) | Whole weeks, one per vehicle (BR-001) |
| Anchor date | Not stated in the source | |

## Rules applied

In the order they are evaluated.

1. **BR-001** Each vehicle has its own safety inspection interval, set in whole weeks; there is no fleet-wide interval. (SRC-001)
2. **BR-002** Only a transport manager sets or changes a vehicle's inspection interval or anchor date. (SRC-001)

> [!IMPORTANT]
> The regulator guidance, as summarised by the Compliance adviser, requires the operator to decide and write down a safety inspection interval for each vehicle ([SRC-002](../../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)).

## Outcomes

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|

## Interactions

## Open items

> [!CAUTION]
> **Unresolved:** which intervals and anchor dates the product refuses, and whether both must be set together. See [Q-017](../../questions/Q-017-refused-intervals-and-anchor-dates.md).

## Sources

- SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
- SRC-002: the Compliance adviser's regulator guidance summary, 2026-10-05
- SRC-005: the Engineering lead's email on anchor dates and VOR, 2026-10-17 (anchor dates are kept per vehicle today, but a re-registered vehicle can end up sharing a record with another vehicle; see R-003 in the [RAID log](../../raid.md))
- SRC-006: the Lead BA's answers while writing the inspection scheduling and dashboard requirement, 2026-10-18
