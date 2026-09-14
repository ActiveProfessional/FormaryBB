# Toolstack reference — the default preference and its rationale

**Default preference** (unless the user specifies otherwise): an **internal team structure**
using **openwebui + openterminal (or a shell agent) + langflow**, with this harness's business
repo as the data layer. The philosophy: own the core, rent the commodity, automate the repeat.

## The default stack

| Layer | Tool | Role in the business | Notes |
|---|---|---|---|
| Model routing / personas / knowledge | **openwebui** | One front door to frontier + local models; personas for business functions (copywriter, analyst, support macro writer); knowledge bases loaded per business | Route frontier for judgment, local for volume — matches this harness's orchestrator/executor split |
| Execution agent | **openterminal** (or any shell agent) | File ops, git, running `foundry.py`, register edits per work orders, deployments | This is the executor tier's hands |
| Flow automation | **langflow** | Repeatable flows: outreach sequences, report generation, social drafting, data syncs, alerts | Build the first automation ≤1 week; prefer flows the internal team can maintain |
| Data layer | **this repo** (markdown + git) | Source of truth for every business | Portable, diff-able, model-legible; registers are the API |

## Commodity categories (rent, don't build)

| Category | Default guidance |
|---|---|
| Payments | Stripe / Square / PayPal — take the boring option with the best fees for the volume |
| Email (transactional) | The provider your platform integrates natively |
| Bookkeeping | Wave/QuickBooks/Xero by region + accountant's preference — ask the accountant at P2 |
| Domain/DNS | Any reputable registrar; DNS with the host |
| Website | Local service: GBP + simple site builder or static site; product: platform per plan |

## Decision rules (when to deviate from defaults)

1. **Compliance forces it** — regulated data (health, financial) may require specific hosting
   or BAA/certified vendors → log the deviation as a `D-nnn` with the compliance row it serves.
2. **Scale forces it** — a flow outgrows langflow's comfort → replace that flow only, keep the rest.
3. **The team can't run it** — self-hosting needs someone on-call; if nobody is, buy the SaaS.
4. **The user specifies it** — preference recorded, honored, logged.

Any deviation: logged decision with the reason. The default exists so deviations are *choices*.

## Security baseline (applies to every stack)

Password manager for all business credentials; MFA on every account; separate business email;
secrets in `.env`/vault, never committed; backups tested; offboarding/revocation procedure
written at P4. See the tech template.

## Cost discipline

- Total run-rate (hosting + subscriptions + model API where used) flows into the financial plan.
- Review tool costs at the quarterly gate; kill anything unused two quarters running.
- The internal stack's compute (local models) is cheap for volume work — use frontier APIs
  only where judgment demands it; the orchestrator/executor split keeps this natural.