# Upload a customer list and run an analysis

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: how_to
Category: analysis

To run an analysis, go to Sidebar > **Analysis** > **Runs** and click **New analysis**. The **Upload a file** dialog opens. There you check your customer file, map its columns and click **Run analysis** to match the list against the portfolio.

## Run an analysis

1. In the sidebar, click **Analysis**. On the **Runs** tab, click **New analysis** at the top right. The **Upload a file** dialog opens over the runs list.
2. Check the file name at the top of the dialog. The summary line under it shows the rows, the size and the columns detected. To use a different file, click **Replace file**.
3. Under **Identifier column**, choose the column that holds the hashed identifier, such as a hashed email. The helper text under the field then says what was detected, for example "Detected as hashed email, SHA-256". Check that it names a hashed identifier.
4. Under **Campaign reference**, you can choose a column to label the run. The helper text reads **Optional · used to label the run**, so you can leave it out.
5. Under **Conversion time**, choose the column that holds the conversion timestamp. The helper text reads **Timestamp · ISO 8601**.
6. Under **Region declared**, choose the region. The helper text reads **Required · drives the consent regime**.
7. Read any amber warning. It names a column and says it "will not be imported". Value data, such as a conversion value, is out of scope, and "Attribution stays with the advertiser."
8. Click **Run analysis**. To close the dialog without running anything, click **Cancel** or the × at the top right.

In the **Runs** list, runs you submitted carry the **You** source chip. Click a run's name to read its results.

## Good to know

- The dialog notes: "Matching runs inside the News Corp account. The file is not copied out and is dropped at teardown."
- **Region declared** is required. **Campaign reference** is optional.
- The identifier must be hashed. A file with an unhashed identifier fails, and the run shows **Failed · identifier not hashed** in **Status** on the runs list.
- **New analysis** is only on the **Runs** tab. The **Portfolio** tab answers questions with no advertiser file involved.

Related: What your analysis file needs; View and filter analysis runs; Why did my analysis run fail?; Read an analysis run's results
