---
name: intake
description: "Turn notes, a transcript, a document or this conversation into proposed knowledge, judged against the knowledge base"
---

Read [`agents/intake.md`](../../../agents/intake.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$intake` is the command's arguments
(usage: `$intake [inbox/<file or folder> | knowledge/_staging/<file> | pasted text | nothing for this conversation]`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
