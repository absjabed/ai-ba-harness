# Staging: <command> <source>, YYYY-MM-DD

<!-- Proposed knowledge changes waiting for the BA. Nothing here is in the knowledge base yet.
     Start with the Critic section. Tick one box per item, or answer in the chat ("accept 1-4,
     reject 5, edit 6: ..."). When you say apply (normally once every item is decided), the command
     applies the accepted items and deletes this file, or keeps only the undecided ones. -->

| Field | Value |
|---|---|
| Input | <inbox path, pasted text, conversation, Jira keys, Confluence pages> |
| Kind | <meeting, document, email, transcript, conversation, jira, confluence> |
| Source record to create | SRC-new |
| Items | <n> (<n> new, <n> confirm, <n> contradict, <n> duplicate) |
| Needs redaction | <yes: what / no> |
| Critic | <n> findings: <n> fixed, <n> for you to check |

## Summary

<Three to five sentences on what the input contains.>

## Critic

<How the second look ran (sub-agent or second pass), what it changed in this file, and what it left
for you to check, with item numbers. "No findings" if it found nothing.>

## Items

### 1. <Short name>

| Field | Value |
|---|---|
| Kind | <requirement, rule, decision, action, question, answer, term, risk, fact> |
| Verdict | <new / confirms CAP-012 / contradicts BR-104 / duplicate of Q-014> |
| Clarity | <clear / vague: "fast" / incomplete: no error case> |
| Authority | <can decide (role) / cannot (role) / unknown> |
| Sensitivity | <clean / redact: what> |
| Quote | "<exact words>" (<location: file ¶, time, key and comment>) |
| Critic | <ok / fixed: what changed / check: what to look at> |
| Proposed change | <create CAP-new-1 in domains/<area>/ / edit CAP-012 (diff below) / new Q-new-1 / new DEC-new-1 awaiting <role> / action for <role> by <date> / add T- term / ignore> |

```diff
<only for edits: the exact lines added and removed>
```

- [ ] accept
- [ ] edit: <what to change>
- [ ] reject: <why>

## Play-back message (optional)

<A short message for the participants, listing what was captured, so they can confirm or correct it.>
