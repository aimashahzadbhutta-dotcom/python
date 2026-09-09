import csv

with open('Data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    fields = next(csv_reader)

    with open('New_Data.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(fields)
    
# there are two method to write rows 
# method 1:
        #csv_writer.writerows(csv_reader)

# method 2:
        #for lines in csv_reader:
            #csv_writer.writerow(lines)

# In method 2, we can select desired number of rows and columns, Following is the example of selection of 1st 3 rows:
        count = 0
        for lines in csv_reader:
            count += 1
            csv_writer.writerow(lines)
            if count == 3:
                break
