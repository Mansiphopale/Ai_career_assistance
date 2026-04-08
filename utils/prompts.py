RESUME_ANALYSIS_PROMPT = """
Analyze this resume and provide:

1. Strengths
2. Weaknesses
3. Suggested Improvements

Resume:
{resume}
"""

JOB_MATCH_PROMPT = """
Compare the resume with the job description.

Provide:
1. Match Percentage
2. Missing Skills
3. Recommendations

Resume:
{resume}

Job Description:
{jd}
"""

CAREER_CHAT_PROMPT = """
Answer this career/interview question professionally:

Question:
{question}
"""