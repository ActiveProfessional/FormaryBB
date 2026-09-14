#!/usr/bin/env python3
"""Business Foundry CLI — machine operations for the harness.

Stdlib-only. Works from anywhere; finds the harness root by walking up from
this file's location. Run `foundry.py --help` for the command menu.

Every command prints plain text that any model (frontier or local) can act on.
Errors go to stderr with exit code 1; success is quiet unless it has news.
"""
from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

HARNESS_ROOT = Path(__file__).resolve().parent.parent
BIZ_ROOT = HARNESS_ROOT / "businesses"
TEMPLATES = HARNESS_ROOT / "harness" / "templates"
TODAY = datetime.date.today().isoformat()

GATE_ORDER = ["P0", "P1", "P2", "P3", "P4", "P5", "P7"]  # P6 never gates

# ---------------------------------------------------------------- helpers

def eprint(*a):
    print(*a, file=sys.stderr)

def fail(msg):
    eprint(f"ERROR: {msg}")
    sys.exit(1)

def biz_dir(slug: str) -> Path:
    p = Path(slug)
    if p.is_dir():  # allow running against any path (e.g. examples/<biz> or a moved repo)
        return p
    d = BIZ_ROOT / slug
    if not d.is_dir():
        fail(f"business '{slug}' not found (looked in {BIZ_ROOT}). Existing: " +
             ", ".join(sorted(q.name for q in BIZ_ROOT.glob('*'))) if BIZ_ROOT.is_dir()
             else f"business '{slug}' not found (no businesses/ dir yet)")
    return d

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""

def rows(path: Path) -> list[dict]:
    """Parse a markdown table: header row, then data rows keyed by lowercase header."""
    out = []
    for line in read(path).splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            continue  # separator row
        out.append(cells)
    return out

def parse_table(path: Path) -> tuple[list[str], list[list[str]]]:
    r = rows(path)
    if not r:
        return [], []
    header = [h.lower() for h in r[0]]
    data = [x for x in r[1:] if len(x) == len(header)]
    return header, data

def dicts(path: Path) -> list[dict]:
    header, data = parse_table(path)
    return [dict(zip(header, row)) for row in data]

def reg(b: Path, name: str) -> list[dict]:
    return dicts(b / "registers" / f"{name}.md")

def fmt_row(d: dict, keys: list[str]) -> str:
    return " | ".join(str(d.get(k, "")) for k in keys)

def gates_passed(b: Path) -> set[str]:
    g = set()
    gdir = b / "gates"
    if gdir.is_dir():
        for f in gdir.glob("P*-record.md"):
            g.add(f.name.split("-")[0])
    return g

def next_id(ids: list[str], prefix: str) -> str:
    nums = []
    for i in ids:
        m = re.search(r"(\d+)$", i)
        if m:
            nums.append(int(m.group(1)))
    return f"{prefix}{(max(nums) + 1) if nums else 1:03d}"

def task_id_for_phase(b: Path, phase: str) -> str:
    ids = [t.get("id", "") for t in reg(b, "tasks")]
    nums = [int(m.group(1)) for i in ids for m in [re.fullmatch(rf"T-P{phase[1:]}-(\d+)", i)] if m]
    return f"T-P{phase[1:]}-{(max(nums) + 1) if nums else 1:03d}"

def append_table_row(path: Path, values: list[str]) -> None:
    """Append one data row to the last markdown table in a file."""
    lines = read(path).splitlines()
    last_pipe = max(i for i, l in enumerate(lines) if l.strip().startswith("|")) if any(
        l.strip().startswith("|") for l in lines) else fail(f"no table found in {path.name}")
    lines.insert(last_pipe + 1, "| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def update_front(path: Path, key: str, value: str) -> None:
    text = read(path)
    if text.startswith("---"):
        end = text.find("\n---", 3)
        front = text[:end]
        if re.search(rf"^{re.escape(key)}:", front, re.M):
            new = re.sub(rf"^{re.escape(key)}:.*$", f"{key}: {value}", front, flags=re.M)
        else:
            new = front.rstrip() + f"\n{key}: {value}"
        rest = text[end:]
        # keep everything after the closing --- marker
        path.write_text(new + rest, encoding="utf-8")
    else:
        path.write_text(f"---\n{key}: {value}\n---\n\n" + text, encoding="utf-8")

# ---------------------------------------------------------------- init

def cmd_init(args):
    slug = re.sub(r"[^a-z0-9]+", "-", args.name.lower()).strip("-") if not args.slug else args.slug
    if not slug:
        fail("could not derive a slug from the name; pass --slug explicitly")
    dest = BIZ_ROOT / slug
    if dest.exists():
        fail(f"businesses/{slug} already exists")
    BIZ_ROOT.mkdir(exist_ok=True)

    def t(name: str) -> str:
        return read(TEMPLATES / name)

    profile = t("business-profile.md")
    profile = profile.replace("<Name>", args.name)
    fm = ("---\n"
          f"business: {slug}\nphase: P0\ntype: document\nstatus: draft\nupdated: {TODAY}\n---\n\n")
    dest.mkdir(parents=True)

    # plan + legal + future + gates dirs with .gitkeep
    for sub in ["docs/plan", "docs/business-plan", "docs/legal", "docs/future",
                "registers", "gates", "scratch", "source", "assets"]:
        (dest / sub).mkdir(parents=True, exist_ok=True)
        (dest / sub / ".gitkeep").touch()

    # profile (front matter with slug, region, type)
    prof_fm = (f"---\nbusiness: {slug}\nphase: P0\ntype: document\nstatus: draft\nupdated: {TODAY}\n"
               f"slug: {slug}\nname: {args.name}\nregion: {args.region or ''}\n"
               f"btype: {args.type or ''}\n---\n\n")
    body = re.sub(r"^---\n.*?\n---\n\n", "", profile, count=1, flags=re.S)
    (dest / "business-profile.md").write_text(prof_fm + body, encoding="utf-8")

    # plan docs
    plan_docs = {
        "00-goals-mission.md": "00-goals-mission.md",
        "10-market-research.md": "10-market-research.md",
        "20-financial-plan.md": "20-financial-plan.md",
        "30-competition-analysis.md": "30-competition-analysis.md",
        "40-marketing-gtm.md": "40-marketing-gtm.md",
        "50-brand-identity.md": "50-brand-identity.md",
    }
    for fname, tname in plan_docs.items():
        (dest / "docs" / "business-plan" / fname).write_text(
            fm + t(tname).replace("<Name>", args.name), encoding="utf-8")
    (dest / "docs" / "business-plan" / "00-master-plan.md").write_text(
        fm + t("00-master-plan.md").replace("<Name>", args.name), encoding="utf-8")
    (dest / "docs" / "legal" / "10-incorporation.md").write_text(
        fm + t("10-incorporation.md").replace("<Name>", args.name), encoding="utf-8")
    (dest / "docs" / "plan" / "40-tech-infrastructure.md").write_text(
        fm + t("40-tech-infrastructure.md").replace("<Name>", args.name), encoding="utf-8")
    (dest / "docs" / "plan" / "50-execution-plan.md").write_text(
        fm + t("50-execution-plan.md").replace("<Name>", args.name), encoding="utf-8")
    (dest / "docs" / "future" / "00-pipeline.md").write_text(
        fm + t("future-pipeline.md").replace("<Name>", args.name), encoding="utf-8")
    (dest / "docs" / "future" / "proposal-v1.md").write_text(
        fm + t("future-proposal.md").replace("<Name>", args.name), encoding="utf-8")
    (dest / "metrics.md").write_text(fm + t("metrics.md").replace("<Name>", args.name),
                                      encoding="utf-8")
    (dest / "status.md").write_text(fm + t("status-log.md").replace("<Name>", args.name),
                                    encoding="utf-8")

    # registers — each register file gets ONLY its own section from the template
    names = ["tasks", "questions", "decisions", "business-facts", "assumptions", "risks", "compliance"]
    regs = t("registers.md")
    sections, cur = {}, None
    for line in regs.splitlines():
        m = re.match(r"^## (tasks|questions|decisions|business-facts|assumptions|risks|compliance)\.md$", line)
        if m:
            cur = m.group(1)
            sections[cur] = []
            continue
        if line.startswith("## "):
            cur = None  # any other heading ends a section (e.g. the README note)
            continue
        if cur:
            sections[cur].append(line)
    for n in names:
        body = "\n".join(sections.get(n, [])).strip("\n")
        # strip example rows so real registers start clean (tasks/questions seeds stay)
        body = "\n".join(l for l in body.splitlines()
                       if not re.match(r"^\| (D-001|F-001|A-001|R-001|C-001) \|", l))
        (dest / "registers" / f"{n}.md").write_text(
            f"---\nbusiness: {slug}\ntype: register\nupdated: {TODAY}\n---\n\n" +
            f"# {n.replace('-', ' ').title()} — {args.name}\n\n" + body + "\n", encoding="utf-8")
    (dest / "registers" / "README.md").write_text(
        f"---\nbusiness: {slug}\ntype: register\nupdated: {TODAY}\n---\n\n" +
        "# Registers — " + args.name + "\n\n"
        "One table per file, one truth per table. Formats and statuses: see "
        "`harness/CONVENTIONS.md` (authoritative). Quick map:\n\n"
        "| File | Holds | ID |\n|---|---|---|\n"
        "| tasks.md | the single authoritative task list | T-Pn-nnn |\n"
        "| questions.md | open questions, Block flag = gate it blocks | Q-nnn |\n"
        "| decisions.md | every choice worth remembering | D-nnn |\n"
        "| business-facts.md | sourced facts & figures | F-nnn |\n"
        "| assumptions.md | working beliefs + kill-tests | A-nnn |\n"
        "| risks.md | risk register | R-nnn |\n"
        "| compliance.md | obligations, deadlines → calendar | C-nnn |\n", encoding="utf-8")

    # seed rows ship inside the template sections — nothing extra to append here

    print(f"created businesses/{slug}/ for '{args.name}'")
    print(f"region: {args.region or '(unset — record in profile)'} | type: {args.type or '(unset — record in profile)'}")
    print("next: open harness/phases/P0-INTAKE.md and fill business-profile.md, then")
    print(f"  run: foundry.py validate {slug}")

# ---------------------------------------------------------------- status / next

def cmd_status(args):
    b = biz_dir(args.slug)
    prof = read(b / "business-profile.md")
    name = re.search(r"^name: (.+)$", prof, re.M)
    region = re.search(r"^region: (.+)$", prof, re.M)
    btype = re.search(r"^btype: (.+)$", prof, re.M)
    g = gates_passed(b)
    tasks = reg(b, "tasks")
    done = sum(1 for t in tasks if t.get("status") == "DONE")
    cur = "P0"
    for p in GATE_ORDER:
        if p in g:
            cur = {"P0": "P1", "P1": "P2", "P2": "P3", "P3": "P4", "P4": "P5", "P5": "P7", "P7": "P7"}[p]
    qs = reg(b, "questions")
    open_q = [q for q in qs if q.get("status", "").startswith("OPEN")]
    print(f"{name.group(1) if name else args.slug} [{args.slug}]")
    print(f"region: {region.group(1) if region else '-'} | type: {btype.group(1) if btype else '-'}")
    print(f"gates passed: {', '.join(sorted(g)) if g else 'none'} | current phase: {cur}")
    print(f"tasks: {len(tasks)} total, {done} done, "
          f"{sum(1 for t in tasks if t.get('status') == 'TODO')} todo, "
          f"{sum(1 for t in tasks if t.get('status') == 'DOING')} doing, "
          f"{sum(1 for t in tasks if t.get('status') == 'BLOCKED')} blocked")
    print(f"open questions: {len(open_q)} "
          f"({sum(1 for q in open_q if q.get('block', ''))} blocking)")
    for r in ["risks", "compliance"]:
        n = len(reg(b, r))
        print(f"{r}: {n} rows")

def cmd_next(args):
    b = biz_dir(args.slug)
    g = gates_passed(b)
    cur = "P0"
    for p in GATE_ORDER:
        if p in g:
            cur = {"P0": "P1", "P1": "P2", "P2": "P3", "P3": "P4", "P4": "P5", "P5": "P7", "P7": "P7"}[p]
    tasks = reg(b, "tasks")
    qs = reg(b, "questions")
    blocking = [q for q in qs if q.get("status", "").startswith("OPEN") and q.get("block", "")]
    print(f"current phase: {cur}")
    print(f"phase brief: harness/phases/{ {'P0':'P0-INTAKE','P1':'P1-VETTING','P2':'P2-FOUNDATION','P3':'P3-PLAN','P4':'P4-TECH-INFRA','P5':'P5-EXECUTION','P7':'P7-OPERATE'}[cur] }.md")
    if blocking:
        print(f"BLOCKING QUESTIONS (answer or task before {blocking[0]['block'] if blocking[0].get('block') else 'next'} gate):")
        for q in blocking[:5]:
            print(f"  {fmt_row(q, ['id', 'question'])}")
    cands = [t for t in tasks if t.get("status") in ("TODO", "DOING", "BLOCKED")]
    if not cands:
        print("no open tasks — create some per the phase brief")
        return
    def key(t):
        return ({"BLOCKED": 0, "DOING": 1, "TODO": 2}.get(t.get("status"), 3), t.get("due", "") or "9999")
    cands.sort(key=key)
    print(f"top {args.n} next tasks:")
    for t in cands[:args.n]:
        print("  " + fmt_row(t, ["id", "status", "due", "owner", "task"]))

def cmd_tasks(args):
    b = biz_dir(args.slug)
    tasks = reg(b, "tasks")
    if args.status:
        tasks = [t for t in tasks if t.get("status") == args.status]
    if args.phase:
        tasks = [t for t in tasks if t.get("phase", "").upper() == args.phase.upper()]
    if args.horizon is not None:
        tasks = [t for t in tasks if t.get("horizon") == str(args.horizon)]
    for t in tasks:
        print(fmt_row(t, ["id", "task", "horizon", "phase", "status", "owner", "due"]))

# ---------------------------------------------------------------- gate / question / task ops

def cmd_gate(args):
    b = biz_dir(args.slug)
    gdir = b / "gates"
    gdir.mkdir(exist_ok=True)
    verdict = "PASS" if args.verdict_pass else ("CONDITIONAL" if args.verdict_conditional else "FAIL")
    rec = gdir / f"{args.phase}-record.md"
    if rec.exists() and not args.force:
        fail(f"{args.phase} gate already recorded; use --force to overwrite")
    prev = [p for p in GATE_ORDER if GATE_ORDER.index(p) < GATE_ORDER.index(args.phase)]
    for p in prev:
        if p == "P0":
            continue
        if p not in gates_passed(b) and p in ["P1", "P2", "P3", "P4", "P5"]:
            fail(f"gate {p} not passed yet — cannot record {args.phase}")
    rec.write_text(
        f"---\nbusiness: {args.slug}\ntype: gate\nupdated: {TODAY}\n---\n\n"
        f"# {args.phase} Gate Record\n\n"
        f"- verdict: {verdict}\n- date: {TODAY}\n- recorded by: {args.by}\n"
        f"- notes: {args.notes or '(none)'}\n"
        + ("- conditions: carried as tracked tasks — see registers/tasks.md\n" if verdict == "CONDITIONAL" else "")
        + ("- [U] user approval: " + (args.user_approval or "not recorded — REQUIRED for gates marked [U]") + "\n"
           if verdict in ("PASS", "CONDITIONAL") else "")
        + ("\nFAIL items to repair (then re-run gate):\n" + (args.notes or "") + "\n"
           if verdict == "FAIL" else ""), encoding="utf-8")
    if verdict in ("PASS", "CONDITIONAL"):
        update_front(b / "business-profile.md", "phase", next_phase(args.phase))
    print(f"gate {args.phase} recorded: {verdict}")

def next_phase(p):
    return {"P0": "P1", "P1": "P2", "P2": "P3", "P3": "P4", "P4": "P5", "P5": "P7", "P7": "P7"}[p]

def cmd_task(args):
    b = biz_dir(args.slug)
    tpath = b / "registers" / "tasks.md"
    if args.action == "add":
        tid = args.id or task_id_for_phase(b, args.phase)
        append_table_row(tpath, [tid, args.task, args.horizon, args.phase, "TODO",
                                  args.owner or "", args.due or "", args.done_when or ""])
        print(f"added {tid}")
        if args.due:
            print(f"remind: create calendar event [{args.slug.upper()}] {args.task} (due {args.due}; 1440-min reminder if legal/financial)")
    elif args.action == "status":
        header, data = parse_table(tpath)
        if "id" not in header:
            fail("tasks.md header missing 'id'")
        hit = False
        for row in data:
            if row[header.index("id")] == args.id:
                row[header.index("status")] = args.value
                hit = True
        if not hit:
            fail(f"task {args.id} not found")
        lines = []
        for line in read(tpath).splitlines():
            if line.strip().startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) == len(header) and cells[0] == args.id:
                    cells[header.index("status")] = args.value
                    line = "| " + " | ".join(cells) + " |"
            lines.append(line)
        tpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{args.id} → {args.value}")
        if args.value == "DONE":
            print("check: done-when evidence recorded? commit now ([slug] <id> what changed)")
    elif args.action == "drop":
        pass  # status DROPPED via action status
    update_front(tpath, "updated", TODAY)

def cmd_question(args):
    b = biz_dir(args.slug)
    qpath = b / "registers" / "questions.md"
    if args.action == "add":
        ids = [q.get("id", "") for q in reg(b, "questions")]
        qid = args.id or next_id(ids, "Q-")
        append_table_row(qpath, [qid, args.text, args.why or "", args.block or "", "OPEN", ""])
        print(f"added {qid}")
    else:
        header, data = parse_table(qpath)
        if "id" not in header:
            fail("questions.md header missing 'id'")
        lines = []
        for line in read(qpath).splitlines():
            if line.strip().startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) == len(header) and cells[0] == args.id:
                    cells[header.index("status")] = f"RESOLVED → ({args.answer})"
                    if "answer / ref" in header:
                        cells[header.index("answer / ref")] = args.answer
                    line = "| " + " | ".join(cells) + " |"
            lines.append(line)
        qpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{args.id} resolved → {args.answer}")

# ---------------------------------------------------------------- workorder

def cmd_workorder(args):
    b = biz_dir(args.slug)
    tasks = reg(b, "tasks")
    t = next((x for x in tasks if x.get("id") == args.id), None)
    if not t:
        fail(f"task {args.id} not found in registers/tasks.md")
    wdir = b / "scratch"
    wdir.mkdir(exist_ok=True)
    wonum = next_id([p.name for p in wdir.glob("WO-*.md")], "WO-")
    wo = wdir / f"{wonum}.md"
    wo.write_text(f"""---
business: {args.slug}
type: workorder
status: open
updated: {TODAY}
---

# {wonum} — {t.get('task', '')}

requested-by: orchestrator        # work may only be requested by the orchestrator
date: {TODAY}
budget: ~30 min / one focused pass
output: (register rows or doc section — state exactly)
links: registers/tasks.md (row {args.id})

## Context (what you must know to do this)
- (business-relevant facts from the rollup — IDs, not prose)
- (any source links or constraint the executor needs)

## Task
1. (concrete steps; one unit of work; only files named in output)

## Done when
- (checkable evidence — matches the task row's done-when)

## Rules
- Append-only on registers; never delete or renumber existing rows.
- No decisions: if you find a fork requiring judgment, stop and report it.
- Unsourced numbers are forbidden; label estimates `est.` with an A-nnn.
""", encoding="utf-8")
    print(f"work order drafted: {wo}")
    print("fill Context/Task/Done when from the rollup before handing to an executor")

# ---------------------------------------------------------------- validate

def cmd_validate(args):
    b = biz_dir(args.slug)
    problems = []
    req = ["business-profile.md", "metrics.md", "status.md",
           "docs/business-plan/00-master-plan.md", "docs/legal/10-incorporation.md",
           "docs/plan/40-tech-infrastructure.md", "docs/plan/50-execution-plan.md",
           "docs/future/00-pipeline.md"]
    for f in req:
        if not (b / f).exists():
            problems.append(f"missing required file: {f}")
    for n in ["tasks", "questions", "decisions", "business-facts", "assumptions", "risks", "compliance"]:
        if not (b / "registers" / f"{n}.md").exists():
            problems.append(f"missing register: registers/{n}.md")
    tasks = reg(b, "tasks")
    header, data = parse_table(b / "registers" / "tasks.md")
    if "id" not in header:
        problems.append("tasks.md: no parseable header")
    else:
        ids = [r[header.index("id")] for r in data]
        if len(ids) != len(set(ids)):
            problems.append("tasks.md: duplicate IDs")
        for r in data:
            row = dict(zip(header, r))
            if row.get("status") == "DONE" and not row.get("done when", "").strip():
                problems.append(f"{row.get('id')}: DONE without done-when evidence")
            if row.get("status") == "TODO" and row.get("due") and row.get("due") < TODAY and args.strict:
                problems.append(f"{row.get('id')}: overdue")
    qs = reg(b, "questions")
    qh, qd = parse_table(b / "registers" / "questions.md")
    cur_idx = 0
    g = gates_passed(b)
    for p in GATE_ORDER:
        if p in g:
            cur_idx = GATE_ORDER.index(p) + 1
    if qh and "block" in qh:
        for r in qd:
            row = dict(zip(qh, r))
            blk = row.get("block", "").strip()
            if row.get("status", "").startswith("OPEN") and blk in GATE_ORDER:
                if GATE_ORDER.index(blk) <= cur_idx:  # only a problem once that gate is at hand
                    problems.append(f"{row['id']}: OPEN and blocking gate {blk}")
    # front matter freshness on registers
    for p in (b / "registers").glob("*.md"):
        txt = read(p)
        if txt.startswith("---") and f"updated: {TODAY}" not in txt.split("---")[1] and args.strict:
            problems.append(f"{p.name}: updated stamp not today (stale?)")
    # gate chain sanity
    g = gates_passed(b)
    for p in GATE_ORDER[1:6]:
        if p in g:
            i = GATE_ORDER.index(p)
            prev = GATE_ORDER[i - 1]
            if prev == "P0" or prev in GATE_ORDER[1:6]:
                if prev not in g and prev != "P0":
                    problems.append(f"gate {p} recorded but {prev} missing")
    if problems:
        print("PROBLEMS FOUND:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"validate {args.slug}: OK — files present, registers parse, no rule violations")

# ---------------------------------------------------------------- rollup

def cmd_rollup(args):
    b = biz_dir(args.slug)
    prof = read(b / "business-profile.md")
    name = (re.search(r"^name: (.+)$", prof, re.M) or [None, args.slug])[1]
    region = (re.search(r"^region: (.+)$", prof, re.M) or [None, "-"])[1]
    btype = (re.search(r"^btype: (.+)$", prof, re.M) or [None, "-"])[1]
    oneliner = ""
    m = re.search(r"^\| One-liner \| (.+?) \|", prof, re.M)
    if m:
        oneliner = m.group(1)
    g = gates_passed(b)
    cur = "P0"
    for p in GATE_ORDER:
        if p in g:
            cur = next_phase(p)
    tasks = reg(b, "tasks")
    qs = reg(b, "questions")
    dec = reg(b, "decisions")
    risks = reg(b, "risks")
    comp = reg(b, "compliance")
    stats = {}
    for t in tasks:
        stats[t.get("status", "?")] = stats.get(t.get("status", "?"), 0) + 1
    open_q = [q for q in qs if q.get("status", "").startswith("OPEN")]
    blocking = [q for q in open_q if q.get("block", "")]
    overdue = [t for t in tasks if t.get("status") in ("TODO", "DOING") and t.get("due", "") and t["due"] < TODAY]
    doing = [t for t in tasks if t.get("status") == "DOING"]
    todo = [t for t in tasks if t.get("status") == "TODO"]
    top_risks = [r for r in risks if r.get("status") == "OPEN"][:3]
    last_dec = dec[-3:] if dec else []
    print(f"### {name} [{args.slug}] — phase {cur} | {btype} | {region}")
    if oneliner:
        print(f"{oneliner}")
    print(f"gates: {', '.join(sorted(g)) if g else 'none'} | tasks: "
          f"{stats.get('DONE',0)} done, {stats.get('TODO',0)} todo, {stats.get('DOING',0)} doing, "
          f"{stats.get('BLOCKED',0)} blocked | overdue: {len(overdue)}")
    if doing:
        print("doing: " + "; ".join(fmt_row(t, ['id', 'task']) for t in doing[:3]))
    if todo:
        due_sorted = sorted([t for t in todo if t.get("due")], key=lambda x: x["due"])
        undated = [t for t in todo if not t.get("due")]
        nxt = (due_sorted + undated)[:3]
        print("next: " + "; ".join(fmt_row(t, ['id', 'due', 'task']) for t in nxt))
    if blocking:
        print(f"blocking questions: " + "; ".join(fmt_row(q, ['id', 'question']) for q in blocking[:3]))
    if open_q and not blocking:
        print(f"open questions: {len(open_q)} (none blocking)")
    if overdue:
        print("overdue: " + "; ".join(fmt_row(t, ['id', 'due', 'task']) for t in overdue[:3]))
    if top_risks:
        print("top risks: " + "; ".join(fmt_row(r, ['id', 'risk']) for r in top_risks))
    if last_dec:
        print("recent decisions: " + "; ".join(fmt_row(d, ['id', 'decision']) for d in last_dec))
    due_comp = [c for c in comp if c.get("deadline") and c["deadline"] >= TODAY and c.get("status", "") in ("", "TODO", "DOING")]
    if due_comp:
        print("upcoming compliance: " + "; ".join(fmt_row(c, ['id', 'deadline', 'item']) for c in due_comp[:3]))

# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(prog="foundry.py", description="Business Foundry harness CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="create a new business repo from templates")
    p.add_argument("slug")
    p.add_argument("name")
    p.add_argument("--region")
    p.add_argument("--type")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("status", help="one-glance business state")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("next", help="current phase + next tasks")
    p.add_argument("slug")
    p.add_argument("-n", type=int, default=5)
    p.set_defaults(fn=cmd_next)

    p = sub.add_parser("tasks", help="list tasks (filters optional)")
    p.add_argument("slug")
    p.add_argument("--status")
    p.add_argument("--phase")
    p.add_argument("--horizon", type=str)
    p.set_defaults(fn=cmd_tasks)

    p = sub.add_parser("task", help="add a task or change its status")
    p.add_argument("slug")
    p.add_argument("action", choices=["add", "status"])
    p.add_argument("--id")
    p.add_argument("--phase", default="P5")
    p.add_argument("--task")
    p.add_argument("--horizon", default="1")
    p.add_argument("--owner")
    p.add_argument("--due")
    p.add_argument("--done-when")
    p.add_argument("--value", help="new status for action=status")
    p.set_defaults(fn=cmd_task)

    p = sub.add_parser("question", help="add or resolve a question")
    p.add_argument("slug")
    p.add_argument("action", choices=["add", "resolve"])
    p.add_argument("--id")
    p.add_argument("--text")
    p.add_argument("--why")
    p.add_argument("--block")
    p.add_argument("--answer")
    p.set_defaults(fn=cmd_question)

    p = sub.add_parser("gate", help="record a gate verdict")
    p.add_argument("slug")
    p.add_argument("phase", choices=GATE_ORDER)
    p.add_argument("--pass", dest="verdict_pass", action="store_true")
    p.add_argument("--conditional", dest="verdict_conditional", action="store_true")
    p.add_argument("--notes")
    p.add_argument("--by", default="orchestrator")
    p.add_argument("--user-approval", help="[U] gates: what the user approved and when")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_gate)

    p = sub.add_parser("workorder", help="draft a work order for a task (executor interface)")
    p.add_argument("slug")
    p.add_argument("id")
    p.set_defaults(fn=cmd_workorder)

    p = sub.add_parser("validate", help="automated repo health checks")
    p.add_argument("slug")
    p.add_argument("--strict", action="store_true", help="also flag overdue tasks + stale stamps")
    p.set_defaults(fn=cmd_validate)

    p = sub.add_parser("rollup", help="≤600-token session pack (paste into any new session)")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_rollup)

    args = ap.parse_args()
    args.fn(args)

if __name__ == "__main__":
    main()