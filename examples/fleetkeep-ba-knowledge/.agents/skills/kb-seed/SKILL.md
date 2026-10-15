---
name: kb-seed
description: "Build the first knowledge base from existing documents, Confluence pages and Jira epics (proposals for the BA to accept)"
---

Read [`agents/kb-seed.md`](../../../agents/kb-seed.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$kb-seed` is the command's arguments
(usage: `$kb-seed [confluence | jira | inbox | <path or page>]`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
