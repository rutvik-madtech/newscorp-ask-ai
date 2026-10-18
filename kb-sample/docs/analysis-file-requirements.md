# What your analysis file needs

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: reference
Category: analysis

A customer list for an analysis needs a column of hashed identifiers and a column of conversion timestamps in the format the dialog names, **Timestamp · ISO 8601**. You must also declare a region, and you can add an optional campaign reference. You map all of these in the **Upload a file** dialog (Sidebar > **Analysis** > **Runs** > **New analysis**).

## Fields in Upload a file

| Field | What it needs | Helper text in the dialog |
|---|---|---|
| **Identifier column** | A column of hashed identifiers, such as a hashed email. The email must be hashed, not plain text. | Shows what was detected, for example "Detected as hashed email, SHA-256" |
| **Conversion time** | A column of conversion timestamps, in the format shown in the helper text. | **Timestamp · ISO 8601** |
| **Region declared** | Required. You choose the region in the dropdown. It sets the consent regime that applies to the run. | **Required · drives the consent regime** |
| **Campaign reference** | Optional. A column used only to label the run. | **Optional · used to label the run** |

The summary line under the file name shows the rows, the size and the columns detected, so you can check the file before you run it.

## Columns that are not imported

Value data, such as a conversion value column, is not imported. The dialog shows an amber warning that names the column and says it "will not be imported". The warning explains that value data is out of scope and that "Attribution stays with the advertiser." A run's results say the same: "Conversions and attribution stay with the advertiser."

## What happens to your file

- "Matching runs inside the News Corp account. The file is not copied out and is dropped at teardown."
- On the runs list: "Uploaded files are held for the life of the run and dropped at teardown."
- On a run's page, the **Provenance** panel shows **File** as **Dropped at teardown**.

## If the file doesn't meet these needs

| What you see | Meaning |
|---|---|
| **Failed · identifier not hashed** in **Status** on the runs list | The identifier column held unhashed values. **Matched** shows a dash (—). |
| An amber "… will not be imported" warning in the dialog | That column holds value data and is left out of the run. |

Related: Upload a customer list and run an analysis; Why did my analysis run fail?; Analysis FAQ
