---
type: question
id: Q-004
title: What state does a deferred defect take when its job card closes?
status: confirmed
state: open
asked_on: 2026-10-09
asked_of: Product owner
due: 2026-10-23
answered_on:
answer_source:
blocks:
  - CAP-005
  - ENT-001
  - REQ-defect-escalation-to-workshop
owner: Lead BA
sources:
  - SRC-004
tags:
  - defects
  - workshop
created: 2026-10-09
updated: 2026-10-09
---

# What state does a deferred defect take when its job card closes?

When a technician closes a job card with a defect deferred, which state does that defect take, and
does it come back to the workshop queue?

## Where it comes up

- [Closing a job card](../domains/workshop/CAP-005-closing-a-job-card.md) (BR-010)
- [Defect](../entities/ENT-001-defect.md), lifecycle
- [Defect escalation to workshop](../../requirements/defect-escalation-to-workshop/requirement.md), marked non-blocking

## What is unclear

A job card can close when "every linked defect is resolved or deferred with a reason" (BR-010), but
the defect's states are Reported, Triaged, Job card raised, In progress, Resolved, Closed and
Rejected, with no deferred state and no step backwards (BR-005). Found while writing the escalation
requirement ([SRC-004](../sources/SRC-004-2026-10-09-escalation-requirements-session.md)).

## Possible answers

1. The defect stays In progress and goes on the next job card for the vehicle.
2. A new Deferred state is added, from which the defect returns to the queue.
3. The defect is Resolved with a note, and a new defect is raised for the remaining work.

## Why it matters

It decides whether deferred defects are visible to the workshop, and whether a deferred category-B
defect can be forgotten past its 48 hours. It doesn't block the escalation epic, because escalation
stops once a job card is raised.

## Answer
