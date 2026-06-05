from parser import extract_resume_text
from ats_engine import calculate_ats_score

resume_text = extract_resume_text(
    "C:/Users/AG/Documents/Aaditya_Resume(Updated).pdf"
)

with open(
    "data/job_descriptions/ml_engineer.txt",
    "r",
    encoding="utf-8"
) as f:

    job_description = f.read()

score = calculate_ats_score(
    resume_text,
    job_description
)

print(f"\nATS Score: {score}%")