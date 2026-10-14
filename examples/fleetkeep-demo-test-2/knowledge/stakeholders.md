---
type: register
id: STAKEHOLDERS
title: Stakeholders
status: draft
owner: Lead BA
sources: []
created: 2026-10-15
updated: 2026-10-15
---

# Stakeholders

Who is involved, what they own, and what they can decide. The harness uses the **Can decide** column
to tell a decision from an opinion (conventions, rule 5). Use roles; add a name only where people
need to know who to go to.

| Role | Name (optional) | Organisation | Interest | Owns | Can decide | Contact route |
|---|---|---|---|---|---|---|
| Product owner | | Northwind | A product operators trust | Product scope and behaviour | Product behaviour, business rules, scope, release content | Product channel |
| Lead BA | | Northwind | | This repository and the requirement documents | What enters the knowledge base and the wording of requirements; not product behaviour | |
| BA | | Northwind | | This repository and the requirement documents | What enters the knowledge base and the wording of requirements; not product behaviour | |
| Engineering lead | | Northwind | | Technical design | Technical approach; not business rules | |
| Compliance adviser | | Northwind | | How regulator guidance is reflected in the product | The interpretation of regulator guidance for the product; not scope, which stays with the Product owner | |
| Pilot transport manager | | Pilot customer | | | Nothing in the product | Through the Product owner |
| Pilot workshop supervisor | | Pilot customer | | | Nothing in the product | Through the Product owner |

## RACI for recurring decisions

| Decision | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| A change to a business rule | Lead BA | Product owner | Compliance adviser, Engineering lead | Pilot transport manager |
| Release content | Product owner | Product owner | Engineering lead, Lead BA | Pilot transport manager |
| Interpreting regulator guidance | Compliance adviser | Compliance adviser | Product owner, Lead BA | |
| Accepting a knowledge base change | Lead BA, BA | Lead BA | | |
