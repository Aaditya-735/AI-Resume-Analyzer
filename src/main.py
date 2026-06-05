from report_generator import generate_pdf_report
from analyzer import run_analysis
from output_formatter import print_section
results = run_analysis(
    "C:/Users/AG/Documents/Aaditya_Resume(Updated).pdf",
    "data/job_descriptions/ml_engineer.txt"
)



print(type(results["ats_score"]))
print(results["ats_score"])
print_section("ATS SCORE")
print(results["ats_score"])

print_section("MATCHED SKILLS")
print(results["matched"])

print_section("MISSING SKILLS")
print(results["missing"])

print_section("AI FEEDBACK")
print(results["feedback"])

print_section("INTERVIEW QUESTIONS")
print(results["questions"])

generate_pdf_report(results)

