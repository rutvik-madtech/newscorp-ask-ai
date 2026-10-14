# Troubleshooting a delivery

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /delivery

The Deliveries list on the Delivery page shows each delivery's status.

| Status | Meaning | What to do |
|---|---|---|
| In flight | The delivery is being written or pushed | Wait. Most deliveries finish within 30 minutes |
| Delivered | The destination has the audience | Nothing |
| Held — approval | A contributing business unit hasn't approved this use yet | Ask that business unit to act on the request in Rules of Use |
| Failed | The delivery didn't complete | Open the delivery to see the reason |

## Common failures
- **"No ingest acknowledgement after 45 minutes" (Permutive):** the batch drop was written to storage, but Permutive didn't confirm the ingest. Permutive uses batch transport with no callback, so the CDL can't tell why. Check with Permutive that the drop was picked up, then select **Retry**.
- **"Destination not configured":** the destination class isn't set up for your business unit. An Admin can add it in Connectors.
- **"Envelope rejected":** the destination doesn't accept the envelope, for example because it needs a retention period longer than 30 days. Choose another destination class.

Retrying a delivery sends the same audience version again. It doesn't pick up taxonomy changes made since.
