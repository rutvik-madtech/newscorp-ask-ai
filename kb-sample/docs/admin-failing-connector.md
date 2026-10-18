# A connector is Failing or Not set up

Applies to tier: Power User
Business unit: all
Console page: /admin/connectors
Article type: troubleshooting
Category: admin

On Sidebar > Admin > **Connectors**, **Failing** means a connector's last automatic check failed, and **Not set up** means it has no endpoint. For either, click the connector's name, check or enter the **Endpoint**, and click **Save**.

## Symptom: Health shows Failing

**What you see:** A red **Failing** chip in the connector's **Health** column.

**Why it happens:** "The last check failed: credentials rejected, endpoint unreachable, or the last job errored."

**What to do:**

1. Click the connector's name in the **Connector** column to open its settings.
2. Check that **Endpoint** is correct, and edit it if it isn't.
3. Click **Save**.

If the cause may be credentials: the settings page has only **Endpoint** and **Refresh frequency**, with no field for credentials. Where **Notify connector owner** appears, click it to alert the person responsible for the connector. It appears on the red banner for a failed delivery on **Delivery**, and on load-failure alerts such as **Couldn’t load delivery history**.

## Symptom: Health shows Not set up

**What you see:** A grey **Not set up** chip, and a dash (**—**) in **Last file or success (UTC)**.

**Why it happens:** "No endpoint has been entered yet." A connector that is **Not set up** shows a dash in **Last file or success (UTC)** instead of a time.

**What to do:**

1. Click the connector's name to open its settings.
2. Enter the **Endpoint**.
3. Click **Save**.

## Symptom: Health hasn't changed after you saved

**What you see:** The connector still shows **Failing** or **Not set up** after you click **Save**.

**Why it happens:** Health is checked automatically, and "Nobody sets health by hand". Saving the settings doesn't set health; it updates on the next automatic check.

**What to do:** Wait for the next check. The summary line on **Connectors** shows when the connectors were last checked, and the top of a connector's settings page shows when that connector was last checked, in UTC.

Related: Check connector health; Fix a failed delivery; A page or panel couldn't load
