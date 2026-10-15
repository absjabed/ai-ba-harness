---
description: "Answers a question from the project knowledge base, with citations. Reads only: it can't change files, run commands or write to Jira or Confluence. Used by /ask."
mode: subagent
permission:
  edit: deny
  bash: deny
  task: deny
  webfetch: deny
  "atlassian_*": deny
  "atlassian_getAccessibleAtlassianResources": allow
  "atlassian_searchJiraIssuesUsingJql": allow
  "atlassian_getJiraIssue": allow
  "atlassian_searchConfluence": allow
  "atlassian_getConfluenceContent": allow
  "atlassian_search": allow
---

Read `agents/ask.md` in this repository and do exactly what it describes. The question is in the
message that started you.
