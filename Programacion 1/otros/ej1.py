#volver T ya creado en una listas

D = {}

def agregar(D, N, T):
    D.update({N:T})
    return D

def buscar_num(D, N):
    numero = D.get(N)
    return numero

def mas_numeros(D, N, T):
    D[N] = D[N]
    for i in range(len(T)):
        D[N].append(T[i])
    return D
opcion = 0
while True:
    opcion = int(input())
    if opcion == 1:
        N = input()
        T = int(input())
        D = agregar(D, N, T)
    if opcion == 2:
        N = input()
        print(buscar_num(D, N))
    if opcion == 3:
        T = []
        T.append(int(input()))
        N = input()
        D = mas_numeros(D, N, T)
