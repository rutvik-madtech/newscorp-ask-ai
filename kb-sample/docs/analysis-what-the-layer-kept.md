# See what the layer kept and run an audit check

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: how_to
Category: analysis

To see what happened to a portfolio question and what the console still holds, click **Show what the layer kept** on the screen headed "You have an answer. Nothing left the building." (Sidebar > **Analysis** > **Portfolio** > your question > **See the finding** > **What happens next**). **What the layer kept** opens, with the breadcrumb **Portfolio › Question … › Custody**. It shows "The lifecycle of this query, an audit check anyone can repeat, and the record of the question itself."

## Read the query lifecycle

**Query lifecycle · …** shows each stage the query passed through, with its time:

- **Opened**: Question accepted.
- **Filtered**: Eligibility applied.
- **Evaluated**: each unit evaluated separately.
- **Returned**: Counts shown.
- **Torn down**: Working set discarded.

**Torn down** is the final stage. At teardown, the working set used to evaluate the query is discarded. "Teardown is a recorded state change, not a scheduled cleanup job."

## Run an audit check

Use the audit check to find out whether someone's identifier was used in a query, and whether anything about it is still held.

1. Go to the **Audit check** card.
2. Enter the identifier, in hashed form, in **Identifier, hashed**.
3. Click **Check**.
4. Read the results:
   - **Took part in …**, which names the query, for example **Yes**.
   - **Still held by the layer**, for example **No records**.
   - **Attributes retrievable**, for example **None**.

"The check returns a yes or a no, never a record."

## Read the record of the question

**The record of the question** lists:

- **Asked by**: the business unit and role of the person who asked.
- **Units evaluated**: the business units that evaluated the question.
- **Fields read**: the local fields that were read.
- **Returned**: what the query returned.
- **Left the layer**: **Nothing**.
- **Retained**: **The question, its term mapping, and this record**.

"Each unit can read this record for any query that touched its own fields."

## Good to know

- You can't look a person up in the console. "This is a check against the audit trail. No screen anywhere looks a person up."
- After teardown, the layer keeps only the question, its term mapping and this record.
- To go back to the screen headed "You have an answer. Nothing left the building.", click **Question …** in the breadcrumb.

Related: Save, turn into an audience or export a portfolio question; Analysis FAQ
