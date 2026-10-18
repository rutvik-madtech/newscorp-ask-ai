# Read a portfolio question finding

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: how_to
Category: analysis

A finding is the answer to a portfolio question, stated in plain language. To read it, click **See the finding** on the result screen (Sidebar > **Analysis** > **Portfolio** > your question > **Run the question**). **The finding** opens, with the breadcrumb **Portfolio › Question … › Finding**. It states the answer, breaks it down and shows where each figure came from.

## Steps

1. On **Evaluated at each unit, then resolved**, click **See the finding**.
2. Read the headline sentence at the top and the chips under it:
   - **Deterministic only · no modelled extension applied**: only matched people are counted.
   - **Eligible population**: the figure counts eligible people only.
   - **Portfolio figure pending spine**: shows while the identity spine is pending. The deduplicated portfolio figure depends on the spine.
3. Read the breakdown table. It sets the counts for one shared term from your question against another, and is labelled **Counts of eligible people · as of …**.
4. Read **Where each figure came from** (see below).
5. Read **What this finding is not**, then click **What happens next** to save the question, turn it into an audience or export the counts.

To go back to the result, click **Question …** in the breadcrumb.

## Suppressed cells

A cell with a lock icon and **Suppressed** shows no value. "A suppressed cell falls below the minimum population. It is shown as suppressed rather than hidden or rounded away." Any group below the minimum population is suppressed in the same way, with no value.

## Where each figure came from

Each line names the terms, the business unit that supplied them and that unit's as-of time. The last line, **Deduplication · identity spine**, shows the current state of the identity spine.

## Good to know

- A finding is not an audience: "It is a count, not an audience. Nothing has been created, named or sent. Turning it into something buyable starts a separate path, and that path asks each unit for approval."
- Matched and modelled figures are never added together.
- Reading a finding needs no approval, because nothing leaves the console.

Related: Read a portfolio question result; Save, turn into an audience or export a portfolio question; Minimum population and suppressed figures
