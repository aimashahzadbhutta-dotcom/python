import pandas as pd

data = {
    "name": ["Aspirin", "Ibuprofen", "Metformin", "Penicillin"],
    "dose": [500, None, 1000, None],
    "activity": [0.8, 0.7, None, 0.6]
}
df = pd.DataFrame(data)

# Finding the number and position of nan values
print("Position of missing values: ")
print(df.isnull())
print("Count of missing values per column: ")
print(df.isnull().sum())
# Filling missing dose values with mean of doses
df["dose"].fillna(df["dose"].mean(),inplace=True)
# Replacing missing activity value with 0
df.iloc[2, 2] = 0
print("Filling missing values: ")
print(df)
# no row is left with missing values otherwise, we would drop(delete) that entire row 