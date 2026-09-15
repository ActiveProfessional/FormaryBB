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
# 0. Point the CLI at YOUR workspace (data never lands in the core repo)
export FOUNDRY_WORKSPACE=~/my-foundry-workspace    # see WORKSPACES.md

# 1. Start a business (creates <workspace>/businesses/<slug>/ from templates)
python3 bin/foundry.py init my-biz "My Business" --region US-WI --type local-service

# 2. Work the chain
python3 bin/foundry.py session my-biz --tier t1   # reading list for this session's model tier
python3 bin/foundry.py status my-biz              # where are we?
python3 bin/foundry.py next my-biz               # what's next?
python3 bin/foundry.py workorder my-biz T-P2-001 --tier t3  # brief one task for a local model
python3 bin/foundry.py gate my-biz P0 --pass --notes "intake complete" --user-approval "user confirmed <date>"
python3 bin/foundry.py validate my-biz            # automated repo health checks (--strict for more)
python3 bin/foundry.py rollup my-biz              # ≤600-token resume pack (--tier t3 trims to ~300)
```

Then follow `harness/phases/P0-INTAKE.md`. The business repo (not this harness) is the
source of truth for that business. Every command also accepts a path instead of a slug —
that's how the frozen demo in `examples/lakeside-roasters/` stays addressable
(`foundry.py status examples/lakeside-roasters`). Keep business data in a **workspace**,
not the core repo — `WORKSPACES.md` explains the three-layer model (core / workspace /
overlay) and why core stays clean.

**License:** MIT — see `LICENSE`. **Version:** see `CHANGELOG.md` and git tags.

## Onboarding — how to actually run this (novice walkthrough)

**The engine is not a running program.** No server, no install. It's (1) a state machine
made of files, (2) a CLI wrench, and (3) a protocol your model follows. The model is the
motor; the chat is the control panel; the repo is the engine. Clone-and-chat is the
intended mode of operation.

This walkthrough assumes the default stack: **openwebui** (chat + model routing + knowledge
bases) + **openterminal or any shell-agent tool** (so the model can run commands) +
**langflow** (optional, for scheduling/alerts). If you have none of these, see
"No-tools mode" at the bottom — the engine still works, just slower.

### Step 1 — Get the code onto your machine

You need Python 3 (any recent version; the CLI has zero dependencies) and git.

```bash
# macOS/Linux: open Terminal. Windows: use WSL, PowerShell works too.
git clone <your-repo-url> ~/FormaryBB
cd ~/FormaryBB
python3 bin/foundry.py --help     # if this prints a command list, you're installed
```

If you don't have the repo URL yet (it's private), ask your administrator for clone access
via GitHub → Settings → Developer settings → Personal access tokens, or use the SSH key
you set up. For this guide, `~/FormaryBB` is where the harness lives.

### Step 2 — Create your workspace (where YOUR data lives)

The harness (`~/FormaryBB`) is the machine. Your businesses are your data. They live
**separately**, so your data never contaminates the machine (and pivoting/deleting a
business never touches the engine).

```bash
mkdir ~/foundry-workspace
cd ~/foundry-workspace
git init                # your data gets its own version control — you can always roll back
```

Now tell the CLI where your workspace is. You only need to do this once per session
environment:

```bash
export FOUNDRY_WORKSPACE=~/foundry-workspace
```

To make it permanent, add that line to `~/.bashrc` (Linux) or `~/.zshrc` (macOS), or set it
in your terminal-tool's environment config. **Belt-and-suspenders:** even if you forget,
every command also accepts full paths, and the core repo's `.gitignore` refuses to commit
business data into the core — you can't accidentally pollute the machine.

### Step 3 — Create the "Foundry Orchestrator" persona in openwebui

In openwebui (Admin panel → or your workspace's persona/model area, depending on version):

1. Create a new **Model/Persona** named `Foundry Orchestrator`.
2. Route it to your **strongest model** (frontier API model, or the largest local model you
   run). This persona is T1 — it orchestrates sessions, calls gates, drafts proposals.
3. Set its **System Prompt** to the boot text (below).
4. Attach `harness/` (the folder) as a **Knowledge Base** so the persona can read phase
   briefs and playbooks on demand.
5. Enable the **terminal/shell tool** for this persona so it can actually run commands.

**Boot system prompt** (paste into the persona):

```
You are the Foundry Orchestrator (T1) for the Business Foundry harness.
Rules:
1. Every session starts: run `python3 ~/FormaryBB/bin/foundry.py session <biz> --tier t1`
   (or rollup if already oriented). Work only from what the repo says — never from memory.
2. Read only what the current step needs: rollup first, then the phase brief it names.
3. The repo is the only source of truth. Anything not in the repo gets recorded there
   before it's considered real. User answers are recorded verbatim with dates.
4. Gates marked [U] need explicit user approval — ask in chat, record the quote.
5. One-way doors (spend over {{spend-threshold}}, filings, names, hiring, publishing) stop
   and ask. FAIL is always safe to record; stopping is never a one-way door.
6. End every session with ≤10 lines: moved / blocked / needed from user / next.
7. Delegate self-contained units to work orders when an executor pool exists; verify
   one-way-door-adjacent work fully (risk-tiered verification).
8. Never modify harness/ machinery, gates, or conventions. Propose improvements instead
   (HD-nnn protocol).
```

(Adjust `~/FormaryBB` to your actual path. If your openwebui version lacks personas, the
same text pasted as the first message of a chat works fine.)

### Step 4 — (Optional) Create the "Foundry Executor" persona for small models

If you run local models (7–13B), create a second persona `Foundry Executor` routed to one:
same knowledge base, terminal tool on, system prompt:

```
You are a Foundry Executor (T3). You will receive ONE work order. Read it fully.
Do exactly the ONE step/ONE register it names. Never open other files. Never make
judgment calls — if you find a fork, stop and report it. Unsourced numbers are forbidden.
When done, reply with the exact rows you changed. You do not call gates, make decisions,
or touch anything outside the work order.
```

The Orchestrator drafts work orders via `foundry.py workorder <biz> <id> --tier t3`, then
hands them to this persona (or you paste the work order into a chat with it).

### Step 5 — Start a business (the moment of truth)

Open a chat with **Foundry Orchestrator** and type, in plain English:

> Run a session for a new business. My idea is: <your idea, any roughness>.

The persona should: run `init`, interview you (Tier 1 floor questions first, Tier 2
opportunistically — "I don't know" is a fine answer everywhere outside the floor),
fill the profile, extrapolate what you didn't know, **show you the extrapolations**, ask
you to confirm ([U]), record G0, and hand you the first P1 research tasks. That's the
engine running. Everything after is the same loop: you chat, it works the chain.

### Step 6 — (Optional) Wire the rituals so the engine nudges you

Without this step the engine is silent — it responds only when spoken to. To make it
proactive:

- **Weekly review:** openwebui **Automation** (if your build has them): schedule a prompt
every Monday 9am: *"Run the weekly review: rollup each business in the workspace, report
overdue and [U]-pending, ≤10 lines."* No automations in your build? A host **cron** job or
langflow scheduled flow works identically — anything that can send that prompt on a
schedule, or run `foundry.py status` per business and notify you.
- **Deadline alerts:** daily cron/flow runs `foundry.py rollup` per business; if the output
contains an "overdue:" or "upcoming compliance:" line, send it (email/webhook/chat).
- **Calendar:** if your environment has a calendar tool, the persona creates `[SLUG]`-tagged
events with reminders when tasks get due dates. Vanilla openwebui has no built-in calendar —
the tasks register remains the source of truth either way; calendars are a convenience layer.

### No-tools mode (degraded but fully functional)

A model with no terminal access can still run the engine with you as the relay: you paste
the rollup in, it tells you the next command, you run it yourself and paste the output
back. Clunky, but it proves the harness works in the barest chat environment. Everything
upgrades gracefully: relay → tool model → scheduled rituals → alerting → hosted app.

### Troubleshooting (the three most common novices hits)

1. **"business not found"** — `FOUNDRY_WORKSPACE` isn't set in the environment the model's
terminal tool spawns from. Fix: set it, or use full paths: `foundry.py status
~/foundry-workspace/businesses/my-biz`.
2. **Model ignores the harness** — persona wasn't given the boot prompt, or the knowledge
base wasn't attached. The persona must read the repo files; memory alone isn't the harness.
3. **Nothing ever alerts me** — that's Step 6 not being wired. The engine never pushes on
its own by design; see WORKSPACES.md and the deployment notes for trigger patterns.

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