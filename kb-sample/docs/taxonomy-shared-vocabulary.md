# Taxonomy: the shared vocabulary

Applies to tier: Power User
Business unit: all
Console page: /taxonomy
Article type: concept
Category: taxonomy

The taxonomy is the console's shared vocabulary: one list of canonical terms that every business unit maps its own data to, so audiences and questions use the same words across units. Open it from Sidebar > **Taxonomy**. The page subtitle reads "The shared vocabulary. Canonical terms sit above each unit’s own taxonomy and never overwrite it."

## What a canonical term is

A canonical term is a shared term in that vocabulary. On the Taxonomy page, the left panel lists them under the header **Canonical · IAB Audience …**, which shows the list follows the IAB Audience taxonomy. Terms are grouped into **Demographics**, **Interest**, **Intent** and **Behaviour**, and each category header shows how many terms it holds. Click a term to open its definition, **Steward**, business unit mappings and version history on the right.

## Where to see your own local taxonomy

Each business unit keeps its own taxonomy. Lower in the left panel, under **Local · read only**, the page lists each unit's local taxonomy by source system, with how many terms each holds. The note **Counts as of last sync** gives the time, in UTC, when those counts were taken. Local taxonomies are read only here, and the shared vocabulary never overwrites or modifies them.

## How business units connect to it

Each business unit transforms its own fields into the canonical form of a term. You see this for each term under **How each business unit maps to it**. A unit with nothing that matches is marked **No equivalent**. It is never approximated with a stand-in.

## Where you use shared terms

- **Audiences**: on **Create an audience**, the start option **A blank definition** reads "Write a rule from the shared vocabulary". A suggested rule marked **AI suggestion** can note under **Why this?** that it uses only canonical fields.
- **Analysis**: on the **Portfolio** tab, click **Resolve terms** and **How your words resolved** shows each of your words, the **Shared term** it resolves to and the local field each unit will evaluate. A word with no shared term is marked **Dropped, not approximated**.
- **Ask AI**: answers that rely on the vocabulary say **From the shared vocabulary as of …** and list **Taxonomy · canonical terms** under **Based on:**. That link opens the Taxonomy page.

## Why it matters

Shared terms let one audience definition or portfolio question be evaluated against each contributing unit's own data, in place, while every unit keeps its own naming.

Agency users don't see the Taxonomy page and cannot change the taxonomy. They see category names only as filter tabs on **Portfolio audiences**.

Related: Find a term and read its details; Check and edit how business units map to a term; Taxonomy FAQ
