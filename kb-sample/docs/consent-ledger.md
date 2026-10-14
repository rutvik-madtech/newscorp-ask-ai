# Consent ledger

Applies to tier: Power User, Admin
Business unit: all
Console page: /admin/consent-ledger

The consent ledger records the consent state of every person the CDL holds, per business unit and per jurisdiction.

## Consent states
- **Not opted out (US)**: the person hasn't opted out of sale or sharing under US state privacy laws.
- **Consented (AU, UK)**: the person gave consent under the applicable law.
- **Opted out**: the person opted out. Their records are suppressed by the gating rules and never used in an audience.
- **Unknown**: there is no consent record. Treated as opted out.

## How the ledger is used
Every audience's Consent gate, and every delivery's consent basis, comes from the ledger. When a person opts out, the next gating evaluation removes them from audiences. Deliveries already made aren't recalled, but the opt-out is passed on to destinations that support it.

## Reading the ledger
The ledger shows counts per state and recent changes. It never shows individual records.
