import pandas as pd

def clean_sms():
    df = pd.read_csv("data/sms.csv")

    df.columns = ["label", "message"]
    df["label"] = df["label"].str.lower()

    # ensure fake_support label consistency
    df = df[df["label"] == "fake_support"]

    df.to_csv("data/sms_clean.csv", index=False)
    print("sms.csv cleaned")

if __name__ == "__main__":
    clean_sms()