import pickle

# Load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def predict_message(message):

    msg_vec = vectorizer.transform([message])
    prediction = model.predict(msg_vec)[0]

    # Risk logic
    if prediction == "spam":
        risk = "HIGH RISK 🚨"
    elif prediction == "fake_support":
        risk = "MEDIUM RISK ⚠️"
    else:
        risk = "LOW RISK ✅"

    return prediction, risk


if __name__ == "__main__":
    test = input("Enter message: ")
    label, risk = predict_message(test)

    print("Prediction:", label)
    print("Risk Level:", risk)