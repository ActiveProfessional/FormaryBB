# Context protocol — token budgets, session packs, work orders, model roles

**Audience:** whatever model runs a session for a business. This protocol makes the harness
consumable as context, cheaply, by both frontier and small local models.

## Why this design

- Frontier models can hold large context, but paying to re-read it every session is waste.
- Small local models (running behind openwebui against this same stack) cannot hold
  everything and get lost in long files. They need **small, complete, self-contained units**.
- Solution: **write once, read small.** Registers hold every durable fact exactly once.
  Docs reference IDs. Session packs are regenerated from registers, never hand-copied.

## The 4-level context map (read top-down, only what the next step needs)

| Level | Content | Budget | When read |
|---|---|---|---|
| L0 — Boot | This repo's `README.md` + `harness/PHASES.md` | ~1.2k tokens | First session with a model (once per model) |
| L1 — Business pack | `foundry.py rollup <slug>` output (business card, gate state, task rollups, open questions, risks, decisions) | ≤600 tokens | **Every session, first read** |
| L2 — Section read | One phase brief, one doc section, or one register filtered view | ≤3k tokens | Only what the current item needs |
| L3 — Full file | A whole document or register | As needed | Only when authoring/auditing that file |

Rules:
- Never load L3 wholesale "to be safe." The rollup says what's open; go read that one row's file.
- Never copy facts between files. Reference the ID (F-021), and the fact lives in one row.
- **One register = one truth.** Tasks in `tasks.md`, decisions in `decisions.md`, numbers in `business-facts.md`.
- L2 packs for authoring come from the template + the rollup + the target register — three small reads, one big write.

## Model roles

| Role | Tier | Does | Never does |
|---|---|---|---|
| **Orchestrator** | Frontier (or capable human) | Runs sessions, plans phases, writes plans/proposals, calls gates, drafts user-facing summaries, writes work orders | Bulk copy-editing, mechanical table updates it could delegate |
| **Executor** | Any model, incl. small local | Executes one work order at a time: research a row, draft a section, update a register per its work order | Touches files outside its work order; makes decisions; calls gates |
| **User** | Human | Approves gates [U], one-way doors (entity, spend, names), answers questions | — |

- The orchestrator **must** delegate when a unit of work is self-contained (it saves frontier
  tokens and keeps the local models practiced). It must not delegate: gate calls, judgments,
  user-facing proposals, anything one-way.
- Executors confirm: scope received → done → what changed (back-tick the exact rows).
- When an executor's output contradicts the rollup, the orchestrator resolves it — never assume.

## Work orders (the local-model interface)

A work order is a **complete** instruction set for one unit of work: an executor given only the
work order (plus at most one linked doc) can do the job with zero chat history.

```markdown
# WO-041 — Verify Wisconsin LLC filing fee
business: lakeside-roasters
requested-by: orchestrator        # work may only be requested by the orchestrator
date: 2026-09-14
budget: ~20 min / ~1 research pass
output: 1 register row + status reply
links: businesses/lakeside-roasters/registers/business-facts.md (see F-021 format)

## Context (what you must know to do this)
- Target: LLC filing fee in Wisconsin, as of today. Source must be a government or
  bar-association-grade primary source. Secondary blogs are `reported`, not `verified`.

## Task
1. Find the current fee from an authoritative source.
2. Add ONE row to business-facts.md: next F-nnn, statement, value, source+date,
   confidence (verified/reported), phase P2.
3. If the fee cannot be verified from a primary source, add the row as `reported` with
   the best available source and set the next step to "professional verify".

## Done when
Row exists, source contains a date, reply includes: "F-021 verified: $130 (WI DFI, 2026-09-14)"
```

Rules:
- One work order = one unit = one register/doc touch. If a task needs 3 files, it's 3 work orders (or 1 orchestrator job).
- Context ≤2k tokens. If it can't fit, split the work.
- **The orchestrator may NOT accept a task as done without checking the evidence.** Spot-check
  each executor's output against its done-when before marking the task DONE.
- Work orders live in `businesses/<slug>/scratch/` (disposable evidence of process, not durable record).
- Executors never renumber or delete existing rows — append only. If a row is wrong, they
  report it; the orchestrator edits.

## Session flow (any model, any session)

```
1. BOOT (first time):        read L0 (harness README + PHASES.md)     ~1.2k
2. ORIENT:                   run `foundry.py rollup <slug>`            ≤600 tokens
3. READ:                     the phase brief for the current phase      ≤3k
4. WORK:                     pick next task(s) from the phase brief,
                             write or execute work orders, update registers
5. RECORD:                   update task rows, mark items DONE with evidence, commit
6. REPORT:                   ≤10-line summary to user: done / next / blocked / asked
```

Budget for a routine working session: **~5–8k input tokens** — rollup + phase brief + one
register + one doc section. Deep authoring sessions (writing a full plan section) may use
the template + facts subset. Sessions that "just check status" use the rollup alone.

## Token discipline rules

1. **Append, don't rewrite.** New rows go at the bottom of tables; never re-flow entire files.
2. **No duplication.** If it's in a register, docs link the ID. If you find yourself pasting a
   table into a doc, stop.
3. **Filter views beat full reads.** `foundry.py status/next/tasks` print only what's needed.
4. **Trust the machine checks.** `validate` catches drift so models don't have to re-read to audit.
5. **Small-file writes.** One doc, one session. Never "while I'm here" edits beyond the task scope.
6. **The 10-line report.** End every session user-facing with ≤10 lines. If it needs more, it's a proposal (P6 material).
7. **Templates are the token guide.** Fill the template; don't expand beyond it unless the
   phase brief's » markers say to go deep.

## Moving to a new environment

The harness is `git clone`-portable; a business is `businesses/<slug>/` + git history.
To onboard a fresh model (frontier or local):
1. Give it `README.md` + `harness/PHASES.md` (L0). That's the whole architecture.
2. For a business: run `foundry.py rollup <slug>` and paste it (L1).
3. Hand it the current phase brief (L2) if it's working, or a single work order if it's executing.

Nothing else is needed. No model memory, no chat history, no external state.