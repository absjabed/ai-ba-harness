---
type: decision
id: DEC-002
title: Escalated defects are flagged at the top of the workshop queue
status: confirmed
decided_by: Product owner
decided_on: 2026-10-02
owner: Product owner
sources:
  - SRC-003
  - FK-1192
  - SRC-004
tags:
  - defects
  - workshop
created: 2026-10-06
updated: 2026-10-09
---

# Escalated defects are flagged at the top of the workshop queue

When a defect escalates, it is flagged at the top of the workshop queue of the vehicle's depot, as
well as being sent to the transport manager.

## Context

Escalations reach only the transport manager, who is often away from the depot
([R-001](../raid.md#risks)). The spike [FK-1192](https://northwind.atlassian.net/browse/FK-1192) asked
how escalated defects should reach the workshop ([SRC-003](../sources/SRC-003-2026-10-06-jira-sync.md)).

## Options considered

| Option | For | Against |
|---|---|---|
| Flag at the top of the existing workshop queue | Technicians already work from the queue; nothing new to learn | The queue gets longer at busy depots |
| A separate escalations screen | Clear separation | One more screen nobody watches on shift |
| Email only, as today | No change | Doesn't reach the workshop (R-001) |

## Decision

Flag at the top of the existing workshop queue, because the queue is where technicians already look.

This decision is **confirmed, not approved**: it was recorded second-hand. The Engineering lead wrote
in FK-1192 comment 6 that the Product owner "agreed at stand-up" on 2026-10-02. It becomes approved
when the Product owner confirms it in writing.

## Consequences

- The epic [Defect escalation to workshop](../../requirements/defect-escalation-to-workshop/requirement.md)
  builds on it ([SRC-004](../sources/SRC-004-2026-10-09-escalation-requirements-session.md)).
- [CAP-004](../domains/defects/CAP-004-escalating-unactioned-defects.md) will gain the workshop flag
  when the epic is delivered.

## Sources

- SRC-003: Jira activity 2026-09-28 to 2026-10-06; FK-1192 comment 6
- SRC-004: Requirements session, 2026-10-09, which linked the epic
