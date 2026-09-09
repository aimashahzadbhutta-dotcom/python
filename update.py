import pandas as pd

df = pd.read_csv("students.csv")
df.iloc[4, 2] = 'C'
print(df)
df.to_csv("students.csv", index=False)
print("updated!")