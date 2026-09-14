# P1 — Vetting

**Purpose:** try to kill the idea before it costs money. Research market, customers,
competition, economics, and founder fit — then a verdict: **GO / PIVOT / KILL / HOLD**.
Evidence over enthusiasm.

**Starts when:** G0 PASS. **Exits at:** G1. **Span:** 1–2 weeks of part-time research.

## Steps (in order)

1. **» Research market** → `docs/business-plan/10-market-research.md` (template): size,
   growth, trends — sourced or `est.`, every number a fact row.
2. **» Target segments & evidence** — 2–4 segments, each with the business-type playbook's
   minimum evidence (see `harness/lib/question-seeds.md`). At minimum: a real person's stated
   pain or a verifiable behavioral proxy. Record every contact as a fact row (privacy rule below).
3. **» Competitors** → `registers/business-facts.md` rows + a competition snapshot section:
   who, price, reach, your honest edge. Include the do-nothing alternative — the real competitor.
4. **» Economics sketch** — rough unit economics from facts+assumptions: price, COGS,
   CAC, fixed costs, break-even, gross margin. This is a sketch — P3 financials make it rigorous.
5. **» Regulatory & barrier scan** — licenses, permits, zoning, industry rules, personal
   qualification requirements (licenses, background checks), insurance. Rows in `compliance.md`
   (verify-only at this phase; a task may be "have professional confirm C-004").
6. **» Founder fit** — skills/assets/relationships against the requirements, honest: the user's
   NM field-force internship is the kind of asset that gets recorded here (domain knowledge, relationships).
7. **Kill-tests** — each `A-nnn` gets its test written and run; results logged as fact rows.
8. **Verdict draft** → decision register: GO / PIVOT (what changes) / KILL (why) / HOLD
   (re-test trigger + date). Walk it past the user.
9. `validate` → **G1** → announce P2 (or archive if KILL).

## Research discipline

- Sourced facts only; `est.` when unavoidable, each tied to an `A-nnn`.
- Primary > secondary > AI-synthesized (mark synthesis as `guessed`).
- **Stop rule:** stop researching when new hours stop changing the verdict — the verdict is
  the deliverable, not the research file.
- **Privacy rule:** customer conversations are recorded as facts ("3 of 5 cafe owners in
  Madison raised X") — no names/PII in the repo; raw notes stay with the founder, or in
  `source/` if shareable.
- Budget the research: hours per question, per the question seeds doc.

## Done when

Market doc filled (or honestly stubbed where the playbook allows); every blocking question
resolved or converted to a task; kill-tests run with results on record; verdict decision
written; G1 recorded.

## Failure modes

- Confirmation bias — only seeking supporting evidence (kill-tests exist to counter this).
- Research sprawl without a verdict.
- Treating secondary blogs as `verified`.
- Skipping the do-nothing competitor.
- Verdict by user default ("we started so let's continue") — the verdict needs evidence either way.

## Gate criteria (G1)

Customer evidence ≥ playbook minimum per segment; kill-tested assumptions; verdict decision
recorded; **[U]** verdict shared with the user before P2 begins.