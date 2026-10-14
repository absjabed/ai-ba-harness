---
type: decision
id: DEC-003
title: Amber starts 21 days before a vehicle's next due date
status: approved
decided_by: Product owner
decided_on: 2026-10-22
approved_by: Product owner
approved_on: 2026-10-22
owner: Product owner
sources: [SRC-008]
tags: [inspections]
created: 2026-10-22
updated: 2026-10-22
---

# Amber starts 21 days before a vehicle's next due date

A vehicle shows amber on the inspection dashboard when its next due date is 21 days away or less, instead of 14.

## Context

BR-004 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md) banded a vehicle amber when its next due date was 14 days away or less ([SRC-001](../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md)), and the Product owner signed it off with the [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) requirement on 2026-10-20 ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). On 2026-10-22 the Product owner changed it ([SRC-008](../sources/SRC-008-2026-10-22-amber-band-change.md)).

## Options considered

Not recorded in the source.

| Option | For | Against |
|---|---|---|

## Decision

The Product owner decided that amber starts at 21 days, not 14; green stays "more than that" and red stays overdue. The reason given: customers want more notice.

## Consequences

- On [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), BR-004 is superseded by BR-019.
- The days are still counted as calendar days (BR-014), and an overdue vehicle still shows red whatever its next due date (BR-013).
- The answered questions that cite BR-004 or the 14 days ([Q-015](../questions/Q-015-how-the-14-days-before-a-due-date-are-counted.md), Q-001, Q-002, Q-012, Q-013 and Q-016) stay as they are, as a record of what was answered then; Q-015's answer, calendar days (BR-014), applies to the 21 days as well.
- The approved [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) requirement states the 14 days in its Current state, in FR-012 and in ST-03 (the story statement and AC-2, whose vehicle due 15 days ahead would now show amber), and needs updating.

## Sources

- SRC-008: the Product owner's email of 2026-10-22, paragraph 1
