# Connectors

Applies to tier: Admin
Business unit: all
Console page: /admin/connectors

Connectors link the CDL to a business unit's data sources and destinations. Find them in **Admin › Connectors**.

## Source connectors
A source connector loads a business unit's data into the CDL, for example a nightly export from the business unit's warehouse. Each source has a schedule, a mapping from its fields to taxonomy terms, and a last-run status.

## Destination connectors
A destination connector sets up one destination class for a business unit: the storage location for Your own lake / S3 and for Permutive drops, the seat ID for Xandr Curate, or the vendor account for an external clean room. A destination shows Ready on the Delivery page only after its connector passes a test.

## Agent credentials
Agent credentials let a credentialed agent call the agent endpoint. Create one per agent, set an expiry date, and revoke it here when the agency relationship ends.
