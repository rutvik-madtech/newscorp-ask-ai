# A delivery is Held · approval

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: troubleshooting
Category: delivery

A delivery marked **Held · approval** is waiting for approval, and nothing is sent until a person in each business unit whose data is involved approves. You see it in the **Status** column of **In flight and recent** on Sidebar > **Delivery**. The approval is given in Sidebar > **Rules of Use** by the business unit whose data the audience uses.

## My delivery is held or stuck on Held · approval

**What you see:** an amber **Held · approval** chip in the **Status** column of **In flight and recent**.

**Why it happens:** **Source-unit approval** is one of the rules in the **Permissible-use envelope** that travels with every delivery. A person in each business unit whose data contributes to the audience must approve before anything leaves. The decision sits with the unit whose fields are used, not with the requester.

**What to do:** approve the request in Rules of Use; the Delivery page has no approve button. If the data is your business unit's:

1. In the sidebar, set **Acting as** to that business unit.
2. Click **Rules of Use**. The page title reads **Rules of Use ·** followed by your unit.
3. Find the request. The **Request type** tabs **All**, **Agent**, **Cross-BU** and **Destination** narrow the list.
4. On a request card, click **Review and approve**, tick **I have checked the fields and destination above.** and click **Approve**. On a delivery request (breadcrumb **Rules of Use / Request …**), click **Approve this delivery** under **Your decision**.

## The approval sits with another business unit

**What you see:** for a seed audience, an approval gate named after the other unit, such as **Realtor.com approval**, shows **Pending** in **Step 4 · Before it leaves** on **From a seed**. The **Deliver to …** button is locked, with the text “Unlocks when … approves. Request sent … · expires in …”.

**Why it happens:** the request waits in that unit's own **Rules of Use**. The decision sits with that unit, not with the requester.

**What to do:** a person acting as that business unit approves or declines it in its **Rules of Use**, following the steps above. The text under the locked button shows when the request was sent and when it expires.

## Nobody approves in time

**What you see:** a red **Expires in …** chip at the top right of a delivery request, or **expires in …** on an agent request card, showing the time left to decide.

**Why it happens:** the request has a deadline. “Nothing is delivered on a timeout, and an expired request lapses rather than passing.” A request never approves itself.

**What to do:** approve before the time shown runs out. If the unit declines instead, “Declining stops this delivery and is recorded with your reason.”

Related: Approve a request; Review a delivery request; When a request expires; Rules of Use: how approvals work
