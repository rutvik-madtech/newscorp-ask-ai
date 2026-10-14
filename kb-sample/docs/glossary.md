# Glossary

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /taxonomy

**Composable Data Layer (CDL)**: News Corp's shared data layer, where business units combine audience data under rules each one controls.

**Business unit (BU)**: a News Corp business that contributes data to the CDL, such as Dow Jones or Realtor.com.

**Spine**: the licensed identity graph the CDL uses to recognise the same person across business units. The spine is built on the Experian graph.

**Spine ID**: the CDL's identifier for one person on the spine. Matching links a business unit's record to a Spine ID.

**LUID**: a business unit's local user ID. Accepted as an identifier column in Analysis files.

**ID5**: a shared, privacy-preserving advertising identifier. Accepted in Analysis files and used to link records to the spine.

**Matched, Modelled, Definitional**: how a person got into an audience. Matched people are linked on the spine with exact confidence; modelled people are predicted; definitional people belong by a term's definition.

**Single BU, Cross-BU, From a seed**: the three audience types. A Cross-BU audience combines data from two or more business units; a From a seed audience starts from an analysed customer file.

**Precedence**: in a Cross-BU audience, the business unit whose value wins when two sources assert facts that can't both be true.

**Gate**: a check an audience must pass before it can be delivered, such as Minimum population or Consent.

**Minimum population**: the smallest audience size the CDL will report or deliver. Smaller sizes show as "Below minimum".

**Source obfuscation**: hiding which business units contributed to an audience, from destinations and from Agency users.

**Permissible-use envelope**: the rules recorded with each delivery, such as consent basis and retention at the destination.

**Destination class**: one of four kinds of destination: your own lake or S3, activation, curation, or an external system.

**Index**: how much more common an attribute is among matched people than among everyone a campaign reached. 1.0 is average.

**Extension**: extra reach a modelling provider could add, always reported separately from the matched size.

**Teardown**: the end of an analysis run, when the uploaded file is dropped.

**Insights only**: an audience that can be analysed but not delivered.

**Agent endpoint (MCP)**: the machine-readable interface that credentialed AI agents use to query the CDL.

**Consent ledger**: the record of every person's consent state, per business unit and jurisdiction.

**Role**: Power User, Admin or Agency. Your role decides which pages and details you can see.
