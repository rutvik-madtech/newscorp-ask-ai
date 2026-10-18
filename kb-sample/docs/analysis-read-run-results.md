# Read an analysis run's results

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: how_to
Category: analysis

To read a run's results, go to Sidebar > **Analysis** > **Runs** and click the run's name. The run page (breadcrumb **Analysis / Run …**) shows how much of the list matched, who the matched people are, an AI summary and the run's provenance.

## Read the results

1. Open the run. The subtitle reads "Run by …" followed by the submitter, the date and time in UTC, **complete** and "all figures as of completion". The figures are a snapshot taken when the run completed.
2. Read the cards at the top:
   - **Supplied**: the rows in the uploaded file. The caption "rows in …" names the file.
   - **Matched**: how many rows matched, with their share of the file and "deterministic on the spine", meaning an exact identifier match on the identity spine.
   - **Not matched**: rows with "no resolvable identity".
3. Read **Composition**, captioned "Index against everyone the campaign reached". For each **Attribute**:
   - **Source**: the business unit the attribute comes from, followed by **declared** or **behavioural**. **Resolved on the spine** means one person with attributes from more than one business unit.
   - **Of matched**: the share of matched people who have the attribute.
   - **Index**: how over- or under-represented the attribute is among your matched people, compared with everyone the campaign reached.
   - **Suppressed** (with a lock icon) replaces the **Of matched** and **Index** values when the attribute falls below the minimum population.
4. Read **What this run shows**, marked **AI summary**. It summarises the Composition table only ("Based on: the composition table above · run … only"). Next to **Was this right?**, click **Helpful**, **Wrong facts** or **Outdated**.
5. Check **If you build an audience**. It shows **Matched only** and, separately, **With extension · not contracted**: "Never summed. Matched size is stated before any extension, wherever the audience goes."
6. Check **Provenance** for **Submitted by**, **Channel**, **Units** and **File**.

## Export or build an audience

- To export the results, click **Export** at the top right of the run page.
- To turn the run into an audience, click **Build an audience**. **Create an audience** opens.
- To go back to the list, click **Analysis** in the breadcrumb.

## Good to know

- The note under Composition reads: "Aggregate only, gated by minimum population. No identifiers are returned. Conversions and attribution stay with the advertiser."
- Why is an attribute **Suppressed**? Its group falls below the minimum population, so it is suppressed with no value.
- Matched and modelled figures are never added together.

Related: Build an audience from an analysis run; Run provenance and agent-submitted runs; Minimum population and suppressed figures; Work with AI suggestions and AI summaries
