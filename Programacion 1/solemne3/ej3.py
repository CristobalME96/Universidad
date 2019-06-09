matriz = [[5,0,0],[0,3,0],["a",0,"b"]]
for fila in matriz:
    print(fila)
for fila in matriz:
    for x in fila:
        if x != 0:
            print(1)
        else:
            print(0)
print(matriz[-1][0])
print(matriz[-2][-2])
