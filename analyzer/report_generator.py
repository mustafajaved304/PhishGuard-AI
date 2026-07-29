from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from datetime import datetime


def generate_report(result, filename="PhishGuard_Report.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>🛡 PhishGuard AI - Phishing Analysis Report</b>", styles["Title"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(
        f"<b>Generated On:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        styles["BodyText"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(
        f"<b>Risk Score:</b> {result['score']}%",
        styles["BodyText"]
    ))

    story.append(Paragraph(
        f"<b>Threat Level:</b> {result['level']}",
        styles["BodyText"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<b>Detection Reasons</b>", styles["Heading2"]))

    if result["reasons"]:
        for reason in result["reasons"]:
            story.append(Paragraph("• " + reason, styles["BodyText"]))
    else:
        story.append(Paragraph("• No suspicious indicators detected.", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<b>Security Recommendations</b>", styles["Heading2"]))

    recommendations = [
        "Always verify website URLs before clicking.",
        "Enable Multi-Factor Authentication (MFA).",
        "Never share passwords or OTP codes.",
        "Keep your browser and antivirus updated.",
        "Avoid clicking unknown email or SMS links.",
        "Verify the sender before opening attachments."
    ]

    for rec in recommendations:
        story.append(Paragraph("• " + rec, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<b>Developed By:</b> Mustafa Mehmood Javed", styles["BodyText"]))
    story.append(Paragraph("BS Cyber Security Semester Project", styles["BodyText"]))

    doc.build(story)

    return filename