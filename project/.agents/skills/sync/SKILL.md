---
name: sync
description: "Bring Jira and Confluence activity since the last sync into the knowledge base as proposals (read-only towards Atlassian)"
---

Read [`agents/sync.md`](../../../agents/sync.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$sync` is the command's arguments
(usage: `$sync [jira | confluence]`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
