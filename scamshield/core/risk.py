def calculate_risk(ml_confidence, fake_support_score):
    """
    Combines ML confidence + rule-based score
    to produce final risk level.
    """

    # Normalize fake support score
    # (each keyword/flag adds points, so scale it)
    fs = fake_support_score

    # HIGH RISK CONDITIONS
    if ml_confidence > 0.85 or fs >= 3:
        return "HIGH"

    # MEDIUM RISK CONDITIONS
    elif ml_confidence > 0.6 or fs == 2:
        return "MEDIUM"

    # LOW RISK CONDITIONS
    else:
        return "LOW"