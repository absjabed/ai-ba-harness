---
type: question
id: Q-011
title: What happens to a vehicle's record and schedule when it is re-registered
status: confirmed
state: open
asked_on: 2026-10-17
asked_of: Product owner
due: 2026-10-31
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-001]
owner: Lead BA
sources: [SRC-005]
tags: [vehicles, inspections]
created: 2026-10-17
updated: 2026-10-17
---

# What happens to a vehicle's record and schedule when it is re-registered

When a vehicle is re-registered, does it keep its record, inspection interval and anchor date, and how does the product stop two vehicles sharing one record?

## Where it comes up

- [Setting a vehicle's inspection interval and anchor date](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md).
- R-003 in the [RAID log](../raid.md).

## What is unclear

The Engineering lead reports that anchor dates are kept per vehicle today, "but nothing stops two vehicles sharing a record when a vehicle is re-registered, which could double up their schedules" ([SRC-005](../sources/SRC-005-2026-10-17-anchor-dates-and-vor.md), sentence 2). Nothing in the knowledge base says what re-registering a vehicle should do to its record or its inspection schedule.

## Possible answers

1. The vehicle keeps its record, interval and anchor date; only its registration changes, and the product never lets two vehicles share one record.
2. Something else the Product owner decides.

## Why it matters

Each vehicle has its own interval and anchor date (BR-001); if two vehicles can share a record, their inspection schedules can double up.

## Answer
