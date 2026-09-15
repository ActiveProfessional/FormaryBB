---
business: lakeside-roasters
type: register
updated: 09-15-2026
---

# Roles — Lakeside Roasters

*(Synthetic example.)*

| ID | Role | Type | Assignee | Scope | Status | Approved by | Date |
|----|------|------|----------|-------|--------|-------------|------|
| RL-001 | founder | system | (the user) | owns the business; default owner of all tasks | active | system default | |
| RL-002 | orchestrator | system | (frontier model) | runs sessions, gates, proposals, user-facing work | active | system default | |
| RL-003 | agent | system | (machine executors) | scoped work orders only | active | system default | |
| RL-004 | professional | external | (per engagement) | licensed verification: legal, tax, insurance | active | system default | |
| RL-005 | market-helper | business | (vacant) | seasonal weekend stall help at markets | proposed | (awaiting [U]) | |

System roles exist by default. Business roles (type: business) have no defaults — proposed
by the model using judgment, formalized only with **[U]**; a sole proprietor can run on
system roles alone. Standing rule: **always propose role separation early** so the informal
separation already exists if someone joins later. See `harness/CONVENTIONS.md` "Roles & owners".