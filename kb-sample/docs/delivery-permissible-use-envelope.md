# The permissible-use envelope

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: concept
Category: delivery

The permissible-use envelope is the set of usage rules attached to every delivery. You find it in the **Permissible-use envelope** panel on Sidebar > **Delivery**, which states: “Travels with every delivery and comes back with any measurement.”

## What the envelope is

Every audience you send carries the same rules with it, and when measurement comes back from a destination, the envelope comes back with it. Each row in the panel names a rule and shows its current state.

| Row | State shown | What it means |
|---|---|---|
| **Minimum population** | **Enforced** | The minimum population rule applies. Groups below the minimum population are suppressed with no value. |
| **Source obfuscation** | **On** | Which business unit each person came from is hidden in what is sent. |
| **Source-unit approval** | **Granted** | A person in each business unit whose data contributes has approved. Nothing leaves before that. |
| **Consent basis · …**, followed by the region whose consent check applies | **Passed** | The consent check for that region passed. |
| **Raw PII outbound** | **Never** | Raw personal data never leaves with a delivery. |
| **Retention at destination** | Shown on the row | How long the destination may keep the data. |

## Where you see it

- Sidebar > **Delivery**, in the **Permissible-use envelope** panel on the right of the page, above **Agent endpoint**.
- The same checks appear when your business unit approves a request. The **Approve request** dialog in Sidebar > **Rules of Use** lists **Minimum population**, **Consent · confirmed at source**, **Source obfuscation** and **Raw PII outbound**, and shows **Retention there** for that request's destination.

The panel is read-only. It has no edit controls, so you can't change, add or switch off a rule from the Delivery page.

## Why it matters

- **What rules travel with my delivery?** All the rows above go with every delivery, whichever destination you send to.
- **Does any raw PII leave with a delivery?** No. **Raw PII outbound** reads **Never**. Only audience membership leaves, and row-level data stays behind. In the **Approve request** dialog, **Fields that leave** shows what is actually sent, such as **None · cohort membership only**.
- **How long can the destination keep the data?** Read the **Retention at destination** row on the panel, or **Retention there** in the **Approve request** dialog for a specific request.
- **What if approval is still outstanding?** A delivery waiting for approval shows **Held · approval** in **In flight and recent** and is not sent until a person in each business unit whose data is involved approves.

Related: Audience gates; Approve a request; A delivery is Held · approval; Delivery FAQ
