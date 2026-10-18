# Minimum population and suppressed figures

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: concept
Category: concepts

The minimum population is the smallest group size the console reports on or lets you use. Any group below it shows **Suppressed** with a lock icon and no value, whether you are reading an analysis run or a portfolio answer. On an audience, minimum population shows as a gate.

## What suppressed means

When a segment, row or cell falls below the minimum population, the figure is replaced by **Suppressed** with a lock icon. No value is shown at all. A portfolio question finding puts it this way: "A suppressed cell falls below the minimum population. It is shown as suppressed rather than hidden or rounded away."

Results are aggregate only. A run's Composition note reads "Aggregate only, gated by minimum population. No identifiers are returned."

## Where you see Suppressed

- **Composition** rows on an analysis run (Analysis > Runs > a run): **Of matched** and **Index** both read **Suppressed**.
- **What the portfolio can reach** on Analysis > **Portfolio**: "Suppressed rows show no value at all: they fall below the minimum population."
- Breakdown cells in a portfolio question's finding (**The finding**).

## Where you see it as a check

- The gate **Minimum population** with **Passed**, in an audience's **Gates**, in **Live sizing** on Create an audience, in **Step 4 · Before it leaves** on a seed audience and in the **Approve request** dialog.
- **Minimum population check** with **Passed** on a portfolio question result.
- The row **Minimum population** with **Enforced** in the **Permissible-use envelope** on Delivery.
- On Analysis > **Portfolio**, **Where two units meet** has a **Minimum size** column showing **Passed** or **Below**. A segment pair that is **Below** shows a dash (—) in **Overlap**.

An approver in Rules of Use can also decline a request with the reason "The audience is too small for this use".

## Why it matters

Minimum population applies everywhere a figure is reported or an audience is used. It is a gate an audience must pass before delivery, and it is **Enforced** in the envelope that travels with every delivery. A group below it is never shown as a low or rounded number; it shows as **Suppressed**.

## Common questions

**What is the minimum population?** The smallest group size the console reports on or lets you use. The checks above show whether a group meets it.

**Why is my segment suppressed?** It falls below the minimum population, so the console shows no value for it.

**Can I see a suppressed value?** No. Suppressed values can't be revealed. The row or cell shows no value at all.

**Why does the overlap show a dash?** The segment pair's **Minimum size** is **Below**, so no overlap is shown.

Related: Audience gates; Use the Portfolio tab; Read an analysis run's results
