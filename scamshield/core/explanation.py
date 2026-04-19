def generate_explanation(text, fs_result, risk_level):
    explanations = []

    text_lower = text.lower()

    # 1. Fake support indicators
    if fs_result["label"] == "fake_support_scam":
        explanations.append(
            "The message shows signs of impersonating a technical support team (e.g., Microsoft, Apple)."
        )

    # 2. Urgency patterns
    urgency_words = ["immediately", "urgent", "act now", "within hours"]
    if any(word in text_lower for word in urgency_words):
        explanations.append(
            "It uses urgency language to pressure the user into quick action."
        )

    # 3. Device / infection claims
    if "virus" in text_lower or "infected" in text_lower:
        explanations.append(
            "It claims the device is infected, which is a common scare tactic in scams."
        )

    # 4. Phone number presence
    import re
    if re.search(r"\b\d{10,15}\b", text):
        explanations.append(
            "It contains a phone number, often used to redirect victims to scammers."
        )

    # 5. Risk-based summary
    if risk_level == "HIGH":
        explanations.append(
            "Multiple high-risk indicators were detected, suggesting a strong likelihood of fraud."
        )
    elif risk_level == "MEDIUM":
        explanations.append(
            "Some suspicious patterns were detected, but confirmation is uncertain."
        )
    else:
        explanations.append(
            "No strong scam indicators were found."
        )

    return " ".join(explanations)