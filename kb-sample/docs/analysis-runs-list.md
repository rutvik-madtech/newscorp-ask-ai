# View and filter analysis runs

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: how_to
Category: analysis

Your analysis runs are on Sidebar > **Analysis** > **Runs**, the tab that opens by default. The page subtitle reads: "Match a customer list against the portfolio. Runs submitted by agency agents appear here too." The list holds your own runs, other submitters' runs and agency runs.

## See the runs

1. In the sidebar, click **Analysis**. The **Runs** tab is selected. From a run's page, click **Analysis** in the breadcrumb.
2. Read the table. Its columns are:
   - **Run**: the run's name. Click it to open the run's results.
   - **Source**: who sent the run (see below).
   - **Submitted by**: the submitter. For a person, it shows their business unit and job function. For an agency run, it names the agency's agent.
   - **File**: the uploaded file.
   - **Rows**: how many rows the file held.
   - **Matched**: how many rows matched against the portfolio. A failed run shows a dash (—).
   - **Status**: **Complete** (green) when the run finished, or a red **Failed ·** chip followed by the reason, such as **Failed · identifier not hashed**.
   - **Completed (UTC)**: when the run finished, in UTC.
3. Read the **Source** chip:
   - **You**: you submitted the run.
   - **Agent**: an agency's agent submitted the run. Look for this chip to find agency runs.
   - **BU**: the **Submitted by** column shows the business unit and job function of the person who submitted it.

## Filter the list

1. Click **Filters** to set filters.
2. Each active filter shows as a chip beside the button, such as **Source: Any** for who sent the run, or **Date:** followed by the date range. To filter by date, use the **Date:** filter.
3. To remove one filter, click the × on its chip. To remove every filter, click **Clear all**.
4. The number of matching runs shows at the right of the filter row.

## Open or start a run

- Click a run's name in the **Run** column to open its results page.
- Click **New analysis** at the top right of the **Runs** tab to upload a customer list.

## Good to know

- "Uploaded files are held for the life of the run and dropped at teardown."
- "A failed run keeps its reason on the row so the submitter can fix it."
- Rows have no edit or delete control. Click the run's name to open it, or start a fresh run with **New analysis**.
- Analysis is not available to the Agency role.

Related: Upload a customer list and run an analysis; Read an analysis run's results; Why did my analysis run fail?; Run provenance and agent-submitted runs
