---
type: source
id: SRC-006
title: Lead BA's answers on inspection scheduling and the dashboard
status: confirmed
kind: conversation
input_date: 2026-10-18
created: 2026-10-18
updated: 2026-10-18
---

# Lead BA's answers on inspection scheduling and the dashboard

The Lead BA's answers to the clarifying questions while writing the requirement document for inspection scheduling and the dashboard; every answer about product behaviour is a proposal for the Product owner.

## Details

| Field | Value |
|---|---|
| Kind | conversation |
| Date | 2026-10-18 |
| Participants or author | Lead BA |
| Original | Not kept; the answers are recorded in the Clarifications of [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) |
| Processed by | /requirements on 2026-10-18 |

## Summary

Scope: per-vehicle intervals, the next due date from the anchor date, and the dashboard banding are in; VOR, brake tests, recording inspections, notifications and re-registration are out. Fix version 2026.12; five stories. The Lead BA proposed answers to Q-001 (the next due date is the first one after today that no inspection has met; a missed due date stays overdue until an inspection meets it) and Q-002 (no grace period), and proposed that transport managers and compliance officers see the dashboard (compliance officers read-only), that a vehicle with no anchor date shows grey "Not scheduled", and that the dashboard lists overdue vehicles first, then by next due date. The Lead BA also accepted the command's recommendations: an inspection meets every unmet due date on or before its day, or else the next one; the anchor date isn't itself a due date; the 14 days are calendar days; the next due date shows beside the status and "Not scheduled" vehicles come last. None of these is a rule yet: the Lead BA can't decide product behaviour (stakeholders register), so each is a question to the Product owner with the proposed answer, settled by the Product owner's sign-off of the requirement.

## What it changed

| Item | Change |
|---|---|
| Q-001 | edited: the Lead BA's proposed answer (possible answer 3), with the due-day question; still open |
| Q-002 | edited: the Lead BA's proposed answer (possible answer 1, no grace period); still open |
| Q-012 | opened: who can see the inspection dashboard (Product owner), with a proposed answer |
| Q-013 | opened: how the dashboard shows a vehicle with no anchor date (Product owner), with a proposed answer |
| Q-014 | opened: whether the anchor date itself is a due date (Product owner), with a proposed answer |
| Q-015 | opened: how the 14 days before a due date are counted (Product owner), with a proposed answer |
| Q-016 | opened: what the dashboard shows for each vehicle and in what order (Product owner), with a proposed answer |
| Q-017 | opened: which intervals and anchor dates the product refuses (Product owner), no proposed answer |
| ENT-002 | created: Compliance officer (added by the critic) |
| CAP-001 | edited: caution for Q-017 |
| CAP-002 | edited: caution for Q-014 |
| CAP-003 | edited: cautions for Q-012, Q-013, Q-015 and Q-016 |

## Play-back

To the Product owner:

> While writing the requirement for inspection scheduling and the dashboard (fix version 2026.12),
> the Lead BA proposed answers to these questions. Please confirm or change each; signing off the
> requirement document confirms them all.
>
> 1. Q-001, the next due date after a missed or early inspection: the next due date is the first
>    one after today that no inspection has met; a missed due date stays overdue until an inspection
>    meets it. An inspection meets every unmet due date on or before the day it is done, or, when
>    there is none, the first due date after that day. Read literally, a vehicle not yet inspected
>    would show green (or amber) on the day its inspection is due, because it is measured against
>    the following due date and isn't overdue until the next day. Should the due date itself count
>    ("on or after today")?
> 2. Q-002, grace period: no grace period; a vehicle is overdue from the day after a due date no
>    inspection has met, as the regulator guidance says.
> 3. Q-012, who sees the dashboard: transport managers and compliance officers; compliance officers
>    can look but not change anything.
> 4. Q-013, a vehicle with no anchor date: shown grey, labelled "Not scheduled".
> 5. Q-014, the first due date: the anchor date plus one interval; the anchor date itself is not a
>    due date.
> 6. Q-015, the amber band: the 14 days are calendar days.
> 7. Q-016, the dashboard: each scheduled vehicle's next due date beside its status; overdue
>    vehicles first, then the other scheduled vehicles by next due date, then vehicles not
>    scheduled. In what order should the overdue vehicles themselves be listed: by next due date,
>    or by the oldest missed due date first?
>
> One more, with no proposal: Q-017, which inspection intervals and anchor dates should the product
> refuse, and must both be set together?
>
> Still open and out of this requirement's scope: VOR vehicles (Q-003) and re-registration (Q-011).

## Rejected, ignored and declined

None. All 12 staged items were accepted, and the BA took every critic suggestion (items 1, 4, 7, 8, the play-back, and the Compliance officer entity added as item 12). Scope, the fix version and the story split are the BA's own and were recorded only in the requirement document.
