---
type: process
id: PROC-000
title: <Name of the process, e.g. Building a theatre list>
status: draft
area: <area from the profile>
variant: <as-is | to-be | both>
owner: <role>
sources: []
rules: []
aliases: []
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Title>

<One sentence: what the process achieves. This sentence is used in the index.>

## Trigger

<What starts it.>

## Actors

| Role | Part they play |
|---|---|

## Steps

```mermaid
flowchart TD
  A[Trigger] --> B[Step]
  B --> C{Decision}
  C -- yes --> D[Outcome]
  C -- no --> E[Other outcome]
```

1. <Step, with the role that does it.>

## Variations

<Alternative paths and exceptions.>

## Pain points (as-is) or changes (to-be)

<What hurts today, or what the new process changes and why.>

## Rules applied

1. **BR-000** <Rule.> (SRC-000)

## Diagrams for publishing

<Only if needed: `<slug>.as-is.drawio` and `<slug>.as-is.svg` in this folder, exported YYYY-MM-DD.>

## Sources

- SRC-000: <one line>
