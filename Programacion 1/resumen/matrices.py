# creacion de matrices

Matriz = [[1, 2, 3], [4, 5, 6], [6, 7, 8]] # matriz 3x3 con valores definidos

Matriz2 = []    # creando matriz con ciclos
m = 4           # filas
n = 3           # columnas
for i in range(m):  # iteracion en cantidad de filas
    fila = []
    for j in range(n):  # iteracion en cantidad de columnas
        fila.append(i + j)
    Matriz2.append(fila)

print(Matriz)   #impresion lineal
for fila in Matriz2:    #impresion por fila (forma de matriz)
    print(fila)

# operaciones con matrices

Matriz = [[12, 4], [5, -3], [8, 6], [1, 2]] # matriz 4x2
M = len(Matriz)     # cantidad de filas
N = len(Matriz[0])     # cantidad de columnas (o largo de la primera fila)

print("matriz 4x2")
for fila in Matriz:
    print(fila)

print("recorriendo por filas")
for i in range(M):      # filas
    for j in range(N):  # columnas
        print(Matriz[i][j])

print("recorriendo por columnas")
for i in range(N):      # columnas
    for j in range(M):  # filas
        print(Matriz[j][i])

# Diagonales

Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Diagonal Principal")
for i in range(len(Matriz)):    # Diagonal Principal
    for j in range(len(Matriz[0])):
        if i == j:      # El valor es de la diagonal si sus indices son iguales
            print(Matriz[i][j])

print("Diagonal Secundaria")
for i in range(len(Matriz)):    # Diagonal secundaria
      print(Matriz[i][(len(Matriz[0])-1) - i])       # avanza por las filas y retrocede por las columnas
