# Read a portfolio question result

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: how_to
Category: analysis

When you click **Run the question** on **Terms, before anything runs** (Sidebar > **Analysis** > **Portfolio** > **Resolve terms**), the result opens as **Evaluated at each unit, then resolved**, with the breadcrumb **Portfolio › Question … › Result**. A green **Completed · …** chip shows when the question finished. The screen shows each business unit's count separately, then the deduplicated portfolio figure and the checks that apply.

## Steps

1. Read the card for each business unit, such as **Evaluated at Dow Jones** and **Evaluated at Realtor.com**. Each shows the eligible people who meet that unit's terms, computed inside that unit, with the time it was computed.
2. Read the portfolio card, **Portfolio · …, deduplicated**. It is resolved over the unit results above, never over raw records. While the identity spine is pending, it reads **Pending identity spine** and shows a placeholder instead of a figure. The identity spine is the shared identity layer that removes people counted at more than one unit.
3. Read **Order of operations** to see how the answer was reached.
4. Check the overlap table (see below).
5. Click **See the finding** to read the answer in plain language.

To go back to the terms, click **Question …** in the breadcrumb.

## How the answer was calculated

**Order of operations** lists each step with its time:

- Eligibility is applied at each unit, before any counting.
- Each unit evaluates the same definition on its own data, in its own environment.
- Resolution runs over those unit results only, to remove double counting.
- Counts are returned. No records are moved between units.

No unit sees another unit's result or data. Each unit answers the same question separately.

## The overlap table

The table **Where the … units meet** has the columns **Measure** and **Value**:

- **Overlap between the … populations**: **Not verified**. "No overlap percentage is shown until the analysis is verified against the spine."
- **Minimum population check**: whether the result meets the minimum population, for example **Passed**.
- **Method**: **Deterministic only**. Only directly matched data is counted, and no modelled extension (what some people call lookalikes) is applied.

## Good to know

- Every figure counts consented, eligible people. The footer, which begins "Every figure above: consented, eligible people", shows each unit's as-of time.
- Matched and modelled figures are never added together.
- A result is a count only. It creates no audience and sends nothing anywhere.

Related: Read a portfolio question finding; The identity spine; Minimum population and suppressed figures
