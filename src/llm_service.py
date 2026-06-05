import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
import warnings
warnings.filterwarnings("ignore")

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_resume(
        resume_text,
        job_description,
        matched_skills,
        missing_skills):

    prompt = f"""
You are a senior recruiter.

Analyze the candidate.

Resume:
{resume_text}

Job Description:
{job_description}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Provide:

1. Strengths
2. Weaknesses
3. Suggestions
4. Overall Verdict

Keep the response professional.
"""

    response = model.generate_content(
        prompt
    )

    return response.text