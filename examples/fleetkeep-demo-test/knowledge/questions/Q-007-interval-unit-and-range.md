---
type: question
id: Q-007
title: What unit and range can a safety inspection interval have?
status: confirmed
state: open
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on:
answer_source:
blocks: [CAP-001]
owner: Lead BA
sources: [SRC-002]
tags: [vehicles, inspections]
created: 2026-10-15
updated: 2026-10-15
---

# What unit and range can a safety inspection interval have?

In what unit is a vehicle's safety inspection interval set, and what are its smallest and largest
values?

## Where it comes up

- [CAP-001 Setting a vehicle's safety inspection interval](../domains/vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md) (BR-001).
- Requirement REQ-inspection-due-dates-and-dashboard-banding.

## What is unclear

CAP-001 gives the pilot customer's 6 weeks for HGVs and 8 weeks for vans as their practice, not a
product default; no unit or range is set. The Lead BA gave no specific answer; the recommended option
was adopted as the working answer: "whole weeks, at least 1, no product maximum until the regulator
guidance (ACT-001)" ([SRC-002](../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md)).
The Compliance adviser should be consulted once the regulator's guidance arrives
([ACT-001](../raid.md#actions)). The due date was set for 2026-10-29 by the Lead BA.

## Possible answers

1. Whole weeks, at least 1, no maximum until the regulator's guidance (recommended).
2. Days.
3. Months.

## Why it matters

Setting an interval, checking the value entered, and the due-date arithmetic can't be built or
tested until this is decided.

## Answer

