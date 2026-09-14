---
phase: P2
type: template
status: draft
updated: 2026-09-14
---

# Registers — <Name>

One table per file, one truth per table (see CONVENTIONS.md for column formats and statuses).
These files are the machine-parsed heart of the business repo; local models edit them via work
orders; humans scan them at rituals. Append at the bottom; never renumber. The `init` command
extracts each `## <name>.md` section below into its own file automatically — keep headers intact.

## tasks.md
| ID | Task | Horizon | Phase | Status | Owner | Due | Done when |
|----|------|---------|-------|--------|-------|-----|-----------|
| T-P0-001 | Fill business profile from requestor interview | 0 | P0 | TODO | orchestrator | | profile complete + user confirm |

## questions.md
| ID | Question | Why it matters | Block | Status | Answer / ref |
|----|----------|----------------|-------|--------|-------------|
| Q-001 | (first open question from intake) | | | OPEN | |

`Block` = which phase gate this question blocks (`P0`, `P1`, …) or blank if non-blocking.

## decisions.md
| ID | Decision | Rationale | Date | Status | Linked |
|----|----------|-----------|------|--------|--------|
| D-001 | Proceed as sole prop until revenue justifies LLC | lower filing cost now | | active | R-001 |

## business-facts.md
| ID | Statement | Value | Source + date | Confidence | Phase |
|----|-----------|-------|--------------|-----------|-------|
| F-001 | (founder-provided or researched fact) | | founder, 2026-09-14 | reported | P0 |

Confidence: verified (primary source) / reported (secondary) / estimated (math shown) / guessed (labeled).

## assumptions.md
| ID | Assumption | Kill-test | Status |
|----|------------|-----------|--------|
| A-001 | Customers will pay $X for Y | interview 5 target customers; ≥3 pre-commit | UNTESTED |

Statuses: UNTESTED / TESTING / PASS / FAIL → (result F-nnn).

## risks.md
| ID | Risk | P | I | Mitigation | Status |
|----|------|---|---|------------|--------|
| R-001 | (risk statement) | H/M/L | H/M/L | | OPEN |

P = probability, I = impact. Statuses: OPEN / MITIGATED / HAPPENED → (decision/outcome).

## compliance.md
| ID | Item | Authority | Type | Deadline | Status | Source |
|----|------|-----------|------|----------|--------|--------|
| C-001 | (license/permit/filing/registration) | | one-time / ongoing | | TODO | |

Statuses: TODO / DOING / DONE → (evidence) / N/A → (why). Deadlines get `[SLUG]` calendar events.

## flex.md
| ID | Module | Trigger / context | Anchor | Status | Owner | Approved by | Date |
|----|--------|-------------------|--------|--------|-------|-------------|------|
| FM-001 | (business-specific expansion — e.g. fundraise, licensing gauntlet, seasonal ramp, content engine) | (what surfaced it) | (one of: P1-pivot / P2 / P3P4-parallel / pre-P5 / P7-recurring / P6-driven) | proposed | | (awaiting [U]) | |

Flex modules extend the core chain without altering it. Models may propose; only the user
activates **[U]**. Anchors say where the module slots in. See `harness/PHASES.md` "Flex modules".

## roles.md
| ID | Role | Type | Assignee | Scope | Status | Approved by | Date |
|----|------|------|----------|-------|--------|-------------|------|
| RL-001 | (proposed role — e.g. operations lead, bookkeeper, social media) | business | (vacant) | (what this role owns) | proposed | (awaiting [U]) | |

System roles (founder, orchestrator, agent, professional) are seeded by `init` and need no
approval. Business roles have **no defaults** — proposed with judgment, formalized only with
**[U]**. Standing rule: always propose role separation early (see CONVENTIONS.md). IDs: `RL-nnn`.

## config.md
| ID | Key | Value | Basis | Approved by | Date | Notes |
|----|-----|-------|-------|-------------|------|-------|
| CFG-001 | (parameter key — e.g. date-format, currency, spend-threshold) | (value) | harness default / override: D-nnn (user, date) | — | | |

Single source of business parameters; docs reference keys symbolically ({{spend-threshold}}).
Canonical keys: `harness/lib/defaults.md`. Overrides need **[U]** + logged decision. IDs: `CFG-nnn`.

## registers/README.md (in the business repo)

Keep it to this: the map of what lives where and the parsing rules pointer. When a register
grows past ~100 rows, split into `tasks-archive-<year>.md` via a logged decision; the active
file stays small.