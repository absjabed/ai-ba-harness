---
description: Quality report on a requirement document, a Jira issue, or the knowledge base (kb); changes nothing but its report unless you ask
argument-hint: "<requirements/<slug>/requirement.md | JIRA-KEY | kb>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(git status *), Bash(git log *), Bash(git diff *), Bash(git fetch *), Bash(git pull --ff-only *), Bash(git add *), Bash(git commit *), Bash(git remote -v), Bash(git rev-parse *), mcp__atlassian__getJiraIssue, mcp__atlassian__searchJiraIssuesUsingJql
---

Read [`agents/review.md`](../../agents/review.md) and follow it exactly.

Arguments: $ARGUMENTS

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Claude Code, and deliberately carries no instructions of its own, so the two can never drift apart.
