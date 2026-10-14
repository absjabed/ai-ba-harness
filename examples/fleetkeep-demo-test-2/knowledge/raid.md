---
type: register
id: RAID
title: Risks, assumptions, issues, dependencies and actions
status: draft
owner: Lead BA
sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-007]
created: 2026-10-15
updated: 2026-10-20
---

# Risks, assumptions, issues, dependencies and actions

Statuses: risks `open` or `closed`; assumptions `open`, `confirmed` or `wrong`; issues `open` or
`resolved`; dependencies `open` or `met`; actions `open`, `done` or `dropped`.

## Risks

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status | Source |
|---|---|---|---|---|---|---|---|
| R-001 | If the Product owner's 7-day grace period is built as written, inspections done up to 7 days late would not show as overdue, while the regulator guidance says late inspections must be visible to an auditor | Not assessed | Not assessed | Settle [Q-002](questions/Q-002-grace-period-before-an-inspection-is-overdue.md) before the overdue rules are specified | Product owner | closed | SRC-002, SRC-001, SRC-007 |
| R-002 | Depots without a roller brake tester can't record a brake test reading at all, so they couldn't record a brake test the way the Compliance adviser proposes (a reading for every failed test) | Not assessed | Not assessed | Take it into account when answering [Q-009](questions/Q-009-what-a-brake-test-result-records.md) | Product owner | open | SRC-004 |
| R-003 | When a vehicle is re-registered, nothing stops two vehicles sharing one record, which could double up their inspection schedules | Not assessed | Not assessed | Settle [Q-011](questions/Q-011-what-happens-when-a-vehicle-is-re-registered.md) so the product keeps one record per vehicle | Product owner | open | SRC-005 |

## Assumptions

| ID | Assumption | Why we assume it | How to confirm | Owner | Status | Source |
|---|---|---|---|---|---|---|

## Issues

| ID | Issue | Impact | Action | Owner | Status | Source |
|---|---|---|---|---|---|---|

## Dependencies

| ID | We depend on | For | Needed by | Owner | Status | Source |
|---|---|---|---|---|---|---|

## Actions

Status is `open`, `done` or `dropped`. `/review kb` reports open actions past their due date.

| ID | Action | Owner | Due | Status | Jira | Source |
|---|---|---|---|---|---|---|
| ACT-001 | List the defect states the system has today | Engineering lead | 2026-10-23 | open | | SRC-003 |
