---
type: entity
id: ENT-002
title: Compliance officer
status: confirmed
kind: role
owner: Product owner
sources: [SRC-006, SRC-007]
aliases: []
tags: [inspections, tenancy-and-access]
created: 2026-10-18
updated: 2026-10-20
---

# Compliance officer

A product user role, named among the product's users in the project's purpose, that checks the fleet's inspection status ([SRC-006](../sources/SRC-006-2026-10-18-inspection-scheduling-and-dashboard.md)).

> [!WARNING]
> This is a role in the product. It is not the "Compliance adviser" in [the stakeholders register](../stakeholders.md), who decides how the regulator guidance is read for the product.

## Attributes or permissions

| Name | Meaning | Rules |
|---|---|---|
| Set or change a vehicle's inspection interval and anchor date | Can't: only a transport manager can | [BR-002](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md#rules-applied) |
| See the inspection dashboard | Can see it, without changing any vehicle's schedule | [BR-018](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md#rules-applied) |

## Lifecycle

## Where it appears

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md)

## Open items

None.

## Sources

- SRC-006: the Lead BA's answers while writing the inspection scheduling and dashboard requirement, 2026-10-18
- SRC-007: the Product owner's sign-off of the inspection scheduling and dashboard requirement, 2026-10-20
