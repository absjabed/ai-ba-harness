---
description: Bring Jira and Confluence activity since the last sync into the knowledge base as proposals (read-only towards Atlassian)
argument-hint: "[jira | confluence]"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Bash(git status *), Bash(git log *), Bash(git diff *), Bash(git fetch *), Bash(git pull --ff-only *), Bash(git add *), Bash(git commit *), Bash(git remote -v), Bash(git rev-parse *), mcp__atlassian__getAccessibleAtlassianResources, mcp__atlassian__searchJiraIssuesUsingJql, mcp__atlassian__getJiraIssue, mcp__atlassian__listJiraIssueComments, mcp__atlassian__listJiraIssueChangelogs, mcp__atlassian__searchConfluence, mcp__atlassian__getConfluenceContent
---

Read [`agents/sync.md`](../../agents/sync.md) and follow it exactly.

Arguments: $ARGUMENTS

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Claude Code, and deliberately carries no instructions of its own, so the two can never drift apart.
