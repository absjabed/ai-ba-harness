---
type: capability
id: CAP-005
title: Reporting a defect in a walkaround check
status: confirmed
area: defects
owner: Product owner
sources: [SRC-003, DEC-001]
rules: [BR-006]
aliases: []
tags: [defects]
created: 2026-10-17
updated: 2026-10-17
---

# Reporting a defect in a walkaround check

A driver reports each defect they find in the walkaround check, giving it a category of A, B or C ([SRC-003](../../sources/SRC-003-2026-10-16-defects-workshop.md)).

## Who and when

| Role | What they do here | When |
|---|---|---|
| Driver | Reports a defect and gives it a category | In the walkaround check |

## What the user sees

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Defect category | Yes (SRC-003) | One of A, B or C |

## Rules applied

In the order they are evaluated.

1. **BR-006** A category-A defect takes the vehicle off the road (VOR) immediately. (SRC-003, [DEC-001](../../decisions/DEC-001-category-a-defect-makes-vehicle-vor.md))

## Outcomes

A category-A defect takes the vehicle off the road (VOR) immediately (BR-006).

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|

## Interactions

## Open items

> [!CAUTION]
> **Unresolved:** what makes a defect category B or C, and what follows from each. See [Q-006](../../questions/Q-006-what-defect-categories-b-and-c-mean.md).

> [!CAUTION]
> **Unresolved:** whether a category-A defect takes the vehicle off the road before or after the transport manager's decision. See [Q-007](../../questions/Q-007-transport-manager-decision-on-a-defect.md).

> [!CAUTION]
> **Unresolved:** whether a defect can be re-categorised after it is reported. See [Q-008](../../questions/Q-008-re-categorising-a-reported-defect.md).

## Sources

- SRC-003: the defects workshop, 2026-10-16 (Lead BA's notes)
