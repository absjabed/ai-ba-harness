---
type: question
id: Q-015
title: How the 14 days before a due date are counted
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

# How the 14 days before a due date are counted

Are the 14 days in the dashboard's amber band calendar days or working days?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-004.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-014 and ST-03.

## What is unclear

BR-004 says a vehicle is amber "when it is 14 days away or less", without saying how the days are counted.

## Possible answers

1. Calendar days.
2. Working days.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 1.

## Why it matters

The day a vehicle turns amber can't be tested until this is settled.

## Answer

Possible answer 1, as the Lead BA proposed: calendar days. Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). It is BR-014 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
