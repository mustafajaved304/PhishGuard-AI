def calculate_risk(score):
    """
    Convert a numeric score into a threat level.
    """

    if score >= 80:
        return "Critical"

    elif score >= 60:
        return "High"

    elif score >= 40:
        return "Medium"

    else:
        return "Low"