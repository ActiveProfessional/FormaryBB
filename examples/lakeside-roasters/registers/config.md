---
business: lakeside-roasters
type: register
updated: 09-14-2026
---

# Config — Lakeside Roasters

*(Synthetic example — all defaults, no overrides.)*

| ID | Key | Value | Basis | Approved by | Date | Notes |
|----|-----|-------|-------|-------------|------|-------|
| CFG-001 | date-format | MM-DD-YYYY | harness default | — | | written dates; CLI normalizes for comparison |
| CFG-002 | currency | USD | harness default | — | | ISO 4217; financial docs |
| CFG-003 | spend-threshold | 250 | harness default | — | | purchases above this need [U]; in {{currency}} |

Single source of business parameters. Overrides need **[U]** + `D-nnn` logged in Basis.
Canonical keys and what each affects: `harness/lib/defaults.md`.