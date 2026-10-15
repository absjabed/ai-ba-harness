---
name: backlog
description: "Put approved work into Jira after duplicate checks and your approval - stories from a reviewed requirement (and later changes to them), or a single task, spike or UAT bug"
---

Read [`agents/backlog.md`](../../../agents/backlog.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$backlog` is the command's arguments
(usage: `$backlog <requirements/<slug>/requirement.md | task ACT-<n> | spike Q-<n> | bug <SRC-id> <item>>`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
