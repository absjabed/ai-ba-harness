---
type: question
id: Q-002
title: Is there a 7-day grace period before an inspection is overdue
status: approved
state: answered
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on: 2026-10-20
answer_source: SRC-007
approved_by: Product owner
approved_on: 2026-10-20
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-001, SRC-002, SRC-006, SRC-007]
tags: [inspections]
created: 2026-10-15
updated: 2026-10-20
---

# Is there a 7-day grace period before an inspection is overdue

Does the product treat an inspection done up to 7 days after its due date as not overdue, given that the regulator guidance has no grace period?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md): red means overdue (BR-004).
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-009, which uses the proposed answer below.

## What is unclear

The Product owner's rules say "An inspection done up to 7 days after its due date is not counted as overdue (grace period)" ([SRC-001](../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md), rule 4). The Compliance adviser's summary of the regulator guidance says "An inspection carried out after its due date is late. There is no grace period in the guidance; late inspections must be visible to an auditor." ([SRC-002](../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md), bullet 2)

## Possible answers

1. No grace period: an inspection is overdue from the day after its due date, as the guidance says.
2. A 7-day grace period for the dashboard colour only, while every inspection done after its due date is still recorded as late and visible to an auditor.
3. A 7-day grace period throughout, as in the Product owner's rules; the Compliance adviser would need to confirm this meets the guidance.

**Proposed answer** (the Lead BA, 2026-10-18, [SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md); for the Product owner to confirm or change): possible answer 1, no grace period: a vehicle is overdue from the day after a due date that no inspection has met, as the regulator guidance says.

## Why it matters

When a vehicle turns red, and what an auditor sees as late, can't be specified or tested until this is settled. The Product owner decides product rules; the Compliance adviser decides how the regulator guidance is read for the product, so both are needed. If the answer is possible answer 2 or 3, it is recorded as answered only once the Compliance adviser confirms it meets the guidance.

## Answer

Possible answer 1, as the Lead BA proposed: no grace period; a vehicle is overdue from the day after a due date that no inspection has met, as the regulator guidance says. Given by the Product owner on 2026-10-20 by signing off [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) "including all the proposals marked pending in it" ([SRC-007](../sources/SRC-007-2026-10-20-inspection-scheduling-sign-off.md)). The 7-day grace period in the Product owner's draft rules (SRC-001, rule 4) is not used. It is BR-009 on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).
