---
type: capability
id: CAP-006
title: Deciding what happens to a reported defect
status: confirmed
area: defects
owner: Product owner
sources: [SRC-003, DEC-002]
rules: [BR-007]
aliases: []
tags: [defects]
created: 2026-10-17
updated: 2026-10-17
---

# Deciding what happens to a reported defect

Every reported defect gets a decision from the transport manager first ([SRC-003](../../sources/SRC-003-2026-10-16-defects-workshop.md), [DEC-002](../../decisions/DEC-002-transport-manager-decides-every-defect-first.md)).

## Who and when

| Role | What they do here | When |
|---|---|---|
| [Transport manager](../../entities/ENT-001-transport-manager.md) | Decides what happens to a reported defect | First, after the defect is reported; what it comes before is not stated yet |

## What the user sees

## Inputs

| Input | Required? | Rules |
|---|---|---|

## Rules applied

In the order they are evaluated.

1. **BR-007** Every reported defect gets a decision from the transport manager first. (SRC-003, DEC-002)

## Outcomes

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|

## Interactions

- Defects come from [Reporting a defect in a walkaround check](CAP-005-reporting-a-defect-in-a-walkaround-check.md).
- How it works today: at the pilot customer, technicians sometimes clear category-C defects without a job card (SRC-003). BR-007 was decided in the same discussion at the workshop.

## Open items

> [!CAUTION]
> **Unresolved:** which decisions the transport manager can make on a defect, and what the decision must come before. See [Q-007](../../questions/Q-007-transport-manager-decision-on-a-defect.md).

## Sources

- SRC-003: the defects workshop, 2026-10-16 (Lead BA's notes)
- DEC-002: every defect gets a decision from the transport manager first
