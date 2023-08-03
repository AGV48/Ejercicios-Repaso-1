lista = []
tamaño = int(input("Ingrese el tamaño de la lista: "))
for i in range (tamaño):
    lista.append(int(input("Ingrese un numero: ")))
print(lista)

print("")
print("Lista Invertida")
invertida = list(reversed(lista))
print(invertida)