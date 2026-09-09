import csv

dict = [
    {"Name": "Aima", "Age": 19, "Skill": "Python", "hobby": "None"},
    {"Name": "era", "Age": 55, "Skill": "cooking", "hobby": "painting"},
    {"Name": "ellen", "Age": 66, "Skill": "lab", "hobby": "poetry"},
    {"Name": "aqsa", "Age": 45, "Skill": "research", "hobby": "writing"},
    {"Name": "hoorain", "Age": 64, "Skill": "calisthenics", "hobby": "singing"},
    {"Name": "abdullah", "Age": 73, "Skill": "biopython", "hobby": "cooking"},
    {"Name": "yasi", "Age": 26, "Skill": "AI", "hobby": "day-dreaming"}
]
fields = ['Name', 'Age', 'Skill', 'hobby']

with open("Data.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(dict)


