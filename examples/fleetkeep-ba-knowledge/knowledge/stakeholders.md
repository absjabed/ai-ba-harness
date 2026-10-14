---
type: register
id: STAKEHOLDERS
title: Stakeholders
status: confirmed
owner: Lead BA
sources:
  - SRC-001
created: 2026-09-15
updated: 2026-09-17
---

# Stakeholders

Who is involved, what they own, and what they can decide. The harness uses the **Can decide** column
to tell a decision from an opinion (conventions, rule 5). Use roles; add a name only where people
need to know who to go to.

All names below are fictional.

| Role | Name (optional) | Organisation | Interest | Owns | Can decide | Contact route |
|---|---|---|---|---|---|---|
| Product owner | Dana Whitlock (fictional) | Northwind Systems | A product operators trust to keep their licence | FleetKeep's scope, behaviour and release content | Product behaviour, business rules, scope and release content | Jira project FK (mention), product channel |
| Lead BA | | Northwind Systems | One agreed, cited account of how FleetKeep works | This repository and the requirement documents | What enters the knowledge base, and requirement wording. Not product behaviour | This repository (pull request or staging file) |
| Engineering lead | | Northwind Systems | Feasible, safe changes | Technical design and delivery | Technical approach and estimates. Not business rules | Jira project FK (mention) |
| Compliance adviser | Sam Okafor (fictional) | Northwind Systems | FleetKeep matching what the regulator expects | How regulator guidance is reflected in the product; audit pack content | How regulator guidance is interpreted for the product. Scope changes still go to the Product owner | Compliance mailbox |
| Customer support lead | | Northwind Systems | Supportable features, few support cases | The support process and vendor support access | Support procedures. Not product behaviour | Support desk |
| Pilot transport manager | | Pilot operator (haulage, tenant) | Fewer missed defects, keeping the operator's licence | Working practice at the pilot depots | Nothing in the product; their own depots' practice | Through the Product owner |
| Pilot workshop supervisor | | Pilot operator (haulage, tenant) | A workshop queue that shows what matters first | Workshop practice and shift patterns at the pilot depots | Nothing in the product; workshop shift patterns | Through the Product owner |

## RACI for recurring decisions

| Decision | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Change to a business rule | Lead BA | Product owner | Compliance adviser, Engineering lead | Pilot transport manager |
| Defect escalation thresholds | Lead BA | Product owner | Compliance adviser, Pilot transport manager, Pilot workshop supervisor | Engineering lead, Customer support lead |
| Release content | Product owner | Product owner | Engineering lead, Lead BA | Customer support lead |
| Interpreting regulator guidance | Compliance adviser | Product owner | Lead BA | Engineering lead |
| Accepting a knowledge base change | Lead BA | Lead BA | BA | Everyone with a clone |
