'''
Programa que reciba "n" numeros y los ordene de forma descendente

list() declaracion de una lista, map() aplica una funcion a cada elemtneto, split() divide str en partes
sort() ordena numeros y caracteres, reverse = True valida que sera de manera descendente 
'''

x = list(map(int,input("Ingrese los numeros para ordenar: \n").split()))

x.sort(reverse = True)

print(x)