---
type: question
id: Q-006
title: Which due date does a recorded safety inspection satisfy?
status: confirmed
state: open
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on:
answer_source:
blocks: [CAP-002]
owner: Lead BA
sources: [SRC-002]
tags: [inspections]
created: 2026-10-15
updated: 2026-10-15
---

# Which due date does a recorded safety inspection satisfy?

When a safety inspection is recorded, which of the vehicle's due dates does it count for?

## Where it comes up

- [CAP-002 Calculating the next safety inspection due date](../domains/inspections/CAP-002-calculating-the-next-inspection-due-date.md) (BR-002).
- [CAP-004 Recording a safety inspection](../domains/inspections/CAP-004-recording-a-safety-inspection.md).
- Requirement REQ-inspection-due-dates-and-dashboard-banding.

## What is unclear

BR-002 says neither a late nor an early inspection moves the schedule, but not which due date an
inspection counts for, so it isn't defined when a vehicle stops being overdue or moves on to its next
due date. The Lead BA gave no specific answer; the recommended option was adopted as the working
answer: "The earliest due date not yet satisfied, provided the inspection was done after the due
date before that one (or after the anchor date, for the first); early or late, it doesn't move the
dates" ([SRC-002](../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md)). Also open:
does an inspection done on the previous due date itself count, and does an inspection closed without
a brake test result count ([Q-002](Q-002-block-closing-an-inspection-without-a-brake-test.md))? The
due date was set for 2026-10-29 by the Lead BA.

## Possible answers

1. The earliest due date not yet satisfied, if the inspection was done after the due date before it
   (recommended).
2. Only inspections done within a set number of days before a due date count for it.

## Why it matters

Whether a vehicle is overdue, and what its next due date is, can't be built or tested until this is
decided.

## Answer

