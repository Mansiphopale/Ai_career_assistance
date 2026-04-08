# AI Career Assistant Agent 🤖📄

An offline AI-powered career assistant built using **Ollama**, **Mistral**, and **Streamlit** that helps users:

- Analyze resumes
- Match resumes with job descriptions
- Suggest resume improvements
- Answer career/interview-related questions

---

## 🚀 Features

### 📄 Resume Analysis
Upload your PDF resume and get:
- Strengths
- Weaknesses
- Improvement Suggestions

### 📌 Job Description Matching
Compare your resume with a job description and receive:
- Match Percentage
- Missing Skills
- Recommendations

### 💬 Career Q&A Assistant
Ask career/interview-related questions and get AI-generated answers instantly.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Frontend/UI
- **Ollama** – Local LLM Runtime
- **Mistral / Phi** – Lightweight LLM Models
- **PyPDF** – Resume PDF Parsing

---

## 📂 Project Structure

```bash
ai_agent/
│
├── app.py
├── requirements.txt
│
└── utils/
    ├── __init__.py
    ├── resume_parser.py
    └── prompts.py