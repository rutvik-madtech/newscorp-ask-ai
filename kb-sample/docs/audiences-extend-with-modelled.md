# Extend a matched audience

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

Extending adds lookalikes to a seed audience: people who resemble the matched group, found by the licensed provider's model. From the seed match results (Sidebar > **Audiences** > **From a seed**), click **Look at extension**. The heading reads “Extension, kept in its own column” (breadcrumb **Audiences / From a seed / Extension**), and **Extend** is highlighted in **Progress**.

The people in the extension are not the advertiser's customers, and the matched and modelled figures are never added together.

## Extend the audience

1. On the match results, click **Look at extension**.
2. Check for the **Provider not contracted** banner. It reads “Extension cannot run until an identity and modelling provider is signed. Sizes below are shown as placeholders, not estimates.”
3. Under **The two audiences, side by side**, compare:
   - **Matched · deterministic**: “Known to both the advertiser and the portfolio”.
   - **Modelled · provider’s method**: “Resemble the matched group. Not customers.”
4. Under **How far to extend**, move the **Similarity threshold** slider toward **Closer · smaller** or **Wider · larger**.
5. Check the details below the slider:
   - **Model**: **Provider’s own · not built here**
   - **Trained on**: **The matched group only**
   - **Seed rows sent to the provider**: **None**
   - **Eligibility on the extension**: **Same rule as the matched group**
6. Click **Compare variants** to compare versions side by side before you commit.

## Good to know

- What does the similarity threshold do? It sets how far the extension reaches. “A wider extension reaches more people and resembles the seed less.” Closer gives a smaller audience that is more like the seed.
- Why can't I run an extension? While the **Provider not contracted** banner shows, no identity and modelling provider is signed, so extension cannot run and modelled sizes are placeholders, not estimates. On the Variants page, extended variants show **Draft** for the same reason.
- Extension is optional. The matched-only variant on the Variants page needs **Spine only**, so you can go ahead with the matched audience on its own.
- Are seed rows sent to the modelling provider? No. **Seed rows sent to the provider** reads **None**, and the model is trained on the matched group only.
- Matched and modelled are delivered as separately labelled audiences. “No screen anywhere shows a single combined total.”

Related: Compare audience variants and send one for approval; Matched and modelled audiences; Can't deliver or send an audience
