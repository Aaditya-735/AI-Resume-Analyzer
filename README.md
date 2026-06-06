# AI Resume Analyzer & Interview Coach

An AI-powered Resume Analyzer and Interview Preparation Assistant built using Python, NLP, Sentence Transformers, and Google Gemini AI.

The system analyzes a candidate's resume against a target job description, calculates an ATS score, identifies matching and missing skills, generates professional AI feedback, and helps candidates prepare for interviews.

---

## Features

### Resume Analysis
- Extracts text from PDF resumes
- Parses candidate information
- Identifies technical skills

### ATS Scoring Engine
- Semantic similarity scoring using Sentence Transformers
- Compares resume content with job descriptions
- Generates ATS compatibility score

### Skill Gap Analysis
- Detects matched skills
- Detects missing skills
- Highlights improvement areas

### AI Resume Feedback
Powered by Google Gemini AI

Provides:
- Strengths
- Weaknesses
- Suggestions
- Overall Verdict

### AI Interview Coach
Powered by Google Gemini AI

Generates:
- Interview Questions
- Candidate Evaluation
- Performance Feedback

### PDF Report Generator
Creates professional reports containing:
- ATS Score
- Matched Skills
- Missing Skills
- AI Feedback

---

## Architecture
```text
Resume PDF
    ↓
Resume Parser
    ↓
Skill Extraction
    ↓
ATS Engine
    ↓
Gemini AI Feedback
    ↓
PDF Report Generation

---

## Project Structure

```text
AI-Resume-Analyzer/
│
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── src/
│   ├── parser.py
│   ├── skill_extractor.py
│   ├── ats_engine.py
│   ├── analyzer.py
│   ├── llm_service.py
│   ├── interview_generator.py
│   ├── interview_coach.py
│   ├── report_generator.py
│   ├── output_formatter.py
│   └── main.py
│
├── tests/
│   └── test_interview_coach.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Technologies Used

- Python
- Google Gemini API
- Sentence Transformers
- Scikit-Learn
- PyPDF2
- ReportLab
- NLP Techniques

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Aaditya-735/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from:

https://aistudio.google.com

---

## Run Resume Analysis

```bash
python src/main.py
```

---

## Sample Output

### ATS Score

```text
ATS Score: 60.87%
```

### Matched Skills

```text
Python
Machine Learning
SQL
Deep Learning
Git
```

### Missing Skills

```text
Docker
TensorFlow
```

### AI Feedback

```text
Strengths
Weaknesses
Suggestions
Overall Verdict
```

---

## Future Improvements

- Streamlit Web Application
- Resume Ranking System
- Multi-Resume Comparison
- Interview Voice Bot
- Resume Recommendation Engine
- Job Recommendation System

---

## Author

Aaditya Gupta

B.Tech Computer Science Student

Machine Learning | Generative AI | AI Agents

GitHub:
https://github.com/Aaditya-735

---

## License

MIT License