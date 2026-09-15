# Changelog

All notable changes to FormaryBB core are documented here. Semantic versioning; breaking
changes to gate semantics, register schema, or the ID scheme bump the major version.
Harness upgrades are governed by `HARNESS-DECISIONS.md` (HD-nnn) — see
`harness/lib/business-type-playbooks.md` "Continuous improvement protocol".

## [Unreleased]

## [v1.0.0] — 2026-09-15 — "Operational core"

First tagged release. Complete phase-gated chain (P0–P7 + gates G0–G5 + quarterly), intake
floor with dispositions, pivot-first KILL discipline, flex modules, three-tier model system,
workspace isolation (FOUNDRY_WORKSPACE), 10 registers incl. roles + config, 16-type
business playbooks with depth routing, WI/IL/IN jurisdiction deep rows + on-demand expansion,
MIT license, HARNESS-DECISIONS upgrade register, stdlib-only CLI (init/status/next/tasks/
task/question/gate/workorder/validate/rollup/session) with tier flags.

### Audit fixes included in v1.0.0
- rollup: upcoming-compliance comparison was date-format-blind (items silently invisible) — normalized
- validate: [U] gates now mechanically require recorded user approval
- update_front: registers stamp written-format dates (was ISO)
- init/business data: workspace isolation via FOUNDRY_WORKSPACE; core .gitignore guards businesses/
- playbooks: `other` type depth-matrix row (all-core default)
- config: spend-threshold numeric check
- CLI: dead plan_docs dict removed; floor double-report collapsed to one message
- docs: PHASES slug example aligned to [LAKESIDE-ROASTERS]

Pre-release history (element walkthrough, commits e7eb20f…3d11019) is in git log.
