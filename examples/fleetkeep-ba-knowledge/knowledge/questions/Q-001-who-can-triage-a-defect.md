---
type: question
id: Q-001
title: Who can triage a defect and raise its job card?
status: confirmed
state: answered
asked_on: 2026-09-16
asked_of: Product owner
due: 2026-09-30
answered_on: 2026-10-06
answer_source: SRC-003
blocks:
  - CAP-002
  - ENT-003
owner: Lead BA
sources:
  - SRC-001
  - SRC-003
  - FK-1192
tags:
  - defects
created: 2026-09-17
updated: 2026-10-06
---

# Who can triage a defect and raise its job card?

Which FleetKeep roles can triage a reported defect, reject it, or raise a job card for it?

## Where it comes up

- [Triaging a defect](../domains/defects/CAP-002-triaging-a-defect.md)
- [Transport manager](../entities/ENT-003-transport-manager.md)

## What is unclear

In the discovery workshop the Pilot workshop supervisor said technicians "sort out" new defects at
the start of a shift, while the Pilot transport manager said triage was theirs
([SRC-001](../sources/SRC-001-2026-09-16-discovery-workshop.md)). The role list gives technicians
"read and progress job cards" but doesn't mention triage.

## Possible answers

1. Only the transport manager triages; technicians work on job cards once raised.
2. Technicians can triage defects at their own depot as well.

## Why it matters

The triage screen's permissions, and who escalations should go to, depend on it.

## Answer

Only a transport manager can triage a defect, reject it or raise a job card for it; technicians can't
triage. The Engineering lead confirmed this is how FleetKeep works today in
[FK-1192](https://northwind.atlassian.net/browse/FK-1192) comment 4, on 2026-10-01. This describes
how the product behaves, so it is recorded as a confirmed fact (BR-014 on CAP-002), not a decision.
Source:
[SRC-003](../sources/SRC-003-2026-10-06-jira-sync.md).
