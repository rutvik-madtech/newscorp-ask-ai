# The agent endpoint

Applies to tier: Power User
Business unit: all
Console page: /delivery
Article type: concept
Category: delivery

The agent endpoint is how AI agents, such as an agency's buyer agent, ask the layer about audiences. You see its summary in the **Agent endpoint** panel on Sidebar > **Delivery**, and you decide on agent requests in Sidebar > **Rules of Use**.

## What it does

The panel states: “Returns size, composition and delivery options. It never transacts, and nothing is sent until a person approves.” An agent can ask how big an audience is, what it is made of and where it could go. It can't buy or receive an audience on its own.

## The Agent endpoint panel

The panel sits on the right of the Delivery page, below **Permissible-use envelope**.

- **live**: a green chip in the panel header. The endpoint is live and accepting requests.
- **Agents**: how many agents are using the endpoint.
- **Requests**: how many requests agents have sent, over the recent period named in the label.
- **Awaiting you**: how many agent requests are waiting for your decision.
- **Counts as of …**: the time the figures were taken. They are a snapshot, not a running count.

The panel has no buttons. To act on agent requests, go to **Rules of Use**.

## Where agent requests and runs appear

- **Rules of Use**: an agent's request to use your unit's fields appears under the **Agent** tab with the **Agent request · MCP** chip. The card shows a **Brief:** line with what the agent asked for, **expires in …** with the time left, and an **In plain terms** panel tagged **AI summary**. Click **Review and approve** or **Decline**. In the **Approve request** dialog, the requester is marked **(credentialed, MCP)**.
- **Overview**: agent requests are also listed in **Waiting on you**, starting **Agent request ·** followed by the audience.
- **Analysis**: a run submitted by an agent shows **Credentialed · MCP endpoint** as its **Channel** in the run's **Provenance** panel.

MCP is the credentialed connection agents use to reach the layer.

## Why it matters

- **Can an agent buy an audience without approval?** No. The endpoint never transacts, and nothing is sent until a person in each business unit whose data is involved approves.
- **What does Awaiting you mean?** Agent requests that need a decision from you. Set **Acting as** to your business unit, open **Rules of Use** and choose the **Agent** tab.
- **What if nobody decides?** An expired request lapses and nothing is delivered.

Related: Rules of Use: how approvals work; Run provenance and agent-submitted runs; Find and read a request; Approve a request
