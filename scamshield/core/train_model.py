import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

def train():

    df = pd.read_csv("data/final_dataset.csv")

    X = df["message"]
    y = df["label"]

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    os.makedirs("model", exist_ok=True)

    pickle.dump(model, open("model/model.pkl", "wb"))
    pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

    print("Model trained successfully!")

if __name__ == "__main__":
    train()