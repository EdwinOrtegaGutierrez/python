'''
Programa que lea "n" cadenas y cuente las cadenas repetidas

len() Devuelve la longuitud de un objeto
append() Agrega elementos a una lista
'''
x = list(map(str,input("Ingresa las cadenas: \n").split()))

y = []

#Se crean dos bucles para recorrer cada elemento de la lista
for i in range(len(x)):
    for j in range(len(x)):
        #Se crean dos condiciones para no evaluar la misma posicion
        if i != j:
            if x[i] == x[j] and x[i] not in y:
                y.append(x[i])

print('Cadenas que se repiten: ', y)