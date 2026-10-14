---
type: question
id: Q-003
title: How inspection rules apply to VOR vehicles
status: confirmed
state: open
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-002, CAP-003]
owner: Lead BA
sources: [SRC-001, SRC-003, DEC-001, SRC-005]
tags: [inspections, vehicles]
created: 2026-10-15
updated: 2026-10-17
---

# How inspection rules apply to VOR vehicles

What makes a vehicle VOR, and how do the inspection rules apply to it while it is VOR?

## Where it comes up

- [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md).
- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
- [Reporting a defect in a walkaround check](../domains/defects/CAP-005-reporting-a-defect-in-a-walkaround-check.md).

## What is unclear

The Product owner's rules list "Vehicles that are VOR: to be decided." ([SRC-001](../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md), rule 7). Nothing else in the rules says whether a VOR vehicle's schedule, due date or dashboard status changes. The rules don't define VOR either; the Product owner is asked to say what makes a vehicle VOR, so the glossary can define it.

At the defects workshop on 2026-10-16 the Product owner decided one thing that makes a vehicle VOR: a category-A defect takes it off the road immediately ([DEC-001](../decisions/DEC-001-category-a-defect-makes-vehicle-vor.md)). Whether anything else makes a vehicle VOR, and how the inspection rules apply while it is VOR, is still open.

The Engineering lead reports that the product has no way today to record when a vehicle went VOR, so nothing can be paused while a vehicle is off the road ([SRC-005](../sources/SRC-005-2026-10-17-anchor-dates-and-vor.md)).

## Possible answers

1. Nothing changes: a VOR vehicle keeps its schedule and its dashboard status.
2. The schedule keeps running, but a VOR vehicle is shown apart on the dashboard and not counted as overdue while VOR.
3. The schedule pauses while the vehicle is VOR. The product would then need to record when a vehicle went VOR, which it can't today (see What is unclear). Choosing this would change BR-003 on [CAP-002](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), so it would need a decision that supersedes BR-003.
4. Something else the Product owner decides.

## Why it matters

The due date calculation and the dashboard can't be specified completely for VOR vehicles until this is decided.

## Answer
