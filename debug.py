import pandas as pd

df = pd.read_csv("data/spam.csv", encoding="latin-1")
print(df.shape)
print(df.columns)
print(df.head())