---
type: register
id: RAID
title: Risks, assumptions, issues and dependencies
status: confirmed
owner: Lead BA
sources:
  - SRC-001
  - SRC-002
  - SRC-003
  - SRC-004
created: 2026-09-17
updated: 2026-10-09
---

# Risks, assumptions, issues and dependencies

The project's risks (R-), assumptions (A-), issues (I-) and dependencies (D-), one table each, with
the source each came from.

## Risks

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status | Source |
|---|---|---|---|---|---|---|---|
| R-001 | Escalations reach only the transport manager, who is often away from the depot, so a category-A vehicle stays off the road longer than needed | High | High | Flag escalated defects on the depot's workshop queue ([DEC-002](decisions/DEC-002-escalated-defects-top-of-workshop-queue.md), and the epic it led to) | Product owner | Open | [SRC-001](sources/SRC-001-2026-09-16-discovery-workshop.md) |
| R-002 | Poor signal at depots delays or loses walkaround checks, so a vehicle could be used without a recorded check | Medium | High | Decide the no-signal behaviour ([Q-003](questions/Q-003-walkaround-check-without-a-signal.md)) | Product owner | Open | [SRC-002](sources/SRC-002-2026-09-23-regulator-roadworthiness-guidance.md) |

## Assumptions

| ID | Assumption | Why we assume it | How to confirm | Owner | Status | Source |
|---|---|---|---|---|---|---|
| A-001 | One walkaround check can carry several defects, each with its own category | Every example in the discovery workshop had more than one fault on a vehicle | Walk through a check with the Engineering lead | Lead BA | Open | SRC-001 |
| A-002 | Technicians look at the workshop queue at the start of every shift | The Pilot workshop supervisor described a shift handover at the queue screen | Compare with the pilot depots' shift patterns (D-001) | Lead BA | Open | [SRC-004](sources/SRC-004-2026-10-09-escalation-requirements-session.md) |
| A-003 | Escalations to technicians go by email, the only notification channel FleetKeep has today | Every notification described in the sources is an email | Ask the Engineering lead | Lead BA | Open | SRC-004 |

## Issues

| ID | Issue | Impact | Action | Owner | Status | Source |
|---|---|---|---|---|---|---|
| I-001 | Audit packs for long date ranges fail to generate | A compliance officer can't produce a full 15-month pack in one go | Export in shorter date ranges until FK-1197 is fixed | Engineering lead | Open | [SRC-003](sources/SRC-003-2026-10-06-jira-sync.md) |

## Dependencies

| ID | We depend on | For | Needed by | Owner | Status | Source |
|---|---|---|---|---|---|---|
| D-001 | The pilot depots' shift patterns, from the Pilot workshop supervisor | Answering [Q-002](questions/Q-002-escalation-clock-outside-working-hours.md) and checking A-002 | 2026-10-21 | Lead BA | Open | SRC-004 |
