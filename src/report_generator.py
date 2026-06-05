from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(results, output_file="Resume_Report.pdf"):

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "AI Resume Analysis Report",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>ATS Score:</b> {round(results['ats_score'],2)}%",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            f"<b>Matched Skills:</b><br/>{', '.join(results['matched'])}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            f"<b>Missing Skills:</b><br/>{', '.join(results['missing'])}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "AI Resume Feedback",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            results["feedback"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    content.append(
        Paragraph(
            "Interview Questions",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            results["questions"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(content)

    print(f"\nPDF Report Generated: {output_file}")