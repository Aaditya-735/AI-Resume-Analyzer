SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "docker",
    "aws",
    "git",
    "github",
    "pandas",
    "numpy",
    "opencv",
    "nlp",
    "scikit-learn",
    "power bi"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:

            found_skills.append(skill)

    return list(set(found_skills))

def compare_skills(
        resume_skills,
        jd_skills):

    matched = []

    missing = []

    for skill in jd_skills:

        if skill in resume_skills:

            matched.append(skill)

        else:

            missing.append(skill)

    return matched, missing