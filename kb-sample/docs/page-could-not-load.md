# A page or panel couldn't load

Applies to tier: Power User
Business unit: all
Console page: /
Article type: troubleshooting
Category: overview

When part of a page can't load, the console shows a red alert in its place, for example **Couldn’t load delivery history** on the Delivery page. Click **Try again** in the alert. The last data that loaded stays visible below it, marked as possibly out of date.

## Symptom: a red "Couldn’t load …" alert

**What you see:** A red alert headed, for example, **Couldn’t load delivery history**, with the text "This is usually temporary. The last successful load is shown below, marked as possibly out of date." and the buttons **Try again** and **Notify connector owner**.

**Why it happens:** The console couldn't load that data this time. The alert itself says this is usually temporary.

**What to do:**

1. Click **Try again**.
2. If it still fails, click **Notify connector owner** to alert the person responsible for the connector behind the data.

## Symptom: the data under the alert may be old

**What you see:** Rows or figures below a load-failure alert.

**Why it happens:** They are the last successful load, kept on screen while the current data can't load.

**What to do:** Treat them as possibly out of date, not as current. Click **Try again** to load the data again.

## Symptom: grey bars instead of content

**What you see:** Grey placeholder bars where text, figures or a table should be.

**Why it happens:** The content is still loading. This is not an error.

**What to do:** Wait for the content to fill in. If a red **Couldn’t load …** alert appears instead, follow the steps above.

## Not the same problem

- **An amber banner that starts "Data may be out of date."** The page loaded, but a source's latest data is older than its freshness limit. See Data may be out of date: a feed is Stale.
- **A red alert on Delivery saying a delivery did not reach its destination**, with **Retry** and **Notify connector owner**. That is a failed delivery, not a load failure. See Fix a failed delivery.

Related: Data may be out of date: a feed is Stale; A connector is Failing or Not set up; Fix a failed delivery
