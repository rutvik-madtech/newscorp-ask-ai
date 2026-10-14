# Approve or decline requests in Rules of Use

Applies to tier: Power User, Admin
Business unit: all
Console page: /rules-of-use

Rules of Use is where a business unit decides how others may use its data. The Requests tab lists everything waiting for your business unit.

## Request types
- **Agent**: a credentialed agent, such as an agency's buyer agent, asked for an audience through the agent endpoint. Shown as "via MCP endpoint".
- **Cross-BU**: another business unit wants to use your fields in its audience, for example Realtor.com asking to use your fields in "High-net-worth households".
- **Destination**: a business unit wants to send an already approved audience to a new destination class.

Each request shows the fields involved, the destination, the audience size (matched and modelled) and whether its gates passed. Urgent requests are highlighted. Agent requests expire after 48 hours.

## Approve a request
Check the fields, the destination and the precedence, then select **Approve**. An approval covers that audience version and destination only.

## Decline a request
Select **Decline** and choose a reason, such as "Fields not approved for this destination" or "Precedence not acceptable". The reason is sent to the requester and nothing is delivered. You can edit the prefilled message; the reason "Other" needs a message.

Every approval and decline is written to the audit trail with the actor, time and scope.
