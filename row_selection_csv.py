import csv

rows = []

with open('Data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    fields = next(csv_reader)
    print(fields)

# printing rows
    for lines in csv_reader:
        rows.append(lines)

# selecting rows
for row in rows[2:4]:
    print(row)

# to check total number of rows
print(len(rows))
