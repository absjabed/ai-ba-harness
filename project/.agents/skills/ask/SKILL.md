---
name: ask
description: "Answer a question from the project knowledge base, with citations (read-only; anyone can use it)"
---

Read [`agents/ask.md`](../../../agents/ask.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$ask` is the command's arguments
(usage: `$ask <your question>`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
