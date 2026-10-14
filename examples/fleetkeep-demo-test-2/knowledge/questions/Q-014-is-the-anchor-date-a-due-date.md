---
type: question
id: Q-014
title: Is a vehicle's anchor date itself a due date
status: approved
state: answered
asked_on: 2026-10-18
asked_of: Product owner
due: 2026-11-01
answered_on: 2026-10-20
answer_source: SRC-007
approved_by: Product owner
approved_on: 2026-10-20
blocks: [CAP-002]
owner: Lead BA
sources: [SRC-006, SRC-007]
tags: [inspections]
created: 2026-10-18
updated: 2026-10-20
---

# Is a vehicle's anchor date itself a due date

Is the anchor date itself one of the vehicle's due dates, or is the first due date the anchor date plus one interval?

## Where it comes up

- [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), rule BR-003.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-006 and ST-02.

## What is unclear

The glossary defines each due date as "the anchor date plus a whole number of the vehicle's inspection intervals" (T-001, [glossary](../glossary.md#anchor-date)). A whole number can be zero, so it isn't clear whether the anchor date is a due date itself.

## Possible answers

1. No: the first due date is the anchor date plus one interval.
2. Yes: the anchor date is the first due date.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 1.

## Why it matters

If the anchor date is a due date, a vehicle given an anchor date in the past is overdue straight away. The due date calculation can't be tested until this is settled.

## Answer

Possible answer 1, as the Lead BA proposed: the first due date is the anchor date plus one interval; the anchor date itself is not a due date. Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). It is BR-008 on [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md).
