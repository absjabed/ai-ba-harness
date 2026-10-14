---
type: question
id: Q-004
title: What does the dashboard show for a vehicle with no anchor date?
status: confirmed
state: open
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on:
answer_source:
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-002]
tags: [inspections]
created: 2026-10-15
updated: 2026-10-15
---

# What does the dashboard show for a vehicle with no anchor date?

What does the dashboard show for a vehicle that has no anchor date, and so no next due date?

## Where it comes up

- [CAP-003 Seeing inspection due status on the dashboard](../domains/inspections/CAP-003-seeing-inspection-due-status-on-the-dashboard.md) (BR-003).
- Requirement REQ-inspection-due-dates-and-dashboard-banding.

## What is unclear

BR-003 bands each vehicle by its next due date as green, amber or red; a vehicle with no anchor date
has no due date. The Lead BA's view is that it "shows grey 'Not scheduled'"
([SRC-002](../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md)). That adds a fourth
state to the Product owner's three-band decision
([DEC-002](../decisions/DEC-002-inspection-due-banding.md)), which only the Product owner can decide.
The due date was set for 2026-10-29 by the Lead BA.

## Possible answers

1. Grey, labelled "Not scheduled" (the Lead BA's view).
2. Red, so a missing schedule is treated as a problem.
3. Left off the dashboard.

## Why it matters

What the dashboard shows for vehicles without a schedule can't be built or tested until this is
decided.

## Answer

