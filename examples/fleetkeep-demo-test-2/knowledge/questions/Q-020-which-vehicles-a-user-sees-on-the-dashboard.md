---
type: question
id: Q-020
title: Which vehicles a user sees on the inspection dashboard
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
tags: [inspections, tenancy-and-access]
created: 2026-10-22
updated: 2026-10-22
---

# Which vehicles a user sees on the inspection dashboard

Which vehicles does the inspection dashboard list for a transport manager or a compliance officer: only those of their own operator, or every operator's?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), rule BR-018, which says who can see the dashboard but not which vehicles it lists.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-020, ST-03 and ST-05.

## What is unclear

The review of the requirement on 2026-10-20 noted that the product serves more than one operator, but nothing in the knowledge base says whether a user sees only their own operator's vehicles on the dashboard.

## Possible answers

1. Only the vehicles of the user's own operator.
2. Every operator's vehicles.

## Why it matters

Which vehicles the dashboard lists, and the test that another operator's vehicles stay hidden, can't be specified until this is settled.

## Proposed answer

The Lead BA, 2026-10-22 ([SRC-009](../sources/SRC-009-2026-10-22-inspection-dashboard-proposals.md)); for the Product owner to confirm or change: possible answer 1. The rule it would become, on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md): "A user sees on the inspection dashboard only the vehicles of their own operator."

## Answer
