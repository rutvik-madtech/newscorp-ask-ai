# Check connector health

Applies to tier: Power User
Business unit: all
Console page: /admin/connectors
Article type: how_to
Category: admin

To check whether your data feeds and connections are working, go to Sidebar > Admin > **Connectors** (breadcrumb Admin / Connectors). The subtitle reads "The feeds and file exchanges the layer depends on. Health is checked automatically." Each connector's state shows in the **Health** column.

## Check health

1. In the sidebar, under **Admin**, look at **Connectors**. A red dot with a number means a connector needs attention.
2. Click **Connectors**.
3. Read the summary line above the table. It shows how many connectors there are, how many need attention and when they were last checked.
4. Read the **Health** column for each connector.
5. To see what each state means, read **What the health states mean** below the table.

## What the columns show

- **Connector**: the connector's name. Click it to open its settings. Connectors include each business unit's feed, such as **Dow Jones feed** and **Realtor.com feed**, **Identity provider · match file out**, **Identity provider · results in**, and the clean room and activation connectors used when audiences are delivered.
- **Direction**: **In** is data coming into the layer, such as a unit's file feed or results returned from the identity provider. **Out** is data the layer sends, such as the match file to the identity provider or a delivery to a clean room or activation destination.
- **Endpoint**: where the connector reads from or writes to.
- **Refresh**: the connector's refresh setting, such as **Weekly**, **On return** or **On delivery**.
- **Last file or success (UTC)**: for a feed, when the last file arrived; for an outbound connector, when it last succeeded. A **Not set up** connector shows a dash (**—**).

## Health states

- **Healthy** (green): "The last check passed and, for feeds, a new file arrived within the refresh period."
- **Stale** (amber): "No new file within the refresh period. Request upload emails the unit’s named contact." The row is highlighted and has a **Request upload** button.
- **Failing** (red): "The last check failed: credentials rejected, endpoint unreachable, or the last job errored."
- **Not set up** (grey): "No endpoint has been entered yet."

## Good to know

- Health is checked automatically. "Nobody sets health by hand", and the page has no control to change it.
- The only settings you can edit are the endpoint and the refresh period. See Edit a connector's endpoint or refresh frequency.
- The page has no control to add or delete a connector.
- The Admin section is for Power Users; the Agency role doesn't see it.

Related: Data may be out of date: a feed is Stale; A connector is Failing or Not set up; Edit a connector's endpoint or refresh frequency
