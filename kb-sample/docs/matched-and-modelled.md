# Matched and modelled audiences

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: concept
Category: concepts

Matched people are real people the portfolio found by exact matching; modelled people are an optional extension of people who only resemble them. The console always shows them apart, on Audiences, Analysis and Delivery, and never adds them together.

## Matched

Matched people are found by deterministic matching on the identity spine, which means an exact match on an identifier rather than a model or an estimate. They are consented and deduplicated, so a person found in more than one business unit is counted once. A seed audience's matched card describes them as "Real people the portfolio can reach today."

## Modelled

Modelled people "resemble the matched group, found by the licensed provider’s model. They are not the advertiser’s customers". This is the modelled extension, an optional lookalike step. On a seed audience, no extension is offered until the matched figure has been reported; you then open it with **Look at extension**. The model is the provider's own, trained on the matched group only, and no seed rows are sent to the provider.

When no modelling provider is under contract, the extension shows **Provider not contracted**: "Extension cannot run until an identity and modelling provider is signed. Sizes below are shown as placeholders, not estimates."

## The rule: never added together

- Matched and modelled sit in separate columns or tiles. Matched is a solid tile; modelled is a dashed, striped tile with a plus sign.
- The matched figure is always stated first: "Matched size is stated before any extension, wherever the audience goes."
- They are delivered as separately labelled audiences. "No screen anywhere shows a single combined total."

## Labels you will meet

| Label | Where | Meaning |
|---|---|---|
| **Matched · deterministic** | Size cards on Audiences, **Live sizing**, seed results | The matched audience. |
| **Modelled · separate audience** | Size cards on Audiences and Create an audience | The modelled extension, kept as its own audience. |
| **Modelled · separate** | Column in **Largest definitions** on Overview | Each definition's modelled extension, never added in. |
| **Modelled · provider’s method** | The extension step of a seed audience | People who "Resemble the matched group. Not customers." |
| **Modelled · not yet offered** | The matched step of a seed audience | No extension has been offered. Extension is a separate step, reported as its own number. |
| **Modelled · provider not contracted** | Seed audience results | No final modelled figure, because the provider is not under contract. |
| **With extension · not contracted** | **If you build an audience** on an analysis run | The extension, shown apart from **Matched only**. |
| A dash (—) in a modelled column | Audiences, Overview | There is no modelled extension. |
| **Matched** in the **Label** column | **In flight and recent** on Delivery | The delivered audience is the matched audience. |

## Why it matters

On a seed audience, matched people are "Known to both the advertiser and the portfolio", while modelled people "Resemble the matched group. Not customers." Keeping the figures apart means each claim stays accurate, and a modelled extension always travels as its own labelled audience.

Related: Extend a matched audience; The identity spine; Read seed match results
