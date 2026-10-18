# Your gating rules

Applies to tier: Power User
Business unit: all
Console page: /rules-of-use
Article type: concept
Category: rules_of_use

Your gating rules are your business unit's **DENY** and **ALLOW** rules for how its fields may be used and where they may go. You find them in the **Your gating rules** panel on Sidebar > **Rules of Use**, beside the request cards.

## Where you see them

- Sidebar > **Rules of Use**, in the **Your gating rules** panel. The page belongs to the business unit in **Acting as**, named after **Rules of Use ·** in the page title.
- When nothing needs your decision, the empty state **Nothing waiting on you** offers a **Review your gating rules** link. It opens Rules of Use, where the panel sits.

## How to read a rule

Each rule has a number, a chip and a description:

- **DENY** (red chip): a use of your fields the rule stops.
- **ALLOW** (green chip): a use of your fields the rule permits.
- Some rules also have a short note below the description.

A rule can let a field shape who is in an audience while stopping the field itself from being sent. In the **Approve request** dialog, a field used this way is marked **shape the cohort only** under **Your fields used**, and **Fields that leave** can read **None · cohort membership only**.

## How rules are evaluated

The panel states: “Evaluated deny-first, top to bottom. In a cross-BU output the most restrictive contributing rule wins.”

- **Deny-first**: **DENY** rules are checked before **ALLOW** rules, so a use a DENY rule covers is stopped even when an ALLOW rule also matches it. Rules are read in order from the top of the list.
- **Most restrictive wins**: when an output combines fields from more than one business unit, the strictest rule among the contributing units applies.

## Change a rule

The panel shows a **Fixed this phase** chip. You can't edit, add or delete rules on this page. To ask for a change, click **Request a rule change** under the rules.

## Why it matters

Your gating rules set out which uses of your fields are allowed and where they may go, and the console uses them when it explains a request to you:

- **In plain terms** (tagged **AI summary**), on request cards that have it, explains the request and how your gating rules apply. Its **Based on:** line names the rules it used.
- When you decline, **Message sent to the requester** is an **AI draft · edit before sending**: “Drafted from rule … and the reason you picked.”

A person in your unit still makes every decision, with **Review and approve** or **Decline**. “Nothing of yours enters a cross-unit output until a person here approves it.”

Related: Rules of Use: how approvals work; Decline a request; Rules of Use FAQ; Approve a request
