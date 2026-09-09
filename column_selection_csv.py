import csv


with open('Data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    fields = next(csv_reader)
    print(fields[0:2])
    for lines in csv_reader:
        print(lines[0:2])

