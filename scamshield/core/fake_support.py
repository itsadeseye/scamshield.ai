import re

def detect_fake_support(text):
    text = text.lower()

    score = 0
    matched_keywords = []

    strong_keywords = [
        "microsoft support",
        "apple support",
        "windows support",
        "your device is infected",
        "virus detected",
        "unauthorized access"
    ]

    medium_keywords = [
        "security alert",
        "account suspended",
        "verify your account",
        "call support immediately"
    ]

    weak_patterns = [
        r"immediately",
        r"urgent",
        r"within \d+ hours",
        r"act now"
    ]

    # 🔥 Strong indicators (+3)
    for keyword in strong_keywords:
        if keyword in text:
            score += 3
            matched_keywords.append(keyword)

    # ⚠️ Medium indicators (+2)
    for keyword in medium_keywords:
        if keyword in text:
            score += 2
            matched_keywords.append(keyword)

    # ⚠️ Weak indicators (+1)
    for pattern in weak_patterns:
        if re.search(pattern, text):
            score += 1

    # 📞 Phone number detection (+2)
    if re.search(r"\b\d{10,15}\b", text):
        score += 2

    # 🎯 Decision logic (IMPROVED)
    if score >= 4:
        label = "fake_support_scam"
    elif score >= 2:
        label = "suspicious"
    else:
        label = "normal"

    return {
        "label": label,
        "risk_score": score,
        "matched_keywords": matched_keywords
    }