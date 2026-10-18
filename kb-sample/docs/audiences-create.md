# Create an audience

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

To create a new audience, go to Sidebar > **Audiences** > **New audience**. The **Create an audience** page opens, with the breadcrumb **Audiences / New**. You choose a starting point, build the membership rule, name the audience, then save it as a draft or send it for approval.

## Create an audience

1. Open the page: Sidebar > **Audiences** > **New audience**. To start from a shared term instead, go to Sidebar > **Taxonomy**, open the term and click **Use in an audience**.
2. Under **Step 1 · Start from**, choose one option:
   - **An analysis run**: its subtext names the run.
   - **A blank definition**: "Write a rule from the shared vocabulary".
   - **A seed file**: "Upload identifiers and match them".
3. Under **Step 2 · Membership rule**, accept or edit the AI-suggested rule, or build your own with **+ Add condition**.
4. Enter a **Name**.
5. Choose an option in **Precedence when units disagree**: an option starting **Not needed ·** when only one unit asserts the attribute, or a **Region: … wins** option that names the unit whose value wins, such as **Region: Dow Jones wins**.
6. Check the **Live sizing** panel on the right.
7. Click **Save as draft** to keep working later, or **Send for approval** to submit the audience for approval.

## Read the Live sizing panel

- It "Updates as you edit." The line under the title says when it was last evaluated and that it runs in place on each unit's data, with the time that data is from.
- **Matched · deterministic** and **Modelled · separate audience** show as separate cards and are never added together.
- A line names the unit that contributes the members, "… contributes all members (declared).", and says how many of them are also reachable on another unit.
- **Gates** lists **Minimum population** and **Consent · confirmed at source**. When another unit's data is used, it also lists an approval gate named after that unit, such as **Realtor.com approval**, showing **Required**.

## Good to know

- Saving does not deliver. When another unit's data is used, an amber notice reads "Saving does not deliver. … must approve before this reaches any destination.", naming that unit.
- **Send for approval** submits the audience for approval. Nothing reaches any destination until a person in each business unit whose data is involved approves.
- **Use in an audience** on a Taxonomy term opens the same **Create an audience** page.
- To match an advertiser's list of identifiers, you can also click **From a seed** on the Audiences page.

Related: Write the membership rule; Precedence when units disagree; Audience gates
