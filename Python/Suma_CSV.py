import csv

archivo = "Suma.csv"

total = 0

with open(archivo, "r") as file:
    reader = csv.reader(file, delimiter=",")

    next(reader, None)
    for fila in reader:
        nombre = fila[0]
        dinero = eval(fila[1])
        print(f"Nombre: {nombre}, saldo: {dinero} \n")

        if len(fila[1]) == 5:
            total = total + eval(fila[1][0:6])
        elif len(fila[1]) == 4:
            total = total + eval(fila[1][0:6])
        elif len(fila[1]) == 3:
            total = total + eval(fila[1][0:6])
        elif len(fila[1]) == 2:
            total = total + eval(fila[1][0:6])
        else:
            total = total + eval(fila[1][0:6])

    print("Total: ", str(total))