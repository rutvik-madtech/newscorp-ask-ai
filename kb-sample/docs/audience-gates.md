# Audience gates

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /audiences

Gates are the checks every audience must pass before it can be delivered. The audience detail panel lists each gate with its status.

| Gate | What it checks | If it doesn't pass |
|---|---|---|
| Minimum population | The audience has at least 1,000 matched people. A business unit can set a higher floor | The size shows "Below minimum" and the audience can't be sent for approval. Widen the conditions |
| Consent | Everyone in the audience has a consent state that allows this use, for example "US · not opted out" | People without a valid consent state are removed. If too few remain, the minimum population gate fails |
| Business unit approval | Each business unit whose data contributes has approved the use, for example "Realtor.com approval" | The gate shows Requested until that business unit approves in Rules of Use |
| Source obfuscation | Contributing business units are hidden from destinations and from Agency users | On by default for Cross-BU audiences. Only the contributing business units can turn it off |

## Why is my audience held?
An audience that passes every gate except business unit approval stays in Pending approval, and a delivery of it shows "Held — approval" until the approval arrives. Approval requests expire if nobody acts within 48 hours; you can send the request again from the audience.
