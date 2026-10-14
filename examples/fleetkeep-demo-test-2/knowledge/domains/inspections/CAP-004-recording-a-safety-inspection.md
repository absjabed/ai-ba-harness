---
type: capability
id: CAP-004
title: Recording a safety inspection
status: confirmed
area: inspections
owner: Product owner
sources: [SRC-001, SRC-002, SRC-004]
rules: [BR-005]
aliases: []
tags: [inspections]
created: 2026-10-15
updated: 2026-10-17
---

# Recording a safety inspection

A safety inspection is recorded against its vehicle, including the result of its brake performance test ([SRC-001](../../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md)).

## Who and when

| Role | What they do here | When |
|---|---|---|

## What the user sees

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Brake performance test result | Yes | BR-005 |

## Rules applied

In the order they are evaluated.

1. **BR-005** Every safety inspection includes a brake performance test, and its result is recorded. (SRC-001)

> [!IMPORTANT]
> The regulator guidance, as summarised by the Compliance adviser, requires each safety inspection to include a brake performance test, with the result kept ([SRC-002](../../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)).

## Outcomes

> [!IMPORTANT]
> The regulator guidance, as summarised by the Compliance adviser, requires inspection records to be kept for at least 15 months ([SRC-002](../../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)).

> [!IMPORTANT]
> The regulator guidance, as summarised by the Compliance adviser, requires late inspections to be visible to an auditor ([SRC-002](../../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)).

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|

## Interactions

## Open items

> [!CAUTION]
> **Unresolved:** the date the 15 months of record keeping count from, and who keeps the records. See [Q-004](../../questions/Q-004-when-15-month-record-keeping-starts.md).

> [!CAUTION]
> **Unresolved:** where and how an auditor sees late inspections. See [Q-005](../../questions/Q-005-how-an-auditor-sees-late-inspections.md).

> [!CAUTION]
> **Unresolved:** what a brake test result records: a pass or fail, a reading, or both. See [Q-009](../../questions/Q-009-what-a-brake-test-result-records.md).

> [!CAUTION]
> **Unresolved:** whether an inspection can be closed when its brake test fails. See [Q-010](../../questions/Q-010-closing-an-inspection-after-a-failed-brake-test.md).

## Sources

- SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
- SRC-002: the Compliance adviser's regulator guidance summary, 2026-10-05
- SRC-004: the Compliance adviser's email on brake test results, 2026-10-17
