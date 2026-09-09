import csv

with open('Data.csv', 'r') as f:
    csv_reader = csv.reader(f, skipinitialspace=True, quoting=csv.QUOTE_ALL)
    fields = next(csv_reader)
    print(fields)
    for rows in csv_reader:
        print(rows)