A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[5,8,3],[2,9,4],[6,5,4]]
matriz = []
for i in range(len(A)):
    fila = []
    for j in range(len(A[0])):
        fila.append(A[i][j] + B[i][j])
    matriz.append(fila)
