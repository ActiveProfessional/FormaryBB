# P2 — Foundation

**Purpose:** convert a vetted GO into a legal, funded, named, risk-aware foundation. The
user's request section 1: goals, mission statement, and the incorporation essentials.

**Starts when:** G1 = GO (or PIVOT with the pivot recorded). **Exits at:** G2. **Span:** 1–3 weeks.

## Steps (parallelizable where marked)

1. **» Refine mission & goals** → `docs/business-plan/00-goals-mission.md`: mission refined
   against P1 evidence (one sentence: who, what, where, why), 3–5 measurable goals with dates,
   values only if the user provides them, and non-goals (what we will not do — the discipline list).
2. **» Entity decision** → `docs/legal/10-incorporation.md` (template):
   - Playbook + jurisdiction hints (`harness/lib/jurisdictions.md`) produce a *recommendation draft*.
   - **The recommendation must be verified before it is actionable.** Verification depth is
     risk-tiered: **a primary government source alone satisfies it for simple cases** (e.g.
     state filing-agency guidance for a solo LLC); **a licensed professional is required**
     when anything is ambiguous, regulated (fintech/health/etc.), multi-founder, or
     multi-jurisdiction. Either way the verification is a task with a real due date, and
     compliance-adjacent rows get verify-ALL treatment (CONTEXT-PROTOCOL). Entity type is
     **[U]** user-approved before any filing.
   - Register, member/manager structure, equity/ownership split, tax election notes, and
     what each choice means in plain language.
3. **» Name clearance** → decision rows: state registry search, USPTO trademark search
     (TESS), domain & social handles. Conflicts → new names → user picks **[U]**.
4. **» Funding & runway** — starting capital, runway math against the P5 timeline, burn rate
     (est. labeled); funding sources and any financing tasks.
5. **Banking, accounting, insurance, payroll** — each decided (tasks with due dates are fine;
   open questions are not). Include: business bank account, bookkeeping method/tool,
   insurance types per the playbook with **quotes documented into `source/`** (the
   incorporation doc's Insurance detail section accepts documented numbers — undocumented
   amounts remain guesses), payroll decision (hire or not yet).
6. **» Risk & compliance seeding** — `registers/risks.md` (probability × impact × mitigation,
   including founder risk and key-person risk), `registers/compliance.md` (federal, state,
   county, city; ongoing vs. one-time; deadlines → calendar **now**, tagged `[SLUG]`).
7. **Founder agreements** (if multiple founders) — equity, vesting, exit, roles; **[U]**; legal review task.
8. `validate` → **G2** → announce P3.

## Notes

- The incorporation doc contains **checklists and drafts**, not filings. Filings happen via
  P5 tasks after user approval — but the doc must be complete enough that filing is mechanical.
- Legal/financial recommendations come from professionals; the harness drafts the questions
  to ask them (that's often the highest-leverage deliverable of this phase).
- **[U] one-way doors here:** entity type, name, filings, bank choice, insurance purchase, founder agreements.

## Done when

Mission/goals approved; entity recommendation professional-verified and user-approved; name
cleared; runway math complete; banking/accounting/insurance/payroll decided (task or done);
risk & compliance registers seeded with deadlines calendared.

## Failure modes

- Filing before the user approves **or** before professional verification (never).
- Name chosen on vibes — clearance searches exist because vibes are expensive.
- Runway computed without the execution timeline in view (P5 will fix the timeline; P2 estimates).
- "We'll figure out compliance later" — every known obligation gets a C-nnn now, even if its
  task is deferred. Unknown-to-you obligations are why professional verification exists.

## Gate criteria (G2)

See GATES.md: professional-verified entity recommendation **[U]**, name cleared, runway
complete, mission confirmed, risk/compliance seeded with deadlines.