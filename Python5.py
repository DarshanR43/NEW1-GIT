import csv
with open('C:\Users\admin\Desktop\CSE 2023 1\Computer Problem Solving\NEW1-GIT\contacts.csv', 'r') as F:
    reader = csv.reader(F)
    for row in reader:
        print(row)
    F.close()