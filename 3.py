import random
Tamaño = int(input("Cuantos numeros aleatorios quiere en la lista?: "))
Lista = []
for i in range(Tamaño):
    Lista.append(random.randint(0,10))
print(Lista)