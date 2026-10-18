# What happens to an advertiser's seed file

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: concept
Category: audiences

An advertiser's seed file is read and matched inside the News Corp account, never copied to a business unit, never delivered, and dropped at teardown. You see this on Sidebar > **Audiences** > **From a seed**, where the seed's **Retention** reads **Dropped at teardown**.

## What a seed file is

A seed is "A list of people the advertiser already knows." It is sent so the portfolio can find how many of those people it can reach. On **From a seed**, the seed's card shows details such as **Arrived via** (the connector it came through), **Identifier**, **Region** and **Retention**.

## Where it is read

- The seed is read inside the News Corp account and matched against a licensed spine. "The layer builds no graph of its own."
- "The file is never written into a business unit’s system, and no unit receives a copy of it." No business unit, including Dow Jones and Realtor.com, gets a copy of the file.

## What the layer does with it

The **What the layer will do with it** table on **From a seed** sets the rules:

| Action | Result |
|---|---|
| **Match against …** (it names the business units) | **Deterministic** |
| **Report how many were found, before anything else** | **Always** |
| **Return any of the advertiser’s rows to a unit** | **Never** |
| **Tell the advertiser which unit a person came from** | **Never** |

Further rules apply as the seed moves through **Progress**:

- Unmatched seed rows are **Discarded, never stored**.
- No seed rows go to the modelling provider. On the extension step, **Seed rows sent to the provider** reads **None**, and the extension is **Trained on** **The matched group only**.

## What leaves

Only membership of the approved audience leaves. "The advertiser’s own file is not part of what leaves. Only membership of this audience does." The file is not part of the audience either, so it is never sent to a destination, and row-level data never leaves.

## Retention and teardown

**Retention** reads **Dropped at teardown**: the file is discarded at teardown and is not kept. If the advertiser wants the same seed run again, it starts from a new file. Nothing is kept to make it quicker.

To see the record kept after a seed audience is delivered, including when the seed was discarded, open the delivered audience under Sidebar > **Delivery**.

## Why it matters

These rules let you tell an advertiser exactly what happens to its file: no business unit gets its rows, the advertiser never learns which unit a person came from, and the file is gone after teardown.

Related: Build an audience from an advertiser seed file; Read seed match results; Check what left after a seed audience is delivered
