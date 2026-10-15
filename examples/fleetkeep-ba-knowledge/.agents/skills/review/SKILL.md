---
name: review
description: "Quality report on a requirement document, a Jira issue, or the knowledge base (kb); changes nothing but its report unless you ask"
---

Read [`agents/review.md`](../../../agents/review.md) at the root of this repository and follow it
exactly. Whatever the user wrote after `$review` is the command's arguments
(usage: `$review <requirements/<slug>/requirement.md | JIRA-KEY | kb>`).

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Codex, and deliberately carries no instructions of its own, so the two can never drift apart.
