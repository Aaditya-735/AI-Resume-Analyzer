from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_ats_score(
    resume_text,
    job_description,
    matched_skills,
    missing_skills
):
    
    # Semantic similarity score
    resume_embedding = model.encode([resume_text])
    jd_embedding = model.encode([job_description])

    similarity_score = (
        cosine_similarity(
            resume_embedding,
            jd_embedding
        )[0][0]
        * 100
    )

    # Skill match score
    total_skills = len(matched_skills) + len(missing_skills)

    if total_skills == 0:
        skill_score = 0
    else:
        skill_score = (
            len(matched_skills)
            / total_skills
        ) * 100

    # Final ATS Score
    ats_score = (
        similarity_score * 0.6
        +
        skill_score * 0.4
    )

    return round(float(ats_score), 2)