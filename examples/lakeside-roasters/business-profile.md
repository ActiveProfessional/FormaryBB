---
business: lakeside-roasters
phase: P0
type: document
status: approved
updated: 09-14-2026
slug: lakeside-roasters
name: Lakeside Roasters
region: US-WI
btype: local-service
---

# Business Profile — Lakeside Roasters

*(Synthetic example — every "fact" below is invented to demonstrate the format.)*

One page. A stranger should be able to read this and know what this business *is*.

## Basics

| Field | Value |
|---|---|
| Name (working) | Lakeside Roasters |
| Slug | lakeside-roasters |
| Business type | local-service (coffee roasting — food-adjacent, see note) |
| Region / market | Madison, WI (east side) |
| Founder(s) | Founder A (solo) |
| Status | active |
| One-liner | Small-batch roasted coffee, sold at two farmers markets and via subscriptions, from Madison's east side |

## Nature of the business

Founder roasts coffee in rented commercial kitchen time and sells (a) 12 oz bags at the
Dane County Farmers Market and a smaller east-side market, (b) a weekly subscription
delivered locally. Not a café — no retail space, no employees in year 1.

> "I want to be the coffee people bring to their neighbors, not the coffee that competes
> with Starbucks." — founder, 09-14-2026

## Mission (as intended)

Bring genuinely fresh, locally roasted coffee to the east side of Madison, with a
subscription that makes the neighborhood's mornings better — and keep it a one-person
business the founder actually enjoys.

## Personal / founder context

- 4 years home-roasting hobbyist; 100+ batches on a 500g fluid-bed roaster
- Full-time day job (software) — ~10 hrs/week for the business, weekends for markets
- Startup capital: $3,000 (savings; founder-provided)
- Constraints: no café lease, no employees year 1, keep the day job until revenue ≥ $2k/mo
- Relationships: knows two market organizers socially; neighborhood association member

## Key facts, figures, and constraints

| Fact | Detail | Source |
|---|---|---|
| Capital available | $3,000 | founder, 09-14-2026 |
| Weekly hours available | ~10 | founder, 09-14-2026 |
| Target price point | $16–18 / 12 oz bag | founder's anchor; verify vs. market (P1) |
| Green coffee cost (current) | ~$6.50/lb est. from current hobby supplier | founder, 09-14-2026 |

## Regional / niche specifics

- Madison: strong farmers-market culture; Dane County Farmers Market is a real sales
  channel with a waitlist — east-side market is smaller but accessible (verify process, P1)
- Cottage-food rules may or may not cover roasted coffee in WI — **must verify** (T-P1-001)
- Seasonality: market traffic drops hard Nov–Feb → subscription is the winter revenue plan

## Success looks like (1 year)

25 weekly subscribers + steady market Saturdays ≈ $1,500–2,000/mo revenue, without
quitting the day job or hating weekends.

## Abandon condition

If after two market seasons the subscription can't hold 15 members, stop and return to
hobby roasting. (Founder's words, recorded 2026-09-14.)

## Open questions seeded

See `registers/questions.md` — Q-001 placeholder to be replaced by the real intake
questions; Q-002 answered (shared commercial kitchen rental confirmed).

## Intake floor

**The prerequisite floor for vetting.** Each of the six floor fields must carry a disposition
before G0 can pass. Ask everything, gate only on the floor: prompt comprehensively, gate minimally.

| # | Floor field | Disposition | Value / summary | Evidence |
|---|---|---|---|---|
| 1 | Offering (what is sold) | captured | Small-batch roasted coffee: 12 oz bags at two farmers markets + weekly local subscription | F-001, F-004 (founder, 2026-09-14) |
| 2 | Locale / market region | captured | Madison, WI (east side); Dane County Farmers Market + east-side market | F-001 (founder, 2026-09-14) |
| 3 | Expected customer | captured | East-side Madison coffee drinkers: market shoppers + neighbors on a weekly subscription | F-002 (founder, 2026-09-14) |
| 4 | Founder capacity (time / capital / skills) | captured | ~10 hrs/week; $3,000 capital; 4 yrs roasting experience | F-001, F-002, F-003 (founder, 2026-09-14) |
| 5 | Competitive awareness | captured | Knows of 4 local roasters at retail; Starbucks as the mass alternative; no subscription rival known nearby | F-005 (founder, 2026-09-14; P1 will deepen) |
| 6 | Business-type hint | captured | local-service, food-adjacent (roasted coffee, no café) | playbook routing confirmed at P1 |

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