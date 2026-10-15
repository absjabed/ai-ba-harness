---
name: improve-harness
description: "Change how the harness works - work out what's wrong, decide where the fix belongs (profile, knowledge or harness), draft it as a proposal, and apply it locally only when safe and approved"
---

Read [`agents/improve-harness.md`](../../../agents/improve-harness.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$improve-harness` is the command's arguments
(usage: `$improve-harness [what isn't working | list]`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
