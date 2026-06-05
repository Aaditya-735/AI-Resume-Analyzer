from parser import extract_resume_text
from ats_engine import calculate_ats_score
from skill_extractor import (
    extract_skills,
    compare_skills
)
from llm_service import analyze_resume
from interview_generator import (
    generate_questions
)

def run_analysis(
    resume_path,
    jd_path
):

    resume_text = extract_resume_text(
        resume_path
    )

    with open(
        jd_path,
        "r",
        encoding="utf-8"
    ) as f:

        jd_text = f.read()

    ats_score = calculate_ats_score(
        resume_text,
        jd_text
    )

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        jd_text
    )

    matched, missing = compare_skills(
        resume_skills,
        jd_skills
    )

    feedback = analyze_resume(
        resume_text,
        jd_text,
        matched,
        missing
    )
    questions = generate_questions(
    resume_text,
    jd_text
)
    

    return {
        "ats_score": ats_score,
        "matched": matched,
        "missing": missing,
        "feedback": feedback,
        "questions": questions
    }





