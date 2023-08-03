numero = int(input("Ingrese un numero entero: "))
factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i
print(f"El factorial de ese numero resulta: {factorial}")