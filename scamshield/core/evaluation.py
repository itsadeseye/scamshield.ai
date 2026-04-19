import pandas as pd
import pickle
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model():

    # Load dataset
    df = pd.read_csv("data/final_dataset.csv")

    X = df["message"]
    y = df["label"]

    # Load model + vectorizer
    model = pickle.load(open("model/model.pkl", "rb"))
    vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

    # Transform text
    X_vec = vectorizer.transform(X)

    # Predict
    preds = model.predict(X_vec)

    # Metrics
    print("=== Classification Report ===")
    print(classification_report(y, preds))

    print("\n=== Confusion Matrix ===")
    print(confusion_matrix(y, preds))


if __name__ == "__main__":
    evaluate_model()