#El programa detecta Cadenas de texto palíndromas muy especificas
#un ejemplo de texto palíndromo es "alli ves sevilla", pero escrita de esta forma: "alli ves sev illa"
igual = 0 
aux = 0
texto = input("Ingrese la cadena de texto que desea evaluar: ")

for i in reversed(range(0, len(texto))):
  if texto[i].lower() == texto[aux].lower():
    igual += 1
  aux += 1

if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")