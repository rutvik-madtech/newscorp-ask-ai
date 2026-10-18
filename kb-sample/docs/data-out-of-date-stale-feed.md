# Data may be out of date: a feed is Stale

Applies to tier: Power User
Business unit: all
Console page: /admin/connectors
Article type: troubleshooting
Category: admin

When a business unit's feed stops sending new files, the console warns that data may be out of date and the feed shows **Stale** on Sidebar > Admin > **Connectors**. To chase the missing file, click **Request upload** on the feed's row.

## Symptom: a "Data may be out of date." banner

**What you see:** An amber banner on a page that starts **Data may be out of date.** It names a data source, says when that source's data last arrived compared with its freshness limit, and when an upload was requested.

**Why it happens:** The source's latest data is older than its freshness limit because no new file has arrived. Figures that depend on that source may lag.

**What to do:** Go to Sidebar > Admin > **Connectors**, find the feed that shows **Stale**, and follow the next section.

## Symptom: a feed shows Stale on Connectors

**What you see:** On Sidebar > Admin > **Connectors**, the feed's **Health** shows **Stale** (amber) and its row is highlighted. In the sidebar, **Connectors** shows a red dot with a number, meaning a connector needs attention.

**Why it happens:** "No new file within the refresh period." The business unit that owns the feed, for example Dow Jones or Realtor.com, hasn't dropped a new file within the period set in the feed's **Refresh frequency**.

**What to do:**

1. On **Connectors**, find the **Stale** row.
2. Click **Request upload** at the right of that row. "Request upload emails the unit’s named contact."
3. Wait for the unit to drop a new file.

## Symptom: the feed still shows Stale

**What you see:** The feed keeps showing **Stale** after you click **Request upload**.

**Why it happens:** Health is checked automatically, and "Nobody sets health by hand". The feed shows **Healthy** again on a later check, once a new file has arrived: "The last check passed and, for feeds, a new file arrived within the refresh period."

**What to do:** Wait for the new file and the next automatic check. The summary line on **Connectors** shows when the connectors were last checked.

## Symptom: the expected period is wrong

**What you see:** A feed is marked **Stale** because its expected period doesn't match how often its business unit sends files.

**Why it happens:** The feed's **Refresh frequency** sets that period: "The feed is marked Stale if no new file arrives within this period."

**What to do:** On **Connectors**, click the feed's name. In **Refresh frequency**, choose **Daily**, **Weekly** or **Monthly**, then click **Save**.

Related: Check connector health; Edit a connector's endpoint or refresh frequency; A page or panel couldn't load
