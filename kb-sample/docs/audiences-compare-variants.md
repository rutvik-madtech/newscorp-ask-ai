# Compare audience variants and send one for approval

Applies to tier: Power User
Business unit: all
Console page: /audiences
Article type: how_to
Category: audiences

The Variants page compares versions of the same seed audience and lets you send one for approval. From the Extension page of From a seed, click **Compare variants** (breadcrumb **Audiences / From a seed / Variants**). The subtitle reads “Built from one definition, differing only in how far the extension reaches. Pick one, or take more than one to test in flight.”

## Compare and send a variant

1. On the Extension page, click **Compare variants**.
2. Read the variant cards, such as **A · Matched only**, **B · Close extension** and **C · Wide extension**. Each card shows:
   - a status chip: **Selected** or **Draft**
   - the matched figure, with a note such as **No modelling applied** or **Matched and modelled reported apart**
   - **Composition**, for example **Deterministic core, close modelled ring**
   - **Approval needed**: which business units must approve
   - **Provider needed**: **Spine only** or **Spine and model · not contracted**
3. Read **What separates them**:
   - **Reach**: **Smallest**, **Larger**, **Largest**
   - **Resemblance to the seed**: **Exact**, **High**, **Lower**
   - **Claim you can make**: “These are your customers” for matched only, “These resemble your customers” for extended variants
   - **Performance evidence**: **After flight** for every variant
4. Choose the variant you want to send. Its card shows **Selected** and a highlighted border.
5. Click the **Send variant … for approval** button, which names the selected variant. Each business unit whose data is involved gets a request in Sidebar > **Rules of Use**.

## Good to know

- Which variant performs best? The console does not say before a variant has run: “No variant is described as better before it has run. The console reports the difference, it does not rank them.” Performance evidence comes **After flight**.
- Can I test more than one variant? The subtitle says you can “take more than one to test in flight”. The send button on the page sends the selected variant.
- Variants that need a modelling provider show **Draft** while no modelling provider is signed. The note beside the send button says they stay as drafts until one is signed.
- An approval covers one variant. The request reads “Approving this covers this audience, this destination and this variant.”
- Nothing leaves until a person in each business unit whose data is involved approves. “Nothing is delivered on a timeout, and an expired request lapses rather than passing.”

Related: Extend a matched audience; Run the final checks and deliver a seed audience; Review a delivery request
