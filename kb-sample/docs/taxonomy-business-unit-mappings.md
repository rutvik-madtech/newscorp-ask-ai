# Check and edit how business units map to a term

Applies to tier: Power User
Business unit: all
Console page: /taxonomy
Article type: how_to
Category: taxonomy

Every canonical term shows how each business unit's own data feeds it. Open the term on Sidebar > **Taxonomy** and scroll to **How each business unit maps to it**. You edit your own unit's mapping from the same section.

## Check the mappings

1. In the sidebar, click **Taxonomy**, then click the term in the canonical list.
2. Scroll to **How each business unit maps to it**. The help text reads "Each unit transforms its own fields into the canonical form. A unit with no equivalent is marked, never approximated. Local taxonomies are not modified."
3. Read the row for each unit:
   - **Business unit**: the unit the row is about.
   - **Local term**: the unit's own name for the equivalent term.
   - **Source fields**: the unit's data fields the mapping uses.
   - **Derivation**: how the value is obtained, for example whether it is declared and which record it comes from.
   - **Mapping**: **Mapped** or **No equivalent**.

For a quick summary, **Contributing units** at the top of the term shows how many units are mapped out of all units.

## What the Mapping chips mean

- **Mapped** (green): the unit's local term is transformed into the canonical term and feeds it.
- **No equivalent** (grey): the unit has nothing that matches the term. **Local term** and **Derivation** show a dash (—), and **Source fields** says why. The unit is marked, never approximated with a proxy.

So if Realtor.com shows **No equivalent** for a term, Realtor.com holds no local term or fields that match it. Read its **Source fields** cell for the reason.

## Edit your unit's mapping

1. At the top of the sidebar, set **Acting as** to your business unit.
2. Click **Taxonomy** and open the term.
3. Under **How each business unit maps to it**, click the edit button named after your unit, for example **Edit Dow Jones mapping**.

## Good to know

- The edit button names the unit in **Acting as**. It is the only edit button in the section; the other units' rows have no edit button.
- Editing is for Power Users ("internal · can edit"). Agency users cannot change the taxonomy.
- A mapping never modifies the unit's local taxonomy, which stays under **Local · read only**.
- Changes to a term or its mappings show as new versions in **Version history**. Delivered audiences stay pinned to the version that produced them.

Related: Term versions and comparing them; Members and reach in cross-unit audiences; Taxonomy FAQ
