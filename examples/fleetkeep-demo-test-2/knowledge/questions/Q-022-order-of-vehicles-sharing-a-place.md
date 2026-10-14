---
type: question
id: Q-022
title: How the dashboard orders vehicles its order doesn't separate
status: confirmed
state: open
asked_on: 2026-10-22
asked_of: Product owner
consulted: []
due: 2026-11-05
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-009]
tags: [inspections]
created: 2026-10-22
updated: 2026-10-22
---

# How the dashboard orders vehicles its order doesn't separate

In what order does the dashboard list vehicles that its order doesn't separate: scheduled vehicles with the same next due date, overdue vehicles that the order among overdue vehicles ([Q-018](Q-018-order-of-overdue-vehicles-on-the-dashboard.md)) doesn't separate, and the vehicles that are not scheduled?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-017.
- [Q-016](Q-016-what-the-dashboard-shows-and-in-what-order.md), whose answer set the dashboard's order (BR-017) without saying how vehicles sharing a place are ordered; ordering by registration was one of its possible answers.
- [Q-018](Q-018-order-of-overdue-vehicles-on-the-dashboard.md), the order among overdue vehicles.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-023 and ST-04.

## What is unclear

BR-017 lists overdue vehicles first, then the other scheduled vehicles by next due date, then the vehicles that are not scheduled. It doesn't say how two vehicles with the same next due date are ordered, or how the vehicles that are not scheduled are ordered among themselves. The review of the requirement on 2026-10-20 found the gap. If the answer is by registration number, it also needs to say how digits compare with letters, because registration numbers contain both.

## Possible answers

1. By registration number, A to Z.
2. In the order the vehicles were added to the product.

## Why it matters

The dashboard's order can't be fully tested while two vehicles can share a place in it.

## Proposed answer

The Lead BA, 2026-10-22 ([SRC-009](../sources/SRC-009-2026-10-22-inspection-dashboard-proposals.md)); for the Product owner to confirm or change: possible answer 1. The rule it would become, on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md): "Vehicles the dashboard's order doesn't otherwise separate are listed by registration number, A to Z."

## Answer
