---
phase: P4
type: template
status: draft
updated: 2026-09-14
---

# Technology & Infrastructure Plan — <Name>

**Default stack preference:** internal team structure using **openwebui + openterminal
(shell agent) + langflow**, unless the user specified otherwise. Any deviation is a logged
`D-nnn` with the reason. See `harness/lib/toolstack-reference.md`.

## Needs inventory

| Business function | Software needed | Covered by default stack? | Decision |
|---|---|---|---|
| e.g., invoicing | billing tool | partial — langflow flow + spreadsheet | D-nnn |

## Toolstack decisions »

| Category | Tool/platform | Cost (monthly) | Hosting | Why (ID) | Owner |
|---|---|---|---|---|---|
| Model routing / personas / knowledge | openwebui | | internal | default preference | |
| File ops / git / CLI agent | openterminal or shell agent | | internal | default preference | |
| Flow automation | langflow | | internal | default preference | |
| Website | | | | | |
| Payments | | | | | |
| Email / outreach | | | | | |
| Bookkeeping | | | | | |
| Scheduling / ops | | | | | |

## AI enablement plan »

Which functions get agent assist first (content drafts, outreach personalization, support
macros, bookkeeping reconciliation, market scanning). The **first automation**: one concrete
langflow flow, ≤1 week to build, becomes a P5 task. Persona/knowledge setup tasks for openwebui.

## DevOps & environment

Hosting philosophy (self-hosted vs SaaS per decision), dev/prod separation, deployment
steps, backups (what, where, how often, tested when), monitoring (what gets checked, by whom).

## Security baseline (no exceptions)

- Password manager for all business credentials; MFA on every account
- Separate business email; off-repo secrets (`.env` / vault — never committed)
- Device hygiene standard; access revocation procedure
- Compliance-specific needs only if the type demands (PCI, HIPAA, state rules — see playbooks)

## Procurement tasks »

Accounts to create, domains to buy, hardware, subscriptions — each becomes `T-P4-nnn` with
owner and due date. Spend above the profile threshold is **[U]**.

## Run-rate summary

Total monthly/yearly tech cost → flows into `20-financial-plan.md` (amendment if post-G3).