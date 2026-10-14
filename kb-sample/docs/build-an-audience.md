# Build an audience

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /audiences

An audience is a group of people defined from taxonomy terms, for example "C-suite decision-makers". You build it on the Audiences page, check its gates and send it for approval before it can be delivered.

## Steps
1. Open **Audiences** and select **Build an audience**.
2. Choose the audience type:
   - **Single BU** uses only the selected business unit's data.
   - **Cross-BU** combines data from two or more business units.
   - **From a seed** starts from a customer file analysed in Analysis and finds similar people.
3. Add conditions from the taxonomy, such as "Job function is Finance" and "Company size is 50+ employees".
4. For a Cross-BU audience, set **precedence**: which business unit's value wins when two sources assert facts that can't both be true. Precedence is recorded with the audience and attributed to you. It only resolves attribute values; it says nothing about where the audience may be activated.
5. Review the sizes. Matched and modelled sizes are shown separately.
6. Check the gates in the detail panel.
7. Select **Save**. The audience is saved as Draft.
8. Select **Send for approval**. Only Draft audiences can be sent for approval.

Agency users can build Single BU audiences from data shared with their agency. Cross-BU audiences are built by Power Users and Admins.

## Audience statuses
| Status | Meaning |
|---|---|
| Draft | Saved but not sent for approval. You can still edit it |
| Pending approval | Waiting for the business units whose data it uses |
| Pending you | Another business unit wants to use your data in it. Act on it in Rules of Use |
| Active | Approved and ready to deliver |
| Insights only | Can be analysed but not delivered, usually because approval was limited to insights |

## Duplicating an audience
Only Active or Pending approval audiences can be duplicated. The copy starts as Draft and uses the latest taxonomy versions.
