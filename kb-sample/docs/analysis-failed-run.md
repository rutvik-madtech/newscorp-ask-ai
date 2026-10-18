# Why did my analysis run fail?

Applies to tier: Power User
Business unit: all
Console page: /analysis
Article type: troubleshooting
Category: analysis

When an analysis run fails, Sidebar > **Analysis** > **Runs** shows a red **Failed ·** chip in the **Status** column, with the reason after it. "A failed run keeps its reason on the row so the submitter can fix it." Find your symptom below.

## The status reads Failed · identifier not hashed

**What you see:** a red **Failed · identifier not hashed** chip in **Status**.

**Why it happens:** the file's identifier column held unhashed values. An analysis needs a hashed identifier, such as a hashed email.

**What to do:** fix the file so the identifier column holds hashed values. Then start a new run: Sidebar > **Analysis** > **Runs** > **New analysis**, map the columns and click **Run analysis**.

## Matched shows a dash

**What you see:** a dash (—) in the **Matched** column instead of a figure.

**Why it happens:** the run failed, so it has no match result.

**What to do:** read the reason in **Status** on the same row, fix the file and run it again with **New analysis**.

## There's no retry button on the failed run

**What you see:** the failed row offers no retry or re-run control.

**Why it happens:** the runs list offers no retry on a row. A failed run keeps its reason on the row so the submitter can fix it.

**What to do:** to re-run a failed analysis, click **New analysis** and upload the corrected file.

## Someone else's run failed

**What you see:** a failed run with the **Agent** or **BU** source chip.

**Why it happens:** another submitter sent the run. **Submitted by** shows who.

**What to do:** the reason stays on the row so that submitter can fix it and run it again.

## Avoid a failed run

Before you click **Run analysis** in **Upload a file**:

- Check the helper text under **Identifier column**. It says what was detected, for example "Detected as hashed email, SHA-256".
- Make sure **Region declared** is set. Its helper text reads **Required · drives the consent regime**.
- Check that **Conversion time** points at a timestamp column (**Timestamp · ISO 8601**).

Related: What your analysis file needs; Upload a customer list and run an analysis; View and filter analysis runs
