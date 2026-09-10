import csv 

drug_data = [
    {
        "name": "Aspirin",
        "type": "NSAID",
        "dose": 500,
        "activity": 0.8
    },
    {
        "name": "Ibuprofen",
        "type": "NSAID",
        "dose": 400,
        "activity": 0.7
    },
    {
        "name": "Metformin",
        "type": "Antidiabetic",
        "dose": 1000,
        "activity": 0.9
    },
    {
        "name": "Penicillin",
        "type": "Antibiotic",
        "dose": 250,
        "activity": 0.6
    },
    {
        "name": "Imatinib",
        "type": "Anticancer",
        "dose": 400,
        "activity": 0.95
    }
]

fields = ["name","type","dose","activity"]

with open("Drugz.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames = fields, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    csv_writer.writeheader()
    csv_writer.writerows(drug_data)
    print()