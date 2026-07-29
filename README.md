# 🛡️ PhishGuard AI

**PhishGuard AI** is a modern phishing detection platform developed using **Python** and **Flask**. It helps users analyze suspicious **URLs, Emails, and SMS messages** using a rule-based phishing detection engine to identify potential cyber threats and provide security recommendations.

---

## 📌 Overview

Phishing remains one of the most common cyber threats. This project demonstrates how rule-based detection techniques can identify suspicious indicators in URLs, emails, and SMS messages, helping users recognize and avoid phishing attacks.

---

## ✨ Features

- 🌐 URL Phishing Analysis
- 📧 Email Phishing Detection
- 📱 SMS Scam Detection
- 📊 Risk Score Calculation
- 🚨 Threat Level Classification
- 📝 Detailed Detection Reasons
- 📄 PDF Report Generation
- 🎨 Modern Cybersecurity User Interface
- ⚡ Fast Rule-Based Analysis
- 🔒 Privacy-Friendly (No Database Required)

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Libraries
- ReportLab
- Jinja2

---

## 📂 Project Structure

```text
PhishGuard-AI/
│
├── analyzer/
│   ├── __init__.py
│   ├── url_checker.py
│   ├── email_checker.py
│   ├── sms_checker.py
│   ├── risk_engine.py
│   └── report_generator.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── analyzer.html
│   ├── result.html
│   ├── about.html
│   ├── contact.html
│   ├── navbar.html
│   └── footer.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/mustafajaved304/PhishGuard-AI.git
```

Open the project:

```bash
cd PhishGuard-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🔍 Detection Modules

### 🌐 URL Analyzer

Checks for phishing indicators such as:

- Suspicious keywords
- IP-based URLs
- URL shorteners
- Excessive subdomains
- Fake login pages
- Missing HTTPS
- Suspicious domain patterns

### 📧 Email Analyzer

Detects:

- Urgent phishing language
- Credential requests
- Fake banking emails
- Spoofing indicators
- Suspicious links
- Social engineering techniques

### 📱 SMS Analyzer

Identifies:

- Fake prize messages
- OTP scams
- Banking fraud
- Account verification scams
- Suspicious shortened links
- Urgent payment requests

---

## 📊 Output

After analysis, the application provides:

- ✅ Risk Score
- ✅ Threat Level
- ✅ Detection Reasons
- ✅ Security Recommendations
- ✅ Downloadable PDF Report

---

## 🎯 Project Objectives

- Improve phishing awareness
- Demonstrate rule-based threat detection
- Provide an easy-to-use cybersecurity tool
- Help users identify suspicious online content
- Promote safer browsing and communication practices

---

## 🚀 Future Improvements

- Machine Learning-based phishing detection
- VirusTotal API integration
- URL reputation services
- Browser extension
- Email attachment scanning
- User authentication
- Threat history dashboard
- Cloud deployment

---

## 👨‍💻 Developer

**Mustafa Mehmood Javed**

**GitHub:** https://github.com/mustafajaved304

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is developed for educational and learning purposes.

© 2026 Mustafa Mehmood Javed. All Rights Reserved.
