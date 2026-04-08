import streamlit as st
import ollama

from utils.resume_parser import extract_text_from_pdf
from utils.prompts import *

st.title("AI Career Assistant Agent")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):
        response = ollama.chat(
            model="mistral",
            messages=[
                {
                    "role": "user",
                    "content": RESUME_ANALYSIS_PROMPT.format(
                        resume=resume_text
                    )
                }
            ]
        )

        st.write(response['message']['content'])

st.divider()

jd = st.text_area("Paste Job Description")

if st.button("Match Resume with JD"):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": JOB_MATCH_PROMPT.format(
                    resume=resume_text,
                    jd=jd
                )
            }
        ]
    )

    st.write(response['message']['content'])

st.divider()

question = st.text_input("Ask Career/Interview Question")

if st.button("Ask AI"):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": CAREER_CHAT_PROMPT.format(
                    question=question
                )
            }
        ]
    )

    st.write(response['message']['content'])