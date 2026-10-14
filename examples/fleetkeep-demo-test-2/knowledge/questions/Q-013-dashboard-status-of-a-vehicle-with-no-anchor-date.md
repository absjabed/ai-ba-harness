---
type: question
id: Q-013
title: How the dashboard shows a vehicle with no anchor date
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

# How the dashboard shows a vehicle with no anchor date

How does the dashboard show a vehicle that has no anchor date, and so no next due date?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-004.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-015 and ST-03.

## What is unclear

BR-004 bands a vehicle green, amber or red by its next due date. A vehicle with no anchor date has no due dates (BR-003), so BR-004 doesn't say how it shows. The calculation needs an anchor date ([CAP-002](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), Inputs), but whether a vehicle must have one when its schedule is set isn't stated ([CAP-001](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md), Inputs).

## Possible answers

1. Grey, labelled "Not scheduled".
2. Left off the dashboard.
3. Red, as needing attention.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 1.

## Why it matters

The dashboard can't be specified or tested for vehicles without an anchor date until this is settled.

## Answer

Possible answer 1, as the Lead BA proposed: grey, labelled "Not scheduled". Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). It is BR-015 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
