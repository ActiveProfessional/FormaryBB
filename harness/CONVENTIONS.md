# Conventions — IDs, statuses, file formats

**Audience:** all models. These rules make the repo machine-readable (and machine-writable).
Follow them exactly. A local model that can parse these rules can safely edit any register.

## Front matter (mandatory on every document)

```
---
business: <slug>
phase: P2
type: register
status: draft
updated: 2026-09-14
---
```

Flat `key: value` pairs only — no nesting, no lists. Parsers split on the first `:`.
Required keys: `business`, `updated`. Registers also carry `type: register`.

## ID scheme

| Object | ID format | Example | Lives in |
|---|---|---|---|
| Task | `T-Pn-nnn` | `T-P2-003` | `registers/tasks.md` |
| Question | `Q-nnn` | `Q-014` | `registers/questions.md` |
| Decision | `D-nnn` | `D-007` | `registers/decisions.md` |
| Risk | `R-nnn` | `R-003` | `registers/risks.md` |
| Fact | `F-nnn` | `F-021` | `registers/business-facts.md` |
| Assumption | `A-nnn` | `A-002` | `registers/assumptions.md` |
| Compliance item | `C-nnn` | `C-011` | `registers/compliance.md` |
| Flex module | `FM-nnn` | `FM-002` | `registers/flex.md` |
| Gate | `Pn-GATE` | `P2-GATE` | `gates/Pn-record.md` |
| Work order | `WO-nnn` | `WO-041` | `scratch/` (disposable evidence) |
| Proposal | `PROP-n` | `PROP-2` | `docs/future/proposal-vN.md` |
| Pivot option | `PV-n` | `PV-3` | `docs/business-plan/pivot-scan.md` |
| Role | `RL-nnn` | `RL-005` | `registers/roles.md` |
| Config parameter | `CFG-nnn` | `CFG-003` | `registers/config.md` |

- `nnn` = sequence within the register, zero-padded, **never reused**.
- Task IDs embed their phase (`T-P2-...`) but a task may be worked in a later phase; the ID never changes.
- IDs are the only acceptable way to reference register items in docs ("see F-021", not "see the fact about pricing").

## Plain-name glossary

Phase codes exist for token economy and machine parsing. Their plain names live in the
`PHASES.md` glossary and here, so no reader — human or model — ever has to guess:

| Code | Plain name | One-liner |
|---|---|---|
| P0 | Intake | capture the idea and the founder faithfully |
| P1 | Vetting | try to kill it cheaply; pivot-scan before any KILL |
| P2 | Foundation | entity, name, money, risk — the legal/financial base |
| P3 | Business plan | the operating document |
| P4 | Tech & infra | the stack that runs it |
| P5 | Execution plan | dated tasks and the launch |
| P6 | Future | proposals and expansion |
| P7 | Operate | run, measure, amend — the rhythm |
| G0–G5 | Gates | quality checks between phases (PASS/CONDITIONAL/FAIL) |
| [U] | User approval required | one-way doors and verdicts |
| » / ~ | Deep / stub | playbook depth markers, always with logged reasons for stubs |
| FM | Flex module | business-specific chain extension, user-activated only |
| RL / CFG | Role / config parameter | registers seeded by `init`; business roles need [U] |

## Revival & ID continuity

IDs are never reused while a business lives — and archives keep them forever. If an archived
(`killed`/`parked`) business is revived, its registers **continue** their existing numbering:
a fresh P1 runs against the preserved history, new rows continue the sequence (the next
F-row after F-021 is F-022 even three years later). Continuity is deliberate — old references
in archived plans must keep pointing at the same rows they pointed at when written. A
"reset" would orphan every historical reference; we never reset. A revived business whose
registers have grown huge can split archives by year via a logged decision instead.

## Statuses

| Object | Allowed values |
|---|---|
| Task | `TODO` `DOING` `BLOCKED` `DONE` `DROPPED` |
| Question | `OPEN` `IN PROGRESS` `RESOLVED → (doc ref)` `ANSWERED-NO` (dead end, record why) |
| Document | `draft` `review` `approved` `superseded` |
| Gate verdict | `PASS` `CONDITIONAL` `FAIL` |
| Business | `active` `parked` `graduated` `killed` (in profile front matter) |

## Task table (strict — parsed by `bin/foundry.py`)

```
| ID | Task | Horizon | Phase | Status | Owner | Due | Done when |
|----|------|---------|-------|--------|-------|-----|-----------|
| T-P2-003 | Reserve business name with state registry | 0 | P2 | TODO | founder | 2026-10-01 | Confirmation saved to source/ |
```

- Horizon: `0` = now (≤30 days), `1` = medium (≤90 days), `2` = long (≤1 year). Numbers only —
  the glossary maps them; no prose in the machine column.
- Due: the configured written date format or blank. Owner: a role from `registers/roles.md`
  (system role, approved business role, named person), or `professional`.
- One row per task, verb-first phrasing, no prose inside the table. Details live in work orders or docs.
- "Done when" must be checkable by looking at evidence, not at feelings.

## Roles & owners

Owners on task rows come from `registers/roles.md` (IDs: `RL-nnn`). Two kinds of role:

- **System roles** exist by default in every business: `founder` (the user; default owner
  of all tasks), `orchestrator` (frontier model: sessions, gates, proposals), `agent`
  (machine executors: scoped work orders only), `professional` (licensed external
  verification: legal, tax, insurance).
- **Business roles have no defaults.** The model may propose role separation (and **should**, early —
  the informal separation makes hiring-on later a matter of assigning existing identifiers), but a
  business role is formalized only with **[U]**. A sole proprietor can run on system roles alone;
  nobody pays overhead they didn't approve.

Task Owner column accepts: a system role, a business role, a named person, or `professional`.

## Calendar tagging

Any calendar event belonging to a business uses the title prefix `[SLUG]` (uppercase):

```
[LAKESIDE-ROASTERS] P2 — File Articles of Organization with WI DFI
[ACME] Weekly review            (recurring)
[ACME] Renew business license   (deadline, 1440-min reminder)
```

In agent environments with calendar tools: create the event when a task gets a due date;
cancel it when the task is DROPPED. Deadlines that are legal or financial always get
reminders (default 1440 minutes before). This tag is what keeps each company's obligations
findable and separable from personal calendar noise.

## Dates, numbers & configuration (the variable principle)

- **Written dates** use the business's configured `date-format` (harness default
  MM-DD-YYYY; `registers/config.md` key `date-format`). The CLI accepts ISO on input and
  normalizes for comparisons — never rewrite historical dates by hand; the config owns the format.
- **Currency** is the configured `{{currency}}` (default USD, ISO 4217); financial tables
  state it once per table, not per cell. **Spend threshold** `{{spend-threshold}}` (default 250):
  purchases above it are one-way doors requiring **[U]**.
- **Config lives once per business** in `registers/config.md` (`CFG-nnn`), seeded from
  `harness/lib/defaults.md`. Docs and gates reference keys symbolically (`{{spend-threshold}}`);
  models resolve values at execution time. Overrides need **[U]** + a logged decision in the
  Basis column — `validate` enforces this. One value, one home, referenced everywhere: this is
  how phases stay synchronized and new parameters (timezone, fiscal-year start, review cadence)
  get introduced without desync.
- Metric IDs (`M-nnn`) stay **off** by default; `metrics.md` is display-only. If recursive
  reviews show a recurring need to cross-reference metrics from plans or proposals, add
  `metric-ids: on` as a config key and start numbering — the recursive review should surface
  this itself.

## Facts & evidence

- Every external claim gets a row in `registers/business-facts.md`:
  `| F-021 | WI LLC filing fee | $130 | WI DFI fee schedule, checked 2026-09-14 | verified | P2 |`
- Confidence: `verified` (primary source) / `reported` (secondary) / `estimated` (math shown) / `guessed` (labeled).
- **No unsourced numbers inside plans.** If a number must appear before it's verified, mark it `est.` and cite the assumption ID.

## File naming

- lowercase-kebab-case, numbered prefixes for ordered docs (`00-master-plan.md`, `10-market-research.md`, ...).
- One file per register; one topic per doc. If a doc needs a section that already exists elsewhere, link to it — never copy.
- Raw research dumps, PDFs, screenshots go to `source/` — never pasted into docs.

## Commits

`[<slug>] <ID or area> what changed` — e.g. `[lakeside] T-P2-003 name reserved, confirmation filed in source/`.
One completed item = one commit. The commit history is the work log.

## Supersede rule (history is never deleted)

To change an approved document materially: set `status: superseded`, add a `superseded-by: <file>` line,
create the new version (v2 suffix for major plan revisions), and log a `D-nnn` explaining why.
Small edits (typos, adding rows) do not need superseding.

## Tailoring markers inside documents

- **»** = emphasis required for this business type (deep treatment — see playbooks)
- **~** = often skippable; stub or defer with a `D-nnn`
- No marker = core; always fill.

## The honesty rules

1. Never write a fact you cannot source or label as estimate.
2. Never mark DONE without evidence recorded somewhere in the repo.
3. Never let the plan and a register disagree silently — fix one, log the discrepancy as a decision.