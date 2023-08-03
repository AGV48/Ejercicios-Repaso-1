import random
lista = []
tamaño = int(input("Ingrese el tamaño de la lista: "))
suma = 0
promedio = 0

for i in range (tamaño):
    lista.append(int(input("Ingrese un numero entero: ")))
    suma = suma + lista[i]

promedio = suma / tamaño
print("El promedio es: ", promedio)

