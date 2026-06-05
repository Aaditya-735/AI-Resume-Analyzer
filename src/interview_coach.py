from llm_service import model

def evaluate_answer(
        question,
        answer):

    prompt = f"""
You are a senior technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate:

1. Technical Accuracy (0-10)
2. Communication (0-10)
3. Completeness (0-10)

Provide:

Overall Score

Strengths

Weaknesses

Suggestions
"""

    response = model.generate_content(
        prompt
    )

    return response.text
