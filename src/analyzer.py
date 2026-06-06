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

    

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        jd_text
    )

    matched_skills = list(
    set(resume_skills)
    &
    set(jd_skills)
    )
    missing_skills = list(
    set(jd_skills)
    -
    set(resume_skills)
    )



    ats_score = calculate_ats_score(
        resume_text,
        jd_text,
        matched_skills,
        missing_skills
    )

    feedback = analyze_resume(
        resume_text,
        jd_text,
        matched_skills,
        missing_skills
    )
    questions = generate_questions(
    resume_text,
    jd_text
)
    

    return {
        "ats_score": ats_score,
        "matched": matched_skills,
        "missing": missing_skills,
        "feedback": feedback,
        "questions": questions
    }





