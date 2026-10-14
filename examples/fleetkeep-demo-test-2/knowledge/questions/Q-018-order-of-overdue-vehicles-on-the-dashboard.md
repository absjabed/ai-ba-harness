---
type: question
id: Q-018
title: In what order the dashboard lists overdue vehicles
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
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-006, SRC-007, SRC-009]
tags: [inspections]
created: 2026-10-20
updated: 2026-10-22
---

# In what order the dashboard lists overdue vehicles

In what order does the dashboard list the overdue vehicles among themselves?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-017, which lists overdue vehicles first but doesn't say in what order.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-017, FR-022 and ST-04 (AC-4).
- Split from [Q-016](Q-016-what-the-dashboard-shows-and-in-what-order.md), which the Product owner's sign-off answered except for this part.

## What is unclear

The Lead BA's proposal for Q-016 said "Not yet proposed: the order among the overdue vehicles, for example by next due date, or by the oldest missed due date first" ([SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md)). The Product owner's sign-off approved the proposals marked pending ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)), and this part had none.

## Possible answers

1. The oldest missed due date first.
2. By next due date, earliest first, as for the other scheduled vehicles.

## Why it matters

The dashboard's order can't be fully built or tested when two or more vehicles are overdue.

## Proposed answer

The Lead BA, 2026-10-22 ([SRC-009](../sources/SRC-009-2026-10-22-inspection-dashboard-proposals.md)); for the Product owner to confirm or change: possible answer 1, the oldest missed due date first. The rule it would become, on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md): "The dashboard lists overdue vehicles among themselves by their oldest missed due date, earliest first."

## Answer
