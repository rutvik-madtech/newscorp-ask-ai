# Precedence when units disagree

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: concept
Category: audiences

Precedence decides which business unit's value is used when units hold conflicting values for the same attribute in a cross-unit audience. You set it on Create an audience (Sidebar > **Audiences** > **New audience**), in the **Precedence when units disagree** dropdown under **Step 2 · Membership rule**.

## What precedence means

When an audience draws on more than one business unit, the units can hold different values for the same attribute, such as region. Precedence says whose value wins when that happens. It only matters when more than one unit provides the attribute.

## Set it when you create an audience

The **Precedence when units disagree** dropdown offers options such as:

- **Not needed · one unit asserts …**: only one business unit provides the attribute, so there is no conflict to settle. The rest of the option text names that attribute. Choose it when the attribute your rule depends on comes from one unit only.
- **Region: Dow Jones wins**: where the units disagree on region, the Dow Jones value is used.
- **Region: Realtor.com wins**: where the units disagree on region, the Realtor.com value is used.

The person who creates the cross-unit output sets precedence. Agency users cannot set it: their Portfolio audiences page lists setting precedence under **Not available to your role**.

## Where you see it

- **Audiences list**: the **Precedence** column shows **Region:** followed by the business unit whose values win. A dash (—) means no precedence is set or needed.
- **Rules of Use**: when another unit's output uses your fields, its **Cross-BU output** request card carries an amber notice: “Precedence set by the creator: …, … wins. Your region values lose on conflict.” The notice names the attribute and the unit whose values win. To find these cards, go to Sidebar > **Rules of Use** and open the **Cross-BU** tab.

## Why it matters

If a request says your region values lose on conflict, the creator of that output chose another unit's values for region. Wherever your unit's region value differs from theirs, theirs is used in that output. Read the notice before you click **Review and approve** or **Decline** on the card.

Precedence only decides whose value is used. It is separate from **Your gating rules** on Rules of Use, where the page states: “In a cross-BU output the most restrictive contributing rule wins.”

Related: Create an audience; Find and read a request; Audience types, precedence and statuses
