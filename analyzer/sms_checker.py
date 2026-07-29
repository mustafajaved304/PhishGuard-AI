from analyzer.risk_engine import calculate_risk


def analyze_sms(text):

    score = 0
    reasons = []

    keywords = [
        "otp",
        "prize",
        "winner",
        "click",
        "verify",
        "urgent",
        "limited offer",
        "claim",
        "gift",
        "bank"
    ]

    for word in keywords:
        if word.lower() in text.lower():
            score += 10
            reasons.append(f"Suspicious keyword: {word}")

    if score > 100:
        score = 100

    return {
        "score": score,
        "level": calculate_risk(score),
        "reasons": reasons
    }