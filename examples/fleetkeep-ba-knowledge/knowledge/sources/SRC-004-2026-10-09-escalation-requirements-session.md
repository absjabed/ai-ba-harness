---
type: source
id: SRC-004
title: Requirements session on defect escalation to the workshop
status: confirmed
kind: conversation
input_date: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Requirements session on defect escalation to the workshop

The Lead BA's working session in Claude Code while writing the requirement for escalated defects to
reach the workshop, captured with `/intake` at the end of the session.

## Details

| Field | Value |
|---|---|
| Kind | conversation |
| Date | 2026-10-09 |
| Participants or author | Lead BA, working with Claude Code |
| Original | Not kept (a conversation) |
| Processed by | /intake on 2026-10-09 |

## Summary

While turning DEC-002 and FK-1192 into a requirement, the session found that a job card can close
with a defect deferred, but the defect has no deferred state, and raised it as a question. It
recorded two assumptions the requirement relies on (technicians look at the queue each shift; email
is the only notification channel) and a dependency on the pilot depots' shift patterns. It linked the
new requirement from the pages it builds on. No decisions were made: the Lead BA can't decide product
behaviour.

## What it changed

| Item | Change |
|---|---|
| Q-004 | Opened: what state a deferred defect takes when its job card closes |
| CAP-004, DEC-002, PROC-001, Q-002 | Edited: linked the requirement [Defect escalation to workshop](../../requirements/defect-escalation-to-workshop/requirement.md) |
| CAP-005, ENT-001 | Edited: added the caution linking Q-004 |
| A-002, A-003 | Added: the two assumptions |
| D-001 | Added: depot shift patterns |

## Rejected items

None.
