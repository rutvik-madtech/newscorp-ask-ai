# Audience types, precedence and statuses

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: reference
Category: audiences

The **Type**, **Owner**, **Modelled**, **Precedence** and **Status** columns on Sidebar > **Audiences** describe each audience definition. This reference explains each label. The **Type** and **Owner** columns also appear in **Largest definitions** on the Overview.

## Type

| Label | Meaning | Where it appears |
|---|---|---|
| **Single BU** | The definition uses one business unit's data. | **Type** column on Audiences and on the Overview |
| **Cross-BU** | The definition draws on more than one business unit's data. These rows can show a precedence setting. | **Type** column on Audiences and on the Overview |
| **Cross-BU reach** | One business unit's fields decide membership. Other units add reach, not members: some of the matched people can also be reached on another unit. | **Type** column, and the header line of the definition's detail panel |

**Single BU or Cross-BU?** A **Single BU** definition stays within one unit's data. A **Cross-BU** definition combines data from more than one unit, so you may need to say which unit's value wins when they disagree.

## Other columns

| Label | Meaning |
|---|---|
| **Owner** | The business unit that owns the definition, such as Dow Jones or Realtor.com. |
| **Matched** | Matched people, consented and deduplicated on the spine. |
| **Modelled** | The modelled extension, a separate audience that is never summed with matched. A dash (—) means the definition has no modelled extension. |
| **Precedence** | Which business unit's value wins when units disagree, shown as **Region:** followed by the unit, for example **Region: Realtor.com**. A dash means no precedence is set or needed. You choose it in **Precedence when units disagree** on Create an audience. |

## Status

| Label | Colour | Meaning |
|---|---|---|
| **Active** | Green | The definition is live. |
| **Pending you** | Amber | The definition is waiting for action from the business unit you are acting as. Check **Acting as** at the top of the sidebar to see which unit that is. |
| **Insights only** | Grey | The definition is marked for insights only, as the label reads. |

## Row highlight

| Marker | Meaning |
|---|---|
| Blue row | The selected definition. The row stays highlighted while its detail panel is open. |

Related: Precedence when units disagree; Members and reach in cross-unit audiences; Find and filter audience definitions
