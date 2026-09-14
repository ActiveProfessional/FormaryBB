# Runbook — session flow, rituals, user-interaction rules

**Audience:** the orchestrator (frontier model or human) running any session for any business.

## Session flow

1. **Orient.** `foundry.py rollup <slug>`. Announce current phase, gate state, open questions ≤3, next 3 tasks.
2. **Work.** Pick the next item(s) the phase brief lists. Delegate self-contained units as work orders;
   do judgments yourself. One unit at a time; append, don't rewrite.
3. **Record.** Update rows with evidence, then commit `[<slug>] <ID> what changed`. Never
   batch-record — a session ends with rows and commits, not with "I'll write it down later."
4. **Report.** ≤10 lines: what moved, what's blocked, what you need from the user.

**Anti-patterns:** re-reading everything each session; writing prose in chat that should be
in the repo; letting a session end with DONE-feeling but no register updates; delegating
without verifying the executor's evidence.

## User-interaction rules

- **Ask, don't guess, for:** numbers you can't source, anything one-way, and anything marked **[U]**.
- **One-way doors need explicit user approval before action:** entity filing, bank accounts,
  contracts, spend above the profile's threshold, brand names, hiring, publishing.
- Present choices compactly: options + tradeoffs + your recommendation + what you need from them.
- When the user answers: record it — verbatim quote into the doc/decision/proposal-response,
  with date. Unrecorded answers don't exist.
- Push back when evidence disagrees with the user's instinct, citing the F/Q/A IDs. You work
  for the business's success, not for agreement.
- If a request breaks harness rules, say what it would cost and propose the compliant version.

## Rituals

### Weekly review (orchestrator + user, ~15 min)
- Overdue + next-7-days tasks (rollup), gate conditions in progress, new questions to answer.

### Monthly snapshot (orchestrator alone)
- Update `metrics.md` (if operating) and `status.md` (what changed, what's coming).
- Re-run `validate`; fix drift.

### Quarterly review (orchestrator + user)
- Quarterly gate (GATES.md): metrics vs. targets, variance ≥25% triggers plan amendment,
  compliance expiry sweep, decision consistency check.
- Archive old quarter's calendar events; confirm next quarter's.

### P6 proposal cycle
- A proposal is a **proposal first** — draft → share with the user → get a response on record →
  then update the plan/docs accordingly. Never treat acceptance as implied by silence.
- Every proposal gets a row in `decisions.md` once answered (accepted / declined / deferred, with reason).

## Calendar integration

- When a task gets a due date, create a tagged calendar event `[SLUG] <task text>` (see CONVENTIONS.md).
- Deadline events (legal, tax, renewal) get 1440-min reminders; meetings get 10.
- Cancel/reschedule events when task rows change. Review the calendar weekly alongside tasks.
- If no calendar tooling is available, the tasks register due dates are the fallback record.

## Starting a new business (checklist)

1. `foundry.py init <slug> "<name>" --region <r> --type <t>` — creates the repo from templates.
2. Fill `business-profile.md` from the user's idea (P0 brief). Ask the question-seed questions;
   log every answer as facts/questions.
3. Write the P1 research plan, seed the registers, run `validate`.
4. Walk the user through the profile; get explicit confirmation → record G0.
5. Announce next phase (P1) and its first tasks.

## Handling common situations

| Situation | Response |
|---|---|
| User brings a new idea mid-session | Capture it in the relevant doc/register with a date; if it's a strategic change, a P6 proposal draft |
| Business idea proves flawed | Record evidence, draft the G1 KILL **only after the pivot scan** — change the variables (offering, geography, customer, season, channel) before abandoning the idea; walk options past the user; KILL is confirmed when pivots are exhausted or user-rejected on record |
| A phase-gap appears the chain doesn't cover | Propose a flex module (FM-nnn) in `registers/flex.md` with anchor + trigger; **[U]** activates it — core phases stay immutable |
| Flex module proposed | Share compactly: what, why now, anchor, effort; never activate without the user's approval — `validate` enforces this |
| Executor output looks wrong | Verify against source; if wrong, orchestrator fixes and notes the pattern in the work order reply |
| Two registers disagree | Deciding which is right is a `D-nnn`; fix the loser; log it |
| Session interrupted | Rollup on return states where things stand; the last commit is the recovery point |
| User says "just do it" on a one-way door | Confirm scope in one line, record the decision, proceed — but only after the record exists |
| A purchase exceeds `{{spend-threshold}}` | Stop; it's a one-way door — [U] before spending (config key in `registers/config.md`) |
| A task's natural owner doesn't exist yet | Check `registers/roles.md`: system roles cover solo operation; if the work needs a business role, propose it (the standing rule: propose separation early) and wait for [U] before assigning |
| Regulated industry detected at intake | Pull the regulated playbook rows early; legal tasks get professionals and real due dates |
| Founder is a non-resident / multi-region | Jurisdiction rows in compliance register get extra care at P2; one region = primary, others = tasks |