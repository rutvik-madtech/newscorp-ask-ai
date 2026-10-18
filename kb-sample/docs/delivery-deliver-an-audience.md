# Preview and deliver an audience

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: how_to
Category: delivery

You deliver (send) an audience definition from its Delivery page: Sidebar > **Audiences** > click the definition > **Deliver**, then click the **Deliver to …** button, which names the destination. Click **Preview** first to check before you send. Seed audiences are delivered from **Step 4 · Before it leaves** on **From a seed**.

## Deliver an audience definition

1. In the sidebar, click **Audiences**, click the definition, then click **Deliver** in its detail panel. The page heading reads **Delivery ·** followed by the definition's name.
2. Check the destination class card for where you're sending. **Ready** means the class is set up. **Batch drop** means a file is written to storage and the partner ingests it on their side.
3. Check the **Permissible-use envelope** on the right. It lists the rules that travel with the delivery, such as **Minimum population** (**Enforced**), **Source obfuscation** (**On**), **Source-unit approval** (**Granted**), **Consent basis · …** followed by the region (**Passed**) and **Raw PII outbound** (**Never**).
4. Click **Preview** to check the delivery before you send it.
5. Click the **Deliver to …** button at the top right. It names the destination it delivers to.
6. Track the delivery in **In flight and recent**. If an approval is still needed, its **Status** shows **Held · approval** and nothing is sent until a person in each business unit whose data is involved approves.

## Deliver a seed audience

1. Go to Sidebar > **Audiences** > **From a seed** and find **Step 4 · Before it leaves**.
2. Pick where it goes in the **Destination** dropdown. Each option starts with its destination class, such as **External ·** for an external clean room.
3. Click the **Deliver to …** button, which names the destination you picked. It stays locked, greyed out with a padlock, until the other business unit whose data is used approves. The text under it reads "Unlocks when … approves."

## Good to know

- Which destination does it go to? On the Delivery page, the primary button names the destination it delivers to, and each destination class card shows its readiness. For a seed audience, you pick the destination in the **Destination** dropdown; each option starts with its destination class, such as **External ·**.
- Adding a destination class to an audience that is already approved for another destination needs its own approval. It appears as a **New destination** request in **Rules of Use**.
- Nothing leaves until a person in each business unit whose data is involved approves. "Nothing is delivered on a timeout, and an expired request lapses rather than passing."
- Raw personal data and row-level data are never sent.

Related: Delivery statuses; Destination classes; A delivery is Held · approval; Run the final checks and deliver a seed audience
