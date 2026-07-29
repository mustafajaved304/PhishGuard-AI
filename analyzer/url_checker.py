import re
from urllib.parse import urlparse
from analyzer.risk_engine import calculate_risk


def analyze_url(url):

    score = 0
    reasons = []

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    path = parsed.path.lower()

    # -------------------------
    # HTTPS
    # -------------------------

    if not url.startswith("https://"):
        score += 20
        reasons.append("Website does not use HTTPS.")

    # -------------------------
    # HTTP
    # -------------------------

    if url.startswith("http://"):
        score += 10
        reasons.append("Website uses insecure HTTP protocol.")

    # -------------------------
    # IP Address
    # -------------------------

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 20
        reasons.append("URL contains an IP Address.")

    # -------------------------
    # @ Symbol
    # -------------------------

    if "@" in url:
        score += 15
        reasons.append("Contains '@' symbol.")

    # -------------------------
    # Long URL
    # -------------------------

    if len(url) > 75:
        score += 15
        reasons.append("URL is unusually long.")

    # -------------------------
    # Too Many Dots
    # -------------------------

    if url.count(".") > 3:
        score += 10
        reasons.append("Too many subdomains.")

    # -------------------------
    # Hyphens
    # -------------------------

    if "-" in domain:
        score += 10
        reasons.append("Domain contains hyphens.")

    # -------------------------
    # Digits in Domain
    # -------------------------

    if re.search(r"\d", domain):
        score += 5
        reasons.append("Domain contains numbers.")

    # -------------------------
    # URL Shorteners
    # -------------------------

    shorteners = [
        "bit.ly",
        "tinyurl",
        "goo.gl",
        "ow.ly",
        "is.gd",
        "buff.ly",
        "t.co",
        "rebrand.ly"
    ]

    for short in shorteners:
        if short in domain:
            score += 25
            reasons.append("Shortened URL detected.")

    # -------------------------
    # Suspicious Keywords
    # -------------------------

    keywords = [

        "login",

        "secure",

        "verify",

        "bank",

        "account",

        "update",

        "password",

        "signin",

        "paypal",

        "confirm",

        "wallet",

        "security",

        "billing",

        "recover",

        "reset",

        "invoice",

        "amazon",

        "microsoft",

        "apple",

        "facebook"

    ]

    for word in keywords:

        if word in url.lower():

            score += 8

            reasons.append(f"Suspicious keyword detected: {word}")

    # -------------------------
    # Multiple //
    # -------------------------

    if url.count("//") > 1:
        score += 10
        reasons.append("Multiple '//' detected.")

    # -------------------------
    # Encoded Characters
    # -------------------------

    if "%" in url:
        score += 8
        reasons.append("Encoded characters found.")

    # -------------------------
    # Underscore
    # -------------------------

    if "_" in domain:
        score += 8
        reasons.append("Domain contains underscores.")

    # -------------------------
    # Excessive Path Length
    # -------------------------

    if len(path) > 40:
        score += 8
        reasons.append("Long URL path.")

    # -------------------------
    # Too Many Parameters
    # -------------------------

    if url.count("=") > 3:
        score += 10
        reasons.append("Too many URL parameters.")

    # -------------------------
    # Hexadecimal Values
    # -------------------------

    if re.search(r"%[0-9A-Fa-f]{2}", url):
        score += 10
        reasons.append("Hexadecimal encoding detected.")

    # -------------------------
    # Fake TLDs
    # -------------------------

    fake = [

        ".zip",

        ".review",

        ".country",

        ".click",

        ".work",

        ".gq"

    ]

    for ext in fake:

        if domain.endswith(ext):

            score += 15

            reasons.append(f"Suspicious TLD: {ext}")

    # -------------------------
    # Excessive Slash Count
    # -------------------------

    if url.count("/") > 6:
        score += 5
        reasons.append("Too many '/' characters.")

    # -------------------------
    # Final Score
    # -------------------------

    score = min(score, 100)

    level = calculate_risk(score)

    return {

        "score": score,

        "level": level,

        "reasons": reasons

    }