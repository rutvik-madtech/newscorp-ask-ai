# Gating rules

Applies to tier: Power User, Admin
Business unit: all
Console page: /rules-of-use

Gating rules decide what can leave the CDL. Each business unit keeps its own list on the Rules of Use page.

## How rules are evaluated
Rules are evaluated deny-first, from top to bottom; the first deny rule that matches stops the output. In a cross-business-unit output, every contributing business unit's rules apply, and the most restrictive rule wins.

## Example rules
1. **Deny** JOB_TITLE to any external destination. Derived job titles may inform a cohort but never leave as a field.
2. **Deny** any field where consent is opted out. Opted-out records are suppressed at each evaluation.
3. **Allow** aggregate cohort counts to curation.
4. **Allow** matched audiences to a federated clean room.

## Changing rules
Power Users propose a rule change, and an Admin in the same business unit applies it. Changes apply to new deliveries only; deliveries already made keep the envelope they were sent with.
