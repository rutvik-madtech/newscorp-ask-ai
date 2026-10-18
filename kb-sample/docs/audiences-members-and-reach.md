# Members and reach in cross-unit audiences

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: concept
Category: audiences

A business unit adds members to an audience only if it holds the fields the membership rule uses. A unit without those fields can still add reach: people who resolve on the identity spine to that unit can be reached there. You see this on Sidebar > **Audiences**, in a definition's detail panel, and in **Live sizing** on Create an audience.

## Members and reach

- **Members** are the people who meet the membership rule. Only a unit that holds the rule's fields can supply them.
- **Reach** is the part of those members who also resolve on the spine to another unit. That unit adds no new people, but those members can be reached there too. Reach is part of the matched people, not added to them.

The **Type** column on Audiences shows which case applies:

- **Single BU**: the definition uses one business unit's data.
- **Cross-BU**: members come from more than one business unit.
- **Cross-BU reach**: one unit's fields define the members, and another unit adds reach, not members.

## Where you see it

- **Detail panel**: on Audiences, click a definition's name. Under **Size · as of …**, the text below the size cards says which unit's fields define the audience (“Defined by … fields”), how many of the matched people are also reachable on another unit, and that the other unit “adds reach, not members”.
- **Live sizing**: on Create an audience, the panel reads “… contributes all members (declared). … are also reachable on …”. The phrase “contributes all members (declared)” means the named unit supplies every member of the audience. The next sentence says how many of those members can also be reached on another unit.

## Why another unit adds no members

On Sidebar > **Taxonomy**, open the term and read **How each business unit maps to it**. A unit with no matching fields shows **No equivalent** in the **Mapping** column, and its **Source fields** cell says why. The section states: “A unit with no equivalent is marked, never approximated.” The console never fills the gap with a proxy, so that unit can only add reach.

## Ask AI about a definition

When you open **Ask AI** from Audiences, the **Try asking** list can include “Why is Realtor.com shown as reach, not members?”. The answer covers the definition in scope: which fields the membership rule uses, which unit supplies them, how many members resolve on the spine to people also seen on the other unit, and whether that unit is marked **No equivalent**.

Related: Check and edit how business units map to a term; The identity spine; Open an audience definition: rule, size and gates
