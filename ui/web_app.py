import streamlit as st
import pickle
import re

# ---------------- LOAD MODEL ----------------
import pickle
with open("../model.pkl", "rb") as f:
    model = pickle.load(f)
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# ---------------- RISK WORDS ----------------
RISK_WORDS = [
    "microsoft support",
    "apple support",
    "your device is infected",
    "virus detected",
    "call immediately",
    "urgent",
    "act now",
    "account suspended",
    "verify your account"
]

def highlight_text(text):
    for word in RISK_WORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(f"🔴 {word} 🔴", text)
    return text

# ---------------- PREDICT FUNCTION ----------------
def analyze_message(message):

    msg_vec = vectorizer.transform([message])
    prediction = model.predict(msg_vec)[0]

    try:
        confidence = max(model.predict_proba(msg_vec)[0])
    except:
        confidence = 1.0

    if prediction == "spam":
        risk = "HIGH RISK 🚨"
    elif prediction == "fake_support":
        risk = "MEDIUM RISK ⚠️"
    else:
        risk = "LOW RISK ✅"

    return prediction, confidence, risk


# ---------------- UI ----------------
st.set_page_config(page_title="ScamShield AI", page_icon="🧠")

st.title("🧠 Scam & Fake Support Detector AI Framework")
st.write("Enter a message to analyze risk level")

message = st.text_area("Message Input")

if st.button("Analyze"):

    if message.strip() == "":
        st.warning("Please enter a message")
    else:
        label, confidence, risk = analyze_message(message)
        highlighted = highlight_text(message)

        st.subheader("Prediction")
        st.write(label)

        st.subheader("Confidence")
        st.write(round(confidence, 2))

        st.subheader("Risk Level")
        st.write(risk)

        st.subheader("Highlighted Message")
        st.markdown(highlighted)

       