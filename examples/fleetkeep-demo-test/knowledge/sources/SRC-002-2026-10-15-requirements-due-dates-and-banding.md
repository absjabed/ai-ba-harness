---
type: source
id: SRC-002
title: Requirements clarification session, inspection due dates and banding
status: confirmed
kind: conversation
input_date: 2026-10-15
created: 2026-10-15
updated: 2026-10-15
---

# Requirements clarification session, inspection due dates and banding

The Lead BA's answers to the clarification questions of `/requirements inspection due dates and
dashboard banding` on 2026-10-15, including the Product owner's answer to Q-003, relayed by the
Lead BA.

## Details

| Field | Value |
|---|---|
| Kind | conversation |
| Date | 2026-10-15 |
| Participants or author | Lead BA, with the assistant running `/requirements`. The Product owner's answer to Q-003 came by email, relayed by the Lead BA |
| Original | Not kept (the conversation); the Product owner's email isn't in this repository |
| Processed by | /requirements on 2026-10-15 |

## Summary

Nine questions were asked. The Lead BA set the requirement's scope: per-vehicle intervals, due-date
calculation from the anchor date and dashboard banding; brake-test enforcement (Q-002), VOR
behaviour (Q-001) and notifications out. The Lead BA's view is that transport managers set intervals
and see the dashboard and compliance officers see it read-only; that banding counts calendar days
and a vehicle due today is amber; that a vehicle with no anchor date shows grey "Not scheduled"; and
that changing an interval recalculates the next due date from the same anchor date. For which due
date a recorded inspection satisfies, and for the interval's unit, the Lead BA gave no specific
answer and the assistant's recommended options were adopted as working answers. The Product owner
set the dashboard's load time: under 3 seconds for fleets of up to 2,000 vehicles. Proposed fix
version: 2026.12. Except for the day-counting rule, which reads the Product owner's banding
decision literally, the Lead BA's product-behaviour answers went to the Product owner as questions,
because stakeholders.md reserves product behaviour for the Product owner.

## What it changed

| Item | Change |
|---|---|
| [Q-003](../questions/Q-003-dashboard-load-time-for-large-fleets.md) | answered (Product owner, relayed); approved |
| [DEC-003](../decisions/DEC-003-dashboard-load-time-for-large-fleets.md) | created (approved, Product owner) |
| [CAP-003](../domains/inspections/CAP-003-seeing-inspection-due-status-on-the-dashboard.md) | edited: load-time target, BR-005 added, Q-003 callout removed, Q-004, Q-008 and A-001 callouts added, alias "RAG banding" |
| [CAP-002](../domains/inspections/CAP-002-calculating-the-next-inspection-due-date.md) | edited: Q-005, Q-006 and A-001 callouts |
| [CAP-001](../domains/vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md) | edited: Q-007 and Q-008 callouts |
| [Q-004](../questions/Q-004-no-anchor-date-on-the-dashboard.md) | opened, asked of the Product owner |
| [Q-005](../questions/Q-005-due-date-after-an-interval-change.md) | opened, asked of the Product owner |
| [Q-006](../questions/Q-006-which-due-date-an-inspection-satisfies.md) | opened, asked of the Product owner |
| [Q-007](../questions/Q-007-interval-unit-and-range.md) | opened, asked of the Product owner |
| [Q-008](../questions/Q-008-who-sets-intervals-and-sees-the-dashboard.md) | opened, asked of the Product owner |
| BR-005 | added on CAP-003: banding counts calendar days; due today is amber |
| T-002 | added to [glossary.md](../glossary.md#inspection-due-status): inspection due status |
| A-001 | added to [raid.md](../raid.md#assumptions): VOR vehicles banded like any other until Q-001 is answered |

## Rejected items

No item was rejected. Not stored, so it isn't proposed again:

- The requirement's scope as a decision: ignored, because the scope of one epic is held in
  `requirements/inspection-due-dates-and-dashboard-banding/requirement.md` and confirmed when the
  Product owner signs it off.
