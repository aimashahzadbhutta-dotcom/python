import csv

rows = []

with open('Data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    fields = next(csv_reader)
    for lines in csv_reader:
        rows.append(lines)
    
with open('New_Data_2.csv', 'w') as f:
    csv_writer = csv.writer(f)
#instead of giving fields as argument, we will just give particular column names in [] as a single arguement
#writerow() takes only one arguement 
    csv_writer.writerow(['Name', 'hobby'])
#row selection
    for row in rows[4:7]:
#column selection, we use [row[], row[], row[]] as a single arguement
        csv_writer.writerow([row[0], row[2]])
