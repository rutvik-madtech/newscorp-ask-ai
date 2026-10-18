# Open an audience definition: rule, size and gates

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

To see an audience's rule, size and gates, go to Sidebar > **Audiences** and click the definition's name. A detail panel opens on the right of the same page, so you stay on the list.

## Open a definition

1. In the sidebar, click **Audiences**.
2. In the **Definition** column, click the name of the audience. The row is highlighted and the detail panel opens on the right.
3. Read the panel from top to bottom, as described below.

## What the panel shows

- Header line (no label): above the definition's name, the type and when it was last edited, for example **Cross-BU reach · edited …**.
- **Membership rule**: the rule that decides who is in the audience, written in shared-vocabulary field names joined with AND, OR and NOT.
- **Size · as of …**: separate cards for **Matched · deterministic** and **Modelled · separate audience**. The matched and modelled figures are never added together.
- The line under the size cards: for a **Cross-BU reach** definition, it says which unit's fields define the audience and so supply the members, how many of the matched people are also reachable on another unit, and that the other unit adds reach, not members.
- **Why this size?**: a button beside that line, with the caption **from the spine provider · not contracted**. The caption refers to the modelled figure and marks it as coming from a spine provider that is not under contract.
- **Gates**: **Minimum population** (**Passed**), **Consent · confirmed at source** (**Passed**) and **Source obfuscation** (**On**).

## Copy or deliver the audience

- To copy an audience, click **Duplicate** at the top of the panel.
- To deliver it, click **Deliver**. This opens the Delivery page for the definition, with the heading **Delivery ·** followed by the definition's name.

## Good to know

- The panel's only action buttons are **Duplicate** and **Deliver**. If you want to edit or reuse a definition, these are what the panel offers.
- Why is my audience this size? The matched figure counts consented people, deduplicated on the spine. For a **Cross-BU reach** definition, only the defining unit's fields add members; other units add reach. Read the line under the size cards and use **Why this size?** next to it.
- The size is a snapshot from the time shown after **Size · as of …**, in UTC.
- Check **Gates** before you click **Deliver**. Nothing leaves until a person in each business unit whose data is involved approves.

Related: Members and reach in cross-unit audiences; Audience gates; Preview and deliver an audience
