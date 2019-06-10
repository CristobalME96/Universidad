A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[5,8,3],[2,9,4],[6,5,4]]
matriz = []
for i in range(len(A)): #suma de matrices
    fila = []
    for j in range(len(A[0])):
        fila.append(A[i][j] + B[i][j])
    matriz.append(fila)

for fila in matriz:
    print(fila)

print("recorre por filas")
for i in range(len(matriz)): #recorriendo por las filas
    for j in range(len(matriz[0])):
        print("el valor ", matriz[i][j], " esta en la posicion [", i, "][", j, "]")

print("recorre por columnas")
for i in range(len(matriz)): #recorriendo por las columnas
    for j in range(len(matriz[0])):
        print("el valor ", matriz[j][i], " esta en la posicion [", j, "][", i, "]")
