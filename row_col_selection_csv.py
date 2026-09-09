import csv

rows = []

with open('Data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    fields = next(csv_reader)
# Selecting 1st 3 columns only
    print(fields[:3])
    for lines in csv_reader:
        rows.append(lines)

# selecting last 3 rows only
for row in rows[4:]:
    print(row[:3])