# Business Foundry — a repeatable harness for conceiving, vetting, and standing up businesses

**What this is:** a portable, repo-based operating system for turning business ideas into
operating companies. One formula, many businesses. It defines a predictable chain of phases
(P0→P7), the artifacts each phase must produce, quality gates between phases, and a
token-thrifty context protocol so frontier models can orchestrate while small local models
execute the pieces.

**Audience:** any model or human. Start here, then read only what the next step needs.
Nothing in this harness requires a specific vendor, cloud, or model.

## The chain

```
IDEA → P0 INTAKE → [G0] → P1 VETTING → [G1] → P2 FOUNDATION → [G2] → P3 BUSINESS PLAN → [G3]
     → P4 TECH & INFRA → [G4] → P5 EXECUTION PLAN → [G5] → LAUNCH → P7 OPERATE ⇄ P6 FUTURE
```

Inside every phase the same loop: **BRIEF → DO → RECORD → CHECK**. A phase may not start
until the previous gate is recorded PASS or CONDITIONAL (conditions become tracked tasks).

## Quickstart

```bash
# 1. Start a business (creates businesses/<slug>/ from templates)
python3 bin/foundry.py init my-biz "My Business" --region US-WI --type local-service

# 2. Work the chain
python3 bin/foundry.py status my-biz        # where are we?
python3 bin/foundry.py next my-biz          # what's next?
python3 bin/foundry.py workorder my-biz T-P2-001   # brief one task for any model
python3 bin/foundry.py gate my-biz P0 --pass --notes "intake complete"
python3 bin/foundry.py validate my-biz      # automated repo health checks
python3 bin/foundry.py rollup my-biz        # ≤600-token resume pack for any session
```

Then follow `harness/phases/P0-INTAKE.md`. The business repo (not this harness) is the
source of truth for that business. Every command also accepts a path instead of a slug —
that's how the frozen demo in `examples/lakeside-roasters/` stays addressable
(`foundry.py status examples/lakeside-roasters`).

## Repo map

| Path | What it is | Who reads it |
|---|---|---|
| `README.md` | This file — entry point | Everyone, once |
| `harness/PHASES.md` | Thin index of the chain | Everyone, once |
| `harness/CONVENTIONS.md` | IDs, statuses, file formats (machine-readable rules) | Anyone writing anything |
| `harness/GATES.md` | Quality bars, gate procedure, automatic-fail triggers | Orchestrator at each gate |
| `harness/CONTEXT-PROTOCOL.md` | Token budgets, session packs, work orders, model roles | Session runners |
| `harness/RUNBOOK.md` | Session flow, weekly/quarterly rituals, user-interaction rules | Orchestrator, every session |
| `harness/phases/P0..P7` | One brief per phase: steps, done-when, failure modes | When running that phase |
| `harness/templates/` | Fill-in skeletons for every artifact | When creating a doc |
| `harness/lib/` | Playbooks: business-type routing, jurisdictions, toolstack, question bank | On demand |
| `bin/foundry.py` | The CLI (stdlib-only Python, no dependencies) | Everyone |
| `businesses/<slug>/` | One self-contained repo per business — the living record | Its business only |
| `examples/` | A worked synthetic example (read to see "what good looks like") | New models, onboarding |

## Operating rules (the short version)

1. **The business repo is the only source of truth.** The harness is read-only machinery.
2. **Small steps, real artifacts.** One completed item, one commit.
3. **Every number needs a source row** (`registers/business-facts.md`) or an explicit `est.` label.
4. **Frontier orchestrates, locals execute** pieces via work orders, **user approves gates**
   and all one-way doors (entity type, spend, names).
5. **Never batch-record.** If it happened, it's recorded; if it's recorded, it happened.
6. **Unknowns are never blank** — they get a question (Q-nnn) or assumption (A-nnn) ID.

## Design intent (why it is built this way)

- **Predictable chain:** every business travels the same phase sequence, so any model
  (or human) can pick up any business and know exactly where it stands.
- **Token-optimal:** registers hold data once; docs reference IDs; `rollup` regenerates
  session context instead of re-reading files; work orders carry complete context in ≤2k
  tokens so local models never need the repo history.
- **Model-agnostic:** frontier models plan/gate/propose; local models do scoped piece work.
  Everything degrades gracefully to "read file, write file, run python".
- **Not all businesses are equal:** business-type playbooks route emphasis (deep vs. stub)
  per section, and ceremony scales with risk, not template size.
- **Portable:** plain markdown + one stdlib-only Python file. Copy the repo, point any
  model at this README, and it runs. Nothing else to explain.

## Default stack preference

Unless the user specifies otherwise, plan the business around an **internal team structure
using openwebui (model routing/personas/knowledge), openterminal or a shell agent (file
ops, git, CLI), and langflow (flow automation)** — see `harness/lib/toolstack-reference.md`.
The harness itself is stack-agnostic: it works the same in any environment.