# Run the final checks and deliver a seed audience

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

Before a seed audience leaves, the **From a seed** page runs its final checks in **Step 4 · Before it leaves**, the **Deliver** step of **Progress**. Go to Sidebar > **Audiences** > **From a seed** (breadcrumb **Audiences / From a seed**). The panel heading, **Step 4 · Before it leaves · checked …**, shows when the checks last ran, in UTC.

## Check the gates and deliver

1. On **From a seed**, find the **Step 4 · Before it leaves** panel and check each gate:
   - **Row-level data out** shows **Never**: no row-level data leaves.
   - **Minimum population** shows **Passed**: the audience meets the minimum population.
   - **Source obfuscation** shows **On**: which source each person came from is hidden.
   - **Consent · confirmed at source** shows **Passed**: consent was confirmed by the business unit that holds the data.
   - An approval gate named after the other business unit whose data is used, such as **Realtor.com approval**, shows **Pending** until that unit approves.
2. Choose where the audience goes in the **Destination** dropdown. Each option starts with its destination class, such as **External ·** followed by the destination.
3. If the approval request hasn't gone out, click **Send for approval** at the top of the page.
4. Once the button unlocks, click **Deliver to …** (it names the destination you chose).

## Why the Deliver to … button is locked

While an approval is pending, the **Deliver to …** button is greyed out with a padlock. The text under it reads "Unlocks when … approves. Request sent … · expires in …", naming the business unit, when the request was sent and the time left.

For example, **Realtor.com approval** showing **Pending** means the audience uses Realtor.com data and the request is waiting for Realtor.com's answer. The decision sits with that unit, not with you as the requester. A Power User acting as that unit opens the request in Sidebar > **Rules of Use** and clicks **Approve this delivery** or **Decline**. Your button unlocks when that unit approves.

## Good to know

- Row-level data never leaves. Only membership of the audience does, and the advertiser's own file is not part of what leaves.
- Nothing leaves until a person in each business unit whose data is involved approves.
- "Nothing is delivered on a timeout, and an expired request lapses rather than passing." If the request expires, nothing is delivered.
- "Approving this covers this audience, this destination and this variant."
- **Save as a definition** keeps the result as an audience definition without delivering it.
- After delivery, the record is under Sidebar > **Delivery**. Open the delivered audience (breadcrumb **Delivery / …**).

Related: Audience gates; Review a delivery request; Check what left after a seed audience is delivered; Can't deliver or send an audience
