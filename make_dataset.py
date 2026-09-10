import csv

drugs = [
    {"name": "Aspirin",      "molecular_weight": 180, "solubility": 0.8, "toxicity": 0.1, "activity": 0.75},
    {"name": "Ibuprofen",    "molecular_weight": 206, "solubility": 0.6, "toxicity": 0.2, "activity": 0.70},
    {"name": "Metformin",    "molecular_weight": 129, "solubility": 0.9, "toxicity": 0.05,"activity": 0.85},
    {"name": "Penicillin",   "molecular_weight": 334, "solubility": 0.7, "toxicity": 0.1, "activity": 0.90},
    {"name": "Imatinib",     "molecular_weight": 493, "solubility": 0.4, "toxicity": 0.3, "activity": 0.95},
    {"name": "Warfarin",     "molecular_weight": 308, "solubility": 0.5, "toxicity": 0.4, "activity": 0.65},
    {"name": "Oseltamivir",  "molecular_weight": 312, "solubility": 0.8, "toxicity": 0.1, "activity": 0.80},
    {"name": "Remdesivir",   "molecular_weight": 602, "solubility": 0.3, "toxicity": 0.25,"activity": 0.88},
    {"name": "Methotrexate", "molecular_weight": 454, "solubility": 0.6, "toxicity": 0.5, "activity": 0.72},
    {"name": "Chloroquine",  "molecular_weight": 320, "solubility": 0.7, "toxicity": 0.35,"activity": 0.60},
]

fields = ["name", "molecular_weight", "solubility", "toxicity", "activity"]

with open("drugs_dataset.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(drugs)