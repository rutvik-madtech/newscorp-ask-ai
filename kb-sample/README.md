# Ask AI sample knowledge base

**Sample help articles for testing Ask AI.** They are written from the News Corp Data Dexterity Layer console design (Mockups v3), the way a support centre is written: where things are, how to do them in the UI, what terms and statuses mean, who can do what, FAQs and troubleshooting. They contain no numbers, statistics or sample data, and quote UI labels exactly as the design shows them. When the design changes, the articles need checking against it.

## What's here

```
kb-sample/
  docs/                    upload the contents of this folder to S3, nothing else
    <article>.md           94 help articles, one topic each
    <article>.md.metadata.json  the article's filter tags, read by Bedrock at ingestion
  make_sidecars.py         rebuilds the .metadata.json files from the articles
  lambda/                  the Ask AI Lambda (Claude + search_product_docs)
  demo/                    a Streamlit page for demoing the Lambda to the team
  README.md                this file (don't upload it)
```

## How articles are tagged

Each article starts with its title and five lines:

```
# Approve a request

Applies to tier: Power User
Business unit: all
Console page: /rules-of-use
Article type: how_to
Category: rules_of_use
```

`make_sidecars.py` turns them into the sidecar Bedrock ingests, the same job the publish job does in the plan (§2.1):

```json
{
  "metadataAttributes": {
    "title": "Approve a request",
    "doc_type": "how_to",
    "pillar": "rules_of_use",
    "allowed_tiers": ["Power User"],
    "tier_power_user": true,
    "tier_agency": false,
    "business_unit": "all",
    "console_link": "/rules-of-use",
    "source_updated_at": "2026-10-18"
  }
}
```

- **Roles.** The design has two roles: **Power User** (internal, works as one business unit) and **Agency** (external, finds, sizes and requests portfolio audiences). Admin is a sidebar section for Power Users, not a role. `allowed_tiers` uses the role names exactly as the portal sends them.
- **`tier_power_user`, `tier_agency`** carry the same information as one flag per role, filtered with `equals`. The Lambda uses these by default (`TIER_FILTER` = `flags`). In the test account, S3 Vectors also applied `listContains` on `allowed_tiers` correctly, so `list` works there too.
- **An article with no tier line gets Power User only**, so a missing tag never shows an article to Agency users.
- **Business unit.** Every article is `all`: the help is the same for each business unit. The tag stays so business-unit-specific articles can be added later. Their names must match what the portal backend sends from `GET /business-units`.
- **Article types:** `getting_started`, `how_to`, `concept`, `reference`, `faq`, `troubleshooting`.

After editing an article, run `python3 make_sidecars.py` and upload both files again.

## Coverage

| Category | Articles | Visible to |
|---|---|---|
| Sign in and access | 5 | Both roles |
| Getting started | 4 | One per role, plus roles and the general FAQ for both |
| Ask AI and AI suggestions | 5 | Ask AI articles for both roles; AI suggestions for Power Users |
| Portfolio audiences | 6 | Agency only |
| Overview and navigation | 6 | Power User |
| Key concepts and glossary | 7 | Power User |
| Taxonomy | 5 | Power User |
| Audiences | 16 | Power User |
| Analysis | 14 | Power User |
| Rules of Use | 9 | Power User |
| Delivery | 10 | Power User |
| Admin: access and connectors | 7 | Power User |

In all: 76 articles for Power Users only, 7 for Agency only, 11 for both.

## Test cases

A search always returns up to 8 passages the role may see, so a question about another role's feature still gets an answer from what is visible. The real check is the last column: those articles must never come back for that role.

| Question | Role | Expected answer | Must never come back |
|---|---|---|---|
| How do I approve a request? | Power User | Steps from Approve a request | |
| How do I approve a request? | Agency | Only Power Users approve; how approval of the agency's own request works | Approve a request, Rules of Use FAQ |
| How do I request a portfolio audience? | Agency | Steps from Request a portfolio audience | |
| How do I request a portfolio audience? | Power User | That is the agency flow; create an audience instead | Request a portfolio audience |
| I forgot my password | Either | Steps from Reset your password | |
| What does Suppressed mean? | Power User | From Minimum population and suppressed figures | |
| Where do I see why a delivery failed? | Power User | From Fix a failed delivery | |
| Where do I see why a delivery failed? | Agency | Delivery isn't part of the Agency role | Fix a failed delivery |
| How do I give someone access to the console? | Power User | From Invite a person or disable access | |
| How do I give someone access to the console? | Agency | From Request access to the console | Invite a person or disable access |
| A connector shows Stale. What do I do? | Power User | From Data may be out of date: a feed is Stale | |
| How do I switch the business unit I'm working in? | Power User | From Switch the business unit you're acting as | |
| How many people are in my audience? | Either | Declined: Ask AI can't see live figures; where the size is shown | |
| Write me a poem about data | Either | Declined as off-topic, without a search | |

All of these passed against the live Knowledge Base on 2026-10-18, with no article shown to the wrong role.
