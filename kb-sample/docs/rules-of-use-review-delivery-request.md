# Review a delivery request

Applies to tier: Power User
Business unit: all
Console page: /rules-of-use
Article type: how_to
Category: rules_of_use

When an audience built partly from your unit's fields is about to leave the portfolio, for example after someone clicks **Send variant … for approval**, your unit gets a delivery request in Sidebar > **Rules of Use**. Why is your unit asked to approve another unit's audience? The decision sits with the unit whose fields are used, not with the requester.

## Review and decide

1. In the sidebar, set **Acting as** to your business unit.
2. Click **Rules of Use** and open the request. The breadcrumb reads **Rules of Use / Request …** and the heading names your unit, ending “… is asked first”.
3. Check the red **Expires in …** chip at the top right. It shows the time left to decide.
4. Read **What is being asked for**:
   - **Audience**: the audience and variant to be delivered.
   - **Requested by**: the requesting business unit and the requester's role, such as **Power User**.
   - **Destination**: shown with its class first, such as **External · …** for an external clean room.
   - **Your fields involved**: which of your unit's fields the audience uses.
   - **People from your data**: how many people come only from your data and how many are shared with another unit.
   - **Modelled extension**: **None in this variant** when the variant has no modelled people.
5. Read the scope line: “Approving this covers this audience, this destination and this variant.”
6. Read **Checks already passed**:
   - **Row-level data out**: **Never**
   - **Minimum population**: **Passed**
   - **Source obfuscation**: **On**
   - **Consent · confirmed at source**: **Passed**
   - an approval gate named after the requesting unit, such as **Dow Jones approval**, showing **Given** with the time.
7. Under **Your decision**, click **Approve this delivery**. To refuse, click **Decline**, which opens the **Decline request** dialog.

## Good to know

- Does my approval cover other variants? No. It covers this audience, this destination and this variant, and does not carry over to the audience's other variants.
- “The advertiser’s own file is not part of what leaves. Only membership of this audience does.”
- “Declining stops this delivery and is recorded with your reason. Nothing is delivered on a timeout, and an expired request lapses rather than passing.” If you don't decide before it expires, the request never approves itself.
- The requester can't approve on your unit's behalf. Each business unit whose data is in the audience must approve before it leaves. The requesting unit's own approval shows under **Checks already passed**.
- Row-level data never leaves.
- After delivery, the record under **Delivery** shows what actually left.

Related: Decline a request; When a request expires; Check what left after a seed audience is delivered; Approve a request
