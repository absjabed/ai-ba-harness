---
type: question
id: Q-017
title: Which inspection intervals and anchor dates the product refuses
status: confirmed
state: open
asked_on: 2026-10-18
asked_of: Product owner
due: 2026-11-01
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-001]
owner: Lead BA
sources: [SRC-006]
tags: [inspections]
created: 2026-10-18
updated: 2026-10-18
---

# Which inspection intervals and anchor dates the product refuses

Which inspection intervals and anchor dates does the product refuse, and must a vehicle's interval and anchor date be set together?

## Where it comes up

- [Setting a vehicle's inspection interval and anchor date](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md), rule BR-001.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), ST-01.

## What is unclear

BR-001 says the interval is set in whole weeks, but not whether 0 weeks is allowed, or whether there is a longest interval. The interval is required ([SRC-002](../sources/SRC-002-2026-10-05-regulator-inspection-guidance.md)). The calculation needs an anchor date ([CAP-002](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md), Inputs), but whether it must be given when the schedule is set is "Not stated in the source" on the capability page, and nothing says whether an anchor date can be in the future.

## Possible answers

1. The interval is always required, a whole number of weeks from 1 up; the anchor date can be set later, and any date is allowed.
2. Limits the Product owner sets for the interval, the anchor date, or both.

## Why it matters

Without it, the stories can test only the refusal of an interval that isn't in whole weeks; the other refusals can't be specified.

## Answer
