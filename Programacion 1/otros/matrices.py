#A[m][n]
#B[n][p]
#A = [[1,2,3],[4,5,6],[7,8,9]]
#B = [[1,2,3],[-1,-1,-3],[2,2,0]]
m = len(A[0])
n = len(A)
p = len(B)
C = []
for i in range(n): # i indica la columna de B
    C.append([])
    for j in range(n):  # j indica la fila de A
        pos_i = i
        sum = 0
        for k in range(n): #k recorre la fila de A y la columna de B
            sum += A[k][j] * B[i][k]
        C[pos_i].append(sum)
print(C)
