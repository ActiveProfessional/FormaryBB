# Harness defaults — the canonical configuration keys

**Purpose:** the single source of business parameters. `init` seeds each business's
`registers/config.md` from this table. Docs and gates reference keys symbolically
(`{{spend-threshold}}`, `{{currency}}`, `{{date-format}}`); models resolve values from the
business config at execution time — nothing hardcodes a value the config owns. This is the
variable principle: set once, referenced everywhere, no desync across phases.

| Key | Default | Affects | Notes |
|---|---|---|---|
| date-format | MM-DD-YYYY | all written dates: front matter `updated:`, due dates, source dates, gate records | ISO (`YYYY-MM-DD`) accepted on input; the CLI normalizes for comparison |
| currency | USD | financial plan, monetary facts, spend-threshold unit | ISO 4217 three-letter code |
| spend-threshold | 250 | purchases above this amount are one-way doors **[U]** (P4 procurement, RUNBOOK) | value is in `{{currency}}` |
| orchestrator-tier | T1 | tier running sessions: sets reading pattern defaults (CONTEXT-PROTOCOL.md) | T1/T2; T3 never orchestrates |
| executor-tier | T2 | default tier assumed for work-order executors when not declared | T2/T3 |

## Adding keys (per business, by judgment)

When a value recurs across phases or docs — timezone, fiscal-year start, review cadence,
language, brand-name spellings, metric-ID activation — add a `CFG-nnn` row instead of
restating it everywhere. Propose it like any enrichment; log it in `decisions.md` if it
changes behavior.

## Overriding

Edit the row's Value, set Basis to `override: D-nnn (user, date)`, and get **[U]** first —
overrides without a logged decision fail `validate`. Business overrides live in the
business's `registers/config.md`, never in this file (this file is harness machinery).