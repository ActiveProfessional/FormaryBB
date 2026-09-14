---
phase: P0
type: template
status: draft
updated: 2026-09-14
---

# Business Profile — <Name>

One page. A stranger should be able to read this and know what this business *is*.

## Basics

| Field | Value |
|---|---|
| Name (working) | |
| Slug | |
| Business type | (see harness/lib/business-type-playbooks.md for the menu) |
| Region / market | |
| Founder(s) | |
| Status | active |
| One-liner | |

## Nature of the business

What is being sold, in what form, to whom. Plain language. If the user said it in their own
words, quote them verbatim here (in quotes, with date) — intent is evidence.

## Mission (as intended)

What this business is *for*. (Refined against evidence in P2; this is the P0 record of intent.)

## Personal / founder context

Skills, experience, assets, relationships, constraints (time, capital, existing job, family,
non-competes), motivations. Everything about *the person* that shapes what this business
can be. Include the local specifics — where they live, what they know, who they know.

## Key facts, figures, and constraints

| Fact | Detail | Source |
|---|---|---|
| | | founder, <date> |

Every fact here also becomes a row in `registers/business-facts.md` if it will be used in plans.

## Regional / niche specifics

Local market conditions, regulations, culture, geography, community — anything that makes
this business *of a place* rather than anywhere.

## Success looks like (1 year)

What the founder would consider success. Concrete, checkable.

## Abandon condition

What would make the founder stop. (Asked, not assumed.)

## Open questions seeded

See `registers/questions.md` — every gap found while writing this profile has a Q-nnn there.

## Intake floor

**The prerequisite floor for vetting.** Each of the six floor fields must carry a disposition
before G0 can pass. Ask everything, gate only on the floor: prompt comprehensively, gate minimally.

| # | Floor field | Disposition | Value / summary | Evidence |
|---|---|---|---|---|
| 1 | Offering (what is sold) | | | |
| 2 | Locale / market region | | | |
| 3 | Expected customer | | | |
| 4 | Founder capacity (time / capital / skills) | | | |
| 5 | Competitive awareness | | | |
| 6 | Business-type hint | | | |

**Dispositions** (exact words; `validate` enforces):

- `captured` — the user provided it. Value required; becomes a fact row (source: founder).
- `extrapolated` — the user doesn't have it; the model proposes its best contextual judgment.
  Must cite an `A-nnn` in Evidence whose kill-test is **first in the P1 research plan** — the
  extrapolation is the first thing vetting tests, not a silent guess. User sees every
  extrapolation at the [U] walk-through and approves or corrects it.
- `unknown-by-choice` — the user confirmed they don't know and extrapolation isn't meaningful
  (e.g. competitive data is P1's job). Must cite a `Q-nnn`; non-blocking.

**Floor rule 1:** the Offering (field 1) can only be `captured`. If the requester cannot
articulate the idea even with help, it isn't ready for vetting yet — help them shape it first.
**Floor rule 2:** fields 2–6 may be extrapolated freely — a one-line idea passes the floor with
five extrapolations; a detailed brief passes with everything captured. Both are G0-valid.