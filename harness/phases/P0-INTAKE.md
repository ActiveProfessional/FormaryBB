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
   (offering, locale, expected customer, founder capacity, competitive awareness, type hint;
   the Tier 1 interview questions), each needing a disposition: `captured` (user provided →
   fact row), `extrapolated` (user doesn't have it → model's best contextual judgment as an
   A-nnn, kill-test first in the P1 plan), or `unknown-by-choice` (user confirmed they don't
   know → Q-nnn, non-blocking).
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

## Question seeds — explicit two-tier interview structure

**Tier 1 — floor fields (blocking):** collected first, without exception. These six map 1:1
to the intake floor and G0 cannot pass without them:
1. What are you selling? (offering — must be `captured`)
2. Where will this operate? (locale)
3. Who might buy this? (expected customer)
4. What can you bring — time, money, skills? (founder capacity)
5. What do you know about who does this today? (competitive awareness — "P1 will research" is a fine answer)
6. What kind of business is this? (type hint — a guess is fine, refined at P1)

**Tier 2 — everything else (asked, never blocking):** asked opportunistically as the
conversation allows — mission in their own words, price anchors, personal constraints
(family, existing job, non-competes), assets and relationships, success-in-1-year, abandon
condition, regional quirks, stack preferences. Unanswered Tier 2 items become Q-nnn rows or
A-nnn extrapolations — never blockers, never silently skipped.

A terse requestor answers Tier 1 in five sentences and the session still ends G0-valid. A
detailed requestor answers everything. Both are equally welcome; only Tier 1 can stop the gate.

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