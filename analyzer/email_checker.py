from analyzer.risk_engine import calculate_risk


def analyze_email(text):

    score = 0
    reasons = []

    suspicious_words = [
        "urgent",
        "verify",
        "password",
        "click",
        "bank",
        "winner",
        "gift",
        "lottery",
        "limited",
        "confirm",
        "account suspended"
    ]

    for word in suspicious_words:
        if word.lower() in text.lower():
            score += 10
            reasons.append(f"Suspicious phrase detected: {word}")

    if score > 100:
        score = 100

    return {
        "score": score,
        "level": calculate_risk(score),
        "reasons": reasons
    }