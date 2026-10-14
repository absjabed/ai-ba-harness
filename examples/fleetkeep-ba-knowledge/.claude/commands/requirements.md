---
description: Write the requirement document for an epic or topic, grounded in the knowledge base
argument-hint: "<epic name, topic or Jira epic key>"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Bash(git status *), Bash(git log *), Bash(git diff *), Bash(git fetch *), Bash(git pull --ff-only *), Bash(git add *), Bash(git commit *), Bash(git remote -v), Bash(git rev-parse *), mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql
---

Read [`agents/requirements.md`](../../agents/requirements.md) and follow it exactly.

Arguments: $ARGUMENTS

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Claude Code, and deliberately carries no instructions of its own, so the two can never drift apart.
