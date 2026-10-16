# Ask AI demo app

A small Streamlit page for showing Ask AI to the team. It sends each question to the `askai-poc` Lambda exactly as the portal backend will (question, role, business unit) and shows Claude's answer, the pages it cited and what it searched.

**It answers from the sample docs in `kb-sample/docs`, not real CDL documentation.**

## Run it

You need Python 3.10 or later and AWS credentials that may invoke the function.

```bash
cd kb-sample/demo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
AWS_PROFILE=<your-profile> streamlit run app.py
```

The page opens at http://localhost:8501. Run it from this folder so Streamlit picks up `.streamlit/config.toml`, which hides its developer toolbar.

| Variable | Default | What it sets |
|---|---|---|
| `AWS_PROFILE` | your default profile | Which AWS credentials to use |
| `AWS_REGION` | `us-east-1` | The function's region |
| `ASKAI_FUNCTION` | `askai-poc` | The function's name |

The credentials only need this permission:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "lambda:InvokeFunction",
    "Resource": "arn:aws:lambda:us-east-1:<account-id>:function:askai-poc"
  }]
}
```

Run it on your own laptop and share your screen. Don't start it with `--server.address 0.0.0.0`: anyone who can reach the page would ask questions with your AWS credentials.

## The two views

- **Ask:** a chat. Pick a role and business unit in the sidebar, then type a question or select a sample. Each question is answered on its own; Ask AI doesn't remember earlier ones.
- **Compare:** one question asked for every role, or in every business unit, side by side. **What Ask AI searched** is open in each column, so you can see which pages each user's search returned.

Each answer takes 5–15 seconds and costs a few cents in Bedrock.

## A five-minute demo

1. **A how-to.** Ask view, Power User, Dow Jones: "How do I approve a request from Realtor.com?" Ask AI gives the steps from the Rules of Use page and cites it.
2. **The same question as Agency.** Switch the role to Agency and ask again. Ask AI says Agency users can't approve requests, citing What each role can see. Open **What Ask AI searched**: the Rules of Use page isn't there, because the search never returns it for Agency.
3. **Side by side.** Compare view, demo "Approving requests, by role", **Run**. Power User and Admin find the Rules of Use page; Agency doesn't.
4. **Business units.** Demo "Realtor.com signals, by business unit". The Realtor.com column lists the three signals; the Dow Jones column says the docs it can see don't list them.
5. **What it won't do.** Ask view: "How many people are in my C-suite audience?" (it can't see live data and points to the Audiences page), then "Write me a poem about data" (declined without a search).
