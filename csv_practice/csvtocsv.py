import pandas as pd

df = pd.read_csv('students.csv')
filter = df[df["Grade"] == 'A']
df2 = filter[["Name","Grade"]]
print(df2.to_csv("Top_students", index=False))

