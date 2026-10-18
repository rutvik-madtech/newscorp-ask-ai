# Write the membership rule

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

The membership rule decides who is in an audience. You write it under **Step 2 · Membership rule** on Sidebar > **Audiences** > **New audience**, using canonical (shared-vocabulary) field names joined with AND, OR and NOT. You can accept an AI-suggested rule or add your own conditions.

## Use the AI suggestion

1. Under **Step 2 · Membership rule**, find the box titled **Suggested rule from run …** with the **AI suggestion** chip. It appears when you start from an analysis run, and its title names the run.
2. Expand **Why this?** to read why the rule was suggested. The reasons draw on how attributes indexed in the run, and the suggestion uses only canonical fields that both the steward and the requester can see.
3. Choose what to do with it:
   - **Accept into rule** uses the suggestion as it is.
   - **Edit first** lets you change the suggestion before you use it.
   - **Dismiss** discards it.

## Write your own rule

1. To start from scratch, choose **A blank definition** ("Write a rule from the shared vocabulary") under **Step 1 · Start from**.
2. Under **Step 2 · Membership rule**, click **+ Add condition** for each condition you want.
3. Watch the **Live sizing** panel on the right. It updates as you change the rule, shows matched and modelled sizes separately and lists the **Gates**.

## Which fields you can use

Rules use canonical fields from the shared vocabulary, the terms listed on Sidebar > **Taxonomy**. Each business unit's own fields are mapped to these shared terms. For an existing definition, the rule shows under **Membership rule** in its detail panel on Audiences.

## If a term you need isn't available

Check the term's mapping on Taxonomy:

1. Go to Sidebar > **Taxonomy** and open the term.
2. Under **How each business unit maps to it**, read the **Mapping** chip for each unit. **Mapped** means the unit supplies the term. **No equivalent** means it does not: "A unit with no equivalent is marked, never approximated."
3. To change your own unit's mapping, click the edit button named after your business unit, for example **Edit Dow Jones mapping**.

## Good to know

- You can change the suggested rule before using it: click **Edit first**.
- To start a new audience from a shared term, click **Use in an audience** on the term in Taxonomy.

Related: Create an audience; Build an audience from an analysis run; Work with AI suggestions and AI summaries
