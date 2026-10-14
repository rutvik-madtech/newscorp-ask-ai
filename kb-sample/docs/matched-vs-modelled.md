# Matched, modelled and definitional audiences

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /audiences

Every audience size in the CDL says how people got into the audience. The three kinds are kept apart and never added together into one number.

- **Matched**: people matched deterministically on the spine, with exact confidence. A person is matched when a business unit's record links to a Spine ID.
- **Modelled**: people predicted to belong because they look like matched people. Modelled sizes are estimates and are labelled as such everywhere.
- **Definitional**: people who belong by the definition of a term, for example everyone with a declared job title from a given list.

## Why they travel separately
Destinations and measurement treat matched and modelled people differently, and some gating rules allow matched audiences only, such as "Matched audiences to a federated clean room". Keeping them separate keeps those rules enforceable.

## Matched size comes first
The matched size is reported before any extension. If extra reach from a modelling provider is available, it appears as a separate extension figure, with a status that says whether a provider is contracted.
