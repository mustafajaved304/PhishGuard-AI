from flask import Flask, render_template, request, send_file
from analyzer.url_checker import analyze_url
from analyzer.email_checker import analyze_email
from analyzer.sms_checker import analyze_sms
from analyzer.report_generator import generate_report

app = Flask(__name__)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# ANALYZER PAGE
# ==========================================

@app.route("/analyzer")
def analyzer():
    return render_template("analyzer.html")


# ==========================================
# ABOUT PAGE
# ==========================================

@app.route("/about")
def about():
    return render_template("about.html")


# ==========================================
# CONTACT PAGE
# ==========================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================================
# ANALYZE INPUT
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():

    analysis_type = request.form.get("type")
    text = request.form.get("text", "").strip()

    if not text:
        return render_template(
            "result.html",
            result={
                "score": 0,
                "level": "Low",
                "reasons": ["No input was provided."]
            },
            input_text=text,
            analysis_type=analysis_type
        )

    if analysis_type == "url":
        result = analyze_url(text)

    elif analysis_type == "email":
        result = analyze_email(text)

    elif analysis_type == "sms":
        result = analyze_sms(text)

    else:
        result = {
            "score": 0,
            "level": "Low",
            "reasons": ["Invalid analysis type selected."]
        }

    return render_template(
        "result.html",
        result=result,
        input_text=text,
        analysis_type=analysis_type
    )


# ==========================================
# DOWNLOAD PDF REPORT
# ==========================================

@app.route("/download_report", methods=["POST"])
def download_report():

    analysis_type = request.form.get("type")
    text = request.form.get("text", "").strip()

    if analysis_type == "url":
        result = analyze_url(text)

    elif analysis_type == "email":
        result = analyze_email(text)

    else:
        result = analyze_sms(text)

    filename = generate_report(result)

    return send_file(
        filename,
        as_attachment=True,
        download_name="PhishGuard_Report.pdf"
    )


# ==========================================
# CUSTOM ERROR PAGES
# ==========================================

@app.errorhandler(404)
def page_not_found(error):
    return "<h2>404 - Page Not Found</h2>", 404


@app.errorhandler(500)
def internal_server_error(error):
    return "<h2>500 - Internal Server Error</h2>", 500


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )