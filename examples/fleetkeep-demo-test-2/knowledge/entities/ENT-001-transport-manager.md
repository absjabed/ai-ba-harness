---
type: entity
id: ENT-001
title: Transport manager
status: confirmed
kind: role
owner: Product owner
sources: [SRC-001, SRC-003, DEC-002, SRC-007]
aliases: []
tags: [inspections, defects]
created: 2026-10-15
updated: 2026-10-20
---

# Transport manager

A product user role, and the only one that sets or changes a vehicle's inspection interval and anchor date ([SRC-001](../sources/SRC-001-2026-10-02-product-owner-inspection-rules.md)).

> [!WARNING]
> This is a role in the product. It is not the "Pilot transport manager" in [the stakeholders register](../stakeholders.md), who is a person at the pilot customer.

## Attributes or permissions

| Name | Meaning | Rules |
|---|---|---|
| Set or change a vehicle's inspection interval and anchor date | Only this role can do it | [BR-002](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md#rules-applied) |
| Decide what happens to a reported defect | Every reported defect gets this role's decision first | [BR-007](../domains/defects/CAP-006-deciding-what-happens-to-a-reported-defect.md#rules-applied) |
| See the inspection dashboard | Can see it | [BR-018](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md#rules-applied) |

## Lifecycle

## Where it appears

- [Setting a vehicle's inspection interval and anchor date](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md)
- [Deciding what happens to a reported defect](../domains/defects/CAP-006-deciding-what-happens-to-a-reported-defect.md)
- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md)

## Open items

None.

## Sources

- SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
- SRC-003: the defects workshop, 2026-10-16 (Lead BA's notes)
- SRC-007: the Product owner's sign-off of the inspection scheduling and dashboard requirement, 2026-10-20
