# Fix a failed delivery

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: troubleshooting
Category: delivery

When a delivery fails, Sidebar > **Delivery** shows a red banner at the top of the page and the delivery's row in **In flight and recent** shows **Failed**. Use the banner's **Retry** or **Notify connector owner** button, and check the destination's connector under Sidebar > Admin > **Connectors**.

## A delivery shows Failed

**What you see.** A red alert banner names the definition and the destination it didn't reach: "… did not reach …. The file was written to storage, but no ingest acknowledgement arrived within …. Batch transport has no callback." The banner has **Retry** and **Notify connector owner** buttons. In **In flight and recent**, the same delivery's **Status** is **Failed** (red).

**Why it happens.** Batch destinations, such as **Activation**, whose card shows **Batch drop**, work by writing a file to storage that the partner ingests on their side. Batch transport has no callback, so the only confirmation is an ingest acknowledgement: the destination's side confirming it has ingested the file. If no acknowledgement arrives within a set time, the delivery is marked **Failed**, even though the file was written to storage.

**What to do.**

1. Click **Retry** in the banner to retry the delivery.
2. Or click **Notify connector owner** to alert the person responsible for that destination's connector. The connector owner is whoever looks after the connection to that destination; the banner offers this button rather than a name.
3. Check the connector under Sidebar > Admin > **Connectors**. Destination connectors show **Out** in **Direction** and **On delivery** in **Refresh**. In **Health**, **Failing** means "The last check failed: credentials rejected, endpoint unreachable, or the last job errored." **Not set up** means "No endpoint has been entered yet."

## The delivery history won't load

**What you see.** A red alert reading **Couldn’t load delivery history**, with the text "This is usually temporary. The last successful load is shown below, marked as possibly out of date." It has **Try again** and **Notify connector owner** buttons.

**Why it happens.** The console couldn't load the list of deliveries. The alert is about loading the history, not about a delivery's status.

**What to do.** Click **Try again**. Until it loads, treat the rows below as possibly out of date. You can also click **Notify connector owner**.

## Good to know

- **Failed** is different from **Held · approval**. A held delivery is waiting for approval, and nothing is sent until a person in each business unit whose data is involved approves.
- Connector health is checked automatically. Nobody sets health by hand.
- Raw personal data never leaves, whether a delivery succeeds or fails.

Related: Delivery statuses; A connector is Failing or Not set up; Destination classes; A page or panel couldn't load
