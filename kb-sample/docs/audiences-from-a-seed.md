# Build an audience from an advertiser seed file

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

A seed is an advertiser's list of people it already knows, such as its own customers. To match one against the News Corp portfolio, go to Sidebar > **Audiences** > **From a seed** (breadcrumb **Audiences / From a seed**). The page subtitle reads “Match an advertiser list against the portfolio, then optionally extend it.”

**Progress** at the top of the page shows **Seed**, **Match**, **Extend** and **Deliver**. The step you are on is highlighted.

## Match a seed file

1. In the sidebar, click **Audiences**, then click **From a seed** at the top right, next to **New audience**.
2. Check the seed card. It shows the **Accepted** chip and these details:
   - **Rows**: how many rows the file holds.
   - **Arrived via**: the connector the file came in through.
   - **Identifier**: the type of identifier in the file, such as hashed email.
   - **Region**: the region shown for the file.
   - **Read where**: **Inside the News Corp account**.
   - **Retention**: **Dropped at teardown**.
3. Read **What the layer will do with it**:
   - **Match against Dow Jones and Realtor.com**: **Deterministic**
   - **Report how many were found, before anything else**: **Always**
   - **Return any of the advertiser’s rows to a unit**: **Never**
   - **Tell the advertiser which unit a person came from**: **Never**
4. In **Ready to match**, click **Match against the portfolio**. “No extension is offered until the matched figure has been reported.”
5. Review the matched figure and where it was found.
6. Optionally, click **Look at extension**, then **Compare variants**.
7. Choose a variant and click the **Send variant … for approval** button, which names it.
8. Finish in **Step 4 · Before it leaves**: check the final gates, choose a **Destination**, and deliver with the **Deliver to …** button (it names the destination) once it unlocks.

## Save or send for approval

The **From a seed** page also has these buttons at the top:

- **Save as a definition** keeps the result as an audience definition in the Audiences list.
- **Send for approval** asks each business unit whose data is involved to approve.

## Good to know

- Where does the seed file come from? **Arrived via** names the connector it came in through.
- The seed is read inside the News Corp account. “The file is never written into a business unit’s system, and no unit receives a copy of it.”
- **Dropped at teardown**: the advertiser's seed file is not kept after teardown.
- “Matching runs inside the News Corp account against a licensed spine. The layer builds no graph of its own.”
- Matched and modelled are delivered as separately labelled audiences and are never added together.
- Nothing leaves until a person in each business unit whose data is involved approves.

Related: Read seed match results; Run the final checks and deliver a seed audience; What happens to an advertiser's seed file
