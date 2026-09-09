import csv

with open('Data.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    fields = next(csv_reader)

    with open('Dict_Data.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=fields)
        csv_writer.writeheader()
        csv_writer.writerows(csv_reader)