# P4 — Technology & Infrastructure

**Purpose:** stand up the minimal, right-sized technology the business needs — with a
default preference for an **internal team structure and open-source AI tooling**
(openwebui + openterminal/shell agent + langflow) unless the user specifies otherwise.

**Starts when:** G2 (may run parallel to P3 for tech-heavy types). **Exits at:** G4. **Span:** 1–2 weeks.

## Steps

1. **Inventory needs from the plan** (P3 draft) — what does this business *do* daily, and
   which of those need software: selling, marketing, scheduling, invoicing, inventory,
   accounting, support, content. Map each to a tool category; mark categories the internal
   stack can cover.
2. **» Tech stack decisions** → `docs/plan/40-tech-infrastructure.md` (template) —
   for each category: options, decision, cost, why. Every choice gets a `D-nnn`.
   - **Default preference:** internal team structure using **openwebui** (model routing,
     personas, knowledge), **openterminal or a shell agent** (file ops, git, the foundry
     CLI), **langflow** (flow automation) — see `harness/lib/toolstack-reference.md`.
   - Any deviation from the default is a logged decision with the reason (cost,
     compliance, skill, scale, or user preference).
3. **DevOps approach** — hosting philosophy, environments (dev/prod), secrets handling,
   backups, monitoring. Self-hosted where the team can run it; SaaS where it can't. Record the run rate.
4. **Marketing/outreach tooling** — email, social, website, analytics; region-relevant
   platforms (e.g., Google Business Profile for local services; niche platforms per playbooks).
5. **Security baseline** (no exceptions): password manager, MFA on all accounts, separate
   business email, off-repo secrets, device hygiene; PCI/HIPAA/etc. only if the type demands.
6. **AI enablement** (default-on): which business functions get an agent assist first —
   content, outreach, support macros, bookkeeping reconciliation, market scanning. One
   concrete first automation, sized ≤ a week to build in langflow, becomes a P5 task.
7. **Procurement tasks** → `registers/tasks.md` (`T-P4-nnn`): accounts to create, domains,
   hardware, software purchases **[U]** for spend above threshold.
8. **Reconciliation pass (if P3 ran in parallel)** — confirm both directions: tech run-rate is
   in the financial plan; plan sections referencing the stack (ops, GTM, team) match these
   decisions. Re-check anything G3's reconciliation flagged, don't re-argue it.
9. `validate` → **G4** → announce P5.

## Decision hygiene

- Cost column sourced or `est.`; run-rate totals flow into the P3 financials (or next amendment).
- Right-size: the stack should run the business **as planned for the next 6–12 months** —
  not the imagined version at scale.
- Buy-vs-build: default to buy for commodity (email, payments), build in langflow for glue
  and repeat-flows the internal team can maintain.
- Data residency/compliance only where the type/regulation demands (see playbooks).

## Done when

Every tool category in the template is decided (chosen / deferred with D-nnn / N/A);
devops + security baseline written; procurement tasks exist with due dates; cost run-rate
in the financials; G4 recorded.

## Failure modes

- Tool sprawl "to be safe" — every tool is a liability; the default stack keeps this honest.
- Choosing for the business at scale instead of the business at launch.
- Unrecorded exceptions to the default preference (if you deviate, log why).
- No security baseline because "we're small" — small is who gets hit hardest.
- Procurement tasks without owners/dates (they rot).

## Gate criteria (G4)

Stack decisions logged with costs; default-preference adherence or logged exceptions;
security baseline present; run-rate in financials; procurement tasked. See GATES.md.