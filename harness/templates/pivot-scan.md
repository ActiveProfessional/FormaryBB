---
phase: P1
type: template
status: draft
updated: 2026-09-14
---

# Pivot Scan — <Name>

**Trigger:** P1 kill-tests drafted a KILL. **Purpose:** find the viable adjacent business
before abandoning the idea — change the variables, not necessarily the dream.
**Rule:** kill the variables before you kill the idea. KILL is confirmed only when pivot
options are exhausted or user-rejected on record.

## Root variables — re-examine each

| Variable | Current value | Alternatives considered | Why it might fix the failed test |
|---|---|---|---|
| Customer / segment | | | |
| Geography / market | | | |
| Offering (product/service) | | | |
| Channel | | | |
| Pricing model | | | |
| Season / timing | | | |
| Capability & assets (equipment, licenses, relationships) | | | |
| Scale / ambition | | | |

## Pivot options

| ID | Pivot | Which failed test it answers | Cheap kill-test | Verdict |
|----|-------|------------------------------|----------------|---------|
| PV-1 | | | | viable / not viable / unknown |
| PV-2 | | | | |

Each option gets a **cheap feasibility kill-test**, not a full P1 — enough evidence to
decide whether it's worth a real test, not enough to prove it works.

## User response [U] (verbatim, dated)

> "<quoted answer>" — <date>

## Outcome

- **Accepted pivot** → profile amended (logged `D-nnn`), affected P1 tests re-run, verdict
  continues as PIVOT → GO.
- **All rejected / exhausted** → KILL confirmed; archive the repo with this scan attached.
- Rejection reasons recorded verbatim — resource constraints ("I only have a push mower,
  no way to get a tractor") are valid and final.

*(Canonical example: lawn mowing in Alaska fails the season test — but the same equipment
class, a tractor with a plow blade instead of a mowing deck, turns the business 365 days
a year. The customer stays, the place stays, the offering changes. The first version
deserved to die; the idea didn't.)*