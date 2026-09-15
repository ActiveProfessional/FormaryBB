# Workspaces — keeping user data out of the core

**The three-layer model:** CORE (this repo — machinery only) / WORKSPACE (a user's own git
repo with their `businesses/` data) / OVERLAY (per-workspace customization). Core tenants
stay intact; user data and dry runs live in workspaces; nothing a user does can write into
core history.

## How to use a workspace

```bash
# 1. Create your workspace (anywhere; its own git repo — recommend cloning as its own private repo)
mkdir ~/my-foundry-workspace && cd ~/my-foundry-workspace
git init

# 2. Point the CLI at it (env var or per-command)
export FOUNDRY_WORKSPACE=~/my-foundry-workspace

# 3. Run everything as normal — data lands in the workspace, never in core
python3 /path/to/FormaryBB/bin/foundry.py init my-biz "My Business" --region US-WI --type local-service
```

- Every command accepts a business path directly too, so a workspace needs no env var if
  you pass full paths: `foundry.py status ~/my-foundry-workspace/businesses/my-biz`.
- The core repo's `.gitignore` excludes `businesses/` as belt-and-suspenders: even if the
  env var is forgotten, core can't commit user data.
- Pin your workspace to a core version: record the tag in your workspace README
  (e.g. `core: v1.0.0`) and check `CHANGELOG.md` before upgrading.

## Workspace layout

```
my-workspace/
├── README.md          # notes, pinned core version
├── businesses/        # init writes here (each business its own subdirectory + git history)
└── overlay/           # optional: per-workspace customization (see below)
```

## Overlay rules (additive-only)

A workspace may carry an `overlay/` directory that mirrors core structure:
`overlay/lib/jurisdictions-oh.md` (new state rows), `overlay/templates/…` (extra templates),
`overlay/playbooks/…` (new business types). Core reads first, overlay second. Overlays may:

- **add** new files, new business types, new jurisdiction rows, new template variants
- **extend** playbooks with additional per-type notes

Overlays may **never**: redefine or remove core phases, gates, registers, the ID scheme,
conventions, or templates; contradict core tenets. `validate` rejects any overlay that
renames/deletes core content (additive-only enforcement).

Genuinely valuable overlays should be proposed upstream (HD-nnn protocol,
`HARNESS-DECISIONS.md`) — good ones become core so every future business benefits.

## Why this protects commercialization

- Core stays clean of user data (workspace isolation + .gitignore) — the product is never
  contaminated by a specific business's history, even yours.
- Users clone/branch the core under MIT; their workspaces are theirs; core tenants hold.
- A hosted/app future is thin: pin a core release, mount N workspaces, run the same CLI
  per user. No database, no rewrite — directory-level + git-level isolation.