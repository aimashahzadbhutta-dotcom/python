import pandas as pd

df = pd.read_csv("students_new_file.csv")

print("Students with age above 20: \n")
f = df[df["Age"] >= 20]
print(f)

print("\nStudents with grade 'A': \n")
g = df[df["Grade"] == "A"]
print(g)

print("\nTotal number of students: \n\n",len(df))

