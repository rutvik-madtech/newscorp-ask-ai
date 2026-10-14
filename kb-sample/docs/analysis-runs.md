# Run an analysis on a customer file

Applies to tier: Power User, Admin, Agency
Business unit: all
Console page: /analysis

Analysis shows who is in a customer or campaign file and what they look like, using the CDL's data, without sending the file's records anywhere.

## Start a run
1. Open **Analysis** and select **New analysis**.
2. Upload a CSV file with one identifier column: hashed email (SHA-256 of the lowercased address), ID5 ID or LUID. Other columns are ignored.
3. Name the run and select **Start**. Files of up to 5 million rows are supported.

Credentialed agents can also submit runs through the agent endpoint. Those runs show "via MCP endpoint" as the source.

## Reading the results
- **Matched**: rows that matched a person on the spine.
- **Composition**: the attributes most common among matched people. Each row shows the attribute, its source (for example "Dow Jones · declared"), the share of matched people who have it, and an **index**: how much more common it is than among everyone the campaign reached. An index of 1.0 is average; 2.3 means 2.3 times as common.
- **Extension**: extra reach a modelling provider could add. "Provider not contracted" means extension isn't available yet.
- **Provenance**: who submitted the run and how, which business units contributed, and what happened to the file.

Agency users see their own runs. Composition rows from obfuscated sources show "Contributing business unit" instead of the business unit's name.

## What happens to your file
The uploaded file is used only for matching and is dropped at teardown, when the run finishes. If a run shows "Teardown incomplete", the file is still deleted automatically within 24 hours; tell your Admin if it stays.

## Why a run fails
A run fails validation when the file has no recognised identifier column, contains unhashed emails, or matches fewer people than the minimum population. The run detail shows the reason.
