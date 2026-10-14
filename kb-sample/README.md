# Ask AI sample knowledge base

**Sample content for testing Ask AI. This is not real CDL product documentation.** The pages mirror the screens, roles and terms in the CDL portal code (`cdl_ui`, branch `hetvi-ui-setup`), so retrieval, citations and tier filtering can be tested before the real docs are written. Figures and rules in the pages (such as the 1,000-person minimum population) are made up.

## What's here

```
kb-sample/
  docs/                    upload the contents of this folder to S3, nothing else
    <page>.md              23 product-doc pages, one topic each
    <page>.md.metadata.json  the page's filter tags, read by Bedrock at ingestion
  make_sidecars.py         rebuilds the .metadata.json files from the pages
  README.md                this file (don't upload it)
```

## How pages are tagged

Each page starts with three lines, as the plan's doc template asks (§2):

```
Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /audiences
```

`make_sidecars.py` turns them into the sidecar Bedrock ingests, the same job the publish job does in the plan (§2.1):

```json
{
  "metadataAttributes": {
    "title": "Build an audience",
    "doc_type": "how_to",
    "pillar": "audiences",
    "allowed_tiers": ["Power User", "Admin", "Agency"],
    "tier_power_user": true,
    "tier_admin": true,
    "tier_agency": true,
    "business_unit": "all",
    "console_link": "/audiences",
    "source_updated_at": "2026-10-01"
  }
}
```

- **`allowed_tiers`** uses the portal's role names exactly as `/api/auth/me` returns them, so the Lambda can pass the role straight into the filter.
- **`tier_power_user`, `tier_admin`, `tier_agency`** carry the same information as one flag per role. Use them with an `equals` filter if the vector store can't filter on a list (plan §5.3).
- **A page with no tier line gets Power User and Admin only.** `release-notes.md` has none, on purpose, to test that a missing tag fails safe.

After editing a page, run `python3 make_sidecars.py` and upload both files again.

## Coverage

| Who can see it | Pages |
|---|---|
| All roles (15) | getting-started, glossary, roles-and-access, overview-page, taxonomy, build-an-audience, audience-gates, matched-vs-modelled, analysis-runs, delivery-destinations, permissible-use-envelope, delivery-troubleshooting, faq, bu-dow-jones (Dow Jones only), bu-realtor (Realtor.com only) |
| Power User and Admin (6) | rules-of-use-approvals, gating-rules, agent-endpoint, consent-ledger, audit-trail, release-notes (no tier line) |
| Admin only (2) | admin-access-roles, admin-connectors |

## Test cases this set is built for

| Question | Role | Business unit | Expected |
|---|---|---|---|
| How do I build a Cross-BU audience? | Agency | Dow Jones | Answer from build-an-audience, including that Cross-BU audiences are built by Power Users and Admins |
| How do I approve a request from Realtor.com? | Power User | Dow Jones | Answer from rules-of-use-approvals |
| How do I approve a request from Realtor.com? | Agency | Dow Jones | No internal page retrieved. Ask AI says this isn't available for the Agency role |
| What signals does Realtor.com contribute? | Agency | Realtor.com | Answer from bu-realtor |
| What signals does Realtor.com contribute? | Agency | Dow Jones | bu-realtor filtered out by business unit. Ask AI says it found nothing for this business unit |
| How do I add a user? | Power User | Dow Jones | admin-access-roles filtered out (Admin only) |
| How do I add a user? | Admin | Dow Jones | Answer from admin-access-roles |
| What changed in the September release? | Agency | Dow Jones | release-notes filtered out (default tags) |
| My Permutive delivery failed. What do I do? | Any | Any | Answer from delivery-troubleshooting |
| What does an index of 2.3 mean? | Any | Any | Answer from analysis-runs or glossary |
| How many people are in my C-suite audience? | Any | Any | Declined: live numbers aren't available in Ask AI |
| Write me a poem about data | Any | Any | Declined as off-topic, without a search |
