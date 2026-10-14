# Delivery destination classes

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /delivery

A delivery sends an Active audience to a destination. Destinations are grouped into four classes, each with its own transport and reporting.

| Class | Destination | How it works | Reporting back |
|---|---|---|---|
| 1 | Your own lake / S3 | Writes to the business unit's own storage | Bidirectional: measurement can be read back |
| 2 | Activation · Permutive | Writes a batch drop to storage, which Permutive ingests on its side | No callback; the CDL waits for an ingest acknowledgement |
| 3 | Curation · Xandr Curate | Pushes the audience for curated deals | Push only; no reporting returns |
| 4 | External system | A federated clean room or planning tool, such as InfoSum | Depends on the vendor |

## Deliver an audience
1. Open **Delivery** and choose the audience and version.
2. Choose a destination class. A Ready badge means the destination is set up for your business unit.
3. Review the permissible-use envelope.
4. Select **Deliver**.

Only Active audiences can be delivered. A delivery to an external system (class 4) also needs approval from every contributing business unit.
