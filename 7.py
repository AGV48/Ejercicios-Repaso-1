lista = []
tamaño = int(input("Ingrese el tamaño de la lista: "))
grande = 0
pequeño = 100

for i in range(tamaño):
    lista.append(int(input(f"Ingrese un número: ")))
print(lista)

print("")

for i in range(len(lista)):
    if grande < lista[i]:
        grande = lista[i]
print(f"El número más grande de la lista es: {grande}")

for i in range(len(lista)):
    if pequeño > lista[i]:
        pequeño = lista[i]
print(f"El número más pequeño de la lista es: {pequeño}")