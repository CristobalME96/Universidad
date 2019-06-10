#A[m][n]
#B[n][p]
A = [[1,4,7],[2,5,8],[3,6,9]]
B = [[1,-1,2],[2,-1,2],[3,-3,0]]
m = len(A)
n = len(A[0])
p = len(B)
C = []
for i in range(n):
    C.append([])
    for j in range(n):
        pos_i = i
        sum = 0
        for k in range(n):
            sum += A[i][k] * B[k][j]
        C[pos_i].append(sum)
print(C)
