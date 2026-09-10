import pandas as pd
import csv

df = pd.read_csv("drugs_dataset.csv")
print("Basic statistics of numeric values: \n", df.describe())
print("Drugs with toxicity less than 0.3: \n", df[df["toxicity"] < 0.3][["name","toxicity"]])
print("Sorted Drug data with respect to descending activity values: \n", df.sort_values(by= "activity", ascending=False))
print("\nDrug with minimun toxicity: ")
print(df[df["toxicity"] == df["toxicity"].min()][["name","toxicity"]])
print("\nDrug with maximum activity: ")
print(df[df["activity"] == df["activity"].max()][["name","activity"]])
first5 = df.head()
first5.to_csv("top_drugs.csv")
print(first5)