---
name: requirements
description: "Write the requirement document for an epic or topic, grounded in the knowledge base"
---

Read [`agents/requirements.md`](../../../agents/requirements.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$requirements` is the command's arguments
(usage: `$requirements <epic name, topic or Jira epic key>`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
