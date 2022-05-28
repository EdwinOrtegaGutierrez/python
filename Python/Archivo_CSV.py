import csv

with open("CSV.csv") as file:
    reader = csv.reader(file)

    for i in reader:
        print("Nombre: {0}, Dinero: {1}".format(i[0], i[1]))