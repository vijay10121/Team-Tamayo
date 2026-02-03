import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Question Filter", page_icon="🤖")
st.title("🤖 Should this question be answered?")

question = st.text_area("Enter a question:")

if st.button("Evaluate"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1"
    )

    system_prompt = """
You are a safety evaluator AI.

For any user question, you must decide ONE of three:

1. ANSWER — if the question is safe and appropriate.
2. ASK — if the question is unclear and needs clarification.
3. REFUSE — if the question is harmful, illegal, or inappropriate.

Reply strictly in this format:

DECISION: <ANSWER / ASK / REFUSE> 
\n RESPONSE: <your response here>
"""

    response = client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )

    output = response.choices[0].message.content
    st.success("Result")
    st.write(output)
