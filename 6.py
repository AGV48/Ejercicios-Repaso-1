tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = []
suma = 0
for i in range(tamaño):
    numero = int(input(f"Ingrese un numero: "))
    lista.append(numero)
    suma = suma + numero
print(f"La suma de los numeros de la lista es: {suma}")
