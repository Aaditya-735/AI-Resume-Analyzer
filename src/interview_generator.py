from llm_service import model

def generate_questions(
        resume_text,
        job_description):

    prompt = f"""
You are an experienced interviewer.

Based on the resume and job description:

Generate:

1. 5 Technical Questions
2. 5 Resume-Based Questions
3. 5 HR Questions

Format properly.

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = model.generate_content(
        prompt
    )

    return response.text