# Destination classes

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: concept
Category: delivery

A destination class is the kind of place an audience can be delivered (sent) to. You see the destination classes as cards across the top of Sidebar > **Delivery**, labelled **Class 1** to **Class 4**. Each card names the class, says how data moves there and shows whether the class is ready.

## The destination classes

| Card | Class | How it works |
|---|---|---|
| **Class 1** | **Your own lake / S3** | **Bidirectional**: data can go out and come back. |
| **Class 2** | **Activation** | **Written to storage, ingested their side**: a batch file is written to storage and the partner picks it up on their side. |
| **Class 3** | **Curation** | **Push only · no reporting returns**: you can send to it, but no reporting comes back. |
| **Class 4** | **External clean room** | **Federated**: the audience is matched in the clean room without the data being handed over. |

The **Activation** and **External clean room** cards also name the partner after a **·**.

## Readiness chips

Each card shows a readiness chip:

- **Ready** (green): the class is set up and can receive deliveries.
- **Batch drop** (amber): delivery is a file dropped into storage with no callback. Success depends on an ingest acknowledgement from the partner's side. If none arrives within a set time, the delivery shows **Failed**.
- **Vendor TBC** (grey): no vendor is confirmed for that class.

The caption **Destination readiness checked …** under the cards shows when readiness was last checked, in UTC.

## Where else you see destination classes

- On **From a seed**, the **Destination** dropdown in **Step 4 · Before it leaves** lists each option with its class first, such as **External ·** followed by the destination.
- On a request in **Rules of Use**, the **Destination** line shows where the audience would go and can also say how it is delivered there, such as federated or batch.
- A **New destination** request in **Rules of Use** asks to add a destination class to an audience that is already approved for another destination.

## Why it matters

The class decides what comes back and how you know a delivery worked. No reporting returns from curation, and activation relies on an ingest acknowledgement, so a missing one shows as a failed delivery.

The class also affects approval. Sending an approved audience to another destination class needs its own approval, through a **New destination** request in **Rules of Use**. Nothing leaves until a person in each business unit whose data is involved approves, and raw personal data never leaves.

Related: Preview and deliver an audience; Fix a failed delivery; Delivery FAQ; Delivery statuses
