# The identity spine

Applies to tier: Power User
Business unit: all
Console page: /
Article type: concept
Category: concepts

The identity spine (often just "the spine") is the licensed identity layer the console uses to match people and to deduplicate them across business units. You see it named next to matched figures and overlaps on Overview, Audiences and Analysis.

## What the spine is

Matching runs against a licensed spine, not one the layer builds. A seed audience states: "Matching runs inside the News Corp account against a licensed spine. The layer builds no graph of its own."

Matching on the spine is deterministic: an exact match on an identifier, not a model or an estimate. You see this in labels such as **Deterministic, on the licensed spine** and, under **Matched** on an analysis run, "deterministic on the spine".

## How people are counted once

- A person found in more than one business unit is counted once. A seed audience's match table shows this as the row **Both · counted once**.
- Matched figures on Audiences and Overview are consented people "deduplicated on the spine".
- On an analysis run's **Composition**, a **Source** of **Resolved on the spine** means one person with attributes from more than one business unit.
- For a portfolio question, each business unit evaluates the question on its own data, in its own environment. The combined figure is then resolved over each unit's results to remove double counting, never over raw records. No records are moved between units.

## When the portfolio figure is pending

These labels mean the deduplicated portfolio figure is not available, so a placeholder shows instead of a value:

- **Pending spine** under **Portfolio reachable · matched** on Overview.
- **Pending identity spine** on the portfolio card of a portfolio question result.
- **Portfolio figure pending spine** as a chip on a portfolio question's finding.

On a portfolio question result, the cards for each business unit still show their own figures. Only the combined, deduplicated figure is pending.

## Overlaps marked Not verified

**Not verified** means an overlap has not been verified against the spine. "No overlap percentage is shown until the analysis is verified against the spine." You see it in the **Overlap** column on Analysis > **Portfolio** and in the overlap row of a portfolio question result.

## Figures from a provider that is not under contract

In an audience's detail panel on Audiences, the caption next to **Why this size?** ends **from the spine provider · not contracted**. It marks figures that depend on a provider that is not under contract.

## Why it matters

The spine is what lets the console report one deduplicated figure across business units without moving records between them. When a figure or overlap depends on it and is not available, the console shows a pending or **Not verified** marker instead of a number.

Related: Matched and modelled audiences; Use the Portfolio tab; Read a portfolio question result
