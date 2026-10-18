# Run provenance and agent-submitted runs

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: concept
Category: analysis

A run's provenance is its record of who submitted it, how it was submitted, which business units' data it used and what happened to the file. You find it in the **Provenance** panel on the run's page: Sidebar > **Analysis** > **Runs** > click the run's name.

## What the Provenance panel shows

- **Submitted by**: who ran it. For a run from an agency, this names the agency's agent. The page subtitle also starts "Run by …" with the same submitter.
- **Channel**: how the run was submitted. A run from an agency's agent reads **Credentialed · MCP endpoint**.
- **Units**: which business units' data the run used.
- **File**: **Dropped at teardown**. The uploaded file is held for the life of the run and then dropped.

## Agent-submitted runs

Agencies' agents can submit runs to the layer through a credentialed connection. When the **Channel** reads **Credentialed · MCP endpoint**, an agency's agent sent the run through that connection. The runs list says so in its subtitle: "Runs submitted by agency agents appear here too."

On Sidebar > **Analysis** > **Runs**, the **Source** column tells you where each run came from:

- **Agent**: an agency's agent submitted it.
- **You**: you submitted it.
- **BU**: the **Submitted by** column shows the submitter's business unit and job function.

## Where else agents appear

- **Rules of Use**: when an agent's request involves your unit's fields, it arrives on Sidebar > **Rules of Use** under the **Agent** tab. The card carries the **Agent request · MCP** chip and a **Brief:** line with the agent's request. You decide it there.
- **Delivery**: the **Agent endpoint** panel on Sidebar > **Delivery** summarises the endpoint agents use. It has a **live** chip and figures for **Agents**, **Requests** and **Awaiting you**. The panel reads: "Returns size, composition and delivery options. It never transacts, and nothing is sent until a person approves."

## Why it matters

Provenance answers "who submitted this run?" and "which units' data did it use?" before you act on the results, for example before you click **Build an audience**. Run results are aggregate only and return no identifiers, whoever submitted the run. Nothing leaves until a person in each business unit whose data is involved approves.

Related: View and filter analysis runs; The agent endpoint; Rules of Use: how approvals work; Read an analysis run's results
