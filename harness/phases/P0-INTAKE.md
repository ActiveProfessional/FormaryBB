# P0 — Intake

**Purpose:** capture the idea faithfully so a stranger could act on it. No judgment yet —
that's P1. Mission as *intended*, facts as *given*, gaps as *questions*.

**Starts when:** G-1 (none) — the chain starts here.
**Exits at:** G0 (see GATES.md). **Span:** ~1 session.

## Inputs the requestor provides

Nature of the idea, mission intent, region/market, personal situation, and any key facts,
figures, constraints, or preferences (regional, specific, personal, niche). Everything else
is derived in later phases. Missing items become questions, never assumptions.

## Steps

1. **Create the repo.** `foundry.py init <slug> "<name>" --region <r> --type <t>`
   — slug from name; region/type from the user or your read of the idea; record both in
   the profile and flag any type uncertainty as a question.
2. **Interview for the profile.** Walk `harness/lib/question-seeds.md` + the question seeds
   below. Pull `harness/lib/business-type-playbooks.md` once the type is clear.
3. **Fill `business-profile.md`** (template). Verbatim quotes where the user said something
   in their own words — the record of intent is evidence.
4. **Fill the registers from what you know already** (they're mostly empty at P0):
   - `questions.md` — every unknown that matters, `Block` flag = "does this block the next phase?"
   - `business-facts.md` — founder-provided facts, source = "founder, <date>", confidence `reported`
   - `assumptions.md` — your working assumptions, each kill-testable
   - `risks.md` — the obvious ones; the real risk pass is P1
   - `tasks.md` — only P1 research tasks belong here so far
5. **Write the P1 research plan** into `scratch/p1-research-plan.md` and convert its items
   to tasks (`T-P1-nnn`) — it answers: what must we learn to test this idea, and how, cheaply?
6. **Run `validate`.** Fix fails.
7. **Walk the profile past the user.** Explicit confirmation → `gate <slug> P0 --pass`.
8. **Announce** P1 start + first tasks.

## Question seeds (minimum set)

What are you selling, to whom, and where? Why you? What's the money story (price, cost)?
What do you already have (skills, assets, relationships, licenses)? What constraints
(time, capital, family, existing job, non-competes)? What does success look like in 1 year?
What would make you abandon it? What's the region and its quirks that affect the idea?

## Done when

Profile complete-enough to act on; every gap is a numbered question with a Block flag;
P1 research plan exists as tasks; user confirmed; G0 recorded.

## Failure modes

- Filling gaps with plausible-sounding assumptions (they belong in `assumptions.md`, kill-tested).
- Judging the idea now — P1 does that. P0 records.
- Over-long sessions: if the interview can't finish in one sitting, the remaining seeds become OPEN questions, not blockers.
- A profile that reads like marketing copy — record what is, not what's hoped.

## Gate criteria (G0)

Profile completeness (nature/mission/region/founder facts); questions register live with
Block flags; P1 research plan written; **[U]** user confirms the profile reflects the idea.