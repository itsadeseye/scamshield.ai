from.preprocess import clean_text
from.fake_support import detect_fake_support
from.risk import calculate_risk
from.explanation import generate_explanation

def analyze_message(model, text):
    cleaned = clean_text(text)

    # ML model
    prediction = model.predict([cleaned])[0]
    probability = model.predict_proba([cleaned]).max()

    # Fake support detection
    fs_result = detect_fake_support(text)

    # Risk level
    risk_level = calculate_risk(probability, fs_result["risk_score"])

    # Explanation engine
    explanation = generate_explanation(text, fs_result, risk_level)

    return {
        "ml_label": str(prediction),
        "confidence": round(float(probability), 2),
        "fake_support_detection": fs_result,
        "risk_level": risk_level,
        "explanation": explanation
    }