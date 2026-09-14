# The Foundry Chain — phase overview

**Audience:** all. This is a thin index; details live in `phases/Pn-*.md`. Gate criteria live in `GATES.md`.

```
IDEA → P0 INTAKE → [G0] → P1 VETTING → [G1] → P2 FOUNDATION → [G2] → P3 BUSINESS PLAN → [G3]
     → P4 TECH & INFRA → [G4] → P5 EXECUTION PLAN → [G5] → LAUNCH → P7 OPERATE ⇄ P6 FUTURE
```

| Phase | Purpose | Core outputs | Gate | Typical span* |
|---|---|---|---|---|
| P0 Intake | Capture the idea faithfully: nature, mission, region, founder facts, key figures | `business-profile.md` complete, question seed, P1 research plan | P0 | 1 session |
| P1 Vetting | Try to kill the idea: market, customer evidence, economics, founder fit | `market-research.md`, competitor rows, unit-economics sketch, **verdict: GO / PIVOT / KILL / HOLD** | P1 | 1–2 weeks |
| P2 Foundation | Refined mission & goals, entity decision, name clearance, capital & runway, risk/compliance groundwork | `goals-mission.md`, `incorporation.md`, registers live, name cleared | P2 | 1–3 weeks |
| P3 Business plan | The operating document — localized, personalized, followable | `docs/business-plan/` (master, market, competition, financials, GTM, brand) | P3 | 2–4 weeks |
| P4 Tech & infra | Minimal AI-operable stack, devops, security baseline | `tech-infrastructure.md`, stack decisions, procurement tasks | P4 | 1–2 weeks |
| P5 Execution plan | Dated, owned task list across horizons; calendar synced; launch checklist | `execution-plan.md`, fully populated `registers/tasks.md`, tagged calendar events | P5 | ~1 week |
| P7 Operate | Run per plan; measure vs. targets; keep the repo truthful | metrics snapshots, quarterly reviews, amended plans | P7 (quarterly) | ongoing |
| P6 Future | Expansion proposals, each shared with user and answered on record | `docs/future/proposal-vN.md` with verbatim user response | — (no gate) | opportunistic |

\* Spans assume a solo founder with a day job. Compress per the business-type playbook
(`harness/lib/business-type-playbooks.md`); a one-person local service may clear P2–P5 in
days, while a regulated or funded venture takes longer. Effort follows risk, not template size.

## Order rules

- Never skip a gate. CONDITIONAL moves forward with tracked conditions; FAIL stops and repairs.
- P4 may run in parallel with P3 for tech-heavy businesses (orchestrator judgment), but both gates precede P5.
- P6 proposals may be drafted any time after P1, but accepted P6 tasks never displace P5 horizon-0 (launch) tasks.
- Killed businesses are archived, never deleted. Revival = fresh P1 against the preserved profile (history intact).

## The loop inside every phase

**BRIEF** (pick the item; write a work order if delegating) → **DO** (execute or delegate)
→ **RECORD** (update the task row, registers, and doc; commit) → **CHECK** (gate impact).

## Tailoring — not all businesses are created equal

1. **Type routing:** the profile records a business type; `harness/lib/business-type-playbooks.md`
   marks which plan sections get depth (**»**) vs. stubs (**~**), typical legal/stack/KPI load,
   and phase compression guidance.
2. **Ceremony scaling:** a one-person local service passes P3 with a 6-page plan; a regulated
   multi-founder venture gets the full template. The gate is "could a stranger execute this?",
   not "did you fill every box?".
3. **Local law wins:** `harness/lib/jurisdictions.md` is a starting map, never the last word —
   every legal claim becomes a verification task with a source or a professional to confirm it.