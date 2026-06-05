
from interview_coach import evaluate_answer

question = "Explain Random Forest."

print("=" * 50)
print("INTERVIEW QUESTION")
print("=" * 50)
print(question)

answer = input("\nCandidate: ")

print("\nEvaluating answer...\n")

feedback = evaluate_answer(
    question,
    answer
)

print("\n" + "=" * 50)
print("INTERVIEW FEEDBACK")
print("=" * 50)

print(feedback)