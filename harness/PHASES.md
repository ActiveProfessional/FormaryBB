# The Foundry Chain — phase overview

**Audience:** all. This is a thin index; details live in `phases/Pn-*.md`. Gate criteria live in `GATES.md`.

```
IDEA → P0 INTAKE → [G0] → P1 VETTING → [G1] → P2 FOUNDATION → [G2] → P3 BUSINESS PLAN → [G3]
     → P4 TECH & INFRA → [G4] → P5 EXECUTION PLAN → [G5] → LAUNCH → P7 OPERATE ⇄ P6 FUTURE
```

| Phase | Plain name | Purpose | Core outputs | Gate | Typical span* |
|---|---|---|---|---|---|
| P0 | Intake | Capture the idea faithfully: nature, mission, region, founder facts, key figures | `business-profile.md` complete, question seed, P1 research plan | G0 | 1 session |
| P1 | Vetting | Try to kill the idea cheaply: market, customer evidence, economics, founder fit — **pivot-scan before any KILL** | `10-market-research.md`, competitor rows, unit-economics sketch, verdict | G1 | 1–2 weeks |
| P2 | Foundation | Refined mission & goals, entity decision, name clearance, capital & runway, risk/compliance groundwork | `00-goals-mission.md`, `10-incorporation.md`, registers live, name cleared | G2 | 1–3 weeks |
| P3 | Business plan | The operating document — localized, personalized, followable | `docs/business-plan/` (master, market, competition, financials, GTM, brand) | G3 | 2–4 weeks |
| P4 | Tech & infra | Minimal AI-operable stack, devops, security baseline | `40-tech-infrastructure.md`, stack decisions, procurement tasks | G4 | 1–2 weeks |
| P5 | Execution plan | Dated, owned task list across horizons; calendar synced; launch checklist | `50-execution-plan.md`, fully populated `registers/tasks.md`, tagged calendar events | G5 | ~1 week |
| P7 | Operate | Run per plan; measure vs. targets; keep the repo truthful | metrics snapshots, quarterly reviews, amended plans | quarterly | ongoing |
| P6 | Future | Expansion proposals, each shared with user and answered on record | `docs/future/proposal-vN.md` with verbatim user response | — (no gate) | opportunistic |

\* Spans assume a solo founder with a day job. Compress per the business-type playbook
(`harness/lib/business-type-playbooks.md`); a one-person local service may clear P2–P5 in
days, while a regulated or funded venture takes longer. Effort follows risk, not template size.

## Glossary (plain-language definitions — the codes exist for token economy, the meanings live here)

| Code | Means |
|---|---|
| P0–P7 | Phases of the chain (see table above for plain names) |
| G0–G5 | Gates: quality checks between phases. Verdicts: PASS / CONDITIONAL / FAIL |
| Quarterly gate | P7's recurring review (metrics vs. targets, compliance sweep, plan amendments) |
| [U] | User approval required before action — verdicts and one-way doors always |
| » / ~ | Depth markers from the business-type playbooks: go deep / stub-with-logged-reason |
| [SLUG] | Calendar event tag tying events to a business (e.g. `[LAKESIDE]`) |
| T/Q/D/F/A/R/C/FM | Register ID prefixes: task, question, decision, fact, assumption, risk, compliance, flex module |
| Flex module (FM-nnn) | Business-specific extension to the chain — proposed by models, activated only by the user |
| N/A → (D-nnn) | Deliberately skipped, with the logged reason. Never blank, never silent |

## Order rules

- Never skip a gate. CONDITIONAL moves forward with tracked conditions; FAIL stops and repairs.
- **Pivot-first:** a draft KILL at G1 triggers a mandatory **pivot scan** before the KILL can
  be confirmed (see the P1 brief). We exhaust the variables before we abandon the idea.
- P4 may run in parallel with P3 for tech-heavy businesses, but parallel work requires a
  **reconciliation pass** (checked at G3 and G4), and both gates precede P5.
- P6 proposals may be drafted any time after P1, but accepted P6 tasks never displace P5 horizon-0 (launch) tasks.
- Active flex modules join the chain at their anchor; they extend the core, never alter it.
- Killed businesses are archived, never deleted. Revival = fresh P1 against the preserved profile (history intact).

## The loop inside every phase

**BRIEF** (pick the item; write a work order if delegating) → **DO** (execute or delegate)
→ **RECORD** (update the task row, registers, and doc; commit) → **CHECK** (gate impact).

## Flex modules — the expansion valve

The core chain is a spine, not a cage. When a business needs work the chain doesn't cover
(a fundraise, a licensing gauntlet, a seasonal ramp, a content engine, a co-founder search),
the harness proposes a **flex module**:

- Recorded in `registers/flex.md`: `FM-nnn | module | trigger/context | anchor | status | owner | approved-by | date`
- **Proposed by any model; activated only by the user [U].** Never the reverse.
- Anchored where it slots into the chain: `P1-pivot`, `P2`, `P3P4-parallel`, `pre-P5`, `P7-recurring`, `P6-driven`.
- Worked like any phase work: its tasks get IDs, its outputs land in docs, and the gate at
  its anchor checks them.
- `validate` enforces anchors and approval records, and flags any tampering with core phases.

This is how the harness "learns" a business without the core path being corrupted: models
propose enrichment, the spine stays stable, the user decides.

## Immutability rules (what models may not change)

The core chain — phases P0–P7, gates G0–G5, the quarterly gate — is the stable spine every
model and human can rely on. Processing models may NOT rename, reorder, remove, or add core
phases or gates. They MAY: propose flex modules (user-approved), mark sections N/A with a
logged decision, and deepen or stub sections per the playbooks.

## Completion checklist (chain level)

Per phase, the phase brief's checklist is the authority. The chain-level done list:

- [ ] G0: profile confirmed by the user
- [ ] G1: verdict on record (KILL only after a pivot scan — options exhausted or user-rejected)
- [ ] G2: entity professional-verified + user-approved; name cleared; runway complete
- [ ] G3: plan approved; reconciled with P4 if they ran in parallel
- [ ] G4: stack decided; security baseline written; run-rate in financials
- [ ] G5: dated/owned task list; calendar tagged; launch checklist approved
- [ ] Launch: launch-day actions complete; P7 rhythm running
- [ ] Flex: every proposed module decided (active or dropped) — nothing pending without a user answer

## Tailoring — not all businesses are created equal

1. **Type routing:** the profile records a business type; `harness/lib/business-type-playbooks.md`
   marks which plan sections get depth (**»**) vs. stubs (**~**), typical legal/stack/KPI load,
   and phase compression guidance.
2. **Ceremony scaling:** a one-person local service passes P3 with a 6-page plan; a regulated
   multi-founder venture gets the full template. The gate is "could a stranger execute this?",
   not "did you fill every box?".
3. **Local law wins:** `harness/lib/jurisdictions.md` is a starting map, never the last word —
   every legal claim becomes a verification task with a source or a professional to confirm it.
4. **The chain is a floor, not a ceiling:** anything the business needs beyond the core phases
   lands as a flex module (`registers/flex.md`) — proposed, user-approved, anchored — so nothing
   important gets lost just because the core didn't name it.