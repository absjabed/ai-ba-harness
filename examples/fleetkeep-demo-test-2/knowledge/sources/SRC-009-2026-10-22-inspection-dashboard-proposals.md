---
type: source
id: SRC-009
title: Lead BA's proposals on the inspection dashboard
status: confirmed
kind: conversation
input_date: 2026-10-22
created: 2026-10-22
updated: 2026-10-22
---

# Lead BA's proposals on the inspection dashboard

The Lead BA's answers to the clarifying questions while updating the inspection scheduling and dashboard requirement for the 21-day amber band; every answer about product behaviour is a proposal for the Product owner.

## Details

| Field | Value |
|---|---|
| Kind | conversation |
| Date | 2026-10-22 |
| Participants or author | Lead BA |
| Original | Not kept; the answers are recorded in the Clarifications (session 2026-10-22) of [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) |
| Processed by | /requirements on 2026-10-22 |

## Summary

The requirement was updated after the Product owner changed the amber band to 21 days (DEC-003). Scope of the update (the Lead BA's own): the 21-day band, bringing the document in line with the knowledge base and the 2026-10-20 review, and raising the review's open gaps as proposals. The Lead BA proposed that a user sees only their own operator's vehicles on the dashboard, that an empty dashboard shows the message "No vehicles to show", that overdue vehicles are listed by their oldest missed due date first (Q-018), and that vehicles the order doesn't separate are listed by registration number, A to Z. None of these is a rule yet: the Lead BA can't decide product behaviour (stakeholders register), so each is a question to the Product owner with the proposed answer, settled by the Product owner's sign-off of the updated requirement. The Lead BA also set the document back to draft, with its 2026-10-20 approval cleared, until the Product owner signs off this version.

## What it changed

| Item | Change |
|---|---|
| Q-020 | opened: which vehicles a user sees on the inspection dashboard (Product owner), with a proposed answer |
| Q-021 | opened: what the dashboard shows when there are no vehicles to list (Product owner), with a proposed answer |
| Q-018 | edited: the Lead BA's proposed answer (the oldest missed due date first); still open |
| Q-022 | opened: how the dashboard orders vehicles its order doesn't separate (Product owner), with a proposed answer |
| CAP-003 | edited: cautions for Q-020, Q-021 and Q-022 |

## Play-back

To the Product owner (to send):

> Following your change of the amber band to 21 days (DEC-003), the inspection scheduling and
> dashboard requirement (fix version 2026.12) has been updated: FR-012 and ST-03 now use 21 days.
> Because the document changed after your sign-off of 2026-10-20, it is back in draft until you sign
> off this version.
>
> While updating it, the Lead BA proposed answers to these questions. Please confirm or change each;
> signing off the updated requirement confirms them all.
>
> 1. Q-020, which vehicles a user sees on the dashboard: only the vehicles of their own operator.
> 2. Q-021, an empty dashboard: it shows the message "No vehicles to show".
> 3. Q-018, the order among overdue vehicles: the oldest missed due date first.
> 4. Q-022, vehicles the order doesn't separate (the same next due date, the same oldest missed due
>    date, or not scheduled): by registration number, A to Z.
>
> Still open, with no proposal: Q-019 (whether a vehicle is measured against its due date on the day
> it is due) and Q-017 (which intervals and anchor dates the product refuses). Out of this
> requirement's scope: VOR vehicles (Q-003) and re-registration (Q-011).

## Rejected, ignored and declined

None. All 4 staged items were accepted, and the BA took every critic suggestion (items 1 to 4 and the play-back). Scope, the document's status and whether Q-019 blocks anything are the BA's own and were recorded only in the requirement document.
