---
type: question
id: Q-003
title: What happens when a driver submits a check with no signal?
status: confirmed
state: open
asked_on: 2026-09-24
asked_of: Product owner
due: 2026-10-30
answered_on:
answer_source:
blocks:
  - CAP-001
  - R-002
owner: Lead BA
sources:
  - SRC-002
tags:
  - defects
created: 2026-09-24
updated: 2026-09-24
---

# What happens when a driver submits a check with no signal?

What should happen when a driver completes a walkaround check, or reports a defect, at a depot with
no mobile signal?

## Where it comes up

- [Reporting a defect from a walkaround check](../domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md)
- Risk [R-002](../raid.md#risks)

## What is unclear

The regulator's guidance expects a check before the vehicle is used
([SRC-002](../sources/SRC-002-2026-09-23-regulator-roadworthiness-guidance.md)), and depot signal is
known to be poor. Nothing says whether a check can be completed without a signal, or how its time is
recorded if it is sent later.

## Possible answers

1. The check is kept on the phone and sent when signal returns, with the time it was completed.
2. The driver can't submit until there is signal, and uses the depot's paper fallback meanwhile.
3. A depot administrator enters paper checks afterwards.

## Why it matters

A category-A defect only sets the vehicle to VOR once it reaches FleetKeep (BR-003). Until this is
answered, nobody can say how long an immobilising defect might go unrecorded.

## Answer
