# Business-type playbooks — routing depth where it belongs

**Purpose:** "not all businesses are created equal." The profile records a business type;
this file says where each phase/section goes deep (**»**), where it stubs (**~**), what the
legal/stack/KPI load typically is, and how the chain compresses. Pick the closest type at
P0; refine at P1. When in doubt, treat as the simpler type and let evidence upgrade it.

## The types

| Type | Examples |
|---|---|
| local-service | plumber, salon, lawn care, cleaning, tutor |
| retail | grocery, boutique, ecom with physical goods |
| digital-product | SaaS, apps, digital content/templates |
| agency-consulting | marketing agency, bookkeeping, fractional exec |
| content-media | newsletter, podcast, creator business |
| ecommerce | drop-ship, DTC brand, marketplace seller |
| hospitality | cafe, restaurant, food truck, B&B |
| skilled-trade | electrician, contractor (licensed trades) |
| health-wellness | gym, coaching, therapy (touch regulated zones) |
| b2b-services | B2B services, outsourced functions |
| fintech-finance | anything touching money of others |
| education | courses, academies, child care (child-facing = regulated) |
| tech-platform | marketplaces, platforms, dev tools |
| nonprofit-civic | nonprofits, community orgs |
| holding-entity | shell, IP holding, real-estate holding |
| other | everything else — define the type in the profile |

## Depth routing matrix

Plan sections: G&M = goals/mission, Inc = incorporation, Mkt = market research, Fin = financial
plan, Ops = operations, GTM = marketing, Brand, Tech = tech plan, Exec = execution plan.

| Type | G&M | Inc | Mkt | Fin | Ops | GTM | Brand | Tech | Exec |
|---|---|---|---|---|---|---|---|---|---|
| local-service | » | » | » | core | core | » | core | core | core |
| retail | core | core | » | » | » | core | core | core | core |
| digital-product | core | core | » | » | core | core | core | » | core |
| agency-consulting | core | core | core | » | core | » | core | core | core |
| content-media | core | ~ | » | core | core | » | » | core | core |
| ecommerce | core | core | » | » | » | » | core | » | core |
| hospitality | core | » | » | » | » | » | core | core | core |
| skilled-trade | core | » | core | core | » | core | core | ~ | core |
| health-wellness | core | » | » | core | » | core | core | » | core |
| b2b-services | core | core | » | core | core | » | core | core | core |
| fintech-finance | » | » | » | » | » | core | core | » | » |
| education | core | » | » | core | » | core | core | core | core |
| tech-platform | core | » | » | » | » | core | core | » | » |
| nonprofit-civic | » | » | » | core | core | core | core | core | core |
| holding-entity | core | » | ~ | ~ | ~ | ~ | ~ | ~ | core |

**~** = stub with pointer + `D-nnn` (why deferred); **»** = deep treatment required;
core = standard template treatment.

## Per-type notes

### local-service
- **Legal load:** city business license, state trade registration if regulated, liability
  insurance (non-negotiable), vehicle/commercial considerations. Simple formation, often
  solo LLC or sole prop until revenue justifies.
- **KPIs:** booked jobs/wk, quote→close rate, repeat %, reviews velocity, cost/job.
- **Compress:** P2 in days, P3 lean (6-page plan passes), P4 light (website + GBP +
  booking + invoicing + openwebui/langflow for follow-ups).
- **GTM is local:** reviews, GBP, referral incentives, community presence, vehicle signage.

### retail
- **Legal:** sales tax registration + monthly remittance, signage/zoning permits, weights
  & measures, health dept if food-adjacent.
- **KPIs:** basket size, traffic→conversion, inventory turns, shrink, margin by category.
- **Ops is the moat:** supplier terms, stock discipline, shrink, staffing schedules.
- **Stack:** POS with tax handling; inventory tool; the default AI stack for content/reordering.

### digital-product
- **Legal:** entity light; ToS/privacy policy **»** (template then counsel review); payments;
  sales tax nexus rules if US.
- **KPIs:** activation rate, retention curve, churn, MRR/ARR, support load.
- **Vetting:** landing-page test, waitlist, concierge MVP before building (build last).

### agency-consulting
- **Legal:** light formation; contracts and SOW templates **»**; professional liability (E&O).
- **KPIs:** utilization, pipeline coverage, retention rate, effective hourly rate.
- **GTM:** founder network first; case studies compound; referral loop is the growth engine.

### content-media
- **Legal:** ~ (entity when money arrives); IP ownership + fair-use hygiene if derivative.
- **KPIs:** subs, open rate, CPM/sponsor revenue, engagement, churn of paid subs.
- **Money:** sponsorship, paid subs, product tie-ins; direct-to-paid niche beats scale.

### ecommerce
- **Legal:** sales tax nexus (multi-state rules), product safety/compliance, returns policy.
- **KPIs:** CAC, LTV, margin after shipping/returns, inventory cash cycle.
- **Ops:** fulfillment, returns handling, supplier risk. **Kill-tests:** ad math before inventory buys.

### hospitality
- **Legal:** health permits, food handler certs, liquor license (if), fire/occupancy,
  sign permits. **» professional verification mandatory.**
- **KPIs:** covers/day, ticket avg, food cost %, labor %, prime cost target.
- **Ops:** menus, prep lists, staffing, health inspections readiness. **AI stack:** staff
  scheduling, prep forecasting, review responses, social clips.

### skilled-trade
- **Legal:** state license (verify exact scope **»**), bonding, insurance, permits per job.
- **KPIs:** jobs/wk, margin/job, callback rate, quote turnaround time.
- **Compress:** lean plan; reputation + license = the moat. P4 ~ (phone, truck, invoicing).

### health-wellness
- **Legal:** scope-of-practice (what you may legally say/do **»**), certifications, liability
  waiver, client privacy; professional board rules if licensed.
- **KPIs:** client retention, package renewals, no-show %, referral rate.
- **Sensitive:** medical claims discipline — marketing must stay inside scope.

### b2b-services
- **Legal:** entity light; MSA/SOW templates, data-handling agreements if client data touched.
- **KPIs:** pipeline value, win rate, NRR, delivery margin.

### fintech-finance
- **Everything is »**: licensing (money transmission, lending, advice), KYC/AML, SEC/FINRA/
  state regulators, data security. **No DIY legal here — counsel from P1 onward.**
- **KPIs:** regulatory filing status, unit risk, fraud loss %, runway with legal burn.
- **Compress:** nothing. P2–P5 stretch. Budget 2–3× legal/consulting line items.

### education
- **Legal:** child care licensing if minors **»**, background checks, zoning for in-person,
  accreditation only if claimed.
- **KPIs:** enrollment, completion, outcome testimonials, referral rate.

### tech-platform
- **Legal:** ToS/privacy **»**, Section 230/UGC considerations, gig/labor classification if
  two-sided workforce, data residency.
- **KPIs:** GMV or engagement, both-side liquidity, take rate, churn.
- **Vetting:** two-sided cold-start is the kill-test; solve the harder side first.

### nonprofit-civic
- **G&M »** (mission and theory of change are the product), 501(c)(3) or local equivalent
  filing, state charity registration, board governance, grant reporting.
- **KPIs:** beneficiaries served, cost/beneficiary, grant pipeline, donor retention.
- **AI stack:** grant-letter drafting, donor comms, impact reporting.

### holding-entity
- Thin everything, » incorporation + tax treatment only. Execution plan = the operating
  calendar of a few filings. Exists to serve another business — treat as a P2-only exercise.

## Using the playbooks

1. At P0, pick the closest type → paste its depth row into the profile.
2. At P1, refine: if the business is a blend (e.g., retail + local service), take the union
   of » requirements and the intersection of ~ allowances.
3. If evidence in P1 suggests a different type, record the change as a `D-nnn`.
4. Regulated zone (fintech, health, education-minors, licensed trades): add professional
   verification tasks **before** P2 ends — no exceptions, regardless of compression elsewhere.