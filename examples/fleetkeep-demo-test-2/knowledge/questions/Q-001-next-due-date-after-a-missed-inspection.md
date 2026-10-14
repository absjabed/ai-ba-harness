---
type: question
id: Q-001
title: Which due date is next after a missed or early inspection
status: approved
state: answered
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on: 2026-10-20
answer_source: SRC-007
approved_by: Product owner
approved_on: 2026-10-20
blocks: [CAP-002, CAP-003]
owner: Lead BA
sources: [SRC-001, SRC-006, SRC-007]
tags: [inspections]
created: 2026-10-15
updated: 2026-10-20
---

# Which due date is next after a missed or early inspection

When an inspection is missed or done early, which "anchor date plus a whole number of intervals" is the vehicle's next due date?

## Where it comes up

- [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), rule BR-003.
- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-004, which bands on the next due date.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-007, FR-008, FR-010, FR-013 and FR-019, which use the proposed answer below.

## What is unclear

The rules say "The next due date is the anchor date plus a whole number of intervals; doing an inspection early or late doesn't move the schedule" ([SRC-001](../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md), rule 2). They don't say which multiple of the interval counts as next when the last due date passed without an inspection, or when an inspection was done before its due date.

## Possible answers

1. The next due date is the earliest one not yet covered by an inspection: a missed inspection stays due (and overdue) until it is done, and an early inspection covers the due date it was done ahead of.
2. The next due date is the earliest one after today: a missed due date drops off once the following one comes round, and the miss shows only in the inspection history.
3. The next due date is the first one after today that no inspection has met, and a missed due date stays overdue until an inspection is recorded that meets it. An inspection meets every unmet due date on or before the day it is done; when there is none, it meets the first due date after that day.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 3. Read literally, "after today" means that on the due date itself the vehicle is measured against the following due date, and since it isn't overdue until the next day, a vehicle not yet inspected shows green (or amber, for a 2-week interval) on the day its inspection is due. The Product owner is asked whether the due date itself should count ("on or after today").

## Why it matters

The dashboard status and any overdue reporting can't be specified or tested until it is known which due date a vehicle is measured against.

## Answer

Possible answer 3, as the Lead BA proposed: an inspection meets every unmet due date on or before the day it is done, and when there is none, the first due date after that day; a vehicle's next due date is the first due date after today that no inspection has met; a missed due date stays overdue until an inspection is recorded that meets it, and an overdue vehicle shows red whatever its next due date. Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "as written, including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). The sign-off approves "after today" as written, so on its due date a vehicle not yet inspected is measured against the following due date, and it is overdue from the next day. Whether the due date itself should count was not answered separately; it is asked in [Q-019](Q-019-measuring-a-vehicle-on-its-due-date.md). It is BR-010 and BR-011 on [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), and BR-012 and BR-013 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
