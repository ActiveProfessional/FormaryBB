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
4. **Walk the intake floor.** The floor is the minimum P1 will not start without — six fields
   (offering, locale, expected customer, founder capacity, competitive awareness, type hint),
   each needing a disposition: `captured` (user provided → fact row), `extrapolated` (user
   doesn't have it → model's best contextual judgment as an A-nnn, kill-test first in the P1
   plan), or `unknown-by-choice` (user confirmed they don't know → Q-nnn, non-blocking).
   - **Ask for everything; gate only on the floor.** The question seeds are asked of every
     requestor — but only the six floor fields can block. A one-line idea passes with five
     extrapolations; a detailed brief passes with everything captured.
   - **Offering (field 1) must be `captured`.** If the requestor can't articulate the idea
     even with help, help them shape it before vetting — don't extrapolate their idea for them.
   - Extrapolate with best contextual judgment (locale from their location, customers from the
     offering, capacity from their situation), then show **every extrapolation** at the
     [U] walk-through for approval or correction. Ask; if they don't have it, move forward on
     extrapolations with their approval of your judgment.
5. **Fill the registers from what you know already** (they're mostly empty at P0):
   - `questions.md` — every unknown that matters, `Block` flag = "does this block the next phase?"
   - `business-facts.md` — founder-provided facts, source = "founder, <date>", confidence `reported`
   - `assumptions.md` — your working assumptions + every floor extrapolation, each kill-testable
   - `risks.md` — the obvious ones; the real risk pass is P1
   - `tasks.md` — only P1 research tasks belong here so far; floor extrapolation kill-tests come first
   - `roles.md` — system roles are seeded by `init`; propose business-role separation early, but
     formalize only with [U] (a sole proprietor runs on system roles alone)
   - `config.md` — seeded with harness defaults (date-format, currency, spend-threshold);
     confirm or override with [U]; this file is the business's single parameter source
6. **Write the P1 research plan** into `scratch/p1-research-plan.md` and convert its items
   to tasks (`T-P1-nnn`) — it answers: what must we learn to test this idea, and how, cheaply?
   Floor extrapolations lead the list.
7. **Run `validate`.** Fix fails — the floor check is mechanical; it fails until all six
   dispositions exist and every extrapolation cites a kill-tested A-nnn.
8. **Walk the profile past the user** — including every extrapolated floor row, shown
   explicitly. They approve or correct each one in this single [U] confirmation →
   `gate <slug> P0 --pass` with the approval noted.
9. **Announce** P1 start + first tasks.

## Question seeds (minimum set)

What are you selling, to whom, and where? Why you? What's the money story (price, cost)?
What do you already have (skills, assets, relationships, licenses)? What constraints
(time, capital, family, existing job, non-competes)? What does success look like in 1 year?
What would make you abandon it? What's the region and its quirks that affect the idea?

## Done when

All six intake-floor fields dispositioned (offering captured; extrapolations cited to kill-tested
A-nnns); every gap beyond the floor is a numbered question with a Block flag; P1 research plan
exists as tasks with extrapolation tests first; user confirmed profile + extrapolations; G0 recorded.

## Failure modes

- Filling gaps with silent assumptions — every model-generated floor value must be an explicit
  `extrapolated` row with an A-nnn, or it's a violation, not a shortcut.
- Blocking on detail beyond the floor — the floor is the gate; the seeds are prompts, not requirements.
- Judging the idea now — P1 does that. P0 records.
- Over-long sessions: if the interview can't finish in one sitting, the remaining seeds become OPEN questions, not blockers.
- A profile that reads like marketing copy — record what is, not what's hoped.

## Gate criteria (G0)

Intake floor complete (six dispositions, offering captured, extrapolations cited and user-approved);
profile complete-enough to act on; questions register live with Block flags; P1 research plan written
with floor extrapolation kill-tests first; **[U]** user confirms the profile — extrapolations
included — reflects the idea.