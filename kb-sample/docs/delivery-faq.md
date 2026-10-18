# Delivery FAQ

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: faq
Category: delivery

Answers to common questions about Sidebar > **Delivery**, where you send an audience definition to a destination and see what has already been sent.

**Can I send row-level data or personal data to a destination?**
No. Only audience membership leaves. The **Permissible-use envelope** shows **Raw PII outbound** as **Never**, and after a seed delivery **What actually left** lists **Membership of one audience** as **Sent** while **Attributes behind the definition** are **Held back**.

**Is anything sent without approval?**
No. Nothing is sent until a person in each business unit whose data is involved approves, and until then the delivery shows **Held · approval** in **In flight and recent**. An expired request lapses and nothing is delivered.

**Are matched and modelled delivered together?**
No. They are delivered as separately labelled audiences and are never added together. The **Label** column in **In flight and recent** shows **Matched**, and a delivered seed audience has separate **Delivered · matched** and **Delivered · modelled** cards.

**How do I deliver or export to activation, the lake or curation instead of the clean room?**
The destination cards at the top of Delivery show each class and its readiness (**Class 1** Your own lake / S3, **Class 2** Activation, **Class 3** Curation and **Class 4** External clean room), and the **Deliver to …** button names the destination it sends to. For a seed audience, choose the **Destination** in **Step 4 · Before it leaves** on **From a seed**. When an approved audience is to go to another destination class, the unit whose fields it uses gets a **New destination** request in **Rules of Use**.

**Does measurement come back after delivery?**
The envelope “Travels with every delivery and comes back with any measurement.” The **Curation** card reads **Push only · no reporting returns**, so no reporting comes back from that class.

**What does Batch drop mean?**
A file “Written to storage, ingested their side”, for the partner to pick up, with no callback. If no ingest acknowledgement arrives within a set time, the delivery shows **Failed** and a red banner offers **Retry** and **Notify connector owner**.

**Who is the connector owner?**
The person responsible for a destination's connector. Reach them with **Notify connector owner** on the failed-delivery banner. Connectors are listed under Sidebar > Admin > **Connectors**.

**Will my delivered audience change if a taxonomy term changes?**
No. “Delivered audiences stay pinned to the version that produced them, so returned measurement stays traceable.” The **Approve request** dialog also shows the audience **pinned to** a version.

**Are delivery times in UTC?**
Yes. **In flight and recent** shows start times in the **Started (UTC)** column.

Related: Destination classes; The permissible-use envelope; Fix a failed delivery; Matched and modelled audiences
