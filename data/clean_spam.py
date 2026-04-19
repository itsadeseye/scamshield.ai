import pandas as pd
import os

def clean_spam():

    # Build safe path to spam.csv
    file_path = os.path.join("data", "spam.csv")

    # Load dataset
    df = pd.read_csv(file_path, encoding="latin-1")

    # Handle Kaggle format (v1, v2)
    if "v1" in df.columns and "v2" in df.columns:
        df = df[["v1", "v2"]]
        df.columns = ["label", "message"]

    # Clean labels
    df["label"] = df["label"].str.lower()

    # Keep only valid labels
    df = df[df["label"].isin(["ham", "spam"])]

    # Save cleaned file
    output_path = os.path.join("data", "spam_clean.csv")
    df.to_csv(output_path, index=False)

    print("✅ spam.csv cleaned successfully!")
    print("Saved to:", output_path)


if __name__ == "__main__":
    clean_spam()