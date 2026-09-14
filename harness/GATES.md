# Gates — what "good enough to proceed" means

**Audience:** the orchestrator at each gate; the user who signs it. The gate record is the
only place a verdict lives.

## Procedure

1. Run `python3 bin/foundry.py validate <slug>` (cheap automated checks).
2. Read the phase's **Gate criteria** section (in its `phases/Pn-*.md`).
3. Walk the automatic-fail list (below). Any hit → **FAIL**. Fix and re-run.
4. If criteria are met but open items remain, you may pass **CONDITIONAL** — every open
   item must be carried as a tracked task (give it an ID before you write the verdict).
5. Verdicts requiring the user's sign-off are marked **[U]**. The user must explicitly
   approve before the verdict is recorded.
6. Record with `python3 bin/foundry.py gate <slug> Pn --pass|--conditional|--fail --notes "..."` —
   this creates `businesses/<slug>/gates/Pn-record.md`. Commit.
7. Announce: phase started/complete, next phase, gate conditions if any.

## Automatic fails (any phase)

1. A required document is missing.
2. Any question marked blocking (see `registers/questions.md`, column `Block`) is unanswered
   and has no task with a due date.
3. A required artifact contains unsourced numbers (facts not in `business-facts.md` and not labeled `est.`).
4. A gate was passed without the user's approval where required **[U]**.
5. The previous gate record does not exist.
6. The tasks register has a DONE row with no evidence pointer in "Done when".

## The gates

### G0 — Intake gate
- Profile complete enough to act on: nature, mission intent, region, and at least the
  founder-relevant personal facts. Remaining gaps live in `questions.md`, each with a Block flag.
- Every profile fact that can be wrong has a matching verification question or task.
- P1 research plan written. The user has seen the profile and confirmed it reflects the idea.
- **[U]** User must confirm: "this is what I mean."

### G1 — Vetting gate
- **» Market evidence:** at least one primary (or primary-substitute) customer-evidence row
  per target segment, or the business-type playbook's minimum for this type.
- Every assumption underpinning the verdict has an `A-nnn` with a kill-test attached.
- Verdict recorded in a decision (`D-nnn`): **GO / PIVOT / KILL / HOLD**, dated, with reasoning.
  PIVOT must state what changes; HOLD must state the re-test trigger and date.
- **Pivot-first rule:** a draft KILL is not confirmable until a pivot scan exists
  (`docs/business-plan/pivot-scan.md`), its options are cheap-tested, and the user has
  accepted/rejected them **[U]** on record. KILL requires exhausted or user-rejected pivots.
- **[U]** Verdict shared with the user for approval before P2 starts. KILL requires no further
  argument once pivots are exhausted — the archive plus the scan is the argument.

### G2 — Foundation gate
- **» Entity:** a professional-verified recommendation exists (lawyer/accountant/registered
  agent/official agency source), entity type **[U]** user-approved, and a name cleared
  (state registry + trademark TESS check + domain availability).
- Bank, insurance, accounting, payroll are decided — may be tasks with due dates, but never open questions.
- Funding and runway math complete, every number sourced or estimated; runway ≥ planned
  horizon-0 spend (est. acceptable).
- Mission refined against P1 evidence and confirmed by the user. Risk & compliance registers
  seeded, each risk with at least a placeholder mitigation.

### G3 — Business-plan gate
- The master plan **» tells the localized story** — a stranger reading it alone could answer:
  what is sold, to whom, in what place, how money moves, what happens in year one.
- Every core assumption cross-referenced to `A-nnn`s (not restated).
- Financial projections tie to the facts register: revenue drivers → facts → assumptions, no orphan numbers.
- **Followability check:** the plan's operating cadence names who does what and when — the
  "how to ensure the plan is followed" requirement. Include a plan-review task with a date.
- Local personal details present where the type playbook demands (»).
- **Reconciliation (if P3/P4 ran in parallel):** plan-tech dependencies both directions are
  resolved — every tool the plan names is in the tech plan's decisions, every tech decision
  the plan relies on is reflected in the plan's ops/financials. Discrepancies are `D-nnn`s, fixed pre-gate.
- **[U]** User reads and approves the master plan.

### G4 — Tech & infrastructure gate
- Stack decisions follow the default preference (openwebui + openterminal/shell agent +
  langflow) unless the user specified otherwise — and any exception is a logged decision.
- Every tool choice has a decision row covering cost, data residency, lock-in, and whether
  an internal team could run it vs. a hosted option is justified.
- Security baseline specified even for zero-data businesses (password manager, MFA on
  everything, off-repo secrets).
- Total run-rate cost sourced or estimated, and included in financials.
- **Reconciliation (if P3/P4 ran in parallel):** both directions confirmed — tech costs in
  the financial plan, plan sections referencing the stack (ops, GTM, team) consistent with
  the decisions here. G3's reconciliation findings are re-checked, not re-argued.

### G5 — Execution-plan gate
- Every task has an owner and a due date. No orphan TODOs outside the register.
- **Horizon completeness:** the horizon list covers everything P2–P4 set in motion; every
  G2/G3/G4 condition has a task with a due date.
- Legal/financial deadlines are on the user's calendar (tagged `[SLUG]`) with reminders.
- Critical-path call-out: the ≤7 tasks that, if late, move launch — identified and reviewed
  with the user.
- **[U]** User approves the launch checklist and the critical path before launch mode starts.

### Quarterly gate (P7)
- Run `foundry.py rollup` against the current metrics; compare metrics to targets in
  `docs/business-plan/` — **variance ≥25% → triggers review** and plan amendment.
- Each compliance item (C-nnn) has status reviewed; anything expired or approaching gets a task.
- Every decision from the quarter is still consistent with registers (discrepancies → decisions).

## Gate philosophy

- The gate's job is to kill bad ideas **cheaply, early** — not to make paperwork.
- The pass bar **scales by business type** (see PHASES.md tailoring): a side business's G3 is
  a lean plan; a regulated venture's G3 is the full template. The test is always: *"could a
  stranger execute this business from what's written?"* — never "is every box filled?".
- CONDITIONAL is legitimate — but every condition must become a tracked task before the verdict is written.
- Gates are cheap: `validate` + the phase checklist. If a gate takes more than a session, the
  phase wasn't done incrementally.