# Find and read a request

Applies to tier: Power User
Business unit: all
Console page: /rules-of-use
Article type: how_to
Category: rules_of_use

Requests to use your business unit's fields appear as cards on Sidebar > **Rules of Use**. Each card shows who is asking, which of your fields are involved, where the audience would go and whether the system checks passed.

## Find and read a request

1. In the sidebar, set **Acting as** to your business unit, then click **Rules of Use**. The title reads **Rules of Use ·** followed by your unit.
2. To filter the list, click a **Request type** tab: **All**, **Agent**, **Cross-BU** or **Destination**. Each tab shows how many requests it holds. To see only agent requests, click **Agent**.
3. Read the card header: the type chip (**Agent request · MCP**, **Cross-BU output** or **New destination**) and the requester line beside it, which also shows when the request arrived, in UTC.
   - On **Cross-BU output** and **New destination** cards, the requester line shows the requesting business unit and a job function such as **Data steward**. Data steward is a job function, not a console role; the console's roles are Power User and Agency.
   - On agent request cards, it shows **expires in …**, the time left to decide.
4. Read the card body:
   - The audience name. Agent requests add **Brief:** with the agent's request in quotes.
   - **Your fields involved**: which of your unit's fields the request uses.
   - **Destination**: where the output would go and how it is delivered, such as a federated clean room or a batch activation.
   - **Size · at request time**: the matched size when the request was made. It can also say whether an extension is requested, such as **no extension requested**.
   - **System gates · checked …**: the automatic checks and the time they last ran. **All passed** (green) means every check passed at that time.
5. On cards that have it, read **In plain terms**, tagged **AI summary**. It explains the request in plain language and how your gating rules apply. **Based on:** names its sources, such as the request and your gating rules. Rate it under **Was this right?** with **Helpful**, **Wrong facts** or **Outdated**.
6. On a **Cross-BU output** card, read the amber notice that starts **Precedence set by the creator:**. It names the unit whose values win on a dimension and tells you when yours lose, as in “Your … values lose on conflict.”
7. On a **New destination** card, read the line under the audience name: the audience is already approved for one destination class, and the request adds another.
8. Click **Review and approve** or **Decline**.

## Good to know

- The page shows requests for the unit in **Acting as** only. If a request is missing, check **Acting as** and click **All**.
- Every decision is recorded with your name and the time.

Related: Approve a request; Decline a request; Precedence when units disagree; Rules of Use: how approvals work
