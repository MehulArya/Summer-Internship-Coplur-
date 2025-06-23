import csv

data = [["Name", "Address", "Mobile", "Email"],
        ["Mehul", "Durgapura, Jaipur", "9452173950", "mehul@gmai.com"],
        ["Prabhav", "Vishweshpura, Bengaluru", "9876545678", "prabhav@gmail.com"],
        ["Elisa", "West Lafayette, Indiana", "8345678909", "elisa@gmail.com"]
        ]

with open("assignment.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
