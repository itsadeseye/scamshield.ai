import pandas as pd
import os

def merge_datasets():

    spam = pd.read_csv(os.path.join("data", "spam_clean.csv"))
    sms = pd.read_csv(os.path.join("data", "sms_clean.csv"))

    # Combine both datasets
    final = pd.concat([spam, sms], ignore_index=True)

    # Shuffle (VERY important for ML training)
    final = final.sample(frac=1).reset_index(drop=True)

    output_path = os.path.join("data", "final_dataset.csv")
    final.to_csv(output_path, index=False)

    print("✅ Datasets merged successfully!")
    print(final["label"].value_counts())

if __name__ == "__main__":
    merge_datasets()