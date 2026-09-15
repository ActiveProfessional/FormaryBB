---
type: register
updated: 09-15-2026
---

# Harness Decisions — FormaryBB upgrade register

This is the **harness's own** decision register (harness-scoped `D-nnn` sequence — separate
from any business's register). It records every accepted change to core machinery: playbooks,
conventions, gates, templates, the CLI. See `harness/lib/business-type-playbooks.md`
"Continuous improvement protocol".

| ID | Decision | Rationale | Evidence (business/gate) | Date | Status |
|----|----------|-----------|--------------------------|------|--------|
| HD-001 | Three-tier model system (T1/T2/T3) with tier-qualified guardrails | User: guardrails must not cap frontier synthesis while keeping local executors safe | walkthrough E4 | 09-15-2026 | active |
| HD-002 | Quarterly variance threshold 25%→10% | User: tighter drift detection | walkthrough E3 | 09-15-2026 | active |
| HD-003 | Jurisdictions: WI/IL/IN deep rows; other states on-demand | User: WI, IL, IN are the operational trio | walkthrough E8 | 09-15-2026 | active |
| HD-004 | Playbook improvement protocol (models propose, user approves, HARNESS-DECISIONS logs) | User: continuous improvement tracked formally | walkthrough E8 | 09-15-2026 | active |

**Rules:** harness changes are [U]-activated only; HD-nnn never reused; every accepted
proposal updates `lib/`, `harness/`, or `bin/` in the next commit and cites its HD-nnn here.
