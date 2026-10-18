# Check what left after a seed audience is delivered

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: how_to
Category: delivery

After a seed audience is delivered, its page under Sidebar > **Delivery** shows exactly what was sent, what was held back, who approved it and that the advertiser's file is gone. The heading reads “Delivered, and the file is gone”.

## Check what left

1. In the sidebar, click **Delivery** and open the delivered seed audience. The breadcrumb reads **Delivery /** followed by the audience name.
2. Read the cards at the top:
   - **Delivered · matched**: **One labelled audience**, with the destination it went to and when.
   - **Delivered · modelled**: a dash (**—**) when the variant carries no extension.
   - **Seed rows still held**: none, marked **Discarded at teardown** with the time.
3. Read **What actually left**:

   | Item | State |
   |---|---|
   | **Membership of one audience** | **Sent** |
   | **Attributes behind the definition** | **Held back** |
   | **Which unit each person came from** | **Held back** |
   | **The advertiser’s original rows** | **Never left** |

4. Read **The record**, which logs each step of the delivery:
   - **Seed read at**: when the seed was read, **inside the News Corp account**.
   - **Approvals**: each business unit that approved, with its time.
   - **Delivered to**: the destination and the time.
   - **Seed discarded**: the time the seed was dropped, logged as a **recorded state change**.
   - **Retained here**: **The definition, the approvals, this record**.

## Good to know

- What did we send to the clean room? Only membership of the audience. The attributes behind the definition and which unit each person came from are held back. Row-level data and raw personal data never leave.
- Was the advertiser's file deleted? Yes. **Seed rows still held** shows none, with **Discarded at teardown**, and **Seed discarded** records when it happened. The page subtitle reads: “The advertiser can now buy against people it already knows. The list it sent to find them no longer exists here.”
- What does the console keep? Only what **Retained here** lists: the definition, the approvals and this record. The seed file is not kept.
- Matched and modelled are delivered as separately labelled audiences and are never added together.
- Running the same seed again starts again from a new file, from Sidebar > **Audiences** > **From a seed**. “Nothing was kept to make it quicker.”
- Times on the record are shown in UTC.

Related: What happens to an advertiser's seed file; Delivery statuses; Review a delivery request
