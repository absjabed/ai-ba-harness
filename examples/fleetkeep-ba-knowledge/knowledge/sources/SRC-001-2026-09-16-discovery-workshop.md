---
type: source
id: SRC-001
title: Discovery workshop on defects, the workshop and return to service
status: confirmed
kind: meeting
input_date: 2026-09-16
created: 2026-09-17
updated: 2026-09-17
---

# Discovery workshop on defects, the workshop and return to service

A half-day workshop with the pilot operator that walked through a defect from the driver's report to
the vehicle going back on the road, and gave the knowledge base its first glossary, capabilities and
open questions.

## Details

| Field | Value |
|---|---|
| Kind | meeting |
| Date | 2026-09-16 |
| Participants or author | Product owner, Lead BA, Engineering lead, Compliance adviser, Pilot transport manager, Pilot workshop supervisor |
| Original | Lead BA's typed notes and whiteboard photos, on the team shared drive under FleetKeep / Discovery / 2026-09-16 (not in this repository) |
| Processed by | /intake on 2026-09-17 |

## Summary

The group traced a defect through FleetKeep: a driver reports it in the walkaround check with a
category (A, B or C); a category-A defect takes the vehicle off the road at once; the transport
manager triages it; the workshop works a job card and closes it with labour, parts and a signature;
and the transport manager authorises return to service. The Product owner decided the escalation
clock starts when a defect is reported. Two disagreements were left open: who triages (the Pilot
workshop supervisor and the Pilot transport manager gave different accounts) and whether escalations
should wait for working hours. The Pilot workshop supervisor's main complaint was that escalations
never reach the workshop.

## What it changed

| Item | Change |
|---|---|
| T-001 to T-011 | Created: eleven glossary terms, from walkaround check to compliance banding |
| STAKEHOLDERS | Edited: confirmed the roles drafted by /setup, added the two pilot roles |
| CAP-001 | Created: reporting a defect from a walkaround check, BR-001 to BR-004 |
| CAP-002 | Created: triaging a defect, BR-005 and BR-006 |
| CAP-003 | Created: escalating an unactioned category-A defect, BR-007 and BR-008 (superseded on 2026-10-06) |
| CAP-005 | Created as draft: closing a job card, BR-009 to BR-011 |
| ENT-001, ENT-002, ENT-003 | Created: Defect, Vehicle (draft), Transport manager |
| PROC-001 | Created: from defect report to return to service, BR-012 |
| DEC-001 | Created, approved: the escalation clock starts at the report |
| Q-001 | Opened: who can triage a defect |
| Q-002 | Opened: does the escalation clock run outside working hours |
| A-001 | Added: one check can carry several defects |
| R-001 | Added: escalations reach only the transport manager |

## Rejected items

- **Vendor support should be able to triage for small operators** (Customer support lead's
  suggestion, relayed by the Product owner). Rejected: vendor support access is read-only, and the
  Product owner said it is out of scope for the pilot.
- **A daily email of parts below reorder level.** Rejected: a passing idea that nobody owned; the
  reorder alert already exists (CAP-005).
