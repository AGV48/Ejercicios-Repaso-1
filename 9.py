def CrearMatriz(M,F,C):
    import random
    for f in range (F):
        for c in range (C):
            M[f][c] = random.randint(1,10)
            print(M[f][c], end="\t")
        print("\n")
    return

def main():
    matriz = []
    filas = int(input("Ingrese el numero de filas de la matriz: "))
    columnas = int(input("Ingrese el numero de columnas de la matriz: "))
    for i in range(filas):
        matriz.append([0]*columnas)
    print("")
    CrearMatriz(matriz, filas, columnas)
main()