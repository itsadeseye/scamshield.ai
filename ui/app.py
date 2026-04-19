import tkinter as tk
import pickle
import re

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model/model.pkl", "rb"))
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
    highlighted = text

    for word in RISK_WORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        highlighted = pattern.sub(f"🔴 {word} 🔴", highlighted)

    return highlighted

# ---------------- PREDICTION LOGIC ----------------
def analyze_message(model, vectorizer, message):

    msg_vec = vectorizer.transform([message])
    prediction = model.predict(msg_vec)[0]

    # confidence (if supported)
    try:
        confidence = max(model.predict_proba(msg_vec)[0])
    except:
        confidence = 1.0

    # risk logic
    if prediction == "spam":
        risk = "HIGH RISK 🚨"
    elif prediction == "fake_support":
        risk = "MEDIUM RISK ⚠️"
    else:
        risk = "LOW RISK ✅"

    return {
        "ml_label": prediction,
        "confidence": round(confidence, 2),
        "risk_level": risk,
        "explanation": "AI-based classification using trained model"
    }

# ---------------- THEME COLORS ----------------
PINK_BG = "#F7D6E0"
BROWN = "#7B4F3B"
WHITE = "#FFFFFF"
LIGHT_PANEL = "#FFF7FA"

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Scam & Fake Support Detector")
root.geometry("650x550")
root.configure(bg=PINK_BG)

# ---------------- HEADER ----------------
header = tk.Label(
    root,
    text="AI Scam & Fake Support Detector",
    bg=PINK_BG,
    fg=BROWN,
    font=("Arial", 18, "bold")
)
header.pack(pady=15)

# ---------------- INPUT FRAME ----------------
frame = tk.Frame(root, bg=LIGHT_PANEL, padx=10, pady=10)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Message:", bg=LIGHT_PANEL, fg=BROWN, font=("Arial", 12))
label.pack(anchor="w")

text_box = tk.Text(frame, height=8, width=60, bg=WHITE, fg="black")
text_box.pack()

# ---------------- RESULT BOX ----------------
result_label = tk.Label(
    root,
    text="",
    bg=PINK_BG,
    fg=BROWN,
    font=("Arial", 11),
    wraplength=550,
    justify="left"
)
result_label.pack(pady=20)

# ---------------- FUNCTION ----------------
def analyze():

    message = text_box.get("1.0", tk.END).strip()

    if not message:
        result_label.config(text="Please enter a message.")
        return

    result = analyze_message(model, vectorizer, message)

    highlighted_message = highlight_text(message)

    output = f"""
ML Prediction: {result['ml_label']}
Confidence: {result['confidence']}
Risk Level: {result['risk_level']}

🔍 Highlighted Message:
{highlighted_message}

Explanation:
{result['explanation']}
"""

    result_label.config(text=output)

# ---------------- BUTTON ----------------
button = tk.Button(
    root,
    text="Analyze Message",
    command=analyze,
    bg=BROWN,
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
button.pack(pady=10)

# ---------------- RUN ----------------
root.mainloop()