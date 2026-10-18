# Audience gates

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: concept
Category: concepts

A gate is a check an audience or request must pass before it can go ahead. Each gate is a row with the check on the left and its result chip on the right. You find gates in an audience's detail panel on Audiences, on Create an audience, on a seed audience and in Rules of Use.

## Gates you will see

| Gate | Result | What it means |
|---|---|---|
| **Minimum population** | **Passed** | The audience meets the minimum population. |
| **Consent · confirmed at source** | **Passed** | Consent was confirmed by the business unit that holds the data. |
| **Source obfuscation** | **On** | Which source each person came from is hidden. |
| An approval gate named after the business unit whose data is used, such as **Realtor.com approval** | **Required**, **Pending** or **Given** | **Required**: that unit's approval is still needed. **Pending**: an approval request has been sent and is waiting for an answer. **Given**: that unit has approved. |
| **Row-level data out** | **Never** | No individual records leave. |
| **Raw PII outbound** | **Never** | No raw personal data is sent out. |

## Where you see gates

- Audiences > click a definition > **Gates** in the detail panel.
- Audiences > **New audience** > **Live sizing** panel > **Gates**.
- A seed audience, under **Step 4 · Before it leaves**.
- Rules of Use > **Review and approve** on a request card, in the **Approve request** dialog.
- A delivery request in Rules of Use (breadcrumb **Rules of Use / Request …**), under **Checks already passed**.
- Rules of Use request cards, as **System gates · checked …** with **All passed**.

## How gates affect delivery

An approval gate that shows **Required** or **Pending** keeps delivery locked until that business unit approves. On a seed audience, the **Deliver to …** button (it names the destination) shows a padlock, with helper text that starts "Unlocks when …" and names the unit, followed by when the request was sent and when it expires. On Create an audience, an amber notice explains that saving does not deliver and that the named unit must approve before the audience reaches any destination.

The decision sits with the business unit whose data is used, not with the requester. A person in that unit approves or declines in Rules of Use. Nothing leaves until a person in each business unit whose data is involved approves, and "Nothing is delivered on a timeout, and an expired request lapses rather than passing."

## Common questions

**What does Realtor.com approval Required mean?** Realtor.com's data is in the audience, so a person at Realtor.com must approve before it can reach any destination.

**Why is a gate Pending?** The approval request has been sent and that unit has not answered. Check the helper text under the locked button for when it expires.

**What is source obfuscation?** A protection that hides which source each person came from. It shows **On**.

Related: Approve a request; Run the final checks and deliver a seed audience; Can't deliver or send an audience; Minimum population and suppressed figures
