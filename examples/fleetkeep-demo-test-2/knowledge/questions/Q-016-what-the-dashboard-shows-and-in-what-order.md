---
type: question
id: Q-016
title: What the dashboard shows for each vehicle, and in what order
status: approved
state: answered
asked_on: 2026-10-18
asked_of: Product owner
due: 2026-11-01
answered_on: 2026-10-20
answer_source: SRC-007
approved_by: Product owner
approved_on: 2026-10-20
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-006, SRC-007]
tags: [inspections]
created: 2026-10-18
updated: 2026-10-20
---

# What the dashboard shows for each vehicle, and in what order

Besides its inspection status, what does the dashboard show for each vehicle, and in what order does it list the vehicles?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-016, FR-017 and ST-04.

## What is unclear

The knowledge base says the dashboard shows each vehicle's status (BR-004) but not what else it shows or how it orders the vehicles.

## Possible answers

1. Each scheduled vehicle's next due date beside its status; overdue vehicles first, then the other scheduled vehicles by next due date (earliest first), then the vehicles that are not scheduled.
2. Another order the Product owner chooses, such as by registration or by depot.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 1. Not yet proposed: the order among the overdue vehicles, for example by next due date, or by the oldest missed due date first.

## Why it matters

The dashboard's layout and order can't be built or tested until this is settled.

## Answer

Possible answer 1, as the Lead BA proposed: each scheduled vehicle's next due date beside its status; overdue vehicles first, then the other scheduled vehicles by next due date (earliest first), then the vehicles that are not scheduled. Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). It is BR-016 and BR-017 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md). The order among the overdue vehicles had no proposal, so the sign-off doesn't answer it; it is asked in [Q-018](Q-018-order-of-overdue-vehicles-on-the-dashboard.md).
