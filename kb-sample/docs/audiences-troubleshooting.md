# Can't deliver or send an audience

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: troubleshooting
Category: audiences

When you can't deliver or send an audience from Sidebar > **Audiences**, the reason shows on the page: in its gates (in **Live sizing** on **Create an audience** or under **Step 4 · Before it leaves** on **From a seed**) or on the extension and variant steps of **From a seed**.

## The Deliver to … button is locked

**What you see:** on **From a seed**, the **Deliver to …** button (it names the destination) is greyed out with a padlock. The text under it reads "Unlocks when … approves. Request sent … · expires in …".

**Why it happens:** another business unit's approval gate, such as **Realtor.com approval**, shows **Pending**.

**What to do:** the button unlocks once a person in that unit approves in Rules of Use. An expired request lapses and nothing is delivered.

## An approval gate shows Required

**What you see:** in **Gates**, an approval gate named after another business unit, such as **Realtor.com approval**, shows **Required**.

**Why it happens:** the audience uses that unit's data, so that unit decides.

**What to do:** click **Send for approval**. A person in that unit then approves or declines in Rules of Use.

## “Saving does not deliver…” notice

**What you see:** an amber notice on **Create an audience** reads "Saving does not deliver. … must approve before this reaches any destination."

**Why it happens:** this is expected. **Save as draft** only stores the definition.

**What to do:** click **Send for approval** when you are ready.

## The extension can't run

**What you see:** on the extension step of **From a seed**, a **Provider not contracted** banner shows. Under **Steps 2 and 3 · Result**, the modelled figure reads **Modelled · provider not contracted**.

**Why it happens:** the extension needs an identity and modelling provider, and none is under contract. Sizes there are "shown as placeholders, not estimates."

**What to do:** go ahead with the matched audience, which needs only the spine.

## A variant is stuck in Draft

**What you see:** on **Variants**, an extended variant shows **Draft**, and its **Provider needed** reads **Spine and model · not contracted**.

**Why it happens:** it stays a draft until a modelling provider is signed.

**What to do:** send the matched-only variant (its **Provider needed** reads **Spine only**) with the **Send variant … for approval** button.

## The audience is too small to leave

**What you see:** **Minimum population** in **Gates** doesn't show **Passed**.

**Why it happens:** the audience is below the minimum population, and groups below it are suppressed with no value.

**What to do:** watch the gate in **Live sizing** on **Create an audience**, which "Updates as you edit". The audience leaves only once it shows **Passed**.

Related: Audience gates; When a request expires; A delivery is Held · approval; Run the final checks and deliver a seed audience
