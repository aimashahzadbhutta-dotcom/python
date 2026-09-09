import pandas as pd

with open("summary.txt", "w") as f:

    df = pd.read_csv("students.csv")

    f.write("Oldest students:")
    filter_old =  df[df["Age"] == df["Age"].max()]
    f.write(filter_old.to_string())
    f.write("\n")

    f.write("Youngest students:")
    filter_young =  df[df["Age"] == df["Age"].min()]
    f.write(filter_young.to_string())
    f.write("\n")

    f.write("Average students:")
    filter_average =  df[df["Age"] == df["Age"].mean()]
    f.write(filter_average.to_string())
    f.write("\n")

    f.write("Count of students with same grades:\n")
    filter_grades = df.groupby("Grade")["Name"].count()
    f.write(filter_grades.to_string())

    
print("File is ready!!")
