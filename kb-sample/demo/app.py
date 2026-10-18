"""Ask AI demo: a small Streamlit front end for the askai-poc Lambda.

Run it with AWS credentials that may invoke the function:
    AWS_PROFILE=<profile> streamlit run app.py

Optional environment variables:
    ASKAI_FUNCTION  the Lambda function name (default askai-poc)
    AWS_REGION      the function's region (default us-east-1)
    APP_PASSWORD    a password the page asks for first (the hosted demo sets it)
"""
import hmac
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import PurePosixPath

import boto3
import streamlit as st
from botocore.config import Config

FUNCTION_NAME = os.environ.get("ASKAI_FUNCTION", "askai-poc")
REGION = os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION") or "us-east-1"

ROLES = ["Power User", "Agency"]
# The "Acting as" choices each role has in the console.
ACTING_AS = {"Power User": ["Dow Jones", "Realtor.com"], "Agency": ["News Corp portfolio", "Realtor.com"]}

SAMPLE_QUESTIONS = [
    "How do I approve a request?",
    "Where do I see why a delivery failed?",
    "What does Suppressed mean?",
    "How do I request a portfolio audience?",
    "How do I give someone access to the console?",
    "I forgot my password",
    "How many people are in my audience?",
    "Write me a poem about data",
]

# Each preset asks the same question as each role, side by side, to show the role filter.
COMPARE_PRESETS = {
    "Approving a request": "How do I approve a request?",
    "Requesting an audience": "How do I request a portfolio audience?",
    "Giving someone access": "How do I give someone access to the console?",
    "Your own question": "",
}


@st.cache_resource
def lambda_client():
    # An answer can take up to the function's 2-minute timeout. No retries, so a slow answer never runs twice.
    return boto3.client("lambda", region_name=REGION,
                        config=Config(read_timeout=150, retries={"total_max_attempts": 1}))


def ask(question, role, bu):
    """Send one question to the Lambda, exactly as the portal backend will."""
    started = time.time()
    try:
        response = lambda_client().invoke(
            FunctionName=FUNCTION_NAME,
            Payload=json.dumps({"question": question, "role": role, "bu": bu}).encode(),
        )
        result = json.loads(response["Payload"].read())
        if response.get("FunctionError"):
            result = {"error": result.get("errorMessage", "The function failed. See its CloudWatch logs.")}
    except Exception as e:  # missing credentials, no permission, network
        result = {"error": f"Couldn't call {FUNCTION_NAME}: {e}"}
    result["seconds"] = round(time.time() - started, 1)
    return result


def show_result(result, expand_searches=False):
    if result.get("error"):
        st.error(result["error"])
    else:
        # Streamlit reads $...$ as maths, so escape dollar signs in Claude's answer.
        st.markdown(result.get("answer", "").replace("$", "\\$"))

    searches = result.get("searches") or []
    sources = result.get("sources") or []
    st.caption(f"{result['seconds']} s · {len(searches)} search{'' if len(searches) == 1 else 'es'}")
    if sources:
        with st.expander(f"Sources cited ({len(sources)})"):
            for s in sources:
                st.markdown(f"- **{s['title']}** · `{PurePosixPath(s['source']).name}`")
    if searches:
        with st.expander("What Ask AI searched", expanded=expand_searches):
            for s in searches:
                st.markdown(f"“{s['query']}” returned:")
                st.markdown("\n".join(f"{i}. {title}" for i, title in enumerate(s["found"], 1)))


def require_password():
    """On the hosted demo, ask for the team password before anything else. Local runs have none set."""
    password = os.environ.get("APP_PASSWORD")
    if not password or st.session_state.get("signed_in"):
        return
    st.title("Ask AI demo")
    entered = st.text_input("Team password", type="password")
    if entered and hmac.compare_digest(entered.encode(), password.encode()):
        st.session_state.signed_in = True
        st.rerun()
    if entered:
        st.error("That password isn't right.")
    st.stop()


st.set_page_config(page_title="Ask AI demo", page_icon="💬", layout="wide")
require_password()

with st.sidebar:
    st.title("Ask AI")
    mode = st.radio("View", ["Ask", "Compare"], horizontal=True)
    st.subheader("Signed in as")
    role = st.selectbox("Role", ROLES)
    bu = st.selectbox("Acting as", ACTING_AS[role], key=f"acting-as-{role}")
    if mode == "Ask" and st.button("Clear conversation", width="stretch"):
        st.session_state.history = []
    st.divider()
    st.markdown(
        "**How it works.** Claude searches the console's help articles through one tool, `search_product_docs`. "
        "Every search is filtered to the articles the role may see, so restricted articles never reach Claude. "
        "Each question is answered on its own."
    )
    st.caption(f"Lambda `{FUNCTION_NAME}` in {REGION}. Sample help articles written from the console design.")

if mode == "Ask":
    st.header("Ask about the console")
    st.caption("Pick a role on the left, then ask a question or try one of these.")
    history = st.session_state.setdefault("history", [])

    picked = None
    columns = st.columns(2)
    for i, sample in enumerate(SAMPLE_QUESTIONS):
        if columns[i % 2].button(sample, key=f"sample-{i}", width="stretch"):
            picked = sample

    for turn in history:
        with st.chat_message("user"):
            st.markdown(turn["question"])
            st.caption(f"{turn['role']} · {turn['bu']}")
        with st.chat_message("assistant"):
            show_result(turn["result"])

    question = st.chat_input("Ask a question about the console") or picked
    if question:
        with st.chat_message("user"):
            st.markdown(question)
            st.caption(f"{role} · {bu}")
        with st.chat_message("assistant"):
            with st.spinner("Searching the docs…"):
                result = ask(question, role, bu)
            show_result(result)
        history.append({"question": question, "role": role, "bu": bu, "result": result})

else:
    st.header("Compare what each role sees")
    st.caption("Ask one question as a Power User and as an Agency user, side by side.")
    preset = st.selectbox("Demo", list(COMPARE_PRESETS))
    question = st.text_input("Question", value=COMPARE_PRESETS[preset], key=f"compare-question-{preset}")

    if st.button("Run", type="primary", disabled=not question.strip()):
        cases = [(r, bu if r == role else ACTING_AS[r][0]) for r in ROLES]
        with st.spinner(f"Asking {len(cases)} times in parallel…"):
            with ThreadPoolExecutor(len(cases)) as pool:
                results = list(pool.map(lambda case: ask(question.strip(), *case), cases))
        st.session_state.compare = {"question": question.strip(), "cases": cases, "results": results}

    shown = st.session_state.get("compare")
    if shown:
        st.subheader(f"“{shown['question']}”")
        for column, (r, b), result in zip(st.columns(len(shown["cases"])), shown["cases"], shown["results"]):
            with column:
                st.markdown(f"#### {r}")
                st.caption(f"Acting as {b}")
                show_result(result, expand_searches=True)
