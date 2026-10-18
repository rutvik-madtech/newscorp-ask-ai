# Glossary: matching, sizes and privacy

Applies to tier: Power User
Business unit: all
Console page: All pages
Article type: reference
Category: concepts

This glossary explains the matching, audience size and privacy terms you meet across the console, mostly on **Audiences**, **Analysis** and **Delivery**. Terms are in alphabetical order.

- **Aggregate**: a total count for a group, never individual records. A run's Composition note reads "Aggregate only, gated by minimum population."
- **Consent · confirmed at source**: consent was confirmed by the business unit that holds the data. It appears as a gate row with **Passed**.
- **Deduplicated / counted once**: a person found in more than one business unit is counted once, as in **Both · counted once** on seed match results.
- **Deterministic**: an exact match on an identifier, not modelled or estimated, as in **Matched · deterministic**.
- **Eligible (for cross-unit use)**: people who may be used across business units. "Opted-out records are excluded at each unit before counting." A portfolio question's finding (**The finding**) carries an **Eligible population** chip.
- **Hashed identifier**: an identifier, such as an email address, supplied in hashed form rather than as readable text. A run with an unhashed file shows **Failed · identifier not hashed**.
- **Identity spine (the spine)**: the licensed identity layer people are matched and deduplicated on across business units.
- **Matched**: people found by deterministic matching on the spine, consented and deduplicated. The matched figure is always reported first.
- **Members and reach**: in a cross-unit audience, members come from the business units that hold the fields the membership rule uses. Other units can only add reach.
- **Minimum population**: the smallest group the console reports on or lets you use. Groups below it are suppressed.
- **Modelled (extension)**: people who resemble a matched group, found by a licensed provider's model. They are not the advertiser’s customers, and they are always kept separate: matched and modelled figures are never added together.
- **Overlap / Not verified**: overlap is the people in both segments of a pair. Until it is verified against the spine, it shows **Not verified** and no percentage.
- **Raw PII**: raw personally identifiable information. It is never sent out; the **Raw PII outbound** row reads **Never**.
- **Row-level data**: individual records. They never leave; the **Row-level data out** gate reads **Never**.
- **Seed (seed file)**: "A list of people the advertiser already knows", matched against the portfolio to see how many of them it can reach. Start one from Audiences > **From a seed**.
- **Source obfuscation**: hides which source each person came from. It shows as a gate or envelope row with **On**.
- **Suppressed**: shown with a lock icon and no value when a group falls below the minimum population. Nothing is rounded.
- **Teardown**: the point where working data, such as an uploaded file, is discarded. It is a recorded state change; files show **Dropped at teardown**.

Related: Matched and modelled audiences; Minimum population and suppressed figures; The identity spine; Glossary: console, roles and approvals
