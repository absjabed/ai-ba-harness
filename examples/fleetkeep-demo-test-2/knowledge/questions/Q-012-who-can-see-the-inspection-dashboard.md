---
type: question
id: Q-012
title: Who can see the inspection dashboard
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
tags: [inspections, tenancy-and-access]
created: 2026-10-18
updated: 2026-10-20
---

# Who can see the inspection dashboard

Which product roles can see the inspection dashboard, and can any of them change a vehicle's schedule from it?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-018 and ST-05.

## What is unclear

The knowledge base says what the dashboard shows (BR-004) but not who can see it. Only a transport manager sets or changes a vehicle's inspection interval or anchor date (BR-002, on [CAP-001](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md)).

## Possible answers

1. Transport managers and compliance officers; compliance officers can look but not change anything (they can't change intervals or anchor dates anyway, by BR-002).
2. Transport managers only.
3. Every product role.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 1.

## Why it matters

The dashboard's access, and the stories for compliance officers, can't be built or tested until it is known who sees it.

## Answer

Possible answer 1, as the Lead BA proposed: transport managers and compliance officers; compliance officers can look but not change anything (they can't change intervals or anchor dates anyway, by BR-002). Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). It is BR-018 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
