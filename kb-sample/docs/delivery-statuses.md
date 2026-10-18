# Delivery statuses

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: reference
Category: delivery

A delivery status tells you what has happened to an audience you sent. You see it in the **Status** column of **In flight and recent** on Sidebar > **Delivery**. The table is marked **live** with a time, and it lists deliveries across definitions, not only the one named in the page heading.

## Columns in In flight and recent

| Column | What it shows |
|---|---|
| **Definition** | The audience definition that was sent. |
| **Destination** | Where it was sent. |
| **Label** | Which audience was sent, such as **Matched**. |
| **Status** | Where the delivery stands now. |
| **Started (UTC)** | When the delivery started, in UTC. |

## Statuses

| Status | Colour | Meaning |
|---|---|---|
| **Delivered** | Green | The delivery reached the destination. |
| **In flight** | Amber | The delivery has started and is still in progress. |
| **Failed** | Red | The delivery didn't reach the destination. A red banner at the top of the page explains why and offers **Retry** and **Notify connector owner**. |
| **Held · approval** | Amber | The delivery is waiting for approval. Nothing is sent until a person in each business unit whose data is involved approves. |

## Labels

| Label | Meaning |
|---|---|
| **Matched** | The delivered audience is the matched audience, consented and deduplicated, not a modelled extension. |

Matched and modelled are never added together. They are delivered as separately labelled audiences.

## Good to know

- Where do I see what's been sent? In **In flight and recent** on the Delivery page. Open it from Sidebar > **Delivery**, or from Sidebar > **Audiences** > a definition > **Deliver**.
- A delivery stuck on **Held · approval** is waiting for each business unit whose data is involved to approve. Those units decide in **Rules of Use**. An expired request lapses and nothing is delivered.
- A **Failed** delivery to a batch destination can mean the file was written to storage but no ingest acknowledgement arrived in time. The red banner says so.
- The chips on the destination cards (**Ready**, **Batch drop** and **Vendor TBC**) describe a destination's readiness, not a delivery's status.

Related: Fix a failed delivery; A delivery is Held · approval; Preview and deliver an audience; Destination classes
