# Edit a connector's endpoint or refresh frequency

Applies to tier: Power User
Business unit: all
Console page: /admin/connectors
Article type: how_to
Category: admin

You change where a connector reads or writes, and the period within which a feed must send a new file, on the connector's settings page. Go to Sidebar > Admin > **Connectors** and click the connector's name.

## Open a connector's settings

1. In the sidebar, under **Admin**, click **Connectors**.
2. In the **Connector** column, click the connector's name. Its settings page opens, headed with the connector's name. The breadcrumb reads Admin / Connectors / … with the connector's name at the end. Click **Connectors** in the breadcrumb to go back to the list.
3. Read the line at the top of the settings card. It shows the health chip, when the last file arrived and when the connector was last checked, in UTC.

## Change the endpoint

1. In **Endpoint**, edit where the connector reads from or writes to. For a business unit's feed, this is where the unit drops its files. The help text names the unit: "Where … drops its files. Each drop is a dated folder with a completion marker."
2. Click **Save**. You return to the **Connectors** list.

## Change the refresh frequency

1. Open **Refresh frequency** and choose **Daily**, **Weekly** or **Monthly**. The help text reads "The feed is marked Stale if no new file arrives within this period."
2. Click **Save**. You return to the **Connectors** list.

To leave without saving, click **Cancel**. You return to the **Connectors** list.

## Set up a connector that shows Not set up

A **Not set up** connector has no endpoint. On **Connectors**, click its name, enter the **Endpoint** and click **Save**.

## Good to know

- **Only the endpoint and the refresh period are editable.** The settings page has **Endpoint**, **Refresh frequency**, **Cancel** and **Save**.
- **You can't change health here.** Health is set by automatic checks, and "Nobody sets health by hand".
- **A longer period flags later.** Choosing a longer refresh frequency means a feed takes longer to be marked **Stale**.
- **Request upload isn't on this page.** It appears on the **Connectors** list, on a **Stale** row.

Related: Check connector health; Data may be out of date: a feed is Stale; A connector is Failing or Not set up
