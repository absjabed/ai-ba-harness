---
type: source
id: SRC-003
title: Defects workshop
status: confirmed
kind: meeting
input_date: 2026-10-16
created: 2026-10-17
updated: 2026-10-17
---

# Defects workshop

The Lead BA's notes from the defects workshop on 2026-10-16, the first material on the defects area.

## Details

| Field | Value |
|---|---|
| Kind | meeting |
| Date | 2026-10-16 |
| Participants or author | Product owner, Lead BA, Engineering lead, Pilot workshop supervisor; notes by the Lead BA |
| Original | The BA's own copy (`inbox/2026-10-16-defects-workshop.md` on the machine it was staged on, not committed) |
| Processed by | /intake: staged 2026-10-16, decided and applied 2026-10-17 by the BA on another machine |

## Summary

Drivers report defects during the walkaround check, each with a category A, B or C. The Product owner decided that a category-A defect takes the vehicle off the road (VOR) immediately, and that every defect gets a decision from the transport manager first. The Pilot workshop supervisor said technicians at the pilot customer sometimes clear category-C defects without a job card. Nobody knew whether a defect can be re-categorised after it is reported; the Product owner is to decide. The Engineering lead will list the defect states the system has today by 2026-10-23. The notes define the walkaround check as the driver's check of the vehicle before using it; the Pilot workshop supervisor calls it the "daily check". The supervisor's name in the notes is not recorded here.

## What it changed

| Item | Change |
|---|---|
| CAP-005 | created: reporting a defect in a walkaround check, with BR-006 and three cautions |
| Q-006 | opened: what defect categories B and C mean (Product owner) |
| DEC-001 | recorded, approved by the Product owner: a category-A defect makes the vehicle VOR immediately |
| BR-006 | added on CAP-005 |
| Q-003 | edited: one cause of VOR recorded (DEC-001), link to CAP-005; still open |
| DEC-002 | recorded, approved by the Product owner: every defect gets a decision from the transport manager first |
| CAP-006 | created: deciding what happens to a reported defect, with BR-007 and today's practice at the pilot customer |
| BR-007 | added on CAP-006 |
| Q-007 | opened: what the transport manager decides on a defect, and what it comes before (Product owner) |
| ENT-001 | edited: new permission (BR-007) and link to CAP-006 |
| Q-008 | opened: whether a defect can be re-categorised after it is reported (Product owner) |
| ACT-001 | added: Engineering lead to list today's defect states, due 2026-10-23 |
| T-004 | added: Walkaround check (also called daily check) |
| T-005 | added: VOR (also called grounded) |

## Play-back

> Subject: Defects workshop, 16 October 2026: what we recorded
>
> Thank you for the workshop. This is what we recorded; please reply if anything is wrong.
>
> **Decided (by Product owner)**
> - A category-A defect takes the vehicle off the road (VOR) immediately.
> - Every defect gets a decision from the transport manager first.
>
> **Still open**
> - Whether a defect can be re-categorised after it is reported. The Product owner will decide.
>
> **Follow-up questions for the Product owner**
> - What makes a defect category B or C, and what follows from each?
> - Which decisions can the transport manager make on a defect, and what does that decision come before?
>
> **Actions**
> - Engineering lead: list the defect states the system has today, by 23 October 2026.
>
> **Terms**
> - Walkaround check: the driver's check of the vehicle before using it. Also called the daily check; we will use "walkaround check".

## Rejected, ignored and declined

- Critic's missed point (declined by the BA): a RAID risk or issue about the pilot workshop clearing category-C defects without a job card or a transport manager decision. Not added; the practice is recorded as a fact on CAP-006.
- Critic's date finding (not taken): the critic took the session date as 2026-10-15. The items were applied on 2026-10-17, so pages carry `created` 2026-10-17 and questions are due 2026-10-31; the decisions keep `decided_on` 2026-10-16, the meeting date.
