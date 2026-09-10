import pandas as pd

df = pd.read_csv("Drugz.csv")
Group_type = df.groupby("type")
for type,data in Group_type:
    print(f"Type of Drug: {type}")
    print(f"Number of {type} drugs found: ",data["name"].count(), "\n",data, "\n")
average = Group_type["activity"].mean()
print("Mean of activity of each type: ", average)
print("Highest activity: ", average.max())
sorting = df.sort_values(by = "activity", ascending=False)
print("Sortation type from highest to lowest activity': \n", sorting)