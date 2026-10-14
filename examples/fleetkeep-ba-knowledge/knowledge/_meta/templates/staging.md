# Staging: <command> <source>, YYYY-MM-DD

<!-- Proposed knowledge changes waiting for the BA. Nothing here is in the knowledge base yet.
     Start with the Critic section. Tick one box per item, or answer in the chat ("accept 1-4,
     reject 5, edit 6: ..."); the command writes chat decisions into this file. When you say apply
     (normally once every item is decided), the command applies the accepted items and deletes this
     file, or keeps only the undecided ones. -->

| Field | Value |
|---|---|
| Input | <inbox path, pasted text, conversation, Jira keys, Confluence pages> |
| Kind | <meeting, document, email, transcript, conversation, jira, confluence> |
| Source record to create | SRC-new-1 (number them across the files of one run: SRC-new-1, SRC-new-2) |
| Items | <n> in all: <n> new, <n> confirms, <n> extends, <n> contradicts, <n> duplicate, <n> answers; of these, <n> proposed as ignore |
| Needs redaction | <no / yes: what was replaced in the quotes> |
| Critic | <n> findings: <n> fixed, <n> for you to check |

## Summary

<Three to five sentences on what the input contains.>

<!-- For meetings and transcripts only: the next three sections. -->

### Attendees

<Roles, one line. No names unless the person's name is needed.>

### Decisions

| Decision | By | Can decide? |
|---|---|---|
| <what was decided> | <role> | <can decide / needs owner: role> |

### Actions

| Action | Owner | Due |
|---|---|---|
| <what> | <role> | <date, or none given> |

<!-- For a conversation or pasted text only: -->

### Source excerpt

<The passages the items quote, copied from the conversation or text, so the critic can check them.>

## Critic

<How the second look ran (critic sub-agent or second pass). What it changed in this file, and what it
left for you to check, with item numbers. "No findings" if it found nothing.>

**Other findings:** <findings about the summary, the play-back, or points the critic raised that
aren't items. "None" if none.>

## Items

### 1. <Short name>

| Field | Value |
|---|---|
| Kind | <requirement, rule, decision, action, approval, question, answer, term, risk, fact> |
| Verdict | <new / confirms CAP-012 / extends CAP-012 / contradicts BR-104 / duplicate of Q-014 / answers Q-009> |
| Searched for | <the wordings searched, for a new item> |
| Depends on | <item numbers this one needs, or leave the row out> |
| Clarity | <clear / vague: "fast" / incomplete: no error case> |
| Authority | <can decide (role) / cannot (role; owner is role) / unknown: why / n/a> |
| Sensitivity | <clean / redact: what> |
| Quote | "<exact words, names replaced by [role]>" (<location: file and bullet or paragraph, time, key and comment>) |
| Critic | <ok / fixed: what changed / check: what to look at> |
| Affects delivery | <only when changing an existing page: REQ-<slug> ST-01 (PROJ-1234), ... or none> |
| Proposed change | <create CAP-new-1 in domains/<area>/ (status confirmed) / edit CAP-012 (diff below) / new Q-new-1 for <role>, due YYYY-MM-DD (proposed) / new DEC-new-1, approved by <role> / new ACT-new-1 for <role> / add T-new-1 / ignore: why> |

<details>
<summary>The proposed page, exactly as it will be written (for a new page or decision)</summary>

```markdown
<the whole page: properties, title, summary sentence, and every section the source covers>
```

</details>

```diff
<for an edit: the exact lines added and removed>
```

- [ ] accept
- [ ] accept with the critic's suggestion
- [ ] edit: <what to change; a new page goes in its own details block here>
- [ ] reject: <why>

## Play-back message

<For meetings and transcripts: a short message for the participants: Decided (by role), Still open,
Follow-up questions, Actions, Terms. For /requirements: a message to the owner of the pending proposals, asking them to
confirm or change each. Never the risks, internal notes or the critic's findings.>

**Critic:** <ok / what it flagged in this message>
